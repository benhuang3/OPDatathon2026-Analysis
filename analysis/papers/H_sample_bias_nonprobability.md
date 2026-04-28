# Stream H — Sample bias, non-probability surveys, and convenience-sample inference

Paper-cards for prior work on inference from non-probability and convenience samples — directly relevant to the GivingTuesday 2024 sample (n=930, four self-selected sub-frames: `gt` 549, `india` 251, `tech` 86, `hubs` 44) and to Phase 5/6's planned IPW reweighting and `ref`-as-random-intercept robustness checks.

---

## H1 — Baker et al. (2013) — AAPOR Task Force on Non-probability Sampling

```yaml
id: H1
stream: H
relevance_score: 5
peer_reviewed: yes
year: 2013
tags: [AAPOR, non-probability, total-survey-error, foundational]
verified_url: yes
```

**Citation.** Baker, R., Brick, J. M., Bates, N. A., Battaglia, M., Couper, M. P., Dever, J. A., Gile, K. J., & Tourangeau, R. (2013). Summary report of the AAPOR Task Force on Non-probability Sampling. *Journal of Survey Statistics and Methodology*, 1(2), 90–143.

**DOI / URL.** https://doi.org/10.1093/jssam/smt008 (https://academic.oup.com/jssam/article-abstract/1/2/90/941418)

**Sample / Method.** Task-force literature synthesis commissioned by AAPOR Executive Council (2011); reviews case-control, intercept, opt-in panel, and river-sample designs against the Total Survey Error framework.

**Key claim(s).**
- Non-probability designs do not fit the TSE framework cleanly; "fit-for-purpose" is the right standard.
- All inference from such samples is **model-dependent**; transparency about the model and the auxiliary variables used to weight is essential.
- Quasi-randomization (propensity-score) and superpopulation modeling are the two defensible inferential approaches.

**Takeaway for this dataset.** The GivingTuesday sample is exactly the kind of multi-source opt-in design Baker et al. describe; their playbook (declare the inferential model, weight to known auxiliaries, report sensitivity) is the template for our Phase 5 IPW pass.

**Confirms / Complicates / Contradicts.** Confirms our methodological plan for Phase 5: IPW + random-intercept on `ref` is the AAPOR-endorsed minimum.

---

## H2 — Baker et al. (2010) — AAPOR Research Synthesis on Online Panels

```yaml
id: H2
stream: H
relevance_score: 5
peer_reviewed: yes
year: 2010
tags: [AAPOR, online-panels, opt-in, foundational]
verified_url: yes
```

**Citation.** Baker, R., Blumberg, S. J., Brick, J. M., Couper, M. P., Courtright, M., Dennis, J. M., Dillman, D., Frankel, M. R., Garland, P., Groves, R. M., Kennedy, C., Krosnick, J., Lavrakas, P. J., Lee, S., Link, M., Piekarski, L., Rao, K., Thomas, R. K., & Zahs, D. (2010). Research synthesis: AAPOR report on online panels. *Public Opinion Quarterly*, 74(4), 711–781.

**DOI / URL.** https://doi.org/10.1093/poq/nfq048 (https://academic.oup.com/poq/article-abstract/74/4/711/1832222)

**Sample / Method.** Task-force review (commissioned 2008) of empirical literature on opt-in online panels through ~2010.

**Key claim(s).**
- Opt-in panel members are systematically more politically engaged, more wired, and more "professional respondent"-like than the general public.
- Demographic-only weights typically fail to remove the bias; attitudinal/behavioural auxiliaries are needed.

**Takeaway for this dataset.** Self-selected NGO recruits (especially `tech` n=86, `hubs` n=44) are likely more digitally sophisticated than the average global NGO — suggesting our `person_ai_comfort` and `tech_person` distributions are shifted right relative to any plausible population.

**Confirms / Complicates / Contradicts.** Complicates raw F-7 (size-and-tech-staff dominance): some of the "size effect" may itself be selection into the panel.

---

## H3 — Cornesse et al. (2020) — Probability vs Non-Probability Survey Research Review

```yaml
id: H3
stream: H
relevance_score: 5
peer_reviewed: yes
year: 2020
tags: [non-probability, accuracy, review, IPW]
verified_url: yes
```

**Citation.** Cornesse, C., Blom, A. G., Dutwin, D., Krosnick, J. A., De Leeuw, E. D., Legleye, S., Pasek, J., Pennay, D., Phillips, B., Sakshaug, J. W., Struminskaya, B., & Wenz, A. (2020). A review of conceptual approaches and empirical evidence on probability and nonprobability sample survey research. *Journal of Survey Statistics and Methodology*, 8(1), 4–36.

**DOI / URL.** https://doi.org/10.1093/jssam/smz041

**Sample / Method.** Systematic review of empirical comparisons between probability and non-probability sample surveys across multiple countries and topics.

**Key claim(s).**
- Across every reviewed comparison, probability samples produced more accurate point estimates than non-probability samples — even after post-stratification.
- Adjustment can shrink but rarely eliminate non-probability bias; sample-specific selection mechanisms matter more than weighting cleverness.

**Takeaway for this dataset.** Tells us not to over-claim the "after IPW, F-1 still holds" result. Even after weighting, residual bias is the modal finding.

