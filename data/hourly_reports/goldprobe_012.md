# Gold Probe — Agent Discovery Alpha — 2026-09-07 17:35 Asia/Phnom_Penh

Date: Mon, 7 Sep 2026 06:38:33 -0400

# Gold Probe — Agent Discovery Alpha — 2026-09-07 17:35

## 1. EXECUTIVE ALPHA

This first run found six field-grade signals that materially sharpen the agent-discovery thesis.

**1) AI commerce is real, but referral analytics systematically under-measures it.** Ethercycle analyzed 24 months across 10 established Shopify stores: 94M sessions, $274M revenue, 2.2M orders. In 2026 YTD AI assistants were still only 0.10% of sessions and revenue, but AI sessions grew 6x YoY, converted 2.66% vs 1.91% portfolio average, and 85% of AI-referred revenue came from first-time buyers. Panda Patches independently found AI assistants produced 63 orders / $16,783.76 / 6.2% of revenue, but explicitly says the result only appears because it combines surviving referrer data with a post-purchase “how did you hear about us?” field. This strongly supports an attribution-blindness mechanism: many stores may be measuring AI worse rather than receiving no AI demand.

**2) Shopify is turning product data itself into the distribution surface.** Shopify says Q1 2026 orders from AI referrals were nearly 13x Q1 2025. Its 2026 product-discovery guidance emphasizes product titles, galleries, alt text and structured product information, while Shopify Catalog now acts as a product index used by AI shopping surfaces. This is not evidence that “schema ranks you,” but it is direct platform evidence that machine-readable catalog quality determines eligibility and product comprehension inside Shopify’s agentic distribution layer.

**3) Generic schema is NOT a universal citation lever.** Ahrefs tracked 1,885 pages that added JSON-LD, matched against 4,000 controls. ChatGPT citations moved +2.2% and Google AI Mode +2.4%, both statistically indistinguishable from zero; AI Overviews declined 4.6%. This is one of the highest-value null results in the field. Structured data may be necessary for product/entity legibility in commerce systems, but adding schema to already-visible pages does not automatically increase citation frequency.

**4) llms.txt is currently almost useless for AI-search visibility.** Ahrefs analyzed server logs from 137,210 domains. Of roughly 38,000 valid llms.txt files, 97% received zero requests in May 2026; only 19.5% of requests to the tiny minority that were fetched came from named AI bots. This directly falsifies the common “publish llms.txt to show up in ChatGPT” tactic for normal commerce sites.

**5) ChatGPT Shopping behaves more like probabilistic offer selection than a stable SERP.** Profound measured 22.5M buy offers over ten days. Roughly 95% of product titles appeared in fewer than 30% of repeated runs for the same prompt, and only 0.5% reached 70%+ consistency. The moat cannot be “rank #1 in ChatGPT Shopping” in the Google sense. More plausible targets are eligibility, product-entity quality, retailer inclusion, offer freshness and repeated selection probability.

**6) External corroboration appears structurally important, but causal evidence is still weak.** Aleyda Solís’ cross-vertical citation analysis found external domains represented 69.6%–82.3% of top cited source mixes, with marketplaces/competitors especially important in ecommerce. This strongly suggests the “best factual entity about the transaction” may need to exist across the wider web, not only the merchant’s own domain. However, this is observational; it does not yet establish that creating third-party mentions causes recommendation lift.

## 2. FIELD EVIDENCE TABLE

| Rank | Source / person | Palace proximity | New evidence | Decision impact |
|---|---|---:|---|---|
| 1 | Kurt Elster / Ethercycle | 88 | 94M sessions / $274M / 10 Shopify stores; AI converts above portfolio average but remains only 0.10% of 2026 YTD sessions/revenue | High — establishes true channel scale + conversion + new-customer mix |
| 2 | Panda Patches / Hassan Jamal | 92 | 63 AI-attributed orders / $16,783.76; ChatGPT 4.3% of revenue; attribution requires self-report + referrer | Very high — measurement architecture changes interpretation of AI revenue |
| 3 | Ahrefs / Xibeijia Guan + Louise Linehan | 85 | 1,885-page schema quasi-experiment; 137K-domain llms.txt log study | Very high — hard nulls against two popular tactics |
| 4 | Shopify platform team | 96 | AI-referral orders nearly 13x YoY in Q1 2026; Catalog is now agent-facing product index | Very high — primary platform distribution mechanics |
| 5 | Profound | 82 | 22.5M ChatGPT Shopping buy offers; extreme repeat-run instability | High — changes optimization target from rank to inclusion/selection probability |
| 6 | Aleyda Solís | 58 | External domains = 69.6%–82.3% of top citation mix across verticals | Medium-high — supports off-site corroboration hypothesis but is not causal |

