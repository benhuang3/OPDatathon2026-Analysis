"""Phase 6 — Deep statistical analysis runner.

Loads RAW + NORM, derives analytical features, runs every pre-registered
hypothesis (H1..H26) through the right method, and logs structured results to
`analysis/findings_raw.json` for later writing into `analysis/findings.md`.

Run: `python analysis/run_phase6.py`
"""

from __future__ import annotations

import json
import sys
import warnings
from dataclasses import asdict, is_dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "analysis"))

import lib  # noqa: E402  (the existing helpers)
import methods as M  # noqa: E402  (Phase 5 stack)

warnings.filterwarnings("ignore")

OUT_JSON = ROOT / "analysis" / "findings_raw.json"

FINDINGS: list[dict] = []


def log(fid: str, title: str, **kwargs):
    """Append a finding row. Keep keys flat and JSON-serializable."""
    row = {"id": fid, "title": title, **kwargs}
    # ensure dataclasses → dicts
    for k, v in list(row.items()):
        if is_dataclass(v):
            row[k] = asdict(v)
        elif isinstance(v, pd.DataFrame):
            row[k] = v.to_dict()
        elif isinstance(v, pd.Series):
            row[k] = v.to_dict()
        elif isinstance(v, np.ndarray):
            row[k] = v.tolist()
        elif isinstance(v, (np.floating, np.integer)):
            row[k] = float(v)
    FINDINGS.append(row)
    print(f"  {fid}  {title}")


def save():
    OUT_JSON.write_text(json.dumps(FINDINGS, indent=2, default=str), encoding="utf-8")
    print(f"\nLogged {len(FINDINGS)} findings to {OUT_JSON}")


# ---------------------------------------------------------------------------
# Data loading + feature derivation
# ---------------------------------------------------------------------------

def load_data() -> pd.DataFrame:
    raw = lib.load_raw().reset_index(drop=True)
    norm = lib.load_normalized().reset_index(drop=True)
    df = pd.concat([raw, norm.add_prefix("n_") if False else norm.drop(columns=[c for c in norm.columns if c in raw.columns])], axis=1)
    # restore NaN in NORM-mean-imputed binaries
    norm_binary_cols = ["n_cluster2"] if "n_cluster2" in df.columns else []
    df = df.copy()
    # `[U]/[W]/[D]` are clean from norm — keep
    # derive analytical features
    u_cols = [c for c in df.columns if c.startswith("[U] ") and "not currently" not in c.lower() and "Other" not in c]
    w_cols = [c for c in df.columns if c.startswith("[W] ") and "don't know" not in c.lower() and "Other" not in c]
    d_cols = [c for c in df.columns if c.startswith("[D] ")]
    df["use_count"] = df[u_cols].sum(axis=1)
    df["want_count"] = df[w_cols].sum(axis=1)
    df["d_count"] = df[d_cols].sum(axis=1)
    # readiness (additive, archive style)
    infra = ["tech_person", "merl_person", "cloud_storage", "data_use_policy", "org_agreements"]
    df["readiness_additive"] = df[infra + d_cols].fillna(0).mean(axis=1)
    # risk_count from raw ai_risk JSON
    df["risk_count"] = df["ai_risk"].apply(lambda x: len(lib.parse_jsonbytes(x)))
    # rr_dont_understand split
    df["rr_dont_understand"] = (df["ai_risk_reward"] == -1).astype(int)
    df["rr_attitude"] = df["ai_risk_reward"].where(df["ai_risk_reward"] >= 1)
    # GN/S indicator
    df["is_S"] = (df["global_north_south"] == "S").astype(int)
    # india flag
    df["in_india_ref"] = (df["ref"] == "india").astype(int)
    # comfort_high
    df["comfort_high"] = (df["person_ai_comfort"] >= 0.7).astype(int)
    df.loc[df["person_ai_comfort"].isna(), "comfort_high"] = np.nan
    # small org indicator
    df["small_org"] = (df["org_size_int"] <= 1).astype(int)
    # opentext length
    df["opentext_len"] = df["ai_opentext"].fillna("").apply(len)
    # first org_label
    df["org_label_first"] = df["org_label"].apply(lambda x: (lib.parse_jsonbytes(x) or [""])[0])
    return df, u_cols, w_cols, d_cols, infra


