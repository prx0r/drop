The core build should be **an operator system that happens to launch a store**, not a store generator. The most important current implementation detail is that Merchant Center’s old Content API is now sunset, so new work must use **Merchant API v1**. Merchant Center still provides free listings, Standard Shopping is still supported, and its BigQuery transfer can backfill Performance and Best Sellers for up to two years; Price Competitiveness has no backfill, so start collecting it immediately once available. ([Google for Developers][1])

This is the master prompt I would give the coding agent:

# Mission

Build and launch ONE evidence-selected, low-capital specialist ecommerce store designed around existing Google purchase intent.

Do not start by choosing a niche based on intuition.

Do not build multiple stores.

Do not build a generic “dropshipping store.”

Do not optimize for revenue screenshots.

The goal is to systematically find a:

**PRODUCT × COUNTRY × SUPPLIER × QUERY × MERCHANT × AUCTION**

combination where the economics are favorable enough that a relatively ordinary Google Shopping implementation can make money.

Then build the store, instrument it, acquire free traffic first, run a tightly controlled paid experiment capped at **$10/day**, and continuously classify the evidence into WAIT / FIX / KILL / SCALE decisions.

A winning outcome cannot be guaranteed. Optimize for rapidly discovering a viable opportunity while minimizing capital at risk.

---

# Hard constraints

Advertising budget:

**$0/day preferred. Hard maximum: $10/day total paid advertising unless explicitly changed by the owner.**

Infrastructure already available:

* VPS for hosting.
* Cloudflare for DNS/CDN/domain registration.
* Full AI API backend.
* Strong image-generation capability.
* Ability to create sites and content in arbitrary languages.
* Developer capable of maintaining custom infrastructure.

Paid APIs are allowed when they materially improve decision quality, but:

1. prefer official/free data first;
2. cache everything;
3. record API cost;
4. do not silently subscribe to expensive recurring services;
5. justify paid-data usage against the uncertainty it removes.

No inventory purchase unless explicitly approved.

No fake reviews.

No fake business locations.

No fake GTINs, brands, MPNs, availability, delivery times or product specifications.

Do not create deceptive AI images that make the physical product look materially different from what the buyer receives.

Do not manufacture social proof.

---

# Prime operating principle

The thing we are optimizing is NOT:

“Can we make Google Ads work?”

It is:

**“Can we find an auction where Google Ads has an economically easy job?”**

A campaign can be implemented perfectly and still correctly reveal that the market opportunity is bad.

That is successful experimentation.

---

# Current Google implementation requirements

Use:

**Merchant API v1**

Do NOT build new integrations against the deprecated Content API for Shopping.

Use Merchant Center for:

* product submission;
* product status;
* product issues;
* free listings;
* shipping information;
* return-policy information;
* inventory/availability;
* reporting where available.

Use Merchant Center → BigQuery transfers where eligible.

Important datasets include:

* Performance;
* Best Sellers;
* Price Competitiveness;
* Price Insights;
* Products / product issues.

Best Sellers and Performance can provide substantial historical data.

Price Competitiveness does not have historical backfill, so snapshot it continuously as soon as access exists.

Do not block the entire project if the account is not initially eligible for Market Insights / Best Sellers.

Implement fallback research sources.

---

# Architecture

Create one monorepo with clear modules:

```text
/apps
  /store
  /operator-dashboard

/services
  /research
  /catalog
  /supplier
  /merchant
  /google-ads
  /analytics
  /ai-expert
  /seo
  /experiments

/packages
  /economics
  /schemas
  /scoring
  /localization
  /shared

/data
  /raw
  /normalized
  /snapshots
  /exports

/infra
  docker-compose.yml
  nginx/
  backups/
  monitoring/

/docs
  RESEARCH.md
  DECISIONS.md
  OPERATOR_RUNBOOK.md
  LAUNCH_REPORT.md
```

Use PostgreSQL on the VPS for durable production data.

Exports must also be available as:

```text
CSV
JSONL
Parquet where useful
```

Everything important should be queryable without using the UI.

