# Pre-registered hypotheses

> **Pre-registration discipline.** This file is locked before Phase 6 starts. Hypotheses added after Phase 6 begins must be flagged `pre_registered: no` in `findings.md`. Each hypothesis specifies: (a) prior, (b) operationalization, (c) test, (d) confirm/contradict direction.

> **Cross-references.** F-1…F-20 = `archive/4hr_pass/analysis/findings.md`. Stream IDs (A1…H25+) = `analysis/papers/<stream>.md`. Methods D1…D9 = `analysis/methods.py`.

Hypotheses are clustered by the method that decides them, so Phase 6 can batch-execute.

---

## Cluster I — Re-tests of headline findings (F-1, F-8, F-9, F-10, F-11, F-18)

### H1 — Aspiration inversion survives multilevel adjustment
- **Prior.** Stanford HAI, McKinsey, Salesforce, Rotter et al. (B1, B2, B5, A2): GenAI adoption tilts to content tasks; analytical tasks lag.
- **Operationalization.** Per-task paired delta `[W]_t − [U]_t` for each of the 7 tasks (Ask, Assist, Generat, Interpret, Organi, Predict, Translat).
- **Test.** Per-task **paired multilevel logistic** with `ref` as random intercept and controls for `org_size_int`, `tech_person`, `cluster3`. Add cluster-bootstrap CI on the gap, resampling whole `ref` strata.
- **Confirms if.** Analytical tasks (Predict, Organi, Interpret, Assist) show `[W] > [U]` deltas > +30 pp at p_FDR < 0.01 after multilevel adjustment.
- **Contradicts if.** Adjustment shrinks gap to non-significant on ≥3 of 4 analytical tasks.

### H2 — Late-Adopter typology survives LCA replacement
- **Prior.** F-10 found 52.8% of K-means-defined Late Adopters say "don't understand AI"; their cloud_storage and data_use_policy are *higher* than Skeptics'. This is the headline supporting finding.
- **Operationalization.** Replace the K-means/HDBSCAN typology with stepmix LCA on the 18 binary `[U]`/`[W]` indicators (or 20 incl. `[D]`).
- **Test.** Fit LCA k=2..6, pick by BIC + entropy. For the chosen k, compute posterior class probabilities; identify the class where mean(use_count) < 0.5 AND mean(want_count) > 2 AND mean("don't understand AI") > 0.4.
- **Confirms if.** Such a class exists, sized ≥150, with item-response probabilities showing low `[U]` items + moderate `[W]` items + high "don't understand".
- **Contradicts if.** No class has the comprehension-bottleneck profile; or LCA collapses Late + Skeptic into one class.

### H3 — Comfort × infrastructure interaction is continuous, not threshold
- **Prior.** F-9 used median-split. The McKinsey/HAI prior is that infrastructure and comfort each *enable* AI use, but the median-split obscures whether the relationship is linear or has a threshold.
- **Operationalization.** Continuous `person_ai_comfort` × `data_readiness` (IRT-scored) interaction in a Poisson GLM on `use_count`.
- **Test.** Poisson with `use_count ~ comfort + readiness + comfort:readiness + ref` (ref as fixed for comparability). Plot 2-D marginal-effects heatmap.
- **Confirms if.** Both main effects significant (p < 0.01) AND interaction term β > 0 with p < 0.05.
- **Contradicts if.** Interaction n.s. (additive model fits as well).

### H4 — Mediation through readiness has a robust direct path
- **Prior.** F-11: readiness mediates only 18.5% of risk_reward → use_count.
- **Operationalization.** `risk_reward → readiness → use_count` (excluding `risk_reward = -1`). Use IRT-scored readiness instead of additive.
- **Test.** `mediation_full` with bootstrap CI + DoWhy refute_estimate (placebo treatment, random common cause).
- **Confirms if.** Indirect effect CI excludes 0; proportion mediated 10–30%; refute placebo p > 0.5.
- **Contradicts if.** Indirect CI includes 0 OR refute placebo "significantly" non-zero.

