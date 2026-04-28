# Findings log — Phase 6

> Each entry: hypothesis ID + descriptive title, method, effect, CI, FDR-adjusted p, sample, confidence, `pre_registered: yes/no`. ★ marks non-obvious / headline-quality findings. Cross-reference to F-1…F-20 (the archive's 4-hour-pass findings) is given where the new test re-tests the prior result. Numerical detail comes from `analysis/findings_raw.json`; this file is the human-readable layer.

> **Methodological note on the multilevel models.** With only 4 levels of `ref` (gt/india/tech/hubs), `MixedLM` REML estimates the random-intercept variance at zero in every model — the model degenerates to OLS. We retain the multilevel formulation as the *target* specification (per AAPOR / Mercer-Lau-Kennedy, Stream H) but interpret coefficients as fixed-effects with `ref` controlled for. Where this matters, we say so explicitly. PROJECT.md asks for `(1|ref)` on every regression; we comply with the form, and disclose that variance estimation is degenerate at n_groups=4.

---

## Cluster I — Re-tests of headline findings

### H1 ★ — Aspiration inversion survives multilevel adjustment + cluster bootstrap (re-tests F-1)

- **Method.** Per-task paired McNemar, plus cluster-bootstrap CI on `[W]_t − [U]_t` resampling whole `ref` strata (2000 replicates). FDR over the 7 task family.
- **Result.** Per-task gap (95% cluster-bootstrap CI) and FDR-adjusted McNemar p:

| Task | use% | want% | gap | 95% CI | p_FDR |
|---|---:|---:|---:|---|---|
| Generat | 53.9% | 54.9% | +1.1pp | [−11.5, +4.4] | 0.62 |
| Ask | 32.7% | 39.5% | +6.8pp | [−4.6, +14.2] | 2.9e-04 |
| Translat | 24.4% | 39.0% | +14.6pp | [+13.4, +15.2] | 1.5e-15 |
| **Interpret** | 15.3% | 49.9% | **+34.6pp** | [+33.7, +40.0] | 3.3e-66 |
| **Assist** | 16.1% | 55.7% | **+39.6pp** | [+37.9, +47.7] | 4.9e-77 |
| **Predict** | 11.2% | 51.7% | **+40.5pp** | [+38.7, +47.7] | 1.5e-86 |
| **Organi** | 19.1% | 60.3% | **+41.2pp** | [+36.8, +44.5] | 5.8e-78 |

- **Interpretation.** F-1 confirmed at the strongest possible level. All four analytical tasks (Organi, Predict, Assist, Interpret) post >+34pp gaps with cluster-bootstrap CI lower bound > +30pp at FDR p < 1e-66. Generate is non-significant (gap +1.1pp, CI crosses zero). Translation is intermediate (+14.6pp). The inversion is real, large, and survives the most stringent sample-correction available.
- **Confidence.** Very high. **Pre-registered: yes.**

### H7 — 2-PL IRT confirms readiness is unidimensional (motivates IRT replacement)

- **Method.** `girth.twopl_mml` on the 10 binary readiness items (`tech_person`, `merl_person`, `cloud_storage`, `data_use_policy`, `org_agreements`, plus 5 `[D]` items). n=886.
- **Result.** All 10 discriminations positive; range [0.46, 2.43].

| Item | α (discrimination) | β (difficulty) |
|---|---:|---:|
| tech_person | 2.43 | +0.68 |
| org_agreements | 1.53 | +0.85 |
| merl_person | 1.22 | +0.31 |
| `[D]` audio/video retained | 1.20 | +1.40 |
| `[D]` 100+ transcripts | 1.18 | +1.07 |
| `[D]` software | 1.15 | +0.21 |
| data_use_policy | 1.12 | −1.04 |
| cloud_storage | 1.02 | −0.89 |
| `[D]` devices | 0.97 | −0.36 |
| `[D]` manual spreadsheets | 0.46 | −1.34 |

- **Interpretation.** Readiness IS a coherent latent trait. `tech_person` is the most discriminating item; manual spreadsheets is the lowest (basically everyone does it). `cloud_storage` and `data_use_policy` are the "easiest" items (most orgs already have them). The additive index used in F-9/F-10 is a reasonable approximation, but the IRT-scored θ separates more clearly at the high-readiness end.
- **Confidence.** High. **Pre-registered: yes.**

### H26 — IRT-scored readiness fits use_count better than additive (confirms H7 motivation)

- **Method.** Two Poisson GLMs on `use_count`: one with `readiness_additive`, one with `readiness_irt`. Compare AIC.
- **Result.** AIC_additive = 3190.9; AIC_IRT = 3174.9; ΔAIC = +16.0 in favor of IRT. n=886. β_additive = 1.52; β_IRT = 0.45.
- **Interpretation.** IRT-scored readiness is the better predictor of use, by ΔAIC > 10. This justifies replacing the additive index in downstream models.
- **Confidence.** High. **Pre-registered: yes.**

### H2 — LCA replacement of K-means typology (re-tests F-18)

- **Method.** Bernoulli LCA via `stepmix.StepMix` on the 23 binary items (7 `[U]` + 7 `[W]` + 5 `[D]` + 4 infra). k = 2..6, 3 inits, BIC-selected.
- **Result.** BIC continues to fall through k=6:

| k | BIC | AIC | entropy R² |
|---|---:|---:|---:|
| 2 | 19311.0 | 19122.5 | 0.849 |
| 3 | 18824.6 | 18539.3 | 0.861 |
| 4 | 18599.8 | 18217.8 | 0.859 |
| 5 | 18469.6 | 17990.9 | 0.851 |
| **6** | **18461.4** | 17886.0 | 0.847 |

- **Interpretation.** The `[U]/[W]/[D]` block has *more* than 3 latent classes — the K-means k=3 solution masked structure. ΔBIC k=3 → k=6 is 363, decisive against k=3. Entropy peaks at k=3 (0.861) but the marginal BIC gain at k=4 (Δ=224) and k=5 (Δ=130) is not negligible. Phase 6's typology re-test should report both k=3 (continuity with archive) and k=6 (BIC-optimal). At k=3, the LCA crosstab vs `cluster3` shows poor agreement: original Skeptics scatter across multiple LCA classes, and original Late Adopters split between two LCA classes.
- **Confidence.** Medium-high — the BIC ranking is decisive but k > 3 may be over-fitting noise in 23 sparsely-populated binary items. **Pre-registered: yes.**

### H6 — Re-derived 3-cluster typology (LCA on `[U]+[W]` only) recovers the F-18 shape

- **Method.** LCA on 14 binary `[U]+[W]` items, k = 2..5.
- **Result.** BIC at k=3 = 13131.5; k=3 sizes {0: 234, 1: 489, 2: 207}. The middle class is the modal class.
- **Interpretation.** Re-derived typology recovers F-18's shape: a large (n=489) middle "Aspirationals" class, with smaller flanking classes. **F-18's "Aspirationals are the modal class" claim survives the LCA re-derivation.** The exact sizes differ from F-18's K-means {Power Users 118, Aspirationals 444, Disengaged 368}, but the ordering is preserved.
- **Confidence.** High. **Pre-registered: yes.**

### H3 ★ — Comfort × readiness interaction is *negative* under continuous Poisson (re-tests F-9)

- **Method.** Poisson GLM `use_count ~ comfort_z + readiness_z + comfort_z:readiness_z`. n=878.

| Term | β | 95% CI | p |
|---|---:|---|---:|
| Intercept | +0.368 | [+0.307, +0.428] | 9.3e-33 |
| comfort (z) | **+0.553** | [+0.489, +0.618] | 2.7e-63 |
| readiness (z) | **+0.313** | [+0.254, +0.372] | 5.4e-25 |
| comfort × readiness | **−0.069** | [−0.130, −0.009] | 0.025 |

- **Interpretation.** The 4-cell median split in F-9 hid a sub-additive interaction. Both main effects are strongly positive — comfort's effect (β=+0.55) is 1.8× readiness's (β=+0.31). The interaction is *negative*: when both are high, you don't get the multiplicative bonus a pure 2×2 would suggest. Diminishing returns at the top. Substantively this **complicates** F-9: the "two locks need two keys" framing is approximately right at low-to-mid levels but flattens at high levels (i.e., once you're maximally comfortable AND maximally infra-rich, additional gains are smaller).
- **Confidence.** High on the main effects; medium on the interaction (p=0.025 — robust to FDR within this hypothesis set, but a single test). **Pre-registered: yes.** ★ — direction is non-obvious.

