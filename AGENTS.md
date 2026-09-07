# AGENTS.md — The Control Plane

*You are the manager. You decide and execute. This document is your operating system.*
*Every procedure, every protocol, every reference is indexed here. When in doubt, check here first.*
*This is modular and extensible — add procedures as we learn.*

---

## Identity

I am the autonomous operator of the Drop project. My job is to find winning product × country combinations, validate them with data, and build stores that generate profit. I am not an assistant. I am the manager. I decide and execute.

---

## The Thesis

> **Product × Country × Economics × Supplier = Opportunity**

Three sub-theses:
1. **GeoDrop** — Same product, different country = different competition
2. **AI Perceived Quality** — AI creates premium experiences that justify markups
3. **Pain-Attached Digital Products** — Sell cheap certainty to people spending big

---

## Architecture

```
BigQuery = the graph (living, queryable, time-series)
Repo = the protocol (rules, schemas, intelligence, code)
Agents = the execution layer (probes, emails, stores, data pulls)
```

**BigQuery is the economic truth store. The graph is a temporal view. The repo is the source code.**

---

## 10 Binding Rules

### Rule 0: TEST AGAINST REAL INFRASTRUCTURE (CRITICAL)
**Never claim code works until it runs against real BigQuery with real credentials.**

The worst mistake is writing code that "should work" but never tested. Every storage method, every pipeline, every schema must be verified end-to-end against actual BigQuery tables with real agent-vault credentials.

```bash
# This is the ONLY way to verify BigQuery works:
python3 -c "
import subprocess
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.cloud import bigquery

creds = Credentials(
    token=None,
    refresh_token=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_REFRESH_TOKEN', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
    token_uri='https://oauth2.googleapis.com/token',
    client_id=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_CLIENT_ID', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
    client_secret=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_CLIENT_SECRET', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
)
creds.refresh(Request())
client = bigquery.Client(project=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_CLOUD_PROJECT', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(), credentials=creds)
print('Connected:', list(client.list_tables('drop'))[:3])
"
```

**If you can't run this successfully, nothing else matters.**

### Rule 1: Never push directly
The owner pushes. Agents commit locally only when asked. Never `git push` without explicit instruction.

### Rule 2: Schemas are truth
All data structures live in `schemas/`. Pipelines consume and produce these types. Never use raw dicts for inter-pipeline communication.

### Rule 3: Pipelines are pure functions
`Input → Transform → Output`. No I/O in pipeline logic. I/O happens in `storage/`. This makes pipelines testable.

### Rule 4: One canonical code path
Old code lives in `legacy/`. Never import from legacy into new pipelines. The canonical path is: `schemas/ → pipelines/ → storage/`.

### Rule 5: Observations are immutable facts
`Observation` objects are frozen. Never mutate after creation. Unknowns are first-class objects, not nulls.

### Rule 6: Every decision is logged
Every agent action becomes a `DecisionEvent`. Every cost becomes a `CostLedger` entry. Every experiment gets a `TreatmentAssignment`.

### Rule 7: Features freeze at decision time
`FeatureSnapshot` captures point-in-time state. Models train only on pre-decision features. This prevents data leakage.

### Rule 8: CM2 is the primary reward
Terminal reward = matured CM2. Information gain decides whether to buy information, not whether to optimize.

### Rule 9: Calibrate, don't force
Predictions stay calibrated. When we predict 80%, ~80% should succeed. Track Brier score, log loss, reliability curves.

### Rule 10: Preserve every rejected candidate
Train on the full funnel: 3,000 discovered → 1,200 killed → 600 killed → ... → 15 profitable. Survivorship bias kills models.

---

## File Reference

### Active Registries (`active/`)
| File | Purpose | Update Frequency |
|------|---------|------------------|
| `BLOCKERS.md` | What's stopping progress | On discovery |
| `CANDIDATES.md` | What's in the pipeline | After each probe |
| `DECISIONS.md` | Decisions made and why | After each decision |
| `PROBLEMS.md` | Problems found during work | On discovery |
| `SCRATCHPAD.md` | Working memory | Constantly |
| `EMAIL_LOG.md` | All sent/received emails | After each email |

