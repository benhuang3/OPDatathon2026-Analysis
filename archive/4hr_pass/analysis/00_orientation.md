# Phase 1 — Orientation

## Dataset shapes

- Raw: `ai_survey_results_2024_n=930.parquet` — **930 × 47**
- Normalized: `ai_survey_normalized_clustering_data.parquet` — **930 × 37**
- Row order matches between files; `cluster3` agrees row-by-row across them.

## Cluster columns — corrected understanding

The data dictionary swaps the labels in its prose, but the actual columns behave logically:

| Column | Where | Distribution | Method | Suggested name |
|--------|-------|--------------|--------|----------------|
| `cluster3` | both files | `{1: 523, 0: 265, -1: 142}` | HDBSCAN/UMAP, 3 groups | **AI Consumers / Late Adopters / AI Skeptics** |
| `cluster2` | normalized only | `{1: 524, 0: 406}` | K-means, 2 groups | broad consumer / non-consumer split |

`cluster3` is the more informative label and is what the "1=Consumer / 0=Late Adopter / -1=Skeptic" naming attaches to.

## Sample composition

| `ref` | n | % |
|-------|---|---|
| gt (GivingTuesday main list) | 549 | 59.0% |
| india (multiple India sublists) | 251 | 27.0% |
| tech (Fundraising.AI etc.) | 86 | 9.2% |
| hubs (regional GT hubs) | 44 | 4.7% |

| Continent | n |
|-----------|---|
| North America | 534 |
| Asia | 260 |
| Africa | 60 |
| Europe | 33 |
| South America | 22 |
| Australia | 6 |
| missing | 15 |

| Global N/S | n |
|------------|---|
| N | 573 |
| S | 342 |
| missing | 15 |

| Role | n |
|------|---|
| Leader | 418 (45%) |
| Fundraiser | 144 |
| Governance | 91 |
| Admin | 73 |
| Comms | 65 |
| Programs | 39 |
| Tech | 29 |
| Individual | 26 |
| Other | 23 |
| MERL | 15 |

| Org size | n |
|----------|---|
| 0–5 | 368 (40%) |
| 6–15 | 218 |
| 16–30 | 121 |
| 31–60 | 61 |
| 61–120 | 64 |
| 121+ | 93 |

96% of respondents are nonprofits (vs consultants / startups / other). 88% of orgs collect data.

## Missingness table (sorted descending, % of 930)

Conditional / opt-in columns (expected high missingness — gated by `ref`):

| Column | % missing | Why |
|--------|-----------|-----|
| `non_org_type` | 96.0% | only set for non-nonprofits (n=37) |
| `af_region`, `hubs_rural_urban` | 95.4% | only `ref=hubs` (n=44) |
| `non_data_work` | 82.3% | only if `collects_data == 0` |
| `india_state`, `india_rural_urban`, `in_india` | 75–76% | only India-source surveys |
| `ai_opentext` | 34.8% | optional free-text |
| `regionality` | 15.7% | not asked of all respondents |
| `data_kinds` | 14.1% | only if `collects_data` |

True item missingness (low across the board):

| Column | % missing |
|--------|-----------|
| `ai_risk` | 8.1% |
| `org_opentext` | 6.9% |
| `person_ai_comfort` | 5.6% |
| `collab_feasibility` | 3.9% |
| `ai_want` | 3.7% |
| `ai_risk_reward` | 3.3% |
| `org_agreements`, `data_use_policy`, `tech_person`, `cloud_storage`, `merl_person`, `ai_use` | 2.4–3.7% |
| `multi_country`, `continent`, `global_north_south`, `collects_data`, `role`, `org_size` | 0.5–2.2% |

`source`, `ref`, `org_label`, `org_years*`, `person_org_years*`, `cluster3` — zero missing.

## Numeric columns at a glance (raw)

| Column | mean | median | range |
|--------|------|--------|-------|
| `person_ai_comfort_raw` (0–10) | 6.53 | 7 | 0–10 |
| `collab_feasibility_raw` (0–10) | 6.08 | 6 | 0–10 |
| `org_years_raw` | 39.1 | 23 | 0–150 |
| `person_org_years_raw` | 10.5 | 7 | 0–60 |
| `ai_risk_reward` | 1.72 | 2 | **−1 to 5** |
| `regionality` | 1.62 | 1 | 1–3 |

**`ai_risk_reward` has a special code:** `-1` means *"I don't understand AI enough to have a clear view"* — **314 of 930 (33.8%) gave this answer.** Treating it as a low end of the scale would be wrong; it should be modeled as a separate category or excluded.

## Binary share-of-1 (raw)

