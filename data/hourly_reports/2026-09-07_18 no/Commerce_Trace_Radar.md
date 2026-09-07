# [Commerce Trace Radar] 2026-09-06 22:00 — 18 novel records

# Commerce Trace Radar — 18 accepted novel records

## Executive summary

This run deliberately stopped at 18 accepted records rather than padding to 20. The strongest new evidence is not generic campaign advice; it is state-transition evidence showing that ecommerce outcomes can break at the infrastructure layer before product-market fit is even being tested.

The highest-value cluster is Shopify→Google Merchant Center state corruption and relapse. In separate 2026 traces, routine SKU edits changed product identity and removed items, Merchant API migration reset Local Feed Partnership and duplicated a ~6,000-item catalog, manual recrawls temporarily cleared 'product page unavailable' errors before the count later jumped from 0 to ~400, and a backend restoration removed storefront ghost products but left GraphQL ghost data intact. These should become explicit SUPPLIER_ANOMALY / PLATFORM_STATE records in the market graph rather than being treated as ad-performance noise.

The second cluster isolates acquisition quality from site quality. A supplement-adjacent drink store reported 4.2% overall CVR and 3.6% paid-social CVR on the same page, yet Google produced 449 clicks, ~$650 spend and zero sales. Another established store with £300k+ historical Facebook revenue produced only 1 Google Shopping purchase from 260 clicks after a Max Clicks→Manual CPC transition. These are unusually useful because they weaken the default explanation 'the site just does not convert.'

The third cluster strengthens the foreign-market thesis. Norway shows concrete friction around VOEC thresholds, high shipping, retailer discovery and local postal integration. Finland shows hidden dropship fulfillment and last-mile carrier trust problems. This is exactly the kind of 'proven demand + mediocre merchant execution' negative space that should feed the transplant matrix.

Run stats: 18 accepted / 54 reviewed / 11 duplicates or near-duplicates skipped. Evidence: 7 A-grade and 11 B-grade.

## Top 3 highest-signal findings

### 1. Manual recrawl and site cleanup suppressed GMC page-unavailable errors, but the fault later relapsed from 0 to ~400 products.
- **Before:** Products gradually flagged product-page-unavailable despite 200 responses and no redirect issue
- **Action:** Manual recrawls; Shopify re-index request; disabled some web pixels; code cleanup
- **After:** Issue 'settled down dramatically' after remediation, then later jumped from 0 to ~400 affected products on Jun 3
- **Evidence grade:** A
- **Why it matters:** new recurrent pre/post/relapse trace
- **Source:** https://community.shopify.com/t/recurring-google-merchant-center-product-page-unavailable-issue-manual-recrawl-fixes-it-then-it-slowly-comes-back/599372

### 2. The identical product page converted on paid social but produced zero sales from 449 Google clicks, isolating traffic/acquisition quality as a major suspect.
- **Before:** Same store converts 4.2% overall and 3.6% from paid social on the same product page
- **Action:** Ran 4 Google campaigns on Maximize Clicks while validating search terms and paid attribution
- **After:** 3 weeks Google delivery: 449 clicks, ~$650 spend, $1.46 CPC, 0 paid-Google sales
- **Evidence grade:** B
- **Why it matters:** new cross-channel controlled landing-page contrast
- **Source:** https://www.reddit.com/r/googleads/comments/1vmswcs/zero_sales_on_450_clicks_but_paid_social_converts/

### 3. A Finnish retailer showed apparent immediate stock while fulfillment was actually supplier-direct, creating a visible stock/transparency gap.
- **Before:** Product appeared immediately available; chatbot reported 19 in stock
- **Action:** Customer ordered an item shown with many units and immediate availability, then queried support chatbot
- **After:** Order remained 'waiting for products'; chatbot disclosed it was a dropship product shipped from supplier and that this status was not clearly exposed to shoppers
- **Evidence grade:** B
- **Why it matters:** new native-language Finland merchant-quality gap
- **Source:** https://www.reddit.com/r/Suomi/comments/1rozo7l/verkkokauppacom_myy_tuotteita/

## Updated longitudinal / platform-state cases

