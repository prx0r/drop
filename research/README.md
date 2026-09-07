# Google Shopping / Low-Capital Dropshipping Research Bundle

Built from the resources investigated in this conversation, with sources rechecked where possible on 2026-09-06.

## Contents

- `data/sources.csv|json` — 52 source records with provenance/evidence grade.
- `data/case_studies.csv|json` — normalized quantitative case-study snapshots.
- `data/operator_events.csv|json` — state/action/outcome-style operator interventions.
- `data/strategy_rules.csv|json` — synthesized working rules + source IDs.
- `data/research.db` — SQLite database containing the same tables for immediate querying.
- `schemas/` — canonical market/product/action/experiment/store schemas.
- `sql/` — GAQL + SQL templates for building the live dataset.
- `source_indexes/` — human-readable indexes grouped by source type.
- `notes/STRATEGY_SYNTHESIS.md` — the working strategy derived from the cases.
- `notes/MACHINE_READABLE_PLAN.md` — how to turn live data + diaries into replay data.
- `repos/README.md` — Google reference repos and clone commands.

## Start here

```bash
cd data
sqlite3 research.db
```

Example:

```sql
SELECT operator, start_daily_budget, revenue, first_sale_day, notes
FROM case_studies
WHERE start_daily_budget <= 30
ORDER BY start_daily_budget, days;
```

Then inspect `notes/STRATEGY_SYNTHESIS.md` and `source_indexes/ALL_SOURCES.md`.

## Important caveat

Most ecommerce case studies are self-reported. This bundle deliberately preserves evidence grade and source type. Official API/data documentation is high confidence; Reddit/YouTube/agency revenue claims should be treated as hypothesis-generating operator traces unless independently reconciled.
