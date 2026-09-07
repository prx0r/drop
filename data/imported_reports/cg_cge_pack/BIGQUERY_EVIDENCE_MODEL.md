# BigQuery Evidence Architecture

## Principle

BigQuery is not a bag of narrative reports.

It is an **append-only evidence warehouse + graph + experiment ledger**.

Use five datasets:

```text
drop_raw        raw collection artifacts / source metadata
drop_evidence   normalized observations and verified claims
drop_graph      entity/compatibility/supplier/installed-base relationships
drop_campaign   campaign versions, runs, mutations, actions
drop_live       real transactions and operating outcomes
```

## Evidence flow

```text
WEB / OEM PDF / API / RETAILER / SUPPLIER EMAIL / GOOGLE DATA / LIVE STORE
                       ↓
                  raw_observation
                       ↓
               extraction candidate
                       ↓
                    verifier
                       ↓
              verified observation
                       ↓
              graph / metric projection
                       ↓
               evidence snapshot
```

## Core rule: event-sourced truth

Never update:
- old stock observation;
- old price;
- prior installed-base publication;
- prior supplier terms.

Insert a newer observation.

A view resolves current state.

## Evidence snapshot strategy

### Cheap ordinary runs
Use append-only evidence IDs and an `as_of` timestamp.

Snapshot manifest contains exact evidence IDs.

### Promotion / launch runs
Materialize read-only BigQuery table snapshots of critical evidence tables.

Current BigQuery supports:
- table snapshots;
- `FOR SYSTEM_TIME AS OF` inside its time-travel window;
- long-lived snapshots beyond that window.

The CG receipt stores snapshot table identifiers.

## Evidence compiler

Input:
- campaign_version_id;
- as_of;
- rubric_version.

It queries only verified evidence.

Output:

```json
{
  "evidence_snapshot_id": "es_...",
  "campaign_version_id": "cv_...",
  "as_of": "...",
  "evidence_ids": ["EV1","EV2"],
  "table_snapshots": [],
  "compiler_version": "...",
  "manifest_hash": "..."
}
```

The bundle is copied into the CG judge environment.

No live BigQuery query during evaluation.

## Why compile evidence?

It gives:
- reproducibility;
- exact provenance;
- no race with changing stock;
- cheap replay;
- deterministic secret evaluation;
- clear "what did we know then?" history.
