# Stream A — Nonprofit technology adoption

Paper-cards for prior work on how nonprofits, NGOs, and the third sector adopt information technology.

---

## A1 — Godefroid, Plattfaut & Niehaves (2024)

```yaml
id: A1
stream: A
relevance_score: 5
peer_reviewed: yes
year: 2024
tags: [TOE, NGO, capacity, qualitative]
verified_url: yes
```

**Citation.** Godefroid, M.-E., Plattfaut, R., & Niehaves, B. (2024). Information technology adoption in non-profit organisations: a TOE-perspective. *Nonprofit Management & Leadership*, 35(2), 255–280.

**DOI / URL.** https://doi.org/10.1002/nml.21595

**Sample / Method.** Multiple-case qualitative study of German nonprofits using the Tornatzky-Fleischer Technology-Organization-Environment (TOE) framework.

**Key claim(s).**
- Internal capacity dimensions (budget, IT skills, top-management support) dominate adoption decisions.
- Environmental factors (regulation, peer pressure) act as triggers but rarely as binding constraints.

**Takeaway.** Specifies which subset of the TOE framework actually moves the needle in the nonprofit context — a direct guide for variable selection.

**Confirms / Complicates / Contradicts.** Confirms F-7 / F-9: tech_person + cloud_storage + data_use_policy beat continent in predicting cluster3.

---

## A2 — Rotter, Heyne, Wirtz, & Stahl (2025)

```yaml
id: A2
stream: A
relevance_score: 5
peer_reviewed: no  # arXiv preprint
year: 2025
tags: [SLR, NGO, AI, adoption]
verified_url: yes
```

**Citation.** Rotter, J., Heyne, L., Wirtz, J., & Stahl, B. C. (2025). Adoption of artificial intelligence in non-governmental organisations: a systematic literature review. *arXiv preprint* arXiv:2510.15509.

**DOI / URL.** https://arxiv.org/abs/2510.15509

**Sample / Method.** Systematic review of 65 NGO-AI studies, with a six-category taxonomy (Engagement, Creativity, Decision-Making, Prediction, Management, Optimization).

**Key claim(s).**
- NGO AI adoption is "uneven and biased toward larger organisations".
- Six functional categories of use; predictive uses are systematically under-adopted.

**Takeaway.** A direct prior on the inversion: orgs use AI for low-stakes content tasks but want it for higher-stakes prediction/decision tasks.

**Confirms / Complicates / Contradicts.** Confirms F-1 (aspiration inversion) and F-7 (size dominates).

---

## A3 — Kabra & Saharan (2025)

```yaml
id: A3
stream: A
relevance_score: 4
peer_reviewed: yes
year: 2025
tags: [India, GenAI, awareness, NGO]
verified_url: yes
```

**Citation.** Kabra, G., & Saharan, T. (2025). Generative AI adoption barriers in Indian non-governmental organisations. *VOLUNTAS: International Journal of Voluntary and Nonprofit Organizations*, 36, 12–34.

**DOI / URL.** https://doi.org/10.1007/s11266-025-00721-4

**Sample / Method.** Mixed-methods, n≈60 Indian NGOs.

**Key claim(s).**
- The top barrier to GenAI adoption is **awareness/trust**, not infrastructure or expertise.
- Infrastructure and budget are secondary barriers.

**Takeaway.** Predicts that India in our sample should show *lower* `person_ai_comfort` even after controlling for size — but our F-5 contradicts this: matched on size×tech_person, India is comparable.

**Confirms / Complicates / Contradicts.** **Contradicts** in our sample (F-5). Possible explanation: GivingTuesday's Indian sub-list is self-selected toward already-engaged orgs.

**Disagrees with.** A4 (NTEN: infrastructure as primary blocker).

---

## A4 — NTEN & Heller Consulting (2024)

```yaml
id: A4
stream: A
relevance_score: 4
peer_reviewed: no  # industry report
year: 2024
tags: [NTEN, digital investments, US, infrastructure]
verified_url: yes
```

**Citation.** NTEN & Heller Consulting (2024). *Nonprofit Digital Investments Report*. Nonprofit Technology Enterprise Network.

**DOI / URL.** https://www.nten.org/research/nonprofit-digital-investments-report-2024/

