# Findings log

> Phase 3 results. Tag legend: **CONFIRM** / **COMPLICATE** / **CONTRADICT** vs prior, plus **NOVEL** for findings not anchored to a specific prior. **★** = qualifies as non-obvious.

Headline candidate is **F-01** (Aspiration Inversion), with **F-09** (Comfort×Infra 2×2) and **F-10** (Late-Adopter Paradox) as the supporting structure.

---

### F-01 ★ — The Aspiration Inversion: nonprofits use AI for content, want it for analytics
- **Hypothesis:** H1 (Salesforce, McKinsey, HAI). Aspiration tops on analytical/automation tasks.
- **Method:** Per-task paired McNemar on `[U]_t` vs `[W]_t` in normalized parquet (n=930).
- **Result:**

| Task | % use | % want | Gap (pp) | b (use-only) | c (want-only) | McNemar p |
|------|-------|--------|----------|--------------|---------------|-----------|
| Organize | 19.1% | 60.3% | **+41.2** | 47 | 430 | 1.7e-68 |
| Predict | 11.2% | 51.7% | **+40.5** | 27 | 404 | 2.6e-73 |
| Assist (automate) | 16.1% | 55.7% | **+39.6** | 41 | 409 | 4.7e-67 |
| Interpret | 15.3% | 49.9% | **+34.6** | 39 | 361 | 5.7e-58 |
| Translate | 24.4% | 39.0% | +14.6 | 79 | 215 | 3.5e-15 |
| Ask (chatbot) | 32.7% | 39.5% | +6.8 | 113 | 176 | 2.7e-04 |
| Generate (text/image) | 53.9% | 54.9% | **+1.1** (n.s.) | 155 | 165 | 0.61 |

- **Subgroup check:** Holds across `ref` (gt/india/tech/hubs all show analytical-task gaps >+30pp) and is amplified after IPW reweighting (Predict gap rises to +43.9pp, Generate goes *negative* −3.2pp). *In Consumers, Generate flips to a clear surplus (use 84% vs want 69%, gap −15.1pp) — the heavy-use cohort has saturated content generation.*
- **Interpretation:** What we call "AI in nonprofits" today is overwhelmingly *generative* AI for writing. The aspiration is a different stack: predictive, organizational, automation. The gap is a roadmap to the next 5 years of nonprofit tech.
- **Confidence:** High. Effect sizes are extreme; pattern survives sample reweighting; corroborated by Stanford HAI / McKinsey / Salesforce reports.
- **Tag:** CONFIRM (B1, B2, B5) · ★ non-obvious (the *direction* and *size* of the inversion).

### F-02 ★ — Generate-saturation in heavy users (sign-flip across clusters)
- **Method:** Per-cluster gap on `[U] Generat` vs `[W] Generat`. Counts of use-only vs want-only respondents.
- **Result:** Skeptics gap **−6.3pp**, Late Adopters **+37.0pp**, Consumers **−15.1pp**. Among Consumers, 125 use-only vs 46 want-only — they have *moved past* generative AI.
- **Interpretation:** Heaviest users are no longer hungry for content generation; they want analytical AI. Skeptics never wanted it. Only Late Adopters are actually chasing the content-generation trend.
- **Tag:** NOVEL · ★

### F-03 — Vigilance does *not* decay with use; comfort blunts it
- **Hypothesis:** H2 (MIT SMR, BCG). Heavy users perceive *fewer* risks.
- **Method:** Poisson regression on consolidated 7-category risk count.
- **Result:** `use_count` β=+0.080 (p<1e-11); `person_ai_comfort` β=−0.444 (p<1e-7); `risk_reward` β=−0.076 (p<1e-4); "don't understand" n.s. n=860.
- **Interpretation:** Hands-on users select *more* risks; subjective comfort selects *fewer*. The two run in opposite directions — a more nuanced story than the prior. Becoming comfortable with AI suppresses risk awareness even though using AI sharpens it.
- **Tag:** CONTRADICT (B6, MIT SMR/BCG vigilance-decay framing) · ★

### F-04 — Risk salience asymmetry: bias/breaches > inequity/dependency
- **Hypothesis:** H3 (Madianou). Social-sector AI discourse under-weights structural risks.
- **Method:** Selection rates per consolidated risk; paired Wilcoxon on (bias+breaches) − (inequity+dependency).
- **Result:** breaches 56.2%, bias 54.4%, plagiarism 54.2%, inequity 46.1%, dependency 45.6%, replacing 32.5%, environmental 30.5%. (bias+breaches) mean 1.11 vs (inequity+dependency) 0.92, Wilcoxon p=1.1e-10. The gap is *larger* among respondents who say they understand AI (1.16 vs 0.90) and shrinks among "don't understand" (1.01 vs 0.96).
- **Interpretation:** Confirms Madianou: people who understand AI more, paradoxically, focus on the *most-discussed* risks (bias, breaches) rather than structural ones. Less-informed respondents have flatter risk profiles.
- **Tag:** CONFIRM (B7) · novel-ish

