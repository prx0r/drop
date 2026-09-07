# HANDOVER.md — The Operational Bible

*This document is the definitive handoff for the next agent.*
*Read this first. Then read AGENTS.md. Then check active/ for current state.*

---

## What This Project Is

**Drop** is an autonomous geographic commerce allocator. It discovers fragmented demand, tests it with nearly zero inventory, and moves capital progressively into whichever businesses demonstrate the highest risk-adjusted economic return.

**Core thesis:** Product × Country × Economics × Supplier = Opportunity

**Endgame:** A continually learning map of where the next marginal unit of research, compute, ad spend and working capital has the highest expected economic return anywhere in the world.

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
│   └── economics.py             ← Cost ledger, decision events, feature snapshots
│
├── pipelines/                   ← Pure transform functions (no I/O)
│   ├── gmail_import.py          ← Raw email → Observations
│   ├── state_machine.py         ← Observations → State transitions
│   ├── hypothesis_ledger.py     ← Observations → Hypothesis updates
│   ├── evi_planner.py           ← Unknowns → Research priorities
│   └── kernel_generator.py      ← Observations → Kernels
│
├── storage/                     ← I/O layer
│   ├── bigquery.py              ← BigQuery read/write (parameterized)
│   └── local.py                 ← Local JSON for fast iteration
│
├── active/                      ← Live registries (read/write)
│   ├── BLOCKERS.md
│   ├── CANDIDATES.md
│   ├── DECISIONS.md
│   ├── PROBLEMS.md
│   ├── SCRATCHPAD.md
│   └── EMAIL_LOG.md
│
├── probes/                      ← Probe system
│   ├── PROBE_REGISTRY.json
│   ├── PROBE_SPECS.md
│   ├── FRESHNESS_TRACKER.md
│   └── PROBE_LOGIC.md
│
├── countries/                   ← Country intelligence
│   ├── NO/country.json
│   ├── FI/country.json
│   ├── intel/
│   └── international/
│
├── bigquery/                    ← BigQuery architecture docs
│   ├── BIGQUERY_MASTERY.md
│   ├── VISIONARY_ARCHITECTURE.md
│   └── economic_ledger_ddl.sql
│
├── data/                        ← Canonical data
│   ├── feeds/                   ← 7 Merchant Center XML feeds
│   ├── hourly_reports/          ← 47+ probe reports (B02-B12)
│   └── hypotheses.json
│
├── output/                      ← Generated reports
│   ├── CANONICAL_STRATEGY.md
│   ├── reviews/
│   └── stale/
│
├── services/                    ← Business logic
│   ├── research/
│   └── scoring/
│
├── packages/                    ← Shared packages
│   ├── schemas/
│   ├── economics/
│   └── scoring/
│
└── legacy/                      ← DO NOT USE (preserved for reference)
    └── README.md