**Confirms / Complicates / Contradicts.** Complicates the strength of any "headline holds after reweighting" claim — it's necessary, not sufficient.

---

## H4 — Park, Gelman & Bafumi (2004) — MRP Foundational Paper

```yaml
id: H4
stream: H
relevance_score: 5
peer_reviewed: yes
year: 2004
tags: [MRP, multilevel, poststratification, Bayesian]
verified_url: yes
```

**Citation.** Park, D. K., Gelman, A., & Bafumi, J. (2004). Bayesian multilevel estimation with poststratification: State-level estimates from national polls. *Political Analysis*, 12(4), 375–385.

**DOI / URL.** https://doi.org/10.1093/pan/mph024 (https://www.cambridge.org/core/journals/political-analysis/article/abs/bayesian-multilevel-estimation-with-poststratification-statelevel-estimates-from-national-polls/22A5EF78D027E76C782B3280D400FCC9)

**Sample / Method.** Multilevel logistic regression on 1988/1992 US pre-election polls; cells defined by state × demographics; validated against actual state vote shares.

**Key claim(s).**
- Partial pooling across small cells produces sub-population estimates that beat raw cell means and design weighting.
- The MRP machinery generalizes: any sub-population estimate can be reweighted to a known auxiliary marginal.

**Takeaway for this dataset.** With n=930 across 4 source frames and several country sub-buckets, raw subgroup means are noisy. MRP-style partial pooling on `ref × continent × org_size` is the right small-area extension after Phase 6's multilevel models.

**Confirms / Complicates / Contradicts.** Confirms the Phase 6 plan to use random intercepts on `ref` rather than fixed-effect dummies.

---

## H5 — Wang, Rothschild, Goel & Gelman (2015) — Forecasting Elections with Non-Representative Polls

```yaml
id: H5
stream: H
relevance_score: 5
peer_reviewed: yes
year: 2015
tags: [MRP, non-probability, Xbox, forecasting]
verified_url: yes
```

**Citation.** Wang, W., Rothschild, D., Goel, S., & Gelman, A. (2015). Forecasting elections with non-representative polls. *International Journal of Forecasting*, 31(3), 980–991.

**DOI / URL.** https://doi.org/10.1016/j.ijforecast.2014.06.001

**Sample / Method.** Daily Xbox gaming-platform survey (n≈350,000 responses, drastically non-representative — heavily young/male/white/conservative-leaning); MRP applied to recover state-level 2012 vote intent.

**Key claim(s).**
- A massively biased convenience sample (Xbox users) recovered the 2012 election outcome with accuracy comparable to gold-standard probability polls — *because* the MRP model included the right auxiliaries.
- Non-representativeness is recoverable when (a) the auxiliaries that explain selection also explain the outcome and (b) reliable benchmark marginals exist.

**Takeaway for this dataset.** The encouraging case for our IPW pass: even a 7×-skewed sample (Xbox vs US population) can yield valid inference *when the right covariates are weighted on*. The hard case for us: we lack a clean global-NGO benchmark for the marginals we'd most want to weight on (org size × country × budget).

**Confirms / Complicates / Contradicts.** Confirms feasibility of the IPW approach; complicates it because we lack Wang et al.'s benchmark quality.

---

## H6 — Mercer, Lau & Kennedy (2018) — Pew "What Matters Most for Weighting Online Opt-In Samples"

```yaml
id: H6
stream: H
relevance_score: 5
peer_reviewed: no  # Pew Research methodological report
year: 2018
tags: [Pew, raking, propensity, opt-in, weighting]
verified_url: yes
```

**Citation.** Mercer, A., Lau, A., & Kennedy, C. (2018). *For weighting online opt-in samples, what matters most?* Pew Research Center, January 26, 2018.

**DOI / URL.** https://www.pewresearch.org/methods/2018/01/26/for-weighting-online-opt-in-samples-what-matters-most/

**Sample / Method.** ≈30,000 interviews across three opt-in panel vendors (June–July 2016); benchmarked against ACS and CPS; tested raking, propensity weighting, and matching with two adjustment-variable sets (basic demographics; demographics + political).

**Key claim(s).**
- Including non-demographic, **substantively predictive** auxiliaries (here: party ID, voter registration, ideology) reduced bias more than adding more demographics.
- Propensity weighting was never strictly better than raking in their tests — simpler methods are competitive when the right variables are used.
- All methods left meaningful residual bias on most estimates.

**Takeaway for this dataset.** For the GivingTuesday IPW pass, the "right" auxiliaries are likely org-size and country (which we have on the benchmark side via NCCS / Candid for the US slice), and possibly digital-maturity proxies — not just region.

**Confirms / Complicates / Contradicts.** Confirms our plan to weight on org-size/country. Complicates: even the best-weighted opt-in still misses on substantive estimates, so we must report unweighted + weighted side by side.

---

## H7 — Couper (2000) — Web Surveys: Issues and Approaches

```yaml
id: H7
stream: H
relevance_score: 4
peer_reviewed: yes
year: 2000
tags: [web-survey, coverage, foundational, typology]
verified_url: yes
```

**Citation.** Couper, M. P. (2000). Review: Web surveys: A review of issues and approaches. *Public Opinion Quarterly*, 64(4), 464–494.

**DOI / URL.** https://doi.org/10.1086/318641

