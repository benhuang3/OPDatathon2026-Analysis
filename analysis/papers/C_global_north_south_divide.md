# Stream C — Global North / South digital divide

Paper-cards for prior work on how the GN/GS divide manifests (or does not) in NGO and civil-society technology adoption, with specific attention to AI / ML localization and "amplification vs leveling" debates.

---

## C1 — Heeks (2022) — Adverse digital incorporation

```yaml
id: C1
stream: C
relevance_score: 5
peer_reviewed: yes
year: 2022
tags: [ICT4D, digital divide, Global South, inequality]
verified_url: yes
```

**Citation.** Heeks, R. (2022). Digital inequality beyond the digital divide: conceptualizing adverse digital incorporation in the global South. *Information Technology for Development*, 28(4), 688–704.

**DOI / URL.** https://doi.org/10.1080/02681102.2022.2068492

**Sample / Method.** Conceptual paper synthesizing ICT4D, development studies, and political-economy literatures.

**Key claim(s).**
- The "divide" framing (in vs out) is outdated; GS users *are* online, but on disadvantageous terms — included into systems that extract disproportionate value from them.
- Inequality migrates from access to terms of incorporation (data extraction, platform dependency, asymmetric value capture).

**Takeaway for our dataset.** Predicts the GN/GS gap will not appear on adoption *rates* (cluster3) but on *terms* — which `[U]`/`[W]` tasks differ, and how dependent vs autonomous each side is on GN-built tools.

**Confirms / Complicates / Contradicts.** **Complicates** F-12 (the null on continent post-controls) and **predicts** F-14 (translation `[W]` over-indexes in GS — incorporation on disadvantageous linguistic terms). Reframes F-8 not as a "reversal" but as evidence of GS being *incorporated* into consumer-LLM platforms while GN orgs build institutional stacks.

**Disagrees with.** A naive reading of A25 (Andreasson) that treats divides purely as access deficits.

---

## C2 — Nemer (2022) — Technology of the Oppressed

```yaml
id: C2
stream: C
relevance_score: 5
peer_reviewed: yes
year: 2022
tags: [Latin America, ethnography, decolonial, favela]
verified_url: yes
```

**Citation.** Nemer, D. (2022). *Technology of the Oppressed: Inequity and the Digital Mundane in Favelas of Brazil*. Cambridge, MA: MIT Press.

**DOI / URL.** https://mitpress.mit.edu/9780262543347/technology-of-the-oppressed/  (open access via https://direct.mit.edu/books/oa-monograph/5266/)

**Sample / Method.** Multi-year ethnographic fieldwork in Brazilian favelas, telecenters, and lan-houses; decolonial Mundane-Technology analytic framework drawing on Freire.

**Key claim(s).**
- The deficit narrative is empirically wrong at the user level — favela residents are sophisticated, creative technology users.
- Inequities live in *institutional* infrastructure and political economy, not in user capability.
- Technology is simultaneously a site of oppression and a tool of liberation, depending on institutional surround.

**Takeaway.** **Confirms the null** on individual-level measures (`person_ai_comfort`, `cluster3` continent effect) and predicts the gap reappears on `tech_person`, `org_size`, `data_use_policy` — which is what F-12 finds.

**Confirms / Complicates / Contradicts.** Confirms F-12 (regional effects vanish after size + tech_person). Complicates F-8 (small-org reversal): Nemer would say GS users have always been ahead of where institutional narratives place them.

---

## C3 — NASSCOM Foundation & CGI (2021) — India's First Tech for Good Report

```yaml
id: C3
stream: C
relevance_score: 4
peer_reviewed: no  # industry / foundation report
year: 2021
tags: [India, NGO, Tech4Good, NASSCOM]
verified_url: yes
```

**Citation.** NASSCOM Foundation & CGI (2021). *India's First Tech for Good Report*. NASSCOM Foundation.

**DOI / URL.** https://www.cgi.com/en/article/esg/strengthening-partnership-nasscom-foundation-india-first-tech-good-report  (organization page: https://www.nasscomfoundation.org/techforgood)

**Sample / Method.** Survey of 548 organizations: 305 NGOs, 124 social enterprises/startups, 119 corporates.

**Key claim(s).**
- 91% of organizations view "Tech for Good" as a strategic focus.
- A small minority of Indian NGOs have dedicated technology staff; rural and Tier-3 city NGOs lag metro NGOs sharply on tooling and on staff capacity.

