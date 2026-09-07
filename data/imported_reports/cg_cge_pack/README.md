# DROP × CG × CGE — Campaign Evolution System

**Status:** implementation specification  
**Date:** 2026-09-07

## The endgame

Turn Drop from a collection of persuasive campaign reports into a **replayable campaign compiler**:

```text
COUNTRY / MARKET INTELLIGENCE
          +
OEM / INSTALLED-BASE / SUPPLIER / COMPATIBILITY DATA
          +
LIVE WEB / SUPPLIER / PLATFORM EVIDENCE
          ↓
      BIGQUERY EVIDENCE LAKE
          ↓
   IMMUTABLE EVIDENCE SNAPSHOT
          ↓
DROP CAMPAIGN HYPOTHESIS (structured JSON)
          ↓
CG — TRUSTED JUDGE
hard gates + statistical rubric + secret counterexamples
          ↓
 ┌────────┴─────────┐
 │                  │
ELIGIBLE          BLOCKED / FAIL
 │                  │
 │                  ↓
 │          CGE — UNTRUSTED PROPOSER
 │          narrow / reroute / mutate / expand
 │          + propose highest-EVI research actions
 │                  ↓
 │          WEB / BIGQUERY / SUPPLIER CONTACT
 │                  ↓
 │          VERIFIED NEW EVIDENCE ONLY
 │                  ↓
 └──────────────→ CG rerun
                    ↓
              LAUNCH CLAIM
                    ↓
 Google / Shopify / RFQ / service workflow
                    ↓
           OBSERVED OUTCOMES
                    ↓
                BIGQUERY
                    ↓
             NEXT GENERATION
```

## Repo roles

### `prx0r/drop`
**Domain/control plane.**

Owns:
- canonical campaign schema;
- rubric versions;
- evidence-source policy;
- domain mutation operators;
- campaign lineage;
- BigQuery schemas/views;
- country intelligence;
- launch manifests;
- live outcome ingestion.

It must **not** contain an LLM that can declare its own claims verified.

### `prx0r/cg`
**Trusted deterministic judge.**

CG already has the correct primitives:
- deterministic/replayable worlds;
- hard `QualityGate`s;
- Wilson intervals;
- paired bootstrap;
- lexicographic selection where gates dominate objectives;
- content-addressed `RunReceipt`s;
- sealed/secret evaluation;
- worldpacks.

Use CG as the **only authority that can say a campaign is ELIGIBLE**.

### `prx0r/cge`
**Untrusted search-space expander / proposer.**

CGE adds:
- feedback-guided mutation;
- peer review;
- adversarial benchmark generation;
- MAP-Elites diversity;
- adaptive mutation;
- space-expansion charter.

Use CGE to answer:
- “What nearby campaign atom could legitimately pass?”
- “Which failed assumption should we change?”
- “What evidence should we acquire next?”
- “Should this D2C campaign reroute to B2B or service?”
- “What adjacent OEM/generation/component/country should be explored?”

CGE can **propose**. It cannot certify evidence or calculate authoritative gates.

### BigQuery
**Evidence + analytics plane.**

BigQuery stores:
- raw immutable observations;
- normalized evidence claims;
- compatibility/supersession edges;
- installed-base statistics;
- buyer-role observations;
- demand events;
- supplier stock/terms;
- incumbent benchmark observations;
- campaign versions;
- CG run results;
- CGE mutation proposals;
- research actions and outcomes;
- live sales / CAC / wrong-part / return outcomes.

## Critical trust boundary

`cg` and `cge` are forks of the same `cogym-kernel` Python package.

**Do not install them side-by-side in one environment.**

Recommended deployment:

```text
cg-judge container/process
  pinned CG git SHA
  read-only campaign/evidence bundle
  owns rubric + secret suite
        ↑↓ JSON/MCP/HTTP
cge-proposer container/process
  pinned CGE git SHA
  never sees secret suite
  cannot write evidence truth
```

## The non-negotiable anti-Goodhart rule

> **Campaign mutations may change the hypothesis. They may not change facts.**

Allowed:
- narrow from “heat-pump electronics” to “owner-replaceable Wi-Fi modules”;
- reroute D2C → service;
- change country;
- change OEM;
- split a campaign;
- select another supplier;
- propose a supplier-contact action.

Forbidden:
- `gross_margin: UNKNOWN → 35%`;
- `supplier_will_sell: UNKNOWN → PASS`;
- `consumer_selects_sku: FAIL → PASS`;
- deleting a strong incumbent from the comparison set;
- changing rubric thresholds to save a campaign;
- moving evidence dates or source tiers.

New evidence enters through the **evidence ingestion + verification pipeline**, never through CGE mutation.

## Recommended first implementation

1. Add `drop.campaign_gate-v1` worldpack to CG.
2. Add `drop.evidence_acquisition-v1` worldpack to CG.
3. Add campaign-specific typed mutation operators to CGE.
4. Add append-only evidence/campaign/run tables to BigQuery.
5. Convert current campaign JSONs into immutable `campaign_version`s.
6. Run every existing campaign through the trusted judge.
7. Let CGE propose mutations only for BLOCKED/REJECTED campaigns.
8. Feed results from supplier calls/web research back as new evidence.
9. Launch only a campaign with a signed/content-addressed CG eligibility receipt.

See `IMPLEMENTATION_PLAN.md`.