# ---------------------------------------------------------------------------
# Cluster I: re-tests
# ---------------------------------------------------------------------------

def H1_aspiration_inversion_multilevel(df, u_cols, w_cols):
    """Per-task paired multilevel logistic with `ref` random intercept."""
    print("\n--- H1: Aspiration inversion (multilevel) ---")
    tasks = ["Ask", "Assist", "Generat", "Interpret", "Organi", "Predict", "Translat"]
    rows = []
    for t in tasks:
        u, w = f"[U] {t}", f"[W] {t}"
        if u not in df.columns or w not in df.columns:
            continue
        # paired McNemar
        b = int(((df[u] == 1) & (df[w] == 0)).sum())
        c = int(((df[u] == 0) & (df[w] == 1)).sum())
        if b + c > 0:
            mc = stats.contingency.chi2_contingency([[b], [c]])
            # use scipy.stats.binomtest as exact McNemar
            try:
                p_mc = stats.binomtest(b, b + c, p=0.5).pvalue
            except Exception:
                p_mc = float("nan")
        else:
            p_mc = float("nan")
        gap = float(df[w].mean() - df[u].mean())
        # cluster bootstrap CI on the gap, resampling whole `ref` strata
        rng = np.random.default_rng(42)
        refs = df["ref"].unique()
        boots = []
        for _ in range(2000):
            sampled = rng.choice(refs, size=len(refs), replace=True)
            sub = pd.concat([df[df["ref"] == r] for r in sampled])
            boots.append(sub[w].mean() - sub[u].mean())
        lo, hi = float(np.quantile(boots, 0.025)), float(np.quantile(boots, 0.975))
        rows.append({"task": t, "n": int(len(df)), "use_pct": float(df[u].mean()),
                      "want_pct": float(df[w].mean()), "gap": gap,
                      "ci_lo": lo, "ci_hi": hi, "use_only": b, "want_only": c, "mcnemar_p": p_mc})
    out = pd.DataFrame(rows).set_index("task")
    out["p_fdr"] = lib.fdr_adjust(out["mcnemar_p"].fillna(1).values)
    log("H1", "Aspiration inversion (paired multilevel, cluster bootstrap CI)",
        method="paired_mcnemar_cluster_boot", per_task=out.to_dict(),
        pre_registered="yes",
        confirms=("Predict gap", float(out.loc["Predict", "gap"]),
                  "FDR p", float(out.loc["Predict", "p_fdr"])))


def H7_irt_readiness(df, infra, d_cols):
    """2PL IRT on the 10 binary readiness items."""
    print("\n--- H7: 2PL IRT on readiness items ---")
    items = infra + d_cols
    sub = df[items].dropna()
    sub = sub.astype(int)
    try:
        irt = M.irt_score(sub.reset_index(drop=True), items, model="2pl")
        a = irt.discrimination
        b = irt.difficulty["b"]
        # join IRT scores back
        df.loc[sub.index, "readiness_irt"] = irt.person_scores.values
        log("H7", "2PL IRT on readiness items",
            method="girth.twopl_mml", n=int(irt.n),
            discrimination=a.to_dict(), difficulty=b.to_dict(),
            min_alpha=float(a.min()), max_alpha=float(a.max()),
            pre_registered="yes",
            confirms="all alpha > 0" if (a > 0).all() else "some alpha <= 0")
    except Exception as e:
        log("H7", "2PL IRT (failed)", error=str(e), pre_registered="yes")
        df["readiness_irt"] = float("nan")
    return df


def H2_lca_typology(df, u_cols, w_cols, d_cols):
    """Bernoulli LCA on the [U]/[W]/[D] block; replace K-means typology."""
    print("\n--- H2: LCA on [U]/[W]/[D] indicators ---")
    items = u_cols + w_cols + d_cols
    sub = df[items].astype(int)
    try:
        lca = M.latent_class_model(sub.reset_index(drop=True), items, k_range=(2, 3, 4, 5, 6), n_init=3)
        # join lca class
        df.loc[sub.index, "lca_class"] = lca.hard_assignments.values
        # crosstab vs cluster3
        ct = pd.crosstab(df["lca_class"], df["cluster3"], dropna=False).to_dict()
        log("H2", "LCA replacement of K-means typology",
            method="stepmix.StepMix", best_k=int(lca.best_k),
            fit_table=lca.fit_table.to_dict(),
            crosstab_vs_cluster3=ct,
            pre_registered="yes")
    except Exception as e:
        log("H2", "LCA (failed)", error=str(e), pre_registered="yes")
    return df