**Sample / Method.** Conceptual review proposing a typology of web survey designs (probability vs non-probability; list-based vs intercept vs panel).

**Key claim(s).**
- Web surveys vary by *orders of magnitude* in inferential validity depending on the recruitment frame.
- Coverage error from internet access remains the dominant concern in non-probability web designs.

**Takeaway for this dataset.** Locates the GivingTuesday survey unambiguously in Couper's "self-selected web survey" type — the type with the weakest a priori inference guarantee.

**Confirms / Complicates / Contradicts.** Complicates any naive generalization from n=930 to "the global NGO sector".

---

## H8 — Bethlehem (2010) — Selection Bias in Web Surveys

```yaml
id: H8
stream: H
relevance_score: 5
peer_reviewed: yes
year: 2010
tags: [web-survey, self-selection, weighting, reference-survey]
verified_url: yes
```

**Citation.** Bethlehem, J. (2010). Selection bias in web surveys. *International Statistical Review*, 78(2), 161–188.

**DOI / URL.** https://doi.org/10.1111/j.1751-5823.2010.00112.x

**Sample / Method.** Theoretical decomposition of web-survey bias into under-coverage and self-selection components, with simulation and adjustment-weight evaluations.

**Key claim(s).**
- Under-coverage bias may attenuate over time as internet access converges; self-selection bias does not.
- Adjustment weighting against a probability "reference survey" is the most defensible correction — but only as good as the auxiliaries it uses.

**Takeaway for this dataset.** The GivingTuesday sample's two main bias sources differ by sub-frame: `india` likely has under-coverage; `gt`/`tech`/`hubs` are dominated by self-selection. Our IPW must address both — which is why a single global weight scheme will be insufficient.

**Confirms / Complicates / Contradicts.** Confirms the need for stream-level (per-`ref`) sensitivity, not just a global weight.

---

## H9 — Yeager, Krosnick et al. (2011) — Probability vs Non-Probability Accuracy Comparison

```yaml
id: H9
stream: H
relevance_score: 4
peer_reviewed: yes
year: 2011
tags: [probability, non-probability, benchmarking, accuracy]
verified_url: yes
```

**Citation.** Yeager, D. S., Krosnick, J. A., Chang, L., Javitz, H. S., Levendusky, M. S., Simpser, A., & Wang, R. (2011). Comparing the accuracy of RDD telephone surveys and Internet surveys conducted with probability and non-probability samples. *Public Opinion Quarterly*, 75(4), 709–747.

**DOI / URL.** https://doi.org/10.1093/poq/nfr020

**Sample / Method.** Parallel-deployment study: identical questionnaire fielded across multiple probability and non-probability internet vendors plus RDD telephone; benchmarked against gold-standard government statistics on demographics and behaviours.

**Key claim(s).**
- Probability samples were uniformly more accurate than non-probability samples on benchmarked items, even after post-stratification.
- Non-probability sample bias was heterogeneous across vendors — there is no generic "opt-in error".

**Takeaway for this dataset.** Re-emphasizes that the four `ref` sub-frames in our data are not interchangeable; each may have its own bias signature.

**Confirms / Complicates / Contradicts.** Complicates pooling across `ref` without random intercepts.

---

## H10 — Schonlau, van Soest, Kapteyn & Couper (2009) — Selection Bias in Web Surveys & Propensity Scores

```yaml
id: H10
stream: H
relevance_score: 4
peer_reviewed: yes
year: 2009
tags: [web-survey, propensity-score, self-selection, HRS]
verified_url: yes
```

**Citation.** Schonlau, M., van Soest, A., Kapteyn, A., & Couper, M. P. (2009). Selection bias in web surveys and the use of propensity scores. *Sociological Methods & Research*, 37(3), 291–318.

**DOI / URL.** https://doi.org/10.1177/0049124108327128

**Sample / Method.** Health and Retirement Study sub-sample (US 50+) where the internet-using subset is a probability draw, allowing direct measurement of web-only bias and the curative power of propensity adjustment.

**Key claim(s).**
- Mean bias across estimands fell from 6.5% to 3.7% after propensity adjustment — non-trivial but partial.
- Education + income alone are insufficient adjustments for behaviorally complex outcomes (e.g., stock ownership).

**Takeaway for this dataset.** A direct prior: simple demographic-only IPW will only cut, not eliminate, bias on AI-related measures, because the variables that select people into a digital NGO list also predict AI comfort.

**Confirms / Complicates / Contradicts.** Complicates the headline robustness check — IPW reduces but cannot guarantee away selection bias in F-1.

---

## H11 — Lee & Valliant (2009) — Propensity + Calibration for Volunteer Web Panels

```yaml
id: H11
stream: H
relevance_score: 4
peer_reviewed: yes
year: 2009
tags: [propensity, calibration, web-panel, variance]
verified_url: yes
```

**Citation.** Lee, S., & Valliant, R. (2009). Estimation for volunteer panel web surveys using propensity score adjustment and calibration adjustment. *Sociological Methods & Research*, 37(3), 319–343.

**DOI / URL.** https://doi.org/10.1177/0049124108329643

**Sample / Method.** Methodological paper deriving and simulating a two-stage weighting scheme (propensity → calibration) for opt-in panel data; compares three variance estimators including jackknife replication.

