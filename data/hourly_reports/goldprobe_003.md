# Gold Probe — Agent Discovery Alpha — 2026-09-07 19:38 Asia/Phnom_Penh

Date: Mon, 7 Sep 2026 08:41:48 -0400

# Gold Probe — Agent Discovery Alpha — 2026-09-07 19:38 Asia/Phnom_Penh

## 1. EXECUTIVE ALPHA

This run produced four accepted evidence clusters. Three are from entities not present in the prior two reports. The strongest update is that **citation, mention, recommendation and click are separate layers**, and the source graph varies sharply by engine and query type.

1. **Shopping queries are much more commerce-page-heavy than generic AI-search advice implies.** FoundGPT analyzed 58,846 ChatGPT shopping citations generated from 3,601 buyer-decision prompts across 107 Shopify stores (Apr 19–Aug 9, 2026). Retailer/marketplace pages were 52.8% of citations and brand/store sites another 14.7%, so 67.5% of citations were commerce pages. Two independent Shopify stores each out-cited Amazon roughly 10× within their own tracked niches (255 and 241 citations vs 22 for amazon.com). This materially weakens a generic “you need big-domain authority” hypothesis for niche shopping prompts.

2. **The “Reddit is essential for AI visibility” thesis fails badly for shopping on ChatGPT.** In FoundGPT’s broader 207,297-citation corpus across ChatGPT, Google AI Mode, Perplexity, Gemini and Claude, Reddit represented only 0.5% of shopping citations overall. ChatGPT cited Reddit 0 times in 58,846 shopping citations; Google AI Mode cited it 578 times / 17,145 (3.4%) and Perplexity 453 / 8,190 (5.5%). YouTube was the top community source across engines. The mechanism is therefore conditional: query class × engine determines which external corroboration surfaces matter.

3. **Citation is not recommendation.** Semrush + Kevin Indig logged 3,981 domain appearances across 115 prompts, 14 countries and four AI surfaces. 61.7% were “ghost citations”: the source was linked but the brand was never named. Only 13.2% were both cited and mentioned; 25.1% were mentioned without citation. ChatGPT cited in 87% of appearances but mentioned brands in only 20.7%; Gemini showed the inverse pattern, naming brands in 83.7% of appearances but citing only 21.4%. This is a major measurement correction: citation-share dashboards can materially overstate actual recommendation visibility.

4. **Certain third-party identity surfaces appear structurally important in B2B/professional queries.** Semrush analyzed 325,000 prompts and 89,000 LinkedIn URLs across ChatGPT Search, Google AI Mode and Perplexity. LinkedIn appeared in 11% of responses on average; 14.3% for ChatGPT Search, 13.5% for Google AI Mode and 5.3% for Perplexity. Long-form LinkedIn articles and original posts dominated citations, while most cited posts had only moderate engagement. This suggests agent discovery can rely on indexable first-party-professional identity surfaces rather than viral social popularity.

**Net belief update:** the discovery layer is not one universal “authority graph.” It is better modeled as:

**query class → engine-specific retrieval corpus → source eligibility → citation → brand/entity mention → recommendation slot → click/transaction.**

Optimizing one layer and measuring another can produce false confidence.

---

## 2. FIELD EVIDENCE TABLE

| Rank | Record | Palace proximity | Novelty | Decision impact | Core evidence |
|---|---|---:|---|---|---|
| 1 | ADA-20260907-01 FoundGPT shopping citation map | 82 | HIGH | VERY HIGH | 58,846 ChatGPT citations; 67.5% commerce pages; niche independent stores out-cited Amazon ~10× |
| 2 | ADA-20260907-02 FoundGPT Reddit null | 82 | HIGH | VERY HIGH | Reddit 0 / 58,846 ChatGPT shopping citations; 0.5% across 207,297 citations |
| 3 | ADA-20260907-03 Semrush ghost citations | 58 | HIGH | VERY HIGH | 61.7% citations did not name the brand; ChatGPT and Gemini have opposite citation/mention behavior |
| 4 | ADA-20260907-04 Semrush LinkedIn corpus | 58 | HIGH | HIGH | 325k prompts; 89k LinkedIn URLs; LinkedIn in 11% of AI responses on average |

Accepted sources are descriptive, not causal, unless explicitly noted.

