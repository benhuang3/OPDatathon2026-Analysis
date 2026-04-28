# Stream E — Risk perception & technology acceptance

Paper-cards on how people perceive risk and decide whether to accept new technologies — the canonical risk-perception, trust-in-automation, and technology-acceptance literatures, plus the algorithm-aversion vs algorithm-appreciation debate that frames how nonprofit staff actually approach AI tools.

---

## E1 — Slovic (1987)

```yaml
id: E1
stream: E
relevance_score: 5
peer_reviewed: yes
year: 1987
tags: [risk perception, psychometric paradigm, classic]
verified_url: yes
```

**Citation.** Slovic, P. (1987). Perception of risk. *Science*, 236(4799), 280–285.

**DOI / URL.** https://doi.org/10.1126/science.3563507

**Sample / Method.** Synthesis of psychometric studies (Decision Research lab, Oregon) on lay risk perception across dozens of hazards, mapped onto a two-factor space: **dread** (catastrophic, uncontrollable, fatal) × **unknown** (unobservable, new, delayed effects).

**Key claim(s).**
- Lay risk judgments are *not* irrational; they incorporate qualitative features experts ignore (controllability, voluntariness, dread, exposure of future generations).
- Hazards new and unknown sit in the upper-right of the dread×unknown space — exactly where novel technologies (nuclear power in 1987; AI today) tend to land.

**Takeaway.** AI is a textbook "unknown + dread" hazard for non-experts — predicting that less-informed respondents will perceive AI risks as both higher and more uniform than experts do.

**Confirms / Complicates / Contradicts.** Frames F-3 and F-4. Slovic predicts that comprehension shifts risk perception qualitatively, not just in magnitude — which matches our finding that "don't understand" respondents have *flatter* risk profiles (F-4) and that hands-on use *raises* (not lowers) selected risks (F-3).

---

## E2 — Slovic, Finucane, Peters & MacGregor (2004)

```yaml
id: E2
stream: E
relevance_score: 5
peer_reviewed: yes
year: 2004
tags: [affect heuristic, dual process, risk perception]
verified_url: yes
```

**Citation.** Slovic, P., Finucane, M. L., Peters, E., & MacGregor, D. G. (2004). Risk as analysis and risk as feelings: some thoughts about affect, reason, risk, and rationality. *Risk Analysis*, 24(2), 311–322.

**DOI / URL.** https://doi.org/10.1111/j.0272-4332.2004.00433.x

**Sample / Method.** Theoretical synthesis spanning psychometric, neuroscience, and behavioral-economics work on dual-process risk evaluation.

**Key claim(s).**
- Risk is processed two ways: an analytic system (probabilities, expected values) and an experiential/affective system (gut feeling).
- The two systems often disagree; affect typically dominates when stakes feel personal or vivid.

**Takeaway.** Predicts that subjective AI *comfort* (an affective signal) and selected AI *risks* (a more analytical inventory) should diverge — exactly the pattern in F-3, where comfort suppresses and use elevates risk count.

**Confirms / Complicates / Contradicts.** Confirms F-3's two-mechanism structure: comfort = affective system, hands-on use = analytic system updating its risk inventory. The two indeed run in opposite directions in our Poisson model.

---

## E3 — Finucane, Alhakami, Slovic & Johnson (2000)

```yaml
id: E3
stream: E
relevance_score: 5
peer_reviewed: yes
year: 2000
tags: [affect heuristic, risk-benefit inverse, classic]
verified_url: yes
```

**Citation.** Finucane, M. L., Alhakami, A., Slovic, P., & Johnson, S. M. (2000). The affect heuristic in judgments of risks and benefits. *Journal of Behavioral Decision Making*, 13(1), 1–17.

**DOI / URL.** https://doi.org/10.1002/(SICI)1099-0771(200001/03)13:1<1::AID-BDM333>3.0.CO;2-S

**Sample / Method.** Two experiments manipulating affect (time pressure; valence framing) and measuring judged risk and benefit of hazards.

**Key claim(s).**
- People reliably judge risks and benefits as *inversely* correlated even when they are objectively independent.
- Inducing positive affect lowers perceived risk and raises perceived benefit; the inverse relationship strengthens under time pressure.

**Takeaway.** Explains why `ai_risk_reward` collapses risk and reward into one dimension for many respondents: the affect heuristic *forces* an inverse coupling. The 33.8% who answer "I don't understand" may be the population that has not yet formed an affective stance.

**Confirms / Complicates / Contradicts.** Confirms F-3 mechanism (comfort suppresses risks). Complicates the survey's `ai_risk_reward` design: a single bipolar item pre-bakes the affect heuristic into the response.

---

## E4 — Fischhoff, Slovic, Lichtenstein, Read & Combs (1978)

```yaml
id: E4
stream: E
relevance_score: 5
peer_reviewed: yes
year: 1978
tags: [psychometric paradigm, dread, unknown, classic]
verified_url: yes
```

**Citation.** Fischhoff, B., Slovic, P., Lichtenstein, S., Read, S., & Combs, B. (1978). How safe is safe enough? A psychometric study of attitudes towards technological risks and benefits. *Policy Sciences*, 9, 127–152.

**DOI / URL.** https://doi.org/10.1007/BF00143739

**Sample / Method.** n=76 League of Women Voters members rating 30 activities/technologies on perceived risk, acceptable risk, and benefit; factor analysis revealed the dread × unknown structure.

**Key claim(s).**
- Two factors — dread risk and unknown risk — explain most variance in lay risk ratings.
- Acceptable risk depends on perceived benefit and on voluntariness, not solely on probability of harm.