---

# Commerce backend

Do NOT waste time writing a bespoke payment/order platform.

Preferred low-cost default:

**self-hosted WooCommerce on the VPS** as the boring commerce core.

Use it for:

* products;
* orders;
* checkout;
* customer accounts;
* payment integration;
* coupons;
* taxes;
* shipping;
* refunds;
* order status.

Build a custom fast storefront/theme around it.

If the existing development environment already contains a substantially better battle-tested commerce backend, use that instead.

The architecture should isolate commerce behind an adapter so Shopify or another backend can replace WooCommerce later without rewriting the intelligence layer.

Use Cloudflare for:

* DNS;
* CDN;
* caching;
* TLS;
* basic WAF/rate limiting.

---

# PHASE 1 — Build the opportunity research engine

The first deliverable is NOT a website.

It is a ranked table of candidate opportunities.

## Unit of analysis

Never score only:

```text
"coffee grinders"
```

Score:

```text
specific product/product family
×
country
×
supplier
```

Where possible get down to:

```text
GTIN × country × supplier
```

because niche-level competition can look weak while the exact SKU is sold by 25 identical retailers.

---

# Candidate universe

Start with affluent ecommerce markets that are operationally realistic, but do not assume any one is superior.

Initial comparison universe can include:

```text
GB
NO
DK
SE
FI
IE
NL
BE
AT
CH
AU
NZ
```

Do NOT launch in all of them.

Country is a variable.

One country eventually wins the initial experiment.

---

# Product profile preference

Prioritize products that are:

* already searched for;
* relatively boring;
* established enough for customers to recognize the product category;
* research-driven purchases;
* commonly searched by exact product type, feature, brand or model;
* approximately $150–$1,000 equivalent AOV as a preference, not a hard rule;
* capable of meaningful absolute gross-profit dollars per sale;
* reasonably low-return;
* not highly size-dependent;
* not extremely fashion-dependent;
* not fragile unless supplier fulfillment is excellent;
* not legally problematic;
* suitable for remote fulfillment;
* suitable for normal ecommerce checkout.

Do NOT assume “high ticket = good.”

A $5,000 product may have enough friction that the actual product is a consultation/sales funnel rather than a checkout purchase.

---

# Data sources

Use as much structured data as possible.

Priority:

## Google

* Merchant Center Best Sellers where available.
* Merchant Center Price Competitiveness.
* Merchant Center Price Insights.
* Google Ads Keyword Planner.
* Google Trends where programmatic access is available.
* Google Shopping SERPs.
* Google Search SERPs.
* Search Console once our site exists.
* Merchant Center free-listing performance once live.

Best Sellers fields of particular interest:

```text
country
category
product/brand
rank
previous_rank
rank_delta
relative_demand
previous_relative_demand
relative_demand_change
price_range
GTIN/entity mapping
```

## Suppliers

Search:

* manufacturers;
* official distributors;
* wholesale programs;
* dealer programs;
* dropship programs;
* private fulfillment suppliers;
* regional wholesalers.

Do NOT default to AliExpress/CJ purely because integration is easy.

Easy supplier onboarding is potentially a negative signal because every competitor can list the same product.

Prefer supplier relationships with some friction/selectivity where economics justify it.

## SERP / competitor data

For each promising exact SKU/product:

collect:

```text
Shopping seller count
seller domains
prices
price distribution
shipping cost
shipping estimate
review stars/count where visible
Amazon presence
manufacturer direct-to-consumer presence
specialist retailers
marketplaces
organic SERP competition
```

If official/free methods are insufficient, use a reputable compliant paid SERP API.

Cache responses heavily.

---

# Supplier schema

Normalize supplier offers:

```text
supplier_id
supplier_name

sku
gtin
mpn
brand

wholesale_price
currency

shipping_cost
shipping_country
destination_country
shipping_days_min
shipping_days_max

inventory
inventory_timestamp

MOQ

return_window
return_cost
warranty

dropship_allowed
dealer_authorized
MAP_policy

stock_feed_available
api_available

retailer_selectivity_score
estimated_retailer_saturation
```

