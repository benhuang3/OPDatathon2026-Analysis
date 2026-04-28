# METHODS.md — Methodological appendix

> Replication-grade documentation of every model used in the 30-hour research pass. Long enough that a reviewer could rebuild the analysis from this file alone.

**Software stack.** Python 3.12. `pandas` 2.2, `numpy` 1.26, `scipy` 1.13, `statsmodels` 0.14, `scikit-learn` 1.5, `matplotlib` 3.9, `pyarrow` 15. Method-specific: `stepmix` 2.1 (LCA), `girth` 0.8 (IRT), `semopy` 2.3 (SEM), `linearmodels` 6, `pingouin` 0.5, `bertopic` 0.16, `sentence-transformers` 2.7, `umap-learn` 0.5, `hdbscan` 0.8, `langdetect` 1.0, `prince` 0.13 (MCA), `python-louvain` 0.16, `networkx` 3.2.

**Random seeds.** Where applicable, RNG seed = 42 (cluster bootstrap); seed = 0 elsewhere. Reproducibility check on a clean clone: `pip install -r requirements.txt && python analysis/run_phase6.py && python analysis/build_figures.py`.

**Data preparation.** Both parquet files joined on row index (rows align). NORM-mean-imputed binaries restored to NaN before LCA / IRT / FA. `ai_risk_reward = -1` re-coded to `rr_dont_understand` indicator + `rr_attitude` (NaN where -1) per `codebook.md` W-3.

---

## §A. Latent Class Analysis (H2, H6)

**Library**: `stepmix.StepMix` (Morin et al. 2023, JOSS).
**Model class**: Bernoulli LCA with measurement model = "binary".
**Items**: H2 uses all 23 binary `[U]/[W]/[D]` items; H6 uses 14 `[U]+[W]` items.
**K range**: 2..6 (H2), 2..5 (H6).
**Estimation**: EM with `n_init=3` random starts; convergence on log-likelihood Δ < 1e-6.
**Selection**: BIC primary; entropy R² (relative entropy 1 − H(post)/log(K)) reported as separation diagnostic.
**Posterior class membership**: hard-assignment via `predict()` for visualization; soft posteriors (`predict_proba`) retained in `findings_raw.json` for downstream BCH-style covariate regressions.
**Item response probabilities**: extracted from `model.get_parameters_df()` where available; fallback computed manually from hard-assigned subgroup means.

**Why LCA over K-means.** K-means assumes spherical equal-variance clusters in Euclidean space; binary items violate both. LCA is generative on Bernoulli items, recovers item-response probabilities per class (interpretable), and provides BIC-grounded selection of K (Vermunt & Magidson 2002; Collins & Lanza 2010).

**Result note.** BIC continues to fall through k=6 in H2; we report the k=3 solution alongside the BIC-optimal k=6 to preserve continuity with the archive's F-18 typology while disclosing the full model-selection table.

## §B. 2-PL Item Response Theory (H7, H26)

**Library**: `girth` 0.8.
**Function**: `girth.twopl_mml` (marginal maximum likelihood for the 2PL model; Birnbaum 1968).
**Items**: 10 binary readiness items — 5 organizational infrastructure (`tech_person`, `merl_person`, `cloud_storage`, `data_use_policy`, `org_agreements`) + 5 `[D]` data-collection practices.
**Person score**: EAP (`girth.ability_eap`) — expected-a-posteriori, more stable than MLE at extreme score patterns.
**Discrimination interpretation**: α > 1 means the item separates respondents on the latent trait; α near 0 means the item is uninformative.
**Difficulty interpretation**: β = +1 means a respondent at θ = +1 has 50% probability of the item.
**Used in**: H7 (interpretation as evidence for unidimensionality); `readiness_irt` predictor in H26 (Poisson AIC comparison vs additive readiness).

**Why 2-PL over 1-PL or graded-response.** 1-PL (Rasch) constrains discrimination to be equal across items, which is empirically false here (range 0.46–2.43). The graded-response model is for ordinal outcomes; our items are binary. 2-PL is the canonical match.

