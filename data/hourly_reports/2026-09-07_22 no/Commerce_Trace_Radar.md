# [Commerce Trace Radar] 2026-09-07 02:00 — 22 novel records

# Commerce Trace Radar — 22 accepted novel records

## Executive summary

This run accepted 22 novel high-signal records after deduplicating against the latest sent Commerce Trace reports. The best new evidence came from controlled or quasi-controlled transitions: pausing quota-constrained PMax while Search remained profitable; a recurring PayPal checkout bug with a failed platform fix; and an AutoDS inventory-sync mechanism that silently blocked checkout.

The main learning is that 'ad performance' is often not an ad problem. Feed identity, optimization goals, payment integrations, supplier inventory sync, bot traffic, and checkout platform state can each alter observed CVR or delivery enough to invalidate naïve campaign conclusions. These variables should be first-class nodes in the market graph.

A second learning is that cross-channel contrast is highly diagnostic. Several stores convert on Meta, brand search, or Search while generic Shopping/PMax underperforms. That weakens generic 'bad website/product' explanations and supports separating acquisition-quality failures from storefront failures.

A third learning is geographic: Norway continues to produce concrete evidence that landed-cost transparency and regional fulfillment can be a moat. Distance-based freight and duplicate import-charge experiences create exactly the friction a locally stocked specialist can remove.

Run stats: 22 accepted / 67 reviewed / 15 duplicates or near-duplicates skipped. Evidence: 7 A, 14 B, 1 C.

## Top 3 highest-signal findings

### 1. After pausing quota-constrained PMax, Search produced 5 purchases, $4,139 revenue and 11.9 ROAS with clean transaction verification.
- Before: 351,174 products submitted: 110,721 approved, 102,595 limited, 117,910 disapproved, 19,948 under review
- Action: Paused PMax after Merchant Center showed Shopping Ads quota limit outside CSS program
- After: Search then generated 5 purchases, $4,139 attributed revenue and 11.90 ROAS; GA4 transaction IDs matched without duplication
- Grade: A
- Source: https://www.reddit.com/r/Google_Ads/comments/1v4m49h/need_advice_from_ppc_experts_on_how_to_scale_an/

### 2. A Germany-heavy Shopify store saw PayPal checkout recover briefly, then relapse; Shopify later confirmed its first fix failed.
- Before: Issue active since ~Feb 6; conversion rate around 1% for ~2 weeks; temporary fix restored PayPal checkout share to ~50%
- Action: Shopify deployed an initial fix; merchant monitored PayPal checkout share and escalated logs after relapse
- After: Mar 4 PayPal conversions crashed again; store CVR 1.43%; on Mar 8 Shopify confirmed initial fix had failed and escalated to second dev team
- Grade: A
- Source: https://community.shopify.com/t/paypal-express-login-failure-for-logged-in-customers-since-aprox-feb-6-new-customer-accounts-migration/588982

### 3. AutoDS inventory resync silently re-enabled stock tracking and triggered an out-of-stock modal that blocked most checkout starters.
- Before: 14 days: 1,821 sessions, 84 ATCs, 87 checkout-reaching sessions, only 6 orders; ~77 checkout starters entered no info
- Action: Diagnosed AutoDS inventory sync; changed inventoryPolicy to CONTINUE and tracked=false on every variant
- After: Found supplier inventory sync flipping tracking back on and triggering out-of-stock modal that blocked checkout; fix deployed, later sales outcome not yet known
- Grade: A
- Source: https://www.reddit.com/r/dropshipping/comments/1tmqg5r/95_of_my_shopify_checkoutstarters_bail_before/

## Longitudinal / action→outcome records

