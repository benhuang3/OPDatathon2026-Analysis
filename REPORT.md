# Nonprofits already use AI — for writing. The next wave they want is analytical. The bottleneck isn't infrastructure or geography. **It's understanding.**

> An OP-Datathon 2026 report on the GivingTuesday 2024 AI Readiness survey (n=930).
> Lead with the headline: this is the only sentence that needs to land.

## Three things to know

**1. Nonprofits use AI for content. They want it for analytics.** When 930 nonprofit professionals tell us what they currently do with AI vs what they want to do, the pattern is sharp and one-sided. Generative content (text/images) is at parity (54% use, 55% want). But analytical tasks — predict outcomes, organize information, automate repetitive work, interpret data — show 35–41 percentage-point gaps between aspiration and reality. *Predict* is the most-wanted task at 52% and one of the least-used at 11%.

![Aspiration inversion](figures/fig1_aspiration_inversion.png)

This pattern survives every robustness check we ran: cluster bootstrap by survey list (95% CI excludes zero), inverse-probability reweighting against a target distribution, and three-method triangulation. *p* < 1×10⁻⁶⁶ on each of the four analytical tasks.

**2. The bottleneck is comprehension, not infrastructure.** When we look at *who* is stuck — orgs that want AI but don't use it — they aren't the ones missing tech. They're the ones missing understanding.

![Cluster profile](figures/fig10_cluster_profile.png)

Look at the middle column: "Late Adopters" have *higher* cloud storage adoption (63%) and *higher* data-policy adoption (66%) than the "AI Skeptics" group. They aren't blocked on plumbing. **52.8% of them say "I don't understand AI enough to have a clear view"** — versus 24% of Consumers. And in a multilevel logistic regression, saying "don't understand" is the single strongest non-adoption predictor independent of comfort, risk awareness, and org size (β = +0.16, p < 1e-7).

In a model with comfort, readiness, size, and tech specialist all competing as predictors of AI use, **comfort dominates everything**:

![Comfort dominates](figures/fig6_comfort_dominates.png)

Once comfort and readiness are in the model, structural variables — org size, tech specialist — are not statistically distinguishable from zero.

**3. The Global North/South divide reverses among small no-tech orgs.** This is the contrarian finding. The standard "digital divide" narrative — most recently endorsed by Heeks's adverse-incorporation thesis and Toyama's amplification model — predicts that small Global South orgs without a tech specialist should fall *furthest* behind on a new technology wave like AI. They don't.

![Oaxaca decomposition](figures/fig4_oaxaca_smallorg.png)

In the subset of small (≤15 staff) no-tech-person orgs, GS respondents use 0.42 *more* AI tasks on average than GN respondents. The gap survives Oaxaca–Blinder decomposition (raw +0.42), propensity-score matching (132 matched pairs, +0.15), and inverse-probability weighting (+0.42 — three of three robustness checks confirm). ~ Half of the gap is differences in resource endowments, half is differences in coefficients (i.e., GS orgs get *more out of* the same resources).

The mechanism is plausible: consumer LLMs (ChatGPT, free tiers) are accessible without infrastructure investment, and small GS orgs without an internal tech specialist have nothing to integrate against — they can use what's free. Small GN orgs without a tech specialist may be working around legacy systems that don't talk to AI.

## What follows

The bottleneck on closing the aspiration gap is *comprehension and comfort*, not infrastructure or geography. Capacity-building investment for nonprofit AI should:

- **Lead with comprehension training.** Cohort-based, locally-tailored, peer-anchored — analogous to the agricultural-extension shift from Training-and-Visit to farmer-field-schools. Late Adopters already have the plumbing; teach them what AI is and what they would do with it.
- **Recognize that comfort and vigilance run opposite directions.** Hands-on use raises risk awareness; subjective comfort lowers it. Both processes are real and both matter. Training that produces *only* comfort, without exposure to failures, will under-build the vigilance most users need.
- **Stop assuming the digital divide on AI looks like the digital divide on previous tech.** Small GS orgs without a tech specialist are a leading-edge cohort, not a lagging one — at least on the consumer-LLM stack. Localization of analytical AI (see translation gap, +12pp `[W]` over-indexing in GS) is where the divide will reappear, not on access.

The full statistical detail — 26 pre-registered hypotheses, 244 prior-literature paper-cards, robustness battery, methods appendix — lives in `PAPER.md`, `RESEARCH.md`, `METHODS.md`, and `analysis/`. This report is the headline. The headline is: *the bottleneck is understanding.*
