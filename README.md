# Drop — Compatibility Commerce Compiler

*Last Updated: 2026-09-07*

---

## What Is This?

We build the machine-readable compatibility layer that AI agents need to transact with local service providers and specialist product merchants. Then we own the supply side by giving them a free AI front desk.

---

## Project Structure

```
drop/
├── AGENTS.md              # Binding rules
├── THESIS.md              # Core thesis
├── README.md              # This file
├── HANDOVER.md            # State for next agent
├── campaigns/             # Active campaigns
│   └── active/            # 25 campaigns
├── docs/                  # Documentation
│   ├── guides/            # Setup guides
│   ├── maritime/          # Maritime opportunities
│   ├── plans/             # Queued plans
│   └── verification/      # Campaign verification
├── data/                  # Data files
│   └── dropcomp/          # Competitor intelligence
├── bigquery/              # BigQuery schemas
├── corpus/                # Case studies
└── secrets/               # Credentials (not in git)
```

---

## Active Campaigns (25)

Located in `campaigns/active/`:

| Campaign | Country | Gap Score |
|----------|---------|-----------|
| balcony-door-hardware | NO | 10/10 |
| vallox-ventilation | FI | 10/10 |
| heatpump-electronics | FI | 9/10 |
| hottub-control-panels | NO/SE/FI | 9/10 |
| marine-electronics-retrofit | NO | 8/10 |
| window-hardware-scandinavia | SE | 8/10 |
| + 19 more | Various | 5-9/10 |

---

## The Stack (No Shopify)

| Layer | What You Need | Cost |
|-------|---------------|------|
| Google Merchant Center | Product feed with conversational attributes | Free |
| Feed Management | Feedify or direct CSV | Free-$50/mo |
| Web Store | Next.js on Vercel | Free |
| Payments | Stripe | 2.9% + $0.30 |
| Domain | ~$15/year | ~$15/year |

**Total: ~$15/year + Stripe fees**

---

## What's Next

1. Build balcony-door subgraph in voiceagent
2. Deploy to Cloudflare
3. Add JSON-LD structured data
4. Submit to Google Merchant Center
5. Apply for ChatGPT merchant access
6. Test with 50 compatibility questions

---

## Git Repos

| Repo | Purpose |
|------|---------|
| prx0r/drop | This repo |
| prx0r/voiceagent | Drop Resolver Runtime |
| prx0r/cg | CG judge worldpack |
| prx0r/dropcomp | Competitor intelligence |
| prx0r/gitgoblin | Opportunity discovery |
