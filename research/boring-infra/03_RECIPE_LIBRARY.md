# Recipe library

## Recipe 1 — Ugly input → exact clean output

**Proof:** BankConv; receipt/document utilities.  
**Buyer:** accountants, bookkeepers, operations teams, agencies, property managers, trades.  
**Trigger:** “I have this file/export every week/month and need it in that system.”

MVP:
1. one input format;
2. one target schema;
3. preview + validation;
4. export;
5. save mapping;
6. email/API/Sheets delivery.

Pricing: £2–£10 per document, £19–£99/month, or practice/team plan.

Moat: corpus of edge cases + mappings + correction feedback, not the OCR model.

---

## Recipe 2 — Many suppliers → one normalized API

**Proof:** 1Lookup; LLM Gateway.  
**Buyer:** developers/ops teams tired of maintaining several integrations.

MVP:
1. shared request schema;
2. provider routing;
3. retries/fallbacks;
4. common response schema;
5. usage metering;
6. one invoice;
7. audit log.

Pricing: markup + subscription, or committed credits.

Moat: reliability, routing logic, billing simplicity, compatibility layer.

---

## Recipe 3 — Valuable event → instant alert

**Proof:** Groups Watcher.  
**Buyer:** service firms, sales teams, procurement, investors, operators.

MVP:
1. watch 1–3 lawful/public sources;
2. normalize events;
3. rule/LLM classification;
4. dedupe;
5. email/Slack/webhook;
6. 1-click “relevant / irrelevant” feedback.

Pricing: £49–£499/month if event value is high. A £5k job makes a £199 monitor rational.

Moat: source coverage + precision + latency + workflow integration.

---

## Recipe 4 — Sticky incumbent → expert adapter

**Proof:** Synta around n8n.  
**Buyer:** people already paying for or depending on a complex system.

MVP:
1. official API/OAuth;
2. domain object model;
3. 5 high-frequency jobs;
4. dry-run;
5. validation;
6. human approval for consequential actions;
7. rollback / activity log.

Pricing: £20–£100/user/month or team/site pricing.

Moat: safe execution + workflow knowledge + history/memory.

---

## Recipe 5 — Existing webpage → browser-native workflow tool

**Proof:** FriendFilter/GroupFilter.  
**Buyer:** users trapped in a portal/system that will not change.

MVP:
1. detect page/context;
2. extract current objects;
3. add one decision/action;
4. keep data local where practical;
5. optional cloud sync.

Pricing: £10–£50/month.

Moat: convenience at the exact place work happens.

Risk: platform ToS/API changes. Prefer extensions over official/authorized interfaces or user-side transformations; avoid credential theft or covert automation.

---

## Recipe 6 — Fragmented market → buyer-facing directory → seller-paid distribution

**Proof:** OpenAlternative; JobBoardSearch.  
**Buyer side:** free search/discovery.  
**Seller side:** paid placement, sponsorship, verification, feeds, lead routing, category ownership.

MVP:
1. narrow taxonomy;
2. 100–500 high-quality entities;
3. buyer filters that genuinely matter;
4. canonical detail pages;
5. free claim/update flow;
6. paid featured placement only after traffic exists.

Pricing: £19–£599/month depending on traffic and deal size.

Moat: structured data + audience + update process.

---

## Recipe 7 — Local recurring outcome → productized automation

**Proof:** Local SEO Bot.  
**Buyer:** SMB with obvious local customer economics.

MVP:
1. connect GBP/analytics/search data;
2. baseline audit;
3. weekly actions;
4. ranking/call tracking;
5. exception queue;
6. concise outcome report.

Pricing: £79–£499/location/month.

Moat: localized process + proof of outcome + low-touch operations.

---

## Recipe 8 — Open-source/free primitive → hosted reliability layer

**Proof:** LLM Gateway illustrates the broader pattern.  
**Buyer:** teams that do not want to operate infrastructure themselves.

What is sold:
- hosting;
- observability;
- billing;
- SLA;
- backups;
- upgrades;
- access control;
- policy/guardrails;
- support.

The asymmetric move is not to invent a new category. It is to turn a technically annoying but proven open-source primitive into a boring paid service for a narrower market.
