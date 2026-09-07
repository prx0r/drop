# API Stack — Dropshipping Opportunity Engine
*Updated: 2026-09-06*

## Principle

Start with $0 additional API spend. Use what we already own. The only real money should go into actual clicks once candidates pass economic filters.

---

## What We Use NOW (Phase 1 — Research)

| Need | Use | Cost |
|------|-----|------|
| Search volume + CPC + bid ranges | **Google Ads API / Keyword Planner** | $0 API cost |
| Live Shopping competitors/prices/shipping | **SerpApi** (~500 credits left) | $0 (already paid) |
| Trends/seasonality | **SerpApi Google Trends** | $0 with credits |
| Product feed + free Shopping listings | **Merchant Center + Merchant API v1** | $0 |
| Organic query data after launch | **Search Console API** | $0 |
| Merchant history/Best Sellers later | **BigQuery transfer** | ~$0 at our scale |
| Weird supplier sites | requests/Playwright first, Apify if needed | $0 initially |
| Large-scale Shopping research later | DataForSEO | Don't buy yet |

---

## What We Already Own

| Credential | Value | Vault Key |
|------------|-------|-----------|
| SerpApi Key | `0f9f1e0...` | `SERPAPI_API_KEY` |
| Cloudflare API Token | `cfat_zxMk0x...` | `CLOUDFLARE_API_TOKEN` |
| Cloudflare Account ID | `954612af...` | `CLOUDFLARE_ACCOUNT_ID` |
| Cloudflare R2 Access Key | `6fd280af...` | `CLOUDFLARE_R2_ACCESS_KEY` |
| Cloudflare R2 Secret Key | `99edd0da...` | `CLOUDFLARE_R2_SECRET_KEY` |
| OpenCode API Key | Live | `OPENCODE_API_KEY` |

---

## #1 PRIORITY: Google Ads API

This is the single most important credential we don't have yet.

Without credible `expected_CPC`, we can't distinguish good from bad before spending money:

```
GOOD
  Contribution/order     £250
  Expected CPC            £0.80
  Realistic CVR             0.8%
  Headroom                 2.50×

BAD
  Contribution/order      £30
  Expected CPC            £2.10
  Realistic CVR             2%
  Headroom                 0.29×
```

The lumbar-pillow failure was the second scenario. $65 product, $2.13 CPC. Even great CVR couldn't rescue it.

The $10k/day case was the first. $300-500 products meant every conversion was worth enough that 0.48% CVR still worked.

### How to set up

1. Go to **ads.google.com** → Tools → Billing → create manager account if needed
2. Go to **API Center** → apply for developer token
3. Google offers Explorer access: 2,880 operations/day (vastly more than we need)
4. Create OAuth2 credentials in Google Cloud Console
5. Store in vault:

```bash
agent-vault vault credential set GOOGLE_ADS_DEVELOPER_TOKEN="..." --vault oracle
agent-vault vault credential set GOOGLE_ADS_CUSTOMER_ID="..." --vault oracle
agent-vault vault credential set GOOGLE_ADS_REFRESH_TOKEN="..." --vault oracle
agent-vault vault credential set GOOGLE_CLIENT_ID="..." --vault oracle
agent-vault vault credential set GOOGLE_CLIENT_SECRET="..." --vault oracle
```

### What we get

For every `PRODUCT × COUNTRY × QUERY`:

- Average monthly searches
- Monthly search history (12 months)
- Competition index
- 20th percentile bid
- 80th percentile bid
- Average CPC
- Forecast impressions/clicks/cost

Google specifically recommends caching because historical metrics refresh monthly.

---

## How to Spend the 500 SerpApi Credits

Not random products. Strategic allocation:

### Research Phase (150 searches)

```
100 plausible product families
  ↓
30 serious candidates (filtered by economics)
  ↓
10 deep dives
```

For each of the 30 candidates, run 5 queries:

1. Generic commercial query → Shopping results
2. Exact product query → Shopping results
3. Exact model query → Shopping results
4. Feature/use-case query → Shopping results
5. Google Trends → seasonality

```
30 candidates × 5 = 150 searches
```

### Country Comparison (100-200 searches)

For top 10 candidates, compare across countries:

```
Eureka Mignon Specialita
  → UK Shopping
  → Norway Shopping
  → Denmark Shopping
  → Sweden Shopping
```

This creates a real geographic competition matrix.

### Reserve (150-250 searches)

For ad-hoc investigation during store operation.

### What SerpApi gives us per Shopping query

```
country, location, language
position, product_id, title
seller/source, price, delivery
rating, review count
multiple sellers per product
```

This catches the exact-SKU saturation problem that killed the 165-click zero-sale case.

---

## What We Need at Launch (Phase 2)

