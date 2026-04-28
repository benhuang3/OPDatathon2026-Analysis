# Codebook — GivingTuesday 2024 AI Readiness survey (n = 930)

This codebook supersedes the data dictionary at `ai_readiness_survey_results/ai_exports/README_datadictionary.md`. Differences from that document — and from `archive/4hr_pass/analysis/00_orientation.md` — are flagged inline. Built from a fresh audit of both parquet files (`analysis/_scratch/audit.py`).

## File layout

| File | Shape | Use for |
|---|---|---|
| `ai_survey_results_2024_n=930.parquet` (**RAW**) | 930 × 47 | descriptive stats, free-text, raw-scale numerics, anything where missingness must be preserved |
| `ai_survey_normalized_clustering_data.parquet` (**NORM**) | 930 × 37 | clustering, distance-based methods, multi-select co-occurrence, anything that needs a complete numeric matrix |

**Row order matches between the two files.** `cluster3` agrees row-for-row 100% across them; merge by row index, not by any key column.

---

## Universal warnings (read before any analysis)

### W-1 — NORM mean-imputes every NaN
Every binary feature in NORM has **three** unique values: `0`, `1`, and the column mean. Same pattern for `org_small_med_large`, `regionality`, `global_north_south_int`. NORM has zero NaNs *by construction* — missingness has been silently filled with the marginal mean.

Implications:
- Any LCA / IRT / SEM / regression that assumes binary inputs **must** convert NORM's mean-imputed values back to NaN, or use RAW.
- Identifying respondents with original missingness on `tech_person`, `cloud_storage`, etc. requires RAW (NORM lost that signal).
- Cell counts on NORM columns include imputed rows — never report a frequency from NORM as a clean denominator.

### W-2 — Two raw-normalized fields are absent from NORM
`person_ai_comfort` and `collab_feasibility` are **only in RAW**. Spot-checked 5 random rows: NORM[`person_ai_comfort`] returns `None`. To use these on the clustering dataset, join from RAW (`load_joined()` in `lib.py`, or `pd.concat([raw, norm], axis=1)`).

### W-3 — `ai_risk_reward = -1` is a separate category, not a low extreme
314 / 930 (33.8%) of respondents answered *"I don't understand AI enough to have a clear view"*, encoded as `-1`. The other valid values are 1–5. **Filter or treat as its own bucket** in every quantitative use; never average it into a 1–5 mean.

### W-4 — Cluster columns: ignore the data dictionary's prose
The data dictionary's text inverts which column is which. Reality (verified row-by-row):

| Column | Where | Distribution | Method |
|---|---|---|---|
| `cluster3` | RAW + NORM, identical | `{1: 523, 0: 265, -1: 142}` | HDBSCAN / UMAP, 3 groups |
| `cluster2` | NORM only | `{1: 524, 0: 406}` | K-means, 2 groups |

`cluster3 = 1` ≈ AI Consumers, `0` ≈ Late Adopters, `-1` ≈ AI Skeptics — but the "Skeptics" label is misleading: cluster `-1` uses *more* AI today (use_count ≈ 1.31) than cluster `0` (use_count ≈ 0.15). See `archive/4hr_pass/analysis/findings.md` F-15 for the disengagement reframe.

`cluster2` adds almost no information beyond `cluster3`: crosstab shows `cluster2 = 0` contains all 142 Skeptics + 264 of 265 Late Adopters; `cluster2 = 1` contains all 523 Consumers + 1 stray Late Adopter. So `cluster2 ≈ I(cluster3 == 1)`, modulo one row. Treat as redundant.

### W-5 — `regionality` differs between RAW and NORM
RAW `regionality` ∈ {1, 2, 3} with 146 NaNs. NORM `regionality` ∈ {0.25, 0.5, 0.75, 1.0} plus a mean-imputed level (`≈0.498`) for the 22 NaN rows that survived. **The NORM column is 4-level, not 3-level**: the 4th level is constructed from `multi_country = 1` rows (i.e., NORM stretched the scale to {local, regional, national, multi-country}). Spearman across the two = 0.96, *not* 1 — they encode different variables. The data dictionary's NORM coding "1=local; 2=regional; 3=national; 4=multi-country" is correct after rescaling to {0.25, 0.5, 0.75, 1.0}.

