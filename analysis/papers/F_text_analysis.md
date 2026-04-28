# Stream F — Free-text and computational text analysis

Paper-cards for prior work on topic models, sentence embeddings, multilingual NLP, sentiment, and qualitative coding methods relevant to analyzing the GivingTuesday `org_opentext`, `ai_opentext`, and `non_data_work` free-text fields (n≈600 of 930 respondents, mixed English / Hindi / regional Indian languages).

---

## F1 — Blei, Ng & Jordan (2003)

```yaml
id: F1
stream: F
relevance_score: 5
peer_reviewed: yes
year: 2003
tags: [LDA, topic-model, generative, foundational]
verified_url: yes
```

**Citation.** Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet Allocation. *Journal of Machine Learning Research*, 3, 993–1022.

**DOI / URL.** https://jmlr.csail.mit.edu/papers/v3/blei03a.html

**Sample / Method.** Theoretical derivation; evaluated on TREC AP corpus and Reuters-21578.

**Key claim(s).**
- Documents are mixtures of latent topics; topics are distributions over a fixed vocabulary.
- Variational Bayes / EM gives tractable inference for a three-level hierarchical Bayesian model.

**Takeaway.** The canonical baseline against which any newer topic model (Top2Vec, BERTopic, STM) must be benchmarked. We will report LDA results alongside BERTopic for comparison.

**Confirms / Complicates / Contradicts.** Method baseline; relevant to F-16 (free-text patterns differ across cluster3 groups).

---

## F2 — Blei (2012)

```yaml
id: F2
stream: F
relevance_score: 4
peer_reviewed: yes
year: 2012
tags: [topic-model, review, CACM]
verified_url: yes
```

**Citation.** Blei, D. M. (2012). Probabilistic topic models. *Communications of the ACM*, 55(4), 77–84.

**DOI / URL.** https://doi.org/10.1145/2133806.2133826

**Sample / Method.** Review article surveying LDA and its extensions (correlated, dynamic, supervised topic models).

**Key claim(s).**
- Topic models are useful exploratory tools but their topics require human interpretation.
- Held-out perplexity is a poor proxy for human-judged topic quality.

**Takeaway.** Justifies our two-track validation: quantitative coherence + human inspection of representative documents per topic.

**Confirms / Complicates / Contradicts.** Method framing.

---

## F3 — Angelov (2020)

```yaml
id: F3
stream: F
relevance_score: 4
peer_reviewed: no  # arXiv preprint
year: 2020
tags: [Top2Vec, embedding-cluster, topic-model]
verified_url: yes
```

**Citation.** Angelov, D. (2020). Top2Vec: Distributed representations of topics. *arXiv preprint* arXiv:2008.09470.

**DOI / URL.** https://arxiv.org/abs/2008.09470

**Sample / Method.** Joint document-and-word embedding (doc2vec) followed by UMAP + HDBSCAN clustering on benchmark corpora (20 Newsgroups, Yahoo Answers).

**Key claim(s).**
- Topic count is discovered automatically rather than pre-specified.
- No stop-word removal or lemmatization required.
- Outperforms LDA and PLSA on benchmark coherence and informativeness.

**Takeaway.** Architectural prior to BERTopic; validates the embed→reduce→cluster pipeline. We use BERTopic (its successor) but Top2Vec is the conceptual stepping stone.

**Confirms / Complicates / Contradicts.** Method baseline.

---

## F4 — Grootendorst (2022) — BERTopic

```yaml
id: F4
stream: F
relevance_score: 5
peer_reviewed: no  # arXiv preprint
year: 2022
tags: [BERTopic, c-TF-IDF, sentence-transformer, planned-method]
verified_url: yes
```

**Citation.** Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF procedure. *arXiv preprint* arXiv:2203.05794.

**DOI / URL.** https://arxiv.org/abs/2203.05794

**Sample / Method.** Sentence-transformer embeddings → UMAP → HDBSCAN → class-based TF-IDF for topic word extraction. Benchmarked on 20 Newsgroups, BBC News, Trump tweets.

**Key claim(s).**
- Decoupling embedding from topic-word extraction lets the model swap in any sentence-transformer (incl. multilingual).
- c-TF-IDF gives interpretable per-topic vocabulary without retraining.
- Competitive with classical and neural baselines on NPMI coherence and topic diversity.

**Takeaway.** **The planned Phase 5/6 method.** Fits our regime: ~600 responses, mixed languages, short texts where bag-of-words / LDA struggles.

**Confirms / Complicates / Contradicts.** Method core; directly addresses F-16 (`ai_opentext` topic structure across cluster3).