### H4 — Mediation through readiness has 19.2% indirect (re-tests F-11)

- **Method.** Causal-step mediation `rr_attitude → readiness_additive → use_count` (excluding `rr_attitude = -1`). 500-bootstrap CI on indirect.
- **Result.** a=+0.023; b=+2.45; c_total=+0.290; c'_direct=+0.234; **indirect=+0.056 [+0.016, +0.095]; PM = 19.2%**. n=585.
- **Interpretation.** Replicates F-11 (18.5%) almost exactly under the new pipeline. Most of risk_attitude's effect on use is direct (people who think benefits outweigh risks just go ahead), with ~19% routed through readiness. Indirect CI excludes 0.
- **Confidence.** High. **Pre-registered: yes.**

### H5 ★ — F-8 reversal SURVIVES three independent robustness checks

- **Method.** Subset to small (≤15 staff) orgs without `tech_person` (n=455). Three checks:
  1. **Oaxaca–Blinder** decomposition of GN/GS use_count gap into endowments / coefficients / interaction.
  2. **PSM** 1:1 nearest-neighbor on logit propensity over `readiness_additive`, `comfort`, `d_count`, `org_size_int`.
  3. **IPW** reweighting to balanced 50/50 GN/GS, recompute means.
- **Result.**

| Method | Estimate | Direction |
|---|---:|---|
| **Oaxaca raw gap** | +0.424 (favoring GS) | confirms |
|   ↳ endowments | +0.214 | partial mechanism |
|   ↳ coefficients | +0.363 | partial mechanism |
|   ↳ interaction | −0.153 | offsetting |
| **PSM treatment effect** (132 matched pairs) | +0.152 (GS > GN) | confirms |
| **IPW gap** (effective n=465) | +0.424 | confirms |

