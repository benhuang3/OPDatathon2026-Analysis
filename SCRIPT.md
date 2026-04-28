# SCRIPT.md — Presenter script

Speaker notes for the slides in `SLIDES.md`. ~7 minute talk for a mixed-skill audience: policy analysts, foundation program officers, nonprofit directors, and the technically curious. Statistical methods are kept in the background; what's foregrounded is what each result *means* for a funding or program decision.

---

## Slide 1 — Title

> Hi. I'm going to give you one sentence and then spend seven minutes defending it.
>
> **Nonprofits already use AI — for writing. The next wave they want is analytical. And the thing standing between them and that wave is not money or infrastructure. It's understanding.**
>
> If you fund nonprofit capacity, design training, or set policy on technology in the social sector, this should change where you put the next dollar.

---

## Slide 2 — The data

> The dataset is the GivingTuesday 2024 AI Readiness Survey. 930 nonprofit professionals responded — directors, program staff, M&E people, technologists.
>
> They came in through four channels: the main GivingTuesday list (which is broadly representative of US and global nonprofits), an Indian sub-sample, a tech-leaning channel, and regional hubs.
>
> Each respondent told us what they currently do with AI, what they want to do with AI, what infrastructure their organization has, and how they feel about the technology. Plus an open-ended box, which a few of them answered in Hindi.
>
> One thing to flag up front: the Indian sub-sample is large — 27% of the total. I'll come back to this, but every result I'm about to show holds when you reweight away from it.

---

## Slide 3 — Headline: the aspiration inversion

> [Click to Fig 1]
>
> Here's the headline. On the left, paired bars: what people use AI for *today*, versus what they *want* to use it for. On the right, the gap between the two.
>
> Look at the top three rows — generate text, ask a chatbot, translate. Use and want are basically tied. Nonprofits are already using AI for content, and they're already getting what they want there.
>
> Now look at the bottom four — interpret data, assist with workflow, predict outcomes, organize information. These are the analytical tasks. The gaps are 35 to 41 percentage points. *Predict* is the most-wanted task in the survey, at 52%, and one of the least-used, at 11%.
>
> The picture is sharp: today's AI use is content. Tomorrow's demand is analytics.

---

## Slide 4 — It survives every check

> [Click to Fig 7]
>
> Before reading too much into this, the obvious question: is this just an artefact of who happens to be in the survey?
>
> No. We tested it three different ways. We re-ran the analysis after stripping out and rebuilding entire source channels — the gap held. We re-weighted the sample to a target mix that downweights the over-represented Indian channel and pulls up the under-represented ones — the per-task gaps moved by less than half a percentage point. And the statistical significance is overwhelming on every analytical task.
>
> What you're seeing is not a sample-quirk. It's a real pattern in the field.

---

## Slide 5 — The bottleneck is comprehension, not plumbing

> [Click to Fig 10]
>
> So who is stuck? Who *wants* AI but doesn't use it?
>
> The dataset gives us a three-group breakdown: Skeptics, Late Adopters, Consumers. The Late Adopters are the willing-but-not-using middle — the group most capacity-building dollars are aimed at.
>
> Look at the middle bars: cloud storage and data policy. Late Adopters score *higher* on infrastructure than the Skeptic group. They are not blocked on plumbing. They have the basics.
>
> What they're missing is something else: 53% of them say "I don't understand AI enough to have a clear view." Compared to 24% of the active-user group. **That's the bottleneck.** Not cloud, not policy, not staffing. Comprehension.

---

## Slide 6 — Comfort dominates structural variables

> [Click to Fig 6]
>
> Let's stress-test that. We modeled how much AI an organization uses, with four candidate explanations competing: how comfortable the *person* is with AI, how data-ready the *organization* is, whether they have a tech specialist on staff, and how big the org is.
>
> Personal comfort with AI is the largest factor by a wide margin. Data readiness is second. Organization size and having a tech specialist are statistically indistinguishable from zero once those two are in.
>
> In plain terms: how big you are and whether you have a tech person on staff don't predict AI use, once you account for whether the *people* in the org are comfortable with the technology. The human factor swamps the structural one.

---

## Slide 7 — Comfort and readiness reinforce each other

> [Click to Fig 2]
>
> Here's the same finding visualized differently. Personal comfort on one axis, organizational readiness on the other. The color is predicted AI use.
>
> Each axis pulls AI use up by roughly a factor of three across its full range. They reinforce each other.
>
> But there's a slight ceiling effect when both are high — you can't compensate for a weak leg by piling more onto your strong one. Practical implication: if you only fund infrastructure, or only fund training, you cap how far an organization can actually go. The two have to move together.

---

## Slide 8 — The contrarian finding: the digital divide reverses

