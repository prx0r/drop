# Research Basis

This schema encodes both GeoDrop's prior falsification work and external evidence.

External cross-border ecommerce research supports measuring vendor trust/reputation, price competitiveness, uniqueness, communication/waiting cost, logistics, trusted payment/certification, reviews and return policy. Current Norwegian consumer evidence independently shows local payment, shipping cost, delivery choices and nearby-market trust matter materially. These are therefore data fields/gates rather than cosmetic recommendations.

Current platform infrastructure makes much of the architecture directly machine-readable:
- Google Ads Keyword Planner historical metrics are geo/language targetable and include volume, monthly history, competition/index, average CPC and bid ranges.
- Google Trends API alpha supplies a rolling 5-year consistently scaled series by region/subregion.
- Merchant Center -> BigQuery exposes Performance, Best Sellers (up to 2-year backfill), Price Competitiveness and Price Insights, subject to eligibility.
- Prisjakt Partner Search supports Norway/Finland/Denmark and exposes purchasable in-stock offers and popularity ordering.
- Statistics Norway PxWebApi v2 exposes roughly 7,500 tables without registration.

The pack deliberately does not include fake Keyword Planner/dealer values where authenticated/private access is required.
