# FIGURES.md — How each figure was built

A walk-through of the 10 figures in `figures/`. Each entry lists what the figure shows, which columns of the survey it draws from, the statistical method that produced the numbers, and the headline takeaway.

All figures are produced by `analysis/build_figures.py` from two inputs:

- `ai_readiness_survey_results/ai_exports/ai_survey_results_2024_n=930.parquet` — raw responses (n=930).
- `ai_readiness_survey_results/ai_exports/ai_survey_normalized_clustering_data.parquet` — same respondents with binaries one-hot expanded and continuous variables rescaled to 0–1.

Findings are loaded from `analysis/findings_raw.json`, which is written by `analysis/run_phase6.py`. Method definitions live in `analysis/methods.py`; helper functions in `analysis/lib.py`.

Conventions used throughout: `[U] X` = "currently uses AI for X"; `[W] X` = "wants to use AI for X"; `[D] X` = "data-collection practice X". `ref` is the 4-bucket source stratum (`gt`, `india`, `tech`, `hubs`).

---

## Fig 1 — Aspiration inversion (`fig1_aspiration_inversion`)

**Shows.** A paired bar chart of "use today" vs "want" rates per AI task (left), and the want−use gap with 95% cluster-bootstrap confidence intervals (right). The gap is largest for analytical tasks (Predict, Interpret, Assist, Organize) and smallest for content tasks (Generate, Ask, Translate).

**Source columns.** Seven `[U] ...` and seven `[W] ...` task columns from the normalized parquet, paired by task stem (`Generat`, `Ask`, `Translat`, `Interpret`, `Assist`, `Predict`, `Organi`).

**Method.** For each task, `use_pct` and `want_pct` are sample means of the binary indicator. The paired difference is tested with McNemar's exact test (one row per respondent, two columns: uses-task, wants-task). The CI is a **cluster bootstrap** that resamples whole `ref` strata with replacement (2,000 replicates) and recomputes the gap each time — see `lib.bootstrap_ci` and `methods.cluster_bootstrap`. Cluster bootstrap is more conservative than iid bootstrap when respondents are nested within source list (Cameron & Miller 2015).

**Result.** McNemar p < 1e-66 for the four analytical tasks; gap = +41pp (Organize), +40pp (Predict), +40pp (Assist), +35pp (Interpret).

---

## Fig 2 — Comfort × readiness heatmap (`fig2_comfort_readiness_heatmap`)

**Shows.** Predicted AI use_count (number of `[U]` tasks per respondent) over the 2-D grid of `person_ai_comfort` × `readiness_additive`, with actual respondents overplotted. Two main effects pull use_count up; the small negative interaction (mild concavity at the top right) appears as the slight bending of the high-value contours.

**Source columns.** `person_ai_comfort` (0–1 normalized), `readiness_additive` (mean of `tech_person`, `merl_person`, `cloud_storage`, `data_use_policy`, `org_agreements`, and the five `[D]` items — built in `build_figures.main`), and `use_count` = sum of the seven `[U]` task indicators.

**Method.** Poisson GLM (log link) with z-standardised predictors and their interaction (`methods.poisson_glm`). The fitted coefficients (intercept, β_comfort, β_readiness, β_interaction) come from `findings_raw.json[H3]`. The figure evaluates `exp(β · z)` over an 80×80 grid in original units, after re-standardising using the data's mean/std.

**Result.** β_comfort = +0.55, β_readiness = +0.31, β_interaction = −0.07 (p = 0.025). n = 878 after dropping rows with missing comfort, readiness, or use_count.

---

## Fig 3 — Latent-class profile (`fig3_lca_profile`)

**Shows.** Per-item probability that a member of each latent class endorses each `[U]` and `[W]` task. The middle class — labelled *Disengaged Aspirational* — has near-zero P(use) but high P(want) on the analytical items; this is the willing-but-not-using middle that the cluster3 column does not isolate.

**Source columns.** Seven `[U]` + seven `[W]` task columns from the normalized parquet (excluding "not currently" and "Other" / "don't know" placeholder columns).