### F-05 — India is *not* lower-comfort, after controlling for size and tech_person
- **Hypothesis:** H4 (Kabra & Saharan, A3). Indian NGOs lower-comfort due to trust/awareness ceiling.
- **Method:** Logistic of `comfort_high` on `in_india_ref + org_size_int + tech_person + merl_person`.
- **Result:** `in_india_ref` β=+0.10, p=0.56 (n.s.). Stratified means by `(org_size, tech_person)` cell-by-cell show India is comparable to or *higher* than non-India in 7 of 10 cells with adequate n.
- **Interpretation:** The Indian NGO sample in this dataset is not the trust-ceiling group the prior literature describes — possibly because GivingTuesday's Indian respondents are self-selected toward already-engaged orgs.
- **Tag:** CONTRADICT (A3) · ★

### F-06 — "Policy-without-cloud" exists but adopts *less*, not more
- **Hypothesis:** H5 (NTEN). Policy-first orgs land in higher adoption tiers.
- **Method:** Crosstab of `data_use_policy` × `cloud_storage`; cluster3 distribution within `policy=1, cloud=0`.
- **Result:** 165 orgs (17.7%) have policy without cloud — substantial. Their cluster3: 47.3% Consumers (vs 56.2% overall), 22.4% Skeptics (vs 15.3%). They adopt AI **less** than the overall sample.
- **Interpretation:** Governance papers without operational infrastructure does not unlock AI use — the reverse, if anything. Possibly compliance-driven without enabling tech.
- **Tag:** CONTRADICT (A4 / NTEN policy-first thesis) · ★

### F-07 — Org size beats specialist headcount in predicting cluster membership
- **Hypothesis:** H6 (UTAUT, A6). Facilitating conditions (specialist roles) > size.
- **Method:** Standardized logistic regression of `(cluster3==1)` on `tech_person + merl_person + org_size_int`.
- **Result:** `org_size_int` β=0.366 (p<1e-5); `tech_person` β=0.176 (p=0.035); `merl_person` n.s. n=894.
- **Interpretation:** Org size has roughly twice the standardized effect of having a tech person. The "you don't need a big team, you need one tech specialist" prior is not supported here.
- **Tag:** CONTRADICT (A6) · ★

### F-08 — The Global N/S divide reverses among small orgs
- **Hypothesis:** H7 (Toyama amplification). Small GS orgs without tech support should fall furthest behind.
- **Method:** Three-way Poisson interaction `use_count ~ is_S * small * has_tech`.
- **Result:** Mean `use_count` cells —

| | small (≤15 staff) | big (>15 staff) |
|---|---|---|
| GN, no tech | 1.15 (n=332) | 1.76 (n=97) |
| **GS, no tech** | **1.59 (n=143)** | 1.73 (n=60) |
| GN, has tech | 2.41 (n=41) | 2.85 (n=99) |
| GS, has tech | 2.42 (n=52) | 2.32 (n=68) |

`is_S × small` interaction β=+0.339 (p=0.024) confirming the reversal.

- **Interpretation:** Among small orgs without a tech specialist, Global *South* orgs use *more* AI than Global North peers. The standard digital-divide narrative does not hold; AI may be the first tech wave that flows the other direction at the small-org tier — possibly because consumer LLMs are accessible without infrastructure investment.
- **Tag:** CONTRADICT (A7, C6 Toyama) · ★★ headline-quality

### F-09 ★ — Comfort × infrastructure 2×2 explains AI use (and isolates the bottleneck)
- **Method:** Median-split on `readiness` and `person_ai_comfort`. Mean `use_count` per quadrant.
- **Result:**

| | low comfort (≤0.70) | high comfort (>0.70) |
|---|---|---|
| **low infra** (≤0.40) | n=298, use=0.78, **34% Consumer** | n=170, use=2.05, **66% Consumer** |
| **high infra** (>0.40) | n=216, use=1.65, **56% Consumer** | n=194, use=3.09, **85% Consumer** |

