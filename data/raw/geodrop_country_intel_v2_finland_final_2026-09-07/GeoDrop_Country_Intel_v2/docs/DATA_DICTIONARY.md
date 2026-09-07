# GeoDrop v2 High-Signal Data Dictionary

## Country baseline
Population, household count/income/purchasing context, ecommerce penetration/growth, cross-border behavior, online retail share, payment preference, checkout abandonment, delivery preference/cost sensitivity, returns behavior, marketplace penetration, price-comparison use, social discovery and relevant age/cohort differences.

## Installed-base ecosystem
`installed_base_current`, stock definition, inclusion/exclusion, annual additions, historical stock, growth rates, cohort/age distribution, geographic distribution, expected lifetime if evidenced, replacement share/rate, second-hand transfers, regulation/subsidy drivers, climate exposure, ownership type and service-channel density.

## Problem/job
Trigger type: `FAILURE | MAINTENANCE | REPLACEMENT | UPGRADE | COMPATIBILITY | INSTALLATION | COMPLIANCE | SEASONAL | CONSUMABLE`. Store incidence/rate where measured, urgency, seasonal/geographic exposure, affected cohort/component, service-vs-DIY suitability, safety/regulatory constraints and evidence.

## Native query
Native phrase, normalized intent, problem/ecosystem linkage, search volume, CPC/bids, competition, monthly history, Trends growth, transactional/informational intent, SERP seller count, shopping presence, source of vocabulary and measurement timestamp. Seed queries are never treated as measured demand.

## Merchant/service census
Domain/legal entity, merchant type, local/foreign, category specialization, product/SKU breadth, price/stock/delivery, payment/returns/warranty, support, reviews, decision content, installer/service capability, source-market resemblance, merchant-quality score and evidence snapshot.

## Source-market archetype
Source country, merchant/domain, ecosystem, brand/SKU breadth, accessories/replacements, compatibility data, selectors/comparisons, bundles, installation/configuration/service, acquisition surfaces, checkout/logistics, monetization and evidence that the model is operational. Do not infer profitability unless audited.

## Source-target gap
Comparable source/target seller counts, good merchants, SKU/part breadth, decision assets, service capabilities, delivered prices and demand. Core derived measures: assortment gap, merchant gap, content/service gap, `problem_demand_density`, seller-growth vs installed-base-growth and price compression.

## Supply/economics
Supplier/distributor identity, authorization, net cost, stock, feed/API, MOQ/MOV, direct/blind shipping, country warehouse, freight, ETA, VAT/duty, payment fee, expected returns/warranty/support reserve, net selling price, pre-ad contribution, CPC, break-even CVR, economic headroom.

## Outcome
Impressions, clicks, qualified clicks, ATC, checkout, orders, revenue ex-tax, discount, COGS, inbound/outbound freight, payment fees, refunds, returns, chargebacks, warranty/support, ad spend and realized contribution. Record tracking/supplier anomalies separately.

## Critical definitions
- `GOOD_SELLER_COUNT`: sellers that pass a documented local trust/service threshold, not raw SERP results.
- `CONTENT_GAP`: target merchants fail to answer buying/compatibility questions well.
- `MERCHANT_GAP`: too few genuinely good local merchants.
- `REPLACEMENT_PRESSURE`: installed population exposed to evidence-backed replacement probability; never manufacture a rate from an unevidenced lifetime.
- `POINT_IN_TIME_SAFE`: evidence has a known availability timestamp no later than the decision timestamp.