**Key claim(s).**
- Propensity adjustment first, then calibration to known marginals, improves on either alone.
- Standard linearization variance estimators understate uncertainty; replicate methods (jackknife) are recommended.

**Takeaway for this dataset.** Specifies the recipe for Phase 5: estimate `ref`-membership propensities, then calibrate to NCCS/Candid marginals where available; report jackknife or bootstrap CIs.

**Confirms / Complicates / Contradicts.** Confirms the two-stage IPW + calibration design.

---

## H12 — Elliott & Valliant (2017) — Inference for Nonprobability Samples

```yaml
id: H12
stream: H
relevance_score: 5
peer_reviewed: yes
year: 2017
tags: [non-probability, inference, quasi-randomization, superpopulation]
verified_url: yes
```

**Citation.** Elliott, M. R., & Valliant, R. (2017). Inference for nonprobability samples. *Statistical Science*, 32(2), 249–264.

**DOI / URL.** https://doi.org/10.1214/16-STS598

**Sample / Method.** Methodological review distinguishing two paradigms — quasi-randomization (estimate pseudo-inclusion probabilities from covariates) and superpopulation modeling (predict outcomes for non-sampled units).

**Key claim(s).**
- The two paradigms make different assumptions; researchers should pick consciously.
- Both require an *external benchmark dataset* with the same auxiliaries — not just population marginals.

**Takeaway for this dataset.** Quasi-randomization (IPW) is feasible only to the extent we have a benchmark with `org_size`, `country`, `budget` for global NGOs; the absence of one is the single biggest threat to a clean Phase 5.

**Confirms / Complicates / Contradicts.** Confirms the inferential framework; flags benchmark availability as the binding constraint.

---

## H13 — Buelens, Burger & van den Brakel (2018) — Comparing Inference Methods for Non-Probability Samples

```yaml
id: H13
stream: H
relevance_score: 4
peer_reviewed: yes
year: 2018
tags: [non-probability, machine-learning, predictive-inference, simulation]
verified_url: yes
```

**Citation.** Buelens, B., Burger, J., & van den Brakel, J. A. (2018). Comparing inference methods for non-probability samples. *International Statistical Review*, 86(2), 322–343.

**DOI / URL.** https://doi.org/10.1111/insr.12253

**Sample / Method.** Simulation study using Dutch vehicle-mileage administrative data; benchmarks IPW, calibration, regression imputation, and ML predictive methods (random forests, boosting).

**Key claim(s).**
- ML-based predictive inference can dominate classical IPW when the selection mechanism is highly non-linear in observable covariates.
- No single method dominates uniformly; method choice should follow from the diagnosed selection mechanism.

**Takeaway for this dataset.** Suggests we should also try a model-based prediction sensitivity check (e.g., XGBoost predicting AI-use patterns conditional on a benchmark covariate set) alongside IPW.

**Confirms / Complicates / Contradicts.** Extends Phase 5 with an additional ML-based robustness option.

---

## H14 — Couper (2017) — Birth and Diffusion of the Concept of Paradata

```yaml
id: H14
stream: H
relevance_score: 2
peer_reviewed: no  # journal article in JASR (Japanese Association for Survey Research)
year: 2017
tags: [paradata, web-survey, diffusion]
verified_url: yes
```

**Citation.** Couper, M. P. (2017). Birth and diffusion of the concept of paradata. *Survey Research (JASR)*, 2017.

**DOI / URL.** https://jasr.or.jp/english/JASR_Birth%20and%20Diffusion%20of%20the%20Concept%20of%20Paradata.pdf

**Sample / Method.** Personal/methodological review by the originator of the term "paradata" (Couper 1998), tracing diffusion across web-survey research.

**Key claim(s).**
- Process metadata (timing, breakoffs, device) carries information about respondent quality independent of substantive answers.
- For non-probability designs, paradata are especially valuable as auxiliary for selection-bias diagnostics.

**Takeaway for this dataset.** If timing/device paradata are recoverable from GivingTuesday's collection layer, they could feed the IPW propensity model. We don't currently have them, which is a known limitation.

**Confirms / Complicates / Contradicts.** Complicates Phase 5: an ideal IPW would use paradata we lack.

---

## H15 — Deville & Särndal (1992) — Calibration Estimators in Survey Sampling

```yaml
id: H15
stream: H
relevance_score: 5
peer_reviewed: yes
year: 1992
tags: [calibration, raking, GREG, foundational, weighting]
verified_url: yes
```

**Citation.** Deville, J.-C., & Särndal, C.-E. (1992). Calibration estimators in survey sampling. *Journal of the American Statistical Association*, 87(418), 376–382.

**DOI / URL.** https://doi.org/10.1080/01621459.1992.10475217

**Sample / Method.** Theoretical paper introducing the calibration framework that unifies poststratification, raking, and the generalized regression estimator.

**Key claim(s).**
- All "weight to known marginals" schemes are calibration estimators with different distance functions.
- All such estimators are asymptotically equivalent to the GREG; choice mostly affects tail-weight behavior.

**Takeaway for this dataset.** Justifies using raking-on-marginals (simple, interpretable) as our primary Phase 5 weight rather than full propensity-score IPW, when only marginals are available from NCCS/Candid.

**Confirms / Complicates / Contradicts.** Confirms raking is a valid simplification under our benchmark constraints.

---

## H16 — Kalton & Flores-Cervantes (2003) — Weighting Methods

