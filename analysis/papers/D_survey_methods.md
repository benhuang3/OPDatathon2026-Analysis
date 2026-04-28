# Stream D — Survey statistical methods

Paper-cards for the methodological state-of-the-art that Phase 5 / Phase 6 will draw on: latent class analysis, item response theory, structural equation modeling, decomposition methods, sampling-weight construction, multilevel models, multiple correspondence analysis, multiple-testing correction, mediation, and topic-model evaluation.

---

## D1 — Vermunt & Magidson (2002) — LCA as model-based clustering

```yaml
id: D1
stream: D
relevance_score: 5
peer_reviewed: yes
year: 2002
tags: [LCA, clustering, model-based, methods]
verified_url: yes
```

**Citation.** Vermunt, J. K., & Magidson, J. (2002). Latent class cluster analysis. In J. A. Hagenaars & A. L. McCutcheon (Eds.), *Applied Latent Class Analysis* (pp. 89–106). Cambridge University Press.

**DOI / URL.** https://doi.org/10.1017/CBO9780511499531.004 — chapter PDF: https://jeroenvermunt.nl/hagenaars2002b.pdf

**Sample / Method.** Methodological chapter. Recasts LCA as a probabilistic clustering method, comparing it head-to-head with K-means, and shows that LCA dominates when indicators are categorical, scales differ, or class proportions are unbalanced.

**Key claim(s).**
- LCA is a *model-based* alternative to K-means: it provides BIC, entropy, posterior class probabilities, and a likelihood — none of which K-means offers.
- The K-means objective implicitly assumes equal-variance spherical Gaussians; with binary `[U]/[W]/[D]` items those assumptions are wrong.

**Takeaway.** Direct method blueprint for replacing the existing `cluster3` (HDBSCAN/UMAP) and `cluster2` (K-means) typologies with a Bernoulli-LCA on the binary indicator block in `stepmix`.

**Confirms / Complicates / Contradicts.** Method only — provides the rationale for re-running Phase 5 typology under LCA before re-doing the inversion / aspiration analyses on the new classes.

---

## D2 — Lazarsfeld & Henry (1968) — Latent Structure foundational

```yaml
id: D2
stream: D
relevance_score: 4
peer_reviewed: yes
year: 1968
tags: [LCA, foundational, latent structure]
verified_url: yes
```

**Citation.** Lazarsfeld, P. F., & Henry, N. W. (1968). *Latent Structure Analysis*. Boston: Houghton Mifflin.

**DOI / URL.** Library record: https://www.cambridge.org/core/journals/psychometrika/article/abs/paul-f-lazarsfeld-and-neil-w-henry-latent-structure-analysis-boston-houghton-mifflin-company-1968-950/7E81E82D4C1CAC7AFE130BE20C747BBC (Psychometrika review).

**Sample / Method.** Foundational monograph. Develops the conditional-independence (local independence) axiom that underlies all later LCA / IRT formulations.

**Key claim(s).**
- Observed associations among manifest indicators are explained by an unobserved categorical latent variable; conditional on the latent class, indicators are independent.
- Establishes identifiability conditions for finite mixtures of Bernoulli items.

**Takeaway.** The intellectual ground for D1, D17, D24. Cite when justifying why LCA is the appropriate generative model for the `[U]/[W]/[D]` block.

**Confirms / Complicates / Contradicts.** Method only.

---

## D3 — Collins & Lanza (2010) — LCA / LTA textbook

```yaml
id: D3
stream: D
relevance_score: 5
peer_reviewed: yes
year: 2010
tags: [LCA, LTA, textbook, social-behavioral]
verified_url: yes
```

**Citation.** Collins, L. M., & Lanza, S. T. (2010). *Latent Class and Latent Transition Analysis: With Applications in the Social, Behavioral, and Health Sciences*. Hoboken, NJ: Wiley.

**DOI / URL.** https://doi.org/10.1002/9780470567333

**Sample / Method.** Textbook. Comprehensive treatment of cross-sectional LCA, latent transition analysis, multi-group LCA, parameter restrictions, and identification diagnostics, with worked examples.

**Key claim(s).**
- Class enumeration should rely on BIC, AIC, ABIC, BLRT, and entropy *jointly*, not any single statistic.
- Multi-group LCA can test invariance across `ref` (gt / india / tech / hubs) before pooling.

**Takeaway.** Operationalises Phase 5 LCA decisions: K-selection rule (BIC + BLRT + entropy ≥ 0.7), multi-group invariance test across `ref`, and three-step distal-outcome handling for downstream regressions.

**Confirms / Complicates / Contradicts.** Method only.

---

## D4 — Nylund, Asparouhov, & Muthén (2007) — class-enumeration simulation

```yaml
id: D4
stream: D
relevance_score: 5
peer_reviewed: yes
year: 2007
tags: [LCA, K selection, BIC, BLRT, simulation]
verified_url: yes
```

**Citation.** Nylund, K. L., Asparouhov, T., & Muthén, B. O. (2007). Deciding on the number of classes in latent class analysis and growth mixture modeling: a Monte Carlo simulation study. *Structural Equation Modeling*, 14(4), 535–569.

**DOI / URL.** https://doi.org/10.1080/10705510701575396

**Sample / Method.** Monte Carlo simulation across LCA, factor mixture, and growth mixture models, varying class size, separation, and sample size.

**Key claim(s).**
- BIC outperformed AIC and CAIC for class enumeration in LCA across nearly all conditions.
- The bootstrap likelihood-ratio test (BLRT) is the most consistent indicator of K, especially with small classes; LMR-LRT under-rejects.

**Takeaway.** Justifies our K-selection protocol: report BIC + ABIC + BLRT + entropy + interpretability; tie-break on BLRT for n=930.

**Confirms / Complicates / Contradicts.** Method only.

---

## D5 — Asparouhov & Muthén (2014) — three-step / BCH for distal outcomes