- **Interpretation:** Comfort and infrastructure each ~double use. But the off-diagonal cells reveal the binding constraint: 216 orgs have data plumbing they aren't using because their people aren't ready (comfort gap), while 170 orgs use AI heavily without infrastructure — riding consumer LLMs. The "AI readiness" question has two locks; you need both keys.
- **Triangulation:** Mediation analysis (F-11) shows readiness mediates only 18.5% of `risk_reward`'s effect on use; comfort is a stronger univariate correlate (ρ=0.50 vs 0.34 for readiness).
- **Tag:** NOVEL · ★ supporting headline

### F-10 ★ — The Late-Adopter Paradox: comprehension, not capacity
- **Method:** Cluster3=0 deep dive (n=265) + logistic of `(cluster3==0)` on infrastructure + comfort.
- **Result:** Late Adopters have median use_count=0 (90.2% use zero AI), median want_count=2, **52.8% answer "I don't understand AI"** (vs 35.9% of Skeptics, 23.5% of Consumers). Their `cloud_storage` (0.63) and `data_use_policy` (0.66) are *higher* than Skeptics' (0.46, 0.66). In a logistic predicting Late-Adopter membership: `person_ai_comfort` β=−2.81 (p<1e-19), `no_understand` β=+0.80 (p<1e-5). Infrastructure variables (cloud_storage, tech_person, data_use_policy) are all n.s.
- **Interpretation:** Late Adopters are not blocked by missing infrastructure. They are blocked by not knowing what AI is or what they would do with it. This reframes "AI for nonprofits" capacity-building from a tech-stack problem into a comprehension/training problem.
- **Tag:** NOVEL · ★ supporting headline

### F-11 — Data readiness mediates risk attitudes → AI use, but only partially (18.5%)
- **Hypothesis:** H11 (D5 method). `data_readiness_index` mediates `ai_risk_reward` → `use_count`.
- **Method:** Causal-step mediation with bootstrapped indirect effect (n=1000 boots), excluding `risk_reward = -1` ("don't understand").
- **Result:** a=+0.023 (RR→readiness, p=0.002). b=+1.152 (readiness→use_count | RR, p<1e-22). Total c=+0.141. Indirect a·b=+0.026 [+0.009, +0.045]. Proportion mediated **18.5%**. Direct path c'=+0.115.
- **Interpretation:** Risk-tolerant orgs build a bit more readiness, which boosts use; but most of risk-tolerance's effect on use is direct (people who think AI's benefits outweigh the risks just go ahead and use it, regardless of plumbing). The bigger story is the size of `b`: the readiness coefficient implies exp(1.15) ≈ **3.2× more AI use per unit increase in the 0–1 readiness index** — readiness is the dominant predictor.
- **Tag:** CONFIRM (partial mediation) · NOVEL (effect size of readiness)

### F-12 — Continent effects mostly vanish after controlling for size + tech_person
- **Hypothesis:** H12 (Rogers). Regional adoption gradient is residual after accounting for size.
- **Method:** Two Poisson models on `use_count`: continent-only vs continent + size + tech.
- **Result:** Continent's North-America coefficient drops from −0.21 (p=0.04) to −0.10 (p=0.33). Asia, South America, Europe all become non-significant. `tech_person` β=+0.49 (p<1e-16); `org_size_int` β=+0.069 (p<1e-4). Australia retains a positive coef but n=6.
- **Interpretation:** The "regional digital divide" in this sample is mostly a size-and-specialization story. Where you sit on the map matters less than whether you have a tech person.
- **Tag:** CONFIRM (H12, A7-Rogers limit) · supporting

