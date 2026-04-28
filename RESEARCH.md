# RESEARCH.md — Prior work, methods, and disagreement map

> Compiled across **8 streams (A–H)** with **244 paper-cards** in `analysis/papers/`. Stream-synthesis paragraphs distill each stream; the disagreement map identifies open empirical questions this dataset can adjudicate. Paper-card IDs (e.g., A14, B7, C2, F18) are referenced throughout. The auto-generated BibTeX export is at `bibliography.bib`.

## Coverage

| Stream | Topic | Cards | Peer-reviewed | Verified URLs |
|---|---|---|---|---|
| A | Nonprofit technology adoption | 25 | ≥15 | 25/25 |
| B | AI adoption in social/public sector | 31 | 14 | 30/31 |
| C | Global North/South digital divide | 26 | 21 | 25/26 |
| D | Survey statistical methods | 36 | 35 | 36/36 |
| E | Risk perception & technology acceptance | 35 | 32 | 35/35 |
| F | Free-text and computational text analysis | 29 | 18 | 27/29 |
| G | Capacity building, training, intervention design | 32 | 26 | 32/32 |
| H | Sample bias, non-probability surveys | 30 | 21 | 30/30 |
| **Total** | | **244** | **≥182** | **240/244** |

## Stream syntheses

### Stream A — Nonprofit technology adoption

The dominant prior across this stream is that **organizational capacity (size, specialized roles, infrastructure) outweighs environmental factors (geography, sector pressure)**. This is consistent with our F-7 (size beats specialist headcount) and F-12 (continent vanishes after size). Two notable disagreements: (a) Kabra & Saharan (A3) say *awareness* is the binding constraint, but our sample contradicts this for India specifically; (b) NTEN (A4) says *budget* is primary, but our F-9 / F-10 suggest comfort and comprehension matter more than infrastructure once size is held constant. The TOE/UTAUT/Diffusion canon (A6, A7, A14, A21, A22) all align with size-dominance — a robust finding across 60+ years of innovation-adoption research.

### Stream B — AI adoption in the social / public sector

The Stream B literature converges on three things and disagrees sharply on one. **Consensus 1**: the intent-action gap is real and large; McKinsey 2024/2025 (B5, B13), Salesforce 2024 (B2), Stanford HAI/Project Evident 2024 (B14), Mikalef et al. 2019 (B26), Bhattacherjee & Sanford 2009 (B28) all measure intention-to-use ratios in the same neighborhood (~3–4× the action ratio); F-1 sits squarely in that distribution. **Consensus 2**: governance and comprehension, not infrastructure, are the binding constraints at the firm level — Deloitte Q4 2024 (B4), McKinsey 2025 (B13), Wirtz et al. 2019/2020 (B15, B16), HAI/Project Evident 2024 (B14) corroborate F-9 and F-10. **Consensus 3**: AI-risk discourse over-weights bias/breaches and under-weights structural risks; Madianou (B7), Mohamed/Png/Isaac (B21), Eubanks (B20), Whittlestone et al. (B31) all push the same direction; F-4 confirms with a 19pp asymmetry that *widens* among self-described "understanders".

The big **open debate** is whether the GenAI-skewed adoption shape will rebalance (HAI/McKinsey: yes, B1/B5/B9/B13) or is structural (Madianou/Mohamed et al./Berendt/Bondi: no, B7/B21/B25/B24). F-2 supports rebalance at the top; F-1/F-10/F-14 support structural at the long-tail end. Likely synthesis: **the rebalance is happening at the top of the distribution and stalling at the bottom** — the "willing but not wired" shape F-18 surfaces.

### Stream C — Global North/South digital divide

The Stream C literature splits along a sharp theoretical fault line. **Heeks (C1, C13, C14) and Toyama (C6)** argue the GN/GS divide reappears at the institutional level (adverse incorporation, design-actuality gaps, amplification). **Avgerou (C8) and Nemer (C2)**, with Arora (C19) and the data-colonialism critics (C15, C9, C10), argue the divide is mis-measured: GS users are sophisticated and locally rational; the gaps live in extractive *terms* of incorporation. Our F-8 (small-org N/S reversal) and F-12 (continent vanishes after size) sit closer to the Avgerou/Nemer pole; our F-14 (translation gap) and the Sambasivan/Bender mechanism (C16, C17) recover a Heeks-flavored institutional gap on a *specific* axis (language, data infrastructure for analytical AI). **Synthesis**: the access divide has flipped or vanished for consumer LLMs, but a Heeks-style adverse-incorporation gap persists on language fit, data infrastructure for analytical AI, and the institutional capacity required to escape "stochastic-parrot" defaults.

### Stream D — Survey statistical methods

