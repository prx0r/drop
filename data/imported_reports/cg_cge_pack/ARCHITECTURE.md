# Architecture — Four Planes, Two Worlds, One Judge

## 1. Four planes

### A. Evidence plane — BigQuery

This answers **what is currently known?**

It must contain facts, observations, measurements and provenance, not persuasive narrative.

Examples:
- 250,000 Allaway installations — OEM observation.
- part 1141681 public stock = 277 — retailer observation at timestamp X.
- buyer-role sample: 4 of 30 consumers selected exact SKU — behavioral observation.
- supplier email: dealer discount 28%, MOQ €0 — contractual observation.
- incumbent answered 24/30 benchmark prompts correctly — benchmark observation.

### B. Hypothesis plane — Drop

This answers **what exactly are we betting on?**

A campaign is a compact hypothesis:

```text
country
× track
× OEM ecosystem
× installed asset
× generation
× component
× lifecycle trigger
× buyer
× supplier route
× distribution route
```

It points to evidence IDs. It does not restate unsupported facts.

### C. Judge plane — CG

This answers **does the current hypothesis pass the current rubric under the frozen evidence state?**

CG must be:
- deterministic;
- pinned to a rubric version;
- pinned to an evidence snapshot;
- proposer-blind to secret tests;
- fail-closed on missing evidence.

### D. Search plane — CGE

This answers **what should we try next?**

CGE may:
- mutate the hypothesis;
- branch campaigns;
- recombine winning mechanisms;
- propose evidence-acquisition actions;
- maintain diversity.

It never gets authority over gate truth.

---

# 2. Two worlds

A major architectural improvement over the current mutation draft is to avoid asking one optimizer to both "fix the campaign" and "prove the campaign".

## World A — `drop.campaign_gate-v1`

Candidate:
`CampaignHypothesis`

Inputs:
- canonical campaign JSON;
- evidence-bundle manifest;
- rubric version;
- deterministic benchmark suite.

Outputs:
- route;
- G1..Gn tri-state;
- hard-gate aggregate;
- statistics;
- lower bounds;
- incumbent benchmark;
- economics bounds;
- launch eligibility;
- ordered unresolved gates.

This world does **no live browsing and no BigQuery writes**.

It consumes a frozen bundle.

### CG gate semantics

For boolean gate `Gx`:
- `PASS` → metric 1
- `FAIL` → metric 0
- `UNKNOWN` → metric absent / explicit unknown; gate fails closed

CG's existing `QualityGate(metric, mode="max", value=1.0)` works naturally:
missing metric fails; 0 fails; 1 passes.

Do not collapse FAIL and UNKNOWN in the result artifact even if both block eligibility.

## World B — `drop.evidence_acquisition-v1`

Candidate:
`ResearchActionPlan`

Purpose:
For BLOCKED campaigns, choose which test to run next.

Examples:
- sample 30 buyer journeys;
- contact supplier;
- scrape 100 incumbent PDPs;
- obtain distributor price list;
- resolve 50 compatibility edges;
- query exact-part demand;
- benchmark 30 prompts.

Metrics:
- expected gate kill power;
- expected gate resolution probability;
- action cash cost;
- human time;
- latency;
- source quality;
- reusable information value.

Quality gates:
- legal;
- within research budget;
- source collection is auditable;
- does not fabricate hidden values.

Primary objective is **expected value of information**, not campaign score.

---

# 3. Why this is better than "mutate until 160/200"

The current Drop mutation draft creates a Goodhart path:
- score field is unknown;
- mutator searches data;
- proposed mutation becomes "verified";
- score rises.

Instead:

```text
UNKNOWN G7 reseller path
   ↓
CGE proposes:
CONTACT_SUPPLIER supplier_id=ONNINEN
   ↓
Action executes
   ↓
Email / terms observed
   ↓
Verifier creates EV-123
   ↓
Evidence snapshot v18
   ↓
CG reruns same campaign
   ↓
G7 PASS or FAIL
```

The hypothesis does not get to edit the answer.

---

# 4. Three immutable identifiers

Every authoritative result must bind:

### `campaign_version_id`
Hash of canonical hypothesis JSON excluding volatile timestamps.

### `evidence_snapshot_id`
Hash of the sorted evidence IDs + observation versions used by the run.

### `rubric_version_id`
Hash of rubric config + gate code + platform-rule bundle.

CG's RunReceipt then binds all three plus:
- worldpack ID;
- instance set;
- seed;
- event Merkle root.

That makes:

> “FI Allaway campaign passed on 2026-09-07”

a reproducible computational claim rather than prose.

---

# 5. Promotion rule

A campaign cannot transition to `LAUNCHABLE` from a prose score.

Required:

```json
{
  "campaign_version_id": "...",
  "evidence_snapshot_id": "...",
  "rubric_version_id": "...",
  "cg_run_id": "...",
  "all_required_gates_pass": true,
  "secret_suite_pass": true
}
```

This object becomes the `CampaignEligibilityClaim`.
