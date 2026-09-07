# Legacy Code

**DO NOT USE** — these files are preserved for reference only.

## Canonical Code Path

The canonical code path is:

```
schemas/        → Canonical Pydantic models (one source of truth)
pipelines/      → Pure transform functions (no side effects)
storage/        → BigQuery + local JSON (I/O layer)
```

## What moved here

- `services/research/` — Old pipeline, hypothesis tracker, opportunity engine
- `services/analytics/` — Old funnel classifier, query classifier, guard
- `services/scoring/` — Old scoring (replaced by `packages/scoring/bayesian_v2.py`)

## Why

Multiple scoring implementations existed with incompatible semantics:
- `packages/scoring/bayesian.py` — Beta(1,1) prior (WRONG for ecommerce)
- `packages/scoring/bayesian_v2.py` — Hierarchical priors (CORRECT)
- `services/research/scoring_pipeline.py` — Fragile string-indexed arrays

The old code can still be read for reference, but must not write to production data.

## Rule

**Never allow old code to write new experiment records directly.**