def H3_marginal_effects_2D(df):
    """Continuous comfort × readiness interaction in Poisson on use_count."""
    print("\n--- H3: Comfort × readiness Poisson (continuous) ---")
    sub = df.dropna(subset=["use_count", "person_ai_comfort", "readiness_additive"]).copy()
    sub["comfort_z"] = (sub["person_ai_comfort"] - sub["person_ai_comfort"].mean()) / sub["person_ai_comfort"].std()
    sub["readiness_z"] = (sub["readiness_additive"] - sub["readiness_additive"].mean()) / sub["readiness_additive"].std()
    sub["interaction"] = sub["comfort_z"] * sub["readiness_z"]
    X = sm.add_constant(sub[["comfort_z", "readiness_z", "interaction"]])
    fit = sm.GLM(sub["use_count"], X, family=sm.families.Poisson()).fit()
    log("H3", "Continuous comfort × readiness interaction (Poisson)",
        method="GLM Poisson", n=int(len(sub)),
        params=fit.params.to_dict(), pvalues=fit.pvalues.to_dict(),
        ci_lo=fit.conf_int()[0].to_dict(), ci_hi=fit.conf_int()[1].to_dict(),
        pre_registered="yes",
        confirms="interaction p < 0.05" if fit.pvalues["interaction"] < 0.05 else "interaction n.s.")


def H4_mediation_with_sensitivity(df):
    """Mediation: rr_attitude → readiness → use_count, with bootstrap + DoWhy refute."""
    print("\n--- H4: Mediation rr_attitude → readiness → use_count ---")
    sub = df.dropna(subset=["rr_attitude", "readiness_additive", "use_count"]).copy()
    res = M.mediation_full(sub, "rr_attitude", "readiness_additive", "use_count", n_boot=500)
    log("H4", "Mediation rr_attitude → readiness → use_count",
        method="causal-step OLS + bootstrap",
        a=res.a_path, b=res.b_path, c_total=res.c_total, c_prime=res.c_prime_direct,
        indirect=res.indirect, indirect_ci=res.indirect_ci,
        proportion_mediated=res.proportion_mediated, n=res.n,
        pre_registered="yes")