## 3. EXACT WORDS

**Kurt Elster / Ethercycle** — direct Shopify analytics research:
> “AI referrals are new customers.”
Context: 85% of AI-referred revenue across the 24-month dataset came from first-time buyers.
Source: https://ethercycle.com/pages/state-of-ecommerce-2026

**Panda Patches / Hassan Jamal** — first-hand merchant attribution:
> “Most businesses are not seeing less AI traffic than we are. They are measuring it worse.”
Source: https://www.pandacodegen.com/blog/ai-referral-revenue-2026

**Ahrefs** — server-log study:
> “97% of those files received zero traffic in May 2026.”
Source: https://ahrefs.com/blog/llmstxt-study/

**Ahrefs** — schema intervention study:
> “Adding schema didn't boost citations on any platform.”
Source: https://ahrefs.com/blog/schema-ai-citations/

**Profound** — repeated ChatGPT Shopping runs:
> “This isn't Google SEO, where you rank and hold.”
Source: https://www.tryprofound.com/blog/chatgpt-retail-target-walmart

## 4. MECHANISMS

### M1 — Attribution blindness
Observed mechanism: AI assistant → user learns brand/product → referrer stripped / app handoff / later direct navigation → conversion lands in Direct/Unknown unless source is collected elsewhere.
Evidence for: Panda Patches explicitly combines surviving referrer + customer self-report; Shopify community operators report referrer gaps.
Implication: “AI share of revenue” should be measured as a lower bound unless post-purchase/source-question or first-party identity stitching exists.

### M2 — Eligibility / entity legibility ≠ citation ranking
Observed mechanism: catalog/structured product data gives machines an unambiguous product identity, price, availability, variants and attributes. This can make a product eligible to be surfaced. But generic schema additions to pages already being cited did not increase ChatGPT citations materially in Ahrefs’ controlled study.
Implication: treat structured product data as an eligibility/comprehension primitive, not a magic citation booster.

### M3 — Probabilistic selection surface
Observed mechanism: repeated identical shopping prompts produce highly variable product-card sets.
Implication: optimize for probability of inclusion across query families and for correct offer/entity matching, not stable ordinal “rank.”

### M4 — External corroboration / distributed entity
Observed mechanism: AI answers cite external domains heavily; ecommerce appears especially exposed to marketplaces, competitor pages, comparison sources and reviews.
Implication: the defensible asset may be broad factual entity consistency across multiple independent sources rather than ownership of one perfectly optimized PDP.
Counterevidence: causal lift from intentionally adding third-party corroboration remains unproven.

## 5. FAILED / NULL EXPERIMENTS

### llms.txt — effectively null for normal AI-search visibility
Dataset: 137,210 domains in Ahrefs Web Analytics; ~38,000 valid llms.txt files.
Outcome: 97% got no requests in May 2026.
Decision: do not allocate meaningful GeoDrop engineering effort to llms.txt for discovery today. Cheap auto-generation is fine; it is not a moat.

### Schema added to already-visible pages — near-null
Dataset: 1,885 pages adding JSON-LD vs 4,000 controls.
Outcome: ChatGPT +2.2%, AI Mode +2.4% — statistically indistinguishable from zero; AIO -4.6%.
Decision: schema is not sufficient as an “AI ranking” intervention. Test it specifically on previously ineligible / poorly specified product entities instead.

## 6. WHO TO WATCH NEXT

