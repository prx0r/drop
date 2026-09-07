# [Commerce Trace Radar] 2026-09-06 23:00 — 20 novel records

# Commerce Trace Radar — 20 accepted novel records

## Executive summary

This run accepted 20 novel high-signal records after explicitly deduplicating against the 19:00–22:00 Commerce Trace reports. Sixteen candidates were rejected as repeats or near-repeats.

The strongest fresh signal is that **campaign economics can remain profitable while delivery collapses**. One current single-product Shopping trace has ~70 orders in the last 30 days, 4–5% CVR, break-even ROAS around 1.43x, and actual ROAS around 2x, yet spend fell from a ~$116/day budget toward ~$30–60/day after tROAS/budget and product-price changes. This is valuable because it separates `PROFITABLE_SPARSE` from `SALES_UNPROFITABLE`: the correct response is not necessarily to kill the product.

Second, **conversion-goal and budget edits remain high-risk state transitions**. A new-store Google campaign went from roughly one sale every 2–3 days to seven days with none after the account was changed to count purchases only. Another PMax store went from roughly one order/day at £20/day to zero orders for five days after a 75% budget jump to £35/day.

Third, **multi-market feed infrastructure is emerging as a real commerce moat/risk layer**. France fell from ~1,400 approved products to zero while six sibling Shopify Markets kept syncing; another DE/AT/CH setup left price/removal edits stale for at least three days; Shopify Markets coincided with Search Console product entities collapsing from ~70k to ~670 while Merchant Center still showed ~75k approved. Cross-country launch plans therefore need feed-state monitoring as seriously as CPC/CVR monitoring.

Evidence mix: 10 A, 9 B, 1 C. Reviewed 62 candidates; skipped 16 duplicates/near-duplicates.

## Top 3 highest-signal findings

### 1. A profitable single-product Shopping campaign became severely budget-constrained after tROAS/budget and price changes despite ~70 monthly orders and strong headline ROAS.
- **Before:** 2.0-2.1x actual ROAS, profitable vs 1.43-1.52x break-even; daily budget ~$116 with $60-80 spend
- **Action:** After ~30 conversions switched to tROAS 2.5x, raised budgets ~20%; later raised price $70->$78, then lowered tROAS to 2.0x and raised budget again
- **After:** After price change spend dropped to ~$30-40/day; later ~40-60/day despite lower tROAS; individual days varied from 6 conversions at ~$3 CAC to 1 at $47 CAC
- **Evidence grade:** A
- **Source:** https://www.reddit.com/r/PPC/comments/1vw3ali/shopping_ads_wont_spend_full_daily_budgettroas/

### 2. Narrowing conversion goals to purchases only was followed by reduced delivery and a seven-day sales drought after an initial sale-every-few-days cadence.
- **Before:** From Jun 28 launch: full $50/day spend, first conversion next day, then roughly 1 sale every 2-3 days
- **Action:** Changed conversion tracking so purchases were the only counted conversion instead of ATC/engagement actions
- **After:** Impressions/clicks and spend fell (~$31 of $50 on recent days); 0 sales for 7 days
- **Evidence grade:** A
- **Source:** https://www.reddit.com/r/googleads/comments/1uzw1we/about_to_give_up_on_googleads/

### 3. One child market (France) dropped from ~1,400 approved products to zero while six other Shopify Markets continued syncing.
- **Before:** France feed had ~1,400 approved products before ~Aug 1; other country feeds normal
- **Action:** Operated one Shopify store across 7 Markets with automatic product/country/language/shipping sync
- **After:** France feed label and both FR data sources fell to 0 products while DE/EU/CH/UK/NO feeds remained populated
- **Evidence grade:** A
- **Source:** https://community.shopify.com/t/google-youtube-child-markets-feed-label-stays-empty-0-products-while-all-other-markets-sync/665765

## Action → outcome / longitudinal cases