**Takeaway.** Directly testable in our data with `india_rural_urban` × `tech_person`. Predicts F-3 / F-7 patterns specifically inside the India subset (n=251).

**Confirms / Complicates / Contradicts.** Confirms F-7 (size + specialist roles dominate). Complicates F-5 (India not lower-comfort) — the NASSCOM framing assumes a metro/non-metro stratification our data partially flattens.

---

## C4 — Dasra & Bain (2024) — India Philanthropy Report

```yaml
id: C4
stream: C
relevance_score: 4
peer_reviewed: no  # industry/foundation report
year: 2024
tags: [India, philanthropy, Dasra, Bain, funding]
verified_url: yes
```

**Citation.** Dasra & Bain & Company (2024). *India Philanthropy Report 2024: Philanthropy as the bridge for impact in India's growth*. Mumbai: Dasra.

**DOI / URL.** https://www.bain.com/insights/india-philanthropy-report-2024/  (PDF: https://dasra.org/pdf/resources/1712033199.pdf)

**Sample / Method.** 14th edition; combines public-portal data, GivingPi member data, and 122 anonymized in-depth interviews with high-net-worth givers.

**Key claim(s).**
- Indian social-sector expenditure grew at 13% CAGR over 5 years to ~INR 23 lakh crore (8.3% of GDP) in FY 2023, but still 4.7% short of NITI Aayog's annual target.
- Private giving up 10% YoY; the binding constraint on tech adoption among Indian NGOs is donor-funded capacity-building, not user willingness.

**Takeaway.** Predicts large `[W] − [U]` gaps in India relative to GN — Indian NGOs interested in AI but lacking funded capacity to operationalize.

**Confirms / Complicates / Contradicts.** Confirms the universal-aspiration finding (F-19) within India. **Complicates** F-5 — comfort is not the bottleneck; donor-side capacity is, which our dataset cannot directly observe.

---

## C5 — Friederici, Ojanperä & Graham (2017) — Connectivity in Africa

```yaml
id: C5
stream: C
relevance_score: 5
peer_reviewed: yes
year: 2017
tags: [Africa, EJISDC, connectivity, OII, hubs]
verified_url: yes
```

**Citation.** Friederici, N., Ojanperä, S., & Graham, M. (2017). The impact of connectivity in Africa: grand visions and the mirage of inclusive digital development. *The Electronic Journal of Information Systems in Developing Countries*, 79(2), 1–20.

**DOI / URL.** https://doi.org/10.1002/j.1681-4835.2017.tb00578.x  (SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2855398)

**Sample / Method.** Mixed-methods analysis of African connectivity indicators and qualitative fieldwork on innovation hubs.

**Key claim(s).**
- African digital-economy participation concentrates in urban innovation hubs.
- Rural civil society sees little of the promised "leapfrog" effect; benefits flow to a thin urban tier.

**Takeaway.** Frames H9: within `continent='Africa'`, urban-hub respondents should look more like GN, while rural-Africa respondents should diverge.

**Confirms / Complicates / Contradicts.** **Contradicts F-13** — in our (small-n) Africa subset, rural Africa actually *exceeds* urban Africa on `use_count`. This may be a GivingTuesday-Hub selection artifact, but it is a striking inversion of Friederici's prediction.

---

## C6 — Toyama (2015) — Geek Heresy / Law of Amplification

```yaml
id: C6
stream: C
relevance_score: 5
peer_reviewed: no  # trade book; the underlying argument is academic
year: 2015
tags: [amplification, ICT4D, classic, Toyama]
verified_url: yes
```

**Citation.** Toyama, K. (2015). *Geek Heresy: Rescuing Social Change from the Cult of Technology*. New York: PublicAffairs. (Foundational Atlantic essay: Toyama, K. (2011). "Technology Is Not the Answer." *The Atlantic*, March 2011.)

**DOI / URL.** https://geekheresy.org/  (Atlantic essay archived under "Law of Amplification" tag)  ISBN 978-1610395281.

**Sample / Method.** Synthesis of ~10 years of ICT4D field studies (Microsoft Research India and academic).

**Key claim(s).**
- "Law of Amplification": technology amplifies existing human/institutional intent and capacity — it does not substitute for either.
- Where capacity is asymmetric (GN vs GS, large vs small org), tech *widens* gaps rather than closing them.