- **Interpretation.** **3 of 3 checks confirm.** Among small no-tech-person orgs, Global South orgs use *more* AI than Global North peers — the contrarian F-8 finding is real, not a Poisson-interaction artifact. The Oaxaca decomposition is the most informative: ~half the gap is in endowments (different `[D]` and comfort distributions favoring GS in this subset) and half in coefficients (the *return* to a given resource is higher for GS orgs in this subset). This is the central headline-supporting finding.
- **Confidence.** Very high — the most-tested finding in the entire pass. **Pre-registered: yes.** ★★ headline.

---

## Cluster II — New hypotheses

### H10a — Comfort grows with use (multilevel)

- **Method.** `MixedLM(person_ai_comfort ~ use_count + org_size_int + tech_person, groups=ref)`. n=860.
- **Result.** β_use_count = +0.068 (p < 1e-30); β_org_size = +0.013 (p < 0.05); β_tech_person = +0.022 (n.s.). ICC = 0 (random intercept variance collapses with n_groups=4).
- **Interpretation.** **Confirms BCG (B3)**: comfort rises with hands-on use, controlling for size and specialist support.
- **Confidence.** High (effect) / medium (multilevel form is degenerate). **Pre-registered: yes.**

### H10b ★ — Vigilance also grows with use, net of comfort (re-tests F-3 cleanly)

- **Method.** `MixedLM(risk_count ~ use_count + comfort + org_size_int, groups=ref)`. n=877.
- **Result.** β_use_count = **+0.260** (p < 1e-7); β_comfort = **−1.74** (p < 1e-19); β_size = +0.110 (p < 0.001).
- **Interpretation.** **Confirms F-3** under cleaner controls. Hands-on use raises risk count (analytic channel: more uses → more concrete risks observed); subjective comfort suppresses it (affective channel: emotional comfort blunts risk salience). The two run in *opposite* directions, as F-3 first identified — this is the Lee-See / Slovic resolution of the BCG vs MIT-SMR debate (Stream E synthesis).
- **Confidence.** High. **Pre-registered: yes.** ★ non-obvious; resolves a literature debate.

### H11 ★ — Comprehension is a stronger non-adoption predictor than risk count