---

## 3. EXACT WORDS

**Rahul / FoundGPT, Aug 9 2026, 107 Shopify-store corpus:** “Two-thirds are commerce pages; independent stores out-cite Amazon 10×.”
Source: https://foundgpt.app/blog/where-chatgpt-sends-shoppers

**Rahul / FoundGPT, Aug 9 2026:** “ChatGPT cited Reddit exactly zero times in our corpus.”
Source: https://foundgpt.app/blog/reddit-ai-search-shopping-study

**Semrush / Kevin Indig study, Jun 9 2026:** “62% of AI citations are ghost citations.”
Source: https://www.semrush.com/blog/the-ghost-citations-study/

**Kevin Indig, quoted in Semrush:** “There’s almost no overlap between which brands ChatGPT cites and which ones Gemini names for the same prompt.”
Source: https://www.semrush.com/blog/the-ghost-citations-study/

---

## 4. MECHANISMS

### Mechanism M1 — Shopping discovery is more first-party/commerce-surface-driven than generic GEO advice suggests
Evidence FOR: 67.5% of FoundGPT’s ChatGPT shopping citations were retailer/marketplace + brand/store pages; 11,942 citations landed directly on `/products/` URLs.
Counterevidence: editorial still mattered; WhoWhatWear was the single most-cited domain in that corpus, and specialist magazines remained important.
Interpretation: for shopping prompts, high-quality deep product/collection/buying-guide pages are direct retrieval targets rather than merely landing pages after external corroboration.

### Mechanism M2 — External corroboration is engine/query-specific, not universal
Evidence FOR: Reddit was 0% of ChatGPT shopping citations but 3.4% in Google AI Mode and 5.5% in Perplexity. YouTube was a meaningful community source across engines.
Counterevidence: previous broad studies show Reddit matters heavily in SaaS/tech and some non-shopping tasks.
Interpretation: “get mentioned on Reddit” is not a general mechanism. The correct intervention depends on the actual source family each engine uses for the target query class.

### Mechanism M3 — Recommendation visibility is a distinct objective from source citation
Evidence FOR: 61.7% ghost-citation rate; only 13.2% of appearances were both cited and named. ChatGPT citation-heavy / low-name; Gemini name-heavy / low-citation.
Counterevidence: dataset only 115 prompts, albeit across 14 countries.
Interpretation: a citation dashboard can show improvement without creating any visible brand-selection outcome. The canonical KPI should separate: citation rate, named-brand rate, recommendation-slot rate, click rate, conversion rate.

### Mechanism M4 — Indexable professional identity surfaces can shape B2B answers
Evidence FOR: LinkedIn appeared in 11% of 325k AI-prompt responses on average in Semrush’s corpus; cited content was more often original, educational and consistently published than viral.
Counterevidence: LinkedIn’s effect was measured as citation frequency, not transaction lift, and the sample skewed toward professional/business categories.
Interpretation: entity legibility may be reinforced by authoritative professional identity pages even without viral reach.

---

## 5. FAILED / NULL EXPERIMENTS

### HARD NULL: Reddit-first shopping visibility strategy for ChatGPT
FoundGPT observed **0 Reddit citations in 58,846 ChatGPT shopping citations**. That is not proof Reddit can never influence model knowledge indirectly, but it is a strong null against spending scarce commerce-discovery effort on Reddit solely to earn ChatGPT shopping citations.

### MEASUREMENT NULL: Citation count as recommendation proxy
Semrush found 61.7% of citations were ghost citations. Therefore “our citation count rose” is not sufficient evidence that users saw or were recommended the brand.

### NON-CAUSAL WARNING: Structured/product depth correlation
FoundGPT reports that its best-performing independent stores shared complete structured data, substantive product pages and buying-guide content. This is descriptive, not a controlled intervention result. Do not convert this into “schema caused 10× visibility.”

---

## 6. WHO TO WATCH NEXT