Supplier quality is a first-class variable.

---

# Economic model

For every candidate calculate:

```text
landed_cost =
supplier_price
+ supplier_shipping
+ expected_duties
+ any fulfillment cost
```

Then:

```text
pre_ad_contribution =
selling_price
- landed_cost
- payment_processing
- expected_refunds
- expected_chargebacks
- variable_customer_service
- other_variable_costs
```

Calculate:

```text
break_even_CVR =
expected_CPC / pre_ad_contribution
```

Also:

```text
break_even_CPC =
realistic_CVR × pre_ad_contribution
```

And:

```text
expected_profit_per_click =
(realistic_CVR × pre_ad_contribution)
- expected_CPC
```

Most importantly:

```text
ECONOMIC_HEADROOM =
(realistic_CVR × pre_ad_contribution)
/
expected_CPC
```

Interpretation:

```text
< 1.0   structurally unattractive
~1.0    razor thin
1.25    marginal
1.5+    interesting
2.0+    strong room for error
```

Do NOT use one CVR assumption.

Run:

```text
pessimistic
base
optimistic
```

scenarios.

Record assumptions explicitly.

---

# Example of why this matters

A cheap CPC is not necessarily good.

Example:

```text
Product A:
$30 contribution
$1 CPC
2% CVR

expected value/click = $0.60
expected profit/click = -$0.40
```

Reject.

Example:

```text
Product B:
$250 contribution
$1 CPC
0.8% CVR

expected value/click = $2
expected profit/click = +$1
```

Potentially excellent.

This is why a 0.5–1% high-ticket CVR can outperform a 2% low-ticket CVR.

---

# Opportunity score

Rank candidates using something similar to:

```text
35% economics
20% purchase-intent/search quality
15% exact-SKU competition
15% supplier/fulfillment quality
10% merchant differentiation opportunity
 5% trend/seasonality
```

Then apply an uncertainty penalty.

Do not bury raw values inside a proprietary score.

Every score must remain explainable.

For each candidate produce:

```text
score
confidence
raw metrics
sources
assumptions
why_it_might_work
why_it_might_fail
largest_unknown
cheapest_way_to_test_unknown
```

---

# Search intent scoring

Differentiate:

HIGH VALUE:

```text
"Brand X Model 700"
"Brand X Model 700 buy"
"Model 700 UK"
"best commercial grinder small cafe"
"quiet burr grinder under £500"
```

LOWER VALUE:

```text
"coffee"
"coffee ideas"
"cool kitchen gadgets"
```

Search volume alone is insufficient.

A 300-search/month exact-model query can be more valuable than a 10,000-search/month generic query.

---

# Competition analysis

Do not merely calculate “number of competitors in niche.”

Calculate exact-product competition.

Penalize:

* 20+ merchants carrying identical GTIN;
* heavy Amazon dominance;
* manufacturer selling direct cheaper;
* tight price compression;
* competitors with free next-day shipping where our supplier needs 12 days;
* competitors with thousands of reviews;
* supplier available to everyone.

Reward:

* weak specialist retailers;
* poor product information;
* bad comparison content;
* bad UX;
* poor localized language;
* slow customer support;
* incomplete product feeds;
* weak images;
* significant price dispersion;
* customers needing guidance.

---

# Research output

Produce:

```text
TOP_50_CANDIDATES.csv
TOP_10_DEEP_DIVES.md
TOP_3_FINALISTS.md
FINAL_SELECTION.md
```

Do not ask the owner to choose unless the top candidates are genuinely indistinguishable.

Choose the strongest initial opportunity from the evidence.

Explain why.

---

# PHASE 2 — Build ONE specialist retailer

The store should look like:

**a legitimate specialist retailer**

not:

**a dropshipping experiment.**

Initial catalog:

approximately:

```text
20–100 products
```

depending on niche structure.

Do not upload 10,000 random products.

---

# Required pages

At minimum:

```text
Home
Category pages
Product pages
About
Contact
Shipping
Returns
Warranty
Privacy
Terms
FAQ
Track Order
```

If legally required in the selected market, add appropriate company/tax/disclosure pages.

No fake office/address.

---

# Product page specification

Each product page needs:

```text
exact product title
brand
GTIN/MPN where applicable
price
stock
delivery estimate
warranty
returns
accurate specifications
dimensions
compatibility
use cases
images
manufacturer/supplier attribution if required
FAQs
alternatives
comparison links
```

Product data must come from authoritative supplier/manufacturer sources.

Never hallucinate specifications.

---

# Images

Use manufacturer/supplier-approved exact-product imagery for exact SKU representation.

AI imagery can create:

* category hero images;
* editorial illustrations;
* realistic lifestyle settings;
* visual explainers;
* comparison graphics.

But AI must never change what the actual SKU looks like in a deceptive way.

The goal is:

**better merchandising than competitors**

not fabricated products.

---

# AI differentiation

Add a premium AI product expert.

This is a conversion feature, not the core business.

The assistant should:

* understand the catalog;
* compare products;
* ask purchase-relevant questions;
* recommend only products actually sold;
* explain differences;
* answer compatibility questions;
* answer shipping/warranty questions;
* recommend accessories;
* help buyers narrow choices.

Use RAG over:

```text
catalog
manufacturer specs
manuals
FAQs
shipping policy
returns policy
warranty
comparison data
```

Never allow the model to invent product specs.

If uncertain, say so.

Persist anonymized structured conversation intent:

```text
requested_feature
budget
product_type
comparison
objection
shipping_concern
warranty_concern
recommended_sku
conversion_result
```

This becomes extremely valuable market research.

---

# Localization

Start in ONE language/country.

Use AI to make localization excellent, but do not launch clones yet.

Localization means more than translation:

```text
currency
units
shipping expectations
local terminology
product naming
consumer rights
warranty wording
payment methods
SEO queries
```

Only clone another geography after the first market produces evidence.

---

# PHASE 3 — Merchant Center

Create Merchant API v1 integration.

The integration must support:

```text
product create/update
price update
availability update
shipping data
product status
product issues
data-source management
report extraction
```

Implement scheduled syncing from supplier → internal catalog → Merchant Center.

Never blindly mirror supplier fields.

Normalize and validate.

---

# Feed quality

Required where applicable:

```text
id
title
description
link
image_link
additional_image_link
availability
price
brand
gtin
mpn
condition
google_product_category
product_type
shipping
```

Titles should match how customers search while remaining accurate.

Example:

bad:

```text
X200 Pro
```

better:

```text
Brand X200 Pro Automatic Burr Coffee Grinder — Black
```

Do not keyword-stuff.

---

# Feed validator

Implement automated checks for:

```text
missing GTIN
invalid GTIN
missing brand
invented brand
missing price
site/feed price mismatch
availability mismatch
shipping mismatch
broken image
broken landing page
missing product structured data
policy page failures
Merchant disapproval
```

All Merchant Center problems should become machine-readable issues.

---

# PHASE 4 — Free acquisition BEFORE paid acquisition

Turn on all relevant $0 distribution.

Priority:

1. Google Merchant Center free listings.
2. Organic Google Search.
3. Bing/Microsoft free product listings if supported in market.
4. Pinterest catalog only if niche has strong visual-shopping behavior.
5. Affiliate/revenue-share outreach later.

Merchant Center free listings should be treated as an acquisition channel, not merely an ad prerequisite.

Track product-level free-listing performance.

---

# SEO strategy

Do NOT create thousands of useless AI articles.

Build bottom-funnel search coverage.

Priority pages:

```text
exact model
brand + model
model review
model dimensions
model compatibility
model alternatives
Model A vs Model B
best X for specific use case
X under £Y
X for professional/user-type
brand buying guide
```

Only publish pages with meaningful unique value.

Add:

```text
canonical URLs
XML sitemap
Product structured data
Offer structured data
Breadcrumb structured data
good internal linking
fast Core Web Vitals
```