- **CTR-20260907-001** — A first-time operator spent about $200 on Meta to generate one $60 sale. Source: https://www.reddit.com/r/dropshipping/comments/1snoixx/my_first_sale/
- **CTR-20260907-002** — An Italy-focused first store got its first sale via TikTok→brand search after a €40 paid test failed to convert. Source: https://www.reddit.com/r/dropshipping/comments/1sz3ep2/i_got_my_first_sale/
- **CTR-20260907-003** — A cluster of feed edits preceded free-listing visibility collapsing from 25+ products to about 4. Source: https://www.reddit.com/r/ecommerce/comments/1rtwc8s/google_shopping_free_listings_dropped_from_25_to/
- **CTR-20260907-004** — A mature PMax campaign lost roughly half its purchase volume at similar spend; lowering tROAS had not restored sales. Source: https://www.reddit.com/r/GoogleAdsDiscussion/comments/1vvmifq/pmax_conversions_dropped_50_after_recent_bidding/
- **CTR-20260907-006** — After pausing quota-constrained PMax, Search produced 5 purchases, $4,139 revenue and 11.9 ROAS with clean transaction verification. Source: https://www.reddit.com/r/Google_Ads/comments/1v4m49h/need_advice_from_ppc_experts_on_how_to_scale_an/
- **CTR-20260907-007** — Switching optimization to purchases only preceded both underdelivery and a 7-day sales drought in a previously converting campaign. Source: https://www.reddit.com/r/googleads/comments/1uzw1we/about_to_give_up_on_googleads/
- **CTR-20260907-008** — Ultra-cheap Shopping clicks generated browsing rather than buying; operator switched to Manual CPC after ~5,000 clicks and few orders. Source: https://www.reddit.com/r/Google_Ads/comments/1qsto0b/struggling_with_google_shopping_max_clicks_vs/
- **CTR-20260907-009** — A Germany-heavy Shopify store saw PayPal checkout recover briefly, then relapse; Shopify later confirmed its first fix failed. Source: https://community.shopify.com/t/paypal-express-login-failure-for-logged-in-customers-since-aprox-feb-6-new-customer-accounts-migration/588982
- **CTR-20260907-011** — AutoDS inventory resync silently re-enabled stock tracking and triggered an out-of-stock modal that blocked most checkout starters. Source: https://www.reddit.com/r/dropshipping/comments/1tmqg5r/95_of_my_shopify_checkoutstarters_bail_before/
- **CTR-20260907-014** — A high-CTR funnel stayed near 1% CVR; a rebuilt page briefly sold, then stalled, and audit found 8-11s mobile LCP plus an ATC-blocking popup. Source: https://tr.reddit.com/r/dropshipping/comments/1uk1qji/wildly_streaky_sales_56_in_a_couple_days_then/
- **CTR-20260907-015** — A new Shopping campaign received almost no impressions while bids, bid strategy and feed structure were repeatedly changed in its first week. Source: https://www.reddit.com/r/googleads/comments/1t9xwj6/new_google_shopping_campaign_barely_spending/
- **CTR-20260907-018** — The same store/product served under PMax but Standard Shopping stayed at zero across five rebuilds, indicating campaign-type/backend divergence. Source: https://support.google.com/google-ads/thread/447928053/performance-max-works-standard-shopping-campaigns-get-zero-impressions-%E2%80%94-why?hl=en

## Foreign-market signals

- **US / CTR-20260907-012** — An established Shopify store reported a US-only conversion collapse of about 60% while other markets remained comparatively normal. Source: https://www.reddit.com/r/shopify/comments/1u9pel3/anyone_seeing_big_conversion_rates_declines_over/
- **NO / CTR-20260907-021** — Norwegian furniture ecommerce can have extreme distance-based shipping gaps: one low-cost order showed NOK 4,000 minimum freight. Source: https://www.reddit.com/r/norge/comments/1uffr7i/er_dette_normal_frakt_fra_ikea/
- **NO / CTR-20260907-022** — A Norwegian AliExpress buyer paid NOK 500 at checkout yet still received a second import-payment demand before delivery. Source: https://www.reddit.com/r/norge/comments/1ux7fwe/f%C3%A5tt_tollkrav_n%C3%A5r_jeg_allerede_har_betalt_toll/

## Source-yield updates

- **Shopify Community checkout threads:** HIGH — fine-grained state/action/payment-stage evidence
- **Google Ads Community hidden-serving threads:** HIGH — backend NO_DATA / eligible-but-zero cases
- **r/googleads and r/PPC:** HIGH — strongest numeric acquisition economics
- **r/dropshipping:** MEDIUM-HIGH — useful first-sale and supplier-sync traces, but more hype filtering required
- **r/norge:** HIGH for native-language shipping/import friction; low for operator margin data
- **commercial benchmark posts:** MEDIUM — usable only with explicit commercial-incentive downgrade

## Compact accepted-record table