### W-6 — `org_small_med_large` boundaries are mis-documented
Data dictionary: `{0: '0-15 staff', 0.5: '16-30 staff', 1: '30+ staff'}`. Reality (verified by crosstab):

| `org_small_med_large` | covers raw `org_size_int` | covers raw `org_size` |
|---|---|---|
| 0.0   | 0, 1   | 0–5, 6–15 |
| 0.5   | 2, 3   | 16–30, 31–60 |
| 1.0   | 4, 5   | 61–120, 121+ |
| ≈0.25 | NaN    | (mean-imputed for 5 missing rows) |

Use cut `{0: '0–15', 0.5: '16–60', 1: '61+'}`. The data dictionary undercounts the medium bucket.

### W-7 — `af_region` is NOT hubs-gated
Per the 4hr_pass orientation, `af_region` was described as `ref = hubs` only. Audit shows: 27 of 886 non-hubs respondents also have `af_region` populated. It is populated for any African respondent (continent = Africa), gated by continent, not `ref`. `hubs_rural_urban` is the hubs-only column.

### W-8 — `non_data_work` is dirty
76 of 822 respondents who *do* collect data (`collects_data = 1`) also filled in `non_data_work`. The column should not be treated as cleanly partitioned.

### W-9 — `ai_want_2+` includes "Other", excludes "We don't know yet!"
Exact reverse-engineering: `ai_want_2+ == 1` iff the count over the eight `[W]` columns *except* `[W] We don't know yet!` is ≥ 2. Includes `[W] Other`. Agreement with this definition is **100% (930/930)**; excluding `[W] Other` drops it to 99.6%.

### W-10 — Multi-select fields are bytes-encoded JSON with a trailing empty string
`ai_use`, `ai_want`, `ai_risk`, `data_kinds`, `org_label` are stored as `bytes` like `b'["X","Y",""]'`. Some option strings contain non-breaking space (`\xc2\xa0`). Use `lib.parse_jsonbytes` to parse; for analysis, prefer the pre-expanded `[U]` / `[W]` / `[D]` one-hot columns in NORM.

### W-11 — Survey window: 2024-03-07 to 2024-05-28
`Start time` runs across ~12 weeks. Not documented in the README. Useful for any temporal robustness check; otherwise ignorable.

### W-12 — Sample weighting
4 reference buckets in highly unequal proportions: `gt = 549`, `india = 251`, `tech = 86`, `hubs = 44`. 11 underlying `source` mailing lists collapse into these. **Weight or stratify by `ref` for any whole-sample claim**; put `ref` as a random intercept on every headline regression (per PROJECT.md).

---

## RAW codebook (47 columns)

Conventions:
- **dtype** as stored in parquet
- **n missing** out of 930
- **valid values**: empirical set or range
- **rec.**: recommended treatment for analysis (`numeric` / `binary` / `ordinal` / `nominal` / `multiselect` / `text` / `meta` / `ignore`)

### Identifiers and metadata

| Column | dtype | n miss | valid values | rec. | notes |
|---|---|---|---|---|---|
| `source` | object | 0 | 11 mailing lists | nominal | Use `ref` for analysis; keep `source` for sample-bias diagnostics. |
| `Start time` | datetime64 | 0 | 2024-03-07 to 2024-05-28 | meta | Useful for temporal robustness check only. |
| `ref` | object | 0 | `gt` (549), `india` (251), `tech` (86), `hubs` (44) | nominal | Primary stratification variable. Always include as random intercept. |
| `cluster3` | int64 | 0 | -1 (142), 0 (265), 1 (523) | nominal | HDBSCAN/UMAP. Misleading "Skeptics" label — see W-4. |

### Respondent (person)