Use Search Console immediately.

---

# PHASE 5 — Analytics

Implement first-party event storage AND Google analytics/conversion integration.

Track:

```text
session
product_view
search
AI_assistant_open
AI_assistant_question
recommendation_click
add_to_cart
begin_checkout
purchase
refund
```

Every purchase must include:

```text
order_id
revenue
currency
SKU
quantity
COGS
supplier_shipping
payment_fees
contribution_profit
```

Google Ads conversion tracking must send real transaction-specific value.

Do NOT tell Google:

```text
$30 order = 1
$500 order = 1
```

when economics differ.

---

# Core daily tables

Implement:

## product_day

```text
date
country
sku
gtin

price
benchmark_price
supplier_cost
shipping_cost

impressions_free
clicks_free

impressions_paid
clicks_paid
ad_cost

product_views
ATCs
checkouts
orders
units

revenue
COGS
fees
refunds
contribution_profit
```

## store_day

```text
date
sessions
orders
revenue
AOV

COGS
supplier_shipping
ad_spend
payment_fees
refunds
software_cost

gross_profit
contribution_profit
cash_profit
```

## action_log

```text
timestamp
actor
entity_type
entity_id

action

before_state_json
after_state_json

hypothesis
reason

primary_metric
expected_direction
evaluation_date

result
```

Every meaningful campaign/feed/site change goes here.

---

# PHASE 6 — Decide whether paid traffic deserves to exist

Do not immediately spend $10/day just because it is available.

Use:

```text
free-listing impressions
free clicks
Search Console queries
SERP evidence
economic score
supplier reliability
feed approval
```

to choose ONE product cluster.

Paid budget:

```text
MAXIMUM TOTAL = $10/day
```

Do not spread this across five channels.

Use it as an information-acquisition budget.

---

# Initial paid campaign

Preferred initial test:

**Standard Shopping**

because we want interpretable product/query data and tight low-budget control.

Manual CPC is acceptable and currently supported for Shopping.

Maximize Clicks may be tested deliberately as an exploration mechanism, but remember:

**its objective is clicks, not buyers.**

Do not treat cheap Maximize Clicks traffic as proof that Google found purchase intent.

Do NOT launch PMax simply because it is fashionable.

PMax becomes a later experiment after:

* correct conversion-value tracking exists;
* enough purchase data exists;
* winning products have emerged;
* we can measure whether it actually improves contribution profit.

---

# Initial CPC calculation

Calculate:

```text
break_even_CPC =
realistic_CVR × pre_ad_contribution
```

Do not bid close to full theoretical break-even immediately.

Use a safety factor.

Example:

```text
base break_even_CPC = $2.40

initial max CPC might be:
$0.80–$1.50
```

depending on auction feasibility.

If Google cannot deliver impressions at an economically sane bid:

that itself is evidence.

Do not automatically raise CPC until the economics become impossible.

---

# PHASE 7 — Evidence-based operator state machine

Never diagnose using:

```text
"Day 7"
"Day 14"
```

alone.

Elapsed calendar time is a weak signal.

Evidence volume matters.

Classify every SKU/campaign into:

```text
NO_DELIVERY
IMPRESSIONS_NO_CLICKS
CLICKS_NO_ATC
ATC_NO_CHECKOUT
CHECKOUT_NO_PURCHASE
SALES_UNPROFITABLE
PROFITABLE_SPARSE
PROFITABLE_SCALABLE
```

---

# Diagnostic rules

## NO_DELIVERY

Investigate:

```text
Merchant eligibility
product disapproval
feed quality
bid too low
search demand absent
country/feed-label issue
inventory
account issues
```

Do not redesign the product page.

---

## IMPRESSIONS_NO_CLICKS

Investigate:

```text
product title
hero image
price
shipping
merchant credibility
query relevance
competitive offer
```

---

## CLICKS_NO_ATC

Investigate:

```text
product-market fit
offer
product relevance
landing page
trust
price
shipping
warranty
bad query traffic
```

This is where the $289 red-light-mask type failure belongs.