- **CTR-20260906-2334-001** — A recently reinstated US account launched an eligible Shopping campaign and remained at 0 impressions for more than 72 hours. Source: https://support.google.com/google-ads/thread/450566989/new-shopping-campaign-serving-0-impressions-for-72-hours-despite-eligible-status?hl=en
- **CTR-20260906-2334-003** — The same WooCommerce inventory served in PMax but failed to serve at all in five Standard Shopping rebuilds. Source: https://support.google.com/google-ads/thread/447928053/performance-max-works-standard-shopping-campaigns-get-zero-impressions-%E2%80%94-why?hl=en
- **CTR-20260906-2334-004** — A Turkish merchant fixed feed label, currency and bidding yet both PMax and Standard Shopping continued at zero delivery. Source: https://support.google.com/google-ads/thread/432389110/shopping-campaigns-not-serving-0-impressions-for-2-weeks-despite-eligible-status?hl=en
- **CTR-20260906-2334-006** — After Shopify Markets enablement, Search Console product entities fell from ~70k to ~670 while ~75k products remained approved in Merchant Center. Source: https://community.shopify.com/t/shopify-markets-caused-collapse-in-google-product-snippets-organic-impressions/621588
- **CTR-20260906-2334-011** — Narrowing conversion goals to purchases only was followed by reduced delivery and a seven-day sales drought after an initial sale-every-few-days cadence. Source: https://www.reddit.com/r/googleads/comments/1uzw1we/about_to_give_up_on_googleads/
- **CTR-20260906-2334-012** — A PMax campaign lost more than half its ROAS in one week, driven mainly by mobile CVR collapse despite stable search/channel mix and apparently intact tracking. Source: https://www.reddit.com/r/smallbusiness/comments/1uv94mg/google_roas_dropped_1000_in_a_week/
- **CTR-20260906-2334-013** — A two-year Shopping campaign with >£100k spend and >£450k attributed revenue reportedly lost most conversions at the start of 2026 without feed disapprovals. Source: https://www.reddit.com/r/shopify/comments/1qykheu/google_ads_shopping_campaign_dropped_off_since/
- **CTR-20260906-2334-014** — A 75% PMax budget increase on a £35-£40 product was followed by five days of zero orders after a prior ~1-order/day cadence. Source: https://www.reddit.com/r/googleads/comments/1sqedh7/google_ads_are_too_confusing/
- **CTR-20260906-2334-015** — A sequence of feed/title/category edits preceded free-listing visibility falling from 25+ products to 4, and technical cleanup did not immediately restore discovery. Source: https://www.reddit.com/r/ecommerce/comments/1rtwc8s/google_shopping_free_listings_dropped_from_25_to/
- **CTR-20260906-2334-017** — The same store generated 3-4 daily orders from Standard Shopping while a PMax test spent ~$200 with zero conversions. Source: https://www.reddit.com/r/dropshipping/comments/1u59oym/shopping_campaigns_are_getting_3_to_4_orders/
- **CTR-20260906-2334-019** — A previously stable high-volume Meta creative moved from ~$5/order to ~$12-15/order as CPM tripled or quadrupled, and months of interventions failed to restore economics. Source: https://www.reddit.com/r/FacebookAds/comments/1qxpb9q/2025_was_the_worst_year_of_my_life_as_a_facebook/

## Failure atlas

- **NO_DELIVERY:** 4 records
- **SALES_UNPROFITABLE:** 5 records
- **PROFITABLE_THEN_COLLAPSED:** 4 records
- **PROFITABLE_SPARSE:** 1 records
- **CHECKOUT_OR_TRAFFIC_QUALITY:** 1 records
- **PLATFORM_OR_FEED_ANOMALY:** 5 records

## Foreign / multi-market signals