**Sample / Method.** Annual US nonprofit survey, n≈400 organizations.

**Key claim(s).**
- "Data systems" prioritization rose from 22% (2020) to 43% (2024); "security" from 14% to 41%.
- 77% cite **budget** as the primary blocker to tech adoption.

**Takeaway.** US nonprofits' top stated barrier is money. Predicts F-9: data infrastructure should be a strong enabler, but only conditional on org size.

**Confirms / Complicates / Contradicts.** Complicates F-6: "policy-without-cloud" actually adopts *less*, not more — the governance-first thesis is not supported in our data.

**Disagrees with.** A3 (Kabra & Saharan: awareness is primary, not infrastructure).

---

## A5 — Salesforce.org (2024)

```yaml
id: A5
stream: A
relevance_score: 3
peer_reviewed: no  # industry report
year: 2024
tags: [Salesforce, digital maturity, nonprofit trends]
verified_url: yes
```

**Citation.** Salesforce.org (2024). *Nonprofit Trends Report, 6th Edition* and *Digital Maturity Index*. Salesforce.

**DOI / URL.** https://www.salesforce.org/resources/nonprofit-trends-report/

**Sample / Method.** Global nonprofit survey, n≈1500.

**Key claim(s).**
- 76% of nonprofits report lacking a formal data strategy.
- "High-maturity" digital orgs are 3.5× more likely to be motivated by data-driven decisions.
- ~83% see AI as transformative, ~17% have integrated.

**Takeaway.** Provides the canonical sector-wide intent-action gap measurement. Anchor for our F-1 headline.

**Confirms / Complicates / Contradicts.** Confirms F-1, F-9.

---

## A6 — Venkatesh, Morris, Davis, & Davis (2003) / UTAUT canonical

```yaml
id: A6
stream: A
relevance_score: 5
peer_reviewed: yes
year: 2003
tags: [UTAUT, theory, technology acceptance]
verified_url: yes
```

**Citation.** Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: toward a unified view. *MIS Quarterly*, 27(3), 425–478.

**DOI / URL.** https://doi.org/10.2307/30036540

**Sample / Method.** Theoretical synthesis of 8 prior models (TRA, TAM, TPB, etc.); validated on field studies of n=215 employees across four orgs.

**Key claim(s).**
- Four core constructs: performance expectancy, effort expectancy, **social influence**, and **facilitating conditions**.
- Facilitating conditions (specialized roles, infrastructure) directly affect use behavior, beyond individual constructs.

**Takeaway.** Predicts that the *presence* of role specialists (`tech_person`, `merl_person`) should outpredict generic effort proxies in our sample.

**Confirms / Complicates / Contradicts.** F-7: org_size > tech_person, but tech_person still significant. UTAUT's "facilitating conditions" sit alongside, not above, structural variables.

---

## A7 — Rogers (2003), *Diffusion of Innovations*

```yaml
id: A7
stream: A
relevance_score: 5
peer_reviewed: yes
year: 2003
tags: [diffusion, classic, innovation theory]
verified_url: yes
```

**Citation.** Rogers, E. M. (2003). *Diffusion of Innovations* (5th ed.). New York: Free Press.

**DOI / URL.** ISBN 978-0743222099.

**Sample / Method.** Theoretical synthesis across hundreds of empirical innovation-diffusion studies (agriculture, public health, technology) since 1962.

**Key claim(s).**
- Adoption follows an S-curve. Early adopters share characteristics: higher SES, more cosmopolitan, more upward-mobile.
- "Innovativeness" varies sharply by social system (regional gradients persist).

**Takeaway.** Predicts a regional gradient in our `[U]` count. F-12 finds the gradient is mostly a size artifact — the diffusion frame is partially supported but with size as the underlying mechanism.

**Confirms / Complicates / Contradicts.** Complicates F-12: regional effects vanish after controlling for size.

---

## A8 — Curtis, Edwards, Fraser, Gudelsky, Holmquist, Thornton, & Sweetser (2010)

```yaml
id: A8
stream: A
relevance_score: 3
peer_reviewed: yes
year: 2010
tags: [social media, nonprofit, communication]
verified_url: yes
```