```yaml
id: H16
stream: H
relevance_score: 4
peer_reviewed: yes
year: 2003
tags: [weighting, raking, GREG, nonresponse]
verified_url: yes
```

**Citation.** Kalton, G., & Flores-Cervantes, I. (2003). Weighting methods. *Journal of Official Statistics*, 19(2), 81–97.

**DOI / URL.** https://www.scb.se/contentassets/ca21efb41fee47d293bbee5bf7be7fb3/weighting-methods.pdf (https://www.researchgate.net/publication/44832856_Weighting_Methods)

**Sample / Method.** Tutorial/practical review covering cell weighting, raking, GREG, logistic regression weighting, and weight trimming.

**Key claim(s).**
- Weight trimming (capping extreme weights) trades small bias for large variance reductions and is usually beneficial.
- Logistic-regression-based weighting is preferred when the auxiliary is continuous or rich.

**Takeaway for this dataset.** Use trimmed weights at e.g. the 1st/99th percentile in Phase 5 — the long tail from the small `hubs` (n=44) and `tech` (n=86) frames will otherwise blow up SE.

**Confirms / Complicates / Contradicts.** Confirms operational details for Phase 5 weight construction.

---

## H17 — Battaglia, Hoaglin & Frankel (2009) — Practical Considerations in Raking

```yaml
id: H17
stream: H
relevance_score: 4
peer_reviewed: no  # Survey Practice (peer-reviewed practitioner journal but not indexed as full peer-review by some)
year: 2009
tags: [raking, weighting, practitioner, CDC]
verified_url: yes
```

**Citation.** Battaglia, M. P., Hoaglin, D. C., & Frankel, M. R. (2009). Practical considerations in raking survey data. *Survey Practice*, 2(5).

**DOI / URL.** https://doi.org/10.29115/SP-2009-0019 (https://www.surveypractice.org/article/2953-practical-considerations-in-raking-survey-data)

**Sample / Method.** Practitioner paper — distillation from CDC BRFSS and similar large-scale rakings — covering convergence diagnostics, dimension choice, and trimming.

**Key claim(s).**
- Raking on too many dimensions (or too-fine cells) inflates variance and risks non-convergence.
- 4–6 well-chosen marginal dimensions usually capture the bulk of bias; more is rarely better.

**Takeaway for this dataset.** Practical limit on Phase 5: rake on at most ~4 dimensions (likely `ref`, region, org_size, sector) given n=930.

**Confirms / Complicates / Contradicts.** Confirms a sparse marginal set is the right operational choice.

---

## H18 — Heckman (1979) — Sample Selection Bias as Specification Error

```yaml
id: H18
stream: H
relevance_score: 4
peer_reviewed: yes
year: 1979
tags: [Heckman, selection, two-stage, foundational, econometrics]
verified_url: yes
```

**Citation.** Heckman, J. J. (1979). Sample selection bias as a specification error. *Econometrica*, 47(1), 153–161.

**DOI / URL.** https://doi.org/10.2307/1912352

**Sample / Method.** Theoretical paper introducing the two-stage selection-correction estimator (probit selection equation + outcome equation conditioning on the inverse Mills ratio).

**Key claim(s).**
- Selection-on-unobservables can be reframed as omitted-variable bias and corrected with a two-step estimator under joint normality.
- Identification rests on functional form or an exclusion restriction — fragile in practice.

**Takeaway for this dataset.** Provides an alternative framework to IPW for handling selection. Useful as a robustness check IF we can write a defensible selection equation for "likelihood of being on the GivingTuesday list".

**Confirms / Complicates / Contradicts.** Complements IPW; complicates because we lack a clean exclusion restriction.

---

## H19 — Rosenbaum & Rubin (1983) — Central Role of the Propensity Score

```yaml
id: H19
stream: H
relevance_score: 4
peer_reviewed: yes
year: 1983
tags: [propensity-score, foundational, observational, causal]
verified_url: yes
```

**Citation.** Rosenbaum, P. R., & Rubin, D. B. (1983). The central role of the propensity score in observational studies for causal effects. *Biometrika*, 70(1), 41–55.

**DOI / URL.** https://doi.org/10.1093/biomet/70.1.41

**Sample / Method.** Theoretical paper proving that conditioning on the scalar propensity score balances all observed covariates between treated/control (or, by analogy, sampled/unsampled) groups.

**Key claim(s).**
- Adjustment on the scalar propensity score is sufficient to remove bias from all *observed* covariates.
- Says nothing about unobserved-covariate bias — that is an assumption.

**Takeaway for this dataset.** Justifies the IPW approach mathematically: weights ∝ 1/π(X) restore covariate balance to a benchmark population, given correct propensity model.

**Confirms / Complicates / Contradicts.** Confirms IPW's theoretical underpinning; the no-unobserved-confounding assumption is the standing caveat.

---

## H20 — Groves (2006) — Nonresponse Rates and Nonresponse Bias

```yaml
id: H20
stream: H
relevance_score: 4
peer_reviewed: yes
year: 2006
tags: [nonresponse, response-rate, total-survey-error]
verified_url: yes
```

**Citation.** Groves, R. M. (2006). Nonresponse rates and nonresponse bias in household surveys. *Public Opinion Quarterly*, 70(5), 646–675.