### Google Merchant Center

1. Go to **merchants.google.com**
2. Create/claim Merchant account
3. Apply for Merchant API v1 access (not the deprecated Content API)
4. Verify and claim website
5. Set up product feed

Store in vault:

```bash
agent-vault vault credential set GOOGLE_MERCHANT_ID="..." --vault oracle
```

### What we get

- Free Shopping listings (the $0 traffic source)
- Product approval/disapproval status
- Feed issues and diagnostics
- Free listing impressions and clicks
- Price competitiveness data

This is Helena's feedback loop:

```
300 products → traffic → query analysis → delete 95% → concentrate → profitable
```

### Search Console

1. Go to **search.google.com/search-console**
2. Verify domain ownership
3. Connect to BigQuery for historical storage

Store in vault:

```bash
agent-vault vault credential set SEARCH_CONSOLE_SITE_URL="..." --vault oracle
```

---

## What We Set Up Free (Phase 2-3)

### BigQuery

- Create dataset in GCP console
- Enable Merchant Center transfer
- Free tier: first 1 TiB queries/month (we'll use nothing)

Datasets available:

| Dataset | What | Backfill |
|---------|------|----------|
| Performance | Ads + free listing performance | Yes |
| Best Sellers | Popular products/brands | Up to 2 years |
| Price Competitiveness | Product × country daily benchmarks | No (start collecting immediately) |
| Price Insights | Suggested prices | No |

```bash
agent-vault vault credential set GOOGLE_CLOUD_PROJECT="..." --vault oracle
agent-vault vault credential set BIGQUERY_DATASET="..." --vault oracle
```

### Apify

- Free tier: $5 monthly platform credit
- Only use for JavaScript-heavy catalogs, awkward pagination, anti-bot sites
- Normal manufacturer websites → crawl ourselves with requests/Playwright

---

## What NOT to Buy Yet

| Tool | Why Not |
|------|---------|
| DataForSEO | SerpApi covers Shopping + Trends + SERPs. Revisit when credits exhaust AND model shows value |
| Minea | Doesn't solve core problem as cleanly as Google APIs + our scoring |
| AutoDS | Same |
| Sell The Trend | Same |
| EverBee | Same |
| Premium Apify | Free tier sufficient for now |

**Your first money outside the actual business should not go to another API.**

It should go into the only data source nobody can fake:

> A few dollars of real clicks from actual buyers once a candidate passes economic filters.

---

## Architecture

```
                    OPPORTUNITY ENGINE

 ┌──────────────── GOOGLE ───────────────────┐
 │                                           │
 │ Ads API        Merchant API     Trends    │
 │ (Keyword)      (products)      (SerpApi) │
 │    ↓                ↓              ↓      │
 │ search/CPC      products/data    trend    │
 │                                           │
 │ Search Console       BigQuery              │
 │      ↓                   ↓                 │
 │ organic intent       market history        │
 └───────────────┬───────────────────────────┘
                 │
                 ▼
           NORMALIZED DB
                 ▲
                 │
           SerpApi (Shopping sellers/prices)
           Our crawler (supplier sites)
                 │
                 ▼
           ECONOMIC MODEL
                 ↓
        HARD GATES + SCORE
                 ↓
          FREE-LISTING TEST
                 ↓
            $0 → $10/day
```

---

## Setup Checklist

### Tonight (10 min)

- [ ] Apply for Google Ads API developer token — ads.google.com → Tools → API Center
- [ ] Create Google Cloud project — console.cloud.google.com → New Project
- [ ] Enable APIs: Merchant API, Google Ads API, Search Console API, BigQuery API
- [ ] Create OAuth2 credentials (Desktop app type)

```bash
# Store what you get
agent-vault vault credential set GOOGLE_ADS_DEVELOPER_TOKEN="..." --vault oracle
agent-vault vault credential set GOOGLE_CLIENT_ID="..." --vault oracle
agent-vault vault credential set GOOGLE_CLIENT_SECRET="..." --vault oracle
```

### This Week

- [ ] Set up Merchant Center — merchants.google.com → create account
- [ ] Apply for Merchant API v1 access (not deprecated Content API)
- [ ] Verify domain — search.google.com/search-console
- [ ] Create OAuth2 refresh token for Ads API

```bash
agent-vault vault credential set GOOGLE_ADS_CUSTOMER_ID="..." --vault oracle
agent-vault vault credential set GOOGLE_ADS_REFRESH_TOKEN="..." --vault oracle
agent-vault vault credential set GOOGLE_MERCHANT_ID="..." --vault oracle
agent-vault vault credential set SEARCH_CONSOLE_SITE_URL="..." --vault oracle
```

### At Launch

- [ ] Verify and claim website in Merchant Center
- [ ] Set up product feed (correct GTINs, titles, images, shipping)
- [ ] Enable free listings (the $0 traffic source)
- [ ] Connect Merchant Center → BigQuery transfer
- [ ] Start collecting organic query data

```bash
agent-vault vault credential set GOOGLE_CLOUD_PROJECT="..." --vault oracle
agent-vault vault credential set BIGQUERY_DATASET="..." --vault oracle
```

### When Credits Show Value

- [ ] Evaluate DataForSEO for bulk Shopping scanning (only if 500 SerpApi credits exhaust)

---

## SerpApi Credit Strategy

500 credits remaining. Spend strategically, not randomly.

### Allocation

```
Research Phase:     150 searches (30 candidates × 5 queries)
Country Comparison: 100 searches (10 candidates × 4 countries)
Reserve:            250 searches (ad-hoc investigation)
```

### Per-Candidate Queries (5 each)

| # | Query Type | What It Reveals |
|---|-----------|-----------------|
| 1 | Generic commercial query | Broad Shopping competition |
| 2 | Exact product query | Specific product sellers |
| 3 | Exact model query | Model-level saturation |
| 4 | Feature/use-case query | Intent variations |
| 5 | Google Trends | Seasonality + demand trajectory |

### Country Comparison (for top 10)

```
Product × UK Shopping
Product × Norway Shopping
Product × Denmark Shopping
Product × Sweden Shopping
```

Creates real geographic competition matrix. Catches the exact-SKU saturation that killed the 165-click zero-sale case.

### Per Shopping Query

SerpApi returns: position, product_id, title, seller/source, price, delivery, rating, review count, multiple sellers per product.

This is how we detect: "20+ retailers selling the same supplier SKU" before spending money.

---

## Why Google Ads API Is #1

Without credible `expected_CPC`, we can't distinguish good from bad before spending:

```
GOOD
  Contribution/order     £250
  Expected CPC            £0.80
  Realistic CVR             0.8%
  Expected value/click   £2.00
  Headroom                2.50×

BAD
  Contribution/order      £30
  Expected CPC            £2.10
  Realistic CVR             2%
  Expected value/click   £0.60
  Headroom                0.29×
```

The lumbar-pillow failure was the second scenario. $65 product, $2.13 CPC. Even great CVR couldn't rescue it.

The $10k/day case was the first. $300-500 products meant every conversion was worth enough that 0.48% CVR still worked.

Google Ads data is not "marketing data." It is a fundamental pre-launch economic input.

### What we get per PRODUCT × COUNTRY × QUERY

- Average monthly searches
- Monthly search history (12 months)
- Competition index
- 20th percentile bid
- 80th percentile bid
- Average CPC
- Forecast impressions/clicks/cost

Google specifically recommends caching because historical metrics refresh monthly.

---

## Complete Vault State

```bash
# List all credentials
agent-vault vault credential list --vault oracle

# Get a specific one
agent-vault vault credential get SERPAPI_API_KEY --vault oracle
agent-vault vault credential get CLOUDFLARE_API_TOKEN --vault oracle

# Set a new one
agent-vault vault credential set GOOGLE_ADS_DEVELOPER_TOKEN="xxx" --vault oracle
```

### Current Keys

| Key | Status | Value |
|-----|--------|-------|
| SERPAPI_API_KEY | LIVE | `0f9f1e0...` |
| CLOUDFLARE_API_TOKEN | LIVE | `cfat_zxMk0x...` |
| CLOUDFLARE_ACCOUNT_ID | LIVE | `954612af...` |
| CLOUDFLARE_R2_ACCESS_KEY | LIVE | `6fd280af...` |
| CLOUDFLARE_R2_SECRET_KEY | LIVE | `99edd0da...` |
| OPENCODE_API_KEY | LIVE | mimo-v2.5 access |
| GOOGLE_ADS_DEVELOPER_TOKEN | PENDING | Apply tonight |
| GOOGLE_CLIENT_ID | PENDING | Create in GCP |
| GOOGLE_CLIENT_SECRET | PENDING | Create in GCP |
| GOOGLE_ADS_CUSTOMER_ID | PENDING | After Ads account |
| GOOGLE_ADS_REFRESH_TOKEN | PENDING | After OAuth |
| GOOGLE_MERCHANT_ID | PENDING | After Merchant setup |
| SEARCH_CONSOLE_SITE_URL | PENDING | After domain verify |
| GOOGLE_CLOUD_PROJECT | PENDING | After GCP project |
| BIGQUERY_DATASET | PENDING | After BigQuery setup |

---

*The minimum stack is Google Ads API + existing SerpApi credits. Everything else is free or already owned. First real money goes into actual clicks, not more APIs.*