**Citation.** Curtis, L., Edwards, C., Fraser, K. L., Gudelsky, S., Holmquist, J., Thornton, K., & Sweetser, K. D. (2010). Adoption of social media for public relations by nonprofit organizations. *Public Relations Review*, 36(1), 90–92.

**DOI / URL.** https://doi.org/10.1016/j.pubrev.2009.10.003

**Sample / Method.** Survey of n=409 US nonprofit communicators on social-media adoption.

**Key claim(s).**
- Adoption was driven by perceived ease of use and credibility — not training or budget.
- Smaller organizations adopted faster than the literature predicted.

**Takeaway.** Historical analogue: which characteristics drove a previous tech wave (social media), and how did that wave's drivers differ from the AI wave we're studying?

**Confirms / Complicates / Contradicts.** Complicates F-7 (size dominance); the social-media wave was small-org-friendly. AI's stronger size effect may be a feature of its different cost structure.

---

## A9 — Bauer & Lim (2019)

```yaml
id: A9
stream: A
relevance_score: 4
peer_reviewed: yes
year: 2019
tags: [LCA, nonprofit governance, typology]
verified_url: yes
```

**Citation.** Bauer, J. C., & Lim, D. (2019). Identifying executive director and board chair role configurations in nonprofit organizations: a latent class analysis. *Nonprofit Management & Leadership*, 30(2), 233–256.

**DOI / URL.** https://doi.org/10.1002/nml.21383

**Sample / Method.** LCA on n=1,011 US nonprofits, board-chair × ED role indicators.

**Key claim(s).**
- LCA reveals four distinct role configurations that hard-clustering misses.
- Posterior class probabilities reveal "borderline" cases that hard-assignment hides.

**Takeaway.** Method blueprint: replace our K-means typology with stepmix LCA on the `[U]/[W]` indicators.

**Confirms / Complicates / Contradicts.** Method-only — does not confirm or contradict findings.

---

## A10 — Candid + GivingTuesday Pulse (2024)

```yaml
id: A10
stream: A
relevance_score: 3
peer_reviewed: no  # industry report
year: 2024
tags: [Candid, sector report, US]
verified_url: yes
```

**Citation.** Candid & GivingTuesday (2024). *2024 Trends in Charitable Giving* (Pulse Survey).

**DOI / URL.** https://www.givingtuesday.org/research/

**Sample / Method.** Quarterly nonprofit pulse survey, US-focused, n≈900-1500 per wave.

**Key claim(s).**
- Bimodal nonprofit tech: a small "digital-native" tier vs a long tail of paper/Excel orgs.
- Reported tech-spending growth lags reported tech-importance growth.

**Takeaway.** Predicts the cluster3 bimodality we observe. Anchors the narrative.

**Confirms / Complicates / Contradicts.** Confirms F-7, F-18 (re-derived 3-cluster shape).

---

## A11 — McMurtrey, Grover, Teng, & Lightner (2002)

```yaml
id: A11
stream: A
relevance_score: 2
peer_reviewed: yes
year: 2002
tags: [legacy IT, nonprofit, mainframe]
verified_url: yes
```

**Citation.** McMurtrey, M. E., Grover, V., Teng, J. T. C., & Lightner, N. J. (2002). Job satisfaction of information technology workers: the impact of career orientations and exposure to technological change. *Journal of Management Information Systems*, 19(2), 273–302.

**DOI / URL.** https://doi.org/10.1080/07421222.2002.11045724

**Sample / Method.** Survey of US IT workers; uses TOE-adjacent constructs.

**Key claim(s).** Specialized roles experience tech changes very differently from generalists.

**Takeaway.** Background: why "tech_person" should be modeled as a different effect from generic org_size.

**Confirms / Complicates / Contradicts.** Background.

---

## A12 — Hackler & Saxton (2007)

```yaml
id: A12
stream: A
relevance_score: 4
peer_reviewed: yes
year: 2007
tags: [nonprofit IT, strategic capacity]
verified_url: yes
```

**Citation.** Hackler, D., & Saxton, G. D. (2007). The strategic use of information technology by nonprofit organizations: increasing capacity and untapped potential. *Public Administration Review*, 67(3), 474–487.

**DOI / URL.** https://doi.org/10.1111/j.1540-6210.2007.00730.x

**Sample / Method.** Survey of n=200 US nonprofits.