- **Rahul / FoundGPT** — unusually close to live Shopify AI visibility: 111 stores, 23k+ real AI-search checks, ~99k structured-data fixes. Highest-value follow-up is a controlled before/after intervention dataset tied to citations, sessions and orders.
- **Kevin Indig / Growth Memo** — useful because he is separating mentions from citations and designing cross-engine measurement rather than treating AI visibility as one metric.
- **Margarita Loktionova / Semrush research** — transparent prompt-scale studies across engines and source surfaces; useful for engine-specific source-family shifts.
- **LinkedIn + Semrush joint research** — relevant for B2B/provider discovery where public professional identity may act as entity corroboration.

---

## 7. HYPOTHESIS LEDGER

### H1 — For shopping queries, deep commerce pages are first-class retrieval sources and can outperform larger domains when query-product fit is high.
H0: large authority domains/marketplaces dominate regardless of niche relevance.
Evidence for: two independent Shopify stores earned 255/241 ChatGPT citations within tracked niches vs Amazon 22; 67.5% of shopping citations were commerce pages.
Evidence against: marketplaces still own 52.8% of citation share overall; large editorial sites can dominate specific query classes.
Belief delta: FOR.
Falsifier: a replicated multi-category corpus showing small-store citations disappear after controlling for prompt set, brand/store inclusion bias and category.
Next best test: 100 neutral prompts across 10 categories where tracked merchants are not seeded into the prompt-generation process; compare niche-store vs marketplace citation share.

### H2 — The optimal off-site corroboration source is engine- and query-class-specific.
H0: one universal external authority graph drives recommendation across engines.
Evidence for: Reddit 0% on ChatGPT shopping vs 3.4% AI Mode and 5.5% Perplexity; LinkedIn citation incidence varies by engine.
Evidence against: there may still be common upstream indexing/search factors not visible in final citations.
Belief delta: STRONGLY_FOR.
Falsifier: controlled intervention on the same brand/source showing similar recommendation lift across all engines despite different visible citation families.
Next best test: publish matched evidence on YouTube, Reddit, LinkedIn, specialist editorial and own-site pages for the same entity; track engine-specific inclusion probability over 6 weeks.

### H3 — Named recommendation rate is economically more informative than citation rate.
H0: citation rate is an adequate proxy because citations strongly co-move with brand selection and clicks.
Evidence for: 61.7% ghost citations; ChatGPT 87% citation vs 20.7% mention in Semrush sample.
Evidence against: no conversion dataset attached to the ghost-citation study.
Belief delta: FOR.
Falsifier: merchant-level data showing citation share predicts clicks/conversions as well as named recommendation share.
Next best test: connect prompt-level citation + mention + recommendation position to tagged merchant sessions/orders.

### H4 — Professional identity surfaces can act as entity-definition infrastructure for B2B/provider answers.
H0: LinkedIn citation is incidental to traditional index authority and provides no unique entity-discovery value.
Evidence for: LinkedIn was #2 cited domain in Semrush’s dataset, appearing in 11% of responses; cited content had high semantic similarity with generated answers.
Evidence against: correlation, not causal; platform/category skew.
Belief delta: NEUTRAL→FOR.
Falsifier: controlled entity pages with/without strong LinkedIn presence showing no difference in B2B recommendation probability.
Next best test: 30 low-authority B2B brands matched by website/search strength, stratified by LinkedIn corpus richness; measure recommendation probability across engines.

---

## 8. NOVELTY AUDIT

### Previous-run themes reconstructed
Prior two reports already covered:
- AI referral attribution undercounting / dark traffic.
- AI visitors converting above baseline and skewing toward first-time buyers.
- Shopify catalog/feed/indexing as parallel discovery routes.
- Generic JSON-LD/schema as a citation null.
- llms.txt low/no usage.
- marketplace concentration in AI referrals.
- broad external corroboration / citations.
- ChatGPT shopping selection instability.

### Genuinely new this run
- Citation vs named-brand recommendation split (“ghost citations”).
- Engine-specific inversion: ChatGPT citation-heavy vs Gemini mention-heavy.
- Shopping-specific source composition at 207k-citation scale.
- Hard Reddit null for ChatGPT shopping prompts.
- Independent niche Shopify stores out-citing Amazon inside their own prompt set.
- LinkedIn as a major cited professional-identity surface with content-format and posting-pattern data.

### Semantic duplicates rejected
- Similarweb marketplace referral concentration: already central in previous run.
- Ethercycle AI conversion/first-time-buyer data: already reported.
- Ahrefs schema null: already reported.
- generic “AI traffic converts better” studies: rejected as duplicate and non-mechanistic.
- generic llms.txt advice: rejected due previous null evidence and lack of new implementation outcome.

