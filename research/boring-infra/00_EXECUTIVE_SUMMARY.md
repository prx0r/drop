# Executive summary

## Verdict

There is a real class of asymmetric software businesses here, but the edge is **not** “AI writes lots of websites.” The strongest repeatable pattern is:

> Find a repetitive, expensive, boring workflow that already exists; remove one integration/data-conversion/monitoring step; sell the saved time or reduced failure risk; keep the product narrow enough that one person can support it.

The best current evidence is striking:

- **Web3Forms**: a contact-form backend — about **$44.1k revenue in 30 days, $38.5k MRR, 2,790 active subscriptions**.
- **1Lookup**: one API for phone/email/IP/data validation — about **$406k revenue in 30 days, $235.7k MRR, 669 subscriptions**.
- **LLM Gateway**: one endpoint across LLM providers with routing/usage metering — about **$255k in 30 days, $78.4k MRR, 1,356 subscriptions**.
- **Local SEO Bot**: Google Maps/local-search operations for SMBs — about **$10.5k in 30 days, $11.1k MRR, 83 subscriptions**.
- **Synta**: an expert MCP/web layer around n8n workflows — about **$9.6k in 30 days, $10.2k MRR, 211 subscriptions**, despite a low domain rating.
- **OpenAlternative**: a structured directory monetized with sponsorship/placement — about **$6.7k in 30 days and $5.9k MRR**.
- **BankConv**: bank-statement-to-structured-data utility — about **$788 in 30 days / $846 MRR**; founder states roughly **95% margins**.

The outlier lesson is not “build any API.” The loser comparisons prove that wrong. Generic uptime monitoring, generic PDF parsing and generic agent hosting can sit at tens or hundreds of dollars while adjacent narrow products do five figures.

## The 7 recipes that survive the evidence

1. **One ugly input → one clean output**  
   PDF/CSV/email/portal data goes in; normalized records go out. Charge per document, per usage or per seat.

2. **One fragmented capability → one API key**  
   Aggregate several annoying services behind a common schema, billing balance, dashboard and SDK.

3. **One high-intent stream → one alert**  
   Watch a source buyers already use; classify events; alert immediately; send to CRM/webhook.

4. **One legacy workflow → expert adapter**  
   Don't build “AI for everything.” Build the expert interface for a single sticky product/workflow.

5. **One niche's repetitive admin → browser extension**  
   Extensions win when the user already lives inside a portal and the software can remove clicks without replacing the system of record.

6. **One fragmented market → structured directory/data asset**  
   Free discovery to accumulate demand; monetize suppliers with premium placement, sponsorship, feeds, alerts or lead routing.

7. **One local recurring outcome → productized automation**  
   Customers pay recurring fees for calls/leads/rankings/results, not for a dashboard they must learn.

## What I would build first

For a low-capital solo operator, I would prioritize:

**A. Vertical document normalizer** — e.g. convert a specific recurring statement/export used by accountants, property managers, trades or agencies into exactly the format required by Xero/QuickBooks/Excel/import tool. This is the cleanest BankConv-style wedge.

**B. Niche workflow adapter/MCP** — an expert layer over a system people already use daily (Xero, ServiceM8/Fergus-type field systems, a procurement portal, a compliance portal). The Synta evidence suggests the wedge is strongest when it performs real edits/actions and understands the domain workflow, not when it merely chats.

**C. Intent monitor for a legally accessible source** — procurement pages, tender feeds, public directories, change notices, job feeds or official registries. Avoid depending on fragile/private scraping where platform ToS is a major risk.

**D. Structured niche directory with a seller-funded monetization layer** — but only when the directory answers a transaction-proximate query. JobBoardSearch/OpenAlternative show why “directory + distribution” can work; generic directories usually do not.

## Critical rule

**Clone the economics, not the product.**

The engine in this ZIP scores opportunities by verified demand, willingness to pay, build simplicity, data access, workflow frequency, distribution wedge, localization potential, platform risk and support burden. It is designed to find transplants such as:

> BankConv recipe → insurance commission statement normalizer → property management rent-roll normalizer → UK trade-supplier invoice normalizer.

That is the asymmetric game: repeat a proven *shape* where the customer/workflow/distribution is different.