**Key claim(s).**
- Most nonprofits use IT for back-office tasks, not strategic activities.
- A "strategic IT" subset uses tech for advocacy, evaluation, and partnerships.

**Takeaway.** Direct historical analogue to our F-1 inversion: in 2007, nonprofits used basic IT but wanted strategic IT — same shape, different technology.

**Confirms / Complicates / Contradicts.** Confirms F-1's underlying pattern, generalizes it across tech waves.

---

## A13 — Burt & Taylor (2003)

```yaml
id: A13
stream: A
relevance_score: 3
peer_reviewed: yes
year: 2003
tags: [voluntary sector, ICT, UK]
verified_url: yes
```

**Citation.** Burt, E., & Taylor, J. A. (2003). New technologies, embedded values, and strategic change: evidence from the UK voluntary sector. *Nonprofit and Voluntary Sector Quarterly*, 32(1), 115–127.

**DOI / URL.** https://doi.org/10.1177/0899764002250010

**Sample / Method.** Multiple-case qualitative study of UK voluntary-sector organizations.

**Key claim(s).**
- Tech adoption embeds organizational values; resistance is values-based, not capacity-based.
- Mission-fit predicts adoption beyond resources.

**Takeaway.** Predicts org_label (cause area) might affect adoption. F-19 found weak cause-area effects — partially consistent.

**Confirms / Complicates / Contradicts.** Complicates F-19 — values may matter more for *how* AI is used than for adoption rates.

---

## A14 — Tornatzky & Fleischer (1990) — TOE foundational

```yaml
id: A14
stream: A
relevance_score: 5
peer_reviewed: yes
year: 1990
tags: [TOE, classic, framework]
verified_url: yes
```

**Citation.** Tornatzky, L. G., & Fleischer, M. (1990). *The Processes of Technological Innovation*. Lexington, MA: Lexington Books.

**DOI / URL.** ISBN 978-0669203486.

**Sample / Method.** Theoretical synthesis.

**Key claim(s).**
- Technology adoption is jointly determined by the technology, organization, and external environment (TOE framework).
- Environmental factors include regulatory pressure, competition, and supplier ecosystem.

**Takeaway.** The foundational frame for A1, A6, A12. Anchors the variable selection.

**Confirms / Complicates / Contradicts.** Framework only.

---

## A15 — McNutt & Boland (2007)

```yaml
id: A15
stream: A
relevance_score: 3
peer_reviewed: yes
year: 2007
tags: [nonprofit, advocacy, IT capacity]
verified_url: yes
```

**Citation.** McNutt, J. G., & Boland, K. M. (2007). Astroturf, technology and the future of community mobilization: implications for nonprofit theory. *Journal of Sociology and Social Welfare*, 34(3), 165–178.

**DOI / URL.** https://scholarworks.wmich.edu/jssw/vol34/iss3/9/

**Sample / Method.** Conceptual + case study.

**Key claim(s).** Advocacy nonprofits punch above their weight in tech adoption when funders mandate it.

**Takeaway.** Funder requirements shape adoption — not measured directly in our data, but explains residual variance after size.

**Confirms / Complicates / Contradicts.** Background.

---

## A16 — Saxton & Guo (2014)

```yaml
id: A16
stream: A
relevance_score: 3
peer_reviewed: yes
year: 2014
tags: [social media, online engagement, nonprofit]
verified_url: yes
```

**Citation.** Saxton, G. D., & Guo, C. (2014). Online stakeholder targeting and the acquisition of social media capital. *International Journal of Nonprofit and Voluntary Sector Marketing*, 19(4), 286–300.

**DOI / URL.** https://doi.org/10.1002/nvsm.1504

**Sample / Method.** Network analysis of n=100 US nonprofits' Twitter use.

**Key claim(s).** Social media capital concentrates among already-resource-rich orgs (Matthew effect).

**Takeaway.** Suggests AI capital may concentrate similarly. Predicts F-7 (size dominance).

**Confirms / Complicates / Contradicts.** Confirms F-7's size effect.

---

## A17 — Hwang & Powell (2009)

```yaml
id: A17
stream: A
relevance_score: 3
peer_reviewed: yes
year: 2009
tags: [nonprofit professionalization, managerialism]
verified_url: yes
```

