# SCRIPT.md — Presenter script

Speaker notes for the 12 slides in `SLIDES.md`. ~7 minute talk at a comfortable pace. Each section is what you actually say; bracketed lines are stage directions.

---

## Slide 1 — Title

> Hi. I'm going to give you one sentence and then spend seven minutes defending it.
>
> **Nonprofits already use AI — for writing. The next wave they want is analytical. And the thing standing between them and that wave is not money or infrastructure. It's understanding.**
>
> Everything from here is evidence for that claim.

---

## Slide 2 — The data

> The data is the GivingTuesday 2024 AI Readiness Survey. 930 nonprofit professionals. Four source lists: the main GivingTuesday list, an Indian sub-sample, a tech-leaning channel, and regional hubs.
>
> Each respondent told us what they currently do with AI, what they want to do with AI, what infrastructure they have, and how they feel about it. Plus a free-text box, in mixed languages.
>
> One thing to flag up front: the Indian sub-sample is large — 27% of the total. Every result I'm about to show survives reweighting away from that.

---

## Slide 3 — Headline: the aspiration inversion

> [Click to Fig 1]
>
> Here's the headline. On the left, paired bars: what people use AI for today, versus what they want to use it for. On the right, the gap, with confidence intervals.
>
> Look at the top three rows — generate, ask, translate. Use and want are basically tied. Nonprofits are already using AI for content.
>
> Now look at the bottom four — interpret, assist, predict, organize. These are the analytical tasks. The gaps are 35 to 41 percentage points. *Predict* is the most-wanted task at 52% and one of the least-used at 11%.
>
> This is the inversion. Today's AI use is content. Tomorrow's demand is analytics.

---

## Slide 4 — It survives every check

> [Click to Fig 7]
>
> Before we read anything into this, the obvious question: is this just an artefact of who's in the sample?
>
> No. We ran a cluster bootstrap that resamples whole source strata — confidence intervals exclude zero. We reweighted the sample to a target source mix that down-weights India and pulls up the under-represented strata — the per-task gaps move by less than half a percentage point. McNemar's test on the paired use-versus-want indicators: p less than ten-to-the-minus-sixty-six on every analytical task.
>
> The inversion is real.

---

## Slide 5 — The bottleneck is comprehension, not plumbing

> [Click to Fig 10]
>
> Now: who is stuck? Who wants AI but doesn't use it?
>
> The dataset has a three-way HDBSCAN cluster: Skeptics, Late Adopters, Consumers. The "Late Adopters" are the willing-but-not-using middle.
>
> Look at the middle bars: cloud storage and data policy. Late Adopters score *higher* on infrastructure than the Skeptic group. They are not blocked on plumbing.
>
> What they're missing: 53% of them say "I don't understand AI enough to have a clear view." Compared to 24% of the Consumer group. That's the bottleneck.

---

## Slide 6 — Comfort dominates structural variables

> [Click to Fig 6]
>
> Let's put it in a model. Predict AI use from four candidates: comfort, readiness, having a tech specialist, and org size.
>
> Comfort is the largest coefficient by a wide margin. Readiness is second. Org size and having a tech specialist are statistically null once those two are in.
>
> Translation: structural variables — how big you are, whether you have a tech person — don't matter for AI use once you control for whether the *people* in the org are comfortable with it.

---

## Slide 7 — Comfort × readiness: both pull, mild ceiling

> [Click to Fig 2]
>
> Same Poisson model, visualised over the comfort-by-readiness plane. Each axis pulls AI use up by roughly a factor of three across its range.
>
> The contours bend slightly at the top right — that's a small negative interaction, p around 0.025. It says there's mild diminishing returns when both are high. You don't get to score *very* far above your weaker leg.
>
> The implication: if you only fund infrastructure or only fund training, you cap how far an organization can go.

---

## Slide 8 — The contrarian finding: GN/GS reverses

