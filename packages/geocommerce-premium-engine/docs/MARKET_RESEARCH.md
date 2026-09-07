# Market research — 2026-09-04

## The strongest evidence stack
Use official Google data first:
1. Google Ads API Keyword Planning: country/language keyword ideas, historical monthly searches, competition index and 20th/80th percentile top-of-page bids; forecasts can estimate clicks, CPC and cost.
2. Merchant API Market Insights: best sellers by country/category, competitive price points and competitive visibility, subject to account eligibility.
3. Free listings: launch localized catalog surfaces before meaningful ad spend.
4. SerpApi or another licensed SERP provider only where literal Shopping-result snapshots are needed.
5. DataForSEO as a scalable keyword-data fallback/augmentation; normalize all prices/CPCs into the target market currency before economics.

Google explicitly rate-limits Keyword Planning and recommends caching because historical metrics refresh monthly. This architecture stores every observation with provenance and date instead of calling the API repeatedly.

## Priority markets
### 1. Finland
Why: excellent AI-era language moat, 84% of consumers reported shopping online in the prior 30 days in PostNord's spring 2026 survey, and checkout/delivery localization matters. Online-bank payments remain especially important. Start here for categories where local Shopping competition is measurably weak, not because Finland is universally cheap.

### 2. Norway
Why: high purchasing power and 78% of consumers reported a cross-border purchase in the prior year. Vipps is now the most used and preferred payment method. The danger is checkout friction: PostNord says 6 in 10 had cancelled a purchase during checkout, most commonly due to shipping price. Norway therefore requires unusually explicit delivered-cost and delivery-window handling.

### 3. Switzerland
Why: premium AOV potential and multiple language surfaces. Best for products where a high contribution margin can absorb customs/service overhead. Treat German and French surfaces separately. TWINT/invoice/card expectations matter.

### 4. Belgium
Why: strong ecommerce and a genuine language-fragmentation moat. Compile Dutch and French experiences separately. Bancontact is an important checkout expectation.

### 5. Austria
Why: high-value German-language market that can reuse core German semantics while having its own auction and pricing economics. Do not infer Austria from Germany.

### 6. New Zealand
Why: wealthy ecommerce market with English-language low localization burden. The main constraint is logistics; prioritize AU/NZ stock or products with unusually strong contribution margins.

### 7. Denmark
Strong ecommerce, but not automatically low-ad-cost. Use scanner evidence per category; Denmark is a selective opportunity rather than a blanket priority.

### 8. Portugal
Good language moat but lower purchasing power than Nordics/Switzerland. Bias toward medium-ticket products and local payment expectations such as MB WAY/Multibanco.

## Country selection algorithm
Country score should never be static. For every `product × country × date`, collect:
- exact local-language keyword clusters;
- monthly demand and trend;
- competition index and bid ranges;
- benchmark retail price;
- Shopping seller count/snapshot where licensed;
- supplier landed cost in target currency;
- shipping days and returns path;
- local checkout/payment/delivery fit;
- actual free-listing and paid-test outcomes once live.

The best country is the one with **the best economics for this product now**, not the highest GDP or lowest generic CPC.

## Product-category research
The engine should scan these first because they combine advice value, evergreen intent and premium visual merchandising:

### Tier A — strongest initial hypotheses
- premium pet mobility/furniture: ramps, stairs, crates, feeding/storage systems; avoid medical claims;
- ergonomic workspace systems: desk frames, monitor/workstation systems, premium desk accessories;
- premium coffee equipment: espresso machines, grinders, brew stations; require warranty/service and electrical compliance;
- compact home fitness/recovery equipment where shipping is manageable and medical claims are unnecessary;
- workshop/storage/organization systems;
- craft/prosumer equipment where a novice benefits from guided selection.

### Tier B — potentially excellent but operationally heavier
- massage chairs and large recovery furniture;
- infrared saunas/home wellness furniture;
- premium outdoor living/furniture systems;
- wine/cigar storage appliances;
- higher-end hobby machines.

These can produce strong AOVs but freight, damage, warranty and reverse logistics are capable of destroying apparent margin. Treat them as assisted/quote sales until real data proves direct checkout works.

### Avoid initially
- fashion/sizing-heavy goods;
- supplements/medical devices/medical claims;
- baby/child safety-critical products;
- uncertified electrical goods;
- commodity branded electronics;
- fragile low-margin furniture;
- complex vehicle fitment;
- anything where the supplier cannot provide exact warranty, stock and delivery truth.

## Key research sources
- Google Ads Keyword Planning overview: https://developers.google.com/google-ads/api/docs/keyword-planning/overview
- Google historical metrics: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-historical-metrics
- Google keyword ideas: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas
- Merchant market insights: https://developers.google.com/merchant/api/guides/reports/understand-the-market
- Merchant competitive visibility: https://developers.google.com/merchant/api/guides/reports/explore-competitive-landscape
- Merchant reporting REST: https://developers.google.com/merchant/api/guides/reports/get-started
- Google free listings: https://support.google.com/merchants/answer/13692890
- Merchant languages/currencies: https://support.google.com/merchants/answer/160637
- PostNord Nordics 2026: https://www.postnord.com/insights/reports/e-commerce-in-the-nordics-spring-2026/
- Finland checkout 2026: https://www.postnord.com/insights/finland/finland-spring-2026/finnish-payment-and-checkout-behavior-spring-2026/
- Norway checkout 2026: https://www.postnord.com/insights/norway/norway-spring-2026/norwegian-payment-and-checkout-behavior-spring-2026/
- Norway cross-border 2026: https://www.postnord.com/insights/norway/norway-spring-2026/cross-border-shopping-marketplaces-in-norway-spring-2026/