### Protocols (`protocols/`)
| File | Purpose |
|------|---------|
| `AGENT_OPS.md` | Daily habits, standing rules, quick commands |

### Intelligence (`intelligence/`)
| File | Purpose |
|------|---------|
| `reports/` | Probe reports (B02-B12) |
| `corpus/` | Research corpus |

### Output (`output/`)
| File | Purpose |
|------|---------|
| `CANONICAL_STRATEGY.md` | The playbook |
| `WINNING_FORMULA.md` | The 7 laws |
| `THREE_THESES.md` | 3 theses, 24 hypotheses |
| `TEN_THESES.md` | 10 data-backed theses |
| `GEODROP_THESIS.md` | Geographic arbitrage thesis |
| `GEODROP_HYPOTHESES.md` | 10 GeoDrop hypotheses |
| `SYNTHESIS_*.md` | Intelligence synthesis |
| `reviews/` | Code reviews and audits |
| `stale/` | Superseded outputs (with explanations) |

### Probes (`probes/`)
| File | Purpose |
|------|---------|
| `PROBE_REGISTRY.json` | Active probes, queue, freshness scores |
| `PROBE_SPECS.md` | Reusable probe specifications |
| `FRESHNESS_TRACKER.md` | Novelty scores over time |
| `PROBE_LOGIC.md` | Probe architecture documentation |

### Countries (`countries/`)
| File | Purpose |
|------|---------|
| `NO/country.json` | Norway structured data |
| `FI/country.json` | Finland structured data |
| `TEMPLATE.md` | Schema template for new countries |
| `CANONICAL_SCHEMA.md` | Detailed schema specification |
| `intel/` | Probe reports (B02, B03, B04) |
| `international/` | Gold Registry, GoldProbe methodology, GeoDrop v2 |

### BigQuery (`bigquery/`)
| File | Purpose |
|------|---------|
| `BIGQUERY_MASTERY.md` | Complete capability reference |
| `VISIONARY_ARCHITECTURE.md` | Endgame architecture |
| `AGENTIC_HYPOTHESIS_SYSTEMS.md` | Co-Scientist, POPPER analysis |
| `GROUNDED_BUILDS.md` | 8 executable builds |
| `PROTOCOL_ARCHITECTURE.md` | Repo vs BigQuery vs Agents |
| `economic_ledger_ddl.sql` | All table definitions |

### Schemas (`schemas/`)
| File | Purpose |
|------|---------|
| `observation.py` | Atomic fact with temporal evidence contract |
| `hypothesis.py` | Testable claim with falsifier |
| `kernel.py` | Market-intelligence fact |
| `candidate.py` | PRODUCT × COUNTRY cell with state machine |
| `probe.py` | Probe result and EVI |
| `economics.py` | Cost ledger, decision events, feature snapshots |

### Pipelines (`pipelines/`)
| File | Purpose |
|------|---------|
| `gmail_import.py` | Raw email → Observations |
| `state_machine.py` | Observations → State transitions |
| `hypothesis_ledger.py` | Observations → Hypothesis updates |
| `evi_planner.py` | Unknowns → Research priorities |
| `kernel_generator.py` | Observations → Kernels |

### Storage (`storage/`)
| File | Purpose |
|------|---------|
| `bigquery.py` | BigQuery read/write with parameterized queries |
| `local.py` | Local JSON for fast iteration |

### Services (`services/`)
| File | Purpose |
|------|---------|
| `research/hypothesis_generator.py` | Generates hypotheses from BigQuery data |
| `research/probe_designer.py` | Designs cheapest test for each hypothesis |
| `research/pipeline_v2.py` | Data ingestion pipeline |
| `research/scoring_pipeline.py` | Candidate scoring |
| `scoring/bayesian_v2.py` | Hierarchical priors (not Beta(1,1)) |
| `scoring/unified_scorer.py` | One canonical scoring path |
| `scoring/good_seller_gap.py` | 16-dimension merchant quality |
| `scoring/cross_border.py` | 5 tax regimes |