Estimated substantive novelty: **~80%**.
At least half of accepted records involve newly covered people/entities/source studies.

---

## 9. SOURCE-YIELD LEDGER

| Source family | Reads | Accepted records | Material belief changes |
|---|---:|---:|---:|
| Primary ecommerce AI-visibility operator datasets | 2 | 2 | 2 |
| Search/AI visibility research datasets | 3 | 2 | 2 |
| Reddit operator threads | 3 | 0 | 0 |
| Generic AI-search/SEO blogs | 8+ | 0 | 0 |
| Platform docs / announcements | 3 | 0 | 0 |
| Similarweb current data | 2 | 0 this run | 0 (mostly duplicate) |

Highest-yield family this run: **operator-owned live prompt/citation datasets tied to real merchant cohorts**.

---

## 10. JSONL

```jsonl
{"record_id":"ADA-20260907-01","probe":"agent_discovery_alpha","observed_at":"2026-09-07T19:38:00+07:00","country":"GLOBAL","market_or_entity":"ChatGPT shopping citations / Shopify merchants","person_or_company":"FoundGPT / Rahul","role":"Founder and operator of Shopify AI-visibility platform","source_type":"blog","source_url":"https://foundgpt.app/blog/where-chatgpt-sends-shoppers","published_at":"2026-08-09","palace_proximity_score":82,"evidence_grade":"B","verbatim_excerpt":"Two-thirds are commerce pages; independent stores out-cite Amazon 10×.","detailed_claim":"FoundGPT tracked 3,601 buyer-decision prompts for 107 Shopify stores between Apr 19 and Aug 9 2026, recording 58,846 ChatGPT citations. Retailer/marketplace pages were 52.8% and brand/store sites 14.7%, for 67.5% commerce-page share. Two independent stores received 255 and 241 citations within their tracked niche prompts versus 22 for amazon.com.","quantitative_claims":[{"metric":"ChatGPT shopping citations","value":"58846","denominator":"3601 buyer-decision prompts / 107 Shopify stores","timeframe":"2026-04-19 to 2026-08-09","caveat":"Descriptive, not causal; merchant/prompt mix reflects FoundGPT cohort"},{"metric":"commerce-page citation share","value":"67.5%","denominator":"58846 citations","timeframe":"same","caveat":"52.8% retailer/marketplace + 14.7% brand/store"},{"metric":"independent-store citations vs Amazon","value":"255 and 241 vs 22","denominator":"tracked niche prompts","timeframe":"same","caveat":"Prompt-set and cohort selection may advantage tracked merchants"}],"state_before":"Generic industry belief that large marketplaces/authority domains dominate AI shopping citations","action_taken":"UNKNOWN","observed_agent_behavior":"ChatGPT cited deep commerce/product/store pages heavily and sometimes cited niche independent stores more often than Amazon","outcome":"Evidence that niche relevance plus useful commerce pages can earn direct shopping citations","time_horizon":"4 months","mechanism":"Query-product fit and extractable deep commerce pages appear to be first-class retrieval sources","moat_implication":"Owned product/compatibility/buying-guide pages may be more defensible than generic GEO tactics if they encode uniquely useful decision data","h1":"For shopping queries, deep commerce pages can outperform larger domains when query-product fit is high","h0":"Large authority domains and marketplaces dominate regardless of niche relevance","falsifier":"Neutral multi-category prompt corpus shows independent-store advantage disappears when prompt/cohort selection is controlled","belief_delta":"FOR","next_best_test":"Run 100 neutral prompts across 10 categories with unseeded prompt construction and compare niche-store vs marketplace citation probability","novelty_reason":"Prior reports covered marketplace concentration but not a large shopping-citation corpus showing direct commerce-page dominance and niche-store outperformance","independence_cluster":"foundgpt_shopping_citation_corpus"}
{"record_id":"ADA-20260907-02","probe":"agent_discovery_alpha","observed_at":"2026-09-07T19:38:00+07:00","country":"GLOBAL","market_or_entity":"Cross-engine shopping source composition","person_or_company":"FoundGPT / Rahul","role":"Founder and operator of Shopify AI-visibility platform","source_type":"blog","source_url":"https://foundgpt.app/blog/reddit-ai-search-shopping-study","published_at":"2026-08-09","palace_proximity_score":82,"evidence_grade":"B","verbatim_excerpt":"ChatGPT cited Reddit exactly zero times in our corpus.","detailed_claim":"FoundGPT analyzed 207,297 shopping citation instances from 107 Shopify stores across five AI engines. Reddit represented 1,032 citations / 0.5% overall and 0 of 58,846 ChatGPT citations, while Google AI Mode cited Reddit 578/17,145 and Perplexity 453/8,190. YouTube was the leading community source across engines.","quantitative_claims":[{"metric":"Reddit share of all shopping citations","value":"0.5%","denominator":"207297 citations","timeframe":"2026-04-19 to 2026-08-09","caveat":"Merchant niches skew cycling/books/fashion/outdoor/wellness"},{"metric":"ChatGPT Reddit citations","value":"0","denominator":"58846 ChatGPT shopping citations","timeframe":"same","caveat":"Final visible citations do not capture latent training or uncited influence"},{"metric":"Google AI Mode Reddit share","value":"3.4%","denominator":"17145 citations","timeframe":"same","caveat":"Descriptive"},{"metric":"Perplexity Reddit share","value":"5.5%","denominator":"8190 citations","timeframe":"same","caveat":"Descriptive"}],"state_before":"Common GEO guidance that Reddit is broadly important across AI discovery","action_taken":"UNKNOWN","observed_agent_behavior":"Shopping-source composition differed sharply by engine; ChatGPT ignored Reddit in visible citations while AI Mode/Perplexity used it modestly","outcome":"Generic Reddit-first commerce visibility thesis strongly weakened","time_horizon":"4 months","mechanism":"Retrieval/source preference is conditional on query class and engine","moat_implication":"A merchant should build source presence matched to the engine/query graph rather than universal off-site distribution","h1":"The optimal external corroboration source is engine- and query-class-specific","h0":"One universal authority graph drives recommendation across engines","falsifier":"Matched cross-surface interventions produce similar recommendation lift across engines despite different visible source families","belief_delta":"STRONGLY_FOR","next_best_test":"Publish matched evidence on Reddit, YouTube, LinkedIn, specialist editorial and own-site pages for the same entities and track engine-specific recommendation probability","novelty_reason":"New shopping-specific hard null that contradicts generic Reddit-centric AI-search advice","independence_cluster":"foundgpt_cross_engine_source_mix"}
{"record_id":"ADA-20260907-03","probe":"agent_discovery_alpha","observed_at":"2026-09-07T19:38:00+07:00","country":"GLOBAL","market_or_entity":"AI citation vs brand mention behavior","person_or_company":"Semrush / Kevin Indig","role":"AI visibility research team / growth advisor","source_type":"blog","source_url":"https://www.semrush.com/blog/the-ghost-citations-study/","published_at":"2026-06-09","palace_proximity_score":58,"evidence_grade":"B","verbatim_excerpt":"62% of AI citations are ghost citations.","detailed_claim":"Semrush and Kevin Indig logged 3,981 domain appearances for 115 prompts across 14 countries and ChatGPT, Google AI Overviews, Gemini and Google AI Mode. 61.7% of appearances were citation without brand mention, 13.2% both cited and mentioned, and 25.1% mention without citation. ChatGPT cited brands in 87% of appearances but named them in only 20.7%; Gemini named brands in 83.7% but cited in 21.4%.","quantitative_claims":[{"metric":"ghost citation share","value":"61.7%","denominator":"3981 domain appearances","timeframe":"study published 2026-06-09","caveat":"115 prompts only"},{"metric":"ChatGPT citation vs mention rate","value":"87% citation / 20.7% mention","denominator":"study appearances","timeframe":"same","caveat":"Prompt composition may affect ratios"},{"metric":"Gemini citation vs mention rate","value":"21.4% citation / 83.7% mention","denominator":"study appearances","timeframe":"same","caveat":"Prompt composition may affect ratios"}],"state_before":"Citation share commonly used as proxy for AI brand visibility","action_taken":"Cross-engine prompt logging and classification of source citation vs explicit brand name","observed_agent_behavior":"Engines frequently used sources without naming brands, or named brands without linking their sites","outcome":"Citation and recommendation visibility shown to be distinct measurable states","time_horizon":"UNKNOWN","mechanism":"Retrieval attribution and entity selection are separate stages","moat_implication":"Measurement systems that only track citations can optimize the wrong target; recommendation-slot data is more strategically valuable","h1":"Named recommendation rate is economically more informative than citation rate","h0":"Citation rate is an adequate proxy because citations strongly co-move with recommendation and clicks","falsifier":"Merchant-level prompt-to-order data shows citation share predicts clicks/conversions as well as named recommendation share","belief_delta":"FOR","next_best_test":"Join prompt-level citation, mention and recommendation-position logs to merchant session/order attribution","novelty_reason":"Prior reports tracked citations and traffic but did not separate citation from explicit entity recommendation","independence_cluster":"semrush_ghost_citations"}
{"record_id":"ADA-20260907-04","probe":"agent_discovery_alpha","observed_at":"2026-09-07T19:38:00+07:00","country":"GLOBAL","market_or_entity":"LinkedIn as professional/B2B AI source surface","person_or_company":"Semrush / LinkedIn","role":"Search intelligence research collaboration","source_type":"blog","source_url":"https://www.semrush.com/blog/linkedin-ai-visibility-study/","published_at":"2026-03-10","palace_proximity_score":58,"evidence_grade":"B","verbatim_excerpt":"LinkedIn is second in citations on ChatGPT Search, Google AI Mode, and Perplexity for our dataset.","detailed_claim":"Semrush analyzed 325,000 unique prompts across ChatGPT Search, Google AI Mode and Perplexity, then studied 89,000 unique LinkedIn URLs with LinkedIn-provided metadata. LinkedIn appeared in 11% of AI responses on average, 14.3% on ChatGPT Search, 13.5% on Google AI Mode and 5.3% on Perplexity. Original educational content and active authors were more common among cited URLs than viral/reshares.","quantitative_claims":[{"metric":"prompt sample","value":"325000","denominator":"three AI search tools","timeframe":"2026-01 to 2026-02","caveat":"Industry mix includes strong technology/business/finance/industrial representation"},{"metric":"LinkedIn URLs analyzed","value":"89000","denominator":"cited LinkedIn URLs","timeframe":"same","caveat":"Citation corpus, not causal intervention"},{"metric":"LinkedIn citation incidence","value":"11% average; ChatGPT 14.3%; AI Mode 13.5%; Perplexity 5.3%","denominator":"AI responses in sample","timeframe":"same","caveat":"Category mix matters"}],"state_before":"Professional social content treated mainly as human awareness/brand channel","action_taken":"Cross-engine prompt sampling and citation analysis with LinkedIn content metadata","observed_agent_behavior":"AI systems frequently cited original LinkedIn articles/posts, especially in professional categories","outcome":"Evidence that professional identity/content surfaces can contribute directly to answer construction","time_horizon":"2-month sampling window","mechanism":"Indexable professional identity and educational content can act as retrievable entity/context evidence","moat_implication":"For B2B/provider discovery, a rich public identity graph may improve legibility even without high virality","h1":"Professional identity surfaces can act as entity-definition infrastructure for B2B/provider answers","h0":"LinkedIn citation is incidental to traditional authority and adds no unique discovery value","falsifier":"Matched brands with and without substantive LinkedIn corpora show no difference in B2B recommendation probability after controlling for web authority","belief_delta":"FOR","next_best_test":"Match 30 low-authority B2B brands by website/search strength, stratify by LinkedIn corpus richness, then benchmark recommendation probability across engines","novelty_reason":"New source-family evidence on B2B/professional entity construction, absent from prior runs","independence_cluster":"semrush_linkedin_citation_study"}
```

## Bottom line

The highest-value refinement from this run is:

**Do not optimize for “AI visibility” as one metric. Build a measurement ladder: eligible/retrieved → cited → entity named → recommended/shortlisted → clicked → converted. Then segment the entire ladder by engine and query class.**

The current evidence specifically rejects two dangerous shortcuts: **(1) citation count = recommendation, and (2) Reddit/community authority transfers uniformly into shopping discovery.**