---

## F5 — Reimers & Gurevych (2019) — Sentence-BERT

```yaml
id: F5
stream: F
relevance_score: 5
peer_reviewed: yes
year: 2019
tags: [sentence-embedding, SBERT, EMNLP, foundational]
verified_url: yes
```

**Citation.** Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-Networks. *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP-IJCNLP)*, 3982–3992.

**DOI / URL.** https://aclanthology.org/D19-1410/

**Sample / Method.** Siamese / triplet fine-tuning of pre-trained BERT on NLI + STS datasets; evaluated on STS-B and SentEval.

**Key claim(s).**
- Pooling raw BERT [CLS] embeddings underperforms even GloVe averaging on semantic similarity.
- Siamese fine-tuning on NLI yields embeddings useful for clustering and retrieval.
- 65 hours of BERT pairwise inference reduces to ~5 seconds with SBERT.

**Takeaway.** The architecture underlying every embedding we'll use, including the planned multilingual MiniLM. Foundational for the BERTopic encoder choice.

**Confirms / Complicates / Contradicts.** Method foundation.

---

## F6 — Reimers & Gurevych (2020) — Multilingual distillation

```yaml
id: F6
stream: F
relevance_score: 5
peer_reviewed: yes
year: 2020
tags: [multilingual, distillation, sentence-embedding, EMNLP]
verified_url: yes
```

**Citation.** Reimers, N., & Gurevych, I. (2020). Making monolingual sentence embeddings multilingual using knowledge distillation. *Proceedings of EMNLP 2020*, 4512–4525.

**DOI / URL.** https://aclanthology.org/2020.emnlp-main.365/

**Sample / Method.** Teacher-student distillation: a strong English SBERT teacher trains a multilingual XLM-R / MiniLM student to embed translations into the same vector space. Evaluated on 50+ languages.

**Key claim(s).**
- Aligned multilingual embeddings can be built without parallel training of a bilingual sentence encoder from scratch.
- A translated sentence and its source map to nearly the same vector — enabling cross-lingual clustering.

**Takeaway.** **The exact training recipe behind `paraphrase-multilingual-MiniLM-L12-v2`** — our chosen BERTopic encoder. Directly justifies pooling Hindi/regional-language responses with English in a single topic model rather than splitting by language.

**Confirms / Complicates / Contradicts.** Method core; enables F-16 multilingual extension.

---

## F7 — Wang et al. (2020) — MiniLM

```yaml
id: F7
stream: F
relevance_score: 4
peer_reviewed: yes
year: 2020
tags: [MiniLM, distillation, NeurIPS, efficiency]
verified_url: yes
```

**Citation.** Wang, W., Wei, F., Dong, L., Bao, H., Yang, N., & Zhou, M. (2020). MiniLM: Deep self-attention distillation for task-agnostic compression of pre-trained transformers. *NeurIPS 2020*.

**DOI / URL.** https://arxiv.org/abs/2002.10957

**Sample / Method.** Distill the last-layer self-attention (queries-keys and values-values relations) of a teacher transformer into a much smaller student.

**Key claim(s).**
- A 6-layer MiniLM retains >99% of the teacher's accuracy on SQuAD/GLUE with ~50% parameters.
- Self-attention distribution is the most transferable signal for compression.

**Takeaway.** Justifies using MiniLM (rather than full XLM-R or LaBSE) for our 600-document corpus — adequate quality at order-of-magnitude lower compute.

**Confirms / Complicates / Contradicts.** Method (efficiency justification).

---

## F8 — Devlin et al. (2019) — BERT

```yaml
id: F8
stream: F
relevance_score: 4
peer_reviewed: yes
year: 2019
tags: [BERT, pretraining, transformer, NAACL, foundational]
verified_url: yes
```

**Citation.** Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *Proceedings of NAACL-HLT 2019*, 4171–4186.

**DOI / URL.** https://aclanthology.org/N19-1423/

**Sample / Method.** Masked language modeling + next-sentence prediction on BooksCorpus + Wikipedia (~3.3B tokens). Evaluated on GLUE, SQuAD, SWAG.

**Key claim(s).**
- Bidirectional pretraining via MLM beats left-to-right pretraining on every benchmark tested.
- Same model fine-tunes for sentence-pair, single-sentence, and span-extraction tasks.

**Takeaway.** Background — every encoder we use is BERT-derived. Anchors the methodological lineage SBERT → multilingual-MiniLM → BERTopic.

**Confirms / Complicates / Contradicts.** Method background.

---