```yaml
id: D5
stream: D
relevance_score: 5
peer_reviewed: yes
year: 2014
tags: [LCA, BCH, three-step, distal outcomes]
verified_url: yes
```

**Citation.** Asparouhov, T., & Muthén, B. (2014). Auxiliary variables in mixture modeling: three-step approaches using Mplus. *Structural Equation Modeling*, 21(3), 329–341.

**DOI / URL.** https://doi.org/10.1080/10705511.2014.915181

**Sample / Method.** Methodological. Develops and benchmarks the BCH (Bolck–Croon–Hagenaars) and ML three-step methods for relating LCA classes to covariates and distal outcomes without re-fitting the measurement model.

**Key claim(s).**
- Naïvely regressing class-membership on covariates (one-step) lets the covariate distort the latent classes.
- BCH weights are robust against unequal class variances and outperform Lanza's method when entropy is moderate.

**Takeaway.** When we regress `org_size`, `tech_person`, `ref` on LCA class probabilities, we will use BCH weights computed from `stepmix`'s posteriors — not hard class assignment.

**Confirms / Complicates / Contradicts.** Method only — affects how F-7 / F-9 are re-tested under LCA classes.

---

## D6 — Samejima (1969) — Graded Response Model

```yaml
id: D6
stream: D
relevance_score: 4
peer_reviewed: yes
year: 1969
tags: [IRT, GRM, foundational, polytomous]
verified_url: yes
```

**Citation.** Samejima, F. (1969). Estimation of latent ability using a response pattern of graded scores. *Psychometrika Monograph Supplement*, 34(4, Pt. 2), No. 17.

**DOI / URL.** https://www.psychometricsociety.org/sites/main/files/file-attachments/mn17.pdf

**Sample / Method.** Foundational psychometric monograph. Extends the 2PL logistic model to ordered polytomous responses.

**Key claim(s).**
- For ordered Likert-type items, the GRM models cumulative response probabilities with item-specific discrimination *a* and category thresholds *b₁ < b₂ < … < bₖ*.
- Items contribute to information unevenly along θ; sum-scores discard that information.

**Takeaway.** `person_ai_comfort` (1–5), `ai_risk_reward` (with -1 broken out separately), and the `[D]` policy block are graded — GRM is the right replacement for the additive readiness index.

**Confirms / Complicates / Contradicts.** Method only — directly replaces the additive scoring used in F-9 / F-10.

---

## D7 — Birnbaum (1968) — 2PL / 3PL chapter in Lord & Novick

```yaml
id: D7
stream: D
relevance_score: 4
peer_reviewed: yes
year: 1968
tags: [IRT, 2PL, foundational, dichotomous]
verified_url: yes
```

**Citation.** Birnbaum, A. (1968). Some latent trait models and their use in inferring an examinee's ability. In F. M. Lord & M. R. Novick, *Statistical Theories of Mental Test Scores* (pp. 397–479). Reading, MA: Addison-Wesley.

**DOI / URL.** Chapter PDF: https://faculty.ucmerced.edu/jvevea/classes/290_21/readings/week%209/Birnbaum.pdf

**Sample / Method.** Foundational chapter. Introduces the 2PL and 3PL logistic IRT models.

**Key claim(s).**
- Items differ in *discrimination* (slope a) and *difficulty* (location b); summing items implicitly assumes a=1 for all.
- Test information is the sum of item information at θ — concentrated at b for high-a items.

**Takeaway.** Justifies fitting a 2PL on the binary `[U]` block (currently uses AI for…) and a separate 2PL on the `[W]` block (wants to use AI for…), then comparing latent trait means as a more honest version of count(`[U]`) vs count(`[W]`).

**Confirms / Complicates / Contradicts.** Method only.

---

## D8 — Embretson & Reise (2000) — IRT for psychologists textbook

```yaml
id: D8
stream: D
relevance_score: 5
peer_reviewed: yes
year: 2000
tags: [IRT, textbook, psychometrics]
verified_url: yes
```

**Citation.** Embretson, S. E., & Reise, S. P. (2000). *Item Response Theory for Psychologists*. Mahwah, NJ: Lawrence Erlbaum.

**DOI / URL.** https://doi.org/10.4324/9781410605269

**Sample / Method.** Textbook. Pitches IRT to applied researchers using minimum mathematics; covers 1PL/2PL/3PL/GRM, model fit (S-X², Q1), DIF, and the relationship between CTT and IRT.

**Key claim(s).**
- Person-trait estimates and item parameters are on a common scale; sum-scores conflate them.
- DIF tests whether items behave differently across groups (e.g., `ref`, `global_north_south`) at matched θ.

**Takeaway.** Textbook reference for our IRT pipeline; supplies the DIF tests we need to defend pooling Indian + non-Indian respondents on a single AI-readiness trait.

**Confirms / Complicates / Contradicts.** Method only.

---

## D9 — Reckase (2009) — Multidimensional IRT

```yaml
id: D9
stream: D
relevance_score: 4
peer_reviewed: yes
year: 2009
tags: [IRT, MIRT, multidimensional, textbook]
verified_url: yes
```

**Citation.** Reckase, M. D. (2009). *Multidimensional Item Response Theory*. New York: Springer.

**DOI / URL.** https://doi.org/10.1007/978-0-387-89976-3

**Sample / Method.** Textbook on multidimensional IRT (MIRT): compensatory and non-compensatory models, dimensionality assessment, parameter estimation, and adaptive testing.

**Key claim(s).**
- A unidimensional IRT fit to multidimensional data produces biased item parameters and misleading θ estimates.
- MIRT separates *use* from *want* from *governance* axes when items load on multiple traits.

**Takeaway.** The `[U]`, `[W]`, `[D]` blocks may not be unidimensional — Reckase's framework lets us fit a 2-3 dimensional MIRT and report whether comfort/governance/aspiration are separable factors.