---

## ATC_NO_CHECKOUT

Investigate:

```text
cart friction
unexpected shipping
fees
discount expectations
checkout UX
```

---

## CHECKOUT_NO_PURCHASE

Investigate:

```text
payment methods
delivery estimate
trust
return policy
unexpected costs
checkout bugs
```

---

## SALES_UNPROFITABLE

Do NOT celebrate revenue.

Investigate:

```text
CPC
search terms
supplier cost
price
margin
refund rate
cross-sell
conversion rate
```

---

# Bayesian kill logic

Do not use arbitrary:

```text
100 clicks = kill
```

rules.

For each candidate define:

```text
minimum_viable_CVR =
expected_CPC / pre_ad_contribution
```

Then measure how plausible it remains that real CVR exceeds that threshold.

Simple zero-sale diagnostic:

```text
P(0 purchases | viable_CVR)
=
(1 - viable_CVR) ^ qualified_clicks
```

Example:

if viable economics require:

```text
CVR >= 1.5%
```

and we see:

```text
300 qualified clicks
0 sales
```

then:

```text
P(0) ≈ 1%
```

Strong evidence against viability.

Pause/fix.

But if economics only require:

```text
CVR >= 0.4%
```

300 clicks without a sale is considerably less surprising.

Implement a Beta-Binomial Bayesian model if practical.

Track:

```text
P(actual_CVR > break_even_CVR)
```

Use that probability in operator decisions.

Possible policy:

```text
<5% probability
PAUSE / KILL / MAJOR FIX

5–30%
weak evidence; continue only if test cost is justified

30–70%
uncertain

70–90%
promising

>90%
strong evidence, subject to contribution margin and supplier health
```

Do not treat these numbers as immutable laws; expose them as configuration.

---

# Prevent over-intervention

One of the common failure patterns in real operator diaries is:

```text
6 impressions
↓
change bid
↓
change bidding strategy
↓
change feed
↓
change campaign again
```

This destroys interpretability.

Implement an intervention guard.

Every proposed change should answer:

```text
What evidence triggered this?
What hypothesis are we testing?
What variable is changing?
What metric should respond?
When will we evaluate it?
```

If there is insufficient evidence, recommendation should literally be:

```text
DO NOTHING
```

---

# Search-term analysis

Search queries are a core feedback loop.

Classify them:

```text
exact/high-intent
feature-intent
brand-intent
comparison
generic
informational
irrelevant
```

Add negative keywords to eliminate demonstrably poor generic/irrelevant traffic.

Do not automatically exclude queries after one click.

Use accumulated evidence.

---

# SKU classifier

Every product becomes:

## CHAMPION

```text
repeated profitable sales
healthy contribution
acceptable supplier
```

Action:

```text
increase allocation
```

## POTENTIAL

```text
positive downstream signals
insufficient evidence
```

Action:

```text
continue controlled test
```

## SLEEPER

```text
little exposure
economics still attractive
```

Action:

```text
improve feed or isolate for deliberate test
```

## WASTER

```text
meaningful qualified traffic
economically bad
```

Action:

```text
reduce/pause
```

## ZOMBIE

```text
bad economics
bad demand
bad supply
or conclusively bad behavior
```

Action:

```text
remove
```

---

# Scaling

Do not jump:

```text
$10/day → $100/day
```

because one order happened.

Once evidence supports profitable acquisition:

increase gradually.

A reasonable starting heuristic is approximately:

```text
+10–20%
```

per scaling step, with sufficient observation between changes.

Do not scale if:

```text
supplier stock unstable
shipping deteriorating
refund rate rising
CVR collapsing
contribution margin negative
tracking broken
```

Customers should increasingly fund acquisition growth.

---

# Reinvestment model

Once profitable:

```text
profit
→ controlled acquisition reinvestment
→ more observations
→ more winners
```

Do not finance losers indefinitely with winner profits.

Track product-level capital allocation.

---

# PHASE 8 — Feed experimentation

Once traffic exists, run controlled feed experiments.

Candidate variables:

