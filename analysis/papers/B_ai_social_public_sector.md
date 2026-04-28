# Stream B — AI adoption in the social / public sector

Paper-cards for prior work on how nonprofits, NGOs, governments, and the broader social sector adopt AI — plus the critical "AI for good" / humanitarian-AI literature, the major industry AI-adoption surveys, and the "intent-action gap" tradition that underpins F-1 (Aspiration Inversion).

---

## B1 — Maslej et al. (2024), Stanford HAI AI Index 2024

```yaml
id: B1
stream: B
relevance_score: 5
peer_reviewed: no  # institute-published index, but rigorously vetted
year: 2024
tags: [HAI, AI Index, generative AI, adoption, benchmarks]
verified_url: yes
```

**Citation.** Maslej, N., Fattorini, L., Perrault, R., Parli, V., Reuel, A., Brynjolfsson, E., Etchemendy, J., Ligett, K., Lyons, T., Manyika, J., Niebles, J. C., Shoham, Y., Wald, R., & Clark, J. (2024). *The AI Index 2024 Annual Report*. Stanford Institute for Human-Centered Artificial Intelligence.

**DOI / URL.** https://arxiv.org/abs/2405.19522 · https://hai.stanford.edu/ai-index/2024-ai-index-report

**Sample / Method.** Annual cross-sector synthesis of AI metrics (research, performance, economy, education, policy). Adoption stats sourced from McKinsey, IBM, and Census Bureau panels.

**Key claim(s).**
- GenAI investment rose ~8× from 2022 to ~$25.2B in 2023.
- 55% of orgs use AI in at least one business unit (up from 50% in 2022, 20% in 2017).
- 42% of orgs report cost reductions, 59% revenue gains from AI.
- Adoption is concentrated in marketing/content/customer-service; analytical and forecasting uses lag.

**Takeaway for our dataset.** The HAI canonical baseline that adoption is "wide but content-heavy". Predicts our F-1 inversion shape — and lets us extend the claim from corporates to nonprofits (where it has not been published).

**Confirms / Complicates / Contradicts.** **Confirms** F-1 (content-heavy adoption today) and F-9 (skill/comprehension lags infrastructure). **Complicates** F-2 (HAI implies the content-heavy phase is *early*; F-2's Consumer-cluster surplus suggests it's already passing in heavy users).

---

## B2 — Salesforce.org (2024), *Nonprofit Trends Report, 6th Edition*

```yaml
id: B2
stream: B
relevance_score: 4
peer_reviewed: no  # vendor industry report
year: 2024
tags: [Salesforce, nonprofit, AI, intent-action gap]
verified_url: yes
```

**Citation.** Salesforce.org (2024). *Nonprofit Trends Report, 6th Edition*. Salesforce.

**DOI / URL.** https://www.salesforce.com/form/sfdo/ngo/6th-edition-nonprofit-trends-report/

**Sample / Method.** Global nonprofit survey, n≈1,600 respondents.

**Key claim(s).**
- Nonprofits are optimistic about AI but "many don't know where to begin".
- Staff are buried in routine admin tasks AI could absorb.
- Cautious interest: most see AI as transformative; far fewer have integrated.

**Takeaway for our dataset.** The canonical "aspiration gap" measurement for the nonprofit sector. Anchor for the F-1 headline.

