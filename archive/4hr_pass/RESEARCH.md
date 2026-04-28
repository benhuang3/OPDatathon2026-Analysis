# RESEARCH.md — Prior work and methods

> Phase 2 deliverable. Compiled from four parallel research streams (A–D). Citations were assembled by sub-agents from public-record knowledge — link-verify before publication.

## Stream A — Nonprofit technology adoption

| # | Source | Takeaway | Confirms / Complicates / Contradicts vs this dataset |
|---|--------|----------|------------------------------------------------------|
| A1 | Godefroid, Plattfaut, & Niehaves (2024), *Nonprofit Mgmt & Leadership* — TOE barriers to NGO tech | Internal capacity (budget, IT skills, mgmt support) dominates over environmental factors | **Test:** Do `tech_person`/`merl_person`/`org_size`/`data_use_policy` predict `cluster3` better than `continent`/`global_north_south`? |
| A2 | Rotter et al. (2025), *arXiv:2510.15509* — SLR of 65 NGO AI studies | Adoption is "uneven and biased toward larger orgs"; six use-case categories (Engagement, Creativity, Decision-Making, Prediction, Mgmt, Optimization) | **Confirm/contradict:** Regress count(`[U]`) on `org_size` × `tech_person`; check whether small NGOs concentrate in Generate/Ask while large do Predict/Organize. |
| A3 | Kabra & Saharan (2025), *VOLUNTAS* — GenAI barriers in Indian NGOs | Awareness/trust outrank infrastructure and expertise as the *top* barrier | **Confirm:** India respondents (n=251) should show lower `person_ai_comfort` even at matched org size. |
| A4 | NTEN & Heller Consulting (2024), *Nonprofit Digital Investments Report* | Data-systems prioritization 22%→43%; security 14%→41%. 77% cite budget as the blocker | **Complicate:** Test whether `data_use_policy=1 ∧ cloud_storage=0` ("policy-first") is a non-trivial subgroup. |
| A5 | Salesforce.org (2022/2024), *Nonprofit Trends + Digital Maturity Index* | 76% of nonprofits lack a data strategy; high-maturity 3.5× more motivated | **Confirm:** Lightweight maturity index from `cloud_storage`+`data_use_policy`+`merl_person`+`[D]` count → correlate with `collab_feasibility` and `cluster3`. |
| A6 | Venkatesh et al. (UTAUT, 2003 + 2022 reviews), via Curtis et al. (2010) | "Facilitating conditions" (specialized roles) predict adoption more than individual effort expectancy | **Confirm:** Presence of `tech_person`/`merl_person` should beat `org_size` in a logistic of high-cluster membership. |
| A7 | Rogers (2003), *Diffusion of Innovations* — applied via xarxanet GS evidence | NGO digital adoption follows sharp regional gradient (Africa 55% vs NA 86%) | **Complicate / contradict:** Decompose variance in `[U]` between `continent` and `org_size`; if size dominates, the "diffusion" thesis is weaker. |

## Stream B — AI adoption in the social / nonprofit sector

| # | Source | Takeaway | Confirms / Complicates / Contradicts |
|---|--------|----------|---------------------------------------|
| B1 | Stanford HAI, *AI Index 2024* (Maslej et al.) | GenAI doubled 2022→23; concentrated in marketing/content; analytical uses lag | **Confirms** our 54% Generate vs ~15% Predict/Interpret — and we can extend to the nonprofit sector specifically. |
| B2 | Salesforce, *Nonprofit Trends 6th Ed.* (2024) | ~83% see AI as transformative, ~17% have integrated; blockers are skills, ethics, data quality | **Textbook aspiration gap.** Quantify per-task gap and break down by `cluster3`. |
| B3 | BCG, *AI at Work 2024: Friend or Foe?* | Frontline workers fear displacement/bias; leaders fear governance/IP. Comfort rises with hands-on use | **Test:** Regress `person_ai_comfort` on count(`[U]`) — replicates the "comfort-with-use" curve. |
| B4 | Deloitte, *State of GenAI in Enterprise Q4 2024* | Trust/risk concerns block scaling more than tech; ~25% feel "highly prepared" on governance | **Complicate:** Small nonprofits lack governance scaffolding entirely; `collab_feasibility` may dominate. |
| B5 | McKinsey, *State of AI 2024* | GenAI hit 65% adoption; value concentrated in marketing/sales/eng; analytics & forecasting lag despite higher claimed ROI | **Confirms the inversion** — highest-value uses are least adopted. Anchor for the headline. |
| B6 | Renieris, Kiron, Mills (MIT SMR / BCG, 2023) | Smaller orgs that *buy* AI inherit unmanaged third-party risk; perception lags exposure | **Counterintuitive test:** Heavy `[U]` users may select *fewer* `ai_risk` items (vigilance decay). |
| B7 | Madianou (2021), *Information, Communication & Society* — "Nonhuman humanitarianism" | "AI for good" under-weights inequity/dependency vs bias/privacy | **Test:** Compare selection rates across `ai_risk` items; predict `bias`/`breaches` >> `inequity`/`dependency`. |
| B8 | Candid + GivingTuesday Pulse (2023–24) | Bimodal nonprofit tech: small "digital-native" tier vs long tail of paper/Excel orgs | **Confirms:** `cluster3` operationalizes this bimodality directly. |