## F9 — Conneau et al. (2020) — XLM-R

```yaml
id: F9
stream: F
relevance_score: 4
peer_reviewed: yes
year: 2020
tags: [XLM-R, multilingual, ACL, 100-languages]
verified_url: yes
```

**Citation.** Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzmán, F., Grave, E., Ott, M., Zettlemoyer, L., & Stoyanov, V. (2020). Unsupervised cross-lingual representation learning at scale. *Proceedings of ACL 2020*, 8440–8451.

**DOI / URL.** https://aclanthology.org/2020.acl-main.747/

**Sample / Method.** RoBERTa-style MLM on 2.5TB filtered CommonCrawl across 100 languages.

**Key claim(s).**
- Multilingual MLM at scale outperforms mBERT by +14.6% XNLI accuracy on average.
- Particularly large low-resource gains: +15.7% Swahili, +11.4% Urdu.
- "Curse of multilinguality" — capacity must scale with language count.

**Takeaway.** Provides the XLM-R backbone that the multilingual MiniLM distills from. Confirms Hindi-English cross-lingual transfer is well-supported, reducing risk that India-source responses cluster purely by script.

**Confirms / Complicates / Contradicts.** Method support; relevant to multilingual handling of `org_opentext`.

---

## F10 — NLLB Team (2022) — No Language Left Behind

```yaml
id: F10
stream: F
relevance_score: 3
peer_reviewed: no  # arXiv tech report; later Nature 2024
year: 2022
tags: [NLLB, machine-translation, low-resource, multilingual]
verified_url: yes
```

**Citation.** NLLB Team, Costa-jussà, M. R., Cross, J., Çelebi, O., Elbayad, M., et al. (2022). No Language Left Behind: Scaling human-centered machine translation. *arXiv preprint* arXiv:2207.04672.

**DOI / URL.** https://arxiv.org/abs/2207.04672

**Sample / Method.** Sparsely-gated mixture-of-experts NMT model trained on FLORES-200 + bitexts mined for 200 languages.

**Key claim(s).**
- +44% BLEU vs prior SOTA on the 40,000+ translation directions of FLORES-200.
- Targeted improvement on low-resource Indian and African languages.

**Takeaway.** Optional fallback if BERTopic produces poor topics for non-English clusters: machine-translate Hindi/regional responses to English with NLLB before re-embedding. We will only use this if multilingual MiniLM clusters show language-confounded topics.

**Confirms / Complicates / Contradicts.** Method contingency.

---

## F11 — Mimno et al. (2011) — Semantic coherence

```yaml
id: F11
stream: F
relevance_score: 5
peer_reviewed: yes
year: 2011
tags: [coherence, evaluation, EMNLP, intrinsic]
verified_url: yes
```

**Citation.** Mimno, D., Wallach, H. M., Talley, E., Leenders, M., & McCallum, A. (2011). Optimizing semantic coherence in topic models. *Proceedings of EMNLP 2011*, 262–272.

**DOI / URL.** https://aclanthology.org/D11-1024/

**Sample / Method.** Defines a coherence metric based on log co-occurrence of top topic words within training documents; correlated with expert quality ratings on a NIH-grant corpus.

**Key claim(s).**
- Coherence based on intra-document co-occurrence beats held-out perplexity at predicting expert quality ratings.
- Identifies "junk" and "chained" topics automatically.

**Takeaway.** Provides the C_umass coherence we will report alongside C_v for BERTopic and LDA. Cheap to compute on 600 short docs.

**Confirms / Complicates / Contradicts.** Method validation.

---

## F12 — Röder, Both & Hinneburg (2015) — Coherence space

```yaml
id: F12
stream: F
relevance_score: 5
peer_reviewed: yes
year: 2015
tags: [coherence, NPMI, C_v, WSDM, evaluation]
verified_url: yes
```

**Citation.** Röder, M., Both, A., & Hinneburg, A. (2015). Exploring the space of topic coherence measures. *Proceedings of WSDM 2015*, 399–408.

**DOI / URL.** https://doi.org/10.1145/2684822.2685324

**Sample / Method.** Decomposes coherence into segmentation × probability × confirmation × aggregation; exhaustively searches the space against human-rated topics on multiple corpora.

**Key claim(s).**
- C_v (NPMI + cosine + sliding window) correlates highest with human ratings.
- NPMI alone is the best of the older single-measure metrics.

**Takeaway.** Specifies the exact coherence reporting standard for our BERTopic outputs (C_v primary, C_npmi secondary).

**Confirms / Complicates / Contradicts.** Method validation.

