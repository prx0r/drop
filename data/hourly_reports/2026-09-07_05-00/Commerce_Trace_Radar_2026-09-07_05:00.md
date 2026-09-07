# [Commerce Trace Radar] 2026-09-07 05:00 — 20 novel records

# Commerce Trace Radar — 20 accepted novel records

## Executive summary

This run accepted 20 records after checking the latest sent Radar emails and excluding obvious repeats. The strongest new cluster is not 'Google Ads got worse' in the abstract; it is measurable bidding-state instability around target changes and the August 17 Smart Bidding shift. Multiple mature ecommerce operators report abrupt CPC, ROAS, spend, or query-mix changes even when campaigns previously had deep conversion history.

A second cluster localizes failures below the ad layer. A previously healthy PMax campaign remained at zero delivery after Merchant Center disapprovals were fixed; a Shopify Payments transition coincided with a 46% sales decline despite traffic rising 22% and ATC staying normal; and a separate UK store reached checkout 150 times from 2,191 sessions without a single purchase.

A third cluster reinforces the value of structural comparisons. Brand traffic moved out of PMax converted worse in Search; 37 historical winning SKUs isolated into a new campaign produced zero sales; and an NZ store's switch from Shopping+exact Search to PMax+broad cut ROAS from break-even-ish 1.6-1.8x to 0.8x then 0.6x. The dataset should preserve campaign architecture, product grouping and payment provider as state variables.

Run stats: 20 accepted / 76 reviewed / 18 duplicates skipped. Evidence: 13 A, 6 B, 1 C.

## Top 3 highest-signal findings

### 1. Removing brand terms from PMax and shifting them to Search reduced conversion quality and slightly lowered business revenue within days.
- Before: Brand terms represented ~80% of observable PMax spend; PMax converted branded traffic strongly
- Action: Added 3 exact brand negatives to PMax, moved branded terms to Search, increased Search budget and lowered PMax budget
- After: After a few days, branded Search clicked but converted worse than PMax; business revenue fell slightly and MER increased
- Grade: A
- Source: https://www.reddit.com/r/PPC/comments/1vtksb7/added_negative_brand_keywords_to_pmax/

### 2. Fixing all Merchant Center disapprovals did not restore a previously healthy PMax campaign; delivery stayed at zero even after budget/tROAS loosening.
- Before: PMax had run since January and performed well before GMC link; products then disapproved for missing weight
- Action: Linked Merchant Center, fixed missing-weight disapprovals, doubled budget and removed tROAS
- After: All products became approved in GMC, but some Ads surfaces still showed disapproved and campaign remained at 0 impressions/clicks
- Grade: A
- Source: https://support.google.com/google-ads/thread/461259956/performance-max-campaign-stuck-at-0-impressions-after-fixing-merchant-center-disapprovals?hl=en-7-0

### 3. After switching to Shopify Payments, one store reported sales down 46% despite traffic up 22% and normal ATC, localizing the break near checkout/payment.
- Before: Previously used PayPal credit/debit processing; baseline sales higher
- Action: Activated Shopify Payments around May/June 2025; platform later updated fraud prevention
- After: From late July onward sales down 46% while traffic up 22% and ATC stayed normal; checkout dropped significantly
- Grade: A
- Source: https://community.shopify.com/t/sales-plummeted-shortly-after-activating-shopify-payments/588571

## Updated longitudinal / action→outcome cases