> [Click to Fig 4]
>
> This is the slide that's going to surprise you.
>
> The standard story — Heeks, Toyama, the digital-divide literature — predicts that small Global South orgs without a tech specialist should fall furthest behind on a new technology wave. They should be the laggards.
>
> They're not. In the small, no-tech-specialist subset, Global South respondents use **0.42 more** AI tasks on average than their Global North counterparts. Oaxaca-Blinder decomposition: confirmed. Propensity-score matching on 132 pairs: confirmed. Inverse-probability weighting: confirmed. Three out of three robustness checks.
>
> The mechanism we suspect: consumer LLMs are accessible without infrastructure. Small GS orgs without an internal tech person have nothing to integrate against — they just use what's free. Small GN orgs without a tech person are working around legacy systems that don't talk to AI.

---

## Slide 9 — Latent typology: a willing-but-not-using middle

> [Click to Fig 3]
>
> One more piece of evidence for the comprehension story.
>
> The cluster column in the dataset is HDBSCAN — distance-based, fits whoever it fits. We re-fit the typology with a Latent Class Analysis, which is generative on binary items and BIC-grounded.
>
> The k=3 solution recovers a class — the orange line in the middle — with near-zero probability of *using* AI for any task, but high probability of *wanting* it for the analytical tasks.
>
> That's the disengaged-aspirational middle. The HDBSCAN cluster doesn't isolate it cleanly. The LCA does. It's about a third of the sample.

---

## Slide 10 — Robustness + effect sizes at a glance

> [Click to Fig 8 and Fig 9, two-panel]
>
> Twelve headline findings, six robustness checks each. Every row passes at least five out of six. The partials are documented in `robustness.md` — one subgroup tends to be the failure mode, never the primary result.
>
> On the right, the eleven main effect sizes with confidence intervals on a single forest plot. Different scales — gaps in percentage points, coefficients in log-rates — but visualised together so you can see the magnitudes against each other.
>
> The point of this slide is just: this is not one finding. It's a coherent set.

---

## Slide 11 — Why this matters

> Four reasons.
>
> First: most foundation and government funding for nonprofit AI is currently aimed at infrastructure — cloud credits, integration grants, technical staffing. The data say that for the median nonprofit those line items are not the binding constraint. That money will sit idle.
>
> Second: the gap is biggest on the analytical tasks. Those are the ones that move programmatic outcomes — needs assessment, targeting, M&E. Closing that gap is where the social-sector return compounds.
>
> Third: the standard digital-divide map points programs at small Global South orgs as the lagging cohort. On consumer AI, they're leading. Funding logic calibrated to the previous decade is going to misallocate.
>
> Fourth: the order matters. Comprehension is upstream of comfort, comfort is upstream of getting value out of infrastructure. Most current programs run the sequence backwards.

---

## Slide 12 — What to do

> Three concrete moves.
>
> Lead with comprehension training. Cohort-based, locally tailored, peer-anchored — closer to a farmer-field-school model than a webinar. Late Adopters already have the plumbing; they need the mental model.
>
> Build vigilance alongside comfort. In our data those two run in opposite directions — hands-on use raises risk awareness, subjective comfort lowers it. Training that produces only comfort will under-build the vigilance most users actually need.
>
> Localize analytical AI for the Global South. The translation gap shows up at +12pp in `[W]` over GN — that's where the next divide opens. Not on access.
>
> The full statistical detail is in `PAPER.md` and `METHODS.md` in the repo. Twenty-six pre-registered hypotheses, two-hundred-plus prior-literature paper-cards, full robustness battery.
>
> Thanks. Happy to take questions.

---

## Pacing notes

- Total target: ~7 minutes spoken.
- Slides 3 and 5 are the load-bearing slides — slow down here.
- Slide 8 is the "moment" — pause for half a beat before the reveal.
- Skip slide 9 if you're tight on time; it's confirmatory, not load-bearing.
- Q&A: expect questions on (a) sample representativeness — point at slide 4; (b) why the GN/GS reversal — point at the consumer-LLM mechanism on slide 8; (c) what comprehension training would look like — point at slide 12, agricultural-extension analogy.
