# SPEC.md — Architecture Decisions + Milestones

**Status:** Active (v2.0)
**Last updated:** 2026-09-08

---

## Architecture Decision Records

### ADR-001: BigQuery as Economic Truth Store

**Decision:** BigQuery is the canonical source of truth for all economic data.

**Rationale:**
- Google Ads, GA4, Merchant Center all export to BigQuery natively
- Supports parameterized queries for safety
- Handles time-series data well (partitioning, clustering)
- Supports ML models directly (BigQuery ML)

**Consequences:**
- Local JSON is for fast iteration only, never for production decisions
- Graph is a derived representation, not the primary store
- All features must be freezable at decision time

### ADR-002: Schemas as Single Source of Truth

**Decision:** All data structures live in `schemas/` as Pydantic models.

**Rationale:**
- Type safety prevents runtime errors
- Frozen models prevent accidental mutation
- Clear input/output contracts for pipelines
- One schema per entity (no duplicates)

**Consequences:**
- Never use raw dicts for inter-pipeline communication
- Never create ad-hoc data structures
- Schema changes require updating all dependent pipelines

### ADR-003: Pipelines as Pure Functions

**Decision:** Pipelines are `Input → Transform → Output` with no I/O.

**Rationale:**
- Makes pipelines testable (no mocking needed)
- Makes pipelines composable (output of one is input to another)
- Makes pipelines auditable (every transformation is traceable)
- Separates concerns (logic vs I/O)

**Consequences:**
- I/O happens in `storage/` layer only
- Never import `google.cloud.bigquery` in pipeline files
- Never read files directly in pipeline logic

### ADR-004: Temporal Evidence Contract

**Decision:** Observations have 5 timestamps: `event_time`, `published_at`, `observed_at`, `available_at`, `ingested_at`.