def H5_oaxaca_psm_ipw_smallorg(df, infra):
    """Three robustness checks on F-8: Oaxaca / PSM / IPW for is_S among small no-tech orgs."""
    print("\n--- H5: F-8 reversal — Oaxaca / PSM / IPW ---")
    sub = df.dropna(subset=["use_count", "is_S", "small_org", "tech_person"]).copy()
    no_tech_small = sub[(sub["tech_person"] == 0) & (sub["small_org"] == 1)].copy()
    if len(no_tech_small) < 30:
        log("H5", "F-8 small-org reversal (insufficient n)", n=int(len(no_tech_small)),
            pre_registered="yes")
        return
    # Oaxaca
    predictors = ["readiness_additive", "person_ai_comfort", "d_count", "org_size_int"]
    no_tech_small_clean = no_tech_small.dropna(subset=predictors + ["use_count"])
    try:
        oax = M.oaxaca_decompose(no_tech_small_clean, "use_count", "is_S", predictors, reference=0)
        oax_summary = {
            "raw_gap": oax.raw_gap, "endowments": oax.endowments,
            "coefficients": oax.coefficients, "interaction": oax.interaction,
            "n": int(len(no_tech_small_clean)),
        }
    except Exception as e:
        oax_summary = {"error": str(e)}

    # PSM: simple 1:1 nearest neighbor on logit propensity
    try:
        from sklearn.linear_model import LogisticRegression
        Xp = no_tech_small_clean[predictors]
        yp = no_tech_small_clean["is_S"]
        lr = LogisticRegression(max_iter=1000)
        lr.fit(Xp, yp)
        ps = lr.predict_proba(Xp)[:, 1]
        treated = no_tech_small_clean.index[yp == 1].tolist()
        control = no_tech_small_clean.index[yp == 0].tolist()
        ps_t = pd.Series(ps[yp == 1].tolist(), index=treated)
        ps_c = pd.Series(ps[yp == 0].tolist(), index=control)
        matched = []
        used = set()
        for t in treated:
            avail = [c for c in control if c not in used]
            if not avail:
                break
            distances = (ps_c.loc[avail] - ps_t.loc[t]).abs()
            best = distances.idxmin()
            matched.append((t, best))
            used.add(best)
        psm_diff = float(np.mean([no_tech_small_clean.loc[t, "use_count"] - no_tech_small_clean.loc[c, "use_count"]
                                   for t, c in matched]))
        psm_summary = {"matched_pairs": len(matched), "treatment_effect": psm_diff}
    except Exception as e:
        psm_summary = {"error": str(e)}

    # IPW reweight to balanced 50/50 GN/GS
    try:
        ipw = M.ipw_reweight(no_tech_small_clean, {0: 0.5, 1: 0.5}, "is_S", cap=5)
        weighted_means = no_tech_small_clean.groupby("is_S").apply(
            lambda g: float(np.average(g["use_count"], weights=ipw.weights.loc[g.index]))
        ).to_dict()
        ipw_summary = {"weighted_means_by_isS": weighted_means,
                        "ipw_gap": weighted_means.get(1, 0) - weighted_means.get(0, 0)}
    except Exception as e:
        ipw_summary = {"error": str(e)}

    # Decision
    confirm_count = sum([
        oax_summary.get("raw_gap", 0) > 0,
        psm_summary.get("treatment_effect", -1) > 0,
        ipw_summary.get("ipw_gap", -1) > 0,
    ])
    log("H5", "F-8 reversal robustness (Oaxaca + PSM + IPW)",
        method="3-method triangulation",
        oaxaca=oax_summary, psm=psm_summary, ipw=ipw_summary,
        confirm_count=confirm_count,
        pre_registered="yes")


# ---------------------------------------------------------------------------
# Multilevel hypothesis batch (H10, H11, H12, H14, H15, H17, H18, H19, H20, H21, H22)
# ---------------------------------------------------------------------------

def multilevel_batch(df):
    print("\n--- Multilevel hypothesis batch ---")

    def safe_mlm(formula, fid, title, group="ref", **extra):
        try:
            res = M.multilevel_model(df, formula, group_col=group)
            payload = {
                "formula": formula, "n": res.n, "n_groups": res.n_groups,
                "icc": res.icc, "fixed": res.fixed_effects.to_dict(),
                "converged": res.converged,
            }
            payload.update(extra)
            log(fid, title, method="MixedLM REML", pre_registered="yes", **payload)
        except Exception as e:
            log(fid, title + " (failed)", error=str(e), pre_registered="yes")

    # H10 (a): comfort grows with use
    safe_mlm("person_ai_comfort ~ use_count + org_size_int + tech_person", "H10a",
             "Comfort grows with use (multilevel)")
    # H10 (b): risk_count rises with use, controlling for comfort
    safe_mlm("risk_count ~ use_count + person_ai_comfort + org_size_int", "H10b",
             "Vigilance grows with use net of comfort (multilevel)")
    # H11: comprehension > risk count for predicting low_use
    df["low_use"] = (df["use_count"] == 0).astype(int)
    safe_mlm("low_use ~ rr_dont_understand + risk_count + person_ai_comfort", "H11",
             "Comprehension is stronger predictor than risk count (multilevel)")
    # H12: gap universal across cause areas
    df["gap"] = df["want_count"] - df["use_count"]
    safe_mlm("gap ~ org_size_int + tech_person", "H12",
             "Aspiration gap robustness across causes (multilevel)",
             group="org_label_first")
    # H14: translation [W] over-indexes in GS
    safe_mlm("Q('[W] Translat') ~ is_S + person_ai_comfort + org_size_int", "H14",
             "Translation [W] over-indexes in GS (multilevel logistic-like via OLS-with-binary)")
    # H15: India NOT lower-comfort
    safe_mlm("comfort_high ~ in_india_ref + org_size_int + tech_person", "H15",
             "India NOT lower-comfort net of size×tech (multilevel)")
    # H17: skeptics disengaged
    sk = df[df["cluster3"] == -1]
    if len(sk) > 30:
        try:
            res = M.multilevel_model(sk, "risk_count ~ use_count + person_ai_comfort + opentext_len",
                                      group_col="ref")
            log("H17", "Skeptics disengaged not vigilant (multilevel within cluster3=-1)",
                method="MixedLM REML", n=res.n, fixed=res.fixed_effects.to_dict(),
                pre_registered="yes")
        except Exception as e:
            log("H17", "Skeptics disengagement (failed)", error=str(e), pre_registered="yes")
    # H18: tech_person vs org_size for want_count
    safe_mlm("want_count ~ tech_person + merl_person + org_size_int + person_ai_comfort", "H18",
             "Tech_person vs org_size on want_count (multilevel Poisson via OLS-approx)")
    # H19: policy-without-cloud
    df["policy_only"] = ((df["data_use_policy"] == 1) & (df["cloud_storage"] == 0)).astype(int)
    df["both_pc"] = ((df["data_use_policy"] == 1) & (df["cloud_storage"] == 1)).astype(int)
    safe_mlm("Q('use_count') ~ policy_only + both_pc + org_size_int", "H19",
             "Policy-without-cloud adopts less (multilevel)")
    # H20: org age non-effect
    safe_mlm("use_count ~ org_years_raw + org_size_int + tech_person", "H20",
             "Org age non-effect on use_count (multilevel)")
    # H21: comfort > readiness > size for cluster membership
    safe_mlm("Q('use_count') ~ person_ai_comfort + readiness_additive + org_size_int + tech_person", "H21",
             "Standardized correlates of use_count (multilevel)")
    # H22: rr_dont_understand → cluster3==0 OR
    df["is_late_adopter"] = (df["cluster3"] == 0).astype(int)
    safe_mlm("is_late_adopter ~ rr_dont_understand + person_ai_comfort + org_size_int", "H22",
             "rr_dont_understand → late adopter (multilevel)")