1. **Xibeijia Guan — Ahrefs data scientist.** High-value because she is sitting on cross-site server logs and controlled page datasets capable of killing bad GEO assumptions.
2. **Louise Linehan — Ahrefs research author.** Publishes unusually strong negative-result AI search studies.
3. **Profound research team.** Their repeated-prompt / product-offer datasets expose the stochastic mechanics of actual ChatGPT Shopping selection.
4. **Hassan Jamal / Panda Patches.** Rare merchant/operator publishing order-level AI attribution and measurement methodology.
5. **Shopify Catalog / Agentic product engineering team.** Direct control over one of the largest machine-readable product graphs; watch for eligibility, ranking and source-selection disclosures.
6. **Merchants instrumenting post-purchase source attribution.** This is currently a more valuable class of source than generic “AI traffic” dashboards.

## 7. HYPOTHESIS LEDGER

### H-ADA-001 — AI referral share is materially undercounted by referrer-only analytics
H1: referrer-only GA4/Shopify reporting systematically understates agent-assisted commerce.
H0: self-reported source attribution materially overstates AI influence through recall/selection bias.
Evidence for: Panda Patches; Shopify community reports of missing referrers.
Falsifier: stores with robust first-party identity stitching show AI-assisted share close to raw referrer share.
Belief delta: STRONGLY_FOR.
Next best test: find 5-10 merchants with both post-purchase source survey and referrer data and calculate undercount ratio.

### H-ADA-002 — Machine-readable product completeness is an eligibility layer, not a direct ranking lever
H1: complete product identity/offer/availability data increases probability of being considered by agent commerce systems, while generic schema on already-known pages has little ranking effect.
H0: traditional index authority/content signals dominate and structured product data adds negligible marginal value.
Evidence for: Shopify Catalog architecture/guidance; Ahrefs null on already-visible pages is consistent with eligibility-vs-ranking distinction.
Falsifier: controlled test on previously incomplete product pages shows no increase in agent shopping eligibility/retrieval after product-data completion.
Belief delta: FOR.
Next best test: locate controlled PDP-level before/after cases where only product identifiers/offer/availability were repaired.

### H-ADA-003 — ChatGPT Shopping optimization is a probability-of-selection problem
H1: product-card visibility is stochastic enough that stable rank is the wrong objective; merchant/product eligibility and repeated inclusion rate are the meaningful metrics.
H0: underlying stable ranking exists but title normalization / measurement artifacts make it look random.
Evidence for: Profound 22.5M buy-offer repeated-run dataset.
Falsifier: normalized entity-level analysis shows stable ordering/inclusion after deduplicating title variants.
Belief delta: FOR.
Next best test: inspect Profound’s entity-normalized consistency methodology or independent repeated-prompt dataset.

### H-ADA-004 — Third-party corroboration is a major recommendation-selection signal
H1: consistent entity claims across marketplaces/reviews/comparison/community sources increase recommendation probability.
H0: external citation share simply reflects where answer engines retrieve information and does not causally improve merchant selection.
Evidence for: Aleyda external-source citation mix.
Falsifier: natural experiment where third-party corroboration materially changes without recommendation/citation change, or first-party-only merchants perform similarly after controlling for authority/search rank.
Belief delta: FOR, LOW-MODERATE CAUSAL CONFIDENCE.
Next best test: find brand-level before/after third-party citation acquisition with stable on-site content.

## 8. NOVELTY AUDIT

No prior `Gold Probe — Agent Discovery Alpha` emails were found; this is the baseline run. All six accepted evidence clusters are therefore novel to this series.

Rejected as low-signal / non-primary:
- generic GEO/AEO listicles repeating Adobe/Shopify numbers;
- composite case studies with unverifiable brand identity;
- claims that schema causes 3x citations without a credible causal design;
- claims that llms.txt boosts AI visibility unsupported by server logs;
- secondary articles merely restating Profound/Ahrefs/Shopify findings.

## 9. SOURCE-YIELD LEDGER

| Source family | Reads/searches | Accepted | Material belief changes |
|---|---:|---:|---:|
| Operator / merchant analytics | 4 | 2 | 2 |
| Platform official / Shopify | 4 | 1 | 1 |
| Primary large-scale research | 5 | 2 | 3 |
| Specialist AI-search researchers | 3 | 1 | 1 |
| Reddit / community | 4 | 0 primary records | 0; useful only for discovery leads |
| Generic SEO/GEO blogs | 8+ | 0 | 0 |