**Takeaway.** The foundational two-factor structure that organizes how lay populations (including nonprofit staff) sort technology risks. AI risks in our data (bias, breaches, plagiarism, inequity, dependency, replacing-jobs, environmental) span both factors.

**Confirms / Complicates / Contradicts.** Frames F-4: bias and breaches are *known/dread* risks (frequently in news); inequity, dependency, environmental are *unknown/structural*. The asymmetric salience pattern is exactly what the dread × unknown framework predicts when public discourse spotlights one quadrant.

---

## E5 — Tversky & Kahneman (1974)

```yaml
id: E5
stream: E
relevance_score: 4
peer_reviewed: yes
year: 1974
tags: [heuristics and biases, anchoring, availability, classic]
verified_url: yes
```

**Citation.** Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: heuristics and biases. *Science*, 185(4157), 1124–1131.

**DOI / URL.** https://doi.org/10.1126/science.185.4157.1124

**Sample / Method.** Theoretical and experimental synthesis introducing representativeness, availability, and anchoring-and-adjustment heuristics.

**Key claim(s).**
- People estimate probabilities by retrieving easily available examples, leading to systematic biases.
- Numerical estimates (including risk magnitudes) anchor on irrelevant starting points.

**Takeaway.** Availability predicts that media-prominent AI risks (bias scandals, data breaches) will dominate respondent risk inventories — directly the pattern in F-4. Anchoring predicts the survey's bipolar `ai_risk_reward` scale will pull responses toward whatever frame the question provides.

**Confirms / Complicates / Contradicts.** Confirms F-4's salience asymmetry (availability of bias/breaches stories >> inequity/dependency stories).

---

## E6 — Kahneman & Tversky (1979)

```yaml
id: E6
stream: E
relevance_score: 4
peer_reviewed: yes
year: 1979
tags: [prospect theory, framing, loss aversion, classic]
verified_url: yes
```

**Citation.** Kahneman, D., & Tversky, A. (1979). Prospect theory: an analysis of decision under risk. *Econometrica*, 47(2), 263–291.

**DOI / URL.** https://doi.org/10.2307/1914185

**Sample / Method.** Experimental decision tasks with hypothetical gambles; theoretical model.

**Key claim(s).**
- Losses loom roughly twice as large as equivalent gains (loss aversion).
- People are risk-averse over gains but risk-seeking over losses; small probabilities are overweighted.

**Takeaway.** Predicts that nonprofit decision-makers will weigh AI's downside risks (bias lawsuits, donor backlash, mission drift) more than its upside benefits — explaining the gap between high `ai_want` and lower `ai_use`. The aspiration inversion (F-1) is partly a loss-aversion story: doing AI for analytics feels like a high-stakes loss bet, while writing assistance is a low-stakes gain.

**Confirms / Complicates / Contradicts.** Frames F-1's inversion as loss-aversion-rational, not irrational.

---

## E7 — Dietvorst, Simmons & Massey (2015)

```yaml
id: E7
stream: E
relevance_score: 5
peer_reviewed: yes
year: 2015
tags: [algorithm aversion, JEP-General, classic]
verified_url: yes
```

**Citation.** Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: people erroneously avoid algorithms after seeing them err. *Journal of Experimental Psychology: General*, 144(1), 114–126.

**DOI / URL.** https://doi.org/10.1037/xge0000033

**Sample / Method.** Five experiments (n≈360) on forecasting tasks comparing human judgment vs statistical algorithm.

**Key claim(s).**
- Even when shown that an algorithm out-performs humans, participants prefer the human after seeing the algorithm err once.
- Aversion is asymmetric — humans are forgiven errors at much higher rates than algorithms.

**Takeaway.** Predicts that nonprofit staff who've seen any AI mistake (a bad ChatGPT translation, a wrong summary) will disproportionately discount AI for *predictive* tasks — exactly where the use→want gap is widest in our data (Predict +40.5pp, F-1).

**Confirms / Complicates / Contradicts.** Confirms F-1: the predict/organize/interpret gap is plausibly an algorithm-aversion artifact. Disagrees with E8 (Logg et al., algorithm appreciation).

**Disagrees with.** E8.

---

## E8 — Logg, Minson & Moore (2019)

```yaml
id: E8
stream: E
relevance_score: 5
peer_reviewed: yes
year: 2019
tags: [algorithm appreciation, OBHDP, advice taking]
verified_url: yes
```

**Citation.** Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: people prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes*, 151, 90–103.

**DOI / URL.** https://doi.org/10.1016/j.obhdp.2018.12.005

**Sample / Method.** Six pre-registered experiments (n≈1,500) comparing acceptance of advice labelled "algorithm" vs "human."

**Key claim(s).**
- Lay people (non-experts) update *more* toward algorithmic advice than human advice.
- Effect reverses among experts (who prefer their own judgment) and weakens among the less-numerate.

**Takeaway.** Frames the comprehension bottleneck (F-10): if a respondent has never *seen* an AI suggestion, they cannot exhibit appreciation. Late Adopters (high comprehension deficit, F-10) lack the exposure that drives Logg's appreciation effect.

**Confirms / Complicates / Contradicts.** Complicates F-1: contra Dietvorst, an unencountered algorithm should attract demand. The Predict/Organize *want* spike is consistent with appreciation among the never-tried.

**Disagrees with.** E7.

---

## E9 — Dietvorst, Simmons & Massey (2018)