**Takeaway.** Predicts the size × N/S × `tech_person` interaction: GN/GS gaps should be largest where existing capacity is most asymmetric.

**Confirms / Complicates / Contradicts.** **Contradicts F-8** sharply — Toyama predicts small GS orgs without tech support should fall *furthest* behind; our data shows the *opposite*. This is the central theoretical disagreement the paper can adjudicate. Possible reconciliation: consumer LLMs are unusually substitutive (rather than purely amplificatory) because GS-side institutional barriers (procurement, legal, IT) don't gate them.

**Disagrees with.** C2 (Nemer) — Nemer would predict the F-8 result; Toyama would not.

---

## C7 — Png (2022) — At the Tensions of South and North

```yaml
id: C7
stream: C
relevance_score: 5
peer_reviewed: yes
year: 2022
tags: [FAccT, AI governance, Global South, decolonial]
verified_url: yes
```

**Citation.** Png, M.-T. (2022). At the tensions of South and North: critical roles of Global South stakeholders in AI governance. In *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT '22)* (pp. 1434–1445).

**DOI / URL.** https://doi.org/10.1145/3531146.3533200  (PDF: https://facctconference.org/static/pdfs_2022/facct22-3533200.pdf)

**Sample / Method.** Critical literature synthesis + interviews with GS AI-governance practitioners.

**Key claim(s).**
- GS organizations face GN-built AI tools that are poorly fit to local contexts (language, data, regulation).
- High *adoption* can coexist with low *fit*; the right metric is appropriateness, not penetration.

**Takeaway.** Translation/language `[W]` should over-index in GS as orgs try to localize GN-built models.

**Confirms / Complicates / Contradicts.** **Confirms F-14** directly: translation `[W]` over-indexes 11.9pp in GS while no other task differs by >6pp. This is the cleanest hit on a Stream C prior in our data.

---

## C8 — Avgerou (2019) — Contextual explanation

```yaml
id: C8
stream: C
relevance_score: 4
peer_reviewed: yes
year: 2019
tags: [MISQ, ICT4D, theory, contextual]
verified_url: yes
```

**Citation.** Avgerou, C. (2019). Contextual explanation: alternative approaches and persistent challenges. *MIS Quarterly*, 43(3), 977–1006.

**DOI / URL.** https://doi.org/10.25300/MISQ/2019/13990  (AISeL: https://aisel.aisnet.org/misq/vol43/iss3/15/)

**Sample / Method.** Conceptual / methodological review of contextual explanation in IS research.

**Key claim(s).**
- IS adoption patterns reflect local rationalities, not lag along a fixed GN trajectory.
- "Contextual explanation" requires letting context configure the dependent variable, not just moderate effects on a universal model.

**Takeaway.** Frames the cluster3 null on continent as substantive (not a null due to missing covariates) — different orgs use AI for locally rational reasons.

**Confirms / Complicates / Contradicts.** Confirms F-12 (continent vanishes post-controls) as a substantively meaningful finding rather than a power problem.

**Disagrees with.** C6 (Toyama) — Toyama assumes a single development trajectory; Avgerou rejects that frame.

---

## C9 — Mohamed, Png & Isaac (2020) — Decolonial AI

```yaml
id: C9
stream: C
relevance_score: 5
peer_reviewed: yes
year: 2020
tags: [decolonial, AI ethics, Philosophy & Technology, theory]
verified_url: yes
```

**Citation.** Mohamed, S., Png, M.-T., & Isaac, W. (2020). Decolonial AI: decolonial theory as sociotechnical foresight in artificial intelligence. *Philosophy & Technology*, 33, 659–684.

**DOI / URL.** https://doi.org/10.1007/s13347-020-00405-8  (preprint: https://arxiv.org/abs/2007.04068)

**Sample / Method.** Conceptual paper drawing on post- and decolonial theory.

**Key claim(s).**
- AI development reproduces colonial patterns: extraction of data/labor from GS, deployment of algorithmic governance, ghost-work asymmetries.
- Three tactics: critical technical practice, reverse tutelage, renewed political community.

**Takeaway.** Predicts that the `ai_risk` items selected by GS respondents will tilt toward dependency / inequity (structural) rather than bias / breaches (technical), if respondents have decolonial framings.

