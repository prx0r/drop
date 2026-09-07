# Data Sources & Integrations

## Included adapters

### Serper — Google Shopping observations
Environment variable: `SERPER_API_KEY`

Purpose:
- localized Shopping result collection;
- merchant/price/title/image observation;
- repeated SERP snapshots.

Raw observations should always be persisted so changes in competition and pricing can be measured.

### DataForSEO — Google Ads keyword metrics
Environment variables:
- `DATAFORSEO_LOGIN`
- `DATAFORSEO_PASSWORD`

Purpose:
- local monthly search volume;
- CPC;
- advertiser competition.

### CSV providers — zero-capital path
Use Google Keyword Planner exports and manually captured/scraped Shopping/supplier data without buying an API. The scanner core accepts CSV because acquisition infrastructure should not become a prerequisite for validating the model.

## Recommended additional connectors

### Google Ads API / Keyword Planner
Best long-term first-party source for your own keyword/CPC workflow once the Ads account/API access is established.

### Merchant Center / Google Ads conversion data
Feed actual campaign CPC/CVR/ROAS/conversion-value data back into the database. The model should become empirical after the first tests.

### Supplier feeds/APIs
Prefer:
1. manufacturer/wholesaler CSV/API;
2. Alibaba supplier quote export;
3. CJ/AliExpress catalog discovery;
4. marketplace scraping only as a fallback.

Store supplier quote timestamps because unit/freight prices change.

### FX
Normalize supplier USD/EUR prices into the market currency at scoring time. Cache the FX observation and timestamp. Do not silently use an eternal hard-coded FX rate.

### Shipping quotes
The most useful future integration is a real shipping/3PL quote source because bulky/fragile goods often look spectacular until freight is included.

## Observation provenance

Every measured value should carry:
- provider;
- query/SKU;
- country;
- timestamp;
- raw payload or source URL;
- whether it is `observed`, `supplier_quote`, `modelled`, or `manual`.

Never merge `modelled` values with `observed` values without preserving provenance.

## Seed dataset provenance

`data/live_screening_candidates.csv` contains 50 current screening rows derived from public retail and supplier listings. Retail prices and supplier-category ranges are live observations; scenario CPC/search-volume/landed-cost inputs are explicitly marked as assumptions in `notes`.

`data/source_registry.csv` records the source families used to create the seed set.