```

---

## The Five Active Probes

| Probe | Schedule | Purpose |
|-------|----------|---------|
| GeoDrop Market Anomaly | :00 | Generate/falsify market hypotheses |
| GeoDrop Channel Economics | :10 | Verify supplier/channel economics |
| GeoDrop Demand Surface | :20 | Verify commercial demand |
| GeoDrop Outcome Trace | :30 | Learn from real outcomes |
| GeoDrop Portfolio Decision | :40 | Make portfolio decisions |

Each probe sends exactly one report to `tradesprior@gmail.com` every hour, including runs where the result is NO MATERIAL INFORMATION GAIN.

---

## The State Machine

```
DISCOVERED → DEMAND_VERIFIED → MERCHANT_GAP_VERIFIED → SUPPLY_PATH_VERIFIED
→ MARGIN_VERIFIED → SEARCH_ECONOMICS_VERIFIED → LAUNCHABLE
→ FREE_TRAFFIC_TEST → PAID_TEST → PROFITABLE / KILLED
```

Every candidate MUST progress through states. Each run must: ADVANCE, KILL, or RESOLVE a field. If none → run was wasted.

---

## The Mechanism Orchard

From probes B05-B12, we have discovered these mechanisms:

| Mechanism | Source | Status |
|-----------|--------|--------|
| OPERATING_COST_OBSOLESCENCE_BEFORE_FAILURE | B09 | Supported |
| SERVICE_ADVISOR_REPLACEMENT_GATEKEEPER | B09 | Strong |
| STACKED_COMPONENT_CLOCKS | B09 | Supported |
| ABSENCE_AMPLIFIES_DAMAGE_SEVERITY | B10 | Strong |
| RISK_PRICER_SUBSIDIZES_PREVENTION | B10-B11 | Replicated |
| DETECTION_TO_INTERVENTION_VALUE_SHIFT | B10 | Supported |
| EVENT_GATED_SUPPLY_MARKET | B12 | New |
| CLAIM_GATEKEEPER_CONTROLS_FUNDED_DEMAND | B12 | New |
| REMOVABLE_CONTROL_BOARD_DELOCALIZES_REPAIR | B06 | Supported |
| WARRANTY_EXPIRY_CHANNEL_FLIP | B06 | Supported |

---

## Current State

**Leader candidate:** TBD (need fresh evaluation)
**Emails sent:** 18 (2 acknowledgments)
**Probes completed:** B02-B12 (11 probes)
**Mechanisms discovered:** 10+
**Countries active:** NO, FI, IE, GB, AU

**What to do now:**
1. Check `active/EMAIL_LOG.md` for new responses
2. Run fresh candidate evaluation through new pipeline
3. Update probe freshness scores
4. Begin B13 (US hail/storm roofing) if B12 results are in

---

## Build Notes

### Gotchas

1. **BigQuery parameterization** — Always use `QueryJobConfig` with `ScalarQueryParameter`. Never interpolate strings.

2. **Temporal evidence contract** — Observations have 5 timestamps: `event_time`, `published_at`, `observed_at`, `available_at`, `ingested_at`. Use `available_at <= decision_time` for point-in-time queries.

3. **Frozen models** — `Observation`, `Kernel`, `ProbeResult` are frozen. `Candidate` and `Hypothesis` are NOT frozen (state machine needs mutation). Always deep-copy before mutating in pipelines.

4. **KILL_TRIGGERS** — Uses `(field, value)` tuples, not just field names. This prevents `decision=ADVANCED` from triggering KILL.

5. **Bayesian v2** — Use `packages/scoring/bayesian_v2.py`, NOT `bayesian.py` (which uses Beta(1,1) — wrong for ecommerce).

6. **Gmail credentials** — Use `agent-vault vault credential get GMAIL_CLIENT_ID --vault oracle`. Never hardcode.

7. **GCP project** — Use `os.environ.get("GCP_PROJECT_ID")`. Never hardcode.

---

## Key Commands

```bash
# Run tests
cd /root/drop && python3 -m pytest tests/ -q

# Run pipeline test
cd /root/drop && python3 -c "from pipelines.gmail_import import GmailImportPipeline; print('OK')"

# Check BigQuery tables
cd /root/drop && python3 -c "
from google.cloud import bigquery
client = bigquery.Client()
for t in client.list_tables('drop'):
    print(f'{t.table_id}: {t.num_rows} rows')
"

# Send email
python3 -c "
import subprocess, json, base64, urllib.request
token = subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GMAIL_REFRESH_TOKEN', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip()
# ... compose and send via Gmail API
"

# Check probe freshness
cat /root/drop/probes/FRESHNESS_TRACKER.md
```

---

## Open Questions

1. **When to start paid tests?** — Need at least 20 clean probe results before autonomous campaign selection.

2. **How to handle supplier responses?** — Currently manual. Need automated email parsing pipeline.

3. **When to implement hierarchical Bayesian priors?** — Need 50+ clean CVR observations across countries/categories.

4. **How to enforce calibration?** — Need reliability diagram CI test before scaling budgets.

5. **When to enable contextual bandit?** — Need 200+ decision events with propensities logged.

---

## The Endgame

> **An autonomous geographic commerce allocator that discovers fragmented demand, tests it with nearly zero inventory, and moves capital progressively into whichever businesses demonstrate the highest risk-adjusted economic return.**

The destination isn't a model saying "Davis Norway = 83/100."

It is a calibrated statement like:

> Given the market state known on September 7, this campaign configuration has a 78% posterior probability of positive 30-day CM2, expected CM2 of NOK 2,140, p10 loss of NOK 610, with 63% of predictive uncertainty attributable to CVR and 24% to supplier margin. The highest-EVI next action is dealer-price verification; expected cost NOK 3.40-equivalent and expected decision value NOK 186.

Then the campaign runs.

Thirty or sixty days later Drop grades that prediction.

After enough such predictions across products and countries, it learns **which observable structures actually predict money**.
