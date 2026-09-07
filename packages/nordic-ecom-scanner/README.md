# Nordic E-commerce Arbitrage Scanner

A production-oriented kernel for finding **country × niche × product** opportunities where existing Google Shopping demand can be served with better merchandising, localization, pricing, bundles, and fulfillment.

The initial market profiles are **Norway (NO)** and **Denmark (DK)** with the **United Kingdom (GB)** as a control. Additional profiles are included for Sweden, Finland, Ireland, Switzerland, Australia, New Zealand, UAE, and Saudi Arabia.

## What this is

This is not a “winning product generator.” It is a decision engine that refuses to call a product attractive unless the economics survive:

- VAT/import treatment
- landed cost
- payment fees
- returns allowance
- support allowance
- Google CPC / conversion-rate assumptions
- local checkout expectations
- local delivery / return expectations
- competition density
- merchandising gap
- B2B / multi-unit order potential
- compliance and fragility penalties

The central equation is:

`expected contribution/order = order revenue ex VAT - order landed cost - payment fees - returns - support - expected CPA`

where:

`expected CPA = CPC / conversion_rate`

and:

`break-even CVR = CPC / pre-ad contribution`

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'

# Create and seed the database
ECSCAN_DB=./scanner.sqlite ecomscan init
ECSCAN_DB=./scanner.sqlite ecomscan seed

# Score the seeded 50-candidate market-research dataset
ECSCAN_DB=./scanner.sqlite ecomscan score

# Show the top opportunities
ECSCAN_DB=./scanner.sqlite ecomscan rank --limit 20

# Export scored rows
ECSCAN_DB=./scanner.sqlite ecomscan export --out ranked.csv

# Optional read API
ECSCAN_DB=./scanner.sqlite uvicorn nordic_arbitrage.api:app --reload
```

You can also run:

```bash
./scripts/demo.sh
```

## Data acquisition design

The scanner intentionally separates **data collection** from **decision logic**.

### Zero/low-cost mode

1. Export keyword ideas from Google Keyword Planner to CSV.
2. Export/import Shopping SERP observations to CSV.
3. Import supplier quotes/catalogs to CSV.
4. Run the local SQLite scorer.

### Automated mode

Adapters are included for:

- **Serper** Google Shopping/Search API (`SERPER_API_KEY`)
- **DataForSEO** keyword metrics (`DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD`)
- CSV supplier catalogs / quotations

The scoring engine does not care where the data came from.

### Live localized query

With `SERPER_API_KEY` set:

```bash
ecomscan observe --country NO --query "messing håndtak kjøkken"
```

Add `--with-keywords` when DataForSEO credentials are also set. The normalized result and raw decision features are persisted to SQLite.

### Google Merchant feed validation

```bash
ecomscan feed --input verified_catalog.csv --out merchant_feed.csv
```

## Important implementation principle

Do not fake a domestic identity. Localize language, currency, checkout, merchandising, FAQs and support, while clearly disclosing the legal seller, shipping origin, taxes, delivery expectations and returns address.

## Research dataset

`data/live_screening_candidates.csv` contains 50 price-gap screening rows assembled from live September 2026 market observations. These are **not claimed to be exact SKU matches**. Each row records a local competitor observation plus a supplier-category quote/range and a match-quality field. Their purpose is to prioritize manual validation, not to manufacture fake margin certainty.

See:

- `docs/MARKET_RESEARCH_2026-09-04.md`
- `docs/SCORING.md`
- `docs/OPERATING_PLAYBOOK.md`
- `docs/DATA_SOURCES.md`
- `docs/COUNTRY_EXPANSION.md`


## Verification

At packaging time the automated suite passes **11/11 tests** and the complete offline 50-row seed → SQLite → score → export path has been executed. See `TEST_REPORT.md` and `outputs/OFFLINE_DEMO.md`.

The live paid adapters are code-complete but were not called without API credentials.

## Query seeds

`data/query_seeds.csv` contains 64 Norwegian/Danish commercial-intent seed queries. They are discovery seeds, not claimed keyword-volume evidence; validate them through Keyword Planner/DataForSEO before spend.
