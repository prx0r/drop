# GUIDE.md — Operational Guide

**Status:** Active
**Last updated:** 2026-09-08

---

## Quick Start

```bash
# 1. Check current state
cat active/BLOCKERS.md
cat active/CANDIDATES.md
cat active/SCRATCHPAD.md

# 2. Run a pipeline test
cd /root/drop && python3 -c "
from schemas.observation import Observation
from pipelines.gmail_import import GmailImportPipeline
gmail = GmailImportPipeline()
obs = gmail.run('[Test] 2026-09-07 08:00', 'Total sellers: 5', probe_id='test')
print(f'Extracted {len(obs)} observations')
"

# 3. Check probe freshness
cat probes/FRESHNESS_TRACKER.md
```

---

## Core Loop

The Drop system runs a continuous loop:

```
:00 GENERATE / FALSIFY MARKET HYPOTHESES
         ↓
:10 VERIFY CHANNEL + ECONOMICS
         ↓
:20 VERIFY COMMERCIAL DEMAND SURFACE
         ↓
:30 LEARN FROM REAL OUTCOME TRACES
         ↓
:40 PORTFOLIO DECISION / NEXT EXPERIMENT
         ↓
    next hour
```

Each probe sends exactly one report to `tradesprior@gmail.com` on every run, including runs where the correct result is NO MATERIAL INFORMATION GAIN.

---

## The Pipeline Chain

### 1. Gmail Import
**File:** `pipelines/gmail_import.py`
**Input:** Raw email subject + body
**Output:** `List[Observation]`

```python
from pipelines.gmail_import import GmailImportPipeline

gmail = GmailImportPipeline()
observations = gmail.run(
    email_subject="[GeoDrop Market Anomaly Probe] 2026-09-07 08:00 — Ireland wastewater",
    email_body="GoldProbe B05 — Ireland Domestic Wastewater...",
    probe_id="B05-IE-wastewater",
    candidate_id="IE-WASTEWATER-001",
)
```

### 2. State Machine
**File:** `pipelines/state_machine.py`
**Input:** `Candidate`, `List[Observation]`
**Output:** `StateTransitionResult`

```python
from pipelines.state_machine import StateMachinePipeline
from schemas.candidate import Candidate

sm = StateMachinePipeline()
candidate = Candidate(product_family="Testo 550s", country_code="NO")
result = sm.run(candidate, observations)
if result.transitioned:
    print(f"{result.from_state} → {result.to_state}")
```

### 3. Hypothesis Ledger
**File:** `pipelines/hypothesis_ledger.py`
**Input:** `List[Hypothesis]`, `List[Observation]`
**Output:** `List[HypothesisUpdate]`

```python
from pipelines.hypothesis_ledger import HypothesisLedgerPipeline
from schemas.hypothesis import Hypothesis

hl = HypothesisLedgerPipeline()
hypothesis = Hypothesis(
    claim="Norway has sparse specialist Testo 550s retail",
    null_hypothesis="Hidden B2B distribution",
    falsifier=">=3 competent merchants",
)
updates = hl.run([hypothesis], observations)
```

### 4. EVI Planner
**File:** `pipelines/evi_planner.py`
**Input:** `List[UnknownField]`, `Candidate`
**Output:** `List[ResearchEVI]` (ranked by EVI)

```python
from pipelines.evi_planner import EVIPlannerPipeline
from schemas.observation import UnknownField

evi = EVIPlannerPipeline()
unknowns = [
    UnknownField(
        candidate_id="NO-TESTO-001",
        field="dealer_price",
        why_unknown="Need exact dealer price",
        decision_dependency="Cannot calculate margin",
        resolution_path="Email supplier",
        probability_of_resolve=0.7,
        decision_impact=0.9,
        candidate_value=0.6,
        research_cost=0.5,
    ),
]
rankings = evi.run(unknowns, candidate)
print(f"Best next action: {rankings[0].recommended_action}")
```

### 5. Kernel Generator
**File:** `pipelines/kernel_generator.py`
**Input:** `List[Observation]`, `List[Hypothesis]`, `ProbeResult`
**Output:** `List[Kernel]`