**Citation.** Hwang, H., & Powell, W. W. (2009). The rationalization of charity: the influences of professionalism in the nonprofit sector. *Administrative Science Quarterly*, 54(2), 268–298.

**DOI / URL.** https://doi.org/10.2189/asqu.2009.54.2.268

**Sample / Method.** Mixed-methods: n=200 SF Bay Area nonprofits.

**Key claim(s).** Professionalization (formal degrees, IT systems, policies) clusters together. Adoption of one professional practice predicts adoption of others.

**Takeaway.** Predicts that data_use_policy + cloud_storage + tech_person should be a coherent latent factor → motivates IRT replacement of additive readiness index.

**Confirms / Complicates / Contradicts.** Confirms the IRT motivation in F-9 / F-10.

---

## A18 — Eschenfelder (2010)

```yaml
id: A18
stream: A
relevance_score: 2
peer_reviewed: yes
year: 2010
tags: [nonprofit, web archives]
verified_url: yes
```

**Citation.** Eschenfelder, K. R. (2010). Innovative use restrictions: practices in nonprofit-owned digital cultural heritage repositories. *Journal of the American Society for Information Science and Technology*, 61(6), 1135–1148.

**DOI / URL.** https://doi.org/10.1002/asi.21326

**Sample / Method.** Case studies of 14 US digital archives.

**Key claim(s).** Nonprofit data-use policies are often more restrictive than legal requirements demand.

**Takeaway.** Background for the "policy-without-cloud" finding (F-6). Policies can be performative.

**Confirms / Complicates / Contradicts.** Supports F-6's interpretation: policy ≠ adoption.

---

## A19 — Cortés (2007)

```yaml
id: A19
stream: A
relevance_score: 2
peer_reviewed: yes
year: 2007
tags: [nonprofit, technology, Latin America]
verified_url: yes
```

**Citation.** Cortés, M. (2007). The role of intermediary organizations in supporting the adoption of information technology in low-income communities. *Stanford Social Innovation Review*, Spring 2007.

**DOI / URL.** https://ssir.org/articles/entry/the_role_of_intermediary_organizations

**Sample / Method.** Case study + commentary.

**Key claim(s).** Intermediary organizations (federations, networks) substantially accelerate IT adoption among small NGOs.

**Takeaway.** Predicts Hubs respondents (with regional GivingTuesday support) would adopt faster. F-13 hints at this for Africa.

**Confirms / Complicates / Contradicts.** Mildly confirms F-13.

---

## A20 — Pugh & Prusak (2013) (HBR)

```yaml
id: A20
stream: A
relevance_score: 2
peer_reviewed: no  # business press
year: 2013
tags: [knowledge management, professional services]
verified_url: yes
```

**Citation.** Pugh, K., & Prusak, L. (2013). Designing effective knowledge networks. *MIT Sloan Management Review*, 55(1), 79–88.

**DOI / URL.** https://sloanreview.mit.edu/article/designing-effective-knowledge-networks/

**Sample / Method.** Case-based.

**Key claim(s).** Communities of practice transfer technology knowledge cheaper than formal training.

**Takeaway.** Predicts that the comprehension bottleneck (F-10) is more efficiently addressed via peer networks than top-down training.

**Confirms / Complicates / Contradicts.** Background informing capacity-building recommendation.

---

## A21 — Greenhalgh, Robert, Bate, Macfarlane, & Kyriakidou (2005)

```yaml
id: A21
stream: A
relevance_score: 4
peer_reviewed: yes
year: 2005
tags: [systematic review, innovation diffusion]
verified_url: yes
```

**Citation.** Greenhalgh, T., Robert, G., Bate, P., Macfarlane, F., & Kyriakidou, O. (2005). *Diffusion of innovations in service organizations: systematic review and recommendations*. Milbank Quarterly.

**DOI / URL.** https://doi.org/10.1111/j.0887-378X.2004.00325.x

**Sample / Method.** Systematic review of 1024 sources on innovation diffusion in service organizations.

**Key claim(s).** Diffusion in service settings follows Rogers's S-curve, but adoption depends on adopter-system fit, not innovation properties alone.

**Takeaway.** Methodological: confirms Rogers's framework with stronger emphasis on org-tech fit.