**DOI / URL.** https://doi.org/10.1093/poq/nfl033

**Sample / Method.** Meta-review and theoretical decomposition of the relationship between unit nonresponse rate and nonresponse bias, drawing on a special POQ issue.

**Key claim(s).**
- Response rate alone is a poor predictor of bias; bias depends on the *correlation* between propensity to respond and the survey variable.
- Different statistics from the same survey can have very different nonresponse biases.

**Takeaway for this dataset.** Argues for variable-by-variable bias diagnostics in Phase 5/6, not a single global "weighted" verdict on the dataset.

**Confirms / Complicates / Contradicts.** Confirms the variable-by-variable robustness reporting plan.

---

## H21 — Salganik & Heckathorn (2004) — Respondent-Driven Sampling

```yaml
id: H21
stream: H
relevance_score: 3
peer_reviewed: yes
year: 2004
tags: [RDS, hidden-population, snowball, network]
verified_url: yes
```

**Citation.** Salganik, M. J., & Heckathorn, D. D. (2004). Sampling and estimation in hidden populations using respondent-driven sampling. *Sociological Methodology*, 34, 193–240.

**DOI / URL.** https://doi.org/10.1111/j.0081-1750.2004.00152.x

**Sample / Method.** Theoretical derivation and empirical illustration of RDS — a chain-referral design where degree-based weights yield asymptotically unbiased estimates.

**Key claim(s).**
- Snowball/network samples can be made inferentially valid IF degree information is collected and the chain is long enough to mix.
- Degree-based weights correct for over-representation of high-degree network members.

**Takeaway for this dataset.** GivingTuesday's recruitment is partly word-of-mouth across NGO networks. RDS-style weighting would be ideal but requires referrer/degree information we don't have. Documents the limit of what's possible without that data.

**Confirms / Complicates / Contradicts.** Complicates: a fully clean weighting scheme is not available given the data we have.

---

## H22 — Lohr (2009) — Multiple-Frame Surveys

```yaml
id: H22
stream: H
relevance_score: 3
peer_reviewed: yes
year: 2009
tags: [multiple-frame, dual-frame, estimation]
verified_url: yes
```

**Citation.** Lohr, S. L. (2009). Multiple-frame surveys. In D. Pfeffermann & C. R. Rao (Eds.), *Handbook of Statistics, Volume 29A: Sample Surveys: Design, Methods and Applications* (pp. 71–88). Elsevier.

**DOI / URL.** https://doi.org/10.1016/S0169-7161(08)00004-2

**Sample / Method.** Handbook chapter reviewing dual- and multiple-frame estimators including the single-frame estimator, the Hartley estimator, and pseudo-maximum-likelihood approaches.

**Key claim(s).**
- When sub-frames overlap or have known coverage gaps, multiple-frame estimators (with explicit overlap weights) outperform naive pooling.
- Diagnostic: compare overlap estimates from each frame as an indicator of nonsampling error.

**Takeaway for this dataset.** Our four `ref` buckets behave like an *implicit* multiple-frame design (with unknown overlap). The proper multi-frame estimator requires overlap information we don't have, but the framing motivates random-intercept multilevel modeling on `ref` as a defensible substitute.

**Confirms / Complicates / Contradicts.** Confirms the multilevel-on-`ref` approach for Phase 6.

---

## H23 — Valliant & Dever (2018) — Survey Weights Practical Guide

```yaml
id: H23
stream: H
relevance_score: 4
peer_reviewed: no  # textbook
year: 2018
tags: [weighting, textbook, practical, calibration]
verified_url: yes
```

**Citation.** Valliant, R., & Dever, J. A. (2018). *Survey Weights: A Step-by-Step Guide to Calculation*. Stata Press.

**DOI / URL.** https://www.stata-press.com/books/survey-weights/

**Sample / Method.** Textbook covering base weights, nonresponse adjustment via propensity / boosting, and calibration to external totals.

**Key claim(s).**
- Best practice: build base weights, then nonresponse-adjust, then calibrate to known auxiliaries — in that order.
- Boosting / ML methods for the propensity step often beat plain logistic regression.

**Takeaway for this dataset.** Operational template for Phase 5: base weight (here, design-weight = 1 for each respondent since opt-in), then propensity adjustment to a NCCS / Candid benchmark, then raking.

**Confirms / Complicates / Contradicts.** Confirms three-step weighting recipe.

---

## H24 — Little & Rubin (2019) — Statistical Analysis with Missing Data, 3rd Edition

```yaml
id: H24
stream: H
relevance_score: 3
peer_reviewed: no  # textbook (author Wiley)
year: 2019
tags: [missing-data, MAR, multiple-imputation, weighting]
verified_url: yes
```

**Citation.** Little, R. J. A., & Rubin, D. B. (2019). *Statistical Analysis with Missing Data* (3rd ed.). Wiley.

**DOI / URL.** https://doi.org/10.1002/9781119482260

**Sample / Method.** Definitive reference on missing-data methods: MCAR/MAR/MNAR taxonomy, EM, multiple imputation, and the connection between weighting and imputation.

**Key claim(s).**
- IPW and multiple imputation are duals: both rely on a correctly specified model linking observed-ness to outcomes.
- Sensitivity analysis (varying MNAR assumptions) is the only honest way to bound bias under unverifiable assumptions.

