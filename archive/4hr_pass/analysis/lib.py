"""Reusable statistical helpers for the GivingTuesday AI Readiness analysis.

Functions return structured results (dataclasses), never bare p-values.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence

import numpy as np
import pandas as pd
from scipy import stats

DATA_DIR = Path(__file__).resolve().parent.parent / "ai_readiness_survey_results" / "ai_exports"
RAW_PARQUET = DATA_DIR / "ai_survey_results_2024_n=930.parquet"
NORMALIZED_PARQUET = DATA_DIR / "ai_survey_normalized_clustering_data.parquet"

DEFAULT_SUBGROUPS = ["ref", "global_north_south", "org_size", "role", "continent", "cluster3"]

CLUSTER3_LABEL = {-1: "AI Skeptics", 0: "Late Adopters", 1: "AI Consumers"}

U_TASKS = ["Ask", "Assist", "Generat", "Interpret", "Organi", "Predict", "Translat"]
W_TASKS = U_TASKS  # same vocab pairs across [U]/[W]

DATA_INFRA_BINARY = [
    "tech_person",
    "merl_person",
    "cloud_storage",
    "data_use_policy",
    "org_agreements",
]
DATA_KIND_PREFIX = "[D] "


def load_raw() -> pd.DataFrame:
    """Load raw n=930 survey responses."""
    return pd.read_parquet(RAW_PARQUET)


def load_normalized() -> pd.DataFrame:
    """Load 0-1 normalized + one-hot expanded clustering dataset."""
    return pd.read_parquet(NORMALIZED_PARQUET)


def load_joined() -> pd.DataFrame:
    """Load both files joined on row order. Normalized columns get an `n_` prefix
    where they collide with raw column names."""
    raw = load_raw().reset_index(drop=True)
    norm = load_normalized().reset_index(drop=True)
    overlap = set(raw.columns) & set(norm.columns)
    norm = norm.rename(columns={c: f"n_{c}" for c in overlap})
    return pd.concat([raw, norm], axis=1)


def parse_jsonbytes(value: Any) -> list[str]:
    """Parse the bytes-JSON-array fields (`org_label`, `ai_use`, `ai_want`, etc.).

    Returns [] for missing values. Strips trailing empty strings.
    """
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return []
    if isinstance(value, bytes):
        value = value.decode("utf-8", errors="ignore")
    if isinstance(value, str):
        try:
            arr = json.loads(value)
        except json.JSONDecodeError:
            return []
        return [s for s in arr if isinstance(s, str) and s.strip()]
    if isinstance(value, list):
        return [s for s in value if isinstance(s, str) and s.strip()]
    return []


def expand_multiselect(series: pd.Series, prefix: str = "") -> pd.DataFrame:
    """One-hot expand a bytes-JSON multi-select column. Each unique option becomes
    a 0/1 column. NaNs in the original become rows of all zeros."""
    parsed = series.apply(parse_jsonbytes)
    options = sorted({opt for row in parsed for opt in row})
    out = pd.DataFrame(
        {f"{prefix}{opt}": parsed.apply(lambda r, o=opt: int(o in r)) for opt in options},
        index=series.index,
    )
    return out


# --- Group description ---------------------------------------------------------


@dataclass
class GroupDescription:
    group_col: str
    n_per_group: dict[Any, int]
    means: pd.DataFrame
    missingness: pd.DataFrame


def describe_group(df: pd.DataFrame, group_col: str, cols: Sequence[str] | None = None) -> GroupDescription:
    """Per-group n, means, and missingness for every numeric column (or `cols`)."""
    if cols is None:
        cols = df.select_dtypes(include="number").columns.tolist()
        if group_col in cols:
            cols = [c for c in cols if c != group_col]
    grouped = df.groupby(group_col, dropna=False)
    n_per_group = grouped.size().to_dict()
    means = grouped[cols].mean()
    missingness = grouped[cols].apply(lambda g: g.isna().mean())
    return GroupDescription(group_col, n_per_group, means, missingness)


# --- Compare two/many groups ---------------------------------------------------


@dataclass
class ComparisonResult:
    outcome: str
    group_col: str
    method: str
    effect_size: float | None
    effect_size_name: str
    ci: tuple[float, float] | None
    p_value: float | None
    n_per_group: dict[Any, int]
    extra: dict[str, Any] = field(default_factory=dict)
    notes: str = ""

    def as_row(self) -> dict[str, Any]:
        lo, hi = (self.ci if self.ci is not None else (np.nan, np.nan))
        return {
            "outcome": self.outcome,
            "group_col": self.group_col,
            "method": self.method,
            "effect_size_name": self.effect_size_name,
            "effect_size": self.effect_size,
            "ci_lo": lo,
            "ci_hi": hi,
            "p_value": self.p_value,
            "n_total": sum(self.n_per_group.values()) if self.n_per_group else None,
            "n_groups": len(self.n_per_group),
            **{f"n_{k}": v for k, v in self.n_per_group.items()},
        }


def _is_binary_numeric(s: pd.Series) -> bool:
    vals = set(pd.unique(s.dropna()))
    return vals.issubset({0, 1}) or vals.issubset({0.0, 1.0})


def compare_groups(
    df: pd.DataFrame,
    outcome: str,
    group_col: str,
    method: str = "auto",
    drop_groups: Iterable[Any] = (),
) -> ComparisonResult:
    """Compare an outcome across groups.

    Auto-picks:
      - binary outcome × any group → χ² (or Fisher 2×2 if any cell <5)
      - continuous outcome × 2 groups → Mann-Whitney + r effect size
      - continuous outcome × ≥3 groups → Kruskal-Wallis + epsilon-squared
      - categorical (>2 levels) outcome × group → χ² with Cramér's V
    """
    sub = df[[outcome, group_col]].dropna()
    if drop_groups:
        sub = sub[~sub[group_col].isin(list(drop_groups))]

    n_per_group = sub.groupby(group_col).size().to_dict()
    if sub.empty or len(n_per_group) < 2:
        return ComparisonResult(outcome, group_col, "skip", None, "", None, None, n_per_group, notes="insufficient data")

    y = sub[outcome]
    g = sub[group_col]

    # Categorical or binary outcome → contingency table
    if y.dtype == object or y.dtype.name == "category" or _is_binary_numeric(y):
        ct = pd.crosstab(y, g)
        chi2, p, dof, expected = stats.chi2_contingency(ct)
        n = ct.values.sum()
        cramers_v = float(np.sqrt(chi2 / (n * (min(ct.shape) - 1)))) if min(ct.shape) > 1 else None
        # Fisher exact for 2×2 with small expected cells
        if ct.shape == (2, 2) and expected.min() < 5:
            try:
                _, p_fisher = stats.fisher_exact(ct)
                p = p_fisher
                method_used = "fisher_2x2"
            except Exception:
                method_used = "chi2"
        else:
            method_used = "chi2"
        # Risk ratio for 2×2 binary outcome with 2 groups
        extra = {"contingency": ct.to_dict()}
        rr = None
        if ct.shape == (2, 2):
            a, b = ct.iloc[1, 0], ct.iloc[1, 1]
            n0, n1 = ct.iloc[:, 0].sum(), ct.iloc[:, 1].sum()
            if n0 and n1 and a / n0 > 0:
                rr = float((b / n1) / (a / n0))
            extra["risk_ratio"] = rr
        return ComparisonResult(
            outcome, group_col, method_used, cramers_v, "cramers_v", None, float(p), n_per_group, extra=extra
        )

    # Continuous outcome
    groups_list = [y[g == lvl].values for lvl in sorted(g.unique())]
    if len(groups_list) == 2:
        u, p = stats.mannwhitneyu(groups_list[0], groups_list[1], alternative="two-sided")
        n0, n1 = len(groups_list[0]), len(groups_list[1])
        z = stats.norm.isf(p / 2) * (1 if u > n0 * n1 / 2 else -1)
        r = float(z / np.sqrt(n0 + n1))
        # bootstrap CI on difference of means as an interpretable effect
        diff = float(np.mean(groups_list[1]) - np.mean(groups_list[0]))
        ci = bootstrap_diff_ci(groups_list[0], groups_list[1])
        return ComparisonResult(
            outcome, group_col, "mann_whitney", diff, "mean_diff", ci, float(p), n_per_group,
            extra={"rank_biserial_r": r}
        )
    h, p = stats.kruskal(*groups_list)
    n = sum(len(x) for x in groups_list)
    eps2 = float((h - len(groups_list) + 1) / (n - len(groups_list)))
    return ComparisonResult(
        outcome, group_col, "kruskal", eps2, "epsilon_sq", None, float(p), n_per_group
    )


def bootstrap_diff_ci(a: np.ndarray, b: np.ndarray, n: int = 2000, alpha: float = 0.05, seed: int = 0) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    a = np.asarray(a); b = np.asarray(b)
    boot = np.empty(n)
    for i in range(n):
        sa = rng.choice(a, size=len(a), replace=True)
        sb = rng.choice(b, size=len(b), replace=True)
        boot[i] = sb.mean() - sa.mean()
    return float(np.quantile(boot, alpha / 2)), float(np.quantile(boot, 1 - alpha / 2))


# --- Use-vs-Want gap ----------------------------------------------------------


@dataclass
class GapResult:
    task: str
    pct_use: float
    pct_want: float
    gap: float
    n: int
    by_subgroup: dict[str, pd.DataFrame] = field(default_factory=dict)


def gap_analysis(
    df: pd.DataFrame,
    tasks: Iterable[str] = U_TASKS,
    subgroups: Iterable[str] = ("ref", "global_north_south", "cluster3", "org_size", "role"),
) -> list[GapResult]:
    """Per-task aspiration gap (% want − % use), overall and by subgroup.

    `df` must contain `[U] {task}` and `[W] {task}` columns (e.g. the normalized parquet).
    """
    results: list[GapResult] = []
    for task in tasks:
        u_col, w_col = f"[U] {task}", f"[W] {task}"
        if u_col not in df.columns or w_col not in df.columns:
            continue
        u, w = df[u_col].mean(), df[w_col].mean()
        by_subgroup: dict[str, pd.DataFrame] = {}
        for sg in subgroups:
            if sg not in df.columns:
                continue
            grp = df.groupby(sg, dropna=False)
            tab = pd.DataFrame(
                {
                    "n": grp.size(),
                    "pct_use": grp[u_col].mean(),
                    "pct_want": grp[w_col].mean(),
                }
            )
            tab["gap"] = tab["pct_want"] - tab["pct_use"]
            by_subgroup[sg] = tab
        results.append(GapResult(task, float(u), float(w), float(w - u), len(df), by_subgroup))
    return results


# --- Subgroup sweep -----------------------------------------------------------


def subgroup_sweep(
    df: pd.DataFrame,
    outcome: str,
    primary_group: str,
    by: Iterable[str] = DEFAULT_SUBGROUPS,
    drop_groups: Iterable[Any] = (),
) -> pd.DataFrame:
    """Run the same comparison across every level of every subgroup column.

    For each `sg` in `by`, splits `df` by `sg` and runs `compare_groups(outcome, primary_group)`
    within each stratum. Returns a wide DataFrame; flags strata where effect direction
    flips relative to the overall comparison.
    """
    rows: list[dict[str, Any]] = []
    overall = compare_groups(df, outcome, primary_group, drop_groups=drop_groups)
    overall_row = overall.as_row()
    overall_row.update({"stratum_col": "ALL", "stratum": "ALL"})
    rows.append(overall_row)
    sign_overall = np.sign(overall.effect_size) if overall.effect_size is not None else 0
    for sg in by:
        if sg not in df.columns or sg == primary_group:
            continue
        for level, sub in df.groupby(sg, dropna=False):
            if len(sub) < 30 or sub[primary_group].nunique() < 2:
                continue
            res = compare_groups(sub, outcome, primary_group, drop_groups=drop_groups)
            row = res.as_row()
            row.update({"stratum_col": sg, "stratum": level})
            row["flag_sign_flip"] = bool(
                res.effect_size is not None and sign_overall != 0 and np.sign(res.effect_size) != sign_overall
            )
            rows.append(row)
    out = pd.DataFrame(rows)
    if "p_value" in out.columns:
        ps = out["p_value"].fillna(1.0).values
        out["p_fdr"] = fdr_adjust(ps)
    return out


# --- Bootstrap & FDR ----------------------------------------------------------


def bootstrap_ci(
    stat_fn: Callable[[pd.DataFrame], float],
    df: pd.DataFrame,
    n: int = 2000,
    alpha: float = 0.05,
    seed: int = 0,
) -> tuple[float, float, float]:
    """Bootstrap CI for any scalar statistic. Returns (estimate, lo, hi)."""
    rng = np.random.default_rng(seed)
    estimate = stat_fn(df)
    boot = np.empty(n)
    idx = np.arange(len(df))
    for i in range(n):
        sample = df.iloc[rng.choice(idx, size=len(df), replace=True)]
        boot[i] = stat_fn(sample)
    return float(estimate), float(np.quantile(boot, alpha / 2)), float(np.quantile(boot, 1 - alpha / 2))


def fdr_adjust(p_values: Iterable[float], alpha: float = 0.05) -> np.ndarray:
    """Benjamini-Hochberg FDR-adjusted p-values."""
    p = np.asarray(list(p_values), dtype=float)
    n = len(p)
    if n == 0:
        return p
    order = np.argsort(p)
    ranked = p[order]
    adj = ranked * n / (np.arange(n) + 1)
    adj = np.minimum.accumulate(adj[::-1])[::-1]
    out = np.empty(n)
    out[order] = np.clip(adj, 0, 1)
    return out


# --- Convenience: data readiness index ----------------------------------------


def data_readiness_score(df: pd.DataFrame) -> pd.Series:
    """A simple additive index over data-infra signals. Range 0–1.

    Components: tech_person, merl_person, cloud_storage, data_use_policy,
    org_agreements (binary 0/1) plus the 5 [D] columns from the normalized parquet
    if present. Missing entries are imputed at 0.
    """
    cols = list(DATA_INFRA_BINARY)
    cols += [c for c in df.columns if c.startswith(DATA_KIND_PREFIX)]
    cols = [c for c in cols if c in df.columns]
    if not cols:
        return pd.Series(np.nan, index=df.index)
    sub = df[cols].fillna(0).astype(float)
    return sub.mean(axis=1)


def ai_use_count(df: pd.DataFrame) -> pd.Series:
    cols = [c for c in df.columns if c.startswith("[U] ") and "not currently" not in c.lower() and "Other" not in c]
    return df[cols].fillna(0).sum(axis=1)


def ai_want_count(df: pd.DataFrame) -> pd.Series:
    cols = [c for c in df.columns if c.startswith("[W] ") and "don't know" not in c.lower() and "Other" not in c]
    return df[cols].fillna(0).sum(axis=1)