Recommendation next run: exploit merchant attribution datasets + platform engineers; search more X/Substack/HN/GitHub for first-hand product-visibility interventions. Deprioritize generic GEO blogs.

## 10. JSONL

```jsonl
{"record_id":"ADA-20260907-001","probe":"agent_discovery_alpha","observed_at":"2026-09-07T17:35:00+07:00","country":"GLOBAL","market_or_entity":"Shopify ecommerce AI referrals","person_or_company":"Ethercycle / Kurt Elster","role":"Shopify operator and researcher","source_type":"blog","source_url":"https://ethercycle.com/pages/state-of-ecommerce-2026","published_at":"2026-08","palace_proximity_score":88,"evidence_grade":"A","verbatim_excerpt":"AI referrals are new customers.","detailed_claim":"Across 10 established Shopify stores covering 94M sessions, $274M revenue and 2.2M orders, AI assistants were 0.10% of sessions and revenue in 2026 YTD but sessions grew 6x YoY; AI visitors converted 2.66% vs a 1.91% portfolio average and 85% of AI-referred revenue came from first-time buyers.","quantitative_claims":[{"metric":"AI referral session share","value":"0.10%","denominator":"2026 YTD portfolio sessions","timeframe":"Jan-Jun 2026","caveat":"referrer-based attribution can undercount agent-assisted journeys"},{"metric":"AI visitor conversion","value":"2.66% vs 1.91%","denominator":"Shopify session conversion","timeframe":"24 months","caveat":"10-store established-Shopify portfolio"},{"metric":"first-time buyer revenue share","value":"85%","denominator":"AI-referred revenue","timeframe":"24 months","caveat":"portfolio-specific"}],"state_before":"UNKNOWN","action_taken":"Portfolio-level analytics measurement","observed_agent_behavior":"AI-referred users arrive pre-qualified and disproportionately new","outcome":"Higher conversion than portfolio average but tiny current volume","time_horizon":"24 months","mechanism":"AI assistants pre-qualify shoppers before click","moat_implication":"Measure agent referral as acquisition channel and optimize considered-purchase decision data","h1":"AI referrals are low-volume but high-intent acquisition traffic","h0":"Observed conversion lift is portfolio/category selection bias","falsifier":"Large matched portfolio shows no conversion/new-customer lift after controlling category and attribution","belief_delta":"FOR","next_best_test":"Find category-matched datasets with first-party attribution","novelty_reason":"Baseline high-scale operator dataset","independence_cluster":"ethercycle-10-shopify-stores"}
{"record_id":"ADA-20260907-002","probe":"agent_discovery_alpha","observed_at":"2026-09-07T17:35:00+07:00","country":"GLOBAL","market_or_entity":"Panda Patches AI-attributed ecommerce revenue","person_or_company":"Panda Patches / Hassan Jamal","role":"Store operator / co-founder","source_type":"blog","source_url":"https://www.pandacodegen.com/blog/ai-referral-revenue-2026","published_at":"2026-08-18","palace_proximity_score":92,"evidence_grade":"A","verbatim_excerpt":"Most businesses are not seeing less AI traffic than we are. They are measuring it worse.","detailed_claim":"From Mar 1-Aug 18 2026, the store recorded 760 orders / $271,620.61 revenue; AI assistants generated 63 orders / $16,783.76 (6.2%), ChatGPT alone 51 orders / $11,614.78 (4.3%). Attribution combined surviving referrers with a customer source question because AI referrals frequently disappear into Direct/Unknown.","quantitative_claims":[{"metric":"AI-attributed revenue share","value":"6.2%","denominator":"$271,620.61 total revenue","timeframe":"2026-03-01 to 2026-08-18","caveat":"single store; attribution includes self-reported source"},{"metric":"ChatGPT revenue share","value":"4.3%","denominator":"total revenue","timeframe":"same window","caveat":"single store"}],"state_before":"Referrer-only analytics would undercount","action_taken":"Combined referrer tracking with customer source-question capture","observed_agent_behavior":"AI-assisted demand frequently arrives without durable referrer","outcome":"Material AI revenue becomes visible in attribution","time_horizon":"~5.5 months","mechanism":"Cross-device/app/direct navigation breaks referrer attribution","moat_implication":"Agent-commerce measurement stack is itself infrastructure; post-purchase source capture is high value","h1":"Referrer-only analytics materially undercounts AI-assisted commerce","h0":"Customer self-report overattributes AI due recall bias","falsifier":"Identity-stitched stores show little gap between referrer-only and assisted attribution","belief_delta":"STRONGLY_FOR","next_best_test":"Compare referrer vs post-purchase survey across multiple stores","novelty_reason":"Rare order-level first-hand attribution dataset","independence_cluster":"panda-patches-store"}
{"record_id":"ADA-20260907-003","probe":"agent_discovery_alpha","observed_at":"2026-09-07T17:35:00+07:00","country":"GLOBAL","market_or_entity":"Schema markup and AI citations","person_or_company":"Ahrefs / Xibeijia Guan / Louise Linehan","role":"Data science / research","source_type":"blog","source_url":"https://ahrefs.com/blog/schema-ai-citations/","published_at":"2026-05-11","palace_proximity_score":85,"evidence_grade":"A","verbatim_excerpt":"Adding schema didn't boost citations on any platform.","detailed_claim":"Ahrefs tracked 1,885 pages adding JSON-LD between Aug 2025 and Mar 2026 against 4,000 matched controls. ChatGPT +2.2% and AI Mode +2.4% were statistically indistinguishable from zero; AIO -4.6% relative to controls.","quantitative_claims":[{"metric":"ChatGPT citation effect","value":"+2.2%","denominator":"1,885 treated pages vs 4,000 matched controls","timeframe":"Aug 2025-Mar 2026","caveat":"sample pages already had meaningful AI citation baselines"}],"state_before":"Pages already in AI consideration set","action_taken":"Added JSON-LD schema","observed_agent_behavior":"No material citation lift","outcome":"Null / near-null citation effect","time_horizon":"study observation window","mechanism":"Schema correlates with strong sites but does not necessarily cause citation lift once visibility already exists","moat_implication":"Do not treat generic schema as ranking moat; test entity eligibility/completeness instead","h1":"Schema alone materially raises AI citation frequency","h0":"Schema is mainly correlated with overall site quality / eligibility","falsifier":"Controlled previously-unmarked low-visibility pages show strong citation lift after schema-only intervention","belief_delta":"STRONGLY_AGAINST","next_best_test":"Find controlled product-PDP schema completion tests on previously ineligible pages","novelty_reason":"High-quality null causal study","independence_cluster":"ahrefs-schema-study"}
{"record_id":"ADA-20260907-004","probe":"agent_discovery_alpha","observed_at":"2026-09-07T17:35:00+07:00","country":"GLOBAL","market_or_entity":"llms.txt AI-search visibility","person_or_company":"Ahrefs / Xibeijia Guan / Louise Linehan","role":"Data science / research","source_type":"blog","source_url":"https://ahrefs.com/blog/llmstxt-study/","published_at":"2026-06-15","palace_proximity_score":85,"evidence_grade":"A","verbatim_excerpt":"97% of those files received zero traffic in May 2026.","detailed_claim":"Ahrefs analyzed 137,210 domains and server/bot logs. Roughly 38,000 published valid llms.txt; 97% received no requests at all in May 2026. Of requests to the minority fetched, 19.5% came from named AI bots.","quantitative_claims":[{"metric":"llms.txt zero-request rate","value":"97%","denominator":"~38,000 valid files","timeframe":"May 2026","caveat":"Ahrefs analytics customers skew technical/SEO-aware"}],"state_before":"Sites publish llms.txt expecting AI visibility","action_taken":"Publish llms.txt","observed_agent_behavior":"Majority of files never fetched","outcome":"No observable retrieval path for most sites","time_horizon":"May 2026","mechanism":"AI retrieval systems generally do not proactively discover llms.txt","moat_implication":"llms.txt is not a meaningful commerce-discovery moat today","h1":"llms.txt improves AI-search discoverability","h0":"Major AI retrieval systems ignore it unless explicitly directed","falsifier":"Major assistants begin systematically requesting llms.txt or controlled visibility tests show lift","belief_delta":"STRONGLY_AGAINST","next_best_test":"Monitor platform bot behavior quarterly, but spend near-zero engineering time now","novelty_reason":"Large server-log null result","independence_cluster":"ahrefs-llmstxt-study"}
{"record_id":"ADA-20260907-005","probe":"agent_discovery_alpha","observed_at":"2026-09-07T17:35:00+07:00","country":"GLOBAL","market_or_entity":"ChatGPT Shopping product offer selection","person_or_company":"Profound","role":"AI visibility research platform","source_type":"blog","source_url":"https://www.tryprofound.com/blog/chatgpt-retail-target-walmart","published_at":"2026-04","palace_proximity_score":82,"evidence_grade":"A","verbatim_excerpt":"This isn't Google SEO, where you rank and hold.","detailed_claim":"Profound measured retailer/product-card presence across 22.5M ChatGPT Shopping buy offers over ten days. About 95% of product titles appeared in fewer than 30% of repeated runs for the same prompt; only 0.5% appeared in 70%+ of runs.","quantitative_claims":[{"metric":"low repeat-run product-title consistency","value":"~95% below 30% consistency","denominator":"22.5M buy offers","timeframe":"2026-03-10 to 2026-03-20","caveat":"some variance may come from title-string normalization"}],"state_before":"Assumption of stable product ranking","action_taken":"Repeat identical shopping prompts at scale","observed_agent_behavior":"Highly variable product-card inclusion","outcome":"Stable rank is poor mental model","time_horizon":"10 days","mechanism":"Agent shopping surfaces probabilistically assemble candidate offers","moat_implication":"Optimize eligibility/entity matching/freshness/repeated selection probability rather than rank position","h1":"Agent shopping visibility is primarily probabilistic selection rather than stable rank","h0":"Underlying stable ranking is obscured by entity/title normalization artifacts","falsifier":"Entity-normalized repeated-run analysis reveals stable product ordering/inclusion","belief_delta":"FOR","next_best_test":"Seek independent entity-normalized repeated-prompt benchmark","novelty_reason":"Very large direct shopping-surface measurement","independence_cluster":"profound-chatgpt-shopping-22m"}
{"record_id":"ADA-20260907-006","probe":"agent_discovery_alpha","observed_at":"2026-09-07T17:35:00+07:00","country":"GLOBAL","market_or_entity":"Third-party citation mix","person_or_company":"Aleyda Solís","role":"AI search researcher / consultant","source_type":"blog","source_url":"https://www.aleydasolis.com/en/ai-search/third-party-citation-optimization-ai-search/","published_at":"2026-08","palace_proximity_score":58,"evidence_grade":"B","verbatim_excerpt":"external domains represented between 69.6% and 82.3% of the top cited source mix","detailed_claim":"Cross-vertical analysis found external domains dominate top citation mixes; for ecommerce, marketplaces and competitor domains were especially important external environments.","quantitative_claims":[{"metric":"external-domain share of top citations","value":"69.6%-82.3%","denominator":"top cited source mix across SaaS/ecommerce/finance","timeframe":"2026 study","caveat":"observational and vertical/platform dependent"}],"state_before":"Merchant assumes owned domain is primary entity surface","action_taken":"Observed citation composition across AI platforms/verticals","observed_agent_behavior":"AI answers cite substantial external-source mix","outcome":"Owned-domain-only optimization appears incomplete","time_horizon":"cross-sectional","mechanism":"Answer engines corroborate/assemble entities from third-party environments","moat_implication":"Distributed entity consistency and external factual corroboration may be important","h1":"Independent third-party corroboration raises recommendation probability","h0":"External citation share reflects retrieval availability but does not causally influence merchant selection","falsifier":"Controlled/natural experiments show third-party presence changes without recommendation probability changing","belief_delta":"FOR","next_best_test":"Find brand-level before/after external-citation acquisition with stable on-site state","novelty_reason":"Directly quantifies external-source dominance","independence_cluster":"aleyda-citation-analysis"}
```