- **CTR-20260907-0531-001** — A historically 700-800% ROAS account fell to ~350% after aligning tROAS to recent actual performance around the Aug 17 bidding change. Source: https://www.reddit.com/r/PPC/comments/1vysvjc/roas_targets_vs_actual_roas_after_aug_17th/
- **CTR-20260907-0531-002** — Raising tROAS 900→1100% was followed by lower spend and ~20% lower sales within two weeks. Source: https://www.reddit.com/r/PPC/comments/1w06apr/help_me_understand_troas_vs_max_conv_value/
- **CTR-20260907-0531-003** — A profitable Standard Shopping account saw CPC jump roughly 9x, from $1.30 to $11-12, over ~11 days. Source: https://www.reddit.com/r/PPC/comments/1w0lsbw/standard_shopping_cpc_suddenly_went_from_130_to/
- **CTR-20260907-0531-004** — Removing brand terms from PMax and shifting them to Search reduced conversion quality and slightly lowered business revenue within days. Source: https://www.reddit.com/r/PPC/comments/1vtksb7/added_negative_brand_keywords_to_pmax/
- **CTR-20260907-0531-005** — A high-volume high-ticket Standard Shopping account deteriorated after Aug 17: CPC up, CVR down, query mix broadened. Source: https://www.reddit.com/r/PPC/comments/1w0e17t/standard_shopping_budgetcapped_high_aov/
- **CTR-20260907-0531-006** — A bestseller stockout plus SKU merge was followed by a two-week order decline that did not recover promptly after restocking. Source: https://www.reddit.com/r/DigitalMarketing/comments/1vrwybg/why_the_sudden_drop/
- **CTR-20260907-0531-009** — An NZ store fell from ~1.6-1.8x ROAS to 0.8x/0.6x after an agency replaced Shopping+exact Search with PMax+broad while raising budget. Source: https://www.reddit.com/r/PPC/comments/1l54t55/agency_switched_to_pmax_broad_matchroas_collapsed/
- **CTR-20260907-0531-010** — Splitting 37 proven winners from a 3,800-SKU campaign reset performance: €250 over five days yielded zero sales despite the parent campaign's ~4.5 ROAS. Source: https://www.reddit.com/r/googleads/comments/1qo83ne/google_winner_campaign/
- **CTR-20260907-0531-011** — A two-year ~6x-ROAS PMax setup broke after a $65→$100/day increase; later brand splitting did not simply recreate the old outcome. Source: https://www.reddit.com/r/PPC/comments/1qk7qw4/worse_overall_results_after_splitting_out_branded/
- **CTR-20260907-0531-012** — A Singapore intimate-apparel brand held 2.5-3.5x ROAS for four months, then fell to ~1.5x despite extensive creative and persona iteration. Source: https://www.reddit.com/r/ecommerce/comments/1qn4eya/from_35x_roas_to_15x_in_6_months_20k_invested_now/
- **CTR-20260907-0531-013** — A zero-ad-spend Etsy digital shop reached 85 orders and $503.78 revenue from 2,819 visits in its first month. Source: https://www.reddit.com/r/EtsySellers/comments/1qoqunx/first_month_selling_digital_products_started_jan/
- **CTR-20260907-0531-014** — PGCART's Week 2 AOV rose ₹44.63→₹49.04 and delivered revenue rose despite lower volume, but 14.42% of orders cancelled. Source: https://www.reddit.com/r/StartupIdeasIndia/comments/1w8lwz2/pgcart_week_2_performance_august_1521_2026/
- **CTR-20260907-0531-015** — Fixing all Merchant Center disapprovals did not restore a previously healthy PMax campaign; delivery stayed at zero even after budget/tROAS loosening. Source: https://support.google.com/google-ads/thread/461259956/performance-max-campaign-stuck-at-0-impressions-after-fixing-merchant-center-disapprovals?hl=en-7-0
- **CTR-20260907-0531-016** — An approved US Shopping campaign remained at zero impressions; operator raised budget $20/day as a diagnostic intervention. Source: https://support.google.com/google-ads/thread/459656345/my-shopping-ads-are-set-up-and-approved-but-aren-t-getting-impressions?hl=en-GB
- **CTR-20260907-0531-018** — An online-only reseller spent ~8 months correcting identity/feed trust signals but Merchant Center Misrepresentation remained and appeal capacity was exhausted. Source: https://community.shopify.com/t/google-merchant-center-misrepresentation-suspension-for-8-months-appeals-exhausted-any-similar-cases/666324
- **CTR-20260907-0531-020** — After switching to Shopify Payments, one store reported sales down 46% despite traffic up 22% and normal ATC, localizing the break near checkout/payment. Source: https://community.shopify.com/t/sales-plummeted-shortly-after-activating-shopify-payments/588571

## Foreign-market / transplant signals

- **New Zealand:** a niche store with 500+ customers and ~1.6-1.8x self-managed ROAS fell to 0.8x then 0.6x after agency migration to PMax+broad and a higher budget. Source: https://www.reddit.com/r/PPC/comments/1l54t55/agency_switched_to_pmax_broad_matchroas_collapsed/
- **Singapore:** intimate apparel worked at 2.5-3.5x ROAS initially but later stuck near 1.5x despite extensive creative/persona iteration, a useful saturation prior for small-TAM consumer brands. Source: https://www.reddit.com/r/ecommerce/comments/1qn4eya/from_35x_roas_to_15x_in_6_months_20k_invested_now/
- **India:** PGCART's public week-over-week trace shows AOV increasing from ₹44.63 to ₹49.04 while cancellations remained 14.42%, useful for hyperlocal/COD economics. Source: https://www.reddit.com/r/StartupIdeasIndia/comments/1w8lwz2/pgcart_week_2_performance_august_1521_2026/

## Source-yield changes

- **r/PPC post-Aug-17 bidding threads:** HIGH — dense pre/post metrics and target/budget interventions
- **Google Ads Community serving-state threads:** HIGH — hidden account/feed eligibility states, fewer outcome closures
- **Shopify Community checkout/payment threads:** HIGH — strong funnel localization and platform-state evidence
- **r/dropshipping/general ecom:** MEDIUM — useful first-month cases but more filtering needed
- **local-language Nordic sensors:** LOW this run — searched, but no fresh quantitative operator traces cleared the bar

## Compact accepted-record table