**Method.** Bernoulli LCA with k=3 fit by `stepmix.StepMix`, called via `methods.latent_class_model` in `build_figures.fig3_lca_profile` (n_init=5, EM convergence on Δlog-lik < 1e-6). Hard-assignments produce per-class item-response probabilities by averaging the binary items within class. Classes are ordered by mean use_count and labelled heuristically by (use, want) profile — see lines 200–215 of `build_figures.py`. BIC = 13,131 at k=3.

**Result.** The k=3 LCA recovers a typology dominated by an "Aspirational" middle class — distinct from cluster3's HDBSCAN/UMAP partition because LCA is generative on Bernoulli items rather than distance-based.

---

## Fig 4 — Oaxaca decomposition, small no-tech orgs (`fig4_oaxaca_smallorg`)

**Shows.** Three-fold Oaxaca–Blinder decomposition of the GS−GN gap in `use_count` for the F-8 subset (org_size ≤ 15 AND tech_person == 0). The total gap (rightmost bar) is decomposed into endowments, coefficients, and interaction.

**Source columns.** Outcome `use_count`. Group `is_S` (1 = Global South, derived from `ref`/country). Predictors `readiness_additive`, `person_ai_comfort`, `d_count`, `org_size_int`. Subset filter: `org_size ≤ 15 AND tech_person == 0`.

**Method.** Manual three-fold Oaxaca implemented in `methods.oaxaca_blinder` using two `statsmodels.OLS` fits (one per group). raw_gap = E + C + I, with GN as reference group: E = (mean_X_GS − mean_X_GN) · β_GN; C = mean_X_GN · (β_GS − β_GN); I = remainder. Sensitivity-checked against propensity-score matching (`methods.psm_match`, 1:1 NN on logit propensity, 132 matched pairs) and IPW (`methods.ipw_reweight`, weights capped at 5× mean), both reported in `findings.md` as agreeing with OLS on direction and magnitude.

**Result.** GS small no-tech orgs use *more* AI than their GN counterparts — the F-8 reversal — driven mainly by endowments (GS has somewhat more of the helpful traits in this subset).

---

## Fig 5 — IRT readiness (`fig5_irt_readiness`)

**Shows.** Each of 10 binary readiness items plotted as a point in (difficulty β, discrimination α) space. `tech_person` sits in the top-right: hard to have, but its presence cleanly separates high- from low-readiness respondents.

**Source columns.** Five organizational infrastructure binaries (`tech_person`, `merl_person`, `cloud_storage`, `data_use_policy`, `org_agreements`) + five `[D]` data-practice binaries.

**Method.** 2-PL Item Response Theory via `girth.twopl_mml` (marginal MLE), called from `methods.irt_2pl`. Person abilities estimated with `girth.ability_eap` (expected-a-posteriori; more stable than MLE at extreme score patterns). All α range 0.46–2.43 — none are uninformative — supporting unidimensionality of the readiness latent. n = 886 (rows with at least one non-missing readiness item).

**Result.** Readiness is empirically unidimensional; using the IRT θ as a predictor in a Poisson model of `use_count` does not beat the simpler additive scale (per H26 in findings).

---

## Fig 6 — Comfort dominates (`fig6_comfort_dominates`)

**Shows.** Forest plot of standardised regression coefficients on `use_count` for four candidate predictors. `person_ai_comfort` sits at the top; `org_size_int` is statistically null after controls.

**Source columns.** Predictors: `person_ai_comfort`, `readiness_additive`, `tech_person`, `org_size_int`. Outcome: `use_count`. Random intercept group: `ref`.

**Method.** `statsmodels.formula.api.mixedlm` with REML, L-BFGS optimizer (`methods.mixedlm_fit`). Coefficients and CIs in `findings_raw.json[H21]`. **Critical disclosure**: with only 4 `ref` groups the random-intercept variance collapses to zero (ICC ≈ 0), so the model degenerates to OLS with `ref` controlled at the intercept. We retain the multilevel form for documentation but the substantive interpretation is fixed-effects OLS — see METHODS.md §F. n = 860.

**Result.** Person-level comfort dominates structural variables; the policy implication is that comprehension is upstream of infrastructure for nonprofit AI uptake.