**Takeaway for this dataset.** Phase 5 should pair IPW with a sensitivity analysis varying the strength of unobserved selection — exactly the protocol Little & Rubin advocate.

**Confirms / Complicates / Contradicts.** Confirms the sensitivity-analysis arm of Phase 5.

---

## H25 — Dillman, Smyth & Christian (2014) — Tailored Design Method (4th ed.)

```yaml
id: H25
stream: H
relevance_score: 3
peer_reviewed: no  # textbook
year: 2014
tags: [web-survey, design, response-rate, mixed-mode]
verified_url: yes
```

**Citation.** Dillman, D. A., Smyth, J. D., & Christian, L. M. (2014). *Internet, Phone, Mail, and Mixed-Mode Surveys: The Tailored Design Method* (4th ed.). Wiley.

**DOI / URL.** https://www.wiley.com/en-us/Internet,+Phone,+Mail,+and+Mixed+Mode+Surveys:+The+Tailored+Design+Method,+4th+Edition-p-9781118456149

**Sample / Method.** Comprehensive textbook on survey design, response-rate maximization, and mixed-mode coordination.

**Key claim(s).**
- Survey response rates depend on perceived relevance, sponsor trust, and burden — all of which selectively shape who responds.
- Mixed-mode and tailored contact strategies reduce but do not eliminate mode-specific bias.

**Takeaway for this dataset.** GivingTuesday's recruitment leveraged sponsor trust (the GT brand) — meaning respondents are concentrated among sector members who already trust GT. This is a Dillman-style structural skew.

**Confirms / Complicates / Contradicts.** Complicates external validity to non-GT-affiliated NGOs.

---

## H26 — Lessler & Kalsbeek (1992) — Nonsampling Error in Surveys

```yaml
id: H26
stream: H
relevance_score: 3
peer_reviewed: no  # textbook
year: 1992
tags: [nonsampling-error, frame, foundational, textbook]
verified_url: yes
```

**Citation.** Lessler, J. T., & Kalsbeek, W. D. (1992). *Nonsampling Error in Surveys*. Wiley-Interscience.

**DOI / URL.** https://www.wiley.com/en-us/Nonsampling+Error+in+Surveys-p-9780471869085

**Sample / Method.** Textbook organizing nonsampling error into frame error, nonresponse, and measurement error; defines coverage error formally.

**Key claim(s).**
- Frame coverage error decomposes into under-coverage and over-coverage; both must be measured against an external standard.
- The "frame" concept is itself fluid in modern web/online recruitment, where there is often no enumerated frame at all.

**Takeaway for this dataset.** GivingTuesday has no enumerated sampling frame. The honest formulation is: "we cannot compute coverage error; we must rely on benchmark comparison".

**Confirms / Complicates / Contradicts.** Confirms why we must benchmark against NCCS/Candid rather than try to estimate coverage directly.

---

## H27 — National Center for Charitable Statistics (NCCS / Urban Institute) — Sector Benchmark Data

```yaml
id: H27
stream: H
relevance_score: 5
peer_reviewed: no  # data resource
year: 2024  # latest core file vintage
tags: [NCCS, IRS-990, benchmark, USA, dataset]
verified_url: yes
```

**Citation.** National Center for Charitable Statistics. (2024). *NCCS Core Data Series* [Dataset]. Urban Institute. Retrieved from https://urbaninstitute.github.io/nccs/

**DOI / URL.** https://urbaninstitute.github.io/nccs/datasets/core/ (also mirrored at https://datacatalog.urban.org/dataset/national-center-charitable-statistics-nccs-core-files)

**Sample / Method.** Annual files since 1989 derived from IRS Form 990 and Business Master File for all US tax-exempt organizations meeting filing thresholds; covers public charities, private foundations, and other §501 subsections separately.

**Key claim(s).**
- Provides population-level marginals (count, revenue, expenses, NTEE sector, state) for the universe of US 501(c)(3) filers — the most authoritative US nonprofit benchmark.
- **Limitation.** Excludes US nonprofits below filing thresholds, all non-US NGOs, and informal/unregistered civil-society organizations.

**Takeaway for this dataset.** This is our primary benchmark for the US-resident slice of `gt`. We can rake/IPW only on auxiliaries NCCS publishes (org size by revenue, NTEE sector, state). Cannot benchmark `india`, `tech`, or `hubs` international components against NCCS at all.

**Confirms / Complicates / Contradicts.** Enables Phase 5 IPW for the US slice; confirms the impossibility of a single global benchmark.

---

## H28 — Candid (2023) — State of Diversity in the U.S. Nonprofit Sector

```yaml
id: H28
stream: H
relevance_score: 4
peer_reviewed: no  # sector report / data product
year: 2023
tags: [Candid, GuideStar, demographics, benchmark, USA]
verified_url: yes
```

**Citation.** Candid. (2023). *The state of diversity in the U.S. nonprofit sector* [Report]. Candid.

**DOI / URL.** https://candid.org/about/press-room/releases/candid-s-the-state-of-diversity-in-the-u.s.-nonprofit-sector-report-sets-new-benchmark-for-demographic-data-collection

**Sample / Method.** Analysis of demographic data voluntarily reported via Candid profiles by ~59,550 US public charities (5-year window).