| Column | dtype | n miss | valid values | rec. | notes |
|---|---|---|---|---|---|
| `role` | object | 7 | 10 levels (Leader 418, Fundraiser 144, …) | nominal | Leader is 45% — strong concentration. |
| `role_int` | float64 | 7 | 0–9 | nominal | Same as `role`; ordering is arbitrary, do not treat as ordinal. |
| `person_org_years` | float64 | 0 | 0.0–1.0 (=raw/60) | numeric | Years at current org, normalized. Skewed; median ≈ 0.117 (7 yrs). |
| `person_org_years_raw` | float64 | 0 | 0–60 | numeric | Raw years. |
| `person_ai_comfort` | float64 | 52 | 0.0–1.0 in 0.1 steps | numeric | =`person_ai_comfort_raw / 10`. **Not in NORM** (W-2). |
| `person_ai_comfort_raw` | float64 | 52 | 0–10 integer | ordinal | Self-rated AI comfort. ρ ≈ 0.50 with `use_count` (F-20). |

### Organization

| Column | dtype | n miss | valid values | rec. | notes |
|---|---|---|---|---|---|
| `nonprofit` | float64 | 1 | 0/1, mean 0.96 | binary | 96% nonprofit. The non-nonprofit n=37 is small; mostly worth filtering out for "nonprofit-only" claims. |
| `non_org_type` | float64 | 893 | 1=Consultant, 2=Startup, 3=Other | nominal | Only set when `nonprofit = 0`. |
| `org_size` | object | 5 | `0-5`, `6-15`, `16-30`, `31-60`, `61-120`, `121+` | ordinal | 40% of orgs are 0–5 staff. |
| `org_size_int` | float64 | 5 | 0–5 | ordinal | Mirrors `org_size`; canonical column for regressions. |
| `org_years` | float64 | 0 | 0.0–1.0 (=raw/150) | numeric | Org age, normalized; spearman vs raw = 1.0. |
| `org_years_raw` | float64 | 0 | 0–150 | numeric | Org age in years. |
| `multi_country` | float64 | 20 | 0/1, mean 0.16 | binary | "Operates in multiple countries". Folded into NORM `regionality`'s top tier (W-5). |
| `regionality` | float64 | 146 | 1, 2, 3 | ordinal | local / regional / national. **3-level in RAW; 4-level in NORM** (W-5). |
| `org_opentext` | object | 64 | free text, 823 distinct strings | text | English + some Hindi/regional-language. Topic-modeling target. |
| `org_label` | object | 0 | bytes-JSON list of cause areas | multiselect | Up to ~3 labels per row; ChatGPT-classified from `org_opentext`. |

### Geography

| Column | dtype | n miss | valid values | rec. | notes |
|---|---|---|---|---|---|
| `continent` | object | 15 | NA (534), Asia (260), Africa (60), Europe (33), SA (22), Aust (6) | nominal | NA dominant. |
| `continent_int` | float64 | 15 | 0=NA, 1=Asia, 2=Africa, 3=Europe, 4=SA, 5=Aust | nominal | Same as `continent`. |
| `global_north_south` | object | 15 | N (573), S (342) | binary | Coded GN = NA, Europe, Australia; GS = Africa, Asia, Latin America. |
| `global_north_south_int` | float64 | 15 | 0=N, 1=S | binary | NORM version mean-imputes the 15 missing as ≈0.374 (W-1). |
| `af_region` | object | 887 | N/W/E/Southern Africa | nominal | **Populated for all African respondents, NOT hubs-only** (W-7). |
| `af_region_int` | float64 | 887 | 0–3 | nominal | Same. |
| `hubs_rural_urban` | object | 887 | urban / rural | binary | hubs survey only. |
| `hubs_rural_urban_int` | float64 | 887 | 0=urban, 1=rural | binary | Same. |
| `in_india` | float64 | 694 | 0/1 | binary | India sub-surveys only. |
| `india_state` | object | 704 | 27 states/UTs | nominal | India only. Heavy concentration in a few states. |
| `india_rural_urban` | object | 702 | metro / rural / urban | nominal | India only; 3-level (not 2). |
| `india_rural_urban_int` | float64 | 702 | 0=metro, 1=rural, 2=urban | nominal | Same. |

### Data infrastructure (binary)

All scored as `0/1`, mean (= rate of "yes"), missingness ≈ 2–4%.