---

## F13 — Chang et al. (2009) — Reading Tea Leaves

```yaml
id: F13
stream: F
relevance_score: 5
peer_reviewed: yes
year: 2009
tags: [human-evaluation, intrusion-task, NeurIPS, validation]
verified_url: yes
```

**Citation.** Chang, J., Boyd-Graber, J., Gerrish, S., Wang, C., & Blei, D. M. (2009). Reading tea leaves: How humans interpret topic models. *Advances in Neural Information Processing Systems 22 (NeurIPS 2009)*.

**DOI / URL.** https://papers.nips.cc/paper/3700-reading-tea-leaves-how-humans-interpret-topic-models

**Sample / Method.** Word- and topic-intrusion tasks with crowdworkers on NYT and Wikipedia LDA models.

**Key claim(s).**
- Models with better held-out likelihood often produce *less* interpretable topics — perplexity and human judgment are anti-correlated past a point.
- Word intrusion accuracy is a robust human-grounded measure.

**Takeaway.** **Justifies our human-validation step.** We cannot rely on coherence numbers alone; two of us will run a small intruder task on top topics before reporting.

**Confirms / Complicates / Contradicts.** Method validation; central to our planned validation strategy.

---

## F14 — Roberts, Stewart & Tingley (2014) — STM

```yaml
id: F14
stream: F
relevance_score: 5
peer_reviewed: yes
year: 2014
tags: [STM, structural-topic-model, AJPS, covariates, survey]
verified_url: yes
```

**Citation.** Roberts, M. E., Stewart, B. M., Tingley, D., Lucas, C., Leder-Luis, J., Gadarian, S. K., Albertson, B., & Rand, D. G. (2014). Structural topic models for open-ended survey responses. *American Journal of Political Science*, 58(4), 1064–1082.

**DOI / URL.** https://doi.org/10.1111/ajps.12103

**Sample / Method.** STM applied to open-ended survey questions with treatment-arm covariates; n≈ thousands.

**Key claim(s).**
- Topics' prevalence and content can be modeled as a function of document covariates (treatment, demographics).
- STM enables causal-style "treatment effects on topic prevalence" estimates from open-ended responses.

**Takeaway.** **Methodological alternative to BERTopic.** STM lets us regress topic prevalence directly on `cluster3`, `org_size`, `india_rural_urban`, etc. — exactly what F-16 needs. We will report STM as a complement to BERTopic.

**Confirms / Complicates / Contradicts.** Method core; directly addresses F-16's covariate question.

---

## F15 — Roberts, Stewart & Tingley (2019) — stm R package

```yaml
id: F15
stream: F
relevance_score: 4
peer_reviewed: yes
year: 2019
tags: [STM, software, JSS, R-package]
verified_url: yes
```

**Citation.** Roberts, M. E., Stewart, B. M., & Tingley, D. (2019). stm: An R package for structural topic models. *Journal of Statistical Software*, 91(2).

**DOI / URL.** https://doi.org/10.18637/jss.v091.i02

**Sample / Method.** Software paper documenting EM estimation, covariate effects, content-by-covariate models, perplexity-anchored model selection.

**Key claim(s).**
- searchK / lee-mimno semantic-coherence × exclusivity grid for choosing number of topics.
- Permutation tests for covariate effects.

**Takeaway.** Operational reference for our STM run: `searchK(K = 5:15)`, `prevalence = ~ cluster3 + s(org_years)`, content covariate = `ref` (gt/india/tech/hubs).

**Confirms / Complicates / Contradicts.** Method (implementation).

---

## F16 — Lucas et al. (2015) — Multilingual STM

```yaml
id: F16
stream: F
relevance_score: 4
peer_reviewed: yes
year: 2015
tags: [STM, multilingual, comparative-politics, translation]
verified_url: yes
```

**Citation.** Lucas, C., Nielsen, R. A., Roberts, M. E., Stewart, B. M., Storer, A., & Tingley, D. (2015). Computer-assisted text analysis for comparative politics. *Political Analysis*, 23(2), 254–277.

**DOI / URL.** https://doi.org/10.1093/pan/mpu019

**Sample / Method.** Two case studies (Arabic Islamic legal texts; Chinese microblogs) of cross-lingual topic modeling via STM after machine translation.

**Key claim(s).**
- Machine-translation-then-STM is a defensible pipeline when sentence-level multilingual encoders are unavailable.
- Topic stability across translation backends is a useful robustness check.

**Takeaway.** Provides a bilingual-validation precedent: we can replicate our multilingual MiniLM topics by NLLB-translating to English and re-running, and check overlap.