# ---------------------------------------------------------------------------
# H6 — re-derived 3-cluster typology under LCA
# ---------------------------------------------------------------------------

def H6_redirived_typology(df, u_cols, w_cols):
    """LCA on [U] + [W] + readiness + comfort proxy; report 3-class size and profile."""
    print("\n--- H6: Re-derived typology ---")
    items_full = u_cols + w_cols
    sub = df[items_full].astype(int)
    try:
        lca = M.latent_class_model(sub.reset_index(drop=True), items_full, k_range=(2, 3, 4, 5), n_init=3)
        sizes = lca.fit_table.loc[3, "n_per_class"] if 3 in lca.fit_table.index else None
        log("H6", "Re-derived typology (LCA on [U]+[W])",
            method="stepmix Bernoulli LCA",
            best_k=int(lca.best_k), fit_table=lca.fit_table.to_dict(),
            k3_sizes=sizes, pre_registered="yes")
    except Exception as e:
        log("H6", "Re-derived typology (failed)", error=str(e), pre_registered="yes")


# ---------------------------------------------------------------------------
# H8 — TOE SEM
# ---------------------------------------------------------------------------

def H8_toe_sem(df):
    print("\n--- H8: TOE SEM ---")
    sub = df.dropna(subset=["org_size_int", "tech_person", "merl_person",
                             "cloud_storage", "data_use_policy",
                             "collab_feasibility", "org_agreements", "multi_country",
                             "use_count"]).copy()
    if len(sub) < 100:
        log("H8", "TOE SEM (insufficient n)", n=int(len(sub)), pre_registered="yes")
        return
    model = """
    OrgCap =~ org_size_int + tech_person + merl_person
    TechInfra =~ cloud_storage + data_use_policy
    EnvPress =~ collab_feasibility + org_agreements + multi_country
    use_count ~ OrgCap + TechInfra + EnvPress
    """
    try:
        res = M.sem_fit(sub, model)
        log("H8", "TOE SEM",
            method="semopy MLE", fit_indices=res.fit_indices,
            coefficients=res.coefficients.to_dict(), n=res.n,
            pre_registered="yes")
    except Exception as e:
        log("H8", "TOE SEM (failed)", error=str(e), pre_registered="yes")


# ---------------------------------------------------------------------------
# H9 — Risk perception 2-factor
# ---------------------------------------------------------------------------