**Confirms / Complicates / Contradicts.** **Confirms** F-1 (gap shape) and F-10 (Late Adopters' "don't know where to begin" matches the 52.8% "don't understand AI" finding).

---

## B3 — Boston Consulting Group (2024), *AI at Work 2024: Friend and Foe*

```yaml
id: B3
stream: B
relevance_score: 4
peer_reviewed: no  # consultancy report
year: 2024
tags: [BCG, comfort, frontline, GenAI, training]
verified_url: yes
```

**Citation.** Boston Consulting Group (2024). *AI at Work 2024: Friend and Foe*. BCG X.

**DOI / URL.** https://www.bcg.com/publications/2024/ai-at-work-friend-foe

**Sample / Method.** Global survey of 13,000+ employees in 15 countries.

**Key claim(s).**
- 42% of employees feel confident about AI's impact on work (up from 26% the prior year).
- 58% of GenAI users save ≥5 hours/week.
- Only 28–30% of frontline staff and managers have been trained on AI; 50% of leaders have.
- **Global South respondents (Brazil, India, Nigeria, South Africa, Middle East) report more optimism and less anxiety about GenAI than Global North peers.**

**Takeaway for our dataset.** The "GS less anxious about AI" finding directly mirrors our F-8 (small GS orgs use *more* AI than small GN peers).

**Confirms / Complicates / Contradicts.** **Confirms** F-3 (comfort grows with use) and F-8 (GS over-uses among small orgs). **Complicates** F-3's other direction: BCG implies vigilance and confidence both rise; we find risk-count rises and comfort rises but in opposite directions.

---

## B4 — Deloitte (2024), *State of Generative AI in the Enterprise — Q4 2024*

```yaml
id: B4
stream: B
relevance_score: 4
peer_reviewed: no  # consultancy report
year: 2024
tags: [Deloitte, governance, regulation, scaling]
verified_url: yes
```

**Citation.** Deloitte AI Institute (2024). *State of Generative AI in the Enterprise: Now decides next* (Q4 2024 edition). Deloitte.

**DOI / URL.** https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-generative-ai-in-enterprise.html

**Sample / Method.** Survey of 2,773 director- to C-suite respondents across 14 countries, 6 industries (incl. government & public services). Fielded July–September 2024.

**Key claim(s).**
- Regulation/risk is now the **top barrier** to GenAI deployment (up 10pp Q1→Q4, from 28% to 38%).
- ~75% report their most advanced GenAI initiative is meeting/exceeding ROI expectations.
- Only ~30% of pilots will be fully scaled in next 3–6 months.
- 78% expect to increase AI spending next FY; 26% are exploring agentic AI.

**Takeaway for our dataset.** Predicts that nonprofit governance scaffolding (data_use_policy, cloud_storage) should be a binding constraint. Our F-6 contradicts the simple version of this — policy *without* infrastructure adopts *less*, not more.

**Confirms / Complicates / Contradicts.** **Complicates** F-6 (Deloitte's enterprise governance-first thesis doesn't transfer to small nonprofits without ops infra).

---

## B5 — McKinsey (2024), *The state of AI in early 2024: Gen AI adoption spikes*

```yaml
id: B5
stream: B
relevance_score: 5
peer_reviewed: no  # industry survey
year: 2024
tags: [McKinsey, GenAI, 65 percent, value, marketing]
verified_url: yes
```

**Citation.** Singla, A., Sukharevsky, A., Yee, L., & Chui, M. (2024). *The state of AI in early 2024: Gen AI adoption spikes and starts to generate value*. McKinsey QuantumBlack.

**DOI / URL.** https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2024

**Sample / Method.** Online global survey, n=1,363 respondents, fielded Feb–Mar 2024.

**Key claim(s).**
- 65% of respondents report regular GenAI use — nearly double the prior wave.
- Overall AI adoption jumped from ~50% (held for 6 years) to 72%.
- Value concentrated in marketing/sales, product/service development, and IT/software engineering. Analytics and forecasting trail despite higher claimed ROI.
- 70% report difficulties with data (governance, integration, training data).

**Takeaway for our dataset.** Anchors the F-1 inversion: highest-value uses (analytics) are least adopted in the corporate world; we find the same shape in nonprofits, intensified.

**Confirms / Complicates / Contradicts.** **Confirms** F-1 (inversion). The McKinsey "rebalance is coming" interpretation contrasts with Madianou (B7) — see synthesis.

---

## B6 — Renieris, Kiron, & Mills (2023), MIT SMR / BCG — *Building Robust RAI Programs as Third-Party AI Tools Proliferate*

```yaml
id: B6
stream: B
relevance_score: 4
peer_reviewed: no  # MIT SMR / BCG industry research report
year: 2023
tags: [MIT SMR, BCG, third-party AI, responsible AI, vigilance]
verified_url: yes
```

**Citation.** Renieris, E. M., Kiron, D., & Mills, S. (2023). *Building Robust RAI Programs as Third-Party AI Tools Proliferate*. MIT Sloan Management Review and Boston Consulting Group.

**DOI / URL.** https://sloanreview.mit.edu/projects/building-robust-rai-programs-as-third-party-ai-tools-proliferate/

**Sample / Method.** Global executive survey, n=1,240 respondents from orgs with ≥$100M revenue, 59 industries, 87 countries. Spring 2023.

**Key claim(s).**
- 53% of orgs rely **exclusively** on third-party AI tools.
- 55% of all AI-related failures stem from third-party tools.
- Most orgs are not assessing or managing third-party AI risk; perception lags exposure.

**Takeaway for our dataset.** Predicts that nonprofits — almost all of whom *buy* AI rather than build it (consumer LLMs, off-the-shelf SaaS) — should systematically *under-perceive* the risk profile of their AI use.

**Confirms / Complicates / Contradicts.** **Contradicts** the simple "vigilance grows with use" reading: F-3 finds that hands-on use raises risk-count but subjective comfort *suppresses* it — consistent with B6's "perception lags exposure".

**Disagrees with.** B3 (BCG: confidence and use grow together).

---

## B7 — Madianou (2021), *Nonhuman humanitarianism: when 'AI for good' can be harmful*

```yaml
id: B7
stream: B
relevance_score: 5
peer_reviewed: yes
year: 2021
tags: [AI for good, humanitarianism, decolonial, critique, risk salience]
verified_url: yes
```

**Citation.** Madianou, M. (2021). Nonhuman humanitarianism: when 'AI for good' can be harmful. *Information, Communication & Society*, 24(6), 850–868.

**DOI / URL.** https://doi.org/10.1080/1369118X.2021.1909100

**Sample / Method.** Decolonial / critical-algorithm-studies analysis of humanitarian AI deployments (chatbots in refugee response).

**Key claim(s).**
- "AI for good" reproduces the coloniality of power: chatbots reduce communication to instrumental forms, extract value from displaced communities' data, and assert Eurocentric values.
- Structural risks (dependency, value extraction, experimentation) are systematically under-weighted relative to bias and privacy.

**Takeaway for our dataset.** A direct prior on our F-4: the discourse should over-weight bias/breaches and under-weight inequity/dependency. We confirm this and find the gap is *largest* among self-described "understand AI" respondents.

**Confirms / Complicates / Contradicts.** **Confirms** F-4 (risk salience asymmetry). **Disagrees with** B1/B5 (HAI/McKinsey treat current adoption shape as a transient early phase).

---

## B8 — Candid + GivingTuesday (2024), *Dollars and Change* / GivingPulse

```yaml
id: B8
stream: B
relevance_score: 3
peer_reviewed: no  # sector pulse report
year: 2024
tags: [Candid, GivingTuesday, charitable giving, US]
verified_url: yes
```

**Citation.** Candid, GivingTuesday, & Network for Good (2024). *Dollars and Change: A Decade of US Charitable Giving (2015–2022)*; GivingPulse Q2/Q3 2024 quarterly reports.

**DOI / URL.** https://candid.org/about/press-room/releases/candid-givingtuesday-and-network-for-good-unveil-dollars-and-change-report-key-trends-and-geographic-disparities-in-u.s.-charitable-giving · https://www.givingpulse.givingtuesday.org/

**Sample / Method.** Pooled administrative data + weekly pulse survey (US donors and nonprofits).

**Key claim(s).**
- Bimodal nonprofit landscape: a small "digital-native" tier vs a long tail of paper/Excel orgs.
- Donor base is shrinking but per-donor giving is rising — a top-heavy structure mirrors what we see in tech adoption (size dominance).

**Takeaway for our dataset.** Anchors the bimodality we observe in cluster3 and in our re-derived 3-cluster solution (F-18).

**Confirms / Complicates / Contradicts.** **Confirms** F-7 (size dominance) and F-18 (bimodal cluster shape).

---

## B9 — Maslej et al. (2025), Stanford HAI AI Index 2025

```yaml
id: B9
stream: B
relevance_score: 5
peer_reviewed: no  # institute-published index
year: 2025
tags: [HAI, AI Index, responsible AI, adoption]
verified_url: yes
```

**Citation.** Maslej, N., Fattorini, L., Perrault, R., Gil, Y., Parli, V., Kariuki, N., Capstick, E., Reuel, A., et al. (2025). *The AI Index 2025 Annual Report*. Stanford HAI.

**DOI / URL.** https://arxiv.org/abs/2504.07139 · https://hai.stanford.edu/ai-index/2025-ai-index-report

**Sample / Method.** 8th edition; new chapters on AI hardware, inference-cost estimates, responsible-AI corporate adoption, AI in science/medicine.

**Key claim(s).**
- Business is "all in" — record investment and usage continues, with research showing strong productivity impacts.
- US still leads model production; China is closing the performance gap.
- Adoption of responsible-AI practices remains uneven within firms.

**Takeaway for our dataset.** Confirms that the GenAI adoption wave is broadening, not narrowing, in 2025 — consistent with F-1's gap *not* closing (Consumer cluster is moving past Generate, but the long-tail Aspirational majority is still climbing it).

**Confirms / Complicates / Contradicts.** **Confirms** F-1, F-2 (the wavefront is moving, but unevenly). **Complicates** F-15: HAI shows risk-awareness rising in adopters at scale; our Skeptic cluster *under*-selects risks.

---

## B10 — Maslej et al. (2023), Stanford HAI AI Index 2023

```yaml
id: B10
stream: B
relevance_score: 4
peer_reviewed: no  # institute-published index
year: 2023
tags: [HAI, AI Index, ethics, public opinion]
verified_url: yes
```

**Citation.** Maslej, N., Fattorini, L., Brynjolfsson, E., Etchemendy, J., Ligett, K., Lyons, T., Manyika, J., Ngo, H., Niebles, J. C., Parli, V., Shoham, Y., Wald, R., Clark, J., & Perrault, R. (2023). *The AI Index 2023 Annual Report*. Stanford HAI.

**DOI / URL.** https://arxiv.org/abs/2310.03715 · https://hai.stanford.edu/ai-index/2023-ai-index-report

**Sample / Method.** 6th edition; new chapter on AI public opinion + technical performance + LLMs.

**Key claim(s).**
- AI ethics as a research field has grown 5× since 2014.
- Public opinion on AI is split sharply by region; optimism highest in Asia.
- Industrial AI investment is concentrating in fewer, larger players.

**Takeaway for our dataset.** Background on the public-opinion gradient that the BCG and our F-8 findings echo.

**Confirms / Complicates / Contradicts.** **Confirms** F-8 (regional optimism gradient corroborates the small-GS-leads finding).

---

## B11 — Zhang et al. (2022), Stanford HAI AI Index 2022

```yaml
id: B11
stream: B
relevance_score: 3
peer_reviewed: no  # institute-published index
year: 2022
tags: [HAI, AI Index, industrialization, ethics]
verified_url: yes
```

**Citation.** Zhang, D., Maslej, N., Brynjolfsson, E., Etchemendy, J., Lyons, T., Manyika, J., Ngo, H., Niebles, J. C., Sellitto, M., Sakhaee, E., Shoham, Y., Clark, J., & Perrault, R. (2022). *The AI Index 2022 Annual Report*. Stanford HAI.

**DOI / URL.** https://hai.stanford.edu/ai-index/2022-ai-index-report

**Sample / Method.** Cross-sector synthesis. Investment + research + ethics tracking.

**Key claim(s).**
- Private AI investment more than doubled 2020→2021.
- Cost of training image classification dropped 63.6% since 2018.
- Algorithmic-fairness research now a mainstream subfield (5× growth at ethics-conferences).

**Takeaway for our dataset.** Cost-curve context for why consumer LLMs are now within reach of small nonprofits — the precondition for F-8 (small GS orgs adopting via consumer tools).

**Confirms / Complicates / Contradicts.** Background.

---

## B12 — Zhang et al. (2021), Stanford HAI AI Index 2021

```yaml
id: B12
stream: B
relevance_score: 3
peer_reviewed: no  # institute-published index
year: 2021
tags: [HAI, AI Index, sector adoption, baseline]
verified_url: yes
```

**Citation.** Zhang, D., Mishra, S., Brynjolfsson, E., Etchemendy, J., Ganguli, D., Grosz, B., Lyons, T., Manyika, J., Niebles, J. C., Sellitto, M., Shoham, Y., Clark, J., & Perrault, R. (2021). *The AI Index 2021 Annual Report*. Stanford HAI.

**DOI / URL.** https://arxiv.org/abs/2103.06312 · https://hai.stanford.edu/ai-index-2021

**Sample / Method.** 4th edition; first post-COVID baseline.

**Key claim(s).**
- Top-3 industries for adoption in 2020: high-tech/telecom, automotive, financial services. Civil-society/nonprofit not in the top tier.
- Brynjolfsson: "2020 was a year when AI accelerated its move from the lab to commercial and industrial applications."

**Takeaway for our dataset.** Establishes the late entry of the social sector relative to commercial sectors — context for why our 2024 nonprofit baseline still leans on Generate.

**Confirms / Complicates / Contradicts.** Background; situates F-1 historically.

---

## B13 — McKinsey (2025), *The state of AI: How organizations are rewiring to capture value*

```yaml
id: B13
stream: B
relevance_score: 4
peer_reviewed: no  # industry survey
year: 2025
tags: [McKinsey, workflow redesign, scaling, EBIT impact]
verified_url: yes
```

**Citation.** Singla, A., Sukharevsky, A., Yee, L., & Chui, M. (2025). *The state of AI: How organizations are rewiring to capture value*. McKinsey QuantumBlack.

**DOI / URL.** https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value

**Sample / Method.** Global survey, ~1,500 organizations across 100+ countries, fielded early 2025.

**Key claim(s).**
- 78% of orgs use AI in ≥1 business function (up from 72% in 2024, 55% the year before). 71% regularly use GenAI.
- Of 25 attributes tested, **redesign of workflows** has the biggest effect on whether GenAI produces EBIT impact.
- Just 39% report enterprise-level EBIT impact — the gap between use and value persists.
- CEO oversight of AI governance correlates with bottom-line impact.

**Takeaway for our dataset.** The McKinsey 2025 narrative shifts blame from tech to *organizational rewiring* — directly resonant with our F-9 / F-10 (the bottleneck is comprehension and integration, not infrastructure).

**Confirms / Complicates / Contradicts.** **Confirms** F-9 (the comfort × infra interaction implies workflow redesign is a binding factor) and F-10 (capacity-building is comprehension-shaped, not tech-shaped).

---

## B14 — Stanford HAI & Project Evident (2024), *Inspiring Action: Identifying the Social Sector AI Opportunity Gap*

```yaml
id: B14
stream: B
relevance_score: 5
peer_reviewed: no  # institute working paper
year: 2024
tags: [Stanford HAI, Project Evident, social sector, AI opportunity gap, nonprofit survey]
verified_url: yes
```

**Citation.** Stanford HAI & Project Evident (2024). *Inspiring Action: Identifying the Social Sector AI Opportunity Gap*. Stanford Institute for Human-Centered AI.

**DOI / URL.** https://projectevident.org/wp-content/uploads/2024/02/Inspiring-Action-HAIPE-AI-report.pdf · https://hai.stanford.edu/news/bridging-opportunity-gap-social-sector-ai

**Sample / Method.** First-of-its-kind survey of US social-sector orgs, n=230+, late 2023.

**Key claim(s).**
- ~50% of nonprofit respondents already use AI tools — mostly for back-office (HR, finance, marketing).
- **76% believe their organization would benefit from more AI** — almost identical in shape to our 41pp Predict gap.
- Top concern: **bias** (#1), then cost, then "lack of clarity about how AI will help".
- Most grantmakers do not have a tech-grantmaking priority and don't plan to create one.

**Takeaway for our dataset.** This is the closest direct prior on our exact research question. The shape ("use for ops, want for mission") and the "lack of clarity" finding map almost 1:1 onto our F-1 / F-10.

**Confirms / Complicates / Contradicts.** **Confirms** F-1, F-10 (lack-of-clarity bottleneck), F-4 (bias as headline risk), F-15 (the "AI Skeptic" framing is misleading; orgs are mostly aspirational, not opposed).

---

## B15 — Wirtz, Weyerer, & Geyer (2019)

```yaml
id: B15
stream: B
relevance_score: 4
peer_reviewed: yes
year: 2019
tags: [public sector, AI, governance, framework]
verified_url: yes
```

**Citation.** Wirtz, B. W., Weyerer, J. C., & Geyer, C. (2019). Artificial Intelligence and the public sector—applications and challenges. *International Journal of Public Administration*, 42(7), 596–615.

**DOI / URL.** https://doi.org/10.1080/01900692.2018.1498103

**Sample / Method.** Conceptual literature synthesis identifying 10 AI application areas in public administration.

**Key claim(s).**
- Four binding barriers to public-sector AI: safety concerns, poor data quality/integration, financial constraints/lack of expertise, and organizational resistance / legacy infrastructure.
- AI applications in public sector cluster into 10 functional categories.

**Takeaway for our dataset.** The four-barrier frame predicts the same constraints we see in nonprofits — but our F-9 / F-10 reweight them: comprehension and comfort outrank both data quality and finance once size is held constant.

**Confirms / Complicates / Contradicts.** **Complicates** F-9 (Wirtz's framework lists data quality as primary; our 2×2 shows comfort matters at least as much).

---

## B16 — Wirtz, Weyerer, & Sturm (2020)

```yaml
id: B16
stream: B
relevance_score: 4
peer_reviewed: yes
year: 2020
tags: [AI governance, dark sides, public administration, risk]
verified_url: yes
```

**Citation.** Wirtz, B. W., Weyerer, J. C., & Sturm, B. J. (2020). The dark sides of artificial intelligence: an integrated AI governance framework for public administration. *International Journal of Public Administration*, 43(9), 818–829.

**DOI / URL.** https://doi.org/10.1080/01900692.2020.1749851

**Sample / Method.** Conceptual integrative framework for AI governance in public administration.

**Key claim(s).**
- AI's "dark sides" (bias, opacity, accountability gaps, surveillance) are systematically under-governed.
- Calls for an integrated regulatory architecture combining legal, ethical, technical, and societal dimensions.

**Takeaway for our dataset.** Anchors the Madianou-aligned argument: structural risks deserve more weight than the public discourse gives them. F-4 confirms the asymmetry in nonprofit risk salience.

**Confirms / Complicates / Contradicts.** **Confirms** F-4 / B7 (Madianou) on under-weighting of structural risks.

---

## B17 — Sun & Medaglia (2019)

```yaml
id: B17
stream: B
relevance_score: 4
peer_reviewed: yes
year: 2019
tags: [public sector, AI, healthcare, IBM Watson, China, stakeholders]
verified_url: yes
```

**Citation.** Sun, T. Q., & Medaglia, R. (2019). Mapping the challenges of Artificial Intelligence in the public sector: evidence from public healthcare. *Government Information Quarterly*, 36(2), 368–383.

**DOI / URL.** https://doi.org/10.1016/j.giq.2018.09.008

**Sample / Method.** Case study of IBM Watson adoption in Chinese public healthcare; three stakeholder groups (policymakers, hospital managers/doctors, IT firm managers).

**Key claim(s).**
- Stakeholders frame AI challenges in contradictory ways — what matters depends on role.
- Successful adoption requires more than data, compute, and algorithms: governance, human factors, and inter-organizational coordination dominate.

**Takeaway for our dataset.** Predicts that within a single nonprofit, leaders, MERL staff, and frontline workers should perceive AI risks differently — testable against our `merl_person`/`tech_person`/`leader_role` fields.

**Confirms / Complicates / Contradicts.** **Confirms** F-3 / F-15 (heterogeneous risk framings within orgs).

---

## B18 — Mehr (2017), Harvard Ash Center

```yaml
id: B18
stream: B
relevance_score: 3
peer_reviewed: no  # policy report
year: 2017
tags: [Harvard Ash, citizen services, AI government, early-wave]
verified_url: yes
```

**Citation.** Mehr, H. (2017). *Artificial Intelligence for Citizen Services and Government*. Ash Center for Democratic Governance and Innovation, Harvard Kennedy School.

**DOI / URL.** https://ash.harvard.edu/wp-content/uploads/2024/02/artificial_intelligence_for_citizen_services.pdf

**Sample / Method.** Policy review + practitioner interviews.

**Key claim(s).**
- AI in citizen services should *augment* (not replace) workers.
- Best practice for reducing bias: multidisciplinary teams + ethicists involved at all stages.
- Citizens must be able to trust the systems and know where their data flows.

**Takeaway for our dataset.** Pre-GenAI baseline framing — useful as a "pre-2022 promised land" comparator for the post-ChatGPT shape we observe.

**Confirms / Complicates / Contradicts.** Background.

---

## B19 — Margetts & Dorobantu (2019), *Nature*

```yaml
id: B19
stream: B
relevance_score: 4
peer_reviewed: yes
year: 2019
tags: [AI government, data, public services, policy]
verified_url: yes
```

**Citation.** Margetts, H., & Dorobantu, C. (2019). Rethink government with AI. *Nature*, 568(7751), 163–165.

**DOI / URL.** https://doi.org/10.1038/d41586-019-01099-5

**Sample / Method.** Policy commentary in *Nature*.

**Key claim(s).**
- Governments should harness data to deliver public services that are responsive, efficient, *and* fair.
- Argues for shifting AI in government from automation to data-informed policy design.

**Takeaway for our dataset.** Frames the Predict/Organize gap (F-1) as a call to action: orgs *want* to do exactly the data-informed work Margetts & Dorobantu prescribe.

**Confirms / Complicates / Contradicts.** **Confirms** F-1 normatively.

---

## B20 — Eubanks (2018), *Automating Inequality*

```yaml
id: B20
stream: B
relevance_score: 4
peer_reviewed: yes  # academic monograph
year: 2018
tags: [algorithmic accountability, public services, inequality, ethnography]
verified_url: yes
```

**Citation.** Eubanks, V. (2018). *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor*. New York: St. Martin's Press.

**DOI / URL.** ISBN 978-1250074317 · https://us.macmillan.com/books/9781250074317/automatinginequality/

**Sample / Method.** Three ethnographic case studies (Indiana welfare automation, LA homelessness vulnerability index, Pittsburgh child-welfare predictive model).

**Key claim(s).**
- Automated decision systems deployed in public services often *amplify* inequality by encoding administrative violence at scale.
- The poor and vulnerable are subjected to disproportionate algorithmic surveillance.
- Digital tools hide poverty from the middle class, enabling inhumane policy.

**Takeaway for our dataset.** Direct prior on the structural-risk pole of F-4: when the same nonprofits start adopting predictive AI (the high-`[W]` use cases — Predict, Organize, Assist), the inequity/dependency risks Eubanks documents become live.

**Confirms / Complicates / Contradicts.** **Confirms** F-4 normatively; sharpens the Madianou argument with US public-services case data.

---

## B21 — Mohamed, Png, & Isaac (2020), *Decolonial AI*

```yaml
id: B21
stream: B
relevance_score: 4
peer_reviewed: yes
year: 2020
tags: [decolonial, AI for good, critique, Global South]
verified_url: yes
```

**Citation.** Mohamed, S., Png, M.-T., & Isaac, W. (2020). Decolonial AI: decolonial theory as sociotechnical foresight in artificial intelligence. *Philosophy & Technology*, 33(4), 659–684.

**DOI / URL.** https://doi.org/10.1007/s13347-020-00405-8 · https://arxiv.org/abs/2007.04068

**Sample / Method.** Conceptual / theoretical framework drawing on decolonial studies.

**Key claim(s).**
- AI development reproduces colonial relations of power: dependency, dispossession, ethics dumping, "predatory inclusion".
- "AI for social good" can be a vehicle for these dynamics if naively framed.
- Three tactics for decolonial AI: critical technical practice, reverse pedagogies, renewed political community.

**Takeaway for our dataset.** Anchors the Madianou critique with a more programmatic framework. Predicts F-8: the GS-leads-among-small-orgs result is *not* leapfrogging but a new dependency on consumer-LLM ecosystems built in the GN.

**Confirms / Complicates / Contradicts.** **Complicates** F-8: the surface "GS catching up" pattern may be a deeper dependency, not progress.

---

## B22 — Floridi et al. (2018), *AI4People — An ethical framework for a good AI society*

```yaml
id: B22
stream: B
relevance_score: 4
peer_reviewed: yes
year: 2018
tags: [AI ethics, framework, principles, social good]
verified_url: yes
```

**Citation.** Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Chazerand, P., Dignum, V., Luetge, C., Madelin, R., Pagallo, U., Rossi, F., Schafer, B., Valcke, P., & Vayena, E. (2018). AI4People — an ethical framework for a good AI society: opportunities, risks, principles, and recommendations. *Minds and Machines*, 28(4), 689–707.

**DOI / URL.** https://doi.org/10.1007/s11023-018-9482-5

**Sample / Method.** Ethical framework synthesis (AI4People expert forum).

**Key claim(s).**
- Five-principle frame: beneficence, nonmaleficence, justice, autonomy, explicability.
- Four kinds of social benefit: enabling self-realization, enhancing agency, increasing societal capability, cultivating cohesion — each with a corresponding risk.

**Takeaway for our dataset.** Provides the canonical principle vocabulary against which our F-4 risk-salience asymmetry can be diagnosed.

**Confirms / Complicates / Contradicts.** Framework only.

---

## B23 — Tomašev et al. (2020), *AI for social good: unlocking the opportunity for positive impact*

```yaml
id: B23
stream: B
relevance_score: 3
peer_reviewed: yes
year: 2020
tags: [AI for good, SDGs, partnerships, optimistic]
verified_url: yes
```

**Citation.** Tomašev, N., Cornebise, J., Hutter, F., Mohamed, S., Picciariello, A., Connelly, B., Belgrave, D., Ezer, D., van der Haert, F. C., Mugisha, F., Abila, G., Arai, H., Almiraat, H., Proskurnia, J., Snyder, K., Otake-Matsuura, M., Othman, M., Glasmachers, T., de Wever, W., Teh, Y. W., Khan, M. E., De Winne, R., Schaul, T., & Clopath, C. (2020). AI for social good: unlocking the opportunity for positive impact. *Nature Communications*, 11, 2468.

**DOI / URL.** https://doi.org/10.1038/s41467-020-15871-z

**Sample / Method.** Multi-author position paper from AI4SG community.

**Key claim(s).**
- AI4SG should align with the UN SDGs.
- Long-term partnerships between AI researchers and domain experts are the binding precondition.
- Provides operational guidelines for productive AI4SG collaborations.

**Takeaway for our dataset.** Optimistic counter-pole to Madianou (B7) and Mohamed et al. (B21). Provides the partnership-architecture frame for `collab_feasibility`.

**Confirms / Complicates / Contradicts.** **Confirms** the prior that `collab_feasibility` should correlate with use; **disagrees with** B7, B21 in tone.

**Disagrees with.** B7 (Madianou), B21 (Mohamed et al.).

---

## B24 — Bondi, Xu, Acosta-Navas, & Killian (2021), *Envisioning Communities*

```yaml
id: B24
stream: B
relevance_score: 3
peer_reviewed: yes
year: 2021
tags: [participatory, AI for good, capabilities approach, AIES]
verified_url: yes
```

**Citation.** Bondi, E., Xu, L., Acosta-Navas, D., & Killian, J. A. (2021). Envisioning communities: a participatory approach towards AI for social good. In *Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society* (AIES '21), pp. 425–436.

**DOI / URL.** https://doi.org/10.1145/3461702.3462612 · https://arxiv.org/abs/2105.01774

**Sample / Method.** Conceptual / participatory-design framework drawing on Sen/Nussbaum's capabilities approach.

**Key claim(s).**
- AI4SG presupposes a definition of "social good" that is rarely elaborated and often utilitarian.
- Argues that the impacted community should assess whether an AI system delivers good — using the capabilities approach as the metric.

**Takeaway for our dataset.** Frames why `collab_feasibility` and `non_data_work` matter: who *gets to define* whether nonprofit AI is "working".

**Confirms / Complicates / Contradicts.** Framework only.

---

## B25 — Berendt (2019), *AI for the Common Good?!*

```yaml
id: B25
stream: B
relevance_score: 3
peer_reviewed: yes
year: 2019
tags: [AI ethics, common good, pen-testing, critique]
verified_url: yes
```

**Citation.** Berendt, B. (2019). AI for the Common Good?! Pitfalls, challenges, and ethics pen-testing. *Paladyn, Journal of Behavioral Robotics*, 10(1), 44–65.

**DOI / URL.** https://doi.org/10.1515/pjbr-2019-0004 · https://arxiv.org/abs/1810.12847

**Sample / Method.** Critical / conceptual analysis.

**Key claim(s).**
- "Common Good" in AI is rarely operationalized; "good intent" is not enough.
- Proposes "ethics pen-testing" — adversarial probing of who defines the problem and who benefits.
- Four lead questions: What is the problem? Who defines it? What is the role of knowledge? What are side effects?

**Takeaway for our dataset.** Methodological prior on why the gap between `[U]` and `[W]` matters: aspiration is not a proxy for benefit.

**Confirms / Complicates / Contradicts.** Framework only; informs how F-1 should be interpreted (aspiration ≠ alignment with mission).

---

## B26 — Mikalef, Fjørtoft, & Torvatn (2019)

```yaml
id: B26
stream: B
relevance_score: 3
peer_reviewed: yes
year: 2019
tags: [public sector, Norway, municipalities, AI adoption survey]
verified_url: yes
```

**Citation.** Mikalef, P., Fjørtoft, S. O., & Torvatn, H. Y. (2019). Artificial Intelligence in the public sector: a study of challenges and opportunities for Norwegian municipalities. In *Digital Transformation for a Sustainable Society in the 21st Century* (I3E 2019), Lecture Notes in Computer Science, vol. 11701, pp. 267–277. Springer.

**DOI / URL.** https://doi.org/10.1007/978-3-030-29374-1_22

**Sample / Method.** Survey of IT-management leads in Norwegian municipalities.

**Key claim(s).**
- Aspirations for AI in municipalities greatly outpace current implementation.
- Top barriers: skill shortages, fragmented data infrastructure, regulatory uncertainty.
- The smaller the municipality, the larger the want-have gap.

**Takeaway for our dataset.** A direct public-sector analogue to F-1 (aspiration inversion) and F-7 (size dominance) — in a Northern European context.

**Confirms / Complicates / Contradicts.** **Confirms** F-1, F-7.

---

## B27 — Toll, Lindgren, Melin, & Madsen (2020)

```yaml
id: B27
stream: B
relevance_score: 3
peer_reviewed: yes
year: 2020
tags: [public sector, Sweden, AI policy, values]
verified_url: yes
```

**Citation.** Toll, D., Lindgren, I., Melin, U., & Madsen, C. Ø. (2020). Values, benefits, considerations and risks of AI in government: a study of AI policies in Sweden. *JeDEM — eJournal of eDemocracy and Open Government*, 12(1), 40–60.

**DOI / URL.** https://doi.org/10.29379/jedem.v12i1.593

**Sample / Method.** Discourse analysis of Swedish AI policy documents using an established e-government value framework.

**Key claim(s).**
- AI is overwhelmingly framed in terms of **efficiency** and service quality; equity, deliberation, and rights are under-emphasized.
- Discrepancies between value-ideals expressed across policy levels.

**Takeaway for our dataset.** Predicts our F-4: official discourse over-weights efficiency-aligned risks (bias, breaches) and under-weights structural ones (inequity, dependency).

**Confirms / Complicates / Contradicts.** **Confirms** F-4.

---

## B28 — Bhattacherjee & Sanford (2009) — intent-action gap canonical

```yaml
id: B28
stream: B
relevance_score: 4
peer_reviewed: yes
year: 2009
tags: [intent-action gap, IS adoption, attitude strength, behavioral intention]
verified_url: yes
```

**Citation.** Bhattacherjee, A., & Sanford, C. (2009). The intention–behaviour gap in technology usage: the moderating role of attitude strength. *Behaviour & Information Technology*, 28(4), 389–401.

**DOI / URL.** https://doi.org/10.1080/01449290802121230

**Sample / Method.** Longitudinal field survey of document-management-system usage; tests moderating role of attitude strength.

**Key claim(s).**
- Intention-behavior gap is real and widespread in IS adoption — many form intentions; few translate into action.
- Personal relevance and related expertise moderate the gap.

**Takeaway for our dataset.** Theoretical anchor for the F-1 inversion: it is *the* intent-action gap shape, with the want side being intention and the use side being action. Predicts that `person_ai_comfort` (a relevance/expertise proxy) should narrow the gap — which F-9 / F-20 confirm (ρ=+0.50 with use).

**Confirms / Complicates / Contradicts.** **Confirms** F-1, F-9, F-20 — the gap is well-described by the canonical IS-adoption gap mechanism.

---

## B29 — Eggers, Schatsky, & Viechnicki (2017), Deloitte

```yaml
id: B29
stream: B
relevance_score: 2
peer_reviewed: no  # consultancy report
year: 2017
tags: [Deloitte, AI government, augmentation, early-wave]
verified_url: unable
```

**Citation.** Eggers, W. D., Schatsky, D., & Viechnicki, P. (2017). *AI-augmented government: using cognitive technologies to redesign public sector work*. Deloitte Center for Government Insights.

**DOI / URL.** Cited in academic literature; primary URL not directly retrievable in current Deloitte archive — set `verified_url: unable`.

**Sample / Method.** Policy/practitioner synthesis.

**Key claim(s).**
- AI's earliest big public-sector wins are routine cognitive automation (forms processing, fraud screening) — not strategic decision making.
- "Augmentation" framing predates current GenAI hype.

**Takeaway for our dataset.** Pre-GenAI baseline; predicts our F-1 finding that the earliest wins are routine (Generate, Translate) rather than strategic (Predict, Organize).

**Confirms / Complicates / Contradicts.** **Confirms** F-1 historically.

---

## B30 — Beduschi (2021), *International migration management in the age of AI*

```yaml
id: B30
stream: B
relevance_score: 3
peer_reviewed: yes
year: 2021
tags: [AI ethics, migration, humanitarian, risk]
verified_url: yes
```

**Citation.** Beduschi, A. (2021). International migration management in the age of artificial intelligence. *Migration Studies*, 9(3), 576–596.

**DOI / URL.** https://doi.org/10.1093/migration/mnaa003

**Sample / Method.** Legal/policy analysis.

**Key claim(s).**
- AI in migration management produces specific structural harms — misidentification, refoulement risk, accountability gaps.
- The "do no harm" imperative requires algorithmic accountability frameworks aligned with international human rights law.

**Takeaway for our dataset.** Sharpens the structural-risk pole (F-4 / B7). Predicts that NGOs working on migration/refugee response (a non-trivial cause-area in our `org_label`) should be most attuned to inequity/dependency risks — testable.

**Confirms / Complicates / Contradicts.** Background; informs F-19 (cause-area analysis).

---

## B31 — Whittlestone, Nyrup, Alexandrova, Dihal, & Cave (2019), Nuffield Foundation

```yaml
id: B31
stream: B
relevance_score: 3
peer_reviewed: no  # commissioned policy report (yes-or-no on peer review is borderline; Nuffield report)
year: 2019
tags: [AI ethics, research roadmap, tensions, principles]
verified_url: yes
```

**Citation.** Whittlestone, J., Nyrup, R., Alexandrova, A., Dihal, K., & Cave, S. (2019). *Ethical and Societal Implications of Algorithms, Data, and Artificial Intelligence: A Roadmap for Research*. Nuffield Foundation.

**DOI / URL.** https://www.nuffieldfoundation.org/sites/default/files/files/Ethical-and-Societal-Implications-of-Data-and-AI-report-Nuffield-Foundat.pdf

**Sample / Method.** Literature review + stakeholder workshops; commissioned to inform the Ada Lovelace Institute.

**Key claim(s).**
- Ethics in AI should foreground *tensions* between principles (e.g., accuracy vs fairness, privacy vs transparency), not just principles themselves.
- Calls for context-specific empirical research — exactly the type of data we have.

**Takeaway for our dataset.** Frames why F-4's bias/breaches > inequity/dependency asymmetry is not just an empirical curiosity but a substantive ethical problem.

**Confirms / Complicates / Contradicts.** Framework only.

---

## Stream B synthesis

The Stream B literature converges on three things and disagrees sharply on one. **Consensus (1): the intent-action gap is real and large** — McKinsey 2024/2025 (B5, B13), Salesforce 2024 (B2), Stanford HAI/Project Evident 2024 (B14), Mikalef et al. 2019 (B26), and Bhattacherjee & Sanford 2009 (B28) all measure intention-to-use ratios in the same neighborhood (~3–4× the action ratio), and our F-1 sits squarely in that distribution. **Consensus (2): governance and comprehension, not infrastructure, are the binding constraints at the firm level** — Deloitte Q4 2024 (B4), McKinsey 2025 (B13), Wirtz et al. 2019/2020 (B15, B16), Sun & Medaglia 2019 (B17), and the HAI/Project Evident 2024 nonprofit survey (B14) each independently move the bottleneck off "tech stack" and onto "rewiring" or "comprehension". F-9 and F-10 corroborate exactly this. **Consensus (3): the discourse on AI risk over-weights bias and breaches and under-weights structural risks** (inequity, dependency, value-extraction) — Madianou 2021 (B7), Mohamed/Png/Isaac 2020 (B21), Wirtz/Weyerer/Sturm 2020 (B16), Eubanks 2018 (B20), Toll et al. 2020 (B27), Whittlestone et al. 2019 (B31). F-4 confirms with a 19pp asymmetry that *widens* among self-described "understanders".

The big **open debate** is whether the GenAI-skewed adoption shape (Generate >> Predict/Organize) is a transient early-adoption phase that will rebalance — the **Stanford HAI / McKinsey** position (B1, B5, B9, B13) — or a structural feature of "AI for good" frozen in by funder expectations and consumer-LLM availability — the **Madianou / Mohamed et al. / Berendt / Bondi et al.** position (B7, B21, B25, B24). Our findings adjudicate partially: **F-2 supports the rebalance hypothesis** (heavy Consumer users have moved past Generate into negative gap territory on content tasks), **but F-1 / F-10 / F-14 support the structural hypothesis at the long-tail end** (Aspirational and Late-Adopter clusters are still climbing the same Generate-first ladder, and translation demand stays asymmetrically GS-loaded). The most likely synthesis: **the rebalance is happening at the top of the distribution and stalling at the bottom**, which is precisely the bimodal "willing but not wired" shape F-18 surfaces. This is the contribution our dataset makes that no Stream B paper can claim: a global, nonprofit-specific N=930 measurement of *both ends* of the intent-action gap simultaneously.
