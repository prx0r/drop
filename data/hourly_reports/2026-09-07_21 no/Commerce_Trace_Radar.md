# [Commerce Trace Radar] 2026-09-07 03:00 — 21 novel records

# Commerce Trace Radar — 21 accepted novel records

## Executive summary

This run accepted 21 novel records after checking recent sent reports and rejecting obvious repeats. The dominant pattern is measurement-and-state risk: a campaign can appear profitable because purchase events are duplicated, or appear to collapse because a migration, goal cleanup, payment bug, or bidding reset changes the optimization substrate. These events should be modeled as explicit state changes, not incidental campaign notes.

A second pattern is that successful ecommerce frequently hits an economic ceiling before a traffic ceiling. Several current stores are generating hundreds of orders while net margin remains ~5–7%, or are profitable but cannot spend their nominal budget because tROAS constraints and auction rank cap volume. This reinforces the need to separate SALES_EXIST from PROFITABLE_SCALABLE.

A third pattern is checkout-stage failure in high-value/localized markets. India and GCC traces show large visitor volumes and meaningful ATC intent collapsing between checkout and payment, while Norway/Finland continue to show cross-border landed-cost friction that can support a local-stock specialist thesis.

Run stats: 21 accepted / 73 reviewed / 18 duplicates or near-duplicates skipped. Evidence: 9 A-grade, 12 B-grade.

## Top 3 highest-signal findings

### 1. A 48h pause plus previously duplicated purchase tracking exposed that an apparent 8x-ROAS campaign was actually near 1x and failed to recover for 40+ days.
- Before: Historically reported ~800% ROAS, but tracking was later found to be duplicated
- Action: Paused main campaign for ~48h, reactivated it, then discovered two primary purchase goals had been double-counting conversions
- After: 40+ days later still near break-even/worse; last 30d $3,000 spend, $3,150 revenue, $2,900 product cost, ~1.05x ROAS
- Evidence grade: A
- Source: https://support.google.com/google-ads/thread/445108689/paused-campaign-48hrs-roas-crashed-800-%E2%86%921x-found-duplicate-tracking-40-days-no-recovery-need-reb?hl=en

### 2. An Indian premium-fashion store deteriorated from regular weekly sales to 13 checkouts and zero orders despite historically completing ~30-35% of checkouts.
- Before: Recent weekly sequence: 9,112 sessions→11 orders; 2,917→12; 2,743→4; historical checkout completion ~30-35%
- Action: Operator investigated payment gateway after progressive sales decline
- After: Latest week: 2,338 sessions, 122 ATCs, 13 checkouts, 0 orders; traffic down ~74% from peak
- Evidence grade: A
- Source: https://www.reddit.com/r/shopify/comments/1uywoxk/shopify_sales_have_suddenly_fallen_off_used_to/

### 3. A profitable single-product Shopping account reached ~70 orders but progressively under-spent after moving to tROAS despite headroom above breakeven.
- Before: ~70 orders in last 30 days; actual ROAS ~2.0-2.1x, profitable vs ~1.43x breakeven
- Action: After ~30 conversions, switched from Maximize Clicks to tROAS 2.5x; later price increased and tROAS lowered toward 2x
- After: Google progressively spent less of daily budget despite recommendations to raise budget; account remained profitable but volume-constrained
- Evidence grade: A
- Source: https://www.reddit.com/r/PPC/comments/1vw3ali/shopping_ads_wont_spend_full_daily_budgettroas/

## Longitudinal / action→outcome cases

