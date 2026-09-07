# CG Integration Spec — Trusted Judge

## Why CG is the correct judge

Current CG already provides:
- deterministic world reset;
- content-addressed run IDs;
- hard quality gates;
- lexicographic ranking;
- Wilson intervals;
- bootstrap non-inferiority;
- layered/secret suites;
- worldpack distribution.

The campaign system should be a **new worldpack**, not a new optimizer.

## Worldpack 1 — `drop.campaign_gate-v1`

Suggested location in `prx0r/cg`:

```text
cogym_kernel/worlds/drop_campaign/
├── manifest.json
├── world.py
├── evaluator.py
├── contracts.py
├── fixtures/
│   ├── rubric.v1.yaml
│   └── secret_cases.json.enc / runtime-injected
└── tests/
```

### CandidateArtifact config

Do not stuff evidence into the candidate.

```json
{
  "campaign_version_id": "cv_...",
  "campaign_uri": "bundle/campaign.json",
  "evidence_snapshot_id": "es_...",
  "evidence_manifest_uri": "bundle/evidence_manifest.json",
  "rubric_version_id": "rv_..."
}
```

### Deterministic reset

`reset(instance_id, seed)` loads:
- exact campaign version;
- exact evidence bundle;
- exact rubric;
- selected public/secret evaluation case.

No network call.

### Observations to policy

The normal production evaluation can use a deterministic policy that simply asks the evaluator to compute the metrics.

For adversarial campaign agents, an optional policy can be allowed to choose:
- `ABSTAIN`;
- `ROUTE_SERVICE`;
- `ROUTE_B2B`;
- `COMMIT_D2C`.

But the evaluator owns truth.

### Metrics emitted

```text
route_correct
g1_installed_base_pass
g2_lifecycle_pass
g3_compatibility_pass
g4_buyer_autonomy_pass
g5_supply_pass
g6_ownership_gap_pass
g7_reseller_pass
g8_economics_pass
g9_demand_pass
g10_operations_pass
g11_feed_pass
g12_retrieval_whitespace_pass

unknown_gate_count
fatal_fail_count
annual_events_low
contribution_pool_low
required_market_share
our_resolution_lcb
incumbent_resolution_ucb
consumer_selector_lcb
supplier_catalog_coverage
evidence_freshness_pass_rate
evidence_tier_a_b_share
```

### CG gates

Use `QualityGate` for every required boolean:
```python
QualityGate("g1_installed_base_pass", "max", 1.0)
...
```

A missing metric fails closed.

### Objectives after gates

Use CG lexicographic selection.

Recommended:

1. `annual_contribution_pool_low` — max
2. `our_resolution_lcb` — max
3. `required_market_share` — min
4. `manual_presale_rate_ucb` — min
5. `research_debt` — min
6. `launch_cash_cost` — min

Do not create one magic "campaign quality" scalar as the sole authority.

## Suite layers

### DEV
Public deterministic cases for rapid iteration.

### VALIDATION
Fixed cases sampled from evidence but held out from proposer.

### SECRET
Counterexamples the proposer never sees:
- confusing model generations;
- installer-only exceptions;
- negative compatibility;
- incumbent pages that resolve unusually well;
- stale-stock cases;
- low-demand tails.

The eligibility claim requires all fatal gates plus secret suite.

## Worldpack 2 — `drop.evidence_acquisition-v1`

Input:
blocked campaign + unresolved gates + historical research-action outcomes.

Candidate:
research action plan.

Output:
- expected information value;
- actual cost budget;
- reusable evidence coverage.

The actual web/supplier action happens outside deterministic CG.
CG only ranks action plans based on frozen historical priors and declared costs.

## CapabilityClaim

After an eligibility run, compile:
- campaign_version_id;
- evidence_snapshot_id;
- rubric_version_id;
- worldpack_id;
- run_id;
- gate vector;
- hidden-suite version hash.

This becomes the launch authorization artifact.