**Key claim(s).**
- Provides the largest demographic benchmark for US nonprofits: race, gender, sexual orientation, disability across staff, leadership, and board.
- Self-reported and voluntary — so itself a non-probability sample of the NCCS frame.

**Takeaway for this dataset.** Useful as a secondary benchmark for the leadership/staffing variables in our survey, but with a known second-order self-selection bias of its own (orgs who choose to fill in Candid demographics differ from those who don't).

**Confirms / Complicates / Contradicts.** Complicates clean benchmarking — even our best benchmark has its own selection issue.

---

## H29 — Salamon & Sokolowski (2004) — Global Civil Society: Dimensions of the Nonprofit Sector

```yaml
id: H29
stream: H
relevance_score: 4
peer_reviewed: no  # edited volume / Johns Hopkins CCSS
year: 2004
tags: [global-civil-society, comparative, international, NGO, benchmark]
verified_url: yes
```

**Citation.** Salamon, L. M., Sokolowski, S. W., & Associates (2004). *Global Civil Society: Dimensions of the Nonprofit Sector, Volume Two*. Kumarian Press / Johns Hopkins Center for Civil Society Studies.

**DOI / URL.** http://ccss.jhu.edu/wp-content/uploads/downloads/2011/08/Global_Civil_Soiciety_2_TOC.pdf

**Sample / Method.** Country-by-country measurement of nonprofit-sector size, structure, financing, and workforce across ~36 countries via the Johns Hopkins Comparative Nonprofit Sector Project, harmonized to UN Nonprofit Handbook standards.

**Key claim(s).**
- The first internationally comparable benchmark for global civil society size — but coverage varies hugely by country and the data are dated.
- Many low-income and authoritarian-context countries are absent or undercounted.

**Takeaway for this dataset.** The closest thing to a global NGO benchmark, but it is too coarse and outdated (2004 vintage) to support precise IPW for our `india` / international rows. It documents *why* a clean global IPW is infeasible.

**Confirms / Complicates / Contradicts.** Justifies the conservative path: rake only on auxiliaries available globally (region buckets), not on org-level marginals.

---

## H30 — Mercer, Lau & Kennedy (2017) — How Different Weighting Methods Work (Pew companion)

```yaml
id: H30
stream: H
relevance_score: 3
peer_reviewed: no  # Pew methodological brief
year: 2018
tags: [Pew, weighting, raking, propensity, tutorial]
verified_url: yes
```

**Citation.** Mercer, A., Lau, A., & Kennedy, C. (2018). *How different weighting methods work*. Pew Research Center, January 26, 2018.

**DOI / URL.** https://www.pewresearch.org/methods/2018/01/26/how-different-weighting-methods-work/

**Sample / Method.** Methodological companion to Mercer/Lau/Kennedy 2018 (H6), explaining raking, propensity weighting, matching, and combinations side-by-side.

**Key claim(s).**
- Raking is robust, simple, and competitive when auxiliaries are categorical and few; propensity weighting wins when many continuous covariates are available.
- Matching is typically the *worst* option for opt-in weighting in their tests.

**Takeaway for this dataset.** Reinforces that raking on a sparse marginal set is the right Phase 5 default; propensity-score weighting is a complementary check, not a primary method, given our limited benchmark.

**Confirms / Complicates / Contradicts.** Confirms the hierarchy of methods to try in Phase 5.

---

## Stream H synthesis — Justification for the Phase 5/6 IPW + multilevel approach

The GivingTuesday n=930 survey is a textbook non-probability, multi-frame, opt-in design — with all four sub-frames (`gt` 549, `india` 251, `tech` 86, `hubs` 44) self-selected through different recruitment channels. Under the AAPOR framework (H1, H2) all inference is therefore model-dependent, and the canonical defenses are quasi-randomization (IPW; H10, H11, H12, H19) and calibration to known auxiliaries (H15, H16, H17, H23). The strongest empirical evidence (H5 Xbox; H6 Pew) shows that non-representative samples *can* recover valid estimates, but only when the auxiliaries used to weight also explain the outcome — and even then residual bias is typical (H3, H9, H10). Our Phase 5 plan — inverse-frequency reweighting on `ref` × org-size × region against a hybrid NCCS (H27) / Candid (H28) / Johns Hopkins-CCSS (H29) marginal set, with raked weights trimmed at the 1st/99th percentile (H16, H17), then re-estimating every headline regression unweighted and weighted (Mercer/Lau/Kennedy 2018, H6, H30) — is the AAPOR-compliant minimum. Phase 6 layers on a multilevel model with `ref` as a random intercept, motivated by the multiple-frame logic of Lohr (H22) and the partial-pooling rationale of Park, Gelman & Bafumi (H4) and Wang et al. (H5). Sensitivity analyses follow Little & Rubin (H24): varying the propensity model and re-running the headline F-1 result. The honest limitation, documented explicitly here, is that **no perfect benchmark exists for global NGOs**: NCCS/Candid cover only US 501(c)(3) filers, Salamon & Sokolowski's CNP data are coarse and dated, and we lack RDS-style network paradata (H21) or process paradata (H14) that would tighten the propensity model. Consequently we will report (a) unweighted, (b) US-slice IPW-weighted, and (c) `ref`-multilevel estimates side-by-side, and treat any finding (e.g., F-1 aspiration inversion) as robust only if it survives all three.