```yaml
id: E9
stream: E
relevance_score: 4
peer_reviewed: yes
year: 2018
tags: [algorithm aversion, control, intervention]
verified_url: yes
```

**Citation.** Dietvorst, B. J., Simmons, J. P., & Massey, C. (2018). Overcoming algorithm aversion: people will use imperfect algorithms if they can (even slightly) modify them. *Management Science*, 64(3), 1155–1170.

**DOI / URL.** https://doi.org/10.1287/mnsc.2016.2643

**Sample / Method.** Three experiments (n≈1,200) varying user control over algorithm output.

**Key claim(s).**
- Giving users *any* ability to adjust the algorithm's output (even within tight bounds) substantially raises uptake.
- The mechanism is autonomy, not accuracy — even useless modifications work.

**Takeaway.** Recommendation pathway for closing the use-want gap (F-1): nonprofit-facing AI tools that let users edit/adjust forecasts will be adopted faster than locked black-box predictors.

**Confirms / Complicates / Contradicts.** Provides an actionable mechanism for the F-1 gap.

---

## E10 — Castelo, Bos & Lehmann (2019)

```yaml
id: E10
stream: E
relevance_score: 4
peer_reviewed: yes
year: 2019
tags: [algorithm aversion, task type, marketing]
verified_url: yes
```

**Citation.** Castelo, N., Bos, M. W., & Lehmann, D. R. (2019). Task-dependent algorithm aversion. *Journal of Marketing Research*, 56(5), 809–825.

**DOI / URL.** https://doi.org/10.1177/0022243719851788

**Sample / Method.** Four lab studies + two field studies (n>56,000 in field).

**Key claim(s).**
- Algorithm aversion is task-dependent: stronger for "subjective" tasks, weaker for "objective" tasks.
- Increasing perceived objectivity of a task (or affective human-likeness of the algorithm) reduces aversion.

**Takeaway.** Predicts uneven AI uptake across our seven task categories. Generate (subjective→creative) is high-uptake among nonprofits in our data only because LLMs are framed as writing assistants, not as creative authors. Predict and Organize feel more "objective" → high *want* (F-1).

**Confirms / Complicates / Contradicts.** Helps explain F-1's task-by-task pattern.

---

## E11 — Longoni, Bonezzi & Morewedge (2019)

```yaml
id: E11
stream: E
relevance_score: 4
peer_reviewed: yes
year: 2019
tags: [algorithm aversion, uniqueness neglect, healthcare]
verified_url: yes
```

**Citation.** Longoni, C., Bonezzi, A., & Morewedge, C. K. (2019). Resistance to medical artificial intelligence. *Journal of Consumer Research*, 46(4), 629–650.

**DOI / URL.** https://doi.org/10.1093/jcr/ucz013

**Sample / Method.** Eleven experiments (n>2,500) on consumer willingness to use AI vs human providers in medical contexts.

**Key claim(s).**
- People resist AI providers because they believe AI cannot account for their *unique* circumstances ("uniqueness neglect").
- Resistance persists even when AI is described as more accurate.

**Takeaway.** Direct mechanism for resistance to *Interpret* and *Predict* AI tasks in nonprofit work: program officers see each beneficiary as unique, and AI is perceived as failing to accommodate that. Adds nuance to F-1's gap.

**Confirms / Complicates / Contradicts.** Confirms F-1 and complicates F-15: skeptic disengagement may include implicit uniqueness-neglect concerns even when respondents do not select inequity/dependency on the risk inventory.

---

## E12 — Bigman & Gray (2018)

```yaml
id: E12
stream: E
relevance_score: 3
peer_reviewed: yes
year: 2018
tags: [moral aversion, machine ethics, mind perception]
verified_url: yes
```

**Citation.** Bigman, Y. E., & Gray, K. (2018). People are averse to machines making moral decisions. *Cognition*, 181, 21–34.

**DOI / URL.** https://doi.org/10.1016/j.cognition.2018.08.003

**Sample / Method.** Nine experiments (n≈6,000) varying decision domain (medical, legal, military, driving).

**Key claim(s).**
- Aversion intensifies when decisions are morally weighty and is mediated by perceived inability of machines to "think and feel."
- The effect attenuates when machines act as advisors rather than deciders.

**Takeaway.** Nonprofit work is morally weighty almost by definition (whom to fund, whom to serve). Predicts that AI uptake should be lowest for tasks where mistakes have moral consequences — consistent with the lower current use of Interpret and Predict (F-1) on case-management decisions.

**Confirms / Complicates / Contradicts.** Frames F-1 from a moral-aversion angle.

---

## E13 — Burton, Stein & Jensen (2020)

```yaml
id: E13
stream: E
relevance_score: 4
peer_reviewed: yes
year: 2020
tags: [systematic review, algorithm aversion]
verified_url: yes
```

**Citation.** Burton, J. W., Stein, M.-K., & Jensen, T. B. (2020). A systematic review of algorithm aversion in augmented decision making. *Journal of Behavioral Decision Making*, 33(2), 220–239.

**DOI / URL.** https://doi.org/10.1002/bdm.2155

**Sample / Method.** Systematic review of 61 peer-reviewed papers (1950–2018) on algorithm aversion.

**Key claim(s).**
- Five recurring causes: expectations/expertise mismatch, decision autonomy, incentivization, cognitive (in)compatibility, and divergent rationalities.
- Solutions cluster around enhancing decision autonomy and aligning with users' expectations.

**Takeaway.** Provides the integrative frame for E7–E12. The cognitive-incompatibility theme directly maps onto F-10's comprehension bottleneck.