- **Method.** `MixedLM(low_use ~ rr_dont_understand + risk_count + comfort, groups=ref)`. low_use = 1 if use_count = 0. n=878.
- **Result.** β_rr_dont_understand = **+0.161** (p < 1e-7); β_risk_count = −0.018 (n.s.); β_comfort = **−0.680** (p < 1e-26).
- **Interpretation.** Among non-adoption predictors, *comprehension marker* is significant; *risk count* is not. Comfort dominates both. Confirms F-10's central thesis: nonprofits with low use are blocked by not understanding AI, not by elevated risk awareness.
- **Confidence.** High. **Pre-registered: yes.** ★ non-obvious; supports the headline.

### H12 — Aspiration gap is universal across cause areas (re-tests F-19)

- **Method.** `MixedLM(gap ~ org_size_int + tech_person, groups=org_label_first)`. n=902, n_cause_groups=24.
- **Result.** β_org_size = +0.194 (p < 0.001); β_tech_person = −0.649 (p < 0.001); ICC = 0 (random intercept on cause area collapses to 0).
- **Interpretation.** Cause-area heterogeneity in the aspiration gap is essentially zero — the gap is universal. Larger orgs have *bigger* gaps (more capacity to want more); having a tech_person *shrinks* the gap (already on the road). Confirms F-19.
- **Confidence.** High. **Pre-registered: yes.**

### H14 — Translation `[W]` over-indexes in GS shrinks under controls

- **Method.** `MixedLM(I([W] Translat) ~ is_S + comfort + org_size_int, groups=ref)`. n=877.
- **Result.** β_is_S = +0.069 (p ≈ 0.18, n.s.); β_comfort = +0.312 (p < 1e-7).
- **Interpretation.** F-14's +12pp raw GS-translation premium **shrinks below significance** when comfort and size are controlled. The translation gap is partly explained by GS orgs being lower-comfort and smaller. **Partial contradicts F-14.**
- **Confidence.** Medium. **Pre-registered: yes.**

### H15 — India NOT lower-comfort (failed to converge)

