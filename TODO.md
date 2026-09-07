# Drop Project — TODOs

*Last updated: 2026-09-06*

---

## 10 Priority TODOs

### 1. Apply for Google Ads Standard Access
**Status:** Pending
**Action:** Go to https://ads.google.com/aw/apicenter → apply for Basic or Standard access
**Why:** Current developer token only works with test accounts. Need production access for Keyword Planner and real campaign data.
**Blocked on:** Manual application (3-5 business days)
**File:** `/root/googleapi.md`

### 2. Pull Merchant Center Popular Products
**Status:** Ready to run
**Action:** Run `python3 services/research/pipeline_v2.py --step merchant`
**Why:** First-party demand signal for Norway/Finland/Denmark/Sweden. Better than any third-party tool.
**Blocked on:** API registration may need 5 minutes to propagate
**File:** `data/merchant_popular_products.json`

### 3. Build Prisjakt Scraper
**Status:** Not started
**Action:** Scrape seller count, price history, stock status for top products in NO/FI/SE/DK
**Why:** Free structured competitor database. Gives us `GOOD_SELLER_GAP` metric.
**Output:** `data/prisjakt_products.json`
**Approach:** Python requests + BeautifulSoup, respect rate limits, cache results

### 4. Refresh Candidate Scoring with Live Data
**Status:** Blocked on #2 and #3
**Action:** Re-score all candidates in `real_candidates.json` with Merchant Center + Prisjakt data
**Why:** Current scores are based on estimates. Need real demand and competition data.
**File:** `data/scored_candidates.json`

### 5. Set Up Free Listings Test Store
**Status:** Not started
**Action:** Create local-language WooCommerce store for Norway, add 20 products, enable Google free listings
**Why:** Zero-cost market validation. See which products get impressions, which queries drive traffic.
**Requirements:** WooCommerce store, Merchant Center feed, Norwegian language content
**File:** `apps/store/`

### 6. Wire Operator Events to Auto-Record
**Status:** Not started
**Action:** Modify `pipeline_v2.py` to automatically log every scoring decision and test outcome
**Why:** `data/operator_events.json` has 21 manual entries. Need automated recording for the data flywheel.
**Output:** `data/operator_events.json` (auto-appended)
**Schema:** See `corpus/schemas/action_log.json`

### 7. Clean Up Data Duplication
**Status:** Not started
**Action:** Remove duplicates between `data/`, `corpus/`, and `research/`. Canonical location: `data/`
**Why:** Three copies of the same files causes confusion. `corpus/` should reference `data/`, not duplicate it.
**Files:** `corpus/sources/sources.json`, `research/data/*`, `data/*`

### 8. Connect Drop Scoring to Lab (WorkerKit/HydraDB)
**Status:** Not started
**Action:** Wire `packages/scoring/` into the MWGym loop for tracking and evolution
**Why:** The scoring engine exists but isn't part of the 21-step loop. Needs integration for tracking.
**Requirements:** HydraDB adapter, WorkerKit venue

### 9. Build Keyword Planner Integration
**Status:** Blocked on #1
**Action:** Once Standard access approved, build keyword research pipeline per product per country
**Why:** Demand × CPC matrix is the core input for `ECONOMIC_HEADROOM` calculation
**Output:** `data/keyword_data.json`
**File:** `services/research/pipeline_v2.py` (step_keywords)

### 10. Ship First Store — Norway
**Status:** Blocked on #5
**Action:** Launch lean catalog store in Norway with 20-50 products, free listings first, $5/day paid test after
**Why:** End-to-end validation of the foreign-product scanner thesis
**Timeline:** 30 days from free listings to scale/kill decision
**File:** `output/LAUNCH_PLAN.md`

---

## Dependency Graph

```
#1 (Ads access) ──────────→ #9 (Keyword Planner)
                                        ↓
#2 (Merchant data) ──→ #3 (Prisjakt) ──→ #4 (Re-score)
                                                ↓
                                        #5 (Free listings store)
                                                ↓
                                        #10 (Ship first store)

#6 (Auto-record) ──→ #8 (Lab integration)
#7 (Clean data) ──→ (parallel, do anytime)
```

---

## Quick Wins (Do Now)

- [ ] Apply for Google Ads Standard access (#1)
- [ ] Run Merchant Center Popular Products pull (#2)
- [ ] Clean up data duplication (#7)
- [ ] Set up auto-recording of operator events (#6)

## Blocked On External

- [ ] Google Ads approval (3-5 business days)
- [ ] WooCommerce store setup (needs deployment)
- [ ] Prisjakt scraping (needs testing with live site)

## Completed

- [x] Google OAuth flow — tokens obtained and saved
- [x] Merchant Center API — registered and working
- [x] Google Ads API — connected (test mode)
- [x] Cloudflare DNS — verification record added
- [x] Cloudflare Worker — verification file served
- [x] Credential vault — all 8 Google keys saved
- [x] reviewdrop.md — full strategic review
- [x] insights.md — foreign-product scanner pipeline
- [x] pipeline_v2.py — report ingestion pipeline