**Confirms / Complicates / Contradicts.** Method robustness check.

---

## F17 — DiMaggio, Nag & Blei (2013)

```yaml
id: F17
stream: F
relevance_score: 4
peer_reviewed: yes
year: 2013
tags: [LDA, sociology, culture, application, Poetics]
verified_url: yes
```

**Citation.** DiMaggio, P., Nag, M., & Blei, D. (2013). Exploiting affinities between topic modeling and the sociological perspective on culture: Application to newspaper coverage of U.S. government arts funding. *Poetics*, 41(6), 570–606.

**DOI / URL.** https://doi.org/10.1016/j.poetic.2013.08.004

**Sample / Method.** LDA on ~8,000 newspaper articles 1986–1997 covering NEA arts funding.

**Key claim(s).**
- Topic models are a defensible way to operationalize "frames" and "cultural categories" in a Bourdieu/Swidler tradition.
- Topic prevalence shifts (controversy frame, 1989 onwards) align with offline events.

**Takeaway.** Sociological precedent for treating topics from `org_opentext` as "frames" of nonprofit identity, not just word clusters.

**Confirms / Complicates / Contradicts.** Methodological framing for narrative interpretation.

---

## F18 — Egger & Yu (2022) — LDA vs NMF vs Top2Vec vs BERTopic

```yaml
id: F18
stream: F
relevance_score: 5
peer_reviewed: yes
year: 2022
tags: [comparison, BERTopic, Top2Vec, LDA, NMF, short-text]
verified_url: yes
```

**Citation.** Egger, R., & Yu, J. (2022). A topic modeling comparison between LDA, NMF, Top2Vec, and BERTopic to demystify Twitter posts. *Frontiers in Sociology*, 7, 886498.

**DOI / URL.** https://doi.org/10.3389/fsoc.2022.886498

**Sample / Method.** Head-to-head on travel- and COVID-related tweets; same corpus, four pipelines, evaluated by qualitative inspection + topic diversity.

**Key claim(s).**
- BERTopic and Top2Vec preserve sentence semantics on short texts where bag-of-words methods (LDA) lose them.
- NMF beats LDA on short noisy text.
- Human inspection is still required — no model is unambiguously best.

**Takeaway.** **Direct empirical justification for BERTopic over LDA in our setting** — `ai_opentext` responses average 15–40 words, exactly the regime where the paper's findings apply.

**Confirms / Complicates / Contradicts.** Confirms our planned method choice for F-16.

---

## F19 — Litofcenko, Karner & Maier (2020)

```yaml
id: F19
stream: F
relevance_score: 4
peer_reviewed: yes
year: 2020
tags: [nonprofit, mission, classification, VOLUNTAS, application]
verified_url: yes
```

**Citation.** Litofcenko, J., Karner, D., & Maier, F. (2020). Methods for classifying nonprofit organizations according to their field of activity: A report on semi-automated methods based on text. *VOLUNTAS: International Journal of Voluntary and Nonprofit Organizations*, 31(1), 227–237.

**DOI / URL.** https://doi.org/10.1007/s11266-019-00181-w

**Sample / Method.** Compared rule-based keyword classification vs supervised ML on Austrian nonprofit mission-statement data; benchmarked against the ICNPO taxonomy.

**Key claim(s).**
- Supervised ML beats rule-based keyword approaches when training labels are reliable.
- Mission-statement text length is the strongest single predictor of classification accuracy — short missions are unclassifiable.

**Takeaway.** Direct precedent for using `org_opentext` as a classification signal. Predicts our short-text problem: 65% response rate with many one-line answers will bound BERTopic accuracy.

**Confirms / Complicates / Contradicts.** Confirms F-16 cautionary note: text length matters; lower-cluster (Late Adopters) write less and may be undertyped.

---

## F20 — Ramamoorthy et al. — Identifying Nonprofits via Word Embeddings

```yaml
id: F20
stream: F
relevance_score: 3
peer_reviewed: yes
year: 2021
tags: [word-embedding, nonprofit, scaling, VOLUNTAS]
verified_url: yes
```

**Citation.** Ma, J. (2021). Identifying nonprofits by scaling mission and activity with word embedding. *VOLUNTAS: International Journal of Voluntary and Nonprofit Organizations*, 32(3), 553–566.

**DOI / URL.** https://doi.org/10.1007/s11266-021-00399-7

**Sample / Method.** Word-embedding-based scaling of nonprofit mission/activity descriptions to a continuous typology dimension.