- **CTR-20260906-2235-001** — Routine SKU edits were followed by product-ID churn and disappearing Shopping items; remediation only partially restored state. Source: https://community.shopify.com/t/checkout-intermittently-stops-working-mid-day-gmc-products-vanishing-without-reason-meta-pixel-misconnection-causing-months-of-structural-cv-decline-p-max-cpa-spiking-15x-overnight-2-months-of-platform-level-anomalies-i-cant-explain/592057
- **CTR-20260906-2235-002** — Merchant API migration temporarily cleaned a 6k-SKU feed, but a reset local-feed setting duplicated products and created fresh warnings. Source: https://community.shopify.com/t/removing-products-from-merchant-center-api/587986
- **CTR-20260906-2235-003** — Manual recrawl and site cleanup suppressed GMC page-unavailable errors, but the fault later relapsed from 0 to ~400 products. Source: https://community.shopify.com/t/recurring-google-merchant-center-product-page-unavailable-issue-manual-recrawl-fixes-it-then-it-slowly-comes-back/599372
- **CTR-20260906-2235-004** — A backend restoration cleaned the storefront but did not remove persistent ghost-product data from GraphQL reporting. Source: https://community.shopify.com/t/critical-backend-sync-failure-causing-6k-phantom-products-in-gmc-unresolved-since-december-gmc-suspension/583892?page=2
- **CTR-20260906-2235-005** — Two Swedish Standard Shopping launches delivered traffic and sales during learning, then both flatlined immediately after learning. Source: https://community.shopify.com/t/google-standard-shopping-gets-traffic-during-learning-then-drops-to-zero-impressions/622939

## Paid funnel / economics cases

- **CTR-20260906-2235-006** — The identical product page converted on paid social but produced zero sales from 449 Google clicks, isolating traffic/acquisition quality as a major suspect. Source: https://www.reddit.com/r/googleads/comments/1vmswcs/zero_sales_on_450_clicks_but_paid_social_converts/
- **CTR-20260906-2235-007** — A high-ticket Shopping campaign reached 335 clicks at falling CPC but still had zero purchases after ~12 days. Source: https://www.reddit.com/r/googleads/comments/1tubbou/high_ticket_ecommerce_335_clicks_and_no_sales/
- **CTR-20260906-2235-008** — A UK gaming-PC retailer spent £1,300 for 1,222 Shopping clicks without an attributed sale despite narrowing to popular products. Source: https://www.reddit.com/r/googleads/comments/1fclds9
- **CTR-20260906-2235-009** — Premium cosmetics generated 300 Shopping clicks from 67.6k impressions with zero purchases after ~$500 spend. Source: https://www.reddit.com/r/PPC/comments/1c4h5rd
- **CTR-20260906-2235-010** — An established Facebook-selling store reached only one Google Shopping purchase from 260 clicks after switching Max Clicks to Manual CPC. Source: https://www.reddit.com/r/PPC/comments/1ja6q1c
- **CTR-20260906-2235-011** — A New Zealand niche Shopping campaign produced 3 conversions in 2 days and ~10x ROAS while spending only 10-20% of budget. Source: https://www.reddit.com/r/PPC/comments/1l9g54n/great_roas_extremely_low_budget_consumption_what/
- **CTR-20260906-2235-012** — A broad electronics store using only organic/social/free-listing channels had no sales after its first month. Source: https://www.reddit.com/r/ShopifyeCommerce/comments/1mvryjd

## Foreign-market signals

- **NO / CTR-20260906-2235-013** — A VOEC-labelled cross-border order still produced ~NOK 3k-3.5k delivery-time charges when one item exceeded the per-item threshold. Source: https://www.reddit.com/r/Norway/comments/1ppo8rp/online_shopping_in_norway_what_happens_when_one/
- **FI / CTR-20260906-2235-014** — A Finnish retailer showed apparent immediate stock while fulfillment was actually supplier-direct, creating a visible stock/transparency gap. Source: https://www.reddit.com/r/Suomi/comments/1rozo7l/verkkokauppacom_myy_tuotteita/
- **NO / CTR-20260906-2235-015** — A Norway consumer explicitly reported weaker product discovery, selection, shipping economics and retailer trust than Germany. Source: https://www.reddit.com/r/Norway/comments/1mjh6ht/just_moved_to_norway_struggling_a_bit_with_online/
- **NO / CTR-20260906-2235-016** — A Norwegian micro-merchant abandoned Etsy over postage friction and reported a successful move to a local low-cost platform. Source: https://www.reddit.com/r/norge/comments/1vxre1m/nettbutikk_i_norge/
- **NO / CTR-20260906-2235-017** — Norwegian shopping discovery is visibly comparison-engine and specialist-store driven, with Prisjakt repeatedly acting as the market map. Source: https://www.reddit.com/r/Norway/comments/1k18gz7/where_do_norwegians_shop_online/
- **FI / CTR-20260906-2235-018** — A Finnish delivery failure thread shows last-mile carrier choice can directly damage trust even when the retailer/product is otherwise acceptable. Source: https://www.reddit.com/r/Finland/comments/1mixghm/ups_the_worst_delivery_service_in_the_world/

