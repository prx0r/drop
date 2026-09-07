# boringinfra engine

A dependency-free Python CLI that ranks boring software opportunities and generates recipe transplants.

## Quick start

```bash
python -m boringinfra.cli seed --db opportunities.db
python -m boringinfra.cli rank --db opportunities.db --limit 20
python -m boringinfra.cli report --db opportunities.db --out report.md
python -m boringinfra.cli transplant --pattern document_normalizer --niche "UK bookkeepers"
```

## Import your own candidates

CSV headers accepted:

`name,pattern,niche,problem,economic_event,verified_revenue_signal,wtp,recurrence,build_simplicity,data_access,distribution,localization,gross_margin,competition_gap,workflow_criticality,platform_risk,support_burden,regulatory_burden,notes`

All score fields are 0–10. Risk/burden fields are penalties (10 = bad).

```bash
python -m boringinfra.cli import-csv myideas.csv --db opportunities.db
python -m boringinfra.cli rank --db opportunities.db
```

## Design principles

- Score *economic shapes*, not hype.
- Reward verified revenue evidence and recurring workflow pain.
- Penalize platform risk and support burden.
- Prefer one-input/one-job/one-output products.
- Use the output to prioritize customer interviews, not as proof of demand.
