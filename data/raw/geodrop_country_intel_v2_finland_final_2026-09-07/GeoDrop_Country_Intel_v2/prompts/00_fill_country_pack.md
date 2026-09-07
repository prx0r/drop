# Coding/Research Agent Prompt — Fill a New GeoDrop Country Pack

You are populating a GeoDrop country intelligence pack. Work inside the existing canonical folder. Do not change filenames or invent new report types.

## Non-negotiable rules
1. Do not guess. Unknown required values become `MISSING_REQUIRED` observations.
2. Prefer primary/current country sources: statistical office, tax/customs, consumer authority, payment/logistics reports, Google first-party APIs, local price comparison, manufacturer/distributor evidence.
3. Every factual metric must become an `observations.jsonl` row and point to `sources.jsonl`.
4. Preserve historical rows; append new observations. Reports reference observation IDs rather than duplicating undocumented numbers.
5. Search in the country's native language as well as English.
6. Separate `CONTENT_GAP` from `MERCHANT_GAP`.
7. Exact-SKU/GTIN/MPN validation outranks broad category anecdotes.
8. Public search scarcity is not enough: check B2B distributors/dealer networks.
9. Never mark a product launchable without hard gates in `global/score_model.json`.
10. Do not use generic dropshipping blogs as hard evidence.

## Research sequence
A. Profile: languages, currency, VAT/tax, ecommerce/import regime, local payment and delivery conventions.
B. Consumer: ecommerce penetration, cross-border share/origins, checkout abandonment, payment, delivery, returns, age/cohort/category patterns.
C. Structural demand: housing/ownership, climate, vehicles, energy systems, installed equipment, regulation, demographics, import/product data. Find persistent ecosystems and replacement cycles.
D. Acquisition: collect Google Ads Keyword Planner by segment and native query; monthly searches, monthly volumes, competition index, average CPC, low/high top-of-page bid. Add Trends series and Merchant Center market insights where access exists.
E. Competition: price-comparison and Google Shopping exact products; seller count, GOOD_SELLER_COUNT, prices, stock, merchant quality, content gap and saturation velocity.
F. Supply: authorized distributors, dealer economics, ecommerce rights, MOQ/MOV, direct/blind ship, warehouse, stock feed/API, shipping, warranty/RMA, returns.
G. Source markets: identify mature nearby markets with specialist merchants that prove the service/catalogue archetype.
H. Product markets: score only after evidence collection. List unknowns and falsifiers prominently.

Run `python scripts/validate_pack.py countries/<iso>` before completion.
