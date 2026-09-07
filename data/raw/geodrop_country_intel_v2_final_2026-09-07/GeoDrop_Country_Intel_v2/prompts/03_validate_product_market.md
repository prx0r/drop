# Agent Prompt — Strict Product-Market Validation

Validate one `product_market_id` as if trying to falsify it.

1. Exact identity: GTIN/MPN/model/variant.
2. Demand: Keyword Planner native exact-model + job/use-case terms; Google Trends; Merchant Center or Shopping evidence; seasonality.
3. Competition: local price-comparison + Shopping + native search; list every credible seller; merchant quality rubric; hidden distributor/dealer check.
4. Economics: competitive delivered selling price; dealer net price; freight; VAT/duty treatment; payment; return, chargeback, support and warranty reserves. Calculate pre-ad contribution, break-even CVR and economic headroom from measured CPC.
5. Supply: authorization, online resale rights, stock reliability, direct ship, feed/API, SLA, warranty/RMA.
6. Local conversion: native content, local payment, delivery/pickup, transparent tax/returns, company trust.
7. Falsification: write strongest opposing evidence first.

No dealer cost or no CPC => `HOLD_VALIDATE`, not a guessed score upgrade.
