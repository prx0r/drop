# Drop Architecture Review — 2026-09-08

*From the user's review of the system state.*

---

## The Core Insight

> **The pieces required for a genuinely autonomous commerce allocator now exist, but they are not yet connected into one decision system.**

---

## The First Experiment: Nordic-v1

```text
Experimental cluster: NO + FI + SE + DK
Out-of-cluster control: GB
```

**Without any shadow of a doubt** should mean:
> We cannot eliminate commercial uncertainty, but we can eliminate untraceable judgement.

Given the same frozen evidence, two fresh agents should reach the same decision, or we have a missing rule.

---

## The Architecture

```text
                    WORLD
                      │
                      ▼
                   PROBES
                      │
                      ▼
             IMMUTABLE OBSERVATIONS
                      │
       ┌──────────────┼───────────────┐
       ▼              ▼               ▼
 COUNTRY MODEL   SUPPLY GRAPH    MARKET CENSUS
       │              │               │
       └──────────────┼───────────────┘
                      ▼
              COUNTRY SNAPSHOT
                      │
                      ▼
              MECHANISM ENGINE
                      │
                      ▼
              NEED / OPPORTUNITY
                      │
                      ▼
               CANDIDATE UNIVERSE
                      │
                      ▼
              HYPOTHESIS LEDGER
                H1 / H0 / EVI
                      │
                      ▼
                BUILD DECISION
                      │
          ┌───────────┼────────────┐
          ▼           ▼            ▼
        KILL        PROBE         BUILD
                                  │
                                  ▼
                         CAMPAIGN HYPOTHESIS
                                  │
                                  ▼
                              LAUNCHSPEC
                                  │
                                  ▼
                         DEPLOYED — PAUSED
                                  │
                                  ▼
                              PREFLIGHT
                                  │
                                  ▼
                              REAL MONEY
                                  │
                                  ▼
                       REALIZED CPC/CVR/CM2
                                  │
                                  ▼
                          NEW OBSERVATIONS
                                  │
                                  └──────► LOOP
```

---

## Three Structural Fixes

### 1. Country data must flow through Observation system

Every number in the country model needs to resolve backwards to observations.

```text
installed_base = 484,000
    ↓
derived_feature:
    field: cottage_installed_base
    value: 484000
    observation_ids: [O-123]
    derivation: identity
```

### 2. One canonical country schema

`schemas/campaign.py` defines duplicate `CountryProfile`, `CountryObservation`, `CountryExecutionPolicy`.
These must import from `schemas/country.py`, not redefine.

### 3. Add BuildDecision

The missing decisive object:

```text
BuildDecision
─────────────
decision_id
evidence_cutoff
country_snapshot_id
candidate_snapshot_id
hypothesis_id
mechanisms
H1 / H0 / falsifiers
hard_gate_results
P(positive CM2, 30d)
expected_CM2
p10_CM2
maximum_test_loss
uncertainty_by_variable
expected_information_value
test_cost
deployment_cost
reasons_for[]
reasons_against[]
next_best_test
decision: REJECT | RESEARCH | PROBE | BLOCKED | BUILD | LAUNCH
```

---

## The Mechanism Library

| Mechanism | What produces commercial demand |
|-----------|--------------------------------|
| installed-base lifecycle | Existing equipment ages/requires replacement |
| compatibility complexity | Buyer risks purchasing wrong component |
| remote-property problem | Owner needs control/monitoring while absent |
| climatic stress | Freeze/heat/humidity creates failure |
| regulatory transition | Rules force replacement/adaptation |
| consumable replenishment | System repeatedly consumes parts |
| software/platform EOL | System becomes actionable after support change |
| merchant fragmentation | Demand exists but buying experience poor |
| cross-border supply gap | Nearby supply exists but local merchandising doesn't |
| diagnostic gap | Customer knows problem, not correct SKU |
| decision-support deficit | Products exist but choosing correctly difficult |

**Every experiment updates a mechanism belief, not merely a product score.**

---

## The Acceptance Test

Give a completely fresh agent only:

```text
repo + NO/FI/SE/DK/GB frozen snapshots + candidate universe + API credentials + capital limit
```

Ask: **What should we build?**

Expected answer:

```text
BUILD: X

because:
    evidence O-...
    derived feature D-...
    mechanism M-...

against:
    evidence O-...

unknowns: ...
P(CM2 > 0): ...
Expected CM2: ...
p10: ...
EVI: ...
falsifier: ...
next action: ...
LaunchSpec: ...
```

Run again → same answer.
Verifier reconstructs every claim without asking the original agent.

---

## The 15-Step Implementation

1. Make `schemas/country.py` the sole country contract
2. Force every statistic through immutable Observation + explicit derivation
3. Add populated country surfaces (lifecycle events, merchant census, demand signals)
4. Create identical pipelines for NO/FI/SE/DK/GB
5. Add first-class Mechanism and BuildDecision
6. Freeze NORDIC-v1 with snapshot IDs and evidence cutoff
7. Run same candidate-universe generator over all five countries
8. Generate H1/H0/falsifier chains from mechanism evidence
9. Rank unknown-resolution actions by EVI
10. Apply hard commercial gates
11. Let BuildDecision select first genuinely launchable experiment
12. Pass decision into CampaignHypothesis → LaunchSpec → Deployment
13. Run deterministic preflight, then permit spend
14. Turn every real event into new immutable Observations
15. Grade original frozen prediction before looking at result

---

## The Philosophical Correction

**The country should generate the problem before we generate the product.**

Primitive at discovery layer:

```text
country state
× installed system
× lifecycle event
× consumer problem
× merchant failure
× supply topology
```

yields a commercial need.

Products are candidate interventions downstream.

**Transfer mechanisms, not products.**

If Davis Norway works, learn:

> lifecycle/compatibility mechanism strong, Davis supply path bad

Then search for another implementation of that mechanism.

That is how intelligence compounds.