- **TR — CTR-20260906-2334-004**: A Turkish merchant fixed feed label, currency and bidding yet both PMax and Standard Shopping continued at zero delivery. Source: https://support.google.com/google-ads/thread/432389110/shopping-campaigns-not-serving-0-impressions-for-2-weeks-despite-eligible-status?hl=en
- **ZA — CTR-20260906-2334-005**: Refurbished phones won prominent Shopping auctions cheaply but converted only ~0.25% across ~1,500 clicks. Source: https://www.reddit.com/r/GoogleAdsDiscussion/comments/1v927v7/manual_cpc_getting_clicks_but_low_sales_on_new/
- **multi-market — CTR-20260906-2334-006**: After Shopify Markets enablement, Search Console product entities fell from ~70k to ~670 while ~75k products remained approved in Merchant Center. Source: https://community.shopify.com/t/shopify-markets-caused-collapse-in-google-product-snippets-organic-impressions/621588
- **CA/unknown — CTR-20260906-2334-007**: A store using a private Shopify Collective supplier repeatedly bounced between GMC approval and rejection despite active supplier/merchant product setup. Source: https://community.shopify.com/t/google-merchant-center-rejecting-site-selling-collective-products/636478
- **FR — CTR-20260906-2334-009**: One child market (France) dropped from ~1,400 approved products to zero while six other Shopify Markets continued syncing. Source: https://community.shopify.com/t/google-youtube-child-markets-feed-label-stays-empty-0-products-while-all-other-markets-sync/665765
- **DE/AT/CH — CTR-20260906-2334-020**: Across DE/AT/CH, Shopify product removals and price/attribute changes failed to propagate to Merchant Center for at least three days. Source: https://community.shopify.com/t/google-youtube-merchant-center-feed-not-updating/608036

## Source-yield changes

- **r/googleads current 2026:** HIGH — fresh quantified budget/goal/channel failure traces
- **r/PPC current 2026:** VERY HIGH — best economics and bid/budget sequence density
- **Google Ads Community 2026:** HIGH — clean NO_DELIVERY/backend serving cases
- **Shopify Community multi-market feeds:** VERY HIGH — country-specific sync and Merchant entity failure traces
- **r/ecommerce:** MEDIUM-HIGH — useful cross-channel funnel/merchant-quality contrasts
- **r/FacebookAds:** MEDIUM — high numeric density but more retrospective/self-reported

## Compact accepted-record table