### H5 — GN/GS divide reverses for small orgs without tech (F-8) — Oaxaca + PSM + IPW agreement
- **Prior.** F-8 found a +0.339 interaction coef (`is_S × small`) on use_count, holding tech_person constant. Toyama's amplification (C6) predicts the gap should *widen* for low-capacity orgs, not reverse — so this is contrarian.
- **Operationalization.** Subset to small (≤15 staff) orgs without a `tech_person`. Outcome = `use_count`. Group = `is_S` (1 if global_north_south = "S").
- **Test.** Three robustness checks:
  1. **Oaxaca–Blinder** decomposition of GN/GS use_count gap into endowments (in `[D]` density, comfort, infrastructure) vs coefficients.
  2. **Propensity-score matching**: 1:1 nearest-neighbor on (org_size_int, comfort, readiness, role) within the no-tech-person subset; compare matched `[U]` rates.
  3. **IPW reweighting** to a balanced GN/GS proportion (50/50) and re-fit Poisson.
- **Confirms if.** ≥2 of 3 still show `is_S > is_N` use_count among small no-tech orgs.
- **Contradicts if.** ≤1 of 3 confirms — original interaction is artifact of unbalanced controls.

### H6 — Re-derived 3-cluster typology under LCA places "Aspirationals" as the largest class
- **Prior.** F-18 used K-means; found Aspirationals (n=444) >> Power Users (n=118).
- **Operationalization.** LCA on the same 4-feature standardized matrix; report sizes of the BIC-selected solution.
- **Confirms if.** A class with high want_count + low-to-moderate use_count is the modal class.
- **Contradicts if.** LCA picks a different number of classes or collapses Aspirationals.

---

## Cluster II — New hypotheses (Streams A–H)

### H7 — `data_readiness` is a unidimensional latent trait
- **Prior.** Hwang & Powell (A17) on professionalization clustering; Salesforce digital-maturity index (A5).
- **Operationalization.** 2-PL IRT on the 10 binary readiness items (`tech_person`, `merl_person`, `cloud_storage`, `data_use_policy`, `org_agreements`, plus the 5 `[D]` items).
- **Test.** Fit 2PL via girth; check (i) all discriminations > 0.5; (ii) item-fit infit/outfit < 1.5; (iii) Cronbach's α > 0.7 on the same items as a comparator.
- **Confirms if.** All discriminations positive and α > 0.7 → the additive index in F-9/F-10 is a reasonable approximation of θ.
- **Contradicts if.** ≥2 items with α < 0.3 or negative discrimination → the index is multidimensional and Phase 5 IRT score should replace the additive index in every downstream finding.

### H8 — TOE-style SEM: organizational + technological + environmental → AI use
- **Prior.** Tornatzky & Fleischer (A14), Godefroid et al. (A1), TOE canon.
- **Operationalization.** Latent variables:
  - **Org capacity** ← `org_size_int`, `tech_person`, `merl_person`
  - **Tech infra** ← `cloud_storage`, `data_use_policy`, `[D]` items
  - **Env pressure** ← `collab_feasibility`, `org_agreements`, `multi_country`
  - **Outcome** = `use_count` (manifest, count)
- **Test.** `sem_fit` with semopy; report χ²/df, CFI, TLI, RMSEA, SRMR.
- **Confirms if.** All three latent → outcome paths positive at p < 0.05; CFI > 0.9, RMSEA < 0.08.
- **Contradicts if.** Env or Tech-infra path n.s. or negative.

### H9 — Risk perception has a 2-factor structure (Slovic dread × unknown)
- **Prior.** Slovic (1987), Fischhoff et al. (1978).
- **Operationalization.** EFA / FA on the 7 binary `ai_risk` items.
- **Test.** Parallel analysis for n_factors; rotated loadings.
- **Confirms if.** 2 factors retained; loadings approximately split bias/breaches/plagiarism (dread/known) vs inequity/dependency/environment/replacing (unknown/structural).
- **Contradicts if.** 1-factor or >2-factor solution.

### H10 — Comfort grows with use; vigilance does not (F-3 generalized)
- **Prior.** BCG (B3) — comfort up with use; MIT SMR (B6) — vigilance down with use. Stream E gives the canonical pieces (Glikson & Woolley review; Lee & See trust-in-automation).
- **Operationalization.** Two regressions on `use_count`:
  1. `person_ai_comfort ~ use_count + ref + org_size_int + (1|ref)` — multilevel.
  2. `risk_count ~ use_count + person_ai_comfort + ref + (1|ref)` — multilevel Poisson.
- **Confirms if.** β_comfort > 0 at p < 0.01 AND β_use_count_on_riskcount > 0 at p < 0.05 net of comfort (i.e., hands-on selects more risks; comfort suppresses the count).
- **Contradicts if.** Either path reverses or vanishes.

