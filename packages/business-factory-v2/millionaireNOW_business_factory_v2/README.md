# millionaireNOW Business Factory v2

Five new zero/near-zero-capital kernels chosen because real buyers already pay for the underlying outcome. This version upgrades the first factory from "specification-quality" to "tested kernel": pinned dependencies, shared request IDs/rate limits/admin auth, deterministic scoring, provenance/event ledgers, live-source adapters where official APIs exist, and automated tests.

## The five businesses

| Port | App | Sell this outcome | First niche |
|---|---|---|---|
| 8201 | SaaS Savings Desk | verified annual software savings | 20-200 employee agencies/SaaS firms |
| 8202 | Public Signal Radar | fresh commercial-intent signals | UK builders / solar / architects |
| 8203 | Tender Bid Desk | relevant tenders + bid/no-bid triage | small UK IT/security/professional services |
| 8204 | Database Reactivator | booked appointments from owned dormant lists | high-ticket local services |
| 8205 | RFQ Sourcing Desk | comparable supplier quotes | ugly specialist B2B sourcing niches |

## Why these are better than v1

1. They start with data the customer already owns or public data, not paid traffic.
2. Four can sell an outcome before you integrate any paid third-party API.
3. Each has an explicit money event (`savings`, `won`, `held`, `award`) rather than stopping at a report.
4. External factual claims require source/provenance where relevant.
5. Human approval is retained where communications or procurement decisions create risk.

## Run

```bash
cp .env.example .env
# change ADMIN_TOKEN
docker compose up --build
```

Or locally from repo root:

```bash
pytest -q
uvicorn 01_saas_savings_desk.app:app --port 8201
```

## Launch doctrine

Do not build integrations until one customer asks for them. Use CSV/manual ingestion first where possible. Sell the result manually, observe what customers actually pay for, then automate the repeated bottleneck.

Read `research/MARKET_RESEARCH.md`, `research/V2_POSTMORTEM.md`, `AUDIT_REPORT.md`, and `AGENT_HANDOFF.md`.