## Source-yield changes

- **Shopify Community 2026 sync/API threads:** HIGH for platform-state/action-outcome traces
- **r/googleads and r/PPC quantified threads:** HIGH for paid funnel economics
- **r/Norway + r/norge:** HIGH for country transplant friction/discovery topology
- **r/Suomi / r/Finland:** MEDIUM-HIGH for stock transparency and last-mile friction

## Compact accepted-record table

| ID | Grade | Market | Probe | Before → action → after |
|---|---:|---|---|---|
| CTR-20260906-2235-001 | A | JP/unknown | ACTION_OUTCOME/SUPPLIER_ANOMALY | Products present and serving normally before SKU edits → Added SKUs for the first time; later disabled continue-selling-when-OOS, re-added products through Google & YouTube, stopped automatic crawl source → Mar 10-14: up to 7 products disappeared from GMC; ... |
| CTR-20260906-2235-002 | A | unknown | ACTION_OUTCOME/SUPPLIER_ANOMALY | ~8,000 products with stale 404 items; reduced to ~6,000 SKUs and migrated feed → Migrated Shopify feed to Merchant API, then disabled unintended Local Feed Partnership → ~6,000 products approved, then all 6,000 showed warnings after local feed duplication; ... |
| CTR-20260906-2235-003 | A | unknown | ACTION_OUTCOME/SUPPLIER_ANOMALY | Products gradually flagged product-page-unavailable despite 200 responses and no redirect issue → Manual recrawls; Shopify re-index request; disabled some web pixels; code cleanup → Issue 'settled down dramatically' after remediation, then later jumped from... |
| CTR-20260906-2235-004 | A | unknown | ACTION_OUTCOME/SUPPLIER_ANOMALY | ~40 real products appeared as 6k+ phantom products after December issue → Community fix cleaned storefront; Shopify support performed backend restoration → Storefront ghost products resolved, but GraphQL reporting still contained December ghost products aft... |
| CTR-20260906-2235-005 | A | SE | NO_DELIVERY/ACTION_OUTCOME | During learning: 32.1k impressions, 318 clicks, 439 SEK spend and a few sales → Launched two separate Standard Shopping campaigns with ~2,600 approved products → Day after learning appeared to end: impressions/traffic dropped to almost nothing; pattern occu... |
| CTR-20260906-2235-006 | B | unknown | CLICKS_NO_ATC/HIDDEN_ECONOMICS | Same store converts 4.2% overall and 3.6% from paid social on the same product page → Ran 4 Google campaigns on Maximize Clicks while validating search terms and paid attribution → 3 weeks Google delivery: 449 clicks, ~$650 spend, $1.46 CPC, 0 paid-Google s... |
| CTR-20260906-2235-007 | B | unknown | CLICKS_NO_ATC/HIDDEN_ECONOMICS | New campaign → Launched Shopping May 20; continued testing as CPC drifted down → By Jun 1: 335 clicks, 0 sales; current-day CPC ~$0.39; products $260-$1,300 |
| CTR-20260906-2235-008 | B | GB | FAILURE_ATLAS/CLICKS_NO_ATC | Shopping section added Mar/Apr; broader repair site already established → Adjusted budgets, keywords and number of advertised products; narrowed to 3 most popular products → Since May: £1,300 spend, 578k impressions, 1,222 Shopping clicks, 0 Shopping-attrib... |
| CTR-20260906-2235-009 | B | unknown | FAILURE_ATLAS/CLICKS_NO_ATC | New Standard Shopping test → Ran optimized Merchant feed under Standard Shopping → 10 days: ~$500 spend, 67.6k impressions, 300 clicks, 0 purchases |
| CTR-20260906-2235-010 | A | GB | ACTION_OUTCOME/SALES_UNPROFITABLE | Successful Facebook operation with £300k+ historical revenue over 2 years → Ran Maximize Clicks for 7 days, then switched to Manual CPC at £1.50 → Day 9 Google: 260 clicks, 35.8k impressions, £305 spend, 1 purchase |
| CTR-20260906-2235-011 | A | NZ | PROFITABLE_SPARSE/HIDDEN_ECONOMICS | Account had 50 conversions in prior 30 days at poor ROAS under former agency → Launched Jun 8 with 25 SKUs and tROAS 200%, using prior account conversion history → First 2 days: 3 conversions, ~700 impressions/day, 1-2 clicks/day, only 10-20% budget spend, ... |
| CTR-20260906-2235-012 | B | unknown | LOW_CAPITAL/NO_TRAFFIC | New store → Connected Pinterest, TikTok, Facebook, Instagram, Shop, GMC Free Listings, Search Console and posted daily organically → After ~1 month: no sales and effectively no meaningful store traffic |
| CTR-20260906-2235-013 | B | NO | COUNTRY_TRANSPLANT/MERCHANT_FRICTION | Checkout promised no extra delivery charges → Customer ordered ~NOK 8,000 basket advertised as taxes included → DHL held parcel and requested ~NOK 3,000, later ~NOK 3,500, because one item exceeded NOK 3,000 VOEC item threshold |
| CTR-20260906-2235-014 | B | FI | COUNTRY_TRANSPLANT/MERCHANT_FRICTION | Product appeared immediately available; chatbot reported 19 in stock → Customer ordered an item shown with many units and immediate availability, then queried support chatbot → Order remained 'waiting for products'; chatbot disclosed it was a dropship produ... |
| CTR-20260906-2235-015 | B | NO | COUNTRY_TRANSPLANT/MERCHANT_FRICTION | In Germany, search produced many solid options with low shipping → Consumer compared Norway online shopping experience with Germany while searching everyday goods → In Norway, user reported limited selection, expensive shipping, uncertainty about trustworth... |
| CTR-20260906-2235-016 | B | NO | COUNTRY_TRANSPLANT/ACTION_OUTCOME | Etsy described as impractical for Norway due high shipping/post costs and poor local postal integration → Merchant rejected Etsy due Norwegian postage friction; evaluated local options and switched to Epla → Epla reported to fit the early stage: first 10 pr... |
| CTR-20260906-2235-017 | B | NO | COUNTRY_TRANSPLANT/MERCHANT_FRICTION | Unclear local shopping map → Consumer asked where Norwegians compare/buy multiple product categories → Community repeatedly directed shopper to Prisjakt for price comparison and category specialists such as Komplett, Bikeshop, VetZoo; shipping cost/location... |
| CTR-20260906-2235-018 | B | FI | COUNTRY_TRANSPLANT/MERCHANT_FRICTION | Home delivery expected → Courier marked attempted delivery while recipient reported being present; support promised pickup reroute → No successful reroute or notification; parcel was being returned; commenters reported similar Finnish UPS experiences |

## Open-case / follow-up queue

- Revisit Shopify `product page unavailable` case: test whether the Jun 3 relapse to ~400 affected products was later resolved and whether a durable root cause was identified.
- Revisit the 6k-SKU Merchant API migration case for later feed health and whether OOS 404s were eventually fixed.
- Watch the Swedish 2,600-product Standard Shopping flatline case for any later recovery or bidding/campaign reset outcome.
- Watch the 449-click Google-zero-sales drink company for a strategy change and post-change conversion outcome.
- Expand Finnish merchant-side research beyond consumer complaints into local operator economics, supplier terms and checkout data.

## Coverage gaps

- Only 18 records cleared the bar; not padded to 20.
- Fresh native-language Finnish operator economics remain sparse; current Finnish records are consumer/merchant-quality signals.
- Few current traces expose COGS, net contribution or return rates.
- Need follow-up on 2026 Shopify Merchant API / product-page-unavailable cases to see whether relapses persist.
- Need more supplier-change -> shipping/CVR outcome traces rather than platform-only anomalies.

## Attachments

- `records.jsonl` — normalized append-ready observations
- `records.csv` — flat analysis export
- `run_manifest.json` — run counts, source-yield updates and coverage gaps