**Confirms / Complicates / Contradicts.** Method only.

---

## D10 — Reise & Waller (2009) — IRT in clinical measurement

```yaml
id: D10
stream: D
relevance_score: 3
peer_reviewed: yes
year: 2009
tags: [IRT, applied, clinical psychology]
verified_url: yes
```

**Citation.** Reise, S. P., & Waller, N. G. (2009). Item response theory and clinical measurement. *Annual Review of Clinical Psychology*, 5, 27–48.

**DOI / URL.** https://doi.org/10.1146/annurev.clinpsy.032408.153553

**Sample / Method.** Review of IRT applications in clinical/personality scales (vs cognitive testing).

**Key claim(s).**
- Clinical and attitude items often have *quasi-trait* structure: most respondents cluster at one end, so item information is asymmetric.
- Sum-scores are particularly biased when items have different discrimination — exactly the case for our `[U]` block.

**Takeaway.** Survey attitude items behave like clinical items, not cognitive items — strengthens the case for GRM + Bayesian θ scoring rather than EAP-on-sum.

**Confirms / Complicates / Contradicts.** Method only.

---

## D11 — Kline (2015) — SEM textbook

```yaml
id: D11
stream: D
relevance_score: 5
peer_reviewed: yes
year: 2015
tags: [SEM, textbook, lavaan]
verified_url: yes
```

**Citation.** Kline, R. B. (2015). *Principles and Practice of Structural Equation Modeling* (4th ed.). New York: Guilford Press.

**DOI / URL.** https://www.guilford.com/books/Principles-and-Practice-of-Structural-Equation-Modeling/Rex-Kline/9781462523344

**Sample / Method.** Textbook. Covers identification, estimation (ML, WLSMV), fit indices, measurement vs structural models, mediation, and reporting standards.

**Key claim(s).**
- Two-step modeling (CFA first, then structural) is best practice; one-step risks confounding measurement and structural mis-fit.
- For categorical indicators, WLSMV with delta parameterization should be preferred over ML on tetrachoric correlations.

**Takeaway.** Anchors the Phase 6 SEM where we test whether `data_readiness` mediates `tech_person` → count(`[U]`); WLSMV in `semopy` / `lavaan` because indicators are categorical.

**Confirms / Complicates / Contradicts.** Method only.

---

## D12 — Bollen (1989) — SEM with latent variables foundational

```yaml
id: D12
stream: D
relevance_score: 4
peer_reviewed: yes
year: 1989
tags: [SEM, latent variables, foundational]
verified_url: yes
```

**Citation.** Bollen, K. A. (1989). *Structural Equations with Latent Variables*. New York: Wiley.

**DOI / URL.** https://doi.org/10.1002/9781118619179

**Sample / Method.** Foundational textbook unifying path analysis, confirmatory factor analysis, and full SEM under the LISREL parameterisation.

**Key claim(s).**
- All recursive and non-recursive structural models can be expressed as a system of three matrix equations (Λ, B, Γ).
- Identification requires t-rule + (for non-recursive) order/rank conditions.

**Takeaway.** The reference for identification arguments in Phase 6 SEM. Ensures we don't fit an under-identified mediation model.

**Confirms / Complicates / Contradicts.** Method only.

---

## D13 — Hu & Bentler (1999) — SEM fit-index cutoffs

```yaml
id: D13
stream: D
relevance_score: 4
peer_reviewed: yes
year: 1999
tags: [SEM, fit indices, RMSEA, CFI]
verified_url: yes
```

**Citation.** Hu, L.-T., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis: conventional criteria versus new alternatives. *Structural Equation Modeling*, 6(1), 1–55.

**DOI / URL.** https://doi.org/10.1080/10705519909540118

**Sample / Method.** Simulation study of model-fit cutoffs across true and mis-specified populations.

**Key claim(s).**
- Recommended joint cutoffs: SRMR ≤ .08 paired with CFI/TLI ≥ .95 or RMSEA ≤ .06.
- Single-index thresholds over-reject correctly specified models.

**Takeaway.** Sets the reporting standard for the Phase 6 SEM tables — we will report CFI, TLI, RMSEA, SRMR jointly, and acknowledge that with categorical indicators these cutoffs are conservative.

**Confirms / Complicates / Contradicts.** Method only.

---

## D14 — Oaxaca (1973) — wage decomposition foundational

```yaml
id: D14
stream: D
relevance_score: 5
peer_reviewed: yes
year: 1973
tags: [Oaxaca-Blinder, decomposition, gap analysis]
verified_url: yes
```

**Citation.** Oaxaca, R. (1973). Male-female wage differentials in urban labor markets. *International Economic Review*, 14(3), 693–709.

**DOI / URL.** https://doi.org/10.2307/2525981

**Sample / Method.** Empirical labour-economics paper analysing US 1967 wage gap, n≈30k.

**Key claim(s).**
- The mean gap between two groups can be decomposed into an *endowments* component (differences in observed X) and a *coefficients* component (differences in returns to X).
- The two halves are not unique — they depend on which group's coefficients are taken as the non-discriminatory baseline.

**Takeaway.** Direct method for the Phase 6 GN/GS gap analysis: decompose the count(`[U]`) gap into "GS orgs are smaller / have fewer specialists" vs "GS orgs get less return per unit of size/specialist".

**Confirms / Complicates / Contradicts.** Method only — operationalises the test of F-12.

---

## D15 — Blinder (1973) — wage decomposition foundational

```yaml
id: D15
stream: D
relevance_score: 5
peer_reviewed: yes
year: 1973
tags: [Oaxaca-Blinder, decomposition, foundational]
verified_url: yes
```

**Citation.** Blinder, A. S. (1973). Wage discrimination: reduced form and structural estimates. *Journal of Human Resources*, 8(4), 436–455.

**DOI / URL.** https://doi.org/10.2307/144855