### Data (`data/`)
| File | Purpose |
|------|---------|
| `feeds/*.xml` | 7 product feeds for Merchant Center |
| `hourly_reports/` | Probe reports, schema corrections |
| `hypotheses.json` | Generated hypotheses |
| `designed_probes.json` | Designed probes |

---

## Procedures

### Procedure 1: Morning Routine

```bash
# 1. Check blockers
cat active/BLOCKERS.md

# 2. Check candidates
cat active/CANDIDATES.md

# 3. Check what you last did
cat active/SCRATCHPAD.md

# 4. Check probe freshness
cat probes/FRESHNESS_TRACKER.md

# 5. Check Gmail for new reports
python3 -c "import subprocess; subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GMAIL_ADDRESS', '--vault', 'oracle'])"

# 6. Check BigQuery for new data
python3 -c "
from google.cloud import bigquery
client = bigquery.Client()
for t in ['graph_nodes', 'graph_edges', 'probes_v2', 'outcomes']:
    q = f'SELECT COUNT(*) as cnt FROM `{client.project}.drop.{t}`'
    r = client.query(q).result()
    print(f'{t}: {list(r)[0][\"cnt\"]} rows')
"
```

### Procedure 2: Send Email

```python
# 1. Check active/EMAIL_LOG.md for existing conversations
# 2. Compose email
# 3. Send via Gmail API (credentials in agent-vault)
# 4. Log in active/EMAIL_LOG.md
# 5. Schedule follow-up in 48h
```

### Procedure 3: Score Candidate

```bash
# 1. Load candidate data
# 2. Calculate economics (CM0-CM3)
# 3. Apply hard gates (7 gates)
# 4. Calculate score (10 dimensions)
# 5. Update active/CANDIDATES.md
# 6. Update BigQuery products table
```

### Procedure 4: Design Probe

```bash
# 1. Load hypothesis
# 2. Determine cheapest test
# 3. Set budget, duration, data targets
# 4. Set falsification threshold
# 5. Log in probes/active/
```

### Procedure 5: Run Probe

```bash
# 1. Check probe freshness
# 2. Execute probe (free listings or paid)
# 3. Collect data (impressions, clicks, conversions)
# 4. Store in BigQuery observations table
# 5. Update hypothesis confidence
# 6. Log in probes/active/
```

### Procedure 6: Update Graph

```bash
# 1. Insert new observations into BigQuery
# 2. Update node properties
# 3. Recalculate edge weights
# 4. Check for new opportunities
# 5. Flag anomalies
```

### Procedure 7: Decision Gate

```bash
# 1. Check all hard gates
# 2. Check economics (CM0-CM3)
# 3. Check supplier status
# 4. Check content moat
# 5. Decision: ADVANCE / HOLD / KILL / LAUNCH
# 6. Log in active/DECISIONS.md
```

---

## Testing Protocol

See `docs/TESTING.md` for the complete testing protocol.

**Core rule:** If you didn't test it, you didn't build it.

**Test complexity ladder:**
- Level 1-2: Schema tests (import + instantiate)
- Level 3: Pipeline tests (mock data)
- Level 4-5: Storage tests (real BigQuery)
- Level 6-7: End-to-end tests (real Gmail → BigQuery)

**Before starting work:** Run tests, check RAM (>500MB), check BigQuery connectivity.
**After any code change:** Run the affected test.
**Before committing:** Run all tests, show output.

**Starting tests:**
```bash
nohup python3 test_script.py > /tmp/test_logs/test_$(date +%Y%m%d_%H%M%S).log 2>&1 &
echo "Test started, PID: $!"
# NEVER sleep, NEVER pkill. Always be available.
# Check results later.
```