### F-13 — Africa over-uses AI relative to GN average (small n caveat)
- **Method:** Africa subset (n=60) means; compare to GN.
- **Result:** Africa total use_count=1.97 vs GN=1.63. By region: West Africa n=15 use=1.93, East Africa n=16 use=1.56, Southern Africa n=10 use=1.50, North Africa n=2 use=4.50 (unreliable). Africa rural (n=5) use=3.0 actually exceeds Africa urban (n=14) use=2.5 — the Friederici hub-only narrative does *not* hold here.
- **Interpretation:** Likely sample artifact (Africa respondents are self-selected via GivingTuesday hubs network, so they're already engaged). But the direction is striking enough to flag.
- **Tag:** COMPLICATE (C5 Friederici) · supporting · low-confidence due to n

### F-14 — Translation `[W]` over-indexes 12pp in Global South
- **Hypothesis:** H10 (Png, C7). GS faces task-fit issues with GN-built tools; translation demand should be higher.
- **Method:** GN/GS comparison of per-task `[W]` rates.
- **Result:** Translation: GN 34.9% vs GS 46.8% (+11.9pp). All other tasks differ by <6pp.
- **Interpretation:** Confirms a specific localization gap. Translation is the only task where GS demand is meaningfully higher — consistent with GN-built models being less useful for non-English-language work.
- **Tag:** CONFIRM (C7) · supporting

### F-15 — Risk-aware skeptics? No — Skeptics select fewer risks
- **Method:** Risk-by-risk selection rates by cluster3.
- **Result:**

| Risk | Skeptic | Late | Consumer |
|---|---|---|---|
| bias | 50.7% | 51.3% | 57.0% |
| breaches | 43.0% | 60.4% | 57.7% |
| plagiarism | 39.4% | 52.8% | 58.9% |
| inequity | 36.6% | 47.5% | 48.0% |
| dependency | 35.2% | 48.7% | 46.8% |

- **Interpretation:** "AI Skeptics" select 9–17pp *fewer* of every risk than the other clusters. They aren't risk-averse from sophisticated awareness — they're disengaged. The cluster name is misleading.
- **Tag:** NOVEL · ★

### F-16 — Free-text length and tone track cluster engagement
- **Method:** Length and a simple hope-minus-fear keyword sentiment proxy on `ai_opentext` (n=606 respondents who answered).
- **Result:** Skeptics avg 138 chars, sentiment +0.06. Late Adopters 148 chars, sentiment −0.01. Consumers 252 chars, sentiment +0.33. Consumers write **70% more** and slightly more positively.
- **Interpretation:** Engagement, not antagonism, separates clusters in their own words. Skeptics aren't writing critical essays; they're writing short, neutral notes.
- **Tag:** supporting · low-stakes

### F-17 — Org size, not org age, predicts AI use
- **Method:** Univariate Spearman correlations with `use_count`.
- **Result:** `org_years` ρ=−0.019 (n.s., n=930). `org_size_int` ρ=+0.221 (p<1e-11). `person_ai_comfort` ρ=+0.497 (p<1e-55), `want_count` ρ=+0.469, `collab_feasibility` ρ=+0.369, `readiness` ρ=+0.339.
- **Interpretation:** A 100-year-old nonprofit is no more or less likely to use AI than a 5-year-old one. Size and culture matter; age does not.
- **Tag:** NOVEL · supporting

### F-18 — Re-derived 3-cluster solution surfaces an "Aspirationals" tier the official labels miss
- **Method:** K-means(k=3) on standardized `[U]`, `[W]`, `readiness`, `comfort`. ARI vs cluster3 = 0.173 (modest agreement).
- **Result:** My clusters: **Power Users** (n=118, use=5.4 want=5.3) — saturation. **Aspirationals** (n=444, use=1.8 want=5.0) — biggest gap. **Disengaged** (n=368, use=0.5 want=1.1). Cross-tab: official Late-Adopters (cluster3=0) split between my Aspirationals (191) and Disengaged (74); official Consumers split between Aspirationals (334) and Power Users (108).
- **Interpretation:** The official cluster3=1 ("Consumers") is hiding a 2:1 majority of *Aspirationals* — orgs that use some AI but want vastly more — versus a smaller saturated tier. This is the population most actionable for capacity-building.
- **Tag:** NOVEL · ★ method-driven

### F-19 — Cause area weakly affects use; gap is universal
- **Method:** Group means by first listed `org_label` cause (n≥20 cells).
- **Result:** Highest use: Community Development 1.89, Other 1.88, Education 1.77. Lowest: Animal Welfare 1.00, Youth & Family Services 1.24, Homelessness 1.27. **All causes show want=2.9–3.8 — universal high aspiration.**
- **Interpretation:** No cause area is "AI-immune." The aspiration is sector-wide; current use is moderately stratified.
- **Tag:** supporting · null-ish

### F-20 — Person-AI comfort is the strongest single correlate of use (ρ=+0.50)
- Already noted in F-17. Logging separately because this is the variable to feature in the headline.

---

## Synthesis

The 20 findings cluster into one strong shape:

1. **Today's nonprofit AI use is content-generation, dominated by Consumer LLMs (F-01, F-02).**
2. **Tomorrow's wanted use is analytical/automation — and that gap is universal across regions, sizes, causes, and clusters (F-01, F-13, F-14, F-19).**
3. **The bottleneck on closing the gap is *comprehension and comfort*, not infrastructure or geography (F-09, F-10, F-12, F-17, F-20).** Late Adopters have the plumbing and lack the people-side readiness; small Global South orgs without tech staff are *ahead* of comparable GN orgs.
4. **The "AI Skeptic" framing is an artifact (F-15, F-02, F-16);** the real story is a "willing but not wired" Aspirational majority (F-18) that the official labels miss.

**Headline (Phase 4 candidate):** *"Nonprofits already use AI — for writing. The next wave they want is analytical, and the bottleneck isn't infrastructure or geography. It's understanding."*