- `nonprofit` 0.96 · `collects_data` 0.88 · `data_use_policy` 0.72 · `cloud_storage` 0.68
- `merl_person` 0.43 · `tech_person` 0.29 · `org_agreements` 0.29
- `multi_country` 0.16

## Quick look at the AI use / want / risk multi-selects

Stored as **bytes-encoded JSON arrays** (e.g., `b'["Generating content (text or images)",""]'`). Trailing empty string is normal. Some unicode (non-breaking space `\xc2\xa0`). The normalized parquet already one-hot-expands these into `[U] X`, `[W] X`, `[D] X` columns — prefer those for analysis.

`org_label` is also bytes-encoded JSON list with up to ~3 labels per row — needs parsing if used.

### Use-vs-Want gap (already a strong signal)

| Task | Use today | Want | Gap |
|------|-----------|------|-----|
| Organize information | 19.1% | 60.3% | **+41.2 pp** |
| Predict outcomes | 11.2% | 51.7% | **+40.5 pp** |
| Assist (automate repetitive tasks) | 16.1% | 55.7% | **+39.6 pp** |
| Interpret information | 15.3% | 49.9% | **+34.6 pp** |
| Translate / transcribe | 24.4% | 39.0% | +14.6 pp |
| Ask (chatbot) | 32.7% | 39.5% | +6.8 pp |
| Generate (text/images) | 53.9% | 54.9% | +1.1 pp |

**Today's "AI use" in nonprofits is overwhelmingly *content generation*. The *aspiration* is for the analytical / automation work that requires real data infrastructure.** This is the headline-shape finding of Phase 1.

### Risk endorsement (% selecting each)

| Risk | % |
|------|---|
| AI-related data breaches | 61.2% |
| Decisions based on biased AI models | 59.2% |
| Plagiarism / IP loss | 58.9% |
| Increasing inequity | 50.2% |
| Over-dependency on commercial AI | 49.6% |
| Replacing workers | 35.3% |
| Environmental impact | 33.2% |

## Cluster profiles (the headline-relevant view)

| | Skeptics (-1) | Late Adopters (0) | Consumers (1) |
|---|---|---|---|
| n | 142 | 265 | 523 |
| `[U]` count (avg AI tasks done now) | 1.31 | **0.15** | 2.79 |
| `[W]` count (avg AI tasks wanted) | 2.05 | 2.56 | 4.60 |
| `person_ai_comfort` | 0.58 | 0.48 | 0.76 |
| `ai_risk_reward` | 1.33 | 0.66 | 2.34 |
| `tech_person` | 0.22 | 0.21 | **0.35** |
| `cloud_storage` | 0.46 | 0.63 | 0.75 |
| `data_use_policy` | 0.66 | 0.66 | 0.76 |
| `org_agreements` | 0.26 | 0.17 | 0.36 |
| `multi_country` | 0.14 | 0.07 | 0.22 |

**Surprising:** the cluster labeled "AI Skeptics" actually does *more* AI today (1.31 tasks) than the "Late Adopters" (0.15). The Late Adopters look more like *willing-but-unequipped* — they want AI (w_count=2.56) but use almost none. The Skeptics use modest AI but are pessimistic about benefits.

`ai_risk_reward = -1` ("I don't understand AI") is endorsed by **53% of Late Adopters** vs 24% of Consumers — comprehension itself is a stronger non-adoption signal than risk perception.

## Geography × cluster (n=915 with known GN/GS)

| | Skeptics | Late | Consumers |
|---|---|---|---|
| Global North (n=573) | 14.7% | 30.0% | 55.3% |
| Global South (n=342) | 14.3% | 26.6% | 59.1% |

**No GN/GS gap in cluster membership.** Worth flagging early — this complicates the standard digital-divide narrative.

## Implications for analysis

1. **Use the normalized parquet's `[U]/[W]/[D]` one-hots** — don't reparse the bytes JSON unless you need raw text.
2. **Treat `ai_risk_reward = -1` as a distinct category** ("doesn't understand"), not a numeric extreme. About 1 in 3 respondents are in it.
3. **Stratify or weight by `ref`** for any whole-sample claim — `gt` is 59% of the sample.
4. **The Use-vs-Want gap is the most promising thread.** Concretely: the gap is large *only* for the analytical/automation tasks, which are exactly the ones requiring data infrastructure that most nonprofits lack.
5. **The Late-Adopter paradox** (lots of want, ~zero use) is a candidate sub-narrative worth verifying with regression in Phase 3.
6. **GN/GS digital-divide narrative may not hold here** — flag for Phase 2 to find the prior literature, then Phase 3 to test rigorously.