**Confirms / Complicates / Contradicts.** Confirms F-10 (comprehension is a primary blocker, not just a secondary one).

---

## E14 — Lee & See (2004)

```yaml
id: E14
stream: E
relevance_score: 5
peer_reviewed: yes
year: 2004
tags: [trust in automation, classic, human factors]
verified_url: yes
```

**Citation.** Lee, J. D., & See, K. A. (2004). Trust in automation: designing for appropriate reliance. *Human Factors*, 46(1), 50–80.

**DOI / URL.** https://doi.org/10.1518/hfes.46.1.50_30392

**Sample / Method.** Theoretical synthesis of 20+ years of trust-in-automation research; framework paper.

**Key claim(s).**
- Trust comprises three dimensions: performance (does it work), process (how does it work), and purpose (why was it built).
- Calibrated trust requires that perceived trustworthiness match actual reliability — both over- and under-trust are failures.

**Takeaway.** Predicts that nonprofit AI uptake depends on all three dimensions: today's GenAI delivers on *performance* (visible writing output) but is opaque on *process* and *purpose* — explaining why use is concentrated in low-stakes generation tasks (F-1).

**Confirms / Complicates / Contradicts.** Frames F-3 vs F-15: hands-on users improve calibration (more risks selected as their performance/process map fills in); skeptics never built the map (under-trust → disengagement).

---

## E15 — Hoff & Bashir (2015)

```yaml
id: E15
stream: E
relevance_score: 5
peer_reviewed: yes
year: 2015
tags: [trust in automation, three-layer model, review]
verified_url: yes
```

**Citation.** Hoff, K. A., & Bashir, M. (2015). Trust in automation: integrating empirical evidence on factors that influence trust. *Human Factors*, 57(3), 407–434.

**DOI / URL.** https://doi.org/10.1177/0018720814547570

**Sample / Method.** Systematic review synthesizing 100+ empirical trust-in-automation studies.

**Key claim(s).**
- Three layers of trust: dispositional (stable individual differences), situational (context), and learned (experience-based).
- Each layer has identifiable design and training levers.

**Takeaway.** Maps cleanly onto our variables: `person_ai_comfort` ≈ dispositional + learned; `org_size` and `tech_person` ≈ situational. F-9's 2×2 (comfort × infrastructure) is exactly Hoff & Bashir's dispositional × situational decomposition.

**Confirms / Complicates / Contradicts.** Confirms F-9 framing.

---

## E16 — Glikson & Woolley (2020)

```yaml
id: E16
stream: E
relevance_score: 5
peer_reviewed: yes
year: 2020
tags: [trust in AI, AOM Annals, review]
verified_url: yes
```

**Citation.** Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence: review of empirical research. *Academy of Management Annals*, 14(2), 627–660.

**DOI / URL.** https://doi.org/10.5465/annals.2018.0057

**Sample / Method.** Narrative review of 20 years of AI-trust empirical research; organizes findings by AI representation (robotic / virtual / embedded) and by cognitive vs emotional trust.

**Key claim(s).**
- Cognitive trust forms quickly with reliable AI; emotional trust requires anthropomorphic cues and time.
- Tangibility of AI representation moderates trust formation.

**Takeaway.** Predicts that LLM chatbots (high tangibility, conversational) build cognitive *and* emotional trust faster than embedded/black-box predictive systems — explaining why Generate is the dominant current use (F-1) but not the dominant aspiration.

**Confirms / Complicates / Contradicts.** Confirms F-1's task asymmetry.

---

## E17 — Shin (2021)

```yaml
id: E17
stream: E
relevance_score: 4
peer_reviewed: yes
year: 2021
tags: [explainable AI, XAI, trust, causability]
verified_url: yes
```

**Citation.** Shin, D. (2021). The effects of explainability and causability on perception, trust, and acceptance: implications for explainable AI. *International Journal of Human-Computer Studies*, 146, 102551.

**DOI / URL.** https://doi.org/10.1016/j.ijhcs.2020.102551

**Sample / Method.** Online experiment + survey on news-recommendation AI; structural-equation model of explainability → causability → trust → acceptance.

**Key claim(s).**
- Explainability (model surfaces reasons) builds *cognitive* trust.
- Causability (user understands the explanation) builds *emotional* confidence and is the binding precondition.

**Takeaway.** Direct mechanism for F-10: Late Adopters report not understanding AI; explanations alone won't help unless they're *causable* (intelligible to that user). Predicts that bilingual / locally-relevant explainability will be especially valuable in our India / Africa subsamples.

**Confirms / Complicates / Contradicts.** Confirms F-10 (comprehension as bottleneck) and F-14 (translation gap in GS).

---

## E18 — Mayer, Davis & Schoorman (1995)

```yaml
id: E18
stream: E
relevance_score: 4
peer_reviewed: yes
year: 1995
tags: [organizational trust, ABI model, classic]
verified_url: yes
```

**Citation.** Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). An integrative model of organizational trust. *Academy of Management Review*, 20(3), 709–734.

**DOI / URL.** https://doi.org/10.5465/amr.1995.9508080335

**Sample / Method.** Theoretical synthesis.

**Key claim(s).**
- Trust = ability + benevolence + integrity (ABI).
- Trust enables risk-taking; perceived risk and trust interact to produce reliance.

**Takeaway.** Foundational lens for the Lee & See (E14) extension to automation. ABI maps onto our `person_ai_comfort` (a global trust judgment) and decomposes it: AI ability (does it work), benevolence (whose interests), integrity (was it built honestly).

