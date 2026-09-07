# Reference Guide — Drop Project

*All imported data, tools, APIs, and resources with paths and purposes.*

---

## Imported Code Packages (from z2m)

| Package | Path | What It Does | Use For |
|---------|------|--------------|---------|
| GeoCommerce Premium Engine | `packages/geocommerce-premium-engine/` | Production backend, 20/20 tests, 9 market configs | Store backend |
| Q4 Ecom Radar | `packages/q4ecom-radar/` | 10-market scanner, scoring, Docker-ready | Product discovery |
| Boring Infra Engine | `packages/boringinfra-engine/` | Opportunity scoring, SQLite, verified revenue data | SaaS opportunities |
| Nordic Ecom Scanner | `packages/nordic-ecom-scanner/` | Norway/DK market data, 50 ranked products | Nordic scanning |
| Gift Arbitrage Engine | `packages/gift-arbitrage-engine/` | AI gifting, Prodigi adapter, 40 products | Personalized gifts |
| Business Factory v2 | `packages/business-factory-v2/` | 5 zero-capital business kernels | SaaS businesses |
| Hacksmith Substrate | `packages/hacksmith-substrate/` | 13 autonomous gates, prompt library | Agent workflows |
| 402Arena CG | `packages/402arena-cg/` | CG overlay, research experiments | Evolution kernel |
| LLMDeals SerpApi Kit | `packages/llmdeals-serpapi-kit/` | Quota management, adaptive yield | SerpApi optimization |
| AI Retail Validation | `packages/ai-retail-validation/` | 3 lean prototypes, validation methodology | Quick validation |
| Ecom Agent Moat | `packages/ecom-agent-moat/` | 5 specialization kernels | Agent moats |
| AgentBuild v3 | `packages/agentbuild-v3/` | Standards, security, blueprints | Build pipeline |

## Imported Research (from z2m)

| Report | Path | What It Contains |
|--------|------|------------------|
| Boring Infra Reports | `research/boring-infra/` | 9 reports: verified revenue, winner/loser pairs, recipes, 30-day plan |
| Internet Asset Playbook | `research/internet-asset-playbook/` | Validated business models, agent architecture |
| Pinterest Trend Forecast | `research/pinterest-trend-forecast/` | Forecasting model, automation architecture |
| Q4 Demand Capture | `research/q4-demand-capture/` | Thesis audit, unit economics, scanner code |
| SN19 Blockmachine Guide | `research/sn19-blockmachine-guide.md` | Bittensor mining playbook |
| Import Summary | `research/import-summary.md` | Quick reference for all intelligence |

## Imported Intelligence (from z2m)

| Report | Path | What It Contains |
|--------|------|------------------|
| AISec Money Radar | `intelligence/aisec-money-radar/` | Top 20 security bounties with EV ranking |
| Reddit Money Radar | `intelligence/reddit-money-radar-top20.md` | 20 actionable agentic opportunities |
| Reddit Pain Radar | `intelligence/reddit-pain-radar/` | UK AI security pain points |
| Agent Money Scout | `intelligence/agent-money-scout/` | Time-sensitive bounty opportunities |
| Arb Radar | `intelligence/arb-radar/` | Low-capital arbitrage opportunities |

---

## Data Sources (from user's analysis)

### Google APIs (LIVE)
| API | Status | Use | Config |
|-----|--------|-----|--------|
| Merchant Center Popular Products | PENDING | Demand × country × category | Account 5849184805 |
| Keyword Planner | PENDING (Standard access) | Search volume, CPC, competition | google-ads.yaml |
| Google Trends API (alpha) | AVAILABLE | 5-year rolling window, subregion data | Free |
| Merchant Center → BigQuery | AVAILABLE | Best Sellers, Performance, Price data | 2-year backfill |

### Price Comparison Sites
| Site | Country | Data | API? |
|------|---------|------|------|
| Prisjakt.no | Norway | Seller count, prices, stock, reviews | YES (Partner Search API) |
| Prisjakt.fi | Finland | Same | YES |
| PriceRunner.dk | Denmark | Same | Unknown |
| Prisjakt.nu | Sweden | Same | YES |
| Toppreise.ch | Switzerland | Same | Unknown |
| Geizhals | Germany/Austria | Same | Unknown |
| Hinta.fi | Finland | Same | Scraping |

### Government Data
| Source | Country | Data | API |
|--------|---------|------|-----|
| VOEC Register | Norway | 4,006 foreign sellers registered for VAT | Scraping |
| SSB PxWeb | Norway | 7,500+ Statbank tables | YES (PxWeb API v2) |
| StatFin | Finland | Trade data, import/export | YES (PxWeb) |
| StatBank | Denmark | All published data | YES |
| Eurostat Comext | EU | International trade in goods | YES |
| UN Comtrade | Global | Monthly/annual trade data | YES |