**Rationale:**
- Prevents data leakage (can't use future data for past decisions)
- Enables point-in-time queries (`WHERE available_at <= decision_time`)
- Supports backtesting with strict temporal holdout
- Handles publication lag (SSB publishes data months after collection)

**Consequences:**
- Every observation must have at least `observed_at` and `ingested_at`
- Models must be trained on feature snapshots, not live data
- Backtests must use `available_at`, not `observed_at`

### ADR-005: CM0-CM3 Contribution Levels

**Decision:** Four contribution levels prevent optimizing for headline revenue.

**Rationale:**
- CM0 = Product contribution (pre-acquisition)
- CM1 = Acquisition contribution (post-ads)
- CM2 = Automated operating contribution (post-AI/API costs)
- CM3 = Fully loaded contribution (post-everything)

**Consequences:**
- Primary machine optimization reward = CM2
- Information gain decides whether to buy information, not whether to optimize
- Every cost event must be categorized into CM0-CM3

### ADR-006: Feature Snapshots Prevent Leakage

**Decision:** `FeatureSnapshot` captures point-in-time state before every decision.

**Rationale:**
- Models must only train on data available at decision time
- Prevents "looking into the future" during backtesting
- Enables reproducible predictions (same features + model = same prediction)
- Critical for offline policy evaluation

**Consequences:**
- Every `DecisionEvent` must reference a `feature_snapshot_id`
- Feature snapshots are frozen (immutable after creation)
- Models must be trained on feature snapshots, not live data

### ADR-007: Action Propensities for Offline Policy Evaluation

**Decision:** Every policy action logs the probability under which it was selected.

**Rationale:**
- Agent preferentially tests things it thinks will succeed
- Without propensities, comparing policies offline is biased
- Inverse propensity scoring enables unbiased evaluation
- Critical for contextual bandits with budget constraints

**Consequences:**
- Every `DecisionEvent` must have `action_probability`
- Every `PolicyAction` must log `chosen_action_probability`
- New policies can be evaluated offline using historical data

### ADR-008: Outcome Maturity Windows

**Decision:** Economic outcomes have 5 maturity windows: 1d, 7d, 30d, 60d, 90d.

**Rationale:**
- A sale today isn't economically mature today
- Returns arrive at day 17, warranty claims at day 41
- Training against immature labels creates biased models
- Google Ads exposes conversion lag buckets

**Consequences:**
- Train against mature labels (30d+), not day-2 profit
- Use estimated reserves initially, true-up later
- Never compare campaigns at different maturity levels

### ADR-009: Country Packs as Immutable Memory

**Decision:** Country packs are canonical research/evidence packages, not the model itself.

**Rationale:**
- Human-readable and auditable
- Version-controlled and reproducible
- Separate from high-frequency warehouse data
- Enable transfer learning across countries

**Consequences:**
- Country packs stay small (evidence, not events)
- High-frequency data lives in BigQuery
- Country packs get `country_state_manifest.json` pointing to warehouse state

### ADR-010: Probes Generate Kernels, Not Reports

**Decision:** Probe output is market-intelligence kernels, not prose reports.

**Rationale:**
- Kernels are structured and queryable
- Kernels can be chained (one kernel's output feeds another)
- Kernels are immutable (frozen after creation)
- Kernels enable machine learning over time

**Consequences:**
- Every probe run must produce at least one kernel
- Kernels have type, belief delta, generalizable rule
- Kernels are stored in BigQuery and queried across probes

---

## Milestones

### M0: Foundation (Complete)
- [x] Schemas defined (observation, hypothesis, kernel, candidate, probe, economics)
- [x] Pipelines implemented (gmail_import, state_machine, hypothesis_ledger, evi_planner, kernel_generator)
- [x] Storage layer working (bigquery + local)
- [x] Temporal evidence contract added
- [x] BigQuery parameterization fixed
- [x] Legacy code isolated

### M1: Probe System (Complete)
- [x] 5 probes running hourly
- [x] B02-B12 reports imported (11 probes)
- [x] Mechanisms discovered (10+)
- [x] Probe freshness tracking
- [x] Gmail integration working

### M2: Economic Ledger (In Progress)
- [x] CM0-CM3 schema defined
- [x] Decision event schema defined
- [x] Feature snapshot schema defined
- [x] Treatment assignment schema defined
- [ ] BigQuery tables created
- [ ] Ingestion pipelines wired

### M3: Statistical Foundation (Planned)
- [ ] Bayesian v2 genuinely hierarchical (not static priors)
- [ ] Unified scorer repaired (clicks/orders, positive conversions)
- [ ] Funnel classifier fixed (stage-specific posteriors)
- [ ] Calibration tests passing

### M4: Google Integration (Planned)
- [ ] Google Ads → BigQuery daily transfer
- [ ] GA4 → BigQuery raw events
- [ ] Merchant Center → BigQuery performance
- [ ] Full query/device/geo/auction granularity

### M5: Policy Learning (Planned)
- [ ] 200+ decision events with propensities
- [ ] Thompson sampling for campaign selection
- [ ] Offline policy evaluation working
- [ ] Budget-constrained exploration

### M6: Autonomous Portfolio (Future)
- [ ] Calibrated P(profitable) for every candidate
- [ ] EVI-driven research allocation
- [ ] Contextual bandit for action selection
- [ ] Continuous learning from outcomes

---

## Naming Conventions

### Entity IDs
| Pattern | Example | Purpose |
|---------|---------|---------|
| `O-{hex12}` | `O-1ffe3506ecc5` | Observation |
| `H-{hex12}` | `H-9b4bdb51ddc2` | Hypothesis |
| `K-{hex12}` | `K-0d50bea209f6` | Kernel |
| `C-{hex12}` | `C-79f7afe4e84f` | Candidate |
| `RUN-{hex12}` | `RUN-c2faaf3a5585` | Probe run |
| `DE-{hex12}` | `DE-27d50c88ca30` | Decision event |
| `FS-{hex12}` | `FS-bbb204acc63d` | Feature snapshot |
| `CL-{hex12}` | `CL-abc123def456` | Cost ledger |
| `EO-{hex12}` | `EO-xyz789abc012` | Economic outcome |
| `PA-{hex12}` | `PA-def456ghi789` | Policy action |
| `TA-{hex12}` | `TA-ghi012jkl345` | Treatment assignment |

### Field Names
- `snake_case` for all fields
- Prefix with entity type: `candidate_id`, `hypothesis_id`, `probe_id`
- Use `_at` for timestamps: `created_at`, `observed_at`, `available_at`
- Use `_pct` for percentages: `gross_margin_pct`, `return_rate_pct`
- Use `_count` for counts: `seller_count`, `good_seller_count`

### File Names
- `snake_case.py` for Python modules
- `UPPER-CASE.md` for documentation
- `lowercase.json` for data files
- `B{num}_{COUNTRY}_{topic}.md` for probe reports

### Table Names
- `dim_*` for dimension tables
- `fact_*` for fact tables
- `graph_*` for graph tables
- `ml_*` for ML tables

---

## Schema Enforcement

### Pydantic Validation
All schemas use Pydantic v2 with strict validation:
- Required fields are enforced
- Type coercion is disabled (strict mode)
- Optional fields have defaults
- Frozen models prevent mutation where appropriate

### BigQuery DDL
All table definitions in `bigquery/economic_ledger_ddl.sql`:
- Partitioned by date for performance
- Clustered by common query fields
- Description comments on every table

### CI Validation (Planned)
- Pydantic schema validation on import
- BigQuery DDL syntax check
- Pipeline input/output type checking
- No secrets in committed files

---

## The Endgame

> **A continually learning map of where the next marginal unit of research, compute, ad spend and working capital has the highest expected economic return anywhere in the world.**

Progression:
```
DATA → STATISTICS → PREDICTION → CAUSAL EXPERIMENTS → POLICY LEARNING → AUTONOMOUS CAPITAL ALLOCATION
```

Current stage: **DATA** (accumulating probe results, building economic ledger)
