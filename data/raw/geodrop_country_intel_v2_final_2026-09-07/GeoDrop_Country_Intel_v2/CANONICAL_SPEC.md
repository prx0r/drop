# Canonical Country Architecture

## Design principles

### 1. Facts, interpretations and decisions are separate
`observations.jsonl` contains facts. Reports contain interpretations referencing observation IDs. `product_markets.jsonl` contains decisions/scores. `outcomes.jsonl` contains what actually happened after launch.

### 2. Provenance is mandatory
Every observation has `source_id`, `period`, `evidence_type`, `status`, and `confidence`. Web citations and access URLs live in `sources.jsonl`. Internal operator evidence is allowed but must be marked `internal` or `observational`, never upgraded to audited causal proof.

### 3. Country packs are structurally identical
No country invents new report names. Country-specific detail belongs inside canonical reports or segment/product rows.

### 4. Hard gates beat scores
A candidate with 90/100 and unknown reseller rights is not launchable. A candidate with brilliant search whitespace but hidden B2B distribution is not a merchant gap.

### 5. Product identity is exact
Prefer GTIN, MPN/model, brand and variant. Broad category research may create a segment hypothesis but cannot become a launch candidate without exact SKUs.

### 6. Content gap != merchant gap
`CONTENT_GAP` means existing merchants answer the decision poorly. `MERCHANT_GAP` means there are too few genuinely good merchants. They are measured independently.

### 7. Real contribution beats revenue/ROAS
Store outcomes record net selling price, landed cost, payment/return/warranty/support reserves, ad cost and realized contribution. ROAS is secondary.

## Required standardized reports

1. `01_market_overview.json` — population, ecommerce adoption, cross-border behavior, retail/ecommerce direction, purchasing context.
2. `02_consumer_behavior.json` — payment, checkout abandonment, delivery, returns, trust, age/cohort and category behavior.
3. `03_structural_demand.json` — installed bases, replacement cycles, housing/climate/regulation/vehicle/industry data that creates persistent demand.
4. `04_acquisition.json` — Google Ads Keyword Planner, Google Trends, Merchant Center market insights, Search Console/free traffic, social discovery where relevant.
5. `05_competition.json` — local price comparison, Google Shopping, seller census, GOOD_SELLER_COUNT, merchant quality, content gap, saturation velocity.
6. `06_supply_logistics_compliance.json` — supplier path, inventory/feeds, delivery, returns, VAT/duties, resale authorization, warranty/RMA, local payments.
7. `07_source_markets.json` — mature markets/stores to copy as archetypes; same-SKU price/service comparisons.
8. `08_opportunity_summary.json` — ranked structural opportunity universes and explicit falsifiers; not a launch list.

## Refresh cadence

- Keyword Planner: monthly (Google states historical metrics refresh monthly).
- Google Trends: weekly for monitored terms; monthly archive.
- Price-comparison/Shopping seller snapshots: weekly for active candidates, monthly otherwise.
- Supplier stock/price: daily/hourly only after candidate validation; otherwise weekly.
- National statistics: on release schedule, discovered through source adapters.
- Consumer reports: on publication.
- Product-market outcomes: event-driven from the store.

## Evidence types

`primary_official`, `platform_first_party`, `industry_report`, `peer_reviewed`, `merchant_first_party`, `internal_research`, `operator_observation`, `derived`.

## Observation status

`OBSERVED`, `DERIVED`, `MISSING_OPTIONAL`, `MISSING_REQUIRED`, `STALE`, `DISPUTED`.

## Country-product state machine

`DISCOVERED -> RESEARCH -> HOLD_VALIDATE -> READY_CONTENT_TEST -> READY_FREE_COMMERCE_TEST -> READY_PAID_TEST -> SCALE`

Failure branches: `PAUSE`, `KILL`.