**Sample / Method.** Empirical labour-economics paper, parallel to Oaxaca (1973), using 1967 PSID.

**Key claim(s).**
- A reduced-form decomposition isolates "explained" (X-driven) and "unexplained" (β-driven) portions of the gap.
- The unexplained portion subsumes both true differential treatment and unobserved-X differences.

**Takeaway.** Co-anchor with D14. Together they justify reporting *both* index-base versions of the decomposition (Phase 6).

**Confirms / Complicates / Contradicts.** Method only.

---

## D16 — Jann (2008) — `oaxaca` Stata implementation

```yaml
id: D16
stream: D
relevance_score: 4
peer_reviewed: yes
year: 2008
tags: [Oaxaca-Blinder, software, Stata]
verified_url: yes
```

**Citation.** Jann, B. (2008). The Blinder–Oaxaca decomposition for linear regression models. *The Stata Journal*, 8(4), 453–479.

**DOI / URL.** https://doi.org/10.1177/1536867X0800800401

**Sample / Method.** Software paper introducing the `oaxaca` Stata package; covers detailed decomposition, identification of categorical-variable contributions, and standard-error estimation.

**Key claim(s).**
- The detailed decomposition of categorical predictors is sensitive to the omitted category — solutions include normalisation of effects across categories.
- Closed-form delta-method standard errors and bootstrap give similar inference at moderate n.

**Takeaway.** When we port the decomposition to Python (via `linearmodels` or hand-rolled), we follow Jann's normalisation rules so that the GN/GS detailed decomposition is invariant to which `org_size` band is the reference.

**Confirms / Complicates / Contradicts.** Method only.

---

## D17 — Fortin, Lemieux, & Firpo (2011) — decomposition methods review

```yaml
id: D17
stream: D
relevance_score: 4
peer_reviewed: yes
year: 2011
tags: [decomposition, RIF, distributional, review]
verified_url: yes
```

**Citation.** Fortin, N., Lemieux, T., & Firpo, S. (2011). Decomposition methods in economics. In O. Ashenfelter & D. Card (Eds.), *Handbook of Labor Economics*, Vol. 4A (pp. 1–102). Amsterdam: Elsevier.

**DOI / URL.** https://doi.org/10.1016/S0169-7218(11)00407-2

**Sample / Method.** 102-page handbook chapter reviewing Oaxaca–Blinder, DiNardo–Fortin–Lemieux reweighting, RIF/quantile decompositions, and identification assumptions (overlapping support, ignorability).

**Key claim(s).**
- Decompositions extend beyond the mean: RIF-regression decomposes any distributional statistic (variance, Gini, quantiles).
- Reweighting estimators are equivalent to inverse-probability weighting under the same assumptions.

