# Winner / loser pairs: what the viral “just build a tool” thesis misses

This comparison is more valuable than a list of winners because it shows that **problem category alone does not produce revenue**.

## 1. Contact-form backend

**Winner:** Web3Forms — ~$44k 30d / ~$38.5k MRR / 2,790 active subscriptions.  
**Smaller proof:** Static Forms — ~$964 30d / ~$847 MRR / 102 subscriptions.

**Inference:** the underlying primitive is valid, but distribution, reliability, documentation, free tier, ecosystem integrations and time-in-market create orders-of-magnitude differences.

**Recipe:** do not make another generic form backend. Find an ecosystem where forms are still painful: a static-site generator, localized compliance workflow, vertical website-builder ecosystem, agency white-label workflow, or structured intake that produces a downstream business object.

---

## 2. Document / statement parsing

**Winner:** BankConv — ~$846 MRR, 24 active subscriptions, founder claims ~95% margin and supports 1,000+ banks + multiple target formats.  
**Failure analogue:** Parse My Statement — ~$1 lifetime at the snapshot.  
**Smaller consumer proof:** Receipt Genie — hundreds/month with hundreds of subscriptions.

**Inference:** “AI parses PDF” is not a moat. Breadth, accuracy, target-specific exports, integrations and organic search around exact document types are the product.

**Recipe:** start with one document and one downstream import. Expand formats only after users pay.

---

## 3. AI/agent infrastructure

**Winner:** Synta — ~$10.2k MRR as an expert layer for n8n.  
**Failure analogue:** DeployHermesAgent — ~$29 lifetime at the snapshot despite solving agent hosting/setup.

**Inference:** generic hosting is easy to understand but weakly differentiated. Deep workflow expertise is stronger because it replaces skilled labor inside a product users already depend on.

**Recipe:** “MCP for X” is weak. “Perform the five painful X workflows safely, with domain-specific objects, validation and rollback” is strong.

---

## 4. Monitoring

**Winner-ish adjacent model:** Groups Watcher — ~$24k MRR because the alert directly maps to a sales opportunity.  
**Weak generic example:** UptimeObserver — ~$144 MRR.

**Inference:** monitoring becomes expensive when the detected event is economically valuable and time-sensitive. Generic uptime is crowded and price-compressed.

**Recipe:** monitor events where the alert is worth £100–£10,000 to someone: a tender opens, a permit is filed, a business changes ownership, a key product becomes available, a regulatory notice affects a specific workflow, a prospect explicitly asks for a service.

---

## 5. Directory/data products

**Winner:** OpenAlternative — ~$5.9k MRR plus advertising; 300k monthly pageview claim on its ad page.  
**Winner:** JobBoardSearch — ~$96k lifetime through promotion/distribution economics.  
**Weak generic example:** MicroSaaS Directory — only tens of dollars of MRR at the snapshot.

**Inference:** a directory is not the business. The business is **high-intent discovery + a vendor with money who benefits from being discovered**.

**Recipe:** never build “a directory of things.” Build “the decision surface used immediately before a transaction.”

---

## 6. Generic API vs aggregated utility

**Winner:** 1Lookup — ~$235k MRR and hundreds of subscriptions across many related validations.  
**Weak example:** API Plugin — only hundreds of dollars lifetime at the snapshot.

**Inference:** wrapping an API is weak. Aggregating several messy suppliers into a normalized schema, one balance, reliability layer, docs and support is valuable.

**Recipe:** target a buyer who currently maintains 3–8 vendors, spreadsheets or scripts to accomplish one recurring job.

---

# The common failure modes

1. **Category copying** — seeing a successful parser and building “a parser.”
2. **No distribution wedge** — product launches into a generic keyword dominated by incumbents.
3. **No economic event** — output is interesting, but it does not save money, create revenue, prevent loss or satisfy a recurring obligation.
4. **Dashboard tax** — requiring users to remember to log in instead of sending the answer into email/Slack/CRM/webhook.
5. **Too broad on day one** — broad surface area, low reliability, high support burden.
6. **AI as value proposition** — instead of invisible implementation detail.
7. **Platform fragility** — depending on private scraping or brittle automation with no backup data source.
8. **No retention loop** — a one-time task sold as a subscription.