```text
product title
product type
description
hero image
additional images
price
sale price
shipping proposition
```

Log:

```text
before
after
date
hypothesis
14-day pre-period
14-day post-period
conversion-lag handling
result
```

Prefer one major variable at a time.

---

# PHASE 9 — CRO experiments

Only optimize where funnel evidence says a problem exists.

Potential interventions:

```text
shipping visibility
warranty visibility
returns clarity
comparison tables
AI expert CTA
trust information
product specification layout
payment methods
bundles
accessories
financing for higher-ticket items
```

Do not endlessly redesign a product that receives no qualified traffic.

---

# PHASE 10 — AI advantage

Once traffic exists, use the AI system aggressively where it creates measurable value.

Experiments:

```text
AI expert vs no AI expert
AI recommended alternative
AI comparison
AI accessories
AI objection handling
AI localization
AI post-purchase support
```

Track:

```text
assistant users CVR
non-assistant users CVR
AOV difference
support deflection
recommended-SKU conversion
```

AI must earn its complexity through measurable contribution.

---

# PHASE 11 — Geographic expansion

Do NOT begin by launching UK + Norway + Denmark + Sweden simultaneously.

Once a product/store works in Country A:

rerun the economics for Country B.

Compare:

```text
search volume
CPC
Shopping competition
market price
supplier shipping
returns
tax/compliance
language
payment preference
```

If another market looks materially better:

clone the proven system.

This is where Norway/Denmark/etc. become powerful.

They are expansion hypotheses, not the founding strategy.

---

# Required dashboards

Build an operator dashboard with:

## Opportunity

```text
product
country
supplier
expected CPC
realistic CVR
break-even CVR
economic headroom
competition
shipping
score
```

## Funnel

```text
impressions
clicks
product views
ATC
checkout
purchase
```

## Economics

```text
revenue
COGS
shipping
fees
ads
refunds
contribution
```

## Operator

```text
state
confidence
recommended action
reason
next evaluation
```

---

# Daily machine-readable decision

Generate:

```json
{
  "date": "...",
  "store_state": "...",
  "paid_spend_today": 0,
  "paid_budget_cap": 10,
  "best_skus": [],
  "worst_skus": [],
  "anomalies": [],
  "recommended_actions": [],
  "recommended_no_actions": [],
  "experiments_due_for_evaluation": [],
  "capital_allocation": {},
  "confidence": {}
}
```

---

# Every recommendation must include

```text
OBSERVATION

HYPOTHESIS

ACTION

EXPECTED RESULT

KILL CONDITION

NEXT EVALUATION
```

Example:

```text
OBSERVATION:
SKU 182 received 163 qualified clicks,
0 ATCs.

HYPOTHESIS:
Offer/product relevance is poor rather than
campaign delivery.

ACTION:
Pause paid traffic to SKU 182 and compare
price/shipping/page against top five Shopping merchants.

EXPECTED RESULT:
Identify offer disadvantage.

KILL CONDITION:
No clear correctable disadvantage and economics remain weak.

NEXT EVALUATION:
After competitor/offer review.
```

---

# Paid API philosophy

Use paid APIs only if they improve:

```text
supplier discovery
SERP visibility
Shopping merchant counts
price monitoring
keyword metrics
competitive intelligence
```

Create provider interfaces so no commercial API becomes hardcoded infrastructure.

Example abstraction:

```text
KeywordProvider
SerpProvider
ShoppingSerpProvider
SupplierProvider
TrendProvider
```

The system should continue operating if one provider disappears.

---

# Validation / QA before launch

The site may not launch paid ads until:

```text
checkout works
payment works
mobile works
HTTPS works
policies exist
shipping is accurate
returns are accurate
product prices match feed
availability matches feed
Merchant Center products approved
conversion tracking verified
transaction values verified
COGS ingestion working
analytics events verified
AI expert does not hallucinate specs
```

Run automated end-to-end tests.

---

# Human-required actions

Do everything autonomously that is safe and technically possible.

When an action requires the owner, output a concise checklist.

Examples:

```text
open/verify Google Merchant Center
verify Google Ads billing
supplier dealer agreement
business verification
payment processor KYC
domain purchase
legal company details
```

Do not block other work while waiting if independent tasks remain.

---

# Definition of MVP success

MVP is NOT:

```text
website deployed
```

MVP is:

```text
one selected market
+
one evidence-selected catalog
+
one working supplier path
+
approved Merchant feed
+
free product distribution
+
complete analytics
+
true contribution P&L
+
$10/day experiment capability
+
evidence-based operator decisions
```

---

# Definition of first commercial validation

Minimum:

```text
real unrelated customer
+
successful fulfillment
+
known true contribution economics
```

One order is evidence, not proof.

Continue until confidence in:

```text
CVR
CPA
contribution/order
supplier reliability
refund behavior
```

is adequate.

---

# Definition of scale

Only call something scalable when:

```text
P(CVR > break_even_CVR) is strong
AND
contribution profit remains positive
AND
supplier can support volume
AND
returns/shipping remain healthy
AND
incremental spend remains economically productive
```

---

# Important anti-patterns

Do NOT:

* build six country stores before one sale;
* build a giant AI platform before traffic;
* add 5,000 random supplier SKUs;
* choose a niche because a guru recommended it;
* optimize only ROAS;
* confuse revenue with profit;
* use calendar time alone as a kill rule;
* constantly modify campaigns without evidence;
* blindly use PMax with no conversion-value history;
* blindly use Maximize Clicks and assume clicks equal buying intent;
* invent GTINs;
* invent reviews;
* fake delivery promises;
* compete solely by having prettier AI images;
* rely on 12–20 day shipping for urgent products without pricing that friction into expected CVR;
* call a niche low-competition without examining exact SKU saturation.

---

# First execution sequence

Execute in this order:

```text
1. Build schemas/database.
2. Connect research sources.
3. Generate candidate product × country universe.
4. Find and normalize suppliers.
5. Estimate exact-SKU competition.
6. Calculate economics and uncertainty.
7. Rank candidates.
8. Deep-dive top 10.
9. Select ONE opportunity.
10. Secure viable supplier path.
11. Register/select one domain.
12. Deploy commerce backend.
13. Build specialist storefront.
14. Create accurate catalog.
15. Add AI expert.
16. Implement Merchant API v1.
17. Validate feed.
18. Enable free listings.
19. Implement Search Console/SEO.
20. Collect free signal.
21. Select strongest paid product cluster.
22. Launch maximum $10/day Standard Shopping experiment.
23. Log every state/action.
24. Apply Bayesian WAIT/FIX/KILL/SCALE logic.
25. Reinvest only when economics justify it.
```

---

# Final operating philosophy

We are NOT trying to become world-class Google Ads media buyers.

We are trying to systematically discover:

**markets where a mediocre media buyer can make money because the underlying economics are favorable.**

Treat every dollar spent as buying information.

Treat every failed candidate as valuable negative data.

Treat every change as an experiment.

Treat contribution profit as ground truth.

Find the first product/query/market combination that works.

Then concentrate.

Then scale.

Then automate.

Then expand geographically.

Do not reverse that order.

I would give the coding agent that prompt **plus the ZIP we built from the case studies** as its research corpus. The most important engineering feature is the Bayesian/economic decision layer: that is what turns the real operator diaries into something materially better than another product-research dashboard. Merchant Center’s Best Sellers data explicitly includes rank, previous rank, relative demand, riser/sinker state and market price ranges, which maps directly into the research layer above. ([Google Cloud Documentation][2])

[1]: https://developers.google.com/shopping-content/guides/deprecation-and-sunset?utm_source=chatgpt.com "Deprecation and sunset  |  Content API for Shopping (Deprecated)  |  Google for Developers"
[2]: https://docs.cloud.google.com/bigquery/docs/merchant-center-best-sellers-schema?hl=en&utm_source=chatgpt.com "Google Merchant Center best sellers table  |  BigQuery  |  Google Cloud Documentation"