**Takeaway.** Lets us go past mean-gap decomposition: we can decompose the *spread* of `[U]`-counts (who's in the long tail?) using RIF regression on the 90th percentile.

**Confirms / Complicates / Contradicts.** Method only.

---

## D18 — Mercer, Lau, & Kennedy (2018) — Pew weighting study

```yaml
id: D18
stream: D
relevance_score: 5
peer_reviewed: no  # Pew methodology report
year: 2018
tags: [IPW, raking, weighting, opt-in panel]
verified_url: yes
```

**Citation.** Mercer, A., Lau, A., & Kennedy, C. (2018). *For Weighting Online Opt-In Samples, What Matters Most?* Washington, DC: Pew Research Center.

**DOI / URL.** https://www.pewresearch.org/methods/2018/01/26/for-weighting-online-opt-in-samples-what-matters-most/

**Sample / Method.** ≈30,000 opt-in panel interviews (3 vendors, 2016) reweighted under raking, propensity weighting, and matching, against a probability benchmark.

**Key claim(s).**
- Adjustment *variables* matter more than the adjustment *method*: adding political/attitudinal anchors moved point estimates ~5 points; raking vs propensity weighting barely mattered.
- Weighting cannot fully repair non-coverage in opt-in samples; bias bands remain.

**Takeaway.** Our `ref`-skewed sample (gt 549 / india 251 / tech 86 / hubs 44) is opt-in; we should rake on (a) `ref`, (b) `org_size` band, (c) `continent`, and report unweighted vs raked headlines side-by-side. Don't oversell weighted estimates.

**Confirms / Complicates / Contradicts.** Method only — sets expectations for residual bias.

---

## D19 — Valliant & Dever (2018) — survey weights handbook

```yaml
id: D19
stream: D
relevance_score: 4
peer_reviewed: yes
year: 2018
tags: [survey weights, calibration, raking]
verified_url: yes
```

**Citation.** Valliant, R., & Dever, J. A. (2018). *Survey Weights: A Step-by-Step Guide to Calculation*. College Station, TX: Stata Press.

**DOI / URL.** https://www.stata-press.com/books/survey-weights/ — review: https://doi.org/10.1177/1536867X19874261

**Sample / Method.** Applied handbook covering base weights, nonresponse adjustment, calibration (raking, post-stratification, GREG), trimming, and replicate-weight variance estimation.

**Key claim(s).**
- Trim weights at the 1st/99th percentile (or 3.5×median) to balance bias and variance.
- Replicate-weight variance estimators (jackknife, bootstrap) under-cover when classes are highly imbalanced — recommend ≥ 30 PSUs per stratum.

**Takeaway.** Operational manual for the raking step in Phase 5. Tells us to trim weights and to use rescaled bootstrap for SEs since `tech` (n=86) and `hubs` (n=44) are small.

**Confirms / Complicates / Contradicts.** Method only.

---

## D20 — Deville & Särndal (1992) — calibration estimators

```yaml
id: D20
stream: D
relevance_score: 4
peer_reviewed: yes
year: 1992
tags: [calibration, GREG, raking, foundational]
verified_url: yes
```

**Citation.** Deville, J.-C., & Särndal, C.-E. (1992). Calibration estimators in survey sampling. *Journal of the American Statistical Association*, 87(418), 376–382.

**DOI / URL.** https://doi.org/10.1080/01621459.1992.10475217

**Sample / Method.** Theoretical survey-statistics paper. Develops a unified family of calibration estimators (raking, linear, logit, truncated linear) that adjust base weights to match auxiliary-variable totals.

**Key claim(s).**
- Generalised raking is asymptotically equivalent to the GREG estimator; finite-sample differences come from bounded-vs-unbounded weight functions.
- Calibration is consistent under correct mean specification of the auxiliary model — weaker than IPW's full propensity-model assumption.

**Takeaway.** Justifies using calibration (raking on `ref` × `continent` × `org_size`) rather than full propensity-score IPW given that we have known marginals for `ref` (the survey strata) but not a true selection model.

**Confirms / Complicates / Contradicts.** Method only.

---

## D21 — AAPOR Task Force (Baker et al., 2013) — non-probability sampling

```yaml
id: D21
stream: D
relevance_score: 5
peer_reviewed: yes
year: 2013
tags: [AAPOR, nonprobability, opt-in, inference]
verified_url: yes
```

**Citation.** Baker, R., Brick, J. M., Bates, N. A., Battaglia, M., Couper, M. P., Dever, J. A., Gile, K. J., & Tourangeau, R. (2013). Summary report of the AAPOR Task Force on Non-Probability Sampling. *Journal of Survey Statistics and Methodology*, 1(2), 90–143.

**DOI / URL.** https://doi.org/10.1093/jssam/smt008 — full report: https://aapor.org/wp-content/uploads/2022/11/NPS_TF_Report_Final_7_revised_FNL_6_22_13-1.pdf

**Sample / Method.** Task-force report reviewing non-probability designs (opt-in panels, river samples, snowball, RDS, model-based) and their inferential validity.

**Key claim(s).**
- Non-probability samples can support inference under model-based or pseudo-design-based assumptions, but the inferential burden is far heavier than for probability samples.
- "Fit-for-purpose" framing: use nonprob samples for descriptive comparison, model-building, hypothesis-generation; avoid them for population point estimates without strong auxiliary data.

**Takeaway.** Sets the reporting frame for the whole study: GivingTuesday's list is non-probability; we will frame headlines as relational (gaps, ratios, conditional patterns) rather than as population point estimates of NGO AI use.

**Confirms / Complicates / Contradicts.** Method only — governs the prose tone of `REPORT.md`.

---

## D22 — Gelman & Hill (2007) — multilevel models textbook

```yaml
id: D22
stream: D
relevance_score: 5
peer_reviewed: yes
year: 2007
tags: [multilevel, hierarchical, Bayesian, textbook]
verified_url: yes
```

**Citation.** Gelman, A., & Hill, J. (2007). *Data Analysis Using Regression and Multilevel/Hierarchical Models*. New York: Cambridge University Press.

**DOI / URL.** https://www.cambridge.org/9780521686891

**Sample / Method.** Textbook covering OLS through GLMs, varying-intercept and varying-slope models, partial pooling, and Bayesian estimation.

**Key claim(s).**
- Partial pooling shrinks small-group estimates toward the grand mean — the right default when group sizes vary by an order of magnitude (our `ref` does: 549 vs 44).
- Random intercepts on `ref` (or `continent`) are nearly always preferable to fixed-effect dummies when we want to *generalise* rather than *control*.

**Takeaway.** Phase 5 baseline: every regression on `cluster3` / count(`[U]`) / θ-IRT runs as a `MixedLM` with random intercept on `ref` (and possibly on `continent`).

**Confirms / Complicates / Contradicts.** Method only — replaces the OLS / fixed-effect specifications used in F-7, F-12, F-13.

---

## D23 — Snijders & Bosker (2011) — multilevel analysis 2nd ed.

```yaml
id: D23
stream: D
relevance_score: 4
peer_reviewed: yes
year: 2011
tags: [multilevel, ICC, design effect]
verified_url: yes
```

**Citation.** Snijders, T. A. B., & Bosker, R. J. (2011). *Multilevel Analysis: An Introduction to Basic and Advanced Multilevel Modeling* (2nd ed.). London: Sage.

**DOI / URL.** https://us.sagepub.com/en-us/nam/multilevel-analysis/book234191

**Sample / Method.** Textbook. Detailed treatment of variance components, ICC, design effect (DEFF), centring (group-mean vs grand-mean), and multilevel logistic regression.

**Key claim(s).**
- DEFF = 1 + (n̄ − 1)·ICC; with our `ref` clusters this can inflate effective sample size penalties by 2–4×.
- Group-mean centering separates within-cluster from between-cluster effects, which matters if `tech_person` rates differ across `ref` strata.

**Takeaway.** Justifies reporting ICC by `ref` for every key outcome; flags when between-`ref` variation dwarfs within-`ref` variation (big effects on inference).

**Confirms / Complicates / Contradicts.** Method only.

---

## D24 — Raudenbush & Bryk (2002) — HLM canonical

```yaml
id: D24
stream: D
relevance_score: 3
peer_reviewed: yes
year: 2002
tags: [HLM, multilevel, education research]
verified_url: yes
```

**Citation.** Raudenbush, S. W., & Bryk, A. S. (2002). *Hierarchical Linear Models: Applications and Data Analysis Methods* (2nd ed.). Thousand Oaks, CA: Sage.

**DOI / URL.** https://us.sagepub.com/en-us/nam/hierarchical-linear-models/book9230

**Sample / Method.** Canonical HLM textbook covering 2-level and 3-level models, growth curves, cross-classified models, and HGLM for binary/count outcomes.

**Key claim(s).**
- Cross-classified random effects (e.g., `ref` × `continent` non-nested) require specialised estimation but are necessary when both groupings affect outcomes.
- Empirical-Bayes class means are more reliable than OLS group means for small clusters.

**Takeaway.** If we treat `ref` and `continent` as cross-classified (an India respondent can come from `india` *and* Asia), we need cross-classified random effects, not nested.

**Confirms / Complicates / Contradicts.** Method only.

---

## D25 — Rao & Molina (2015) — small-area estimation

```yaml
id: D25
stream: D
relevance_score: 3
peer_reviewed: yes
year: 2015
tags: [small area estimation, EBLUP, Fay-Herriot]
verified_url: yes
```

**Citation.** Rao, J. N. K., & Molina, I. (2015). *Small Area Estimation* (2nd ed.). Hoboken, NJ: Wiley.

**DOI / URL.** https://doi.org/10.1002/9781118735855

**Sample / Method.** Comprehensive textbook on direct, synthetic, composite, and model-based (Fay-Herriot, unit-level) small-area estimators with mean-squared-error estimation.

**Key claim(s).**
- For sub-domains with small n (our African regions, India states), direct estimates have unreliable variances; Fay-Herriot models borrow strength from area-level covariates.
- EBLUP MSE estimation needs Prasad-Rao or jackknife adjustment to be unbiased.

**Takeaway.** Lets us produce stable estimates for `af_region` (n≈60 split across regions) and `india_state` (n=251 split across many states) by linking to area-level covariates, rather than reporting unstable cell means.

**Confirms / Complicates / Contradicts.** Method only.

---

## D26 — Le Roux & Rouanet (2010) — Multiple Correspondence Analysis

```yaml
id: D26
stream: D
relevance_score: 3
peer_reviewed: yes
year: 2010
tags: [MCA, geometric data analysis, categorical]
verified_url: yes
```

**Citation.** Le Roux, B., & Rouanet, H. (2010). *Multiple Correspondence Analysis*. Quantitative Applications in the Social Sciences No. 163. Thousand Oaks, CA: Sage.

**DOI / URL.** https://doi.org/10.4135/9781412993906

**Sample / Method.** Methodological monograph in the QASS series. Develops MCA as geometric data analysis: respondents and modalities are points in a Euclidean space, axes interpreted via contributions and squared cosines.

**Key claim(s).**
- MCA on indicator matrices recovers latent structure for purely categorical surveys; equivalent to PCA on a re-scaled Burt matrix.
- Supplementary variables (projected post-hoc) preserve unbiased axis interpretation.

**Takeaway.** Phase 5 visualisation: MCA on the `[U]` ∪ `[W]` ∪ `[D]` indicator block gives a 2-D map where `cluster3` / LCA classes are projected as supplementary points — directly interpretable axes.

**Confirms / Complicates / Contradicts.** Method only.

---

## D27 — Greenacre (2017) — Correspondence Analysis in Practice

```yaml
id: D27
stream: D
relevance_score: 3
peer_reviewed: yes
year: 2017
tags: [MCA, CA, applied, visualization]
verified_url: yes
```

**Citation.** Greenacre, M. (2017). *Correspondence Analysis in Practice* (3rd ed.). Boca Raton, FL: Chapman & Hall / CRC.

**DOI / URL.** https://doi.org/10.1201/9781315369983

**Sample / Method.** Applied textbook with worked examples in the social, environmental, marketing, and linguistic sciences; covers CA, MCA, joint correspondence analysis, subset MCA, and stability assessment via bootstrap.

**Key claim(s).**
- Inertia adjustment (Benzécri, Greenacre) corrects MCA's well-known under-statement of explained variance.
- Subset MCA lets us focus axes on a question block (e.g., `[U]` only) while keeping the full coding for projection.

**Takeaway.** Operational guide for the MCA in Phase 5; we will report adjusted inertia and bootstrap stability for the first 2 axes.

**Confirms / Complicates / Contradicts.** Method only.

---

## D28 — Benjamini & Hochberg (1995) — FDR foundational

```yaml
id: D28
stream: D
relevance_score: 5
peer_reviewed: yes
year: 1995
tags: [multiple testing, FDR, BH procedure]
verified_url: yes
```

**Citation.** Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: a practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society, Series B*, 57(1), 289–300.

**DOI / URL.** https://doi.org/10.1111/j.2517-6161.1995.tb02031.x

**Sample / Method.** Foundational statistics paper. Defines the false discovery rate (FDR) as the expected proportion of false rejections among rejections, and derives the BH step-up procedure.

**Key claim(s).**
- BH controls FDR at level q under independence and positive regression dependence (PRDS).
- BH dominates FWER procedures (Bonferroni, Holm) in power when many hypotheses are true alternatives.

**Takeaway.** Across the ~25 paired-task `[W]−[U]` tests + ~30 subgroup sweeps in Phase 5, we use BH at q = 0.05 — exactly the procedure the archived `lib.fdr_adjust` already implements.

**Confirms / Complicates / Contradicts.** Method only — supports the multiple-testing posture of the archived findings.

---

## D29 — Baron & Kenny (1986) — mediation foundational

```yaml
id: D29
stream: D
relevance_score: 4
peer_reviewed: yes
year: 1986
tags: [mediation, foundational, social psychology]
verified_url: yes
```

**Citation.** Baron, R. M., & Kenny, D. A. (1986). The moderator–mediator variable distinction in social psychological research: conceptual, strategic, and statistical considerations. *Journal of Personality and Social Psychology*, 51(6), 1173–1182.

**DOI / URL.** https://doi.org/10.1037/0022-3514.51.6.1173

**Sample / Method.** Conceptual / methodological article. Lays out the four-step "causal-steps" test for mediation.

**Key claim(s).**
- Mediation requires (i) X → Y, (ii) X → M, (iii) M → Y | X, (iv) X → Y attenuated by M.
- Distinguishes mediation (mechanism) from moderation (interaction).

**Takeaway.** Historical anchor; superseded by D30 (MacKinnon) and D31 (Imai) for inference and identification, but still the language reviewers use.

**Confirms / Complicates / Contradicts.** Method only — we cite it for vocabulary, not for inference.

---

## D30 — MacKinnon (2008) — mediation analysis textbook

```yaml
id: D30
stream: D
relevance_score: 4
peer_reviewed: yes
year: 2008
tags: [mediation, bootstrap, indirect effects]
verified_url: yes
```

**Citation.** MacKinnon, D. P. (2008). *Introduction to Statistical Mediation Analysis*. New York: Routledge.

**DOI / URL.** https://doi.org/10.4324/9780203809556

**Sample / Method.** Textbook. Covers single-mediator, multi-mediator, multilevel, and longitudinal mediation; emphasises bootstrap CIs for the indirect effect ab.

**Key claim(s).**
- Sobel-test SEs are biased downward; percentile bootstrap (≥ 5,000 reps) gives correct coverage for ab.
- Causal-steps "stepwise significance" inflates Type II error — test the indirect effect directly.

**Takeaway.** For the H11 mediation test (`tech_person` → `data_readiness` → `[U]`-count), we will report bootstrap (10k reps) percentile CIs for ab, not Sobel.

**Confirms / Complicates / Contradicts.** Method only — operationalises the H11 test.

---

## D31 — Imai, Keele, & Tingley (2010) — causal mediation + sensitivity

```yaml
id: D31
stream: D
relevance_score: 5
peer_reviewed: yes
year: 2010
tags: [mediation, causal, sensitivity, sequential ignorability]
verified_url: yes
```

**Citation.** Imai, K., Keele, L., & Tingley, D. (2010). A general approach to causal mediation analysis. *Psychological Methods*, 15(4), 309–334.

**DOI / URL.** https://doi.org/10.1037/a0020761

**Sample / Method.** Methodological paper formalising mediation under the potential-outcomes framework and providing nonparametric estimators plus a closed-form sensitivity analysis (ρ).

**Key claim(s).**
- The Average Causal Mediation Effect (ACME) is identified under *sequential ignorability* — a strong, untestable assumption.
- The sensitivity parameter ρ (correlation of M, Y residuals) bounds how large unmeasured M-Y confounding must be to overturn the ACME.

**Takeaway.** Critical for honesty on H11: with observational data we *cannot* claim causal mediation without acknowledging the sequential-ignorability assumption. Phase 6 will report the ACME and the ρ at which the indirect effect → 0.

**Confirms / Complicates / Contradicts.** Method only — sets the inferential ceiling for the mediation finding.

---

## D32 — Hayes (2017) — PROCESS / conditional process analysis

```yaml
id: D32
stream: D
relevance_score: 3
peer_reviewed: yes
year: 2017
tags: [mediation, moderation, PROCESS]
verified_url: yes
```

**Citation.** Hayes, A. F. (2017). *Introduction to Mediation, Moderation, and Conditional Process Analysis: A Regression-Based Approach* (2nd ed.). New York: Guilford Press.

**DOI / URL.** https://www.guilford.com/books/Introduction-to-Mediation-Moderation-and-Conditional-Process-Analysis/Andrew-Hayes/9781462534654

**Sample / Method.** Applied textbook documenting the PROCESS macro for SPSS / SAS / R.

**Key claim(s).**
- "Conditional process" models combine mediation and moderation: indirect effect of X on Y through M, conditional on a moderator W.
- Bootstrap CIs for the *index of moderated mediation* test whether the indirect effect varies across W.

**Takeaway.** If `org_size` moderates the `tech_person` → `data_readiness` → `[U]` chain (plausible — small orgs with a tech person should benefit more), the index of moderated mediation is the right test.

**Confirms / Complicates / Contradicts.** Method only.

---

## D33 — Holland (1986) — statistics and causal inference

```yaml
id: D33
stream: D
relevance_score: 3
peer_reviewed: yes
year: 1986
tags: [causal inference, potential outcomes, foundational]
verified_url: yes
```

**Citation.** Holland, P. W. (1986). Statistics and causal inference. *Journal of the American Statistical Association*, 81(396), 945–960.

**DOI / URL.** https://doi.org/10.1080/01621459.1986.10478354

**Sample / Method.** Methodological essay. Introduces the term "Rubin Causal Model" and articulates the fundamental problem of causal inference (we never see both potential outcomes for the same unit).

**Key claim(s).**
- "No causation without manipulation" — attributes that cannot be intervened on (e.g., `continent`) cannot be causes in the RCM sense.
- Statistics should distinguish associational from causal claims explicitly.

**Takeaway.** Frames the limits on Phase 6 mediation/decomposition language: we say "the size-coefficient component of the GN/GS gap" rather than "size *causes* the GN/GS gap".

**Confirms / Complicates / Contradicts.** Method only — disciplines the writeup.

---

## D34 — Rosenbaum & Rubin (1983) — propensity scores

```yaml
id: D34
stream: D
relevance_score: 4
peer_reviewed: yes
year: 1983
tags: [propensity score, IPW, observational, foundational]
verified_url: yes
```

**Citation.** Rosenbaum, P. R., & Rubin, D. B. (1983). The central role of the propensity score in observational studies for causal effects. *Biometrika*, 70(1), 41–55.

**DOI / URL.** https://doi.org/10.1093/biomet/70.1.41

**Sample / Method.** Foundational methodological paper. Proves that the propensity score e(X) = Pr(T=1 | X) is a balancing score: conditional on e(X), treatment is independent of observed covariates.

**Key claim(s).**
- Adjustment on the scalar e(X) suffices to remove bias from all observed X under unconfoundedness.
- Stratification on quintiles of e(X) removes ~90 % of bias due to observed covariates.

**Takeaway.** Underlies our IPW reweighting alternative to raking when we want to compare matched-on-X subgroups (e.g., India vs non-India at matched `org_size` × `tech_person` — the F-5 setup).

**Confirms / Complicates / Contradicts.** Method only.

---

## D35 — Mimno et al. (2011) — topic-coherence metric

```yaml
id: D35
stream: D
relevance_score: 5
peer_reviewed: yes
year: 2011
tags: [topic models, coherence, evaluation, BERTopic]
verified_url: yes
```

**Citation.** Mimno, D., Wallach, H. M., Talley, E., Leenders, M., & McCallum, A. (2011). Optimizing semantic coherence in topic models. *Proceedings of EMNLP 2011*, 262–272.

**DOI / URL.** https://aclanthology.org/D11-1024/

**Sample / Method.** Empirical paper proposing UMass coherence (log conditional co-document frequency over top-N words) and evaluating against expert ratings.

**Key claim(s).**
- Held-out perplexity correlates *negatively* with human topic-quality judgements past a point — i.e., better fit ≠ more interpretable.
- UMass / NPMI coherence on top-10 words tracks human ratings closely and is computable from the training corpus alone.

**Takeaway.** For the BERTopic pass over `org_opentext` / `ai_opentext` / `non_data_work`, we report c_v and NPMI coherence on top-10 words instead of (or alongside) perplexity / silhouette.

**Confirms / Complicates / Contradicts.** Method only.

---

## D36 — Chang et al. (2009) — "Reading Tea Leaves"

```yaml
id: D36
stream: D
relevance_score: 4
peer_reviewed: yes
year: 2009
tags: [topic models, evaluation, human judgement]
verified_url: yes
```

**Citation.** Chang, J., Boyd-Graber, J., Gerrish, S., Wang, C., & Blei, D. M. (2009). Reading tea leaves: how humans interpret topic models. *Advances in Neural Information Processing Systems* 22 (NeurIPS 2009), 288–296.

**DOI / URL.** https://papers.nips.cc/paper/3700-reading-tea-leaves-how-humans-interpret-topic-models

**Sample / Method.** Empirical paper introducing the *word-intrusion* and *topic-intrusion* tasks for human topic-model evaluation.

**Key claim(s).**
- Held-out likelihood is *anti-correlated* with topic interpretability — a model can fit well and still produce semantically incoherent topics.
- Word-intrusion accuracy gives a sample-efficient human benchmark.

**Takeaway.** We will run a small word-intrusion check on Phase 5 BERTopic outputs (a few co-authors rate top-10 words for each topic) before reporting topics in `REPORT.md`.

**Confirms / Complicates / Contradicts.** Method only.

---

## Stream D synthesis

The methodological state-of-the-art for a survey of this size and design (n=930, mostly categorical, opt-in, multi-source) prescribes a specific pipeline that diverges from the archived 4-hour pass on six fronts.

**(1) Typology.** K-means (D1's straw-man) and HDBSCAN are replaced by a Bernoulli LCA on the `[U]/[W]/[D]` block (D1, D2, D3), with K chosen by joint BIC + BLRT + entropy (D4) and downstream covariate regressions run via three-step BCH (D5) so that posterior class membership isn't distorted by predictors.

**(2) Latent traits.** The additive readiness index that drove F-9 / F-10 is replaced by a 2PL on the binary `[U]` block (D7), a GRM on the graded `person_ai_comfort` and `[D]` items (D6), with applied scaffolding from Embretson & Reise (D8), Reckase's MIRT for the `[U]` × `[W]` × `[D]` cross-block (D9), and Reise & Waller's clinical-IRT cautions (D10) about quasi-trait skew.

**(3) Decomposition and gap analysis.** GN/GS and India/non-India gaps are decomposed via Oaxaca–Blinder (D14, D15) using Jann's normalisation (D16) for categorical variables, with Fortin/Lemieux/Firpo (D17) RIF regression as the distributional extension when we care about the long tail of `[U]`-counts rather than the mean.

**(4) Inference under non-probability sampling.** AAPOR's task-force (D21) governs reporting tone: we frame results as relational, not population-representative. `ref` skew is addressed by raking on (`ref` × `org_size` × `continent`) marginals via Deville–Särndal calibration (D20), following Mercer/Lau/Kennedy's (D18) finding that adjustment variables matter more than method, and Valliant–Dever's (D19) operational rules for trimming and replicate-weight variance. Propensity-score IPW (D34) is the alternative when we want matched comparisons rather than population calibration.

**(5) Multilevel structure.** Every regression on `cluster3` / count(`[U]`) / θ-IRT runs as a `MixedLM` with random intercept on `ref` and possibly cross-classified with `continent` (D22, D23, D24). For sub-domains (`af_region`, `india_state`) where direct estimates are unstable, Fay-Herriot small-area models (D25) borrow strength from area-level covariates.

**(6) Mediation, multiple testing, free text.** SEM (D11, D12) with Hu/Bentler cutoffs (D13) tests the H11 mediation chain `tech_person` → data_readiness → `[U]`; bootstrap indirect effects follow MacKinnon (D30); causal interpretation is bounded by Imai–Keele–Tingley sensitivity ρ (D31), with Holland (D33) disciplining the prose. Conditional-process moderation (D32) tests `org_size` × `tech_person` interactions on the indirect path. All sweeps go through BH-FDR at q=0.05 (D28). MCA (D26) with adjusted inertia (D27) provides a 2-D visual map of the indicator space, and BERTopic free-text topics are evaluated by NPMI coherence (D35) and a small word-intrusion check (D36) before being reported. Where mediation language is invoked colloquially, Baron–Kenny (D29) provides only the vocabulary, not the inference.

The takeaway: roughly half the archived findings (F-1, F-3, F-7, F-9, F-12) need to be re-tested under this stack, not merely re-described. Phase 5/6 keeps the headline of the inversion / size-dominance / null-on-cluster3 findings, but expects the *quantitative* claims to shift — likely smaller effects after multilevel + raking + LCA reassignment, with new effects emerging from MIRT and Oaxaca–Blinder that the additive index couldn't see.
