# Implementation Plan

## Phase 0 — Freeze doctrine

**Goal:** no further narrative score mutations.

Tasks:
1. Declare `campaign.schema.v2.json` canonical.
2. Declare `rubric.drop-hcc-v2.yaml` canonical.
3. Mark current `CAMPAIGN_MUTATION_SYSTEM.md` superseded for automatic mutation logic.
4. Preserve it as historical design.
5. Add rule: campaign facts are evidence bindings, never mutable genes.

Exit:
- schema validation passes;
- one existing campaign converted.

## Phase 1 — BigQuery evidence spine

Create:
- observations;
- buyer_role_observations;
- supplier_observations;
- demand_events;
- entities;
- compatibility_edges;
- installed_base_observations;
- campaign_versions;
- evidence_snapshots;
- gate_results;
- evaluation_runs;
- mutation_proposals;
- research_actions/outcomes;
- live transactions.

Import:
- current country data;
- current campaign evidence;
- kill ledger;
- OEM successor mappings;
- incumbent observations.

Do **not** convert unknowns to zero.

Exit:
Allaway and UFH can be reconstructed from evidence IDs.

## Phase 2 — Evidence compiler in Drop

New module:

```text
drop/campaign_engine/
├── compiler.py
├── schemas.py
├── bq.py
├── evidence.py
├── hashing.py
└── tests/
```

CLI proposal:

```bash
drop-campaign compile FI-UFH-LEGACY-CONTROLS-0001 \
  --as-of 2026-09-07T21:00:00+07:00 \
  --out runs/ufh/
```

Outputs:
- campaign.json;
- evidence_manifest.json;
- normalized metrics.json;
- bundle hash.

Exit:
same inputs byte-equal.

## Phase 3 — CG campaign judge worldpack

In CG:
- add `drop.campaign_gate-v1`;
- use existing gate/Wilson/bootstrap primitives;
- load compiled bundle;
- emit gate vector;
- public + secret suites;
- content-addressed receipt.

CLI wrapper proposal:

```bash
cg run-drop-campaign runs/ufh/bundle.json
```

or generic current CG worldpack mechanism.

Exit:
- UNKNOWN fails closed;
- tampered evidence changes run ID;
- same bundle gives same receipt;
- hidden cases cannot be read by candidate process.

## Phase 4 — Research-action world

Implement:
`drop.evidence_acquisition-v1`.

Initial historical prior may be simple:
fatality / action cost.

Later learned from `research_action_outcomes`.

Exit:
UFH correctly chooses buyer-role research ahead of ads/supplier economics if buyer role is unresolved.

## Phase 5 — CGE proposer adapter

Do not rewrite CGE core.

Add Drop adapter:

```text
adapters/drop_campaign/
├── genome.py
├── typed_space.py
├── mutations.py
├── feedback_mapper.py
├── proposer.py
└── tests/
```

CGE consumes public CG result JSON.

It emits:
- child hypothesis mutations;
- research actions.

All proposals go to quarantine.

Exit:
CGE cannot mutate evidence paths.

## Phase 6 — Admission / quarantine

For each CGE proposal:
1. JSON-schema validate.
2. Verify mutation only touches allowed paths.
3. Ensure typed values exist in BigQuery graph.
4. Create immutable child campaign version.
5. Compile current evidence.
6. Run CG.

If blocked:
choose research action.

If fatal fail:
kill or space-expand.

## Phase 7 — Experience graph

Use Hydra as derived memory only.

Project:
- campaign lineage;
- failure mechanisms;
- successful mutation families;
- action outcomes;
- cross-country transfers;
- supplier classes.

Hydra is deletable/rebuildable from BigQuery/Git/receipts.

## Phase 8 — Live store / service execution

Only eligibility-claimed campaigns can enter launch.

Write `LaunchManifest`:
- campaign claim;
- SKU scope;
- supplier agreement;
- feed configuration;
- budget;
- stop rules.

Ingest outcomes.

## Phase 9 — Continuous evolution

Scheduled:
- refresh stock;
- refresh platform eligibility;
- refresh incumbent benchmark;
- ingest GitGoblin/OEM changes;
- compile snapshot;
- replay champions.

If gate decays:
campaign moves back to BLOCKED automatically.

---

# Suggested repo changes

## `drop`

Add:
```text
campaign_engine/
campaigns/
rubrics/
bigquery/
worldpack_contracts/
launch_manifests/
```

## `cg`

Add only domain-neutral worldpack:
`drop.campaign_gate-v1`
and later `drop.evidence_acquisition-v1`.

Do not add BigQuery credentials to CG judge.

## `cge`

Add only proposer adapter.

Do not duplicate authoritative rubric code.

## Process isolation

Run:
- `cg-judge` image pinned SHA;
- `cge-proposer` image pinned SHA;
- `drop-orchestrator` with BigQuery/web credentials.

This solves the identical `cogym-kernel` package-name collision.