**Key claim(s).**
- Embedding-based scaling captures gradations missed by discrete NTEE / ICNPO codes.
- Cosine similarity to anchor terms ("research", "service", "advocacy") gives interpretable axes.

**Takeaway.** Methodological precedent for using sentence embeddings of `org_opentext` to extract latent dimensions (e.g., service-vs-advocacy) for downstream regressions.

**Confirms / Complicates / Contradicts.** Method extension for F-16.

---

## F21 — Braun & Clarke (2006) — Thematic analysis

```yaml
id: F21
stream: F
relevance_score: 4
peer_reviewed: yes
year: 2006
tags: [thematic-analysis, qualitative, methods, foundational]
verified_url: yes
```

**Citation.** Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77–101.

**DOI / URL.** https://doi.org/10.1191/1478088706qp063oa

**Sample / Method.** Methodological article specifying a 6-phase procedure for thematic analysis (familiarisation → coding → searching → reviewing → defining → reporting).

**Key claim(s).**
- Thematic analysis is theoretically flexible and not bound to a particular epistemology.
- Distinguishes semantic vs latent themes; inductive vs theoretical coding.

**Takeaway.** Defines the human-coding procedure for the "hopes and fears" sub-analysis on `ai_opentext`. We will use TA to build a 12-code book, double-code 80 responses for κ, and use it as a *human ground truth* against which to score BERTopic topics.

**Confirms / Complicates / Contradicts.** Method (validation reference standard).

---

## F22 — Hutto & Gilbert (2014) — VADER

```yaml
id: F22
stream: F
relevance_score: 4
peer_reviewed: yes
year: 2014
tags: [VADER, sentiment, lexicon, ICWSM, short-text]
verified_url: yes
```

**Citation.** Hutto, C. J., & Gilbert, E. (2014). VADER: A parsimonious rule-based model for sentiment analysis of social media text. *Proceedings of the International AAAI Conference on Web and Social Media (ICWSM)*, 8(1), 216–225.

**DOI / URL.** https://ojs.aaai.org/index.php/ICWSM/article/view/14550

**Sample / Method.** Crowd-validated lexicon (~7,500 lexical features) + 5 rule heuristics (negation, intensifiers, contrastive conjunctions, punctuation/capitalization). Validated on tweets, NYT editorials, Amazon reviews.

**Key claim(s).**
- F1 = 0.96 vs human F1 = 0.84 on 3-class tweet sentiment.
- Outperforms LIWC and General Inquirer on social-media-style text.

**Takeaway.** **Directly tests F-16's tone claim.** We will run VADER on the English subset of `ai_opentext` and check whether the cluster-3 difference (Consumers more positive) survives a validated sentiment lexicon.

**Confirms / Complicates / Contradicts.** Tests F-16 (Consumers write more positively).

---

## F23 — Pennebaker, Boyd, Jordan & Blackburn (2015) — LIWC2015

```yaml
id: F23
stream: F
relevance_score: 3
peer_reviewed: no  # technical report
year: 2015
tags: [LIWC, sentiment, psycholinguistics, dictionary]
verified_url: yes
```

**Citation.** Pennebaker, J. W., Boyd, R. L., Jordan, K., & Blackburn, K. (2015). *The development and psychometric properties of LIWC2015*. University of Texas at Austin.

**DOI / URL.** https://repositories.lib.utexas.edu/bitstreams/b0d26dcf-2391-4701-88d0-3cf50ebee697/download

**Sample / Method.** Dictionary construction + psychometric validation of word categories: positive/negative emotion, social, cognitive, plus 4 summary scores (analytic, clout, authenticity, tone).

**Key claim(s).**
- LIWC2015 introduces emotional tone as a single bipolar score from positive- and negative-emotion words.
- Validated cross-corpus on essays, conversations, social media.

**Takeaway.** Secondary lexicon for triangulation with VADER. Adds a "cognitive complexity" angle (insight, causation words) potentially mapping to comprehension differences across cluster3.

**Confirms / Complicates / Contradicts.** Triangulation source for F-16.

---

## F24 — Nielsen (2011) — AFINN

```yaml
id: F24
stream: F
relevance_score: 3
peer_reviewed: no  # workshop / arXiv
year: 2011
tags: [AFINN, sentiment, lexicon, microblogs]
verified_url: yes
```

**Citation.** Nielsen, F. Å. (2011). A new ANEW: Evaluation of a word list for sentiment analysis in microblogs. *Proceedings of the ESWC2011 Workshop on Making Sense of Microposts*, 93–98. *arXiv preprint* arXiv:1103.2903.