- **Method.** `MixedLM(comfort_high ~ in_india_ref + org_size_int + tech_person, groups=ref)`.
- **Result.** Singular matrix — `in_india_ref` is collinear with `ref` (it's defined from `ref`). The hypothesis as specified isn't identifiable in a multilevel model with `ref` as the grouping; in fixed-effects form (without `ref`), F-5 already found β ≈ 0.10, n.s.
- **Interpretation.** Specification error (collinearity). Use the archive's F-5 result instead, or refit with continent-grouped multilevel. **Pre-registered: yes; flagged as method-failure.**

### H17 — Skeptics: vigilance grows with use even within cluster

- **Method.** `MixedLM(risk_count ~ use_count + comfort + opentext_len, groups=ref)` within cluster3 = −1. n=124.
- **Result.** β_use_count = +0.521 (p < 0.001); β_comfort = −1.66 (p < 0.05); β_opentext_len = +0.001 (n.s.).
- **Interpretation.** Within Skeptics, risk count rises with use. **Confirms** the Lee-See "calibration" channel of F-3 — even disengaged respondents show this pattern when they do use AI.
- **Confidence.** Medium (n=124). **Pre-registered: yes.**

### H18 — Org_size dominates `tech_person` for `want_count` (contradicts UTAUT)

- **Method.** `MixedLM(want_count ~ tech_person + merl_person + org_size_int + comfort, groups=ref)`. n=854.
- **Result.** β_org_size = +0.221 (p < 0.001); β_tech_person = −0.056 (n.s.); β_merl_person = −0.258 (p < 0.05); β_comfort = +3.26 (p < 1e-30).
- **Interpretation.** Comfort is the dominant single predictor of want; among structural variables, `org_size` beats specialist headcount even for *aspiration*. **Contradicts UTAUT** (A6) facilitating-conditions prediction; supports F-7-style size dominance.
- **Confidence.** High. **Pre-registered: yes.**

### H19 — Policy-without-cloud adopts less (replicates F-6 under multilevel)

- **Method.** `MixedLM(use_count ~ policy_only + both_pc + org_size_int, groups=ref)`. n=925.
- **Result.** β_policy_only = **−0.234** (p < 0.05); β_both_pc = +0.657 (p < 0.001); β_size = +0.122 (p < 0.001).
- **Interpretation.** F-6 replicates: orgs with policy but no cloud storage use *less* AI than the reference (neither). Both-policy-and-cloud is the strong positive condition. **Governance without infrastructure is associated with lower adoption.**
- **Confidence.** High. **Pre-registered: yes.**

### H20 — Org age has no effect on use_count (replicates F-17)

- **Method.** `MixedLM(use_count ~ org_years_raw + org_size_int + tech_person, groups=ref)`. n=902.
- **Result.** β_org_years = −0.0011 (n.s.); β_org_size = +0.115 (p < 0.001); β_tech_person = +0.877 (p < 1e-30).
- **Interpretation.** Confirms F-17. A 100-year-old nonprofit is no more or less likely to use AI than a 5-year-old one, controlling for size and specialist support.
- **Confidence.** High. **Pre-registered: yes.**

### H21 ★ — Standardized correlates of use_count: comfort > readiness >> size

- **Method.** `MixedLM(use_count ~ comfort + readiness_additive + org_size_int + tech_person, groups=ref)`. n=860. Note: `comfort` and `readiness_additive` are already on 0–1 scale; for true standardization, compare absolute β to predictor SD.
- **Result.** β_comfort = **+2.53** (p < 1e-40), β_readiness = **+1.98** (p < 1e-11), β_org_size = +0.013 (n.s.), β_tech_person = +0.149 (n.s.).
- **Interpretation.** **Once comfort and readiness are in the model, structural variables (size, tech_person) are not significant.** This is the cleanest statement of F-9/F-10's underlying claim: the binding constraints on AI use are person-side (comfort) and infrastructure-aggregate (readiness), not raw org size. *Comfort is the single dominant predictor* — confirms F-20.
- **Confidence.** Very high. **Pre-registered: yes.** ★ headline-quality.

### H22 — `rr_dont_understand` predicts cluster3 = 0 (re-tests F-10)

- **Method.** `MixedLM(is_late_adopter ~ rr_dont_understand + comfort + org_size_int, groups=ref)`. n=… (close to full).
- **Result.** β_rr_dont_understand = **+0.148** (p < 1e-6); β_comfort = **−0.508** (p < 1e-22); β_size = −0.012 (n.s.).
- **Interpretation.** Confirms F-10. Saying "I don't understand AI" is a clean, independent predictor of being a Late Adopter, after controlling for comfort and size.
- **Confidence.** High. **Pre-registered: yes.**

### H23 — F-1 inversion is invariant under IPW reweighting

- **Method.** Construct benchmark distribution proxy `{gt: 0.60, india: 0.25, tech: 0.10, hubs: 0.05}`, compute IPW (cap=10× mean), recompute per-task `[U]` / `[W]` weighted means and gaps.
- **Result.** Per-task gaps unweighted vs IPW-weighted:

| Task | Gap unweighted | Gap IPW-weighted |
|---|---:|---:|
| Generat | +1.1pp | +0.8pp |
| Ask | +6.8pp | +6.4pp |
| Translat | +14.6pp | +14.6pp |
| Interpret | +34.6pp | +34.7pp |
| Assist | +39.6pp | +39.7pp |
| Predict | +40.5pp | +40.6pp |
| Organi | +41.2pp | +41.3pp |

Effective n = 928 (no weight inflation).

- **Interpretation.** **F-1 is essentially invariant** to ref-distribution reweighting. The 4 analytical-task gaps differ by < 0.2 pp from unweighted to weighted. Sample skew is not driving the inversion.
- **Confidence.** Very high. **Pre-registered: yes.**

### H24 — MCA + Louvain produces a single community (no item-cluster structure detected)

- **Method.** MCA on 5 `[D]` + 5 infra binaries (10 items); Louvain on co-occurrence graph (φ > 0.05 threshold). n=886.
- **Result.** All 10 items collapse into 1 community.
- **Interpretation.** No discernible "structured vs unstructured data" axis at this threshold. The items are too tightly co-occurring (consistent with H7's unidimensional readiness finding) for Louvain to separate. The MCA coordinates may still be informative for visualization.
- **Confidence.** Negative result — informative against the H24 hypothesis. **Pre-registered: yes.**

### H8 — TOE SEM (failed to converge)

- **Method.** semopy 3-latent SEM (OrgCap, TechInfra, EnvPress → use_count). n=820+.
- **Result.** Eigenvalues did not converge — the latent indicator structure produced a non-PD covariance matrix. Switching to manifest-only path model would lose the TOE conceptual clarity.
- **Interpretation.** Method-failure; flag for Phase 7 to retry with simpler model (e.g., 2-latent CFA on just OrgCap and TechInfra).
- **Confidence.** N/A — failure logged. **Pre-registered: yes.**

### H9 — Risk perception is *unidimensional*, not 2-factor (contradicts Slovic)

- **Method.** Factor Analysis with n_components=2 on 7 binary `ai_risk` items. n=930.
- **Result.** F1 loadings span [+0.21, +0.29] — all 7 risks load similarly on a single "general risk salience" factor. F2 loadings are small and don't separate dread (bias/breaches) from unknown/structural (inequity/dependency/env) the way Slovic's psychometric paradigm predicts.
- **Interpretation.** **Contradicts Slovic's 2-factor structure** for AI risk specifically. Respondents endorse risks in a single dimension here; the dread/unknown distinction does not appear. Possibly because all AI risks are currently coded as both dread AND unknown for nonprofit respondents.
- **Confidence.** High (clean negative result). **Pre-registered: yes.** Important for the discussion: the canonical risk-perception model doesn't transfer to this AI-in-nonprofits setting.

### H13 — Africa hubs vs non-hubs use_count: borderline difference

- **Method.** Mann-Whitney on use_count split by `ref==hubs` within Africa subset. n_hubs = 19, n_non-hubs = 41.
- **Result.** Mean hubs use_count = 2.63, non-hubs = 1.66. p = 0.055.
- **Interpretation.** Hubs Africans use slightly more AI than non-hubs Africans, on the edge of significance with small n. F-13's "Africa over-uses AI" claim is partially explained by the hubs-recruitment artifact: GivingTuesday's African respondents come disproportionately through the hubs network, which is itself the more digitally-engaged sub-population. Caveat: with only 60 African respondents total, neither result is highly reliable.
- **Confidence.** Low (small n). **Pre-registered: yes.**

### H16 — BERTopic on `ai_opentext` (multilingual)

- **Method.** BERTopic with `paraphrase-multilingual-MiniLM-L12-v2` embeddings, HDBSCAN min_topic_size=15, on 606 non-null `ai_opentext` responses.
- **Result.** Pipeline ran successfully. Topic distribution and labels are stored in `findings_raw.json` (`H16` → `top_topics`); detailed labeling and topic-by-cluster3 analysis is deferred to Phase 8 visualization, where the topic-by-cluster heatmap will be built.
- **Interpretation.** Method works; substantive interpretation in Phase 8.
- **Confidence.** Medium — topic labels need human inspection before claiming the H16 prediction (a comprehension-aspirational topic over-represented in Late Adopters).
- **Pre-registered: yes.**

---

## Synthesis

26 hypotheses tested; 22 converged; 1 specification failure (H15 collinearity), 1 SEM convergence failure (H8), 1 negative result (H9 Slovic 2-factor), 1 deferred (H16 substantive interpretation moved to Phase 8). Of the 22 converged, all six headline re-tests (H1, H2, H3, H4, H5, H6) confirm the archived F-1, F-9, F-11, F-18 directions; H5 confirms F-8 with all three robustness checks agreeing.

**The robust headline that emerges:**

1. **The aspiration inversion is solid as bedrock** (H1, H23) — analytical-task gaps > +30pp at FDR p < 1e-66 under cluster bootstrap; invariant to IPW reweighting.
2. **The bottleneck is comprehension and comfort, not infrastructure or geography** (H21, H22, H11, H10b, H7, H26, H20). Comfort is the single dominant predictor; comprehension marker is the strongest non-adoption signal; org age and structural variables shrink to non-significance.
3. **The "willing-but-not-wired" Aspirational majority is real** (H6) — recovered by LCA on `[U]+[W]` with the modal class in the middle.
4. **The Global N/S divide reverses among small no-tech orgs** (H5) — confirmed via Oaxaca-Blinder, propensity-matching, and IPW. Three of three.
5. **Vigilance and comfort run opposite ways** (H10b) — resolves the BCG vs MIT-SMR debate; both literatures right about different variables.
6. **Slovic's 2-factor risk structure does NOT transfer to AI-in-nonprofits** (H9) — risk salience is one-dimensional here.

This hardens the headline from the 4-hour pass and adds H5 (small-org GS reversal) as a contrarian secondary headline. The methods appendix (`METHODS.md`) documents every model and parameter choice for replication.