### H11 — Comprehension is a stronger non-adoption predictor than risk perception
- **Prior.** Kabra & Saharan (A3); F-10 (52.8% of Late Adopters say "don't understand").
- **Operationalization.** Logistic regression: `low_use ~ rr_dont_understand + risk_count + person_ai_comfort + (1|ref)` where `low_use = (use_count == 0)`.
- **Confirms if.** Standardized β for `rr_dont_understand` > Standardized β for `risk_count`.
- **Contradicts if.** Risk count beats comprehension marker.

### H12 — Aspiration gap is universal across cause areas (F-19 generalized)
- **Prior.** F-19 found weak cause-area effects on use; want is universal-high.
- **Operationalization.** Multilevel Poisson with `(1|org_label_first)` random intercept on per-respondent gap (want_count − use_count).
- **Confirms if.** ICC for cause area < 0.05; mean gap > 1 for all causes with n ≥ 20.
- **Contradicts if.** ICC > 0.10 or any cause shows gap < 0.5.

### H13 — Africa subset is a sample artifact (F-13)
- **Prior.** Friederici et al. (C5): African digital activity concentrates in hubs.
- **Operationalization.** Compare Africa respondents (n=60) recruited via `ref=hubs` vs other refs.
- **Test.** Mann-Whitney on use_count split by `ref==hubs` within Africa.
- **Confirms F-13 robustness if.** Hubs vs non-hubs Africans show similar use_count (artifact would predict a difference if hubs respondents were the over-using cohort).
- **Contradicts if.** Hubs Africans use significantly more — F-13 is a hub-recruitment artifact.

### H14 — Translation `[W]` over-indexes in Global South (F-14 multilevel re-test)
- **Prior.** Png (C7), F-14.
- **Operationalization.** Logistic of `[W] Translat` on `is_S` with `ref` random intercept, controlling for `comfort`, `org_size`, `cluster3`.
- **Confirms if.** β > 0 at p < 0.01 net of controls.
- **Contradicts if.** β shrinks below significance.

### H15 — India NGOs are NOT lower-comfort at matched size × tech (F-5 multilevel re-test)
- **Prior.** Kabra & Saharan (A3); F-5.
- **Operationalization.** Multilevel logistic of `comfort_high` on `in_india_ref + org_size_int + tech_person`, with `(1|ref)`.
- **Confirms F-5 (which contradicts A3) if.** β for `in_india_ref` n.s.
- **Contradicts F-5 / supports A3 if.** β < 0 at p < 0.05.

### H16 — Free-text BERTopic recovers an "aspirational" topic in Late Adopters
- **Prior.** F-16; F-10. Multilingual NLP (Stream F).
- **Operationalization.** BERTopic on `ai_opentext` (paraphrase-multilingual-MiniLM-L12-v2). Compute topic distribution per cluster3.
- **Test.** χ² of topic × cluster3; identify topics over-represented in cluster3==0 (Late Adopters).
- **Confirms if.** ≥1 topic over-represented in Late Adopters has top words like "learn", "understand", "training", "explain" (or multilingual equivalents).
- **Contradicts if.** Late Adopters have no distinctive topic OR the topic is dominated by negative/skeptical language.

### H17 — Risk-aware skeptics are disengaged, not vigilant (F-15 generalized)
- **Prior.** F-15.
- **Operationalization.** Among `cluster3 == -1`, regress `risk_count ~ use_count + comfort + opentext_length + (1|ref)`.
- **Confirms F-15 if.** β for use_count n.s. or negative AND opentext_length significantly lower than other clusters (disengagement).
- **Contradicts if.** Risk-count is positively associated with use, controlling for engagement proxies.

### H18 — Tech_person dominates org_size in predicting `[W]` count (UTAUT facilitating-conditions test)
- **Prior.** Venkatesh et al. (A6, UTAUT); Curtis et al. (A8).
- **Operationalization.** Standardized Poisson of `want_count` on `tech_person + merl_person + org_size_int + cluster3 + ref`.
- **Confirms UTAUT if.** Standardized β for `tech_person` > Standardized β for `org_size_int` at p < 0.05.
- **Contradicts (size dominance) if.** β for `org_size_int` larger.