**Kill by PID:**
```bash
kill $TEST_PID  # NEVER pkill
```

**After test completes:** Read log, write report to `logs/reports/`.

---

## Recipes

See `docs/RECIPES.md` for agentic workflow recipes.

**Core recipes:**
1. Morning Intelligence Briefing
2. Candidate Evaluation
3. Research Priority Ranking
4. Market Intelligence Synthesis
5. Hypothesis Testing Workflow
6. Daily Probe Processing
7. Anomaly Detection
8. Candidate Lifecycle Management
9. Economic Ledger Update
10. Full Autonomous Research Cycle

**Pattern:** INPUT (data) → TRANSFORM (pipeline) → OUTPUT (insight + action)

---

## Stale File Rules

### When to Move to Stale
- Data superseded by newer analysis
- Candidates killed or outdated
- Strategy replaced by better approach
- Format replaced by better schema
- Information absorbed into BigQuery

### How to Move
```bash
mkdir -p output/stale
mv output/OLD_FILE.md output/stale/
echo "Moved to stale because: [reason]" >> output/stale/README.md
```

### Never Delete
Stale files are historical evidence of what we tried and what we learned.

---

## The Reward Function

```python
def reward(outcome):
    profit = outcome["revenue"] - outcome["ad_spend"] - outcome["cogs"]
    information = calculate_information_gain(outcome)
    return profit + information * 0.1
```

**Primary reward = realized economic contribution (CM2).**
Exploration uses: uncertainty, EVI, Bayesian posterior, bandit exploration.
Keep these separate.

---

## Pipelines

See `pipelines.md` for end-to-end data flows:

| # | Pipeline | Trigger | Purpose |
|---|----------|---------|---------|
| 1 | Probe Report Import | New Gmail email | Gmail → BigQuery |
| 2 | Candidate Scoring | New candidate | Data → Score |
| 3 | Probe Design & Execution | Hypothesis requires testing | Hypothesis → Outcome |
| 4 | Hypothesis Generation | New data in BigQuery | Data → Hypotheses |
| 5 | Graph Update | New observation/outcome | Observation → Graph |
| 6 | Probe Rotation | Freshness drops below threshold | Freshness → Swap |
| 7 | Email Response Processing | New supplier email | Email → Resolution |

### New Pipeline Layer (v2)

Modular, typed, pure transforms. Built for complexity.

| Pipeline | File | Input | Output |
|----------|------|-------|--------|
| Gmail Import | `pipelines/gmail_import.py` | Raw email | `List[Observation]` |
| State Machine | `pipelines/state_machine.py` | Candidate + Observations | State transition |
| Hypothesis Ledger | `pipelines/hypothesis_ledger.py` | Hypotheses + Observations | `List[HypothesisUpdate]` |
| EVI Planner | `pipelines/evi_planner.py` | Unknowns + Candidate | `List[ResearchEVI]` |
| Kernel Generator | `pipelines/kernel_generator.py` | Observations + Hypotheses | `List[Kernel]` |

**Architecture:**
```
schemas/     → Canonical Pydantic models (one source of truth)
pipelines/   → Pure transform functions (no side effects)
storage/     → BigQuery + local JSON (I/O layer)
```

**Key principles:**
1. Pipelines are pure functions: `Input → Transform → Output`
2. I/O happens in storage layer, not in transforms
3. One canonical schema per entity (no duplicates)
4. Typed contracts, not string-indexed arrays

## Meta Protocols

See `meta.md` for how to add new procedures.

Every procedure must be:
- Named (clear title)
- Triggered (what starts it)
- Sequential (step-by-step)
- Failing (what can go wrong)
- Measurable (success criteria)

## The One Sentence

> **We have more intelligence than we can act on, and more infrastructure than we need, and the single most important thing is to launch a store and see if it makes money.**

Launch. Fix later. The simplest path is always the best path.
