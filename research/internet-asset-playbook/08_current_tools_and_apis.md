# 8. Current tools and APIs — September 2026

## Demand / trend discovery

### Google Trends API alpha

Google now has an official Trends API in alpha. It offers a rolling five-year window, regular interval aggregation, regional/sub-regional data, and consistently scaled data. Apply for alpha access; use the public Trends UI meanwhile.

**Use for:** persistent demand, seasonality, geography, rising terms.

### Google Search Console API

Once the site is live, this is your most valuable free data source because it tells you actual queries, pages, impressions, clicks, countries, and devices for your property.

**Use for:** discovering page families from real impressions rather than keyword-tool guesses.

### X API

X moved to pay-per-use pricing. Current docs list Post reads at about **$0.005 per resource**, user reads around $0.010, and trend reads around $0.010, with monthly caps for pay-per-use access.

**Use for:** targeted complaint/recommendation sampling, not broad firehose scraping.

**Cost rule:** query narrowly; cache aggressively; do not use X as your primary keyword database.

### Reddit API

Reddit’s current Data API terms reserve the right to charge and say commercial uses or uses beyond permitted limits may require a separate agreement. Do not build a commercial corpus assuming unlimited free scraping rights.

**Use for:** manual/high-signal research, allowed API use, and linking back to source discussions rather than mass copying.

### Hacker News API / public feeds

Useful free signal for technical pain, launches, tool replacements, and product sentiment.

### TrustMRR / public revenue databases

Excellent for verifying whether a business model is actually collecting money. Treat the platform’s own verified payment-provider figures as stronger evidence than founder screenshots.

## Search / SERP data

Use paid SERP/keyword APIs only after a candidate niche passes manual validation. The objective is to avoid paying to over-research bad niches.

Useful categories:

- SERP APIs (DataForSEO, Serper-like services);
- SEO suites (Ahrefs, Semrush);
- backlink analysis;
- rank tracking;
- site crawling.

Your first $50 is usually better spent validating partner economics than buying a giant keyword export.

## Data ingestion

Prioritize in this order:

1. official API;
2. public feed/RSS;
3. partner feed;
4. public structured data / JSON-LD;
5. explicitly allowed crawling;
6. manual verification.

## Affiliate rails with meaningful payouts

Current official examples:

### Semrush

Program currently advertises roughly $100–$300 per sale depending on product, with some trial payouts and higher loyalty tiers.

### Kinsta

Eligible WordPress referrals can pay $50–$500 one-time plus 10% recurring.

### Webflow

Base affiliate offer is 50% revenue share on a qualifying new customer’s first eligible subscription, for up to 12 months.

These illustrate why B2B software comparison pages can monetize at low traffic if the intent is strong.

## Hosting / deployment

For the first validation version, static HTML is enough. A domain plus free/cheap static hosting can support a directory until there is real usage.

Do not introduce a database, vector store, queues, or autonomous agent framework before the money loop needs them.

## Recommended “cheap stack”

```text
Discovery: Google Trends + web search + communities
Store: JSON/SQLite/Postgres
Verification: source URL + timestamp + change hash
Site: static generator / Next.js only when needed
Hosting: Cloudflare Pages / Vercel / equivalent
Analytics: Search Console + privacy-respecting web analytics
Email capture: simple provider
Payments: Stripe / Lemon Squeezy / Polar
Automation: cron/GitHub Actions + one LLM call where valuable
Alerts: email/Telegram
```

The sophisticated part should be the **data and selection**, not the infrastructure.