The state-of-the-art for a survey of this design (n=930, mostly categorical, opt-in, multi-source) prescribes a pipeline that diverges from the 4-hour pass on six fronts. **(1) Typology** — K-means/HDBSCAN replaced by Bernoulli LCA on `[U]/[W]/[D]` (D1–D5), K chosen by joint BIC + BLRT + entropy, downstream covariate regressions via three-step BCH. **(2) Latent traits** — additive readiness index replaced by 2PL on the `[U]` block (D7) and GRM on graded items (D6); MIRT for the `[U]×[W]×[D]` cross-block (D9). **(3) Decomposition** — Oaxaca–Blinder (D14, D15) with Jann's normalisation (D16); RIF regression (D17) for distributional gaps. **(4) Inference under non-probability sampling** — AAPOR governance (D21); raking on `ref × org_size × continent` via Deville–Särndal calibration (D20); Mercer/Lau/Kennedy (D18) framework. **(5) Multilevel structure** — every regression as `MixedLM` with random intercept on `ref` (D22, D23); Fay-Herriot small-area for sub-domains (D25). **(6) Mediation, multiple testing, free text** — SEM (D11–D13) with Hu/Bentler cutoffs; Imai–Keele–Tingley sensitivity ρ (D31); BH-FDR at q=0.05 (D28); BERTopic with NPMI coherence (D35) and word-intrusion validation (D36). **The takeaway**: roughly half the archived findings (F-1, F-3, F-7, F-9, F-12) need to be re-tested under this stack, not merely re-described.

### Stream E — Risk perception & technology acceptance

Slovic's psychometric paradigm (E1, E4) and the affect heuristic (E2, E3) jointly predict a "dread + unknown" hazard like AI should produce risk inventories shaped by **availability** (E5), not structural analysis: bias and breaches sit prominently; inequity and dependency under-index (F-4). Madianou (E26) and the FAT* tradition (E27, E28) explain why this asymmetry isn't neutral.

The headline tension between **F-3** and the popular "comfort breeds vigilance-decay" narrative resolves via two literatures. The MIT SMR / BCG comfort-blunts-risk framing aligns with the *misuse* end of Parasuraman & Riley (E19) and over-reliance in Buçinca et al. (E25). But Lee & See (E14) and the trust-as-calibration tradition predict the opposite: hands-on use should *improve* risk discrimination. **F-3 resolves the tension**: comfort and use are different mechanisms running in opposite directions. Comfort (the affective signal) suppresses risk count; use (the analytic signal) raises it.

The **algorithm-aversion vs algorithm-appreciation debate** (E7 Dietvorst vs E8 Logg) maps onto our cluster structure. Dietvorst's aversion appears among the *previously-burned*; Logg's appreciation among the *never-tried*. F-1's inversion (low use, high want for analytical tasks) is consistent with appreciation among the never-tried; F-2's sign-flip is aversion in saturated users. The **TAM lineage** (E21–E23) frames F-9 as comfort ≈ ease-of-use × dispositional trust; infrastructure ≈ facilitating conditions. F-20's primacy of comfort suggests the binding constraint is **PEOU, not PU** — an inversion of canonical TAM ordering.

### Stream F — Free-text and computational text analysis

Plan: BERTopic with `paraphrase-multilingual-MiniLM-L12-v2` embeddings (F4, F6) for the multilingual `ai_opentext` corpus, validated against (a) classical LDA, (b) STM with `cluster3` and `org_size` as prevalence covariates, and (c) human thematic coding. Three drivers. First, the corpus is short, mixed-language, and small (~600 documents) — the regime where Egger & Yu (F18) show bag-of-words LDA loses semantic signal. Second, multilingual-distillation training (Reimers & Gurevych, F6) maps Hindi, English, and code-mixed responses into a shared space; IndicBERT (F25) and MuRIL (F26) are backstops. Third, **two-track validation** is needed (Chang et al. F13: held-out perplexity can anti-correlate with interpretability) — quantitative C_v / C_npmi (F11, F12) plus qualitative Braun–Clarke (F21) intruder. STM (F14–F16) provides the *parametric* covariate-effect channel BERTopic lacks. Sentiment triangulation across VADER (F22), LIWC (F23), AFINN (F24) tests F-16's tone claim with three independent lexicons.

### Stream G — Capacity building, training, intervention design

Three intervention design principles for F-10's comprehension bottleneck. **(1)** Comprehension is a *biologically secondary*, schema-acquisition problem (G1–G3, G14, G15) — exposure-based "just give them ChatGPT" doesn't transfer; explicit instruction with worked examples, segmenting, and learner-tailored sequencing (G4–G7) is required. **(2)** Comprehension is necessary but insufficient: training transfer fails 60–80% of the time when work-environment supports (peer support, supervisor backing, on-the-job practice) are missing (G17, G18, G20); interventions must be end-to-end. **(3)** Most cost-effective delivery in resource-constrained settings is *cohort-based, peer-anchored, locally-tailored* (G8–G11, G22–G24, G32) — analogous to the ag-extension shift from "Training-and-Visit" to farmer-field-schools. Tiered design: light-touch peer networks for AI Consumers (cluster3=1, expertise reversal caution); deep andragogy-aligned, problem-centered cohorts for Late Adopters (cluster3=0). **Critical implication for F-10**: infrastructure-only investments (cloud, policies) will *not* close the gap — Late Adopters already have higher cloud_storage and data_use_policy than Skeptics yet remain stuck on comprehension.

### Stream H — Sample bias, non-probability surveys