| ID | Grade | Market | Probe | Summary |
|---|---:|---|---|---|
| CTR-20260906-2334-001 | B | US | NO_DELIVERY/ACTION_OUTCOME | A recently reinstated US account launched an eligible Shopping campaign and remained at 0 impressions for more than 72 hours. |
| CTR-20260906-2334-002 | B | unknown | NO_DELIVERY/PLATFORM_ANOMALY | Multiple clean Standard Shopping rebuilds stayed at zero delivery, with support surfacing a product-level NO_DATA auction-eligibility state. |
| CTR-20260906-2334-003 | B | unknown | NO_DELIVERY/ACTION_OUTCOME | The same WooCommerce inventory served in PMax but failed to serve at all in five Standard Shopping rebuilds. |
| CTR-20260906-2334-004 | A | TR | NO_DELIVERY/ACTION_OUTCOME | A Turkish merchant fixed feed label, currency and bidding yet both PMax and Standard Shopping continued at zero delivery. |
| CTR-20260906-2334-005 | B | ZA | HIDDEN_ECONOMICS/SALES_UNPROFITABLE | Refurbished phones won prominent Shopping auctions cheaply but converted only ~0.25% across ~1,500 clicks. |
| CTR-20260906-2334-006 | A | multi-market | ACTION_OUTCOME/ORGANIC_COLLAPSE | After Shopify Markets enablement, Search Console product entities fell from ~70k to ~670 while ~75k products remained approved in Merchant Center. |
| CTR-20260906-2334-007 | B | CA/unknown | SUPPLIER_ANOMALY/COUNTRY_TRANSPLANT | A store using a private Shopify Collective supplier repeatedly bounced between GMC approval and rejection despite active supplier/merchant product setup. |
| CTR-20260906-2334-008 | B | unknown | SUPPLIER_ANOMALY/PLATFORM_ANOMALY | A 5,000-product Shopify catalog repeatedly plateaued around 2,400 synced Merchant Center items despite reinstalls and waiting. |
| CTR-20260906-2334-009 | A | FR | COUNTRY_TRANSPLANT/PLATFORM_ANOMALY | One child market (France) dropped from ~1,400 approved products to zero while six other Shopify Markets continued syncing. |
| CTR-20260906-2334-010 | A | EU | HIDDEN_ECONOMICS/SALES_UNPROFITABLE | An EU fashion brand that works on Meta still produced only 3 Shopping conversions from 320 clicks and ~0.5 ROAS in the latest 14 days. |
| CTR-20260906-2334-011 | A | unknown | ACTION_OUTCOME/PROFITABLE_THEN_COLLAPSED | Narrowing conversion goals to purchases only was followed by reduced delivery and a seven-day sales drought after an initial sale-every-few-days cadence. |
| CTR-20260906-2334-012 | A | EU | PROFITABLE_THEN_COLLAPSED/HIDDEN_ECONOMICS | A PMax campaign lost more than half its ROAS in one week, driven mainly by mobile CVR collapse despite stable search/channel mix and apparently intact tracking. |
| CTR-20260906-2334-013 | A | GB | OPERATOR_TIMELINE/PROFITABLE_THEN_COLLAPSED | A two-year Shopping campaign with >£100k spend and >£450k attributed revenue reportedly lost most conversions at the start of 2026 without feed disapprovals. |
| CTR-20260906-2334-014 | A | GB | ACTION_OUTCOME/SALES_UNPROFITABLE | A 75% PMax budget increase on a £35-£40 product was followed by five days of zero orders after a prior ~1-order/day cadence. |
| CTR-20260906-2334-015 | A | NL/unknown | ACTION_OUTCOME/LOW_CAPITAL | A sequence of feed/title/category edits preceded free-listing visibility falling from 25+ products to 4, and technical cleanup did not immediately restore discovery. |
| CTR-20260906-2334-016 | A | unknown | PROFITABLE_SPARSE/HIDDEN_ECONOMICS | A profitable single-product Shopping campaign became severely budget-constrained after tROAS/budget and price changes despite ~70 monthly orders and strong headline ROAS. |
| CTR-20260906-2334-017 | B | unknown | ACTION_OUTCOME/CAMPAIGN_TYPE_CONTRAST | The same store generated 3-4 daily orders from Standard Shopping while a PMax test spent ~$200 with zero conversions. |
| CTR-20260906-2334-018 | B | EU | CHECKOUT_NO_PURCHASE/HIDDEN_ECONOMICS | An established €300-€4,000 EU luxury retailer reported excellent paid engagement but zero paid sales while organic/email/referral continued working. |
| CTR-20260906-2334-019 | C | US | OPERATOR_TIMELINE/PROFITABLE_THEN_COLLAPSED | A previously stable high-volume Meta creative moved from ~$5/order to ~$12-15/order as CPM tripled or quadrupled, and months of interventions failed to restore economics. |
| CTR-20260906-2334-020 | B | DE/AT/CH | PLATFORM_ANOMALY/COUNTRY_TRANSPLANT | Across DE/AT/CH, Shopify product removals and price/attribute changes failed to propagate to Merchant Center for at least three days. |

## Open-case follow-up queue

- Revisit the Aug 23 single-product tROAS underdelivery case for a one-week outcome after the operator's planned no-change hold.
- Revisit the Sep 1 EU fashion case for any SKU pruning, bidding change, or subsequent ROAS recovery.
- Follow France child-market feed failure to determine whether the ~1,400 → 0 product collapse was resolved and by what action.
- Follow the Google Ads Community `NO_DATA` / zero-impression cases for backend-serving resolution rather than accumulating unresolved snapshots.
- Revisit purchase-only conversion-goal case to determine whether delivery/sales recover without further campaign edits.

## Coverage gaps

- Native Norwegian/Finnish records found in this search were mostly duplicates of the previous run, so they were rejected rather than recycled.
- COGS, return rate and net contribution remain scarce even in otherwise strong operator traces.
- Need future same-author follow-ups on Aug/Sep 2026 Shopping cases, especially tROAS underdelivery and EU fashion chronic unprofitability.
- Need more supplier-change -> shipping/CVR outcome traces and fewer platform-only anomalies.
- Google Ads Community NO_DELIVERY cases are diagnostically strong but many remain unresolved, so follow-up state is crucial.

## Machine-readable artifacts

- `records.jsonl` — append-ready normalized records
- `records.csv` — flat analysis export
- `run_manifest.json` — run/source/probe metadata
