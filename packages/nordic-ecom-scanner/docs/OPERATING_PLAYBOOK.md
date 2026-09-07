# Operating Playbook — From Scanner Row to Profitable Store

## Phase 0 — Pick a narrow store thesis

Do not launch “Nordic Home Shop.” Launch a category with a clear buying job, e.g.:

- architectural hardware for design-led renovations;
- rechargeable tabletop lighting and presentation hardware for hospitality;
- acoustic/decorative wall systems with a room calculator;
- compact premium organization hardware.

A narrow thesis improves Google feed relevance, conversion, cross-sell and expert/AI assistance.

## Phase 1 — Discover 100–500 candidate SKUs

Use Kopy/POKY or supplier feeds for catalog discovery, not as the source of truth. Normalize every product into a canonical SKU record:

- supplier URL / supplier ID;
- material, dimensions, finish, weight;
- MOQ;
- unit price tiers;
- packaging dimensions/weight;
- battery/electrical flags;
- available compliance documents;
- sample cost;
- shipping methods;
- manufacturing lead time;
- variants.

Then create market-specific query families in Norwegian and Danish.

## Phase 2 — Observe Google Shopping

For each commercial query capture:

- 10–30 Shopping offers;
- merchant name/domain;
- exact displayed price and shipping if available;
- title;
- image URL;
- product/merchant position;
- brand;
- reviews/ratings if available;
- whether the offer is marketplace/direct retailer;
- duplicate product/image families.

The included Serper adapter automates the basic Shopping observation. Store the raw response in `observations` so historical SERPs can be compared later.

## Phase 3 — Keyword economics

Use Google Keyword Planner export (free/manual) or DataForSEO (automated adapter included) for:

- monthly search volume;
- estimated CPC;
- competition;
- related commercial terms.

Use specific purchase queries rather than broad inspiration queries. Examples:

Norway:
- `messing håndtak kjøkken`
- `knott messing skap`
- `oppladbar bordlampe restaurant`
- `menyholder restaurant`

Denmark:
- `messing greb køkken`
- `knop messing skab`
- `genopladelig bordlampe restaurant`
- `menukortholder restaurant`

Validate actual local phrasing with live query data before spending.

## Phase 4 — Supplier validation

For every top candidate request a written quote including:

- exact SKU/variant;
- MOQ;
- sample price;
- unit price at 1/10/50/100+;
- DDP/DDU freight alternatives;
- carton dimensions and gross weight;
- damage/replacement policy;
- delivery SLA;
- product-safety/compliance documentation;
- battery paperwork where relevant;
- packaging customization;
- neutral dropship packing;
- tracking availability;
- origin address shown to customer/carrier.

Order samples before scaling. For products with meaningful safety/compliance risk, obtain professional compliance review rather than trusting a marketplace badge.

## Phase 5 — Fulfilment strategy ladder

1. **Validation:** supplier-direct only for low-risk products where delivery is acceptable and customer sees the real promise.
2. **Early traction:** negotiate faster lines / consolidation / EU or Nordic warehouse options.
3. **Winner:** hold a small amount at EU/Nordic/UK 3PL; use reorder point based on campaign velocity.
4. **Scale:** private packaging, negotiated manufacture, QA batch checks and possibly exclusive finishes/bundles.

The objective is to use dropshipping as demand validation, not remain permanently dependent on the weakest logistics.

## Phase 6 — Storefront localization

### Norway

Must have:
- high-quality Norwegian copy;
- NOK pricing;
- Vipps + card route where available;
- exact seller identity and contact data;
- transparent shipping origin;
- delivered-price/VAT clarity;
- VOEC handling if eligible;
- realistic delivery range;
- clear return destination/cost;
- local-language support.

Do **not** imply the legal seller is Norwegian if it is not.

### Denmark

Must have:
- natural Danish copy;
- DKK pricing;
- MobilePay + cards;
- seller identity and VAT/legal information;
- total-price/shipping clarity;
- 14-day withdrawal workflow;
- fault/legal-guarantee process;
- OSS/IOSS/import configuration as applicable;
- clear return destination/cost.

## Phase 7 — Merchandising advantage

Improve the offer without misrepresenting the product:

- clean hero image of the actual SKU;
- dimension image;
- finish/material close-up;
- in-context image;
- bundle/quantity selector;
- delivery date estimate;
- concise technical attributes;
- comparison table within your range;
- installation guide where relevant;
- trade quantity request;
- room/project calculator for panels/hardware;
- AI adviser trained only on your verified catalog facts.

Never generate an image that depicts a materially different product and use it as the main commerce image.

## Phase 8 — Google feed

Maintain a market-specific feed with:

- accurate localized title;
- brand/GTIN/MPN where applicable;
- exact availability;
- tax-inclusive local price;
- correct shipping data;
- canonical landing page;
- product category/type;
- material/colour/size attributes;
- image URL representing the exact product.

Google Shopping in Norway, Denmark and many European markets operates through the CSS ecosystem; Google Shopping itself can serve as a CSS.

## Phase 9 — Paid validation

Per candidate or tight product group:

- bounded initial budget;
- no broad automatic scaling before conversion evidence;
- capture search term, impressions, CTR, CPC, product-page CVR, checkout-start CVR, purchase CVR, refund/return and gross contribution;
- distinguish consumer vs trade/multi-unit order;
- kill products that cannot clear break-even under plausible optimization.

A useful early rule is to stop celebrating ROAS and watch **contribution after VAT, product, fulfilment, fees, returns and ads**.

## Phase 10 — Learning loop

Write campaign evidence back to the scanner:

- replace estimated CPC with observed CPC;
- replace assumed CVR with observed cohort CVR;
- replace expected return rate with realized returns;
- update landed cost with invoice truth;
- update delivery days with tracking truth;
- update AOV/bundle multiplier with order truth.

Over time the scanner becomes a private dataset of what actually works by country/category.