```python
from pipelines.kernel_generator import KernelGeneratorPipeline

kg = KernelGeneratorPipeline()
kernels = kg.run(observations, [hypothesis])
for kernel in kernels:
    print(f"{kernel.kernel_type.value}: {kernel.belief_delta.value}")
```

---

## Storage Layer

### Local JSON (fast iteration)
```python
from storage.local import LocalStorage

storage = LocalStorage()
storage.write_observation(observation)
observations = storage.read_observations(candidate_id="NO-TESTO-001")
```

### BigQuery (production)
```python
from storage.bigquery import BigQueryStorage

storage = BigQueryStorage()
storage.write_candidate(candidate)
candidates = storage.read_candidates(state="DEMAND_VERIFIED")
```

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

## Candidate State Machine

```
DISCOVERED → DEMAND_VERIFIED → MERCHANT_GAP_VERIFIED → SUPPLY_PATH_VERIFIED
→ MARGIN_VERIFIED → SEARCH_ECONOMICS_VERIFIED → LAUNCHABLE
→ FREE_TRAFFIC_TEST → PAID_TEST → PROFITABLE / KILLED
```

Valid transitions are defined in `schemas/candidate.py`:
- `DISCOVERED` → `DEMAND_VERIFIED`, `KILLED`, `HUMAN_ACTION_REQUIRED`
- `DEMAND_VERIFIED` → `MERCHANT_GAP_VERIFIED`, `KILLED`, `HUMAN_ACTION_REQUIRED`
- `MERCHANT_GAP_VERIFIED` → `SUPPLY_PATH_VERIFIED`, `KILLED`, `HUMAN_ACTION_REQUIRED`
- `SUPPLY_PATH_VERIFIED` → `MARGIN_VERIFIED`, `KILLED`, `HUMAN_ACTION_REQUIRED`
- `MARGIN_VERIFIED` → `SEARCH_ECONOMICS_VERIFIED`, `KILLED`, `HUMAN_ACTION_REQUIRED`
- `SEARCH_ECONOMICS_VERIFIED` → `LAUNCHABLE`, `KILLED`, `HUMAN_ACTION_REQUIRED`
- `LAUNCHABLE` → `FREE_TRAFFIC_TEST`, `KILLED`, `HUMAN_ACTION_REQUIRED`
- `FREE_TRAFFIC_TEST` → `PAID_TEST`, `KILLED`, `HUMAN_ACTION_REQUIRED`
- `PAID_TEST` → `PROFITABLE`, `KILLED`, `HUMAN_ACTION_REQUIRED`
- `PROFITABLE` → `KILLED`
- `KILLED` → (terminal)
- `HUMAN_ACTION_REQUIRED` → any previous state
- `FROZEN` → any previous state

---

## Economic Ledger

### CM0-CM3 Contribution Levels

```
CM0 = Product contribution (pre-acquisition)
    = net_revenue - COGS - shipping - duty - payments - refunds - returns

CM1 = Acquisition contribution (post-ads)
    = CM0 - paid_acquisition - affiliate_commissions

CM2 = Automated operating contribution (post-AI/API costs)
    = CM1 - ai_tokens - scraping_api - image_generation - agent_compute

CM3 = Fully loaded contribution (post-everything)
    = CM2 - domain_costs - software_costs - human_intervention - samples
```

**Primary machine optimization reward = CM2.**

### Feature Snapshot

Every decision references a point-in-time feature snapshot:
- Country features (GDP, cross-border rate, mobile payment)
- Installed base features (size, growth, replacement pressure)
- Search/demand features (volume, growth, CPC)
- Competition features (seller count, quality gap)
- Supply features (margin, delivery days, risk)
- Economics features (AOV, gross margin, source-target gap)

---

## Where Things Are

When unsure, use these search patterns:

```bash
# Find a concept
grep -rn "concept" schemas/ pipelines/ storage/ | head

# Find a file
find . -name "*.py" -o -name "*.md" | grep -i concept

# Check what imports a module
grep -rn "from schemas.observation import" pipelines/

# Check what uses a field
grep -rn "field_name" schemas/ pipelines/
```