## Stream C — Global North / South digital divide

| # | Source | Takeaway | Confirms / Complicates / Contradicts |
|---|--------|----------|---------------------------------------|
| C1 | Heeks (2022), *ITD* — "Adverse digital incorporation" | The "divide" framing is outdated; GS *is* online but on disadvantageous terms (data extraction, dependency) | **Complicates** our null `cluster3` finding — predicts the divide reappears on *which* `[U]`/`[W]` tasks differ N/S. |
| C2 | Nemer (2022), *Technology of the Oppressed* (MIT Press) | Deficit narrative is empirically wrong at the user level; gaps live in *institutional infrastructure* | **Confirms** the null on individual measures (`person_ai_comfort`, `cluster3`); predicts gap reappears on `tech_person`, `org_size`. |
| C3 | NASSCOM Foundation & Sattva (2023), *Tech4Good in Indian NGOs* | ~25% of Indian NGOs have a dedicated tech person; rural/Tier-3 lag metros sharply on tooling | **Directly testable** with `india_rural_urban` × `tech_person`. |
| C4 | Dasra & Bain (2024), *India Philanthropy Report — Digital & AI chapter* | Indian NGO AI interest far outpaces use; binding constraint is data readiness/donor-funded capacity | **Predicts** large `[W]−[U]` gaps in India vs GN. |
| C5 | Friederici, Ojanperä & Graham (2020), *EJISDC* | African digital-economy participation concentrated in hubs; rural civil society sees little leapfrog | **Test on Africa subset (n≈60)** with `af_region` and `hubs_rural_urban`. |
| C6 | Toyama (2015), *Geek Heresy* + "Law of Amplification" (2011) | Tech *amplifies* existing institutional capacity; new waves widen gaps where capacity is asymmetric | **Contradicts** any "AI as leveler" reading. Predicts N/S × `org_size` × `tech_person` interaction. |
| C7 | Png (2022), *ACM FAccT* — "At the tensions of South and North" | GS orgs face GN-built tools poorly fit to local contexts; adoption can be high while *fit* is low | **Test:** Translation/language `[W]` should over-index in GS. |
| C8 | Avgerou (2021), *MISQ* — Contextual explanation | Adoption patterns reflect local rationalities, not lag on a GN trajectory | Frames the null as substantive, not artifactual. |

## Stream D — Methods (beyond χ² / logistic / k-means)

| # | Method | Where used | Why a good fit here | Python |
|---|--------|------------|---------------------|--------|
| D1 | **Latent Class Analysis (LCA)** | Bauer & Lim (2019), *NML* — typologies of nonprofit boards | Binary `[U]`/`[W]`/`[D]` columns are textbook LCA indicators; gives probabilistic typology + entropy/BIC for K | `stepmix`, `poLCA` via `rpy2` |
| D2 | **Item Response Theory (Graded Response)** | OECD PIAAC; Benitez et al. (2022) on nonprofit digital-capacity | Build *AI-readiness* and *AI-comfort* latent traits — weights items by discrimination, beats sum-scores under `ref` skew | `girth`, `py-irt`, `mirt` via `rpy2` |
| D3 | **Paired multilevel gap model** | Diener et al. (2010) on aspiration-attainment | Per-pair `(W−U)` regressed on org features via mixed-effects Tobit/beta-binomial — identifies *which orgs* have systematic gaps | `statsmodels.MixedLM`, `bambi` |
| D4 | **Oaxaca–Blinder decomposition** | Blinder (1973); Backus & Clifford (2013, *Voluntas*) on volunteer rates | Decompose any GN/GS gap into *endowments* vs *coefficients* — directly answers "smaller orgs, or different returns to same inputs?" | `oaxaca` |
| D5 | **Mediation / Path analysis (SEM)** | MacKinnon (2008); Kim & Lee (2018) on IT-capacity mediation | Test whether `data_infrastructure_index` mediates `ai_risk_reward` → `[U]`-count | `semopy`, `pingouin.mediation_analysis` |
| D6 | **Multiple Correspondence Analysis + co-occurrence network** | Le Roux & Rouanet (2010); Lindsay (2019) on board diversity | One-hot multi-selects → MCA + Louvain on org↔item bipartite — interpretable axes (operational vs programmatic AI) | `prince`, `networkx` + `python-louvain` |
| D7 | **Inverse Probability Weighting / raking** | Mercer et al. (2018, Pew); Valliant & Dever (2018) | Counter `ref` skew (gt 549 / india 251 / tech 86 / hubs 44); compare weighted vs unweighted headlines | `samplics`, scikit-learn for propensity |
| D8 | **Embedding + BERTopic on free-text** | Grootendorst (2022); Litofcenko et al. (2023) on mission statements | `ai_opentext`, `org_opentext`, `non_data_work` — cluster embeddings, join back as features | `bertopic`, `sentence-transformers` |
| D-bonus | Cluster-validation | sklearn `adjusted_rand_score`, `adjusted_mutual_info_score`; `gower` for mixed-type silhouette | Compare HDBSCAN-3 vs K-means-2 vs our re-derived LCA | sklearn, `gower` |

