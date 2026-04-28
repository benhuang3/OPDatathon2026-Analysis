# PROJECT.md — Datathon Workflow (research-grade, 30-hour scope)

This file is the operating brief for agents working on this project. CLAUDE.md covers the **dataset**; this file covers the **work**.

## Goal

Win the OPDatathon 2026 by producing a **data-driven narrative** about the GivingTuesday 2024 AI Readiness survey (n=930) that is:

- **Novel** — surfaces non-obvious patterns, not a restatement of the data dictionary.
- **Defensible at journal-review depth** — backed by reproducible, methodologically rigorous statistical analysis grounded in ≥200 academic sources.
- **Communicable** — lands as a slide-ready story with publication-quality charts and a written report that can also stand on its own.

The 4-hour datathon-grade pass is preserved at **`archive/4hr_pass/`** (see CLAUDE.md for what's there). This brief replaces it with a **30-hour research-grade pass**: the headline shape may stay the same, but every claim must be re-tested under field-standard methods (LCA, IRT, SEM, Oaxaca–Blinder, IPW, multilevel models, multilingual NLP), grounded in a substantially deeper literature, and reported at a level that would survive peer review.

## Time budget — 30 hours

This is now a research project, not a sprint. Budget the time deliberately.

| Phase | Target | Cumulative |
|-------|--------|------------|
| 1. Re-orient & schema audit | 1 h | 1:00 |
| 2. Literature scaffold (database + search strategy) | 2 h | 3:00 |
| 3. Deep literature dive — 200 papers across 8 streams | 10 h | 13:00 |
| 4. Hypothesis crystallization | 1 h | 14:00 |
| 5. Statistical infrastructure expansion | 2 h | 16:00 |
| 6. Deep statistical analysis (full method stack) | 8 h | 24:00 |
| 7. Triangulation & robustness battery | 2 h | 26:00 |
| 8. Narrative synthesis + visualization | 3 h | 29:00 |
| 9. Writing & methodological appendix | 1 h | 30:00 |

**Slack policy.** If a phase finishes early, the slack rolls into the *next* phase, not back to Phase 6 — depth at each stage compounds. If a phase runs >25% over budget, stop and reassess; don't push through.

**Prerequisite.** This brief assumes the 4-hour datathon pass is already complete. Its output lives at **`archive/4hr_pass/`**: `archive/4hr_pass/REPORT.md`, `archive/4hr_pass/RESEARCH.md`, `archive/4hr_pass/analysis/findings.md` (20 logged findings, referred to as **F-1 … F-20** throughout this brief), `archive/4hr_pass/analysis/lib.py` (existing helpers), `archive/4hr_pass/analysis/00_orientation.md`, and `archive/4hr_pass/figures/` (6 charts). Read those before starting Phase 1. Phases here *extend and re-test* that work; they do not redo it from scratch. **Do not modify the archive** — build the new pass in fresh top-level files (`analysis/`, `figures/`, `REPORT.md`, `PAPER.md`, `RESEARCH.md`, `METHODS.md`, `bibliography.bib`).

## Datathon prompt (verbatim)

> Analyze the provided Giving Tuesday dataset and develop a data-driven narrative that uncovers novel insights and patterns.
>
> **Analysis objectives:** focus on exploration, visualization, and storytelling to produce unique insights; use charts and visuals to guide the narrative; identify trends, relationships, or unexpected findings; clearly communicate why your insights matter.
>
> **Seed questions** (use as starting points, not as the final framing):
> - What types of nonprofits are eager to adopt AI?
> - Is there a gap between how nonprofits use AI today vs. how they want to use it?
> - How do perceptions of AI risk influence nonprofit adoption?
> - Do nonprofits with stronger data infrastructure adopt AI more effectively?
>
> **Evaluation criteria:** Insight & Originality · Data Storytelling · Visualization Quality · Analytical Depth.

Optimize every decision against those four criteria; the 30-hour scope is targeted at the **Analytical Depth** dimension specifically.

## Context: GivingTuesday

A global generosity movement that runs the GivingTuesday Data Commons, aggregating donation data via partners (PayPal, Blackbaud, etc.) and sharing it openly so nonprofits can be more effective. The 2024 AI Readiness instrument is heavily skewed to GivingTuesday's main US/global list (59%) and Indian nonprofit sub-lists (27%).

## Deliverables

By the end of the project, this repo should contain:

1. **`analysis/`** — numbered scripts/notebooks, all rerunnable from the parquet files. Includes:
   - `lib.py` — reusable helpers (existing) + new: `latent_class_model`, `irt_score`, `oaxaca_decompose`, `ipw_reweight`, `sem_fit`, `multilevel_model`, `bertopic_pipeline`.
   - `findings.md` — every test logged with method, effect size, CI, FDR-adjusted p, sample, confidence. Aim for **≥40 logged findings** at this scope.
2. **`figures/`** — final chart exports (PNG + SVG). Aim for **8–12 publication-quality charts**, including model-diagnostic plots in an appendix.
3. **`REPORT.md`** — slide-ready narrative for the datathon judges.
4. **`PAPER.md`** — research-grade writeup (12–15 pages prose-equivalent): abstract, introduction, related work, data, methods, results, discussion, limitations, references. Suitable as the basis for a journal submission.
5. **`RESEARCH.md`** — full bibliography with **≥200 sources** organized by stream, each annotated with takeaway + confirms/complicates/contradicts column. ≥60 must be peer-reviewed academic papers (the rest can be high-quality industry reports, government data, dissertations).
6. **`METHODS.md`** — methodological appendix documenting every model used, parameter choices, robustness checks, and software versions. Long enough that a reviewer could replicate the analysis from this file alone.
7. **`bibliography.bib`** — BibTeX export of all 200+ sources for citation reuse.

Keep intermediate exploratory work; mark it `_scratch` so the final pipeline is unambiguous.

## Workflow

Execute the phases in order. Each phase has a **done criterion**; advancing without meeting it is the most common failure mode.

### Phase 1 — Re-orient & schema audit (≈1 h)

The 4-hour pass already produced `archive/4hr_pass/analysis/00_orientation.md`. This phase deepens it (output goes in **the new** `analysis/codebook.md`, not the archive).

- Re-read the data dictionary; cross-check every coding against the actual data (the 4-hour pass already caught the `cluster3`/`cluster2` label inversion and the `ai_risk_reward = -1` "don't understand" code; check whether further codings are wrong).
- Build a **complete codebook** as `analysis/codebook.md`: every column, dtype, valid values, source-conditional missingness, recommended treatment (numeric vs categorical vs ordinal vs ignore).
- Audit **derived variables** in the normalized parquet: are the 0–1 rescalings monotonic with the raw? Spot-check 5 random rows.
- Flag any **constructed indices** that should be IRT-validated rather than additive (the 4-hour pass used an additive `data_readiness_score` defined in `archive/4hr_pass/analysis/lib.py`; flag this for replacement in Phase 5).
- **Done when:** `analysis/codebook.md` exists, every column has a recommended treatment, and any new data-quality issues are logged.

### Phase 2 — Literature scaffold (≈2 h)

Set up the infrastructure that lets a 200-paper dive be tractable.

- Create `bibliography.bib` by extracting the 30 sources logged in `archive/4hr_pass/RESEARCH.md` and converting them to BibTeX format.
- Define a **paper-card template** (one Markdown stub per paper in `analysis/papers/`) with fields: full citation, DOI/URL, year, sample/method, key claim(s), relevance score (1–5), tag(s), takeaway, and "confirms/complicates/contradicts" against the dataset.
- Migrate the 30 sources from `archive/4hr_pass/RESEARCH.md` into paper-cards under `analysis/papers/` so they don't have to be re-found.
- Define **inclusion criteria** per stream: language (English + obvious translations), date range (mostly 2018+; classic theory papers can be older), source quality bar (peer-reviewed > major report > working paper > blog).
- Define **search strategies** per stream: a list of 5–10 search queries, target databases (Google Scholar, Semantic Scholar, arXiv, SSRN, JSTOR, NCBI, ACM/IEEE for tech, Voluntas/NML/NVSQ for nonprofit research), and target Google Scholar citation thresholds.
- **Done when:** the paper-card template and 8 search strategies exist; the existing 30 sources from `archive/4hr_pass/RESEARCH.md` have been migrated to paper-cards under `analysis/papers/`.

### Phase 3 — Deep literature dive: 200 papers across 8 streams (≈10 h)

This is where the project's claim to academic depth is built. **Fan out aggressively** — eight streams running in parallel via sub-agents, each targeting ~25 papers.

#### Stream A — Nonprofit technology adoption (≈25 papers)
TOE, UTAUT, Diffusion of Innovations, NTEN/Nonprofit Tech for Good annual reports, digital maturity indices, Salesforce Nonprofit Trends, Candid research, NCCS data work. Reach back to Rogers (2003) and Venkatesh et al. (2003) for canonical references; cover ≥5 systematic literature reviews.

#### Stream B — AI adoption in social/public sector (≈25 papers)
Stanford HAI AI Index (every relevant chapter, every year 2021–2025), McKinsey/BCG/Deloitte/MIT SMR enterprise AI surveys, MIT/Stanford academic work on AI in social services, Madianou and the "AI for good" critical literature, Rotter et al. (2025) NGO AI SLR, and the broader "aspiration gap" / "intent–action gap" literature.

#### Stream C — Global North/South digital divide (≈25 papers)
ICT4D canon: Heeks, Avgerou, Walsham, Toyama. India NGO tech: NASSCOM Foundation, Sattva, Dasra, Bain India Philanthropy. Africa-specific: Friederici, Graham, Mann; the African Online Research initiative. Latin America: ECLAC reports. AI-specific localization work: Png (2022), Birhane, Mohamed et al.

#### Stream D — Survey statistical methods (≈25 papers)
Latent Class Analysis (Vermunt, Lazarsfeld), Item Response Theory (Reckase, Embretson), Structural Equation Modeling (Kline, Bollen), Oaxaca–Blinder + extensions (Jann), IPW/raking (Mercer, Valliant & Dever), multilevel models (Gelman & Hill), small-area estimation. Method papers from JSS / Psychometrika / Sociological Methods & Research.

#### Stream E — Risk perception & technology acceptance (≈25 papers)
Slovic on risk perception, Kahneman/Tversky on probability framing, the "AI risk perception" literature (Dietvorst on algorithm aversion, Logg et al. on algorithm appreciation, Glikson & Woolley 2020 review). Trust-in-automation and trust-in-AI streams.

#### Stream F — Free-text and computational text analysis (≈25 papers)
LDA (Blei et al.), top2vec, BERTopic (Grootendorst), sentence-transformer embeddings (Reimers & Gurevych), multilingual NLP (mBERT, XLM-R, NLLB), topic-model validation (Mimno et al. on coherence). Application to nonprofit mission statements (Litofcenko et al. 2023, Suárez 2010).

#### Stream G — Capacity building, training, and intervention design in the social sector (≈25 papers)
Cognitive load theory applied to professional training, peer-learning networks in NGOs (Ebrahim, Edwards), evaluation of digital-literacy programs, the "comprehension intervention" precedents in technology adoption (e.g., extension services in agriculture).

#### Stream H — Sample bias, non-probability surveys, and convenience-sample inference (≈25 papers)
The MRP (multilevel regression and post-stratification) literature, propensity-score weighting for online panels, the AAPOR Task Force reports on non-probability samples, weighting against external benchmarks (NCCS, Candid 990 data).

#### Discipline for each stream
- Each paper-card must answer **all** template fields. No "TODO".
- Add `relevance_score` 1–5; only score-4-and-5 papers should be cited in the final report.
- Tag papers that **explicitly disagree** with each other (e.g., HAI's "early-adoption phase will rebalance" vs Madianou's "structural feature won't self-correct"). Disagreements are the seeds of testable hypotheses.
- For each stream, end with a short **stream-synthesis paragraph** in `RESEARCH.md` summarizing the consensus and the open debates.

#### Done criteria for Phase 3
- ≥200 paper-cards committed to `analysis/papers/`
- ≥60 of them are peer-reviewed academic
- ≥8 stream-synthesis paragraphs in `RESEARCH.md`
- ≥10 disagreements explicitly mapped (claim X paper says A; claim X paper says ¬A)
- `bibliography.bib` exported

### Phase 4 — Hypothesis crystallization (≈1 h)

Distill the literature into testable hypotheses against this dataset.

- Aim for **≥25 testable hypotheses**, organized by which stream they came from.
- Each hypothesis must be expressed as: **(a) the prior claim**, **(b) the operationalization on this dataset's columns**, **(c) the statistical test that decides it**, **(d) what direction would confirm vs contradict the prior**.
- Pre-register hypotheses in `analysis/hypotheses.md` *before* running any new analysis. This protects against post-hoc storytelling.
- **Cluster hypotheses** by which method will test them — so Phase 6 can run them in batches efficiently.
- **Done when:** ≥25 pre-registered hypotheses are in `analysis/hypotheses.md`, each one has a concrete test plan, and the hypotheses cover at least 6 of the 8 streams.

### Phase 5 — Statistical infrastructure expansion (≈2 h)

The 4-hour pass left a `lib.py` at `archive/4hr_pass/analysis/lib.py` that is solid for descriptive and basic-inferential work. **Copy it as the starting point for the new `analysis/lib.py`** (it already has `compare_groups`, `gap_analysis`, `subgroup_sweep`, `bootstrap_ci`, `fdr_adjust`, `data_readiness_score`, plus loading helpers). This phase builds the field-standard methods on top.

Confirm `requirements.txt` is installed (`pip install -r requirements.txt`) before writing any of the new helpers — they pull in `stepmix`, `girth`, `semopy`, `dowhy`, `bertopic`, `sentence-transformers`, and friends, none of which are in the base environment.

Add to `analysis/lib.py` (or split into `analysis/methods/`):

- **`latent_class_model(df, items, k_range)`** → fit LCA via `stepmix` for k = 2..6, return BIC/AIC/entropy table + best model, posterior class memberships, item-response probabilities. Used to **replace** the K-means typology in F-18.
- **`irt_score(df, items, model='2pl')`** → fit 2-PL IRT (binary) or graded-response model (ordinal) via `girth`, return discrimination + difficulty params, person scores, model fit. Used to **replace** the additive `data_readiness_score`.
- **`oaxaca_decompose(df, outcome, group_col, predictors)`** → Oaxaca–Blinder decomposition of a group gap into endowments vs coefficients via `linearmodels` or manual implementation. Used to decompose the GN/GS use-count gap.
- **`sem_fit(df, model_string)`** → wrap `semopy` so we can fit the TOE/UTAUT-style causal-graph models that the literature expects.
- **`ipw_reweight(df, target_population, vars)`** → propensity-weighted reweighting against an external benchmark (NCCS or Candid sector totals where available, or a cleanly stratified target). Replace the inverse-frequency reweighting from the 4-hour pass.
- **`multilevel_model(df, formula, group_col)`** → wrap `statsmodels.MixedLM` or `bambi` so we can put `ref` as a random intercept on every headline regression.
- **`mediation_full(df, x, m, y, n_boot=2000)`** → keep the existing manual Baron–Kenny but extend with `dowhy` or `pingouin` for sensitivity analysis.
- **`bertopic_pipeline(texts, lang_detect=True)`** → multilingual topic modeling on `ai_opentext` and `org_opentext` via `bertopic` with `paraphrase-multilingual-MiniLM-L12-v2`. Replace the keyword-based sentiment proxy.
- **`mca_louvain(df, multi_select_cols)`** → Multiple Correspondence Analysis + Louvain community detection for multi-select co-occurrence patterns.

Each new helper must include:
- A docstring with the canonical reference (e.g., "LCA: Vermunt & Magidson 2005").
- A returned dataclass with all model-fit statistics.
- A unit test in `analysis/tests/` that runs on a small synthetic example and checks the function returns the right shape.

**Done when:** all 9 helpers exist, are tested, and at least 5 are documented in `METHODS.md` with parameter-choice justifications.

### Phase 6 — Deep statistical analysis: full method stack (≈8 h)

Run every pre-registered hypothesis through the right method. Re-test every headline finding from the 4-hour pass under stronger methods. **Findings F-1 through F-20 are defined in `archive/4hr_pass/analysis/findings.md`** — read them before re-testing.

#### Re-test the headline findings under field-standard methods
- **F-1 Aspiration Inversion:** keep the McNemar baseline; add a **paired multilevel logistic** with `ref` as random intercept, controlling for `org_size`, `tech_person`, `cluster3`. Add **paired effect-size CIs via cluster bootstrap** (resampling whole `ref` strata).
- **F-9 Comfort × Infrastructure 2×2:** replace the median-split with **continuous interaction terms** in a Poisson GLM; produce a 2-D **marginal-effects heatmap** rather than a 4-cell grid.
- **F-10 Late-Adopter Paradox:** replace the K-means clustering basis with **LCA**. Re-run the cluster-membership logistic; report posterior class probabilities, not hard assignments.
- **F-11 Mediation:** keep the bootstrap; add **sensitivity analysis** for unmeasured confounders (Imai et al. 2010 / `dowhy` `refute_estimate`).
- **F-8 Divide Reversal:** the most contrarian finding — re-test under **Oaxaca–Blinder** (decompose the GN/GS gap), under **propensity-score matching** (compare like-to-like), and under **IPW** weighted to a NCCS-Candid sector benchmark. The headline only stands if at least 2 of 3 robustness checks agree with the original Poisson interaction.
- **F-18 Re-derived Typology:** replace K-means with LCA, report BIC/entropy/class-size diagnostics; add **profile plots** with item-response probabilities per class.

#### Run the new hypotheses
The Phase-3 lit dive will produce hypotheses we didn't test in the 4-hour pass. Common types to expect:
- IRT-based AI-readiness latent trait → predicts both `[U]` count and `[W]` count.
- SEM model of the TOE pathway: organizational + technology + environmental factors → adoption.
- Risk perception sub-structure (Slovic-style 2-factor: dread vs unknown) — does it appear in `ai_risk` items via factor analysis?
- Multilingual topic modeling on `ai_opentext` — do topic distributions differ by cluster, by region, by `[U]` count?
- MRP-style estimates of population-level statistics if a clean external benchmark is found.

#### Discipline rules (carryover + reinforced)
- Every result is logged in `analysis/findings.md` with the method's full output, not just a p-value.
- Every regression is reported with **and** without `ref` as a random intercept.
- BH-FDR within each sweep; at the report level, only highlight findings that survive FDR.
- For every prior the literature says exists, run the test even if the result is null. **Null findings count as findings.**
- Pre-registered hypotheses get reported even if they fail. Add a `pre_registered: yes/no` field to each `findings.md` entry.

#### Done criteria
- All 5 headline findings re-tested under stronger methods.
- All ≥25 pre-registered hypotheses tested.
- ≥40 total findings logged (positive, null, mixed).
- The methods appendix (`METHODS.md`) has a section per major model.

### Phase 7 — Triangulation & robustness battery (≈2 h)

A research-grade headline survives many tests. Run this for each of the 3–5 supporting findings:

- Same finding under at least **3 methods**: e.g., a t-test, a regression, and a non-parametric test.
- **Sensitivity analysis** to sample weights (unweighted, inverse-freq, IPW vs benchmark, raked).
- **Sensitivity analysis** to model specification: drop one predictor, swap a control, change the threshold.
- **Subgroup robustness:** sweep `subgroup_sweep` across `ref`, `global_north_south`, `cluster3`, `org_size_int`, `role` and report the cells where the headline does *not* hold.

Produce a single **robustness matrix** in `analysis/robustness.md`: rows = findings, columns = robustness checks, cells = ✓/✗/partial. The story is only the headline if it has all ✓ in the row.

**Done when:** every claim that makes it into `REPORT.md` or `PAPER.md` has a row in the robustness matrix and at least 4 of 5 checks pass.

### Phase 8 — Narrative synthesis + visualization (≈3 h)

The story shape may stay close to the 4-hour pass; the *evidence* is now stronger. Update accordingly.

#### Synthesis
- Re-examine the headline given the new analyses. If LCA disagrees with K-means on the typology, the headline tightens or shifts.
- Pick **3–4 supporting findings**, each tied to one chart.
- **Stop and check in with the user** if the headline shifts materially from the 4-hour pass.

#### Visualization (8–12 charts)
The 6 charts from the 4-hour pass are a starting point. Add:

- **Marginal-effects 2-D heatmap** for F-9 replacing the median-split 2×2.
- **LCA item-response-probability plot** replacing the K-means typology profile (F-18 redrawn).
- **Oaxaca–Blinder decomposition bar** for F-8 (endowments vs coefficients in the GN/GS gap).
- **SEM path diagram** for the TOE causal model.
- **BERTopic intertopic-distance map + topic-by-cluster heatmap** for the multilingual free-text pass.
- **Robustness matrix figure** — explicitly visualize what survives.
- **Forest plot** of effect sizes across all headline findings, with CIs, ordered by magnitude. *This becomes a strong appendix figure for the academic version.*

Visual system:
- Consistent palette (existing system from 4-hour pass).
- Consistent typography.
- Annotate directly on charts.
- Each chart export at print-ready 300+ DPI plus SVG.

**Done when:** all 8–12 charts exist, the headline figure has been iterated ≥3 times, and a fresh reader can reconstruct the narrative from the charts alone.

### Phase 9 — Writing & methodological appendix (≈1 h)

Two writeups, sharing material:

- **`REPORT.md`** — datathon-judge-facing slide-ready narrative. A draft exists at `archive/4hr_pass/REPORT.md`; copy it to the working tree as a starting point, then revise for new findings and swap in updated charts.
- **`PAPER.md`** — research-grade. Sections: Abstract / Introduction / Related Work / Data / Methods / Results / Discussion / Limitations / References. Aim for the level of an *NVSQ* or *VOLUNTAS* short paper. Cite ≥40 of the 200 sources.
- **`METHODS.md`** — every model documented with: full specification, parameter choices, software/version, references. Long enough for replication.

**Done criteria for the project:**
- Datathon judges can read `REPORT.md` and walk away with the headline.
- A peer reviewer could read `PAPER.md` + `METHODS.md` and find no methodological gap that would block submission.
- The robustness matrix in `analysis/robustness.md` shows every headline claim surviving ≥4 of 5 checks.

## Working norms for agents

- **Sub-agents.** Phase 3's 8 research streams run in parallel. Phase 5's 9 helpers can be split across 2–3 sub-agents (one per group: typology methods / decomposition methods / NLP). Phase 6's hypothesis tests can fan out by hypothesis cluster *after* infrastructure is built. Don't fan out the headline narrative or final writing — those need a single voice.
- **Pre-registration discipline.** Hypotheses are pre-registered in Phase 4 *before* any new analysis runs. This is non-negotiable for a research-grade pass.
- **Choice of dataset format.** Normalized parquet for clustering, IRT, LCA, distance-based work. Raw parquet for descriptive stats, free-text, and human-readable categorical breakdowns. See CLAUDE.md for dataset gotchas.
- **Logging.** Every test result, positive, null, or messy, lands in `findings.md` with a unique ID, method, and `pre_registered: yes/no`. Don't lose findings — null results harden the headline by ruling out alternatives.
- **Triangulation before headlining.** No single test carries a headline. Each headline finding must have ≥3 methods agreeing (the robustness matrix enforces this).
- **Update CLAUDE.md** for any new durable dataset facts. Don't update it for transient findings.
- **Checkpoint with the user** at the end of Phase 4 (pre-registered hypotheses) and the end of Phase 8 (final headline shape, before writing). Skip the Phase-7-end checkpoint only if the robustness battery confirms the existing story.
- **Don't redo done work.** The 4-hour pass produced 20 findings, 6 figures, and a draft `REPORT.md`, all preserved at `archive/4hr_pass/`. Build on it; don't rerun what already passed methodological muster. **Do not modify the archive itself** — the working tree (top-level `analysis/`, `figures/`, `REPORT.md`, etc.) is for the new pass.