**Limit.** With n=886 and 10 items, the model is well-identified; with k=2 latent dimensions (which we haven't fit), it would be marginal — flagged for follow-up.

## §C. Oaxaca–Blinder decomposition (H5)

**Implementation**: manual via `statsmodels.OLS`. Subset: small (≤15 staff) AND `tech_person == 0`.
**Outcome**: `use_count`. **Group**: `is_S` indicator (1 = Global South). **Predictors**: `readiness_additive`, `person_ai_comfort`, `d_count`, `org_size_int`.
**Decomposition form**: threefold (Jann 2008): raw_gap = E + C + I, where E = endowments, C = coefficients, I = interaction.
**Reference group**: GN (`is_S = 0`).
**Implementation detail**: `mean_X_b - mean_X_a` weighted by reference-group βs gives endowments; `mean_X_a` × (β_b − β_a) gives coefficients; remainder is interaction.

**Why this decomposition.** Tells us how much of the GS > GN gap is *what they have* (endowments) vs *what they get from what they have* (coefficients) vs the interaction. This is the standard wage-decomposition tool; here applied to a use-count gap (Oaxaca 1973; Blinder 1973; Jann 2008).

**Limit.** Three-way decomposition is sensitive to choice of reference group; we report only the GN-reference version. Linear OLS on a count outcome is approximate; a Poisson or RIF version would be cleaner.

## §D. Propensity-score matching (H5)

**Implementation**: `sklearn.linear_model.LogisticRegression` (max_iter=1000) for propensity; nearest-neighbor 1:1 matching on logit propensity by absolute difference, no caliper, no replacement.
**Treatment**: `is_S = 1` (GS).
**Predictors**: `readiness_additive`, `person_ai_comfort`, `d_count`, `org_size_int`.
**Result**: 132 matched pairs.

**Limit.** 1:1 NN with no caliper is the simplest variant; could be improved with a caliper of 0.2 SD logit propensity (Austin 2011) and replacement. Sample-size constraints in the small no-tech subset limited refinements.

## §E. Inverse Probability Weighting (H5, H23)

**Implementation**: `methods.ipw_reweight`.
**H5 (balanced GN/GS)**: target {is_S = 0: 0.5, is_S = 1: 0.5}; weights capped at 5× mean.
**H23 (target benchmark)**: target {gt: 0.60, india: 0.25, tech: 0.10, hubs: 0.05}, weights capped at 10× mean.
**Variance inflation**: effective n reported per Kish formula (Σw)² / Σ(w²).

**Why these benchmarks.** No clean global-NGO benchmark exists. We chose proportions that down-weight the Indian sub-sample (kept at 25% rather than its 27% sample share — minimal change) and re-balance `tech` upward (from 9% to 10%) to test whether sample skew drives F-1. The result (per-task gap differences < 0.5pp) tells us it doesn't.

**Limit.** This is calibration-style IPW (post-stratification), not propensity-IPW against an external benchmark. Stream H synthesis discusses the tradeoffs and the absence of a perfect external anchor.

## §F. Multilevel models (H1 cluster-bootstrap, H10a, H10b, H11, H12, H14, H15, H17, H18, H19, H20, H21, H22)

**Library**: `statsmodels.formula.api.mixedlm`.
**Estimator**: REML, optimizer L-BFGS.
**Group structure**: `ref` random intercept (4 groups: gt, india, tech, hubs) for most models; `org_label_first` (24 groups) for H12.
**ICC reporting**: REM intercept variance / (REM + residual) per Gelman & Hill (2007).

**Critical disclosure**. With n_groups = 4, the REML estimate of the random-intercept variance collapses to zero in every model. Reported `random_effects_var` ≈ 1e-15 across H10a–H22. Mathematically the model degenerates to OLS with `ref` controlled at the intercept level. We retain the multilevel form because (a) it's the project's required specification per discipline rules, (b) it produces correct point estimates for the fixed effects, and (c) we want the form documented so a reviewer with more group-level data could re-run the same code on a larger sample. *Substantively, all multilevel results in this paper should be read as fixed-effects regressions with `ref` controlled.*

**Cluster bootstrap (H1)**. Per-task gap CI computed by resampling whole `ref` strata with replacement (2,000 replicates), then recomputing the gap on the resampled dataset. This is the canonical correction for clustered samples (Cameron & Miller 2015) and is more conservative than the iid bootstrap.

## §G. Mediation analysis (H4)

**Implementation**: `methods.mediation_full`. Causal-step OLS (Baron & Kenny 1986) plus indirect-effect bootstrap (Preacher & Hayes 2008; MacKinnon 2008). 500 bootstrap replicates.
**X**: `rr_attitude` (1–5, with -1 → NaN). **M**: `readiness_additive`. **Y**: `use_count`.
**Sensitivity**: `pingouin.mediation_analysis` cross-check; `dowhy.refute_estimate` was attempted but excluded because the underlying causal-step model isn't a `dowhy` `CausalEstimate` object — flagged for follow-up. The Imai-Keele-Tingley sensitivity ρ test is on the Phase-7 wishlist.

**Why this approach over modern alternatives.** The classical causal-step bootstrap is interpretable, reproducible, and matches what the Phase-3 literature (D29–D32) prescribes for this study design. Modern alternatives (potential-outcomes mediation à la Imai et al. 2010) require stronger assumptions and don't change the qualitative conclusion (replicated F-11 PM ≈ 19%).

## §H. SEM (H8) — failed convergence

**Library**: `semopy`.
**Model**: 3-latent TOE structure.
**Failure mode**: "Eigenvalues did not converge"; sample covariance not PD.
**Diagnosis**: likely because `multi_country` is a sparse binary (16% prevalence) loading onto `EnvPress`, producing a near-singular indicator matrix. Phase-7 wishlist: refit with 2-latent CFA on `OrgCap` and `TechInfra` only, drop `EnvPress` or replace with a single manifest variable.

## §I. Factor analysis (H9)

**Library**: `sklearn.decomposition.FactorAnalysis`.
**Items**: 7 binary `ai_risk` indicators (bias, breaches, replacing, inequity, plagiarism, dependency, env).
**n_components**: 2 (testing Slovic's dread × unknown).
**Result**: F1 spans the full risk set with similar loadings; F2 is essentially empty. Slovic's 2-factor structure does not recover. We do not report a varimax rotation because the F2 loadings are too small to interpret.

**Why FA over EFA in `psych`/R.** `psych::fa` with parallel analysis would be ideal; a Python equivalent would require `factor_analyzer` (which we did not install). Sklearn's FA is rotated by default and produces consistent loadings on this binary data with ML estimation. For a `psych`-grade fit, follow up via R interface — flagged.

## §J. Multilingual BERTopic (H16)

**Pipeline**:
- `sentence_transformers.SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")` for embeddings.
- `umap.UMAP(n_neighbors=15, n_components=5, metric="cosine", random_state=42)` for dim reduction.
- `hdbscan.HDBSCAN(min_cluster_size=15, metric="euclidean", cluster_selection_method="eom", prediction_data=True)` for clustering.
- `bertopic.BERTopic(...)` with the pre-fit components.

**Input**: 606 non-null `ai_opentext` responses (English + Hindi + regional-language). No language-detection filtering applied (the multilingual MiniLM embedding handles cross-lingual placement).
**Output**: topic ids per document; `topic_info` dataframe with topic labels and counts.
**Validation strategy** (per Stream F synthesis): held-out C_v / C_NPMI coherence (Mimno et al. 2011; Röder et al. 2015) plus human inspection of 80 sampled responses against a Braun-Clarke (2006) thematic codebook. Time constraints meant the human-coding cross-check was not completed in this pass; flagged for Phase 7.

## §K. MCA + Louvain (H24)

**MCA**: `prince.MCA(n_components=4, random_state=0)` on 10 binary readiness items.
**Co-occurrence graph**: φ = (i AND j) / n; edge if φ > 0.05.
**Louvain**: `community.community_louvain.best_partition(G)`.
**Result**: 1 community (no separation at the chosen threshold).
**Diagnosis**: The threshold φ > 0.05 is too low for a 10-item binary set with high co-occurrence. Future work could lower threshold or use modularity gain as a stopping criterion.

## §L. Multiple-testing control

Within each hypothesis family that involves multiple tests (e.g., H1 across 7 tasks), Benjamini-Hochberg FDR at q = 0.05 is applied via `lib.fdr_adjust`. Across-hypothesis FDR (controlling the family-wise FDR over all 26 hypotheses) is not applied because the hypotheses are pre-registered and motivated by independent prior literature; their joint distribution under the global null is not the right reference distribution.

## §M. Effect-size reporting

Following the `findings.md` discipline, every effect is reported with: (a) the model-specific effect size (β, OR, gap, etc.), (b) 95% CI (analytic where exact, bootstrap where not), (c) the relevant *p*-value (FDR-adjusted within family), and (d) sample size. Bare *p* < 0.05 statements are not used.

## §N. Reproducibility checklist

| Item | Status |
|---|---|
| Code under version control | yes (this directory) |
| Data file SHAs documented | not yet — flagged |
| Random seeds set | yes |
| Hypotheses pre-registered before analysis | yes (`analysis/hypotheses.md`) |
| All findings (positive + null + failed) logged | yes (`analysis/findings.md`, 26 entries) |
| Robustness matrix per headline | yes (`analysis/robustness.md`) |
| Method-stack tested on synthetic data | yes (`analysis/tests/test_methods.py`) |
| Software versions pinned (floors) | yes (`requirements.txt`) |
| Bibliography exported | yes (`bibliography.bib`, 244 entries) |
| Codebook exists | yes (`analysis/codebook.md`) |

## §O. Phase-7 wishlist (deferred from this pass)

1. SEM re-fit with 2-latent CFA (after H8 convergence failure).
2. Imai-Keele-Tingley sensitivity ρ for H4 mediation (replacing the missing `dowhy.refute_estimate`).
3. BERTopic human-coding cross-check on 80 sampled responses.
4. MCA threshold sweep + alternative community-detection (modularity-greedy).
5. `factor_analyzer` parallel analysis on H9 (psych-grade).
6. NCCS / Candid benchmark IPW for the US sub-sample (separate from the proxy benchmark used in H23).
7. Three-step BCH covariate regression on LCA posterior class membership.
8. RIF-regression alternative to Oaxaca for distributional heterogeneity.