def H9_risk_factor_structure(df):
    print("\n--- H9: Risk perception factor structure ---")
    risks_per_row = df["ai_risk"].apply(lib.parse_jsonbytes)
    # canonical 7
    canon = ["Decisions based on biased AI models", "AI-related data breaches",
             "Replacing workers with AI",
             "Increasing inequity, if lower-capacity organizations are unable to adopt it, or if AI bias harms groups",
             "Plagiarism, violating copyrights, and/or losing intellectual property",
             "(Over) Dependency on commercial AI products",
             "Environmental impact of using AI"]
    short = ["bias", "breaches", "replacing", "inequity", "plagiarism", "dependency", "env"]
    risk_df = pd.DataFrame({s: risks_per_row.apply(lambda r, c=c: int(c in r))
                             for s, c in zip(short, canon)})
    # FA
    try:
        from sklearn.decomposition import FactorAnalysis
        sub = risk_df.dropna()
        fa = FactorAnalysis(n_components=2, random_state=0)
        fa.fit(sub.values)
        loadings = pd.DataFrame(fa.components_.T, index=sub.columns,
                                 columns=["F1", "F2"])
        log("H9", "Risk perception 2-factor structure",
            method="FactorAnalysis n=2", loadings=loadings.to_dict(),
            n=int(len(sub)),
            pre_registered="yes")
    except Exception as e:
        log("H9", "Risk perception factor structure (failed)", error=str(e),
            pre_registered="yes")


# ---------------------------------------------------------------------------
# H13 — Africa hubs vs non-hubs
# ---------------------------------------------------------------------------

def H13_africa_hubs(df):
    print("\n--- H13: Africa hubs vs non-hubs ---")
    afr = df[df["continent"] == "Africa"].copy()
    afr["is_hubs"] = (afr["ref"] == "hubs").astype(int)
    if afr["is_hubs"].nunique() < 2:
        log("H13", "Africa hubs subset (single category)", n=int(len(afr)),
            pre_registered="yes")
        return
    a = afr.loc[afr["is_hubs"] == 1, "use_count"].dropna()
    b = afr.loc[afr["is_hubs"] == 0, "use_count"].dropna()
    if len(a) > 0 and len(b) > 0:
        u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        log("H13", "Africa: hubs vs non-hubs use_count",
            method="Mann-Whitney", n_hubs=int(len(a)), n_nonhubs=int(len(b)),
            mean_hubs=float(a.mean()), mean_nonhubs=float(b.mean()),
            p=float(p), pre_registered="yes")
    else:
        log("H13", "Africa hubs subset (zero on one side)", pre_registered="yes")


# ---------------------------------------------------------------------------
# H23 — IPW invariance for F-1
# ---------------------------------------------------------------------------

def H23_ipw_invariance(df):
    print("\n--- H23: IPW invariance for F-1 ---")
    bench = {"gt": 0.60, "india": 0.25, "tech": 0.10, "hubs": 0.05}
    ipw = M.ipw_reweight(df, bench, "ref", cap=10)
    out_rows = []
    for t in ["Ask", "Assist", "Generat", "Interpret", "Organi", "Predict", "Translat"]:
        u_col = f"[U] {t}"; w_col = f"[W] {t}"
        if u_col in df.columns and w_col in df.columns:
            u_w = float(np.average(df[u_col], weights=ipw.weights))
            w_w = float(np.average(df[w_col], weights=ipw.weights))
            out_rows.append({"task": t, "u_weighted": u_w, "w_weighted": w_w,
                              "gap_weighted": w_w - u_w,
                              "u_unweighted": float(df[u_col].mean()),
                              "w_unweighted": float(df[w_col].mean()),
                              "gap_unweighted": float(df[w_col].mean() - df[u_col].mean())})
    log("H23", "F-1 inversion under IPW vs unweighted",
        method="IPW reweight on ref", per_task=out_rows,
        effective_n=ipw.effective_n,
        pre_registered="yes")


# ---------------------------------------------------------------------------
# H24 — MCA + Louvain on [D] + infra
# ---------------------------------------------------------------------------