- **CTR-20260907-0333-001** — A 48h pause plus previously duplicated purchase tracking exposed that an apparent 8x-ROAS campaign was actually near 1x and failed to recover for 40+ days. Source: https://support.google.com/google-ads/thread/445108689/paused-campaign-48hrs-roas-crashed-800-%E2%86%921x-found-duplicate-tracking-40-days-no-recovery-need-reb?hl=en
- **CTR-20260907-0333-002** — Repeated budget increases and tROAS loosening failed to unlock spend for a profitable best-seller Shopping campaign. Source: https://www.reddit.com/r/googleads/comments/1rdfuxp/shopping_campaign_stuck_budget_not_spending_61_is/
- **CTR-20260907-0333-004** — A new Indian luxury account went from 20 January sales at ~4x ROAS to zero February sales with traffic still arriving. Source: https://www.reddit.com/r/googleads/comments/1r4qa0s/new_to_google_ads_20_sales_in_jan_0_in_feb_is_my/
- **CTR-20260907-0333-005** — A domain migration left PMax anchored to two huge early orders, producing a misleading 11.77x ROAS while later conversion volume largely disappeared. Source: https://www.reddit.com/r/googleads/comments/1tn1cc3/pmax_campaign_tanked_after_domain_migration_now/
- **CTR-20260907-0333-006** — Cleaning inflated PMax goals exposed an 87% ROAS and weaker delivery for an Australian supplements store. Source: https://www.reddit.com/r/googleads/comments/1sefy3j/looking_for_google_ads_expert_to_assist_me/
- **CTR-20260907-0333-007** — A profitable single-product Shopping account reached ~70 orders but progressively under-spent after moving to tROAS despite headroom above breakeven. Source: https://www.reddit.com/r/PPC/comments/1vw3ali/shopping_ads_wont_spend_full_daily_budgettroas/
- **CTR-20260907-0333-008** — A profitable premium dog-gear PMax account collapsed to £0 revenue and then failed to regain delivery after moving to Standard Shopping. Source: https://www.reddit.com/r/googleads/comments/1vub92d/pmax_and_shop/
- **CTR-20260907-0333-010** — An Indian premium-fashion store deteriorated from regular weekly sales to 13 checkouts and zero orders despite historically completing ~30-35% of checkouts. Source: https://www.reddit.com/r/shopify/comments/1uywoxk/shopify_sales_have_suddenly_fallen_off_used_to/
- **CTR-20260907-0333-013** — An EU niche store reached 2-3 sales/day and a 10-order peak yet remained ~€700 underwater after full operating costs. Source: https://www.reddit.com/r/dropshipping/comments/1tjcn1i/stuck_at_dropshipping_eu/
- **CTR-20260907-0333-014** — A first-week store raised prices without losing its 5.5% CVR, but $988 ad spend still consumed nearly all $1,060 revenue. Source: https://www.reddit.com/r/dropshipping/comments/1upeock/20_sales_in_my_first_week_but_im_basically/
- **CTR-20260907-0333-015** — A bundle test raised AOV and margin but reduced order volume; 224 orders and $11.8k revenue still produced only ~$752 net profit. Source: https://www.reddit.com/r/dropshipping/comments/1uu3tqp/224_orders_118k_sales_but_752_profit/
- **CTR-20260907-0333-016** — Checkout abandonment reportedly jumped to 70-80% after new app/testing changes, with a plausible mix of true friction and measurement distortion. Source: https://community.shopify.com/t/after-post-purchase-and-clarity-app-abandoned-checkout-rate-jumped-to-70-80/588987/11
- **CTR-20260907-0333-017** — Discount popup, lower pricing and added trust elements failed to fix a store whose Meta top-funnel metrics looked healthy but purchases remained weak. Source: https://www.reddit.com/r/shopify/comments/1s59n0n/my_shopify_sites_conversion/

## Hidden-economics cases

- **CTR-20260907-0333-003** — A custom-product account with ~$1,400 average web sale delivered 20 conversions and 3.16 ROAS, heavily concentrated in PMax. Source: https://www.reddit.com/r/googleads/comments/1rkmfls/boss_wants_to_fire_googleads_agency_and_run_ads/
- **CTR-20260907-0333-009** — An Indian PC/antivirus Shopping campaign hit ~₹500 CPC with no sales, prompting an emergency return to Manual CPC. Source: https://support.google.com/google-ads/thread/447046089/need-advice-troubleshooting-extremely-high-cpc-shopping-campaign-optimization?hl=en
- **CTR-20260907-0333-012** — A 29-order store still lost ~£160-£200: Meta generated all sales while £100 TikTok spend generated none. Source: https://www.reddit.com/r/dropship/comments/1vww9q5/dropshipping_store_with_29_orders_but_currently/
- **CTR-20260907-0333-014** — A first-week store raised prices without losing its 5.5% CVR, but $988 ad spend still consumed nearly all $1,060 revenue. Source: https://www.reddit.com/r/dropshipping/comments/1upeock/20_sales_in_my_first_week_but_im_basically/
- **CTR-20260907-0333-015** — A bundle test raised AOV and margin but reduced order volume; 224 orders and $11.8k revenue still produced only ~$752 net profit. Source: https://www.reddit.com/r/dropshipping/comments/1uu3tqp/224_orders_118k_sales_but_752_profit/
- **CTR-20260907-0333-018** — Back-to-school scaling produced $9.7k revenue and 176 orders but only ~$601 net profit despite 2.39 ROAS. Source: https://www.reddit.com/r/dropshipping/comments/1vplu7n/97k_sales_176_orders_but_601_profit/
- **CTR-20260907-0333-019** — A summer product generated 261 orders and $10.6k revenue but only ~$519 net profit, illustrating the low-AOV volume trap. Source: https://www.reddit.com/r/dropshipping/comments/1uhxqae/261_orders_106k_sales_but_519_profit/

