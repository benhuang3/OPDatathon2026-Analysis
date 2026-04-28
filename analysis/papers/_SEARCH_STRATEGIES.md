# Search strategies — Phase 3 deep literature dive

8 streams, ≥25 papers each. Each stream has its inclusion criteria and target queries.

## Universal inclusion criteria
- **Languages**: English; obvious translations from Spanish/French/Portuguese OK; reject inaccessible Chinese-only / Arabic-only sources unless an English abstract exists.
- **Date range**: prefer 2018+ for empirical AI work, 2010+ for nonprofit-tech reports, classics (TOE 1990, Rogers 1962/2003, Slovic 1987) admitted as canonical.
- **Source quality bar (descending)**: peer-reviewed journal > peer-reviewed conference (FAccT/CHI/ICTD) > major industry/government report (Stanford HAI, McKinsey, NTEN, Salesforce, Candid, NCCS) > working paper > thesis > blog (admit only as supporting commentary).
- **Citation-count floor**: skip blog posts and lightly-cited working papers unless they uniquely cover a topic.
- **Verifiability**: prefer items with a DOI or stable URL. Tag `verified_url: unable` if I can't find a stable link.

## Per-stream queries

### Stream A — Nonprofit technology adoption (target ≥25)
- "TOE framework nonprofit technology adoption" (Tornatzky-Fleischer)
- "UTAUT nonprofit OR voluntary OR third sector"
- "diffusion of innovations nonprofit Rogers"
- "NTEN digital investments report" (every year 2018–2025)
- "Salesforce.org Nonprofit Trends Report"
- "Candid Foundation Center technology nonprofit"
- "NCCS National Center for Charitable Statistics technology"
- "nonprofit digital maturity systematic review"
- "nonprofit information technology adoption barriers"
- "nonprofit data infrastructure capacity"

Targets: ≥5 systematic reviews; ≥10 peer-reviewed; rest can be major reports.

### Stream B — AI adoption in social/public sector (≥25)
- "Stanford HAI AI Index" (2021, 2022, 2023, 2024, 2025 chapters)
- "McKinsey State of AI" 2023, 2024, 2025
- "BCG AI at Work" survey series
- "Deloitte State of Generative AI Enterprise"
- "MIT Sloan Management Review AI workforce"
- "AI for good systematic review nonprofit" (Madianou; Rotter et al. 2025)
- "generative AI nonprofit case study"
- "AI public sector adoption barriers"
- "AI nonprofit ethics governance"
- "intent action gap AI adoption"

### Stream C — Global North/South digital divide (≥25)
- "Heeks digital development inclusion adverse"
- "ICT4D systematic review"
- "Avgerou information systems developing countries"
- "Toyama amplification technology"
- "Walsham critical IT developing"
- "NASSCOM Foundation tech for good India"
- "Sattva Tech4Good Indian NGO"
- "Dasra Bain India Philanthropy AI"
- "Friederici Graham Mann African digital economy"
- "Png AI tensions south north"
- "Mohamed AI decolonial"
- "Birhane algorithmic injustice Global South"
- "ECLAC Latin America digital"

### Stream D — Survey statistical methods (≥25)
- "Vermunt Magidson latent class analysis review"
- "Lazarsfeld Henry latent structure analysis"
- "Reckase multidimensional IRT"
- "Embretson Reise IRT psychometric"
- "Kline structural equation modeling"
- "Bollen structural equations latent variables"
- "Oaxaca Blinder decomposition wage gap"
- "Jann Stata oaxaca"
- "Mercer Pew non-probability survey weighting"
- "Valliant Dever non-probability inference"
- "Gelman Hill multilevel hierarchical models"
- "small area estimation Rao Molina"
- "MRP multilevel regression poststratification"
- "Benjamini Hochberg FDR"

### Stream E — Risk perception & technology acceptance (≥25)
- "Slovic risk perception"
- "Slovic affect heuristic"
- "Kahneman Tversky prospect theory"
- "Fischhoff risk perception lay public"
- "Dietvorst algorithm aversion"
- "Logg algorithm appreciation"
- "Glikson Woolley human trust AI 2020 review"
- "Lee See trust automation"
- "Hoff Bashir trust automation review"
- "Shin explainable AI trust"
- "Davis TAM technology acceptance model"
- "Venkatesh UTAUT2 consumer"

### Stream F — Free-text / computational text analysis (≥25)
- "Blei latent Dirichlet allocation"
- "Mimno topic coherence"
- "Roberts STM structural topic"
- "Grootendorst BERTopic"
- "Reimers Gurevych sentence-BERT"
- "Devlin BERT pre-training"
- "Conneau XLM-R cross-lingual"
- "NLLB no language left behind"
- "Litofcenko mission statement classification"
- "Suarez nonprofit mission statements"
- "topic model evaluation human"
- "BERTopic multilingual evaluation"

### Stream G — Capacity building, training, intervention design (≥25)
- "cognitive load theory professional training Sweller"
- "Ebrahim NGO accountability learning"
- "Edwards Hulme NGO performance"
- "peer learning network nonprofit"
- "digital literacy intervention evaluation"
- "agriculture extension services adoption"
- "AI literacy training curriculum"
- "nonprofit capacity building evaluation"
- "T-shaped skills nonprofit professional"
- "training transfer organisation"

### Stream H — Sample bias / non-probability survey inference (≥25)
- "AAPOR non-probability survey task force"
- "MRP multilevel regression poststratification Park Gelman"
- "propensity score weighting online panel"
- "Wang Forecasting Xbox 2016 MRP"
- "raking calibration weights survey"
- "Mercer Lau Kennedy Pew non-probability"
- "convenience sample bias inference"
- "online panel coverage bias"
- "weighting against benchmark NCCS Candid"
- "990 IRS form nonprofit population"
- "GuideStar Candid panel data"

## Disagreement-mining priority

Before finalizing each stream, check for the following debate axes (each generates a hypothesis):

| Axis | Side X | Side ¬X |
|---|---|---|
| Will the GenAI-skewed adoption rebalance? | Stanford HAI / McKinsey (yes, early phase) | Madianou (no, structural feature) |
| Does comfort grow with use? | BCG (yes) | Renieris/MIT SMR (yes for comfort, but vigilance fails to grow) |
| Does the GN/GS divide reappear at the institutional level? | Heeks / Toyama (yes) | Avgerou / Nemer (no — substantive null) |
| Is governance prior or posterior to adoption? | NTEN (governance enables adoption) | Salesforce digital-maturity (cooperation in both directions) |
| Algorithm aversion vs appreciation? | Dietvorst (aversion after seeing error) | Logg (appreciation when no error visible) |
| Is the binding constraint on AI in nonprofits comprehension or infrastructure? | Kabra & Saharan (comprehension) | NTEN/Salesforce (infrastructure) |

≥10 disagreements get explicitly mapped into RESEARCH.md.

## Verification protocol

For each paper-card:
1. Have I located the paper via WebSearch with a stable URL or DOI?
2. Have I read at least the abstract (or the equivalent: a published summary)?
3. Is the year, journal/venue, and authorship as I recorded it?
4. If any of the above fails, set `verified_url: unable` and lower `relevance_score` accordingly.

The point of this step is journal-review credibility — fabricating a citation is worse than skipping it.