**Confirms / Complicates / Contradicts.** Frames F-3, F-15.

---

## E19 — Parasuraman & Riley (1997)

```yaml
id: E19
stream: E
relevance_score: 4
peer_reviewed: yes
year: 1997
tags: [automation, use misuse disuse abuse, classic]
verified_url: yes
```

**Citation.** Parasuraman, R., & Riley, V. (1997). Humans and automation: use, misuse, disuse, abuse. *Human Factors*, 39(2), 230–253.

**DOI / URL.** https://doi.org/10.1518/001872097778543886

**Sample / Method.** Theoretical / review.

**Key claim(s).**
- Four failure modes around automation: use (appropriate reliance), misuse (overtrust), disuse (under-reliance after false alarms), abuse (system designers ignoring human factors).
- Disuse and misuse are equally costly errors.

**Takeaway.** F-15's "Skeptics" cluster fits the *disuse* pattern: under-engagement, not informed-rejection. F-3's heavy users approach the *misuse* end on the comfort dimension (suppressed risk awareness).

**Confirms / Complicates / Contradicts.** Confirms F-15 (disuse) and F-3 (over-comfort risks misuse).

---

## E20 — Jian, Bisantz & Drury (2000)

```yaml
id: E20
stream: E
relevance_score: 3
peer_reviewed: yes
year: 2000
tags: [trust scale, measurement, methodology]
verified_url: yes
```

**Citation.** Jian, J.-Y., Bisantz, A. M., & Drury, C. G. (2000). Foundations for an empirically determined scale of trust in automated systems. *International Journal of Cognitive Ergonomics*, 4(1), 53–71.

**DOI / URL.** https://doi.org/10.1207/S15327566IJCE0401_04

**Sample / Method.** Three-phase scale-development study (word elicitation; questionnaire; paired comparison).

**Key claim(s).** Trust and distrust are partially distinct constructs, not endpoints of one scale. Produces the widely used 12-item trust-in-automation scale.

**Takeaway.** Method critique of `ai_risk_reward` as a single bipolar item: trust and distrust may need separate measurement, and the −1 "don't understand" code is implicitly a third construct (comprehension), not a low-trust pole.

**Confirms / Complicates / Contradicts.** Method-only; informs `ai_risk_reward` interpretation.

---

## E21 — Davis (1989)

```yaml
id: E21
stream: E
relevance_score: 5
peer_reviewed: yes
year: 1989
tags: [TAM, technology acceptance, classic]
verified_url: yes
```

**Citation.** Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly*, 13(3), 319–340.

**DOI / URL.** https://doi.org/10.2307/249008

**Sample / Method.** Two studies (n=152) developing and validating perceived-usefulness and perceived-ease-of-use scales.

**Key claim(s).**
- Two parsimonious constructs predict adoption intent: perceived usefulness (PU) and perceived ease of use (PEOU).
- PU is the stronger predictor; PEOU has both direct and PU-mediated effects.

**Takeaway.** Maps directly onto `person_ai_comfort` (≈PEOU) and `want_count` / `ai_risk_reward` (≈PU). F-20 (comfort is the strongest single correlate of use) is consistent with TAM but inverts the usual TAM finding that PU > PEOU — suggesting nonprofit staff are stuck on ease-of-use, not usefulness.

**Confirms / Complicates / Contradicts.** Complicates classical TAM ordering; confirms F-20's emphasis on comfort.

---

## E22 — Venkatesh & Davis (2000)

```yaml
id: E22
stream: E
relevance_score: 4
peer_reviewed: yes
year: 2000
tags: [TAM2, social influence, longitudinal]
verified_url: yes
```

**Citation.** Venkatesh, V., & Davis, F. D. (2000). A theoretical extension of the technology acceptance model: four longitudinal field studies. *Management Science*, 46(2), 186–204.

**DOI / URL.** https://doi.org/10.1287/mnsc.46.2.186.11926

**Sample / Method.** Four longitudinal field studies (n=156 across four organizations); voluntary and mandatory adoption settings.

**Key claim(s).**
- TAM2 adds social influence (subjective norm, voluntariness, image) and cognitive instrumental processes (job relevance, output quality, result demonstrability) to TAM.
- Social influence dominates early in adoption; cognitive instrumental processes dominate later.

**Takeaway.** Predicts that early-stage AI adoption in nonprofits is driven by peer signaling (sector buzz) more than demonstrated ROI — consistent with the Aspirational tier's huge `want` numbers (F-18) without comparable use.

**Confirms / Complicates / Contradicts.** Frames F-18 (Aspirationals tier).

---

## E23 — Venkatesh, Thong & Xu (2012) — UTAUT2

```yaml
id: E23
stream: E
relevance_score: 4
peer_reviewed: yes
year: 2012
tags: [UTAUT2, consumer technology, hedonic motivation]
verified_url: yes
```

**Citation.** Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology: extending the unified theory of acceptance and use of technology. *MIS Quarterly*, 36(1), 157–178.

**DOI / URL.** https://doi.org/10.2307/41410412

**Sample / Method.** Two-stage online survey (n=1,512 mobile-Internet consumers) with 4-month follow-up on actual use.

**Key claim(s).**
- UTAUT2 adds three constructs: hedonic motivation (fun), price value, and habit.
- Habit is the single strongest predictor of continued use.

**Takeaway.** Hedonic motivation explains the surprising stickiness of generative AI for writing in our sample (F-2, generative is the only saturated task). Habit predicts that the Power Users tier (F-18) will keep their high use independent of capacity-building effort.

