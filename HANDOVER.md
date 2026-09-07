# HANDOVER.md — The Operational Bible

*This document is the definitive handoff for the next agent.*
*Read this first. Then read AGENTS.md. Then check active/ for current state.*

---

## What This Project Is

**Drop** is an autonomous geographic commerce allocator. It discovers fragmented demand, tests it with nearly zero inventory, and moves capital progressively into whichever businesses demonstrate the highest risk-adjusted economic return.

**Core thesis:** Product × Country × Economics × Supplier = Opportunity

**Endgame:** A continually learning map of where the next marginal unit of research, compute, ad spend and working capital has the highest expected economic return anywhere in the world.

---

## Session Narrative (2026-09-08)

### What We Built Today

1. **Schema layer** — 6 Pydantic models (Observation, Hypothesis, Kernel, Candidate, Probe, Economics)
2. **Pipeline layer** — 5 pure transforms (GmailImport, StateMachine, HypothesisLedger, EVIPlanner, KernelGenerator)
3. **Storage layer** — BigQuery + Local JSON with parameterized queries
4. **Campaign compiler** — Research → LaunchSpec
5. **Installed-base pipeline** — Lifecycle hypothesis generation
6. **GoldProbe knowledge graph** — 80 nodes, 239 edges in BigQuery
7. **Country packs** — NO, FI, GB, DE, CH, SE (6 countries, 1,661 rows)
8. **BigQuery MCP** — Agents can query BigQuery directly
9. **Dashboard** — Next.js skeleton (builds, needs npm run dev)
10. **Three thesis reports** — 30,000 words total
11. **30 campaign ideas** — 10 per thesis
12. **Alpha extraction** — 8 opportunities, 12 X accounts, 9 sources

### What We Learned

1. **The pricing calculator was BS** — Assumed margins, not real data
2. **BigQuery parameterization was broken** — Fixed with QueryJobConfig
3. **Old code was never isolated** — Legacy dir was empty
4. **Hypothesis ledger was not Bayesian** — Just counting evidence
5. **GoldProbe reports were drifting** — B20-B25 explored regulatory, not lifecycle

### The Three Businesses

```
1. Agent-Native Commerce
   Products + compatibility + decision engine

2. Agent-Native Services
   Contractors + AI receptionist + bookings

3. Agent-Native Supplier OS
   CRM + invoicing + parts + reviews
```

All three share the same data infrastructure.

### Where My Head Is At

The biggest insight from this session:

> **The contractor AI receptionist is the real moat, not the lead generation.**

If you save a contractor an hour of admin work per job, you create data that makes the platform indispensable. The contractor never leaves the app because the app knows when parts are low, handles their calendar, chases invoices, and builds their reputation.

The flywheel: provider usage → better data → more bookings → more provider demand → more usage.

---

## Repo Layout

```
/root/drop/
├── AGENTS.md                    ← THE CONTROL PLANE (10 binding rules)
├── HANDOVER.md                  ← THIS FILE (operational bible)
├── SPEC.md                      ← Architecture decisions + milestones
│
├── schemas/                     ← Canonical Pydantic models
│   ├── observation.py           ← Atomic fact with temporal evidence contract
│   ├── hypothesis.py            ← Testable claim with falsifier
│   ├── kernel.py                ← Market-intelligence fact
│   ├── candidate.py             ← PRODUCT × COUNTRY cell with state machine
│   ├── probe.py                 ← Probe result and EVI
│   ├── economics.py             ← Cost ledger, decision events, feature snapshots
│   └── country.py               ← Country profile, installed base, merchant census
│
├── pipelines/                   ← Pure transform functions (no I/O)
│   ├── gmail_import.py          ← Raw email → Observations
│   ├── state_machine.py         ← Observations → State transitions
│   ├── hypothesis_ledger.py     ← Observations → Hypothesis updates
│   ├── evi_planner.py           ← Unknowns → Research priorities
│   ├── kernel_generator.py      ← Observations → Kernels
│   ├── campaign_compiler.py     ← Research → LaunchSpec
│   └── installed_base.py        ← Installed base → Hypotheses
│
├── storage/                     ← I/O layer
│   ├── bigquery.py              ← BigQuery read/write (parameterized)
│   └── local.py                 ← Local JSON for fast iteration
│
├── tests/                       ← Test suite
│   ├── test_schemas.py          ← Level 1-2 schema tests
│   ├── test_pipelines.py        ← Level 3 pipeline tests
│   ├── test_hypothesis_ledger.py ← Level 3 hypothesis tests
│   ├── test_storage.py          ← Level 4-5 BigQuery tests
│   └── test_e2e.py              ← Level 6-7 end-to-end tests
│
├── dashboard/                   ← Next.js dashboard
│   ├── app/page.tsx             ← Main dashboard page
│   ├── lib/bigquery.ts          ← BigQuery client
│   └── package.json
│
├── data/                        ← Canonical data
│   ├── hourly_reports/          ← 33 GoldProbe reports
│   ├── opportunities_alpha.json ← 8 opportunities
│   ├── x_accounts_alpha.json    ← 12 X accounts
│   └── information_sources_alpha.json ← 9 sources
│
├── output/                      ← Generated reports
│   ├── THESIS_1_COMMERCE_FINAL.md
│   ├── THESIS_2_SERVICES_FINAL.md
│   ├── THESIS_3_SUPPLIER_OS_FINAL.md
│   ├── greatalpha.md
│   ├── GOLDPROBE_REALIGNMENT.md
│   ├── STATE_OF_BIGQUERY.md
│   └── reviews/
│
├── bigquery/                    ← BigQuery architecture
│   ├── BIGQUERY_MASTERY.md
│   └── economic_ledger_ddl.sql
│
├── probes/                      ← Probe system
│   ├── PROBE_REGISTRY.json
│   └── PROBE_LOGIC.md
│
├── prompts/                     ← Agent instructions
│   ├── GOLD_PROMPT_1_COMMERCE.md
│   ├── GOLD_PROMPT_2_SERVICES.md
│   └── GOLD_PROMPT_3_SUPPLIER_OS.md
│
└── legacy/                      ← Old code (DO NOT USE)
```

---

## BigQuery State

```
53 tables
1,974 rows
80 graph nodes
239 graph edges
42 observations
8 opportunities
12 X accounts
9 information sources
```

---

## The Three Businesses

```
AGENT-NATIVE COMMERCE
    Products + compatibility + decision engine
    ↓
    Uses service graph for recommendations
    ↓

AGENT-NATIVE SERVICES
    EV, heat pumps, solar, HVAC
    ↓
    Uses supplier OS for operations
    ↓

AGENT-NATIVE SUPPLIER OS
    AI receptionist, CRM, booking
    ↓
    Provides data back to commerce
    ↓

    FLYWHEEL
    more usage → better data → more value → more usage
```

---

## The Key Insight

> **The contractor AI receptionist is the real moat, not the lead generation.**

If you save a contractor an hour of admin work per job, you create data that makes the platform indispensable.

The flywheel: provider usage → better data → more bookings → more provider demand → more usage.

---

## What's Next

1. Build contractor directory (scrape OZEV/MCS)
2. Onboard 10 contractors in Nottingham
3. Launch AI chatbot
4. Complete 50 jobs
5. Measure actual economics

---

*Last updated: 2026-09-08*
*Session: Built schemas, pipelines, storage, campaign compiler, 3 thesis reports, 30 campaign ideas*
