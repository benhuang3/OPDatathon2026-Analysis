# SLIDES.md — Presentation outline

10 slides. Minimal text per slide. Figures referenced by number from `figures/`.

---

## Slide 1 — Title

- **Nonprofits use AI for writing. They want it for analytics.**
- *The bottleneck isn't infrastructure. It's understanding.*
- OP-Datathon 2026 · GivingTuesday AI Readiness Survey · n=930

---

## Slide 2 — The data

- 930 nonprofit professionals, 2024
- 4 source strata: GivingTuesday list (549), India (251), tech (86), hubs (44)
- Use today, want, infrastructure, attitudes, free-text

---

## Slide 3 — Headline: the aspiration inversion

- **Fig 1**
- Content tasks: parity (use ≈ want)
- Analytical tasks: 35–41pp gap
- *Predict*: 52% want, 11% use

---

## Slide 4 — It survives every check

- **Fig 7** (IPW invariance)
- Cluster bootstrap by source list: CI excludes zero
- Reweighting to a target source mix: gaps move <0.5pp
- McNemar p < 1e-66 on each analytical task

---

## Slide 5 — The bottleneck is comprehension, not plumbing

- **Fig 10** (cluster profile)
- "Late Adopters" have *more* cloud + data policy than "Skeptics"
- 53% of Late Adopters say *I don't understand AI enough*
- vs 24% of Consumers

---

## Slide 6 — Comfort dominates structural variables

- **Fig 6** (forest plot)
- β_comfort >> β_readiness >> β_tech_specialist ≈ β_org_size
- Once comfort + readiness are in, size and tech specialist are null

---

## Slide 7 — Comfort × readiness: both pull, mild ceiling

- **Fig 2** (heatmap)
- β_comfort = +0.55, β_readiness = +0.31 (Poisson, standardised)
- Small negative interaction (p = 0.025): diminishing returns at the top

---

## Slide 8 — The contrarian finding: GN/GS reverses

- **Fig 4** (Oaxaca decomposition)
- Subset: small (≤15 staff), no tech specialist
- GS uses **+0.42** more AI tasks than GN
- Confirmed by OLS, PSM (132 pairs), IPW

---

## Slide 9 — Latent typology: a willing-but-not-using middle

- **Fig 3** (LCA item-response profile)
- k=3 LCA on `[U]` + `[W]` items
- Middle class: low P(use), high P(want) on analytical items
- Cluster3 (HDBSCAN) misses this; LCA recovers it

---

## Slide 10 — Robustness + effect sizes at a glance

- **Fig 8** (robustness matrix) · **Fig 9** (forest plot)
- 12 headlines × 6 checks: ≥5/6 pass on every row
- 11 effect sizes on one chart

---

## Slide 11 — Why this matters

- Capacity-building spend is aimed at the wrong bottleneck
- Analytical tasks are the high-leverage ones for social impact
- GN/GS reversal overturns the default funding logic
- Order: comprehension → comfort → infrastructure use

---

## Slide 12 — What to do

- **Lead with comprehension training** — cohort-based, locally tailored
- Build *vigilance* alongside comfort (they run opposite directions)
- Localize analytical AI for GS — that's where the next divide opens
- Full detail: `REPORT.md` · `PAPER.md` · `METHODS.md`