---

## Fig 7 — IPW invariance (`fig7_ipw_invariance`)

**Shows.** Per-task want−use gaps unweighted vs after re-weighting the sample to a target source-mix benchmark. The IPW bars track the unweighted bars within < 0.5pp on every task.

**Source columns.** Same paired `[U]`/`[W]` task columns as Fig 1. Re-weighting variable: `ref` (4 strata).

**Method.** Inverse Probability Weighting via `methods.ipw_reweight`, target proportions {gt: 0.60, india: 0.25, tech: 0.10, hubs: 0.05}. Weights capped at 10× mean. Effective n is reported per Kish formula (Σw)² / Σ(w²). Per-task weighted gaps in `findings_raw.json[H23]`.

**Result.** F-1 (the aspiration inversion) is invariant to the choice of source-mix benchmark within the achievable range — the inversion is not an artefact of the over-representation of any one list.

---

## Fig 8 — Robustness matrix (`fig8_robustness_matrix`)

**Shows.** A 12-row × 6-column grid: each headline finding × six robustness checks (Primary, Method-2, Method-3, Weights, Spec, Subgroup). Green ✓ = pass, beige ~ = partial (one subgroup fails), white = not applicable.

**Source.** Hard-coded summary from `analysis/robustness.md`, which catalogues the alternative-method, alternative-weighting, alternative-specification, and alternative-subgroup re-tests for each headline. The matrix is purely a presentation of those re-tests; no data are re-computed inside `fig8_robustness_matrix()`.

**Result.** Every headline survives at least 5 of 6 checks; the partials (~) are documented in `robustness.md`.

---

## Fig 9 — Forest plot of effect sizes (`fig9_forest`)

**Shows.** 11 effect sizes stacked into a single forest plot — per-task aspiration gaps, the comfort and readiness β's from the Poisson GLM, the F-8 reversal estimate, and the comprehension- and vigilance-β's from the multilevel models.

**Source.** Effect sizes are hard-coded in `fig9_forest()` from `findings.md` and `findings_raw.json`. All effects are on different scales (percentage points for gaps, log-rate β's for Poisson, log-odds for logits) so the figure is read by-row, not by-row-comparison.

**Result.** A single visual roll-up that places the aspiration gap, comfort β, and comprehension/vigilance effects in the same frame — meant to support the headline that the comfort effect is the dominant one across the analytical tasks.

---

## Fig 10 — Cluster3 profile (`fig10_cluster_profile`)

**Shows.** Group means for the three HDBSCAN/UMAP clusters across eight metrics. The Late Adopters' bars on `cloud_storage` and `data_use_policy` exceed the Skeptics' — the data-dictionary's caution that the cluster labels are misleading is visible in this panel.

**Source columns.** `cluster3` (∈ {−1, 0, 1}, present in both parquets). Metrics: `use_count`, `want_count`, `person_ai_comfort`, `readiness_additive`, `tech_person`, `cloud_storage`, `data_use_policy`, `rr_dont_understand`. The last is built as `(ai_risk_reward == -1).astype(int)` per the codebook's W-3 split (the −1 code means "I don't understand AI enough" — not the low end of a scale).

**Method.** Group-by `cluster3` with `mean()` on the eight metrics. `use_count` and `want_count` (each ranging 0–7) are divided by 7 so they live on the same 0–1 axis as the rest of the panel.

**Result.** Late Adopters score higher on infrastructure than Skeptics but lower on use — corroborating the interpretation that cluster `0` is willing-but-unequipped (in *comprehension*, not *infrastructure*), not under-resourced.

---

## Reproducing every figure

```bash
pip install -r requirements.txt
python analysis/run_phase6.py        # writes findings_raw.json
python analysis/build_figures.py     # writes figures/*.png and figures/*.svg
```

`run_phase6.py` is idempotent and produces the same `findings_raw.json` on each run (RNG seeds set in METHODS.md §). `build_figures.py` reads only the parquet files and `findings_raw.json` — it does not refit any model, so it is fast (< 30 s) and deterministic.