This is a textbook non-probability, multi-frame, opt-in design with four self-selected sub-frames (`gt` 549, `india` 251, `tech` 86, `hubs` 44). Under AAPOR (H1, H2) all inference is model-dependent; canonical defenses are quasi-randomization (IPW; H10, H11, H12, H19) and calibration to known auxiliaries (H15, H16, H17, H23). Empirical evidence (H5 Xbox, H6 Pew): non-representative samples can recover valid estimates, but only when weighting auxiliaries also explain the outcome, and residual bias is typical. **Phase 5 plan**: inverse-frequency reweighting on `ref × org_size × region` against a hybrid NCCS (H27) / Candid (H28) / Johns Hopkins-CCSS (H29) marginal set, raked, trimmed at 1st/99th percentile, then every headline regression run unweighted AND weighted. **Phase 6 layer**: multilevel model with `ref` random intercept (Lohr H22; Park/Gelman/Bafumi H4; Wang et al. H5). Sensitivity per Little & Rubin H24. **Honest limit, recorded here**: no perfect benchmark exists for global NGOs (NCCS/Candid cover only US 501(c)(3); CCSS data are coarse and dated). We report (a) unweighted, (b) US-slice IPW-weighted, (c) `ref`-multilevel estimates side-by-side; finding is robust only if it survives all three.

---

## Disagreement map (debates this dataset can adjudicate)

10 explicit disagreements where the dataset's empirical pattern adjudicates. Each row gives the contending positions and which finding decides.

| # | Debate | Side X | Side ¬X | Empirical adjudicator |
|---|---|---|---|---|
| 1 | Will GenAI-skewed adoption rebalance? | HAI / McKinsey: yes (B1, B5, B9, B13) | Madianou / Mohamed: no, structural (B7, B21) | F-2 (top of distribution) vs F-1, F-14 (long tail). **Both sides partly right**; rebalance happens at the top, stalls at the bottom. |
| 2 | Does the GN/GS divide reappear at the institutional level? | Heeks / Toyama: yes (C1, C6, C13, C14) | Avgerou / Nemer / Arora: no — substantive null (C2, C8, C19) | F-12, F-8 sit with Avgerou/Nemer at the cluster level; F-14 (translation), Sambasivan (C17), Bender (C16) recover Heeks at task-fit and language axes. |
| 3 | Comfort breeds vigilance decay vs improves calibration? | BCG / MIT SMR / Parasuraman & Riley over-reliance: comfort blunts vigilance | Lee & See trust-as-calibration: hands-on improves | **F-3** says both: comfort suppresses (affective channel), use raises (analytic channel). |
| 4 | Algorithm aversion vs algorithm appreciation? | Dietvorst (E7, E9): aversion after seeing error | Logg (E8): appreciation when no error visible | F-1 fits Logg (never-tried appreciate analytical AI); F-2 sign-flip in Power Users fits Dietvorst (saturation aversion). |
| 5 | Is the binding constraint comprehension or infrastructure? | Kabra & Saharan / Salesforce digital-maturity: awareness + maturity (A3, A5) | NTEN / Heller: budget / infrastructure (A4) | **F-10 decisive**: Late Adopters have higher cloud_storage/policy than Skeptics; the bottleneck is "don't understand AI" (52.8%). |
| 6 | Does governance precede infrastructure or vice versa? | NTEN: governance enables adoption (A4) | Salesforce digital-maturity: bidirectional (A5) | **F-6**: policy-without-cloud actually adopts *less*, not more — governance ≠ pre-step. |
| 7 | Is org_size a sufficient predictor or do specialist roles dominate? | UTAUT facilitating conditions (A6): specialists matter most | Damanpour & Schneider (A22), Saxton & Guo (A16): size dominates | **F-7**: both significant; size has 2× the standardized effect of `tech_person`. UTAUT only partially supported. |
| 8 | Does the bias/breaches over-weight reflect availability or sophistication? | Slovic affect heuristic (E2): availability bias | Madianou structural critique (E26): elite framing | **F-4**: gap *widens* among "understanders" — supports both *and* identifies a vicious cycle. |
| 9 | Should we treat aspiration gap as a transient friction or a structural ceiling? | McKinsey "rewiring" (B13): friction, addressable | Madianou / Berendt / Bondi (B7, B25, B24): structural | F-2 sign-flip → friction at the top; F-10 comprehension bottleneck → ceiling at the bottom. |
| 10 | Does the digital divide flip in the AI era for small orgs? | Friederici / Heeks / Toyama: small-GS orgs fall further behind | Arora / Nemer / data-colonialism: small-GS orgs leverage cheap consumer tools | **F-8 contrarian**: small no-tech GS orgs *outperform* GN peers in `[U]` count. To be re-tested under Oaxaca + PSM + IPW (H5). |

---

## What's left: hypotheses + Phase 6 execution

Pre-registered hypotheses (n=26) live in `analysis/hypotheses.md`. Phase 6 will execute them in batches by method (LCA, IRT, SEM, multilevel, Oaxaca, mediation, BERTopic, MCA+Louvain) and log every result — including nulls — to `analysis/findings.md`.
