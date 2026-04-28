"""Phase 5 method stack — field-standard models on top of the descriptive
helpers in `lib.py`.

Each helper:
- Has a docstring with the canonical reference.
- Returns a structured dataclass (never bare numbers).
- Degrades gracefully if its optional dependency is missing — the import is
  lazy inside the helper, with a clear error message.
- Has a small unit test under `analysis/tests/`.

Library refs:
- LCA: Vermunt & Magidson (2002) "Latent class cluster analysis"; Collins & Lanza (2010).
- IRT (2PL/GRM): Birnbaum (1968); Samejima (1969); Embretson & Reise (2000).
- SEM: Bollen (1989); Kline (2015).
- Oaxaca–Blinder: Oaxaca (1973); Blinder (1973); Jann (2008) Stata oaxaca.
- Multilevel: Gelman & Hill (2007); Snijders & Bosker (2012).
- IPW / raking: Deville & Särndal (1992); Mercer/Lau/Kennedy (Pew, 2018).
- Mediation sensitivity: Imai et al. (2010); DoWhy `refute_estimate`.
- BERTopic: Grootendorst (2022) arXiv:2203.05794; Reimers & Gurevych (2019)
  Sentence-BERT.
- MCA + Louvain: Le Roux & Rouanet (2010); Blondel et al. (2008).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable, Sequence

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Helper: ensure a column has been NORM-imputed -> NaN-restored before fitting
# binary-only methods. The normalized parquet imputes NaNs with column means;
# every "binary" in NORM may have a third non-{0,1} value.
# ---------------------------------------------------------------------------


def restore_nan(df: pd.DataFrame, cols: Iterable[str]) -> pd.DataFrame:
    """For each col in `cols`, set values not in {0, 1} (or {0.0, 1.0}) to NaN.
    Use this on NORM-derived columns before LCA / IRT.
    """
    out = df.copy()
    for c in cols:
        if c not in out.columns:
            continue
        s = out[c]
        mask_valid = s.isin([0, 1]) | s.isin([0.0, 1.0])
        out.loc[~mask_valid, c] = np.nan
    return out


# ===========================================================================
# 1) Latent Class Analysis (LCA) via stepmix
# ===========================================================================


@dataclass
class LCAResult:
    k_range: list[int]
    fit_table: pd.DataFrame  # k, n_params, ll, aic, bic, entropy, n_per_class
    best_k: int
    posteriors: pd.DataFrame  # rows = respondents, cols = class probs at best_k
    item_response_probs: pd.DataFrame  # P(item=1 | class) at best_k
    hard_assignments: pd.Series
    notes: str = ""


def latent_class_model(
    df: pd.DataFrame,
    items: Sequence[str],
    k_range: Sequence[int] = (2, 3, 4, 5, 6),
    n_init: int = 5,
    random_state: int = 0,
    measurement: str = "binary",
) -> LCAResult:
    """Fit LCA via `stepmix` for k in `k_range`. Returns BIC/AIC/entropy table,
    best-k posteriors and item-response probabilities.

    `measurement = "binary"` for 0/1 indicators; switch to "categorical" or
    "continuous" if needed.

    Reference: Vermunt & Magidson (2002), `stepmix` Morin et al. (2023) JOSS.
    """
    try:
        from stepmix.stepmix import StepMix
    except ImportError as e:
        raise RuntimeError("stepmix not installed. `pip install stepmix`") from e

    sub = df[list(items)].dropna()
    if len(sub) < 50:
        raise ValueError(f"Too few complete rows for LCA: {len(sub)}")
    X = sub.astype(int).values

    rows = []
    fits = {}
    for k in k_range:
        model = StepMix(
            n_components=k,
            measurement=measurement,
            n_init=n_init,
            random_state=random_state,
            progress_bar=False,
        )
        model.fit(X)
        ll = model.score(X) * len(X)  # avg loglik * n
        # parameter count: k-1 class probs + k * len(items) item probs (binary)
        n_params = (k - 1) + k * len(items)
        aic = -2 * ll + 2 * n_params
        bic = -2 * ll + n_params * np.log(len(X))
        # entropy (relative entropy R^2)
        post = model.predict_proba(X)
        eps = 1e-12
        ent = -np.sum(post * np.log(post + eps)) / (len(X) * np.log(k))
        rel_ent = 1 - ent  # higher = cleaner separation
        hard = post.argmax(axis=1)
        sizes = pd.Series(hard).value_counts().sort_index().to_dict()
        rows.append({
            "k": k, "n_params": n_params, "ll": ll, "aic": aic, "bic": bic,
            "entropy_R2": rel_ent, "n_per_class": sizes,
        })
        fits[k] = (model, post, hard)
    fit_df = pd.DataFrame(rows).set_index("k")
    best_k = int(fit_df["bic"].idxmin())
    model, post, hard = fits[best_k]
    posteriors = pd.DataFrame(post, index=sub.index, columns=[f"p_class_{i}" for i in range(best_k)])
    # item-response probs: stepmix .get_parameters_df()
    try:
        irp = model.get_parameters_df()
        # restrict to binary "p" rows
        if "model_name" in irp.index.names:
            irp = irp.xs("binary", level="model_name", drop_level=False)
    except Exception:
        # fallback: compute manually
        item_probs = []
        for c in range(best_k):
            mask = hard == c
            item_probs.append(sub.iloc[mask].mean())
        irp = pd.DataFrame(item_probs, index=[f"class_{i}" for i in range(best_k)]).T
    return LCAResult(
        k_range=list(k_range), fit_table=fit_df, best_k=best_k,
        posteriors=posteriors, item_response_probs=irp,
        hard_assignments=pd.Series(hard, index=sub.index, name="lca_class"),
        notes=f"stepmix StepMix(measurement={measurement}); BIC selected k={best_k}",
    )


# ===========================================================================
# 2) IRT — 2PL / Graded Response via girth
# ===========================================================================


@dataclass
class IRTResult:
    items: list[str]
    discrimination: pd.Series
    difficulty: pd.DataFrame  # for 2PL: 1 col; for GRM: T-1 cols
    person_scores: pd.Series
    model: str
    n: int
    notes: str = ""


def irt_score(
    df: pd.DataFrame,
    items: Sequence[str],
    model: str = "2pl",
) -> IRTResult:
    """Fit a 2-PL (binary) or graded-response (ordinal) IRT model via `girth`.

    Returns discrimination + difficulty parameters per item, EAP person scores.

    Reference: Birnbaum (1968) for 2PL; Samejima (1969) for GRM; girth library.
    """
    try:
        from girth import twopl_mml, grm_mml, ability_eap
    except ImportError as e:
        raise RuntimeError("girth not installed. `pip install girth`") from e

    sub = df[list(items)].dropna()
    n = len(sub)
    if n < 50:
        raise ValueError(f"Too few complete rows for IRT: {n}")

    if model == "2pl":
        X = sub.astype(int).values.T  # girth wants items × persons
        # girth expects 0/1
        result = twopl_mml(X)
        discrimination = pd.Series(result["Discrimination"], index=items, name="alpha")
        difficulty = pd.DataFrame({"b": result["Difficulty"]}, index=items)
        try:
            theta = ability_eap(X, result["Difficulty"], result["Discrimination"])
        except Exception:
            theta = np.full(n, np.nan)
        scores = pd.Series(theta, index=sub.index, name="irt_theta")
        return IRTResult(list(items), discrimination, difficulty, scores, "2pl", n)
    elif model == "grm":
        X = sub.astype(int).values.T
        result = grm_mml(X)
        discrimination = pd.Series(result["Discrimination"], index=items, name="alpha")
        difficulty = pd.DataFrame(result["Difficulty"], index=items)
        difficulty.columns = [f"b_{i}" for i in range(difficulty.shape[1])]
        try:
            theta = ability_eap(X, result["Difficulty"], result["Discrimination"])
        except Exception:
            theta = np.full(n, np.nan)
        scores = pd.Series(theta, index=sub.index, name="irt_theta")
        return IRTResult(list(items), discrimination, difficulty, scores, "grm", n)
    else:
        raise ValueError(f"Unknown model {model!r}; pick '2pl' or 'grm'")


# ===========================================================================
# 3) Oaxaca–Blinder decomposition
# ===========================================================================


@dataclass
class OaxacaResult:
    outcome: str
    group_col: str
    groups: tuple[Any, Any]
    means: dict[Any, float]
    raw_gap: float
    endowments: float
    coefficients: float
    interaction: float
    coef_table: pd.DataFrame
    notes: str = ""


def oaxaca_decompose(
    df: pd.DataFrame,
    outcome: str,
    group_col: str,
    predictors: Sequence[str],
    reference: Any | None = None,
    threefold: bool = True,
) -> OaxacaResult:
    """Threefold Oaxaca–Blinder decomposition of an outcome gap between two
    groups into endowments, coefficients, and interaction.

    Reference: Oaxaca (1973); Blinder (1973); Jann (2008) Stata oaxaca.
    """
    import statsmodels.api as sm

    sub = df[[outcome, group_col, *predictors]].dropna()
    g = sub[group_col].unique()
    if len(g) != 2:
        raise ValueError(f"Need exactly 2 groups; got {g}")
    if reference is None:
        reference = sorted(g.tolist())[0]
    other = [v for v in g if v != reference][0]
    a = sub[sub[group_col] == reference]
    b = sub[sub[group_col] == other]
    Xa = sm.add_constant(a[list(predictors)])
    Xb = sm.add_constant(b[list(predictors)])
    ya, yb = a[outcome], b[outcome]
    fa = sm.OLS(ya, Xa).fit()
    fb = sm.OLS(yb, Xb).fit()
    mean_xa = Xa.mean()
    mean_xb = Xb.mean()
    raw_gap = float(yb.mean() - ya.mean())
    # threefold: gap = E + C + I where
    #   E (endowments) = (Xb_bar - Xa_bar) . beta_a
    #   C (coefficients) = Xa_bar . (beta_b - beta_a)
    #   I (interaction) = (Xb_bar - Xa_bar) . (beta_b - beta_a)
    diff_x = mean_xb - mean_xa
    diff_b = fb.params - fa.params
    E = float((diff_x * fa.params).sum())
    C = float((mean_xa * diff_b).sum())
    I = float((diff_x * diff_b).sum())
    coef_table = pd.DataFrame({
        f"beta_{reference}": fa.params,
        f"beta_{other}": fb.params,
        f"mean_X_{reference}": mean_xa,
        f"mean_X_{other}": mean_xb,
        "endowment_contrib": diff_x * fa.params,
        "coefficient_contrib": mean_xa * diff_b,
        "interaction_contrib": diff_x * diff_b,
    })
    return OaxacaResult(
        outcome=outcome, group_col=group_col, groups=(reference, other),
        means={reference: float(ya.mean()), other: float(yb.mean())},
        raw_gap=raw_gap, endowments=E, coefficients=C, interaction=I,
        coef_table=coef_table,
        notes=f"OLS reference={reference}; threefold; n={len(sub)}",
    )


# ===========================================================================
# 4) SEM via semopy
# ===========================================================================


@dataclass
class SEMResult:
    fit_indices: dict[str, float]
    coefficients: pd.DataFrame
    n: int
    notes: str = ""


def sem_fit(df: pd.DataFrame, model_string: str) -> SEMResult:
    """Wrap `semopy.Model` for lavaan-style SEM. `model_string` uses semopy syntax:
    e.g. 'use_count ~ comfort + readiness ; readiness ~ comfort'.

    Reference: Bollen (1989); semopy library.
    """
    try:
        import semopy
    except ImportError as e:
        raise RuntimeError("semopy not installed. `pip install semopy`") from e

    sub = df.dropna()
    model = semopy.Model(model_string)
    res = model.fit(sub)
    try:
        stats = semopy.calc_stats(model)
        fit = stats.iloc[0].to_dict()
    except Exception:
        fit = {"chi2": np.nan, "df": np.nan, "p": np.nan}
    coefficients = model.inspect()
    return SEMResult(fit_indices={k: float(v) if isinstance(v, (int, float, np.floating)) else v for k, v in fit.items()},
                     coefficients=coefficients, n=len(sub),
                     notes="semopy MLE")


# ===========================================================================
# 5) IPW reweighting against an external benchmark
# ===========================================================================


@dataclass
class IPWResult:
    weights: pd.Series
    benchmark: pd.Series
    sample_dist: pd.Series
    effective_n: float
    notes: str = ""


def ipw_reweight(
    df: pd.DataFrame,
    benchmark: dict[Any, float],
    strata_col: str,
    cap: float = 10.0,
) -> IPWResult:
    """Compute post-stratification weights so that the weighted distribution of
    `strata_col` matches `benchmark`. `cap` limits any single weight relative
    to the mean (controls variance inflation).

    Reference: Deville & Särndal (1992); Mercer/Lau/Kennedy (2018, Pew).
    """
    sample_dist = df[strata_col].value_counts(normalize=True, dropna=False)
    bench = pd.Series(benchmark, name="benchmark") / sum(benchmark.values())
    common = sample_dist.index.intersection(bench.index)
    sample_dist = sample_dist.loc[common]
    bench = bench.loc[common]
    raw_w = (bench / sample_dist).to_dict()
    weights = df[strata_col].map(raw_w)
    # cap weights at `cap` × the mean
    mw = weights.mean()
    weights = weights.clip(upper=cap * mw)
    weights = weights * (len(df) / weights.sum())  # normalize to N
    eff_n = float(weights.sum() ** 2 / (weights ** 2).sum())
    return IPWResult(
        weights=weights, benchmark=bench, sample_dist=sample_dist,
        effective_n=eff_n,
        notes=f"post-stratification on {strata_col}; cap={cap}× mean",
    )


# ===========================================================================
# 6) Multilevel model — `ref` random intercept
# ===========================================================================


@dataclass
class MultilevelResult:
    formula: str
    group_col: str
    fixed_effects: pd.DataFrame
    random_effects_var: float
    icc: float
    n: int
    n_groups: int
    converged: bool
    notes: str = ""


def multilevel_model(
    df: pd.DataFrame,
    formula: str,
    group_col: str = "ref",
) -> MultilevelResult:
    """Fit a linear mixed model with `group_col` as a random intercept.
    `formula` uses statsmodels syntax: 'use_count ~ org_size_int + tech_person'.

    Reference: Gelman & Hill (2007).
    """
    import statsmodels.formula.api as smf
    import statsmodels.api as sm

    needed = set([group_col])
    # crude formula parse
    for tok in formula.replace("~", " ").replace("+", " ").replace("*", " ").split():
        tok = tok.strip()
        if tok and tok in df.columns:
            needed.add(tok)
    sub = df.dropna(subset=list(needed))
    md = smf.mixedlm(formula, sub, groups=sub[group_col])
    fit = md.fit(reml=True, method="lbfgs")
    fe = pd.DataFrame({
        "coef": fit.fe_params,
        "se": fit.bse_fe,
        "z": fit.tvalues[: len(fit.fe_params)],
        "p": fit.pvalues[: len(fit.fe_params)],
        "ci_lo": fit.conf_int().iloc[: len(fit.fe_params), 0],
        "ci_hi": fit.conf_int().iloc[: len(fit.fe_params), 1],
    })
    re_var = float(fit.cov_re.iloc[0, 0]) if hasattr(fit.cov_re, "iloc") else float(fit.cov_re[0][0])
    resid_var = float(fit.scale)
    icc = re_var / (re_var + resid_var) if (re_var + resid_var) > 0 else 0.0
    return MultilevelResult(
        formula=formula, group_col=group_col, fixed_effects=fe,
        random_effects_var=re_var, icc=icc,
        n=len(sub), n_groups=sub[group_col].nunique(),
        converged=fit.converged, notes="MixedLM REML",
    )


# ===========================================================================
# 7) Mediation with bootstrap + sensitivity (uses pingouin if present)
# ===========================================================================


@dataclass
class MediationResult:
    x: str
    m: str
    y: str
    a_path: float
    b_path: float
    c_total: float
    c_prime_direct: float
    indirect: float
    indirect_ci: tuple[float, float]
    proportion_mediated: float
    n: int
    sensitivity: dict[str, Any] = field(default_factory=dict)
    notes: str = ""


def mediation_full(
    df: pd.DataFrame,
    x: str,
    m: str,
    y: str,
    n_boot: int = 2000,
    seed: int = 0,
) -> MediationResult:
    """Causal-step mediation with bootstrap CI on the indirect effect.

    Optional sensitivity analysis: runs `pingouin.mediation_analysis` if available.
    """
    import statsmodels.api as sm
    rng = np.random.default_rng(seed)

    sub = df[[x, m, y]].dropna()
    n = len(sub)

    def fit(sample):
        Xa = sm.add_constant(sample[x])
        a_fit = sm.OLS(sample[m], Xa).fit()
        Xb = sm.add_constant(sample[[m, x]])
        b_fit = sm.OLS(sample[y], Xb).fit()
        Xc = sm.add_constant(sample[x])
        c_fit = sm.OLS(sample[y], Xc).fit()
        return a_fit.params[x], b_fit.params[m], c_fit.params[x], b_fit.params[x]

    a, b, c_total, c_prime = fit(sub)
    indirect = a * b
    boots = np.empty(n_boot)
    idx = np.arange(n)
    for i in range(n_boot):
        s = sub.iloc[rng.choice(idx, size=n, replace=True)]
        ai, bi, _, _ = fit(s)
        boots[i] = ai * bi
    lo, hi = np.quantile(boots, [0.025, 0.975])
    pm = indirect / c_total if c_total != 0 else float("nan")
    sensitivity: dict[str, Any] = {}
    try:
        import pingouin as pg
        sens = pg.mediation_analysis(data=sub, x=x, m=m, y=y, n_boot=500, seed=seed)
        sensitivity["pingouin"] = sens.to_dict()
    except ImportError:
        pass
    return MediationResult(
        x=x, m=m, y=y, a_path=float(a), b_path=float(b),
        c_total=float(c_total), c_prime_direct=float(c_prime),
        indirect=float(indirect), indirect_ci=(float(lo), float(hi)),
        proportion_mediated=float(pm), n=n, sensitivity=sensitivity,
        notes=f"causal-step OLS, {n_boot} bootstraps",
    )


# ===========================================================================
# 8) BERTopic pipeline for multilingual free-text
# ===========================================================================


@dataclass
class BERTopicResult:
    topics: pd.Series  # row index aligned with input
    topic_info: pd.DataFrame  # topic id, count, name, top words
    model: Any
    embeddings: np.ndarray
    notes: str = ""


def bertopic_pipeline(
    texts: Sequence[str],
    lang_detect: bool = True,
    embedding_model: str = "paraphrase-multilingual-MiniLM-L12-v2",
    min_topic_size: int = 8,
    random_state: int = 42,
) -> BERTopicResult:
    """Multilingual BERTopic pipeline.

    Reference: Grootendorst (2022); Reimers & Gurevych (2019).
    """
    try:
        from bertopic import BERTopic
        from sentence_transformers import SentenceTransformer
        from umap import UMAP
        from hdbscan import HDBSCAN
    except ImportError as e:
        raise RuntimeError("bertopic stack not installed; install bertopic, "
                           "sentence-transformers, umap-learn, hdbscan") from e

    embedder = SentenceTransformer(embedding_model)
    embeddings = embedder.encode(list(texts), show_progress_bar=False)
    umap_model = UMAP(n_neighbors=15, n_components=5, metric="cosine",
                      random_state=random_state)
    hdb = HDBSCAN(min_cluster_size=min_topic_size, metric="euclidean",
                  cluster_selection_method="eom", prediction_data=True)
    topic_model = BERTopic(
        embedding_model=embedder, umap_model=umap_model, hdbscan_model=hdb,
        verbose=False,
    )
    topics, _ = topic_model.fit_transform(list(texts), embeddings)
    info = topic_model.get_topic_info()
    return BERTopicResult(
        topics=pd.Series(topics, name="topic"),
        topic_info=info,
        model=topic_model,
        embeddings=embeddings,
        notes=f"BERTopic embedding={embedding_model}",
    )


# ===========================================================================
# 9) MCA + Louvain on multi-select co-occurrence
# ===========================================================================


@dataclass
class MCALouvainResult:
    coords: pd.DataFrame
    eigenvalues: pd.Series
    item_communities: pd.Series
    graph: Any  # networkx.Graph
    notes: str = ""


def mca_louvain(
    df: pd.DataFrame,
    multi_select_cols: Sequence[str],
    n_components: int = 4,
    cooccur_threshold: float = 0.05,
) -> MCALouvainResult:
    """Multiple Correspondence Analysis on multi-select binaries, plus a Louvain
    community detection on the item-cooccurrence graph.

    Reference: Le Roux & Rouanet (2010); Blondel et al. (2008).
    """
    try:
        import prince
        import networkx as nx
        import community.community_louvain as community_louvain  # python-louvain
    except ImportError as e:
        raise RuntimeError("prince, networkx, python-louvain required") from e

    sub = df[list(multi_select_cols)].dropna().astype(int)
    mca = prince.MCA(n_components=n_components, random_state=0)
    mca = mca.fit(sub)
    coords = mca.column_coordinates(sub)
    try:
        eigvals = pd.Series(mca.eigenvalues_, name="eigenvalue")
    except Exception:
        eigvals = pd.Series(dtype=float)

    # Build co-occurrence graph
    M = sub.values
    cooc = M.T @ M  # items x items
    n = M.shape[0]
    G = nx.Graph()
    items = list(sub.columns)
    for i, c in enumerate(items):
        G.add_node(c)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            phi = cooc[i, j] / n
            if phi > cooccur_threshold:
                G.add_edge(items[i], items[j], weight=float(phi))
    if len(G.edges) > 0:
        partition = community_louvain.best_partition(G)
    else:
        partition = {n: 0 for n in G.nodes}
    item_comms = pd.Series(partition, name="community")
    return MCALouvainResult(
        coords=coords, eigenvalues=eigvals,
        item_communities=item_comms, graph=G,
        notes=f"MCA n_components={n_components}; Louvain on co-occur > {cooccur_threshold}",
    )