| ID | Grade | Market | Probe | Claim |
|---|---:|---|---|---|
| CTR-20260907-0531-001 | A | unknown | ACTION_OUTCOME/PROFITABLE_THEN_COLLAPSED | A historically 700-800% ROAS account fell to ~350% after aligning tROAS to recent actual performance around the Aug 17 bidding change. |
| CTR-20260907-0531-002 | A | unknown | ACTION_OUTCOME/PROFITABLE_SPARSE | Raising tROAS 900→1100% was followed by lower spend and ~20% lower sales within two weeks. |
| CTR-20260907-0531-003 | B | unknown | ACTION_OUTCOME/SALES_UNPROFITABLE | A profitable Standard Shopping account saw CPC jump roughly 9x, from $1.30 to $11-12, over ~11 days. |
| CTR-20260907-0531-004 | A | unknown | ACTION_OUTCOME/CATALOG_DYNAMICS | Removing brand terms from PMax and shifting them to Search reduced conversion quality and slightly lowered business revenue within days. |
| CTR-20260907-0531-005 | A | unknown | ACTION_OUTCOME/CATALOG_DYNAMICS | A high-volume high-ticket Standard Shopping account deteriorated after Aug 17: CPC up, CVR down, query mix broadened. |
| CTR-20260907-0531-006 | A | unknown | ACTION_OUTCOME/OPERATOR_TIMELINE | A bestseller stockout plus SKU merge was followed by a two-week order decline that did not recover promptly after restocking. |
| CTR-20260907-0531-007 | A | EU | HIDDEN_ECONOMICS/TRACKING_ANOMALY | A beauty store's apparent 0.07% CVR was materially distorted by bot traffic; operator recalculated human CVR near 0.18%. |
| CTR-20260907-0531-008 | B | unknown | LOW_CAPITAL/FAILURE_ATLAS | A fitness-accessory launch spent ~$800 on Meta for 4 sales and $140 revenue in its first five weeks. |
| CTR-20260907-0531-009 | A | NZ | ACTION_OUTCOME/PROFITABLE_THEN_COLLAPSED | An NZ store fell from ~1.6-1.8x ROAS to 0.8x/0.6x after an agency replaced Shopping+exact Search with PMax+broad while raising budget. |
| CTR-20260907-0531-010 | A | unknown | ACTION_OUTCOME/CATALOG_DYNAMICS | Splitting 37 proven winners from a 3,800-SKU campaign reset performance: €250 over five days yielded zero sales despite the parent campaign's ~4.5 ROAS. |
| CTR-20260907-0531-011 | A | unknown | ACTION_OUTCOME/SALES_UNPROFITABLE | A two-year ~6x-ROAS PMax setup broke after a $65→$100/day increase; later brand splitting did not simply recreate the old outcome. |
| CTR-20260907-0531-012 | C | SG | ACTION_OUTCOME/PROFITABLE_THEN_COLLAPSED | A Singapore intimate-apparel brand held 2.5-3.5x ROAS for four months, then fell to ~1.5x despite extensive creative and persona iteration. |
| CTR-20260907-0531-013 | B | unknown | LOW_CAPITAL/OPERATOR_TIMELINE | A zero-ad-spend Etsy digital shop reached 85 orders and $503.78 revenue from 2,819 visits in its first month. |
| CTR-20260907-0531-014 | A | IN | OPERATOR_TIMELINE/HIDDEN_ECONOMICS | PGCART's Week 2 AOV rose ₹44.63→₹49.04 and delivered revenue rose despite lower volume, but 14.42% of orders cancelled. |
| CTR-20260907-0531-015 | A | unknown | NO_DELIVERY/ACTION_OUTCOME | Fixing all Merchant Center disapprovals did not restore a previously healthy PMax campaign; delivery stayed at zero even after budget/tROAS loosening. |
| CTR-20260907-0531-016 | B | US | NO_DELIVERY/ACTION_OUTCOME | An approved US Shopping campaign remained at zero impressions; operator raised budget $20/day as a diagnostic intervention. |
| CTR-20260907-0531-017 | B | unknown | NO_DELIVERY/TRACKING_ANOMALY | A reactivated dormant account showed eligible campaigns but zero lifetime impressions across three builds, consistent with a hidden dormancy hold. |
| CTR-20260907-0531-018 | A | US | SUPPLIER_ANOMALY/ACTION_OUTCOME | An online-only reseller spent ~8 months correcting identity/feed trust signals but Merchant Center Misrepresentation remained and appeal capacity was exhausted. |
| CTR-20260907-0531-019 | B | GB | CHECKOUT_NO_PURCHASE/FAILURE_ATLAS | A UK Shopify store sent 150 of 2,191 sessions to checkout in 15 days but completed zero purchases. |
| CTR-20260907-0531-020 | A | unknown | ACTION_OUTCOME/CHECKOUT_NO_PURCHASE | After switching to Shopify Payments, one store reported sales down 46% despite traffic up 22% and normal ATC, localizing the break near checkout/payment. |

## Coverage gaps

- Norway/Finland fresh native-language operator economics were sparse this hour; no weak local records were padded in.
- Supplier-change -> measured shipping/CVR outcomes remain under-covered.
- COGS/net profit remain missing in most ad-platform cases.
- Several August-17 Google Ads cases need 7/14/30-day follow-ups to separate update effects from relearning/seasonality.
- Need more product-specific country-transplant evidence rather than general logistics friction.

## Attachments

- `records.jsonl` — normalized append-ready records
- `records.csv` — flat export
- `run_manifest.json` — run/source-yield/coverage metadata