**Confirms / Complicates / Contradicts.** Frames F-2 (Generate-saturation) and F-18 (Power Users tier).

---

## E24 — Bansal et al. (2021)

```yaml
id: E24
stream: E
relevance_score: 3
peer_reviewed: yes
year: 2021
tags: [XAI, explanations, team performance, CHI]
verified_url: yes
```

**Citation.** Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Ribeiro, M. T., & Weld, D. (2021). Does the whole exceed its parts? The effect of AI explanations on complementary team performance. *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems*.

**DOI / URL.** https://doi.org/10.1145/3411764.3445717

**Sample / Method.** Three crowdsourced studies (n>1,500) on human–AI decision teams across NLP and beer-review domains.

**Key claim(s).**
- AI explanations raise *acceptance* of AI suggestions but do not improve team accuracy.
- Explanations function as a trust signal, not a calibration tool.

**Takeaway.** Cautions against assuming explanation features will close the F-10 comprehension gap: explanations may produce trust without comprehension, the worst combination.

**Confirms / Complicates / Contradicts.** Complicates simple "add XAI features" prescription that would follow from F-10.

---

## E25 — Bucinca, Malaya & Gajos (2021)

```yaml
id: E25
stream: E
relevance_score: 3
peer_reviewed: yes
year: 2021
tags: [XAI, overreliance, cognitive forcing, CSCW]
verified_url: yes
```

**Citation.** Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW1), Article 188.

**DOI / URL.** https://doi.org/10.1145/3449287

**Sample / Method.** Three crowdsourced experiments testing cognitive-forcing UI interventions (e.g., delayed AI advice, on-demand explanations).

**Key claim(s).**
- Overreliance on AI is the modal failure, not under-reliance.
- Cognitive-forcing functions reduce overreliance — but most for participants high in Need for Cognition (i.e., people already inclined to think analytically).

**Takeaway.** Pairs with F-3: heavy users with high comfort suppress risk awareness (the overreliance pattern). Cognitive-forcing UI is a candidate intervention to maintain vigilance among Power Users (F-18).

**Confirms / Complicates / Contradicts.** Confirms F-3 (comfort suppresses vigilance).

---

## E26 — Madianou (2021)

```yaml
id: E26
stream: E
relevance_score: 4
peer_reviewed: yes
year: 2021
tags: [humanitarian AI, structural risks, postcolonial]
verified_url: yes
```

**Citation.** Madianou, M. (2021). Nonhuman humanitarianism: when 'AI for good' can be harmful. *Information, Communication & Society*, 24(6), 850–868.

**DOI / URL.** https://doi.org/10.1080/1369118X.2021.1909100

**Sample / Method.** Critical / qualitative analysis of humanitarian AI deployments (chatbots, biometrics, predictive modeling).

**Key claim(s).**
- "AI for good" reproduces colonial power asymmetries even when deployed with benevolent intent.
- Structural risks (data colonialism, dependency, displacement of local capacity) are systematically under-discussed.