**Confirms / Complicates / Contradicts.** Complicates F-4 (bias + breaches >> inequity + dependency). The Madianou-style risk-salience asymmetry holds globally in our data — decolonial framings are not visibly dominating GS risk selections, suggesting either limited diffusion of these framings into NGO discourse or that the Madianou pattern is robust.

---

## C10 — Birhane (2021) — Algorithmic injustice

```yaml
id: C10
stream: C
relevance_score: 4
peer_reviewed: yes
year: 2021
tags: [algorithmic justice, relational ethics, Patterns]
verified_url: yes
```

**Citation.** Birhane, A. (2021). Algorithmic injustice: a relational ethics approach. *Patterns*, 2(2), 100205.

**DOI / URL.** https://doi.org/10.1016/j.patter.2021.100205  (open access: https://www.sciencedirect.com/science/article/pii/S2666389921000155)

**Sample / Method.** Conceptual / philosophical argument.

**Key claim(s).**
- Algorithmic-fairness work is too narrowly scoped — debiasing datasets does not address upstream power asymmetries.
- Justice should be "relational" — sensitive to context, history, and social structure — not a property of a model.

**Takeaway.** Predicts that nonprofit AI risk-perception should track structural concerns (inequity, dependency) more than technical ones (bias, breaches), particularly among orgs working with vulnerable populations.

**Confirms / Complicates / Contradicts.** Complicates F-4 — same pattern as C9. The structural framing is theoretically dominant in critical AI literature but empirically not yet reshaping nonprofit risk salience in our sample.

---

## C11 — Walsham (2002) — Cross-cultural software production

```yaml
id: C11
stream: C
relevance_score: 4
peer_reviewed: yes
year: 2002
tags: [Walsham, MISQ, structuration, cross-cultural]
verified_url: yes
```

**Citation.** Walsham, G. (2002). Cross-cultural software production and use: a structurational analysis. *MIS Quarterly*, 26(4), 359–380.

**DOI / URL.** https://doi.org/10.2307/4132313  (AISeL: https://aisel.aisnet.org/misq/vol26/iss4/5/)

**Sample / Method.** Structuration-theoretic analysis of two cross-cultural cases (Jamaican-Indian software team; UK-India outsourcing).

**Key claim(s).**
- Structurational analysis goes beyond Hofstede-style culture-dimension models in explaining cross-cultural IS phenomena.
- Cross-cultural IS work *changes* the underlying values of participants over time, not just outputs.

**Takeaway.** Frames the long-run question: AI tools built in GN, used in GS, should over time reshape both sides — not a static divide.

**Confirms / Complicates / Contradicts.** Frames F-14 (translation gap) as a transient artifact of current GN-centric model design; predicts the gap shrinks as multi-lingual models mature.

---

## C12 — Walsham (2017) — ICT4D research reflections

```yaml
id: C12
stream: C
relevance_score: 4
peer_reviewed: yes
year: 2017
tags: [ICT4D, review, Walsham]
verified_url: yes
```

**Citation.** Walsham, G. (2017). ICT4D research: reflections on history and future agenda. *Information Technology for Development*, 23(1), 18–41.

**DOI / URL.** https://doi.org/10.1080/02681102.2016.1246406

**Sample / Method.** Reflective review of 30+ years of ICT4D research, broken into three phases.

**Key claim(s).**
- ICT4D field has matured from optimism (Phase 1) through critical scrutiny (Phase 2) into a multidisciplinary stage (Phase 3).
- Future agenda must address theory, methods, and impact assessment more rigorously.

**Takeaway.** Method scaffolding for our Phase 5 — multidisciplinary methods (LCA, IRT, BERTopic) over single-discipline approaches.

**Confirms / Complicates / Contradicts.** Method-only framing.

---

## C13 — Heeks (2002) — IS failure in developing countries

```yaml
id: C13
stream: C
relevance_score: 4
peer_reviewed: yes
year: 2002
tags: [Heeks, design-actuality, developing countries]
verified_url: yes
```

**Citation.** Heeks, R. (2002). Information systems and developing countries: failure, success, and local improvisations. *The Information Society*, 18(2), 101–112.

**DOI / URL.** https://doi.org/10.1080/01972240290075039

**Sample / Method.** Synthesis of e-government project evaluations in developing countries.

**Key claim(s).**
- 35% of IS projects total failures; 50% partial failures; 15% successes.
- "Design-actuality gap" between GN-designed system and local user actuality is the core mechanism.