| Column | n miss | mean | rec. | notes |
|---|---|---|---|---|
| `collects_data` | 14 | 0.88 | binary | Gates `data_kinds` and (mostly) `non_data_work`. |
| `tech_person` | 27 | 0.29 | binary | Strongest non-size predictor of `cluster3 = Consumer` (F-7). |
| `merl_person` | 34 | 0.43 | binary | |
| `cloud_storage` | 27 | 0.68 | binary | |
| `data_use_policy` | 29 | 0.72 | binary | |
| `org_agreements` | 30 | 0.29 | binary | |
| `data_kinds` | 131 | — | multiselect | Bytes-JSON list; pre-expanded as `[D]` columns in NORM. |
| `non_data_work` | 765 | — | text | Dirty (W-8). |

### AI use, want, risk

| Column | dtype | n miss | rec. | notes |
|---|---|---|---|---|
| `ai_use` | object (bytes) | 22 | multiselect | 9 options. Use `[U]` one-hots in NORM. |
| `ai_want` | object (bytes) | 34 | multiselect | 9 options. Use `[W]` one-hots in NORM. |
| `ai_risk` | object (bytes) | 75 | multiselect | 7 risks. NORM does *not* one-hot expand this — must parse RAW with `lib.parse_jsonbytes`. |
| `ai_risk_reward` | float64 | 31 | nominal (special) | **−1 to 5; −1 is a category, not a low extreme** (W-3). 5-level Likert with 33.8% "don't understand" bucket. |
| `collab_feasibility` | float64 | 36 | numeric | 0.0–1.0; = `collab_feasibility_raw / 10`. **Not in NORM** (W-2). |
| `collab_feasibility_raw` | float64 | 36 | ordinal | 0–10. |
| `ai_opentext` | object | 324 | text | Free-text on hopes/fears about AI. 65% response rate. Multilingual. Primary BERTopic input. |

### Note on `ai_risk_reward` recoding

For methods that need a continuous version, use these two columns instead of treating −1 as 0:

| Recoded variable | Definition |
|---|---|
| `rr_dont_understand` | `(ai_risk_reward == -1)` indicator |
| `rr_attitude` | `ai_risk_reward` with `-1 → NaN`; remaining 1–5 ordinal |

Pre-defined as helpers in `lib.py` (Phase 5).

---

## NORM codebook (37 columns)

Many columns share names with RAW. Where a column is in *both* files, NORM's value is `0`/`1`/(column-mean) — i.e., NaN-imputed. **Use RAW for the same column when missingness matters.**

### Carry-overs from RAW (mean-imputed)

`nonprofit`, `org_years`, `regionality`, `global_north_south_int`, `collects_data`, `tech_person`, `merl_person`, `cloud_storage`, `data_use_policy`, `org_agreements`. All binary except `org_years` (numeric 0–1) and `regionality` (4-level — see W-5).

### NORM-only derived

| Column | Definition |
|---|---|
| `org_small_med_large` | Re-bucketed org size: `0=0–15`, `0.5=16–60`, `1=61+`. Mean-imputed for 5 missing → ≈0.251. **Boundaries differ from data-dict prose** (W-6). |
| `cluster2` | K-means 2-group; ≈ `I(cluster3 == 1)` modulo 1 row (W-4). |
| `cluster3` | Same as RAW `cluster3` (HDBSCAN/UMAP, 3 groups). |
| `ai_want_2+` | `1` iff sum of 8 `[W]` cols (all except `[W] We don't know yet!`) ≥ 2 (W-9). |

### `[D]` columns — data-collection practices (5 binaries)

Mean = "share of orgs reporting this practice".

| Column | mean |
|---|---|
| `[D] Our staff manually fill out spreadsheets …` | 0.63 |
| `[D] Our staff uses software to collect data about people …` | 0.44 |
| `[D] We also retained the original audio or video …` | 0.21 |
| `[D] We collect data using devices, such as phones, tablets …` | 0.56 |
| `[D] We have at least a hundred transcripts or records …` | 0.27 |

### `[U]` columns — currently uses AI for… (9 binaries)