**Takeaway.** Provides the structural-risk vocabulary that is *missing* from our F-4 risk inventory: bias and breaches dominate, while inequity and dependency (Madianou's structural risks) are under-selected. The asymmetry isn't neutral — it reflects whose risks get named.

**Confirms / Complicates / Contradicts.** Confirms F-4 (salience asymmetry) and adds an explanation: discourse foregrounds individual-level risks and obscures structural ones.

---

## E27 — Selbst, Boyd, Friedler, Venkatasubramanian & Vertesi (2019)

```yaml
id: E27
stream: E
relevance_score: 3
peer_reviewed: yes
year: 2019
tags: [fairness, sociotechnical, FAT*]
verified_url: yes
```

**Citation.** Selbst, A. D., Boyd, D., Friedler, S. A., Venkatasubramanian, S., & Vertesi, J. (2019). Fairness and abstraction in sociotechnical systems. *Proceedings of the 2019 Conference on Fairness, Accountability, and Transparency (FAT\*)*, 59–68.

**DOI / URL.** https://doi.org/10.1145/3287560.3287598

**Sample / Method.** Conceptual paper.

**Key claim(s).**
- Five "traps" in fair-ML work, including the Framing Trap (treating fairness as a property of the model, not the system) and the Portability Trap (assuming fairness solutions transfer between contexts).
- Fairness is a property of sociotechnical systems, not of algorithms.

**Takeaway.** Predicts that bias risk (F-4's most-selected risk) is poorly addressed by tool-level fixes alone — implying a capacity-building need rather than a procurement need.

**Confirms / Complicates / Contradicts.** Frames F-4's bias dominance as risk-of-deployment, not risk-of-tool.

---

## E28 — Binns et al. (2018)

```yaml
id: E28
stream: E
relevance_score: 3
peer_reviewed: yes
year: 2018
tags: [algorithmic justice, perceptions, CHI]
verified_url: yes
```

**Citation.** Binns, R., Van Kleek, M., Veale, M., Lyngs, U., Zhao, J., & Shadbolt, N. (2018). 'It's reducing a human being to a percentage': perceptions of justice in algorithmic decisions. *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems*.

**DOI / URL.** https://doi.org/10.1145/3173574.3173951

**Sample / Method.** Three online studies (n≈400) on perceived justice of algorithmic vs human decisions across explanation styles.

**Key claim(s).**
- Justice perceptions of algorithmic decisions track procedural-justice cues (voice, explanation) similarly to human decisions.
- Salient concerns: arbitrariness, generalisation, and indignity ("reducing a person to a number").

**Takeaway.** "Indignity" maps onto the inequity / dependency risks under-selected in F-4 — a qualitative confirmation that lay ethical discourse names structural risks even when surveys' fixed risk lists nudge respondents elsewhere.

**Confirms / Complicates / Contradicts.** Complicates F-4 by suggesting open-ended response would surface more inequity / dependency concern than the fixed-list survey reveals.

---

## E29 — Sundar (2020)

```yaml
id: E29
stream: E
relevance_score: 3
peer_reviewed: yes
year: 2020
tags: [HAII, machine agency, theory]
verified_url: yes
```

**Citation.** Sundar, S. S. (2020). Rise of machine agency: a framework for studying the psychology of human–AI interaction (HAII). *Journal of Computer-Mediated Communication*, 25(1), 74–88.

**DOI / URL.** https://doi.org/10.1093/jcmc/zmz026

**Sample / Method.** Theoretical / framework paper extending Theory of Interactive Media Effects to AI.

**Key claim(s).**
- AI affordances act symbolically (cues that signal "AI") and enabling-ly (changes in what users can do) — both shape perception independent of accuracy.
- Algorithmic agency cues can paradoxically *increase* perceived authority and *decrease* user agency.

**Takeaway.** Frames why "AI" branding matters: respondents' `person_ai_comfort` is a response to the *symbolic* cue as much as to actual capability. Predicts that uptake will be sensitive to how a tool is labelled (e.g., "AI assistant" vs "data tool").

**Confirms / Complicates / Contradicts.** Frames F-20 (comfort dominance).

---

## E30 — Araujo, Helberger, Kruikemeier & de Vreese (2020)

```yaml
id: E30
stream: E
relevance_score: 4
peer_reviewed: yes
year: 2020
tags: [public trust in AI, automated decision-making, survey]
verified_url: yes
```

**Citation.** Araujo, T., Helberger, N., Kruikemeier, S., & de Vreese, C. H. (2020). In AI we trust? Perceptions about automated decision-making by artificial intelligence. *AI & Society*, 35(3), 611–623.

**DOI / URL.** https://doi.org/10.1007/s00146-019-00931-w

**Sample / Method.** National-sample scenario survey experiment in the Netherlands (n=958) varying AI-decision contexts (media, health, judicial).

**Key claim(s).**
- General attitudes toward AI decisions are mixed; concerns about risks dominate concerns about fairness.
- Knowledge and prior experience of AI moderate trust and acceptance.

**Takeaway.** Direct prior on the comprehension bottleneck (F-10): in a representative sample, knowledge moderates trust. Predicts that closing the F-10 gap (through training) should disproportionately move Late Adopters from disengagement toward engagement.

**Confirms / Complicates / Contradicts.** Confirms F-10.

---

## E31 — Cave, Coughlan & Dihal (2019)

```yaml
id: E31
stream: E
relevance_score: 3
peer_reviewed: yes
year: 2019
tags: [public attitudes, AI narratives, AIES]
verified_url: yes
```

**Citation.** Cave, S., Coughlan, K., & Dihal, K. (2019). 'Scary robots': examining public responses to AI. *Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society (AIES)*, 331–337.

**DOI / URL.** https://doi.org/10.1145/3306618.3314232

**Sample / Method.** Nationally representative UK survey on responses to eight common AI narratives (four optimistic, four pessimistic).

**Key claim(s).**
- Pessimistic narratives (job loss, surveillance, dehumanization) are more believed than optimistic ones.
- Most respondents feel they cannot influence AI's trajectory.

**Takeaway.** External-population baseline against which the GivingTuesday sample's surprisingly high `ai_want` looks self-selected: nonprofit respondents who took the survey are more techno-optimist than the UK general public.

**Confirms / Complicates / Contradicts.** Frames F-1 (high aspiration) as partly a sample-selection artifact.

---

## E32 — Zhang & Dafoe (2019)

```yaml
id: E32
stream: E
relevance_score: 3
peer_reviewed: no  # research report
year: 2019
tags: [public opinion, AI governance, US]
verified_url: yes
```

**Citation.** Zhang, B., & Dafoe, A. (2019). *Artificial intelligence: American attitudes and trends*. Center for the Governance of AI, Future of Humanity Institute, University of Oxford.

**DOI / URL.** https://www.governance.ai/research-paper/artificial-intelligence-american-attitudes-and-trends

**Sample / Method.** Nationally representative US survey (n=2,000).

**Key claim(s).**
- Americans are anxious about AI governance challenges; trust in tech companies to develop AI is moderate; trust in government to regulate it is low.
- Support for "high-level machine intelligence" being developed is split; support for safety research is high.

**Takeaway.** External baseline. The 33.8% "I don't understand AI" response in our sample is in line with Zhang & Dafoe's finding that most Americans report low AI familiarity — F-10 is not a nonprofit-specific deficit.

**Confirms / Complicates / Contradicts.** Frames F-10 as sector-general, not sector-specific.

---

## E33 — Edelman (2024)

```yaml
id: E33
stream: E
relevance_score: 3
peer_reviewed: no  # industry report
year: 2024
tags: [trust barometer, AI, NGOs, global]
verified_url: yes
```

**Citation.** Edelman (2024). *2024 Edelman Trust Barometer — Innovation in Peril* (with AI special-report supplement).

**DOI / URL.** https://www.edelman.com/trust/2024/trust-barometer

**Sample / Method.** 30-minute online interviews with 32,000+ respondents across 28 countries (Nov 2023).

**Key claim(s).**
- 26-point gap between trust in tech companies (76%) and trust in AI specifically (50%).
- NGOs are seen as "good managers of change" when they help people keep up with innovation.

**Takeaway.** External population baseline. Half of the global public distrusts AI even when trusting the tech sector — predicting that nonprofit *external stakeholders* (donors, beneficiaries) hold higher AI risk perceptions than nonprofit *staff* in our sample.

**Confirms / Complicates / Contradicts.** Background; suggests our internal-sample risk inventory underestimates external-stakeholder risk perception.

---

## E34 — Slovic (2010), edited volume

```yaml
id: E34
stream: E
relevance_score: 3
peer_reviewed: yes
year: 2010
tags: [risk perception, affect, edited volume]
verified_url: yes
```

**Citation.** Slovic, P. (2010). *The feeling of risk: new perspectives on risk perception*. London: Earthscan / Routledge.

**DOI / URL.** https://doi.org/10.4324/9781849776677 (ISBN 978-1849711487).

**Sample / Method.** Edited collection of Slovic's 2000s-era papers on risk-as-feelings, cultural cognition, and worldview-determined perceptions.

**Key claim(s).**
- Risk perception is partly determined by cultural worldviews — facts and values jointly produce risk judgments.
- Affect is causally upstream of cognitive risk evaluation, not merely a downstream reaction.

**Takeaway.** Predicts that organization-level cultures (cause area, values) should modulate AI risk inventories. Our F-19 finds weak cause-area effects on use; this volume suggests the cause-area effect would be stronger on *which risks* are selected, not on overall use level.

**Confirms / Complicates / Contradicts.** Predicts an unanalyzed dimension (cause-area × risk-selection) for Phase 5–6.

---

## E35 — Acemoglu & Restrepo (2020)

```yaml
id: E35
stream: E
relevance_score: 2
peer_reviewed: yes
year: 2020
tags: [labor displacement, automation, structural risk]
verified_url: yes
```

**Citation.** Acemoglu, D., & Restrepo, P. (2020). Robots and jobs: evidence from US labor markets. *Journal of Political Economy*, 128(6), 2188–2244.

**DOI / URL.** https://doi.org/10.1086/705716

**Sample / Method.** Empirical analysis of US commuting-zone employment exposure to industrial robots (1990–2007).

**Key claim(s).**
- One additional robot per 1,000 workers reduces local employment-to-population by 0.2pp and wages by 0.42%.
- Effects concentrate in routine-manual occupations.

**Takeaway.** Provides the empirical basis for "replacing" as a real (not hypothetical) AI risk. In our F-4 inventory, "replacing" is selected by only 32.5% — possibly under-weighted given the labor-economics evidence base.

**Confirms / Complicates / Contradicts.** Complicates F-4 (replacing under-selected relative to economics evidence).

---

## Stream E synthesis

The classical risk-perception canon (E1–E6) anticipates two of our most distinctive findings. Slovic's psychometric paradigm (E1, E4) and the affect heuristic (E2, E3) jointly predict that AI — a "dread + unknown" hazard — should produce risk inventories shaped by **availability** (E5) rather than by structural analysis: bias and breaches sit prominently in news and in respondents' selections, while inequity and dependency under-index (F-4). Madianou's critique (E26) and the FAT\* tradition (E27, E28) explain *why* this asymmetry is not neutral.

The headline tension between **F-3 and the popular "comfort breeds vigilance-decay" narrative** sits at the intersection of two literatures. The **MIT SMR / BCG comfort-blunts-risk framing** (which we could not verify as a peer-reviewed paper but is a known industry-report stance) is consistent with the *misuse* end of Parasuraman & Riley (E19) and with the over-reliance pattern in Buçinca et al. (E25). But Lee & See (E14) and the trust-as-calibration tradition predict the opposite: hands-on use should *improve* risk discrimination because it surfaces concrete failure modes. **Our F-3 is the resolution: comfort and use are different mechanisms running in opposite directions.** Comfort (the affective signal, Slovic E2) suppresses risk count; use (the analytic signal, Lee & See E14) raises it. The two halves of the literature are both right; they just describe different variables.

The **algorithm-aversion vs algorithm-appreciation debate** (E7 Dietvorst et al. vs E8 Logg et al.) maps cleanly onto our cluster structure. Dietvorst's aversion appears among the *previously-burned*: respondents who tried AI and saw it err. Logg's appreciation appears among the *never-tried*: respondents who haven't formed a personal failure-experience. Our F-1 inversion (low use, high want for analytical tasks) is consistent with appreciation among the never-tried and the saturating Generate use is consistent with aversion in some Power Users (F-2's sign-flip). Burton, Stein & Jensen's review (E13) provides the mechanism set linking these to F-10's comprehension bottleneck.

The **technology-acceptance lineage** (E21 TAM → E22 TAM2 → E23 UTAUT2) frames our 2×2 (F-9): comfort ≈ ease-of-use × dispositional trust; infrastructure ≈ facilitating conditions × situational trust. F-20's finding that comfort is the strongest single correlate of use suggests our nonprofit population is bottlenecked at PEOU rather than at PU — an inversion of the canonical TAM ordering, and a hint that the binding constraint is *cognitive accessibility* rather than perceived value. Combined with Shin's (E17) causability work, this points to training-and-translation as the highest-leverage capacity-building investment, consistent with F-10 (Late-Adopter Paradox) and F-14 (translation gap in Global South).