**Takeaway.** Predicts that GN-built AI tooling will partially fail in GS NGO use unless local improvisation closes the gap. The translation `[W]` finding (F-14) is one expression of this gap.

**Confirms / Complicates / Contradicts.** Confirms F-14 mechanism (design-actuality gap on language). Complicates F-8 — predicts that GS small-org adoption is high but partially failing in unmeasured ways (effective use vs nominal use).

---

## C14 — Heeks (2008) — ICT4D 2.0

```yaml
id: C14
stream: C
relevance_score: 3
peer_reviewed: yes
year: 2008
tags: [Heeks, ICT4D 2.0, paradigm]
verified_url: yes
```

**Citation.** Heeks, R. (2008). ICT4D 2.0: the next phase of applying ICT for international development. *Computer*, 41(6), 26–33.

**DOI / URL.** https://doi.org/10.1109/MC.2008.192

**Sample / Method.** Conceptual paradigm paper.

**Key claim(s).**
- Shift from supply-driven (ICT4D 1.0) to demand-driven (2.0) framing — GS users as active producers and innovators, not passive recipients.

**Takeaway.** Frames F-8 as predictable under a 2.0 paradigm: GS orgs *should* be using consumer LLMs creatively when freed from supply-side constraints.

**Confirms / Complicates / Contradicts.** Provides theoretical scaffolding for F-8. Reconciles partly with C6 (Toyama) — the amplification argument was a 1.0-era framing.

---

## C15 — Couldry & Mejias (2019) — Data colonialism

```yaml
id: C15
stream: C
relevance_score: 4
peer_reviewed: yes
year: 2019
tags: [data colonialism, Television New Media, critical]
verified_url: yes
```

**Citation.** Couldry, N., & Mejias, U. A. (2019). Data colonialism: rethinking big data's relation to the contemporary subject. *Television & New Media*, 20(4), 336–349.

**DOI / URL.** https://doi.org/10.1177/1527476418796632

**Sample / Method.** Critical/theoretical paper.

**Key claim(s).**
- Data extraction parallels historical colonial appropriation: territory → data, labor → human attention/behavior.
- Resistance requires re-thinking ownership, not just consent.

**Takeaway.** Sharpens C1 (Heeks adverse incorporation): GS NGOs using GN consumer LLMs are not just under-served — they are sites of data extraction.

**Confirms / Complicates / Contradicts.** Background framing for F-8 / F-14. Predicts that "GS uses more AI" (F-8) has a hidden cost: more data flowing one direction.

---

## C16 — Bender, Gebru, McMillan-Major & Shmitchell (2021) — Stochastic Parrots

```yaml
id: C16
stream: C
relevance_score: 4
peer_reviewed: yes
year: 2021
tags: [LLM, FAccT, language, environmental]
verified_url: yes
```

**Citation.** Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610–623).

**DOI / URL.** https://doi.org/10.1145/3442188.3445922

**Sample / Method.** Critical synthesis of LLM research literature.

**Key claim(s).**
- Large language models concentrate on high-resource (English, mostly GN) data; low-resource languages are systematically under-represented.
- Risks: environmental cost, opacity, encoded bias, hegemonic-language privilege.

**Takeaway.** Direct mechanism for F-14: GS NGOs need translation/language `[W]` because the dominant LLMs underperform in non-English and low-resource languages.

**Confirms / Complicates / Contradicts.** Confirms F-14 mechanistically.

---

## C17 — Sambasivan, Kapania, Highfill, Akrong, Paritosh & Aroyo (2021) — Data Cascades

```yaml
id: C17
stream: C
relevance_score: 5
peer_reviewed: yes
year: 2021
tags: [CHI, data cascades, India, Africa, high-stakes AI]
verified_url: yes
```