## Foreign-market / transplant signals

- **NO / CTR-20260907-0333-020** — Norwegian cross-border buyers can face an unexpected NOK 195 UPS handling fee even when they did not choose the carrier. Source: https://www.reddit.com/r/Norway/comments/1qjo93n/ups_how_is_this_legal/
- **FI / CTR-20260907-0333-021** — Finland added a €3 per-parcel friction for cheap non-EU imports, weakening ultra-low-ticket cross-border economics. Source: https://www.reddit.com/r/Finland/comments/1tniep2/finnish_customs_to_introduce_new_levies_on_cheap/

## Source-yield updates

- **r/googleads + r/PPC:** HIGH — strongest current paid-search transition/economics yield
- **Google Ads Community:** HIGH — particularly valuable for tracking corruption and extreme CPC cases
- **r/dropshipping / r/dropship:** MEDIUM-HIGH — best for real P&L and intervention economics, but self-report bias remains
- **r/shopify:** HIGH for checkout-stage numeric traces
- **Shopify Community:** MEDIUM — useful app/checkout anomalies but fewer hard outcomes
- **Nordic country subreddits:** MEDIUM — strong transplant friction, weaker operator economics

## Compact accepted-record table

| ID | Grade | Market | Probe | Summary |
|---|---:|---|---|---|
| CTR-20260907-0333-001 | A | unknown | ACTION_OUTCOME/TRACKING_ANOMALY | A 48h pause plus previously duplicated purchase tracking exposed that an apparent 8x-ROAS campaign was actually near 1x and failed to recover for 40+ days. |
| CTR-20260907-0333-002 | A | EU | ACTION_OUTCOME/PROFITABLE_SPARSE | Repeated budget increases and tROAS loosening failed to unlock spend for a profitable best-seller Shopping campaign. |
| CTR-20260907-0333-003 | B | unknown | HIDDEN_ECONOMICS/PROFITABLE_SPARSE | A custom-product account with ~$1,400 average web sale delivered 20 conversions and 3.16 ROAS, heavily concentrated in PMax. |
| CTR-20260907-0333-004 | A | IN | PROFITABLE_THEN_COLLAPSED/OPERATOR_TIMELINE | A new Indian luxury account went from 20 January sales at ~4x ROAS to zero February sales with traffic still arriving. |
| CTR-20260907-0333-005 | A | AU | ACTION_OUTCOME/TRACKING_ANOMALY | A domain migration left PMax anchored to two huge early orders, producing a misleading 11.77x ROAS while later conversion volume largely disappeared. |
| CTR-20260907-0333-006 | A | AU | ACTION_OUTCOME/TRACKING_ANOMALY | Cleaning inflated PMax goals exposed an 87% ROAS and weaker delivery for an Australian supplements store. |
| CTR-20260907-0333-007 | A | unknown | ACTION_OUTCOME/PROFITABLE_SPARSE | A profitable single-product Shopping account reached ~70 orders but progressively under-spent after moving to tROAS despite headroom above breakeven. |
| CTR-20260907-0333-008 | A | GB | ACTION_OUTCOME/PROFITABLE_THEN_COLLAPSED | A profitable premium dog-gear PMax account collapsed to £0 revenue and then failed to regain delivery after moving to Standard Shopping. |
| CTR-20260907-0333-009 | B | IN | SALES_UNPROFITABLE/HIDDEN_ECONOMICS | An Indian PC/antivirus Shopping campaign hit ~₹500 CPC with no sales, prompting an emergency return to Manual CPC. |
| CTR-20260907-0333-010 | A | IN | OPERATOR_TIMELINE/CHECKOUT_NO_PURCHASE | An Indian premium-fashion store deteriorated from regular weekly sales to 13 checkouts and zero orders despite historically completing ~30-35% of checkouts. |
| CTR-20260907-0333-011 | B | GCC | FAILURE_ATLAS/CHECKOUT_NO_PURCHASE | A GCC fashion store showed unusually high 24% ATC but only 4.1% checkout reach and 2.7% purchase across 153k sessions. |
| CTR-20260907-0333-012 | B | unknown | HIDDEN_ECONOMICS/SALES_UNPROFITABLE | A 29-order store still lost ~£160-£200: Meta generated all sales while £100 TikTok spend generated none. |
| CTR-20260907-0333-013 | B | EU | OPERATOR_TIMELINE/SALES_UNPROFITABLE | An EU niche store reached 2-3 sales/day and a 10-order peak yet remained ~€700 underwater after full operating costs. |
| CTR-20260907-0333-014 | A | US/CA | ACTION_OUTCOME/HIDDEN_ECONOMICS | A first-week store raised prices without losing its 5.5% CVR, but $988 ad spend still consumed nearly all $1,060 revenue. |
| CTR-20260907-0333-015 | B | unknown | ACTION_OUTCOME/HIDDEN_ECONOMICS | A bundle test raised AOV and margin but reduced order volume; 224 orders and $11.8k revenue still produced only ~$752 net profit. |
| CTR-20260907-0333-016 | B | unknown | ACTION_OUTCOME/CHECKOUT_NO_PURCHASE | Checkout abandonment reportedly jumped to 70-80% after new app/testing changes, with a plausible mix of true friction and measurement distortion. |
| CTR-20260907-0333-017 | B | unknown | ACTION_OUTCOME/CLICKS_NO_ATC | Discount popup, lower pricing and added trust elements failed to fix a store whose Meta top-funnel metrics looked healthy but purchases remained weak. |
| CTR-20260907-0333-018 | B | unknown | HIDDEN_ECONOMICS/SALES_UNPROFITABLE | Back-to-school scaling produced $9.7k revenue and 176 orders but only ~$601 net profit despite 2.39 ROAS. |
| CTR-20260907-0333-019 | B | unknown | HIDDEN_ECONOMICS/SALES_UNPROFITABLE | A summer product generated 261 orders and $10.6k revenue but only ~$519 net profit, illustrating the low-AOV volume trap. |
| CTR-20260907-0333-020 | B | NO | COUNTRY_TRANSPLANT/MERCHANT_FRICTION | Norwegian cross-border buyers can face an unexpected NOK 195 UPS handling fee even when they did not choose the carrier. |
| CTR-20260907-0333-021 | B | FI | COUNTRY_TRANSPLANT/MERCHANT_FRICTION | Finland added a €3 per-parcel friction for cheap non-EU imports, weakening ultra-low-ticket cross-border economics. |

## Open-case follow-up queue

- Revisit the 48h-pause/duplicate-tracking case for any later clean-tracking recovery data.
- Revisit the Indian luxury Jan→Feb collapse after the seasonal Valentine period.
- Revisit the Australian supplements goal-cleanup case after enough purchase-only learning accumulates.
- Revisit the premium dog-gear PMax→Standard Shopping transition for recovery or final abandonment.
- Revisit the single-product profitable-under-spend case after additional tROAS/budget changes.
- Search for later outcome of India premium-fashion payment-gateway investigation.

## Coverage gaps

- Supplier-switch → measured shipping/CVR outcomes remain sparse.
- Fresh Finnish merchant/operator margin traces remain weaker than consumer/regulatory evidence.
- Several PMax/Shopping collapse cases still lack later recovery updates.
- Many dropshipping P&L posts disclose net profit but not refund/chargeback composition.
- Need more $0/free-listing first-sale timelines from 2026 that have a later update.

## Attachments

- records.jsonl — normalized append-ready records
- records.csv — flat export
- run_manifest.json — run metadata, source-yield and coverage gaps