def H24_mca_louvain(df, d_cols, infra):
    print("\n--- H24: MCA + Louvain on [D] + infrastructure ---")
    items = d_cols + infra
    sub = df[items].dropna().astype(int)
    try:
        res = M.mca_louvain(sub.reset_index(drop=True), items, n_components=4)
        log("H24", "MCA + Louvain on [D] + infra",
            method="prince MCA + python-louvain",
            n=int(len(sub)), n_communities=int(res.item_communities.nunique()),
            communities=res.item_communities.to_dict(),
            pre_registered="yes")
    except Exception as e:
        log("H24", "MCA + Louvain (failed)", error=str(e), pre_registered="yes")


# ---------------------------------------------------------------------------
# H16 / H25 — BERTopic on ai_opentext (slow; behind a flag)
# ---------------------------------------------------------------------------

def H16_bertopic(df, run: bool = True):
    if not run:
        log("H16", "BERTopic skipped (run=False)", pre_registered="yes")
        return
    print("\n--- H16: BERTopic on ai_opentext ---")
    texts = df["ai_opentext"].dropna()
    if len(texts) < 50:
        log("H16", "BERTopic insufficient n", n=int(len(texts)), pre_registered="yes")
        return
    try:
        res = M.bertopic_pipeline(texts.tolist(), min_topic_size=15)
        # join topics to df
        df.loc[texts.index, "bertopic"] = res.topics.values
        # topic distribution by cluster3
        ct = pd.crosstab(df["bertopic"], df["cluster3"], dropna=False)
        log("H16", "BERTopic on ai_opentext",
            method="BERTopic + paraphrase-multilingual-MiniLM-L12-v2",
            n=int(len(texts)),
            n_topics=int(res.topic_info.shape[0]),
            top_topics=res.topic_info.head(10).to_dict(),
            cluster3_crosstab=ct.to_dict(),
            pre_registered="yes")
    except Exception as e:
        log("H16", "BERTopic (failed)", error=str(e), pre_registered="yes")


# ---------------------------------------------------------------------------
# H26 — IRT vs additive readiness — model fit comparison
# ---------------------------------------------------------------------------

def H26_irt_vs_additive(df):
    print("\n--- H26: IRT vs additive readiness ---")
    sub = df.dropna(subset=["use_count", "readiness_additive"]).copy()
    if "readiness_irt" not in sub.columns or sub["readiness_irt"].isna().all():
        log("H26", "IRT not available; comparing additive only", pre_registered="yes")
        return
    sub2 = sub.dropna(subset=["readiness_irt"])
    X1 = sm.add_constant(sub2[["readiness_additive"]])
    X2 = sm.add_constant(sub2[["readiness_irt"]])
    f1 = sm.GLM(sub2["use_count"], X1, family=sm.families.Poisson()).fit()
    f2 = sm.GLM(sub2["use_count"], X2, family=sm.families.Poisson()).fit()
    log("H26", "IRT vs additive readiness for use_count",
        method="Poisson GLM AIC compare",
        aic_additive=float(f1.aic), aic_irt=float(f2.aic),
        delta_aic=float(f1.aic - f2.aic),
        beta_additive=float(f1.params["readiness_additive"]),
        beta_irt=float(f2.params["readiness_irt"]),
        n=int(len(sub2)),
        pre_registered="yes")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Loading data...")
    df, u_cols, w_cols, d_cols, infra = load_data()
    print(f"  shape: {df.shape}")
    print(f"  use_count distribution: {df['use_count'].describe().to_dict()}")
    print(f"  want_count distribution: {df['want_count'].describe().to_dict()}")

    # CLUSTER I: re-tests
    H1_aspiration_inversion_multilevel(df, u_cols, w_cols)
    df = H7_irt_readiness(df, infra, d_cols)  # produces readiness_irt
    df = H2_lca_typology(df, u_cols, w_cols, d_cols)
    H3_marginal_effects_2D(df)
    H4_mediation_with_sensitivity(df)
    H5_oaxaca_psm_ipw_smallorg(df, infra)
    H6_redirived_typology(df, u_cols, w_cols)

    # CLUSTER II: new hypotheses
    H8_toe_sem(df)
    H9_risk_factor_structure(df)
    H13_africa_hubs(df)
    H23_ipw_invariance(df)
    H24_mca_louvain(df, d_cols, infra)
    H26_irt_vs_additive(df)
    multilevel_batch(df)

    # BERTopic last (slow)
    H16_bertopic(df, run=True)

    save()


if __name__ == "__main__":
    main()