| Column | mean |
|---|---|
| `[U] Generat` | 0.54 |
| `[U] I am not currently using AI` | 0.34 |
| `[U] Ask` | 0.33 |
| `[U] Translat` | 0.24 |
| `[U] Organi` | 0.19 |
| `[U] Assist` | 0.16 |
| `[U] Interpret` | 0.15 |
| `[U] Predict` | 0.11 |
| `[U] Other` | 0.09 |

### `[W]` columns — wants to use AI for… (9 binaries)

| Column | mean |
|---|---|
| `[W] Organi` | 0.60 |
| `[W] Assist` | 0.56 |
| `[W] Generat` | 0.55 |
| `[W] Predict` | 0.52 |
| `[W] Interpret` | 0.50 |
| `[W] Ask` | 0.39 |
| `[W] Translat` | 0.39 |
| `[W] We don't know yet!` | 0.32 |
| `[W] Other` | 0.12 |

`[U]` and `[W]` are paired by stem (`Ask`, `Assist`, `Generat`, `Interpret`, `Organi`, `Predict`, `Translat`, `Other`). The seven core stems are the McNemar pairs in F-1.

---

## Indices flagged for IRT / LCA replacement (input to Phase 5)

The 4-hour pass used additive 0–1 indices. Phase 5 will replace each with a model-based equivalent.

| 4-hour index | Definition (from `archive/4hr_pass/analysis/lib.py`) | Phase-5 replacement |
|---|---|---|
| `data_readiness_score` | Mean of 5 binary infra indicators + 5 `[D]` indicators (10 cols total), NaN→0 | **2-PL IRT** (`girth`) on the 10 binary items; person score replaces the additive mean. Verifies items load on a single latent trait; flags items with low discrimination. |
| `ai_use_count` | Sum of `[U]` cols excl. `[U] Other` and `[U] I am not currently using AI` (7 cols) | Keep as count outcome; **alternative**: graded-response IRT for a latent "AI breadth" if the 7 items are not equally discriminating. |
| `ai_want_count` | Sum of `[W]` cols excl. `[W] Other` and `[W] We don't know yet!` (7 cols) | Same as above. |
| K-means typology (F-18) | K-means on standardized `[U]`, `[W]`, readiness, comfort, k=3 | **LCA via `stepmix`** for k=2..6, model selection on BIC + entropy. Replaces hard cluster labels with posterior class probabilities. |

---

## Recommended treatment by analysis type

| Analysis | Use file | Notes |
|---|---|---|
| Descriptive statistics, missingness reporting | RAW | Preserve NaNs. |
| Group means / counts (`compare_groups`, `gap_analysis`) | RAW or NORM (`[U]/[W]/[D]` only) | NORM is fine for the one-hots; for binaries with original NaN, drop NORM's mean-imputed rows or use RAW. |
| McNemar paired tests on `[U]` vs `[W]` | NORM | One-hots are clean. |
| Logistic / Poisson regression with `cluster3` outcome | RAW (joined with NORM `[U]/[W]/[D]`) | `lib.load_joined` does this; preserve NaNs for predictors. |
| Multilevel (`ref` random intercept) | Same as above | Required on every headline (PROJECT.md §6 discipline). |
| Distance-based / clustering (LCA, MCA, UMAP) | NORM | Designed for this; tolerate the mean imputation since rows aren't dropped. |
| IRT (`girth`) | RAW (binary items only, NaN preserved) | NORM's mean-imputed values would break the binary assumption. |
| Free-text / topic modeling | RAW | `org_opentext` and `ai_opentext` are RAW-only. |
| External-benchmark IPW | RAW | Need original NaN to know who is in `gt` vs `india` vs `tech` vs `hubs`. |

---

## Open questions / not yet answered

- Which of the 11 `source` lists were sent which translations? (No language column; multilingual responses appear without metadata.)
- For `india_state`, is the encoding consistent (e.g., "Goa" vs "The Government of NCT of Delhi" suggests free-text rather than a standardized list)? — needs a manual pass for state-level analyses.
- `regionality` is 15.7% missing across the sample, not gated by `ref`. Missingness rates: `tech` 37.2%, `hubs` 27.3%, `gt` 16.0%, `india` 5.6%. Treat as item non-response, not a structural gate; the `tech` and `hubs` versions of the form likely de-emphasized this question.