**Citation.** Sambasivan, N., Kapania, S., Highfill, H., Akrong, D., Paritosh, P., & Aroyo, L. (2021). "Everyone wants to do the model work, not the data work": data cascades in high-stakes AI. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems (CHI '21)*.

**DOI / URL.** https://doi.org/10.1145/3411764.3445518

**Sample / Method.** Interviews with n=53 AI practitioners across India, East and West Africa, and the US, working on health, conservation, food, road safety, credit, environment.

**Key claim(s).**
- 92% prevalence of "data cascades" — compounding downstream errors caused by upstream data-quality neglect.
- The cascades are heaviest in high-stakes GS deployments where data infrastructure is weakest.

**Takeaway.** Predicts that the analytical-AI aspiration in F-1 (Predict, Organize, Interpret, Assist) will be especially fragile for GS NGOs without data infrastructure (`cloud_storage`, `data_use_policy`).

**Confirms / Complicates / Contradicts.** Confirms F-9 (infrastructure is one of two locks). Complicates F-1 — the aspiration gap may be even larger than measured because GS orgs underestimate the data-readiness requirements of analytical AI.

---

## C18 — Donner (2015) — After Access

```yaml
id: C18
stream: C
relevance_score: 3
peer_reviewed: yes
year: 2015
tags: [mobile internet, Global South, MIT Press]
verified_url: yes
```

**Citation.** Donner, J. (2015). *After Access: Inclusion, Development, and a More Mobile Internet*. Cambridge, MA: MIT Press.

**DOI / URL.** https://mitpress.mit.edu/9780262029926/after-access/  ISBN 978-0262029926.

**Sample / Method.** Synthesis of fieldwork in South Africa and India plus the broader ICT4D literature.

**Key claim(s).**
- Once basic access is achieved, the binding constraint shifts to "effective use" — what can be done on mobile-only digital repertoires.
- Mobile-only users face structural limits (creation, multitasking, screen real estate) that desktop users do not.

**Takeaway.** Predicts a mobile-only gap on creation/Generate tasks vs Consumption/Ask tasks in GS — relevant to interpreting F-1's task-by-task pattern.

**Confirms / Complicates / Contradicts.** Background for F-1. The dataset doesn't directly capture device type, but Donner's frame predicts under-provision of the "Generate" task in mobile-only orgs.

---

## C19 — Arora (2019) — The Next Billion Users

```yaml
id: C19
stream: C
relevance_score: 3
peer_reviewed: yes
year: 2019
tags: [Global South, leisure, digital ethnography]
verified_url: yes
```

**Citation.** Arora, P. (2019). *The Next Billion Users: Digital Life Beyond the West*. Cambridge, MA: Harvard University Press.

**DOI / URL.** https://www.hup.harvard.edu/books/9780674983786  ISBN 978-0674983786.

**Sample / Method.** Multi-site ethnography across India, China, Brazil, South Africa, Middle East.

**Key claim(s).**
- The Western "global poor as utilitarian users" framing is empirically wrong — leisure, pleasure, and entertainment are central uses.
- Rejects the deficit narrative and the assumption of a universal trajectory.

**Takeaway.** Re-frames F-8: GS small orgs may use AI more *because* the cultural-fit barrier is lower than ICT4D theory assumes — they are sophisticated, motivated, and unconstrained by Western utility framings.

**Confirms / Complicates / Contradicts.** Provides theoretical support for F-8 alongside C2 (Nemer).

---

## C20 — Hilbert (2011) — Manifold definitions of the digital divide

```yaml
id: C20
stream: C
relevance_score: 4
peer_reviewed: yes
year: 2011
tags: [digital divide, Latin America, policy, measurement]
verified_url: yes
```

**Citation.** Hilbert, M. (2011). The end justifies the definition: the manifold outlooks on the digital divide and their practical usefulness for policy-making. *Telecommunications Policy*, 35(8), 715–736.

**DOI / URL.** https://doi.org/10.1016/j.telpol.2011.06.012  (open: https://martinhilbert.net/ManifoldDigitalDivide_Hilbert_AAM.pdf)

**Sample / Method.** Conceptual + Latin American empirics on ICT-affordability thresholds.

**Key claim(s).**
- The digital divide is a multidimensional gradient (have-how-much), not a binary.
- Latin American affordability threshold ≈ US$10/person/month or US$120/year for ICT spend.

**Takeaway.** Frames `org_size_int` and `cloud_storage` as proxies for "how much" rather than "have or not." Aligns with our continuous-readiness modeling.

**Confirms / Complicates / Contradicts.** Methodological — supports F-9's gradient framing of readiness.

---

## C21 — van Deursen, van Dijk, & colleagues (2017) — Second/third-level digital divide

```yaml
id: C21
stream: C
relevance_score: 4
peer_reviewed: yes
year: 2017
tags: [digital divide, skills, outcomes, van Dijk]
verified_url: yes
```

**Citation.** Scheerder, A., van Deursen, A., & van Dijk, J. (2017). Determinants of Internet skills, uses and outcomes: a systematic review of the second- and third-level digital divide. *Telematics and Informatics*, 34(8), 1607–1624.

**DOI / URL.** https://doi.org/10.1016/j.tele.2017.07.007

**Sample / Method.** Systematic review of digital-divide research focused on skills (2nd-level) and outcomes (3rd-level), beyond access.

**Key claim(s).**
- After access (1st-level), inequalities re-emerge in skills (2nd-level) and outcomes / impacts (3rd-level).
- These higher-level divides are *less* tied to GN/GS geography and *more* tied to education, age, and occupation.

**Takeaway.** Provides a clean theoretical frame for F-12 (continent vanishes) and F-9 (comfort × infra 2×2): once access is universalized via consumer LLMs, GN/GS shrinks but skills/outcomes divides reappear within each.

**Confirms / Complicates / Contradicts.** Confirms F-12 and F-9.

---

## C22 — Sey, Hafkin et al. (2019) — EQUALS Taking Stock

```yaml
id: C22
stream: C
relevance_score: 3
peer_reviewed: no  # UN/EQUALS report; multi-author
year: 2019
tags: [gender, EQUALS, UN, digital divide]
verified_url: yes
```

**Citation.** Sey, A., & Hafkin, N. (Eds.) (2019). *Taking Stock: Data and Evidence on Gender Equality in Digital Access, Skills and Leadership*. EQUALS Global Partnership / UNU-CS / ITU.

**DOI / URL.** https://www.itu.int/en/action/gender-equality/Documents/EQUALS%20Research%20Report%202019.pdf  (also archived at the UN: https://www.unwomen.org/...EQUALS report)

**Sample / Method.** Multi-author synthesis (53 researchers, 20+ organizations) of gender-digital-equality data and evidence.

**Key claim(s).**
- Gender digital divide persists irrespective of overall ICT access, GDP, or geography.
- Skills, leadership, and infrastructure barriers operate semi-independently.

**Takeaway.** Background. Our dataset does not include respondent gender, so this is a known unmeasured axis. Adds caution to F-12 — geography may vanish, but other axes are silent in our model.

**Confirms / Complicates / Contradicts.** Background framing for unmeasured heterogeneity.

---

## C23 — Qureshi (2015) — Are we making a better world with ICT4D?

```yaml
id: C23
stream: C
relevance_score: 3
peer_reviewed: yes
year: 2015
tags: [ICT4D, ITD, theory-building]
verified_url: yes
```

**Citation.** Qureshi, S. (2015). Are we making a better world with information and communication technology for development (ICT4D) research? Findings from the field and theory building. *Information Technology for Development*, 21(4), 511–522.

**DOI / URL.** https://doi.org/10.1080/02681102.2015.1080428

**Sample / Method.** Editorial / synthesis of the field.

**Key claim(s).**
- Most ICT4D research is conducted by non-indigenous scholars; Western theory transferred onto GS contexts is a methodological hazard.
- Calls for indigenous theory-building and local typologies.

**Takeaway.** Methodological caution: our N/S split is a coarse proxy; richer typologies (LCA, MCA) are appropriate.

**Confirms / Complicates / Contradicts.** Method-only.

---

## C24 — Nekoto et al. / Masakhane (2020) — Participatory NLP for African languages

```yaml
id: C24
stream: C
relevance_score: 4
peer_reviewed: yes
year: 2020
tags: [Masakhane, NLP, African languages, low-resource]
verified_url: yes
```

**Citation.** Nekoto, W., Marivate, V., Matsila, T., Fasubaa, T., Fagbohungbe, T., Akinola, S. O., et al. (2020). Participatory research for low-resourced machine translation: a case study in African languages. In *Findings of the Association for Computational Linguistics: EMNLP 2020*.

**DOI / URL.** https://doi.org/10.18653/v1/2020.findings-emnlp.195  (preprint: https://arxiv.org/abs/2010.02353)  Org: https://www.masakhane.io/

**Sample / Method.** Participatory case study spanning 28+ African languages and 25+ contributors.

**Key claim(s).**
- "Low-resourcedness" is not just a data problem — it is a community, infrastructure, benchmark, and incentive problem.
- Participatory grassroots research outperforms top-down NLP for under-served languages.

**Takeaway.** Mechanism behind F-14: GS demand for translation `[W]` reflects a real performance gap that grassroots projects (Masakhane) are working to close.

**Confirms / Complicates / Contradicts.** Confirms F-14 mechanism alongside C16 (Bender et al.).

---

## C25 — ECLAC (2020) — Universalizing access to digital technologies

```yaml
id: C25
stream: C
relevance_score: 3
peer_reviewed: no  # UN regional commission report
year: 2020
tags: [ECLAC, Latin America, COVID, connectivity]
verified_url: yes
```

**Citation.** ECLAC (2020). *Universalizing access to digital technologies to address the consequences of COVID-19* (COVID-19 Special Report No. 7). Santiago: Economic Commission for Latin America and the Caribbean.

**DOI / URL.** https://repositorio.cepal.org/handle/11362/45939  (press: https://www.cepal.org/en/pressreleases/eclac-proposes-ensuring-and-universalizing-connectivity-and-affordability-digital)

**Sample / Method.** Regional analysis of LAC connectivity and pandemic-era digital inequality.

**Key claim(s).**
- 66.7% of LAC inhabitants had Internet in 2019; 36% of children 5–12 lived in unconnected households.
- Only 21.3% of LAC employed could telework, vs ~40% in EU/US.
- Connectivity, affordability, and speed gaps deepen pre-existing structural inequalities.

**Takeaway.** Provides a regional baseline for the LAC subset of our `gt` source. Predicts that within-LAC variation should be large and access-mediated.

**Confirms / Complicates / Contradicts.** Background for F-12 (regional effects); supports the size + infrastructure mediation interpretation.

---

## C26 — Birhane, Kalluri, Card, Agnew, Dotan & Bao (2022) — The Values Encoded in ML Research

```yaml
id: C26
stream: C
relevance_score: 3
peer_reviewed: yes
year: 2022
tags: [FAccT, ML values, audit, ethics]
verified_url: unable
```

**Citation.** Birhane, A., Kalluri, P., Card, D., Agnew, W., Dotan, R., & Bao, M. (2022). The values encoded in machine learning research. In *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT '22)*.

**DOI / URL.** https://doi.org/10.1145/3531146.3533083  (preprint: https://arxiv.org/abs/2106.15590) — listed as additional context but not separately re-verified beyond DOI lookup; relevance_score lowered by 1 per protocol.

**Sample / Method.** Annotation of 100 highly cited NeurIPS / ICML papers for stated values.

**Key claim(s).**
- ML research values concentrate on performance, novelty, generalization — and almost never on user wellbeing, justice, or distributional impact.
- The values shape what "AI for good" actually optimizes for in deployment contexts.

**Takeaway.** Background for the misalignment between GS NGO needs (analytic, predictive, locally fitted) and what GN ML research actually optimizes (benchmarks, scale).

**Confirms / Complicates / Contradicts.** Background framing for F-1's aspiration gap.

---

## Stream C synthesis

The Stream C literature splits along a **sharp theoretical fault line** about whether the GN/GS divide reappears at the institutional level once individual-access gaps are closed. **Heeks (C1, C13, C14) and Toyama (C6)** argue yes: adverse incorporation, design-actuality gaps, and the law of amplification all predict that small / under-resourced GS orgs face *widening* gaps as new tech waves arrive — gaps measurable in `tech_person`, `org_size`, and effective-use indicators. **Avgerou (C8) and Nemer (C2)**, joined by Arora (C19) and the data-colonialism critics (C15, C9, C10), argue no: GS users and orgs are sophisticated, locally rational, and the deficit narrative misreads them — apparent gaps live in extractive *terms* of incorporation, not in capability. Our F-8 (small-org N/S reversal) and F-12 (continent vanishes after size + tech_person) sit closer to the Avgerou/Nemer pole; our F-14 (translation gap) and the Sambasivan/Bender mechanism (C16, C17) recover a Heeks-flavored institutional gap on a *specific* axis (language, data infrastructure). The cleanest synthesis our data supports: **the access divide has flipped or vanished for consumer LLMs, but a Heeks-style adverse-incorporation gap persists on language fit, data infrastructure for analytical AI, and the institutional capacity required to escape "stochastic parrot" defaults.** The open empirical question — which Phase 5 analyses (LCA, IRT, Oaxaca–Blinder) should attempt to settle — is whether F-8's reversal is a genuine GS leapfrog or a measurement artifact in which "use" is being scored on tasks where consumer LLMs hide rather than close the institutional gap.
