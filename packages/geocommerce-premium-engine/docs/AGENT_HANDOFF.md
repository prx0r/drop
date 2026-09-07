# Coding-agent handoff

## Mission
Productionize this repo into the internal **GeoCommerce control plane** and a reusable premium consultant storefront.

## P0 — before spending money
1. Implement OAuth refresh-token handling for Google Ads + Merchant via a secrets service.
2. Add timestamped FX adapter and normalize every monetary observation before scoring.
3. Replace SQLite with Postgres only when concurrent workers are needed; current SQLite is intentionally VPS-simple.
4. Add background job queue for scans/media.
5. Implement Merchant best-seller and price-competitiveness ingestion with eligibility/error handling.
6. Implement Google Keyword ideas + historical metrics caching keyed by country/language/query/month.
7. Add Shopify publishing: product shells, market-specific translations, market web presence, inventory/order webhooks.
8. Add supplier sample/QA workflow; no product reaches PAID_TEST without a sample or equivalent verified QA record.
9. Add real supplier adapters in priority order: direct dealer CSV/API, CJ, approved AutoDS API.
10. Add outcome ingestion from Shopify + Google Ads.

## P1 — premium UX
- Next.js/Hydrogen or high-performance Shopify theme based on `docs/PREMIUM_UX.md`.
- product quiz/advisor with deterministic hard filters before LLM explanation;
- compare table and buying guide generated from verified attributes;
- callback/human relay queue;
- local market trust blocks/payment/delivery language;
- event telemetry for every advisor question and comparison click.

## P1 — media
- Runway Product Ad + Veo adapters behind one `MediaProvider` interface;
- store original references, prompts, output IDs and QA status;
- do not auto-publish generated video;
- generate text overlays in HTML/video editing, not model-rendered spec text.

## P2 — autonomous allocation
- nightly scanner ranks `SKU × market`;
- free-listing launch queue;
- paid-test queue requires human budget approval;
- auto-kill can pause but never auto-increase spend without explicit policy;
- learning model replaces assumed CVR/return rate with observed conservative estimates.

## Non-negotiable tests
- currency mismatch cannot produce a launch verdict;
- supplier commission cannot affect ranking;
- regulated/uncertified products hard-fail;
- generated copy cannot introduce attributes absent from canonical truth;
- support bot must hand off unknown specs;
- Merchant feed/landing page language/currency consistent;
- duplicate SKU surface strategy complies with Merchant policies.