**Methods *not* on the standard PROJECT.md toolkit:** LCA, IRT, Oaxaca–Blinder, SEM/mediation, MCA+network, IPW, BERTopic — 7 of 8 are net-new.

---

## Testable hypotheses (consolidated)

These are the explicit prior-vs-data tests Phase 3 must run. Numbered for cross-reference in `findings.md`.

> **H1 — Aspiration gap shape (Salesforce, McKinsey, HAI).** *mean(`[W]_t`) − mean(`[U]_t`)* tops on Predict / Organize / Interpret / Assist; near-zero on Generate. Stratify by `cluster3` and `ref`. **Already supported in Phase 1; need significance + subgroup test.**

> **H2 — Vigilance decay (MIT SMR / BCG).** Among heavy `[U]` users, count(`ai_risk`) is *lower*, controlling for `person_ai_comfort` and `ai_risk_reward`. A negative coefficient on count(`[U]`) would be counterintuitive and original.

> **H3 — Risk salience asymmetry (Madianou).** Within `ai_risk`, `bias` + `breaches` >> `inequity` + `dependency`. Gap may shrink among `ai_risk_reward = -1` ("don't understand AI").

> **H4 — Trust ahead of resources (Kabra & Saharan, India).** India respondents at matched `org_size` × `tech_person` show lower `person_ai_comfort` and more risk-leaning `ai_risk_reward` than non-India peers.

> **H5 — Governance-ahead-of-infrastructure (NTEN).** A meaningful subgroup has `data_use_policy=1 ∧ cloud_storage=0`. This subgroup lands in mid/high `cluster3` tiers — contradicting the assumption that infrastructure precedes governance.

> **H6 — Facilitating conditions > size (UTAUT / Curtis).** In logistic regression of high-`cluster3` membership, presence of `tech_person` or `merl_person` shows larger standardized coefficient than `org_size`.

> **H7 — Amplification (Toyama).** `org_size` × N/S × `tech_person` interaction: GN/GS gap on count(`[U]`) is significant *only* among small orgs without a tech person, even though `cluster3` is balanced overall.

> **H8 — GS unmet-want gap (Dasra / Heeks).** Per-respondent `[W]−[U]` gap is larger in Global South than Global North, and largest in India-rural.

> **H9 — Hub effect in Africa (Friederici).** Within `continent='Africa'`, `hubs_rural_urban='urban'` respondents look like GN; rural Africa diverges sharply on count(`[U]`) and `collab_feasibility`.

> **H10 — Task-fit (Png).** GS over-indexes on translation/language `[W]` tasks; GN over-indexes on generic admin/drafting.

> **H11 — Mediation (D5 method).** `data_readiness_index` mediates the effect of `ai_risk_reward` (and of `tech_person`) on count(`[U]`). Bootstrap the indirect effect.

> **H12 — Diffusion vs size (Rogers, A7).** After controlling for `org_size`, `continent` no longer predicts count(`[U]`); the regional gradient is a *size* artifact.

---

## Where priors disagree (= where this dataset can adjudicate)

- **HAI/McKinsey** treat the Generate-skewed adoption as a natural early-adoption phase that will rebalance. **Madianou** treats it as a structural feature of "AI for good" that won't self-correct. The shape of the `[W]` distribution across `cluster3` adjudicates: if Skeptics want analytical tasks too, HAI/McKinsey win; if only Consumers do, Madianou wins.
- **BCG** says comfort grows with use; **MIT SMR** says risk awareness *fails* to grow with use. Both can be true simultaneously (comfort up, vigilance down). H2 + H3 test both axes.
- **Heeks/Toyama** predict GN/GS gaps reappear at the institutional level; **Avgerou/Nemer** predict the null is substantive. The Phase 1 null on `cluster3` is consistent with the latter; H7/H8 test the former.