**DOI / URL.** https://arxiv.org/abs/1103.2903

**Sample / Method.** ~2,400-word list scored −5…+5 by the author; benchmarked against ANEW and SentiStrength on labeled tweets.

**Key claim(s).**
- A microblog-tuned lexicon outperforms ANEW on Twitter sentiment.
- Simpler than rule-based systems; competitive on accuracy.

**Takeaway.** Third sentiment lexicon for triangulation. Used together with VADER and LIWC, agreement across all three is much stronger evidence than any single tool for the F-16 tone claim.

**Confirms / Complicates / Contradicts.** Triangulation source for F-16.

---

## F25 — Kakwani et al. (2020) — IndicBERT / IndicNLPSuite

```yaml
id: F25
stream: F
relevance_score: 5
peer_reviewed: yes
year: 2020
tags: [IndicBERT, Indian-languages, EMNLP-Findings, multilingual]
verified_url: yes
```

**Citation.** Kakwani, D., Kunchukuttan, A., Golla, S., Gokul, N. C., Bhattacharyya, A., Khapra, M. M., & Kumar, P. (2020). IndicNLPSuite: Monolingual corpora, evaluation benchmarks and pre-trained multilingual language models for Indian languages. *Findings of the Association for Computational Linguistics: EMNLP 2020*, 4948–4961.

**DOI / URL.** https://aclanthology.org/2020.findings-emnlp.445/

**Sample / Method.** 8.8B-token IndicCorp across 11 Indic languages + Indian English; ALBERT-based IndicBERT pretraining; IndicGLUE benchmark.

**Key claim(s).**
- IndicBERT outperforms mBERT and XLM-R on most IndicGLUE tasks despite ~10× fewer parameters.
- Targeted Indic pretraining beats general multilingual pretraining for low-resource Indian languages.

**Takeaway.** **Backstop encoder.** If multilingual MiniLM clusters India-source responses too tightly by language, IndicBERT (or its v2) gives a Hindi-aware embedding to retry.

**Confirms / Complicates / Contradicts.** Method contingency for India sub-sample (n=251).

---

## F26 — Khanuja et al. (2021) — MuRIL

```yaml
id: F26
stream: F
relevance_score: 4
peer_reviewed: no  # arXiv
year: 2021
tags: [MuRIL, Indian-languages, code-switching, transliteration]
verified_url: yes
```

**Citation.** Khanuja, S., Bansal, D., Mehtani, S., Khosla, S., Dey, A., Gopalan, B., Margam, D. K., Aggarwal, P., Nagipogu, R. T., Dave, S., Gupta, S., Gali, S. C. B., Subramanian, V., & Talukdar, P. (2021). MuRIL: Multilingual representations for Indian languages. *arXiv preprint* arXiv:2103.10730.

**DOI / URL.** https://arxiv.org/abs/2103.10730

**Sample / Method.** BERT-base trained on 16 Indian languages + English with augmented translation and *transliteration* parallel pairs.

**Key claim(s).**
- Outperforms mBERT on XTREME for Indian languages.
- Transliteration augmentation handles Hinglish / Latin-script Hindi explicitly — important for code-mixed survey free-text.

**Takeaway.** **Specifically valuable for our India sub-sample**, where romanized Hindi (Hinglish) is common in NGO survey data and is poorly handled by both mBERT and standard multilingual MiniLM.

**Confirms / Complicates / Contradicts.** Method contingency for code-mixed responses.

---

## F27 — McInnes, Healy & Melville (2018) — UMAP

```yaml
id: F27
stream: F
relevance_score: 3
peer_reviewed: yes  # JOSS
year: 2018
tags: [UMAP, dimension-reduction, BERTopic-component]
verified_url: yes
```

**Citation.** McInnes, L., Healy, J., & Melville, J. (2018). UMAP: Uniform manifold approximation and projection for dimension reduction. *arXiv preprint* arXiv:1802.03426; software paper in *Journal of Open Source Software*, 3(29), 861.

**DOI / URL.** https://arxiv.org/abs/1802.03426 ; https://doi.org/10.21105/joss.00861

**Sample / Method.** Riemannian-geometry / algebraic-topology grounded manifold learning; benchmarked vs t-SNE on MNIST, Fashion-MNIST, single-cell RNA.

**Key claim(s).**
- Preserves more global structure than t-SNE while matching local quality.
- Scales to millions of points.

**Takeaway.** UMAP is the dimensionality-reduction step inside BERTopic — relevant when reporting hyperparameters (`n_neighbors`, `min_dist`).