| ID | Grade | Market | Probe | Summary |
|---|---:|---|---|---|
| CTR-20260907-001 | B | unknown | LOW_CAPITAL/OPERATOR_TIMELINE | A first-time operator spent about $200 on Meta to generate one $60 sale. |
| CTR-20260907-002 | B | IT | LOW_CAPITAL/OPERATOR_TIMELINE | An Italy-focused first store got its first sale via TikTok→brand search after a €40 paid test failed to convert. |
| CTR-20260907-003 | A | unknown | ACTION_OUTCOME/FREE_LISTINGS | A cluster of feed edits preceded free-listing visibility collapsing from 25+ products to about 4. |
| CTR-20260907-004 | B | unknown | ACTION_OUTCOME/PROFITABLE_THEN_COLLAPSED | A mature PMax campaign lost roughly half its purchase volume at similar spend; lowering tROAS had not restored sales. |
| CTR-20260907-005 | B | EU | HIDDEN_ECONOMICS/SALES_UNPROFITABLE | An EU fashion brand with profitable Meta and brand search got only 0.5 ROAS from 320 Shopping clicks. |
| CTR-20260907-006 | A | unknown | ACTION_OUTCOME/HIDDEN_ECONOMICS | After pausing quota-constrained PMax, Search produced 5 purchases, $4,139 revenue and 11.9 ROAS with clean transaction verification. |
| CTR-20260907-007 | A | unknown | ACTION_OUTCOME/TRACKING_ANOMALY | Switching optimization to purchases only preceded both underdelivery and a 7-day sales drought in a previously converting campaign. |
| CTR-20260907-008 | B | unknown | ACTION_OUTCOME/SALES_UNPROFITABLE | Ultra-cheap Shopping clicks generated browsing rather than buying; operator switched to Manual CPC after ~5,000 clicks and few orders. |
| CTR-20260907-009 | A | DE | ACTION_OUTCOME/CHECKOUT_NO_PURCHASE | A Germany-heavy Shopify store saw PayPal checkout recover briefly, then relapse; Shopify later confirmed its first fix failed. |
| CTR-20260907-010 | A | US | CHECKOUT_NO_PURCHASE/HIDDEN_ECONOMICS | A $54.99 chopper store had 30 ATCs and 19 checkouts from $300 Meta spend but zero orders; the abandonment split into pre-form and payment-stage failures. |
| CTR-20260907-011 | A | US | ACTION_OUTCOME/SUPPLIER_ANOMALY | AutoDS inventory resync silently re-enabled stock tracking and triggered an out-of-stock modal that blocked most checkout starters. |
| CTR-20260907-012 | B | US | FAILURE_ATLAS/COUNTRY_TRANSPLANT | An established Shopify store reported a US-only conversion collapse of about 60% while other markets remained comparatively normal. |
| CTR-20260907-013 | B | US | TRACKING_ANOMALY/FAILURE_ATLAS | A mature store's checkout analytics were overwhelmed by 1,314 bot visits and 949 abandoned carts, making raw abandonment metrics unreliable. |
| CTR-20260907-014 | A | unknown | ACTION_OUTCOME/CLICKS_NO_ATC | A high-CTR funnel stayed near 1% CVR; a rebuilt page briefly sold, then stalled, and audit found 8-11s mobile LCP plus an ATC-blocking popup. |
| CTR-20260907-015 | B | unknown | NO_DELIVERY/ACTION_OUTCOME | A new Shopping campaign received almost no impressions while bids, bid strategy and feed structure were repeatedly changed in its first week. |
| CTR-20260907-016 | B | US | NO_DELIVERY/TRACKING_ANOMALY | A recently reinstated account remained completely unable to serve Shopping for 72+ hours despite approved products and resolved billing. |
| CTR-20260907-017 | B | unknown | NO_DELIVERY/TRACKING_ANOMALY | Multiple eligible Standard Shopping campaigns stayed at zero for a week, with Google support surfacing a hidden product-level 'NO_DATA' auction state. |
| CTR-20260907-018 | B | unknown | NO_DELIVERY/ACTION_OUTCOME | The same store/product served under PMax but Standard Shopping stayed at zero across five rebuilds, indicating campaign-type/backend divergence. |
| CTR-20260907-019 | B | EU | HIDDEN_ECONOMICS/PROFITABLE_SPARSE | A B2B workwear store with 20k SKUs could preserve margin only at high tROAS, leaving campaigns spending ~20% of available budget. |
| CTR-20260907-020 | C | multi-market | HIDDEN_ECONOMICS/CATALOG_DYNAMICS | A commercial analysis of 1.4M products claims catalog spend is highly concentrated and warns that hard click-based loser thresholds discard later sellers. |
| CTR-20260907-021 | B | NO | COUNTRY_TRANSPLANT/MERCHANT_FRICTION | Norwegian furniture ecommerce can have extreme distance-based shipping gaps: one low-cost order showed NOK 4,000 minimum freight. |
| CTR-20260907-022 | B | NO | COUNTRY_TRANSPLANT/MERCHANT_FRICTION | A Norwegian AliExpress buyer paid NOK 500 at checkout yet still received a second import-payment demand before delivery. |

## Coverage gaps

- Fresh Finnish operator-side quantitative economics remained too sparse to clear the acceptance bar this hour.
- Supplier-switch -> measured shipping/CVR outcome traces remain underrepresented.
- Most operator posts still omit COGS/net contribution; ROAS can overstate business viability.
- Need later outcomes for AutoDS inventory fix, PMax 50% decline, and new Shopping over-editing cases.
- Need native-language Nordic category-specific searches tied to exact product families rather than general ecommerce complaints.

## Machine-readable attachments

- records.jsonl — normalized append-ready records
- records.csv — flat analysis export
- run_manifest.json — source-yield, funnel-state and coverage metadata