### Supplier Platforms
| Platform | Products | Dropship? | API? | Notes |
|----------|----------|-----------|------|-------|
| DistriHUB | 400+ brands | YES (EUR 3/pack) | YES | Best for Nordics |
| CJdropshipping | Millions | YES | YES + MCP | Global, Chinese |
| BigBuy | 400,000+ | YES | YES | EU, 24 languages |
| Syncee | Millions | YES | YES | Aggregation layer |
| AutoDS | Various | YES | YES | Price/stock monitoring |
| Spocket | Various | YES | YES | Filter by shipping destination |
| Hertwill | EU/US brands | YES | YES | Estonia, real brands |
| ELKO Group | Nordics | Via B2B webshop | Unknown | Dreame, Xiaomi distributor |

### Store Intelligence
| Tool | Data | Use |
|------|------|-----|
| Store Leads | Shopify stores by country/category | Merchant census |
| BuiltWith | Technology stack, platform, apps | Store intelligence |
| Similarweb | Traffic estimates | Merchant strength |
| Meta Ad Library | Active advertisers (EU/UK) | Who's spending |
| TikTok Creative Center | Trending products/creative | Product discovery |
| Pinterest Trends | Growing searches by region | Early intent |
| eBay Product Research | 3 years of sales data | Demand validation |

### Content/SEO
| Tool | Data | Cost |
|------|------|------|
| Google Keyword Planner | Search volume, CPC, competition | Free (with Ads) |
| Google Trends | Interest over time, subregion | Free |
| Pinterest Trends API (alpha) | Trending keywords, WoW/MoM/YoY | Free (partner access) |
| TikTok Creative Center | Trending products, hashtags | Free |

---

## The Canonical Engine (from user's analysis)

For every **SKU × country**, store:

```text
DEMAND
  keyword_volume
  keyword_growth_3m
  keyword_growth_12m
  google_best_seller_rank
  pinterest_growth
  import_value_12m
  import_growth_yoy

COMPETITION
  shopping_seller_count
  price_comparison_seller_count
  good_seller_count
  poor_seller_count
  median_merchant_quality
  shopify_specialist_count
  paid_advertiser_count

ECONOMICS
  retail_median
  retail_p10
  supplier_cost
  shipping_cost
  vat
  duty
  payment_fee
  expected_returns
  gross_contribution
  break_even_cpc
  break_even_roas

SUPPLY
  warehouse_country
  stock
  delivery_days
  dropship_allowed
  dealer_authorized
  blind_shipping
  returns
  warranty
  api_or_feed
  moq

LOCALIZATION
  native_content_quality
  local_payment
  local_shipping
  local_reviews
  comparison_content_gap
  expert_advice_gap

OUTCOME
  launched?
  traffic
  ctr
  conversion
  cac
  revenue
  margin
  return_rate
  profit
```

---

## Key Data Points (from user's analysis)

### Market Size
| Country | E-commerce | Population | Online Shoppers | Cross-Border |
|---------|-----------|------------|-----------------|--------------|
| Norway | $10.35B | 5.5M | 86% | 78% buy internationally |
| Finland | $7.2B | 5.5M | 82% | 80% buy internationally |
| Sweden | $16.8B | 10.4M | 88% | 71% cross-border |
| Denmark | $12.5B | 5.8M | 87% | 71% cross-border |

### Store Census
| Country | Shopify Stores | YoY Growth |
|---------|---------------|------------|
| Norway | 10,341 | +23% |
| Finland | 7,181 | +14% |

### VOEC Register
- **4,006 foreign sellers** registered for Norwegian VAT
- Government-maintained list of serious foreign ecommerce companies
- Scrapeable: domain → technology → category → Shopify? → traffic → Prisjakt presence

### DHL Fulfillment
- **March 30, 2026:** DHL expanded fulfillment hubs in Helsinki and Oslo
- Validates: dropship to validate → local 3PL for winners

---

## The Good Seller Gap Framework (from user's analysis)

### Conservative Thresholds
| Test | Minimum |
|------|---------|
| Trusted seller surplus | ≥ 8 |
| Independent trusted directories | ≥ 2 |
| Domain surplus | ≥ 3 |
| Productive discovery queries | ≥ 2 |
| Local merchant quality for "GOOD" | ≥ 70/100 |

### Merchant Quality Score Components
- Target-country shipping/availability
- Warranty/returns clarity
- Delivery evidence
- Category specialization
- Real support/contact information
- Independent reviews
- Company history

### Important Rule
**eBay/Amazon/marketplaces do NOT count as trusted underlying sellers.** They are discovery/demand evidence only.

---

## The Formula (from user's analysis)

```
proven demand × weak merchant execution × good economics × supplier availability × local trust → test with free/high-intent traffic → paid scale only after validation
```

---

## Priority Actions (based on all intelligence)

### Immediate (Today)
1. Import Q4 Ecom Radar to drop repo
2. Import Boring Infra Reports to drop repo
3. Import GeoCommerce Premium Engine to drop repo
4. Set up Google Merchant Center → BigQuery transfer
5. Scrape VOEC register (4,006 foreign sellers)

### This Week
6. Integrate Prisjakt Partner Search API
7. Set up Store Leads / BuiltWith for merchant census
8. Build unified product × market × time schema
9. Start continuous data ingestion pipeline

### This Month
10. Launch first probe store (robot vacuums Finland via DistriHUB)
11. Build scoring engine with all data sources
12. Create 100 product × country hypotheses
13. Test first 10 hypotheses with free listings

---

*This document is the reference layer. Everything else points here.*