**Confirms / Complicates / Contradicts.** Method (BERTopic component).

---

## F28 — Campello, Moulavi & Sander (2013) — HDBSCAN

```yaml
id: F28
stream: F
relevance_score: 3
peer_reviewed: yes
year: 2013
tags: [HDBSCAN, clustering, density-based, BERTopic-component]
verified_url: yes
```

**Citation.** Campello, R. J. G. B., Moulavi, D., & Sander, J. (2013). Density-based clustering based on hierarchical density estimates. In *Advances in Knowledge Discovery and Data Mining (PAKDD 2013)*, LNCS 7819, 160–172.

**DOI / URL.** https://doi.org/10.1007/978-3-642-37456-2_14

**Sample / Method.** Hierarchical density-based clustering with a stability-maximizing flat extraction. Benchmarked vs DBSCAN, OPTICS.

**Key claim(s).**
- Outperforms DBSCAN by automatically choosing per-cluster density thresholds.
- Naturally provides a "noise" cluster — points not assigned to any topic.

**Takeaway.** HDBSCAN is the clustering step inside BERTopic. Its noise-cluster output is *useful* in our setting: short / off-topic responses get filtered out automatically rather than forced into a topic.

**Confirms / Complicates / Contradicts.** Method (BERTopic component).

---

## F29 — Gentzkow, Kelly & Taddy (2019) — Text as Data

```yaml
id: F29
stream: F
relevance_score: 3
peer_reviewed: yes
year: 2019
tags: [text-as-data, review, JEL, methods]
verified_url: yes
```

**Citation.** Gentzkow, M., Kelly, B., & Taddy, M. (2019). Text as data. *Journal of Economic Literature*, 57(3), 535–574.

**DOI / URL.** https://doi.org/10.1257/jel.20181020

**Sample / Method.** Review article surveying text representation, dimensionality reduction, supervised and unsupervised models, with applications in economics.

**Key claim(s).**
- Different research questions demand different text-representation choices; dictionary methods, topic models, and embeddings are *complements*, not substitutes.
- Validation against held-out human judgment is essential.

**Takeaway.** Frames our multi-method approach (BERTopic + STM + sentiment dictionaries + thematic coding) as a feature, not a redundancy.

**Confirms / Complicates / Contradicts.** Methodological framing.

---

## Stream F synthesis

Our planned method for re-testing **F-16** (cluster-3 differences in `ai_opentext` length, topic content, and tone) is **BERTopic with `paraphrase-multilingual-MiniLM-L12-v2` embeddings**, validated against (a) classical LDA, (b) STM with `cluster3` and `org_size` as prevalence covariates, and (c) human thematic coding of 80 sampled responses. Three considerations drive this choice. First, the corpus is short, mixed-language, and small (~600 documents, ~15–40 words each) — exactly the regime where Egger & Yu (F18) show that bag-of-words LDA loses semantic signal that transformer-based models retain, and where Litofcenko et al. (F19) show short-text classification accuracy is bounded by document length regardless of method. Second, the multilingual-distillation training recipe of Reimers & Gurevych (F6) maps Hindi, English, and code-mixed responses into a shared vector space, so we can cluster jointly without language-confounding — with IndicBERT (F25) and MuRIL (F26) as backstop encoders if we observe language-driven topics. Third, neither BERTopic nor LDA is self-validating: per Chang et al. (F13), held-out perplexity can anti-correlate with human interpretability. We therefore adopt a **two-track validation strategy** — quantitative (C_v / C_npmi coherence per Röder F12, semantic coherence per Mimno F11) plus qualitative (Braun-Clarke thematic codebook F21 used as ground truth for an intruder task). The STM track (F14, F15, F16) lets us *regress* topic prevalence on `cluster3`, `org_size`, and `ref` — the exact covariate-effect question F-16 raises — which BERTopic alone cannot answer parametrically. Sentiment triangulation across VADER (F22), LIWC (F23), and AFINN (F24) tests the F-16 tone claim ("Consumers write more positively") with three independent lexicons; agreement across all three is the bar we set for reporting it as confirmed. The choice of BERTopic over STM as the *primary* topic model rests on three considerations the literature backs: (i) STM's bag-of-words representation is poorly suited to short multilingual responses (F18, F19); (ii) BERTopic's HDBSCAN step (F28) produces an explicit noise cluster, which is the right behavior for the ~10–15% of responses that are uncodable single-word answers; and (iii) reporting both gives reviewer-defensible robustness, since they make different modeling assumptions and any topic that survives both is unlikely to be an artifact of either pipeline.
