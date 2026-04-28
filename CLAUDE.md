# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Project and Goal
This repository is for a datathon to analyze the provided Giving Tuesday dataset and develop a data-driven narrative that uncovers novel insights and patterns. Reference PROJECT.md for more instructions.

## Project state — read this before starting

The working tree is set up for the **30-hour research-grade pass** specified in `PROJECT.md`. A prior **4-hour datathon pass** was completed and its full output is preserved at `archive/4hr_pass/`:

- `archive/4hr_pass/REPORT.md` — datathon-style narrative (headline + 3 pillars).
- `archive/4hr_pass/RESEARCH.md` — 30-source bibliography across 4 streams + 12 testable hypotheses.
- `archive/4hr_pass/analysis/findings.md` — 20 logged findings (referred to as **F-1, F-2, … F-20** throughout `PROJECT.md`).
- `archive/4hr_pass/analysis/lib.py` — reusable statistical helpers (`compare_groups`, `gap_analysis`, `subgroup_sweep`, `bootstrap_ci`, `fdr_adjust`, `data_readiness_score`).
- `archive/4hr_pass/analysis/00_orientation.md` — dataset baseline + missingness audit.
- `archive/4hr_pass/figures/` — 6 publication-style charts (PNG + SVG).

**`PROJECT.md` Phases 5–6 explicitly extend and re-test the archived findings under field-standard methods (LCA, IRT, SEM, Oaxaca–Blinder, IPW, multilevel models, BERTopic).** Read the archive before starting Phase 1 — particularly `archive/4hr_pass/analysis/findings.md` and `archive/4hr_pass/analysis/lib.py` — so you know what's already established and what's being re-tested.

Do not modify the archive. Build the new pass under `analysis/`, `figures/`, and the new top-level deliverables (`REPORT.md`, `PAPER.md`, `RESEARCH.md`, `METHODS.md`, `bibliography.bib`).

Python dependencies for the new method stack are pinned in `requirements.txt` — install before Phase 5.




## Repository nature

This repo is a **dataset, not a codebase** — there is no source code, build system, or test suite. It contains the raw and normalized exports from the GivingTuesday 2024 AI Readiness survey (n=930 respondents), distributed for the OPDatathon 2026.

Treat any analysis Claude is asked to do (notebooks, scripts) as new work to be created in this directory; don't expect existing tooling.

## Data layout

`ai_readiness_survey_results/ai_exports/` contains two parallel datasets, each provided in CSV / Parquet / Pickle:

- **`ai_survey_results_2024_n=930.*`** — raw survey responses. Mixed types: ints, floats, free-text (`org_opentext`, `ai_opentext`, `non_data_work`), categorical strings, and multi-select fields stored as delimited strings (`data_kinds`, `ai_use`, `ai_want`, `ai_risk`).
- **`ai_survey_normalized_clustering_data.*`** — same respondents, all features rescaled to 0–1 and one-hot expanded for clustering. This is the file to use for distance-based / ML work.

`README_datadictionary.md` in the same folder is authoritative for column meanings and encodings — **read it before interpreting any column**, especially:

- `cluster3` is the HDBSCAN/UMAP 3-group result (`1`=AI Consumers (523), `0`=Late AI Adopters (265), `-1`=AI Skeptics (142)), present in both files. `cluster2` is the K-means 2-group result (`{1: 524, 0: 406}`), present only in the normalized file. The data dictionary's prose swaps these labels; the actual columns are sensibly named (`cluster3` has 3 groups, `cluster2` has 2 groups). Verified row-by-row.
- The "AI Skeptics" cluster is misleadingly named: cluster `-1` actually uses *more* AI tasks today (~1.3) than the "Late Adopters" cluster `0` (~0.15). The skeptics are modest users with negative risk/reward attitudes; the late adopters are willing-but-unequipped.
- Prefix conventions in the normalized dataset: `[D]` = data-collection practice, `[U]` = currently uses AI for…, `[W]` = wants to use AI for….
- Many fields have both a normalized form (`person_ai_comfort`, `org_years`, `collab_feasibility`) and a `_raw` form — pick based on whether the analysis needs absolute or relative values.
- **`ai_risk_reward` has a special code: `-1` means "I don't understand AI enough to have a clear view"** — given by 314 / 930 (33.8%) of respondents. It's not a low end of a 1–5 scale; it's a separate category. Always either filter or treat as its own bucket.
- `org_label`, `ai_use`, `ai_want`, `ai_risk`, `data_kinds` are stored as **bytes-encoded JSON arrays** (e.g., `b'["X","Y",""]'`) with a trailing empty string. The normalized parquet already one-hot-expands the AI use/want/data kinds into `[U] X` / `[W] X` / `[D] X` columns — prefer those.
- `ref` collapses the longer `source` into 4 buckets: `gt` (549), `india` (251), `tech` (86), `hubs` (44). Sample is heavily weighted toward GivingTuesday's main US/global list and toward India.

## Working with the data

- Prefer the parquet files for loading (`pd.read_parquet`); the pickles are pandas-version-sensitive and the CSVs lose dtypes on multi-select columns.
- The Africa/India sub-region columns (`af_region`, `india_state`, `india_rural_urban`, `hubs_rural_urban`) are only populated for the relevant survey sources — expect `NaN` elsewhere and filter by `ref` before using them.
- Free-text columns are in mixed languages (English, plus some Hindi/regional-language responses from the India sources).
