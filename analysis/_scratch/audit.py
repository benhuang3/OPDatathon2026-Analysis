"""Phase 1 schema audit. Inspects raw + normalized parquet, prints a structured
report so we can build analysis/codebook.md against ground truth."""

from __future__ import annotations
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path("/Users/benjaminhuang/gitssh/OPDatathon2026/ai_readiness_survey_results/ai_exports")
RAW = pd.read_parquet(DATA / "ai_survey_results_2024_n=930.parquet")
NORM = pd.read_parquet(DATA / "ai_survey_normalized_clustering_data.parquet")

pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 80)


def banner(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


banner("Shapes")
print("RAW:", RAW.shape, "  NORM:", NORM.shape)
print("\nRAW columns:")
for c in RAW.columns:
    print(f"  {c!r:<32}  dtype={RAW[c].dtype}")
print("\nNORM columns:")
for c in NORM.columns:
    print(f"  {c!r:<70}  dtype={NORM[c].dtype}")


banner("Row alignment between RAW and NORM")
# cluster3 should agree row-by-row (per existing 4hr_pass note)
print("cluster3 RAW dist:", RAW["cluster3"].value_counts().to_dict())
print("cluster3 NORM dist:", NORM["cluster3"].value_counts().to_dict())
if "cluster2" in NORM.columns:
    print("cluster2 NORM dist:", NORM["cluster2"].value_counts().to_dict())
# Check if both files have a consistent ordering -- look at any obviously-shared col
common = [c for c in RAW.columns if c in NORM.columns]
print("\nColumns in both files:", common)
for c in common:
    if RAW[c].dtype == NORM[c].dtype:
        eq = (RAW[c].fillna(-999) == NORM[c].fillna(-999)).mean()
        print(f"  {c}: row-equal frac = {eq:.3f}")
    else:
        print(f"  {c}: dtypes differ -> RAW {RAW[c].dtype} / NORM {NORM[c].dtype}")


banner("Missingness — RAW")
miss = RAW.isna().mean().sort_values(ascending=False)
print(miss.to_string())

banner("Missingness — NORM")
miss = NORM.isna().mean().sort_values(ascending=False)
print(miss.to_string())


banner("Per-column unique-value summary — RAW")
for c in RAW.columns:
    s = RAW[c]
    nun = s.nunique(dropna=True)
    nmiss = s.isna().sum()
    if pd.api.types.is_numeric_dtype(s):
        print(f"  {c!r:<28} num   nun={nun:<5} miss={nmiss:<4} min={s.min()} max={s.max()} mean={s.mean():.3f}")
    else:
        sample = s.dropna().unique()
        if len(sample) > 12:
            sample_repr = list(sample[:6]) + ["..."] + list(sample[-3:])
        else:
            sample_repr = list(sample)
        print(f"  {c!r:<28} other nun={nun:<5} miss={nmiss:<4} sample={sample_repr}")


banner("Per-column unique-value summary — NORM")
for c in NORM.columns:
    s = NORM[c]
    nun = s.nunique(dropna=True)
    nmiss = s.isna().sum()
    if pd.api.types.is_numeric_dtype(s):
        print(f"  {c!r:<70} num   nun={nun:<4} miss={nmiss:<3} min={s.min()} max={s.max()} mean={s.mean():.3f}")
    else:
        sample = list(s.dropna().unique()[:6])
        print(f"  {c!r:<70} other nun={nun:<4} miss={nmiss:<3} sample={sample}")


banner("Monotonicity audit: NORM 0–1 columns vs RAW")
# Pairs to check: person_ai_comfort vs person_ai_comfort_raw, collab_feasibility vs collab_feasibility_raw,
# org_years vs org_years_raw, person_org_years vs person_org_years_raw,
# regionality vs regionality, org_size_int vs org_small_med_large
def spearman(a, b):
    a = pd.Series(a).reset_index(drop=True)
    b = pd.Series(b).reset_index(drop=True)
    mask = a.notna() & b.notna()
    if mask.sum() < 5:
        return float("nan")
    return a[mask].rank().corr(b[mask].rank())

pairs = [
    ("person_ai_comfort_raw", "person_ai_comfort"),
    ("collab_feasibility_raw", "collab_feasibility"),
    ("org_years_raw", "org_years"),
    ("person_org_years_raw", "person_org_years"),
]
for raw_col, norm_col in pairs:
    if raw_col in RAW.columns and norm_col in NORM.columns:
        rho = spearman(RAW[raw_col], NORM[norm_col])
        print(f"  {raw_col} vs NORM[{norm_col}]: spearman={rho:.4f}")
        # also show min/max of normed conditional on raw extremes
        mn = NORM[norm_col].min(); mx = NORM[norm_col].max()
        print(f"    NORM range: [{mn:.4f}, {mx:.4f}]")
# regionality - exists raw 1..3 and may also be in NORM
if "regionality" in RAW.columns and "regionality" in NORM.columns:
    rho = spearman(RAW["regionality"], NORM["regionality"])
    print(f"  regionality (raw vs norm): spearman={rho:.4f}")
    print("    raw value_counts:", RAW["regionality"].value_counts(dropna=False).to_dict())
    print("    norm value_counts:", NORM["regionality"].value_counts(dropna=False).to_dict())

# org_size_int (raw 0..5) vs org_small_med_large (norm 0/0.5/1)
if "org_size_int" in RAW.columns and "org_small_med_large" in NORM.columns:
    rho = spearman(RAW["org_size_int"], NORM["org_small_med_large"])
    print(f"  org_size_int vs org_small_med_large: spearman={rho:.4f}")
    ct = pd.crosstab(RAW["org_size_int"], NORM["org_small_med_large"], dropna=False)
    print("    crosstab:")
    print(ct)


banner("ai_risk_reward special code -1")
vc = RAW["ai_risk_reward"].value_counts(dropna=False).sort_index()
print(vc)
print(f"-1 fraction = {(RAW['ai_risk_reward'] == -1).mean():.4f}")


banner("Bytes-encoded JSON multi-selects")
for col in ["ai_use", "ai_want", "ai_risk", "data_kinds", "org_label"]:
    s = RAW[col]
    sample = s.dropna().head(3).tolist()
    print(f"  {col}: type(first)={type(sample[0]).__name__ if sample else 'NA'}  examples:")
    for x in sample:
        print(f"     {x!r}")


banner("[U]/[W]/[D] one-hot columns in NORM")
u_cols = [c for c in NORM.columns if c.startswith("[U] ")]
w_cols = [c for c in NORM.columns if c.startswith("[W] ")]
d_cols = [c for c in NORM.columns if c.startswith("[D] ")]
print(f"  [U] columns ({len(u_cols)}):")
for c in u_cols:
    print(f"     {c!r:<40} mean={NORM[c].mean():.4f}  vals={sorted(NORM[c].dropna().unique())[:6]}")
print(f"  [W] columns ({len(w_cols)}):")
for c in w_cols:
    print(f"     {c!r:<40} mean={NORM[c].mean():.4f}")
print(f"  [D] columns ({len(d_cols)}):")
for c in d_cols:
    print(f"     {c!r:<90} mean={NORM[c].mean():.4f}")


banner("Cluster columns spot check")
print("RAW cluster3 vs NORM cluster3 row-equal frac:")
print(f"  {(RAW['cluster3'] == NORM['cluster3']).mean():.4f}")
if "cluster2" in NORM.columns:
    print("\nNORM cluster2 vs cluster3 crosstab:")
    print(pd.crosstab(NORM["cluster2"], NORM["cluster3"], dropna=False))


banner("Source-conditional fields — verify gating")
gated = {
    "non_org_type": ("nonprofit", 0),
    "non_data_work": ("collects_data", 0),
    "af_region": ("ref", "hubs"),  # actually only Africa-hubs; will check
    "hubs_rural_urban": ("ref", "hubs"),
    "in_india": ("ref", "india"),
    "india_state": ("ref", "india"),
    "india_rural_urban": ("ref", "india"),
}
for col, (gate_col, gate_val) in gated.items():
    if col not in RAW.columns or gate_col not in RAW.columns:
        continue
    in_gate = RAW[gate_col] == gate_val
    out_gate = RAW[gate_col] != gate_val
    in_obs = RAW.loc[in_gate, col].notna().sum()
    out_obs = RAW.loc[out_gate, col].notna().sum()
    print(f"  {col}: in-gate({gate_col}={gate_val}) obs={in_obs}/{in_gate.sum()}; out-gate obs={out_obs}/{out_gate.sum()}")


banner("ref vs source")
print(RAW.groupby("ref")["source"].value_counts())


banner("global_north_south table")
print(RAW["global_north_south"].value_counts(dropna=False))
print("global_north_south_int (raw):", RAW["global_north_south_int"].value_counts(dropna=False).to_dict())
if "global_north_south_int" in NORM.columns:
    print("global_north_south_int (norm):", NORM["global_north_south_int"].value_counts(dropna=False).to_dict())


banner("Spot-check 5 random rows: raw vs norm equivalence")
rng = np.random.default_rng(42)
idxs = rng.choice(len(RAW), size=5, replace=False)
for i in idxs:
    r = RAW.iloc[i]
    n = NORM.iloc[i]
    print(f"\n--- row {i} ---")
    print(f"  raw role={r.get('role')}  org_size={r.get('org_size')}  org_size_int={r.get('org_size_int')}  cluster3={r.get('cluster3')}  ref={r.get('ref')}  GN/S={r.get('global_north_south')}")
    print(f"  raw person_ai_comfort_raw={r.get('person_ai_comfort_raw')} -> NORM person_ai_comfort={n.get('person_ai_comfort')}")
    print(f"  raw collab_feasibility_raw={r.get('collab_feasibility_raw')} -> NORM collab_feasibility={n.get('collab_feasibility')}")
    print(f"  raw org_years_raw={r.get('org_years_raw')} -> NORM org_years={n.get('org_years')}")
    print(f"  raw cluster3={r.get('cluster3')}  NORM cluster3={n.get('cluster3')}  NORM cluster2={n.get('cluster2')}")


banner("ai_want_2+ definition verification")
if "ai_want_2+" in NORM.columns:
    w_cols = [c for c in NORM.columns if c.startswith("[W] ")
              and "don't know" not in c.lower() and "Other" not in c]
    counted = NORM[w_cols].sum(axis=1)
    derived = (counted >= 2).astype(int)
    actual = NORM["ai_want_2+"].astype(int)
    agreement = (derived == actual).mean()
    print(f"  derived (>=2 [W] cols, excl 'don't know'/'Other') vs ai_want_2+: agreement={agreement:.4f}")
    if agreement < 1.0:
        # Try variants
        for excl_other in [True, False]:
            for excl_dk in [True, False]:
                cols2 = [c for c in NORM.columns if c.startswith("[W] ")
                         and (not excl_dk or "don't know" not in c.lower())
                         and (not excl_other or "Other" not in c)]
                counted = NORM[cols2].sum(axis=1)
                derived = (counted >= 2).astype(int)
                a = (derived == actual).mean()
                print(f"    excl_other={excl_other} excl_dk={excl_dk}: agreement={a:.4f}, n_cols={len(cols2)}")


banner("Continent / continent_int audit")
print(RAW.groupby("continent")["continent_int"].value_counts(dropna=False))