### H19 — Policy-without-cloud (F-6) replicates under multilevel
- **Prior.** F-6 found 165 orgs (17.7%) with policy=1, cloud=0, adopting AI *less* than overall.
- **Operationalization.** Logistic of `(cluster3==1)` ~ `policy_only + cloud_only + both + (1|ref)` (reference=neither).
- **Confirms if.** β for `policy_only` < 0 at p < 0.05.
- **Contradicts if.** β >= 0.

### H20 — Org age has no effect on use_count (F-17 multilevel)
- **Prior.** F-17: ρ(org_years, use_count) ≈ −0.02 (n.s.).
- **Operationalization.** Multilevel Poisson `use_count ~ org_years_raw + org_size_int + tech_person + (1|ref)`.
- **Confirms if.** β for `org_years_raw` n.s.
- **Contradicts if.** β significant in either direction (size and tech are already controlled).

### H21 — Cluster membership is robustly predicted by comfort > readiness > size
- **Prior.** F-9, F-10, F-17. Stream B (BCG comfort-with-use).
- **Operationalization.** Standardized multinomial logistic of `cluster3` (3 levels) on standardized comfort, readiness (IRT), size, tech_person, and `ref` random intercept (or fixed for multinomial).
- **Confirms if.** standardized β ordering: comfort > readiness > size.
- **Contradicts if.** different ordering.

### H22 — `ai_risk_reward = -1` is the strongest risk attitude category for late adoption
- **Prior.** F-10, F-15.
- **Operationalization.** Multinomial logistic of `cluster3` on `ai_risk_reward` (treating −1 as a separate category, 1–5 as ordinal).
- **Confirms if.** OR(rr=−1 vs rr=3, on cluster3==0) > 2 with CI excluding 1.
- **Contradicts if.** OR ≈ 1.

### H23 — Sample reweighting against a Candid-style benchmark does NOT change the headline F-1 inversion
- **Prior.** Mercer/Pew (Stream H), F-1 already survives inverse-frequency reweighting in archive.
- **Operationalization.** Construct a benchmark distribution proxy: 60% US (gt + tech if US-based), 25% India (india), 10% Africa (hubs Africans), 5% other. Compute IPW. Re-run McNemar on each `[U]`/`[W]` pair.
- **Confirms if.** Predict, Organi, Interpret, Assist gaps remain > +30 pp at FDR < 0.01.
- **Contradicts if.** Any analytical-task gap drops > 50% under reweighting.

### H24 — `[D]` co-occurrence breaks into communities of "structured" vs "unstructured" data practices
- **Prior.** Le Roux & Rouanet MCA; nonprofit data-system literature.
- **Operationalization.** MCA + Louvain (`mca_louvain`) on the 5 `[D]` items + `cloud_storage` + `data_use_policy` + `tech_person`.
- **Confirms if.** ≥2 communities, with software/devices/cloud in one and audio/transcripts in another.
- **Contradicts if.** Single community.

### H25 — Multilingual respondents (Hindi-language `ai_opentext`) cluster differently
- **Prior.** Bender et al. C16, Sambasivan C17.
- **Operationalization.** Run langdetect on `ai_opentext`; compare cluster3 distribution between English-language and non-English responses.
- **Confirms if.** χ² p < 0.05 with non-English over-represented in cluster3 != 1.
- **Contradicts if.** Distribution similar.

### H26 — IRT-scored readiness predicts adoption better than additive readiness
- **Prior.** Embretson & Reise; Stream D.
- **Operationalization.** Compare AIC/BIC of Poisson `use_count ~ readiness_irt + ...` vs `... readiness_additive ...`, both with multilevel `(1|ref)`.
- **Confirms IRT if.** ΔAIC favors IRT version by > 4.
- **Contradicts if.** ΔAIC favors additive or differs by < 2.

---

## Method-cluster summary (Phase 6 batches)

| Method batch | Hypotheses |
|---|---|
| LCA via stepmix | H2, H6 |
| 2-PL IRT via girth | H7, H26 |
| Multilevel logistic / Poisson | H1, H3, H10, H11, H12, H14, H15, H17, H18, H19, H20, H21, H22 |
| Oaxaca / PSM / IPW | H5, H23 |
| SEM via semopy | H8 |
| EFA / FA | H9 |
| Mediation + DoWhy refute | H4 |
| BERTopic | H16, H25 |
| MCA + Louvain | H24 |
| Mann-Whitney + subgroup_sweep | H13 |

26 pre-registered hypotheses, covering 8 streams. Phase 6 will execute, log, and FDR-adjust within each batch.