> [Click to Fig 4]
>
> This is the slide I expect to surprise you the most.
>
> The standard story about technology in the Global South — and it's the story baked into most international capacity-building grants right now — predicts that small Global South nonprofits without an in-house tech person should fall *furthest* behind on a new technology wave like AI. They are supposed to be the laggards.
>
> They aren't. In the small, no-tech-specialist subset of our sample, Global South respondents use **0.42 more** AI tasks on average than their Global North counterparts. We confirmed this three different ways — different statistical approaches, all agreeing on the same direction and roughly the same magnitude.
>
> The mechanism we suspect: consumer AI like ChatGPT is free and accessible without infrastructure. Small GS orgs without an internal tech person have no legacy systems to integrate against — they can just use what's free. Small GN orgs without a tech person are often working around legacy systems that don't talk to AI yet.
>
> The implication for funders: the canonical "lagging cohort" you've been writing programs for is, on consumer AI, the leading cohort.

---

## Slide 9 — A willing-but-not-using middle

> [Click to Fig 3]
>
> One more piece of evidence for the comprehension story.
>
> When we re-fit the typology of respondents using a different statistical approach — one that's better-suited to the binary use-and-want survey items — a clear group emerges that the original three-cluster split misses.
>
> The orange line in the middle: this group has near-zero probability of *using* AI for any task, but high probability of *wanting* it for the analytical tasks. They want predict, interpret, assist, organize. They aren't doing any of it yet.
>
> That's the disengaged-aspirational middle. It's about a third of the sample. This is the group whose presence the headline is built on, and the group capacity programs should be designed around.

---

## Slide 10 — Why this matters

> Four implications.
>
> **First: most foundation and government funding for nonprofit AI is currently aimed at infrastructure** — cloud credits, integration grants, technical staffing. For the median nonprofit, those line items are not the binding constraint. If the bottleneck is comprehension and the program is plumbing, that money will sit idle. Or worse, build infrastructure that nobody on staff can articulate a use case for.
>
> **Second: the gap is biggest on the analytical tasks.** Predict, interpret, organize, assist. These are the tasks that move *programmatic* outcomes — needs assessments, targeting, M&E reporting, case management. Content AI is a productivity tool. Analytical AI is a programmatic capability. The aspiration gap sits exactly on the high-leverage side.
>
> **Third: the standard digital-divide map is pointing programs at the wrong cohort.** Small Global South nonprofits are leading on consumer AI, not lagging. Funding logic calibrated to the previous decade's digital divide is going to misallocate.
>
> **Fourth: the order matters.** Comprehension is upstream of comfort, comfort is upstream of getting value out of infrastructure. Most current capacity programs run the sequence backwards — they fund the tooling first and hope understanding follows. The data say it doesn't.

---

## Slide 11 — What to do

> Three concrete moves for the people in this room.
>
> **Lead with comprehension training, not tools.** Cohort-based, locally tailored, peer-anchored. Closer to the farmer-field-school model used in agricultural extension than to a one-off webinar. Late Adopters already have the plumbing; they need a working mental model of what AI is and what it would do for their program.
>
> **Build vigilance alongside comfort.** In our data those two move in opposite directions: hands-on use raises risk awareness, while subjective comfort *lowers* it. Training that produces only comfort, with no exposure to AI's failure modes, will under-build the caution most users actually need. That's the failure mode most likely to surface as misuse incidents two years from now, and it's preventable at training-design time.
>
> **Localize analytical AI for the Global South.** The translation gap shows up at +12 percentage points in *want* over GN — that's where the next divide opens. Not on access to AI. On AI that works in the languages and contexts where it's actually deployed.
>
> The full statistical detail is in `REPORT.md`, `PAPER.md`, and `METHODS.md` in the repo. Twenty-six pre-registered hypotheses, full robustness battery, two-hundred-plus prior-literature citations.
>
> Thanks. Happy to take questions.

---

## Pacing notes

- Total target: ~7 minutes spoken. Add 30 seconds if the room is quiet on slide 8 — let the surprise land.
- Slides 3, 5, and 8 are the load-bearing slides. Slow down here.
- Slide 8 is the "moment" — pause for half a beat before the reveal.
- Skip slide 9 if you're tight on time; it's confirmatory, not load-bearing.
- Audience translation cheat sheet in case anyone presses for method:
  - "We modeled" = regression with controls.
  - "Three different ways" = multiple statistical methods that agreed.
  - "Re-weighted the sample" = inverse-probability weighting against a target distribution.
  - "Different statistical approach for typology" = Latent Class Analysis instead of HDBSCAN.
- Q&A: expect questions on (a) sample representativeness — point at slide 4; (b) why the GN/GS reversal — consumer LLMs + no legacy systems, slide 8; (c) what comprehension training would look like — agricultural-extension analogy on slide 11.
