# Opportunity Scoring Model

The scanner is deliberately **economics first**. A beautiful margin screenshot is meaningless if VAT, paid acquisition, returns and delivery destroy contribution.

## Core equations

For a tax-inclusive consumer price `P` and VAT rate `v`:

```
net_revenue_ex_vat = P / (1 + v)
```

Pre-ad contribution (using `expected_units_per_order`):

```
order_revenue = unit_price * expected_units_per_order
order_landed_cost = landed_cost_per_unit * expected_units_per_order
pre_ad = net_revenue_ex_vat
       - order_landed_cost
       - payment_fee
       - expected_return_loss
       - support_allowance
```

Expected customer acquisition cost:

```
CPA = CPC / CVR
```

Contribution after paid acquisition:

```
contribution_after_ads = pre_ad - CPA
```

Break-even conversion rate:

```
break_even_CVR = CPC / pre_ad
```

That last number is the best early filter. If the break-even conversion rate is 5% for cold Shopping traffic, the candidate is probably not a sensible first test.

## Score components (100 points)

- **Economics — 35:** contribution margin and CVR safety buffer.
- **Demand — 15:** logarithmic search-volume score so giant generic keywords do not dominate.
- **Competition — 15:** merchant count and dominant-merchant share.
- **Merchandising gap — 10:** opportunity to improve image/title presentation.
- **Basket/B2B — 10:** multipack, room/project order and trade-order potential.
- **Localization — 10:** market localization moat plus payment/return readiness.
- **Operations — 5:** delivery-time, regulatory, fragility and bulk penalties.

## Gates

A score is not enough. Hard/soft gates prevent seductive bad ideas:

- `REJECT`: non-positive pre-ad contribution.
- `RESEARCH`: negative contribution under current CPC/CVR assumptions.
- `RESEARCH`: break-even CVR above 4%.
- `RESEARCH`: delivery beyond the market profile's maximum.
- `RESEARCH`: missing preferred local payment in NO/DK/SE.
- `COMPLIANCE_REVIEW`: regulated-risk score >= 0.75.

A product can score well visually and still be blocked by a gate.

## Conservative input policy

Before calling a row `TEST`, replace scenario values with evidence:

- `monthly_searches`: Keyword Planner / DataForSEO local metric.
- `cpc_local`: local Google Ads CPC estimate or campaign observation.
- `landed_cost_local`: supplier quotation + freight + duty/tax handling + packaging + QA allowance.
- `estimated_delivery_days`: actual service-level commitment, not supplier marketing copy.
- `expected_return_rate`: category/store measurement once available.
- `merchant_count`/`dominant_merchant_share`: current Shopping SERP observations.
- `creative_gap`/`title_gap`: human or vision-model audit of actual competitors.

## Why supplier-price gaps are not margins

A supplier page may quote `$3.50` while a Nordic competitor charges `NOK 699`. The scanner intentionally does **not** calculate 95% margin from those two numbers. The supplier listing may differ in dimensions/material, require MOQ, exclude battery/freight, lack required documentation, or use a different finish. That is why every seed row includes `match_quality` and why `landed_cost_local` is a separate field.

## Recommended experimental thresholds

Good initial screen:

- positive contribution at 2.0–2.5% assumed CVR;
- break-even CVR <= 1.5–2.0% preferred;
- landed cost <= ~30–35% of ex-VAT selling price for paid-search products unless AOV/repeat/B2B is exceptional;
- no extreme compliance/fragility/bulk risk;
- visible merchandising weakness among current Shopping sellers;
- at least one credible path to local returns;
- delivery promise <= market maximum.

These are starting heuristics, not universal truths. Replace them with your own measured posterior as campaigns run.