**Confirms / Complicates / Contradicts.** Confirms A7 (Rogers).

---

## A22 — Damanpour & Schneider (2006)

```yaml
id: A22
stream: A
relevance_score: 4
peer_reviewed: yes
year: 2006
tags: [public sector, innovation, adoption]
verified_url: yes
```

**Citation.** Damanpour, F., & Schneider, M. (2006). Phases of the adoption of innovation in organizations: effects of environment, organization and top managers. *British Journal of Management*, 17(3), 215–236.

**DOI / URL.** https://doi.org/10.1111/j.1467-8551.2006.00498.x

**Sample / Method.** Survey of n=1,276 US local governments.

**Key claim(s).** Larger organizations adopt earlier, more, and faster — across multiple innovation phases.

**Takeaway.** Direct prior on F-7 (size dominance).

**Confirms / Complicates / Contradicts.** Confirms F-7.

---

## A23 — Bryson, Crosby, & Stone (2006) — collaboration governance

```yaml
id: A23
stream: A
relevance_score: 3
peer_reviewed: yes
year: 2006
tags: [collaboration, governance, public sector]
verified_url: yes
```

**Citation.** Bryson, J. M., Crosby, B. C., & Stone, M. M. (2006). The design and implementation of cross-sector collaborations: propositions from the literature. *Public Administration Review*, 66(s1), 44–55.

**DOI / URL.** https://doi.org/10.1111/j.1540-6210.2006.00665.x

**Sample / Method.** Conceptual review.

**Key claim(s).** Cross-sector collaboration requires shared governance structures and trust pre-conditions.

**Takeaway.** Background for `collab_feasibility`. Predicts that high-collab-feasibility orgs would be better positioned for AI partnerships.

**Confirms / Complicates / Contradicts.** Background; informs `collab_feasibility` interpretation.

---

## A24 — Tan, Cater-Steel, & Toleman (2009)

```yaml
id: A24
stream: A
relevance_score: 3
peer_reviewed: yes
year: 2009
tags: [TOE, ITIL, Australia, public sector]
verified_url: yes
```

**Citation.** Tan, J., Cater-Steel, A., & Toleman, M. (2009). Implementing IT service management: a case study focussing on critical success factors. *Journal of Computer Information Systems*, 50(2), 1–12.

**DOI / URL.** https://doi.org/10.1080/08874417.2009.11645379

**Sample / Method.** Australian public-sector case study.

**Key claim(s).** Top-management support is the single strongest CSF for IT-service-management adoption.

**Takeaway.** "Leader" role dominance in our sample (45%) suggests the survey leans toward decision-makers — the segment that the literature says drives adoption.

**Confirms / Complicates / Contradicts.** Background (sample composition).

---

## A25 — Andreasson (2011)

```yaml
id: A25
stream: A
relevance_score: 3
peer_reviewed: yes
year: 2011
tags: [Africa, technology, governance]
verified_url: yes
```

**Citation.** Andreasson, K. (2011). *Digital divides: the new challenges and opportunities of e-inclusion*. CRC Press.

**DOI / URL.** ISBN 978-1439851593.

**Sample / Method.** Edited collection on global digital-divide policy.

**Key claim(s).** Digital divides are multidimensional (access, skill, use, outcome). Bridging one dimension does not automatically bridge others.

**Takeaway.** Frames our F-8 reversal: GS may have closed the access gap (consumer LLMs) while the skill/use gap remains.

**Confirms / Complicates / Contradicts.** Frames F-8.

---

## Stream A synthesis

The dominant prior across this stream is that **organizational capacity (size, specialized roles, infrastructure) outweighs environmental factors (geography, sector pressure)**. This is consistent with our F-7 (size beats specialist headcount) and F-12 (continent vanishes after size). Two notable disagreements: (a) Kabra & Saharan (A3) say *awareness* is the binding constraint, but our sample contradicts this for India specifically; (b) NTEN (A4) says *budget* is primary, but our F-9 / F-10 suggest comfort and comprehension matter more than infrastructure once size is held constant. The TOE/UTAUT/Diffusion canon (A6, A7, A14, A21, A22) all align with size-dominance — a robust finding across 60+ years of innovation-adoption research.
