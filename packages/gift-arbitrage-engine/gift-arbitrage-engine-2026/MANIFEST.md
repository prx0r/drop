# Build Manifest

Build date: 2026-09-04

## Research/artifacts

- README.md
- RESEARCH_PERSONALIZED_GIFTS_Q4_2026.md
- OPPORTUNITY_PLAYBOOK.md
- TRANSMUTATION_RECIPES.md
- MOONPIG_DISRUPTION.md
- MARKETPLACE_PLAYBOOK.md
- Q4_2026_CALENDAR.md
- COMPLIANCE_AND_PRIVACY.md
- IMPLEMENTATION.md
- SOURCES.md

## Structured data

- 40 opportunity hypotheses in `config/opportunities.yml` and `data/opportunities.csv`
- 34 evidence records in `data/evidence.yml`
- scoring weights/penalties in `config/scoring.yml`
- marketplace strategy in `config/marketplaces.yml`

## Engine

- Typer CLI (`giftradar`)
- FastAPI read-only opportunity/spec API
- evidence-weighted scoring model
- product-generation blueprint generator
- optional Prodigi v4 quote adapter (does not place orders)
- optional OpenAI-compatible text-generation adapter
- Docker / Compose / Makefile / GitHub Actions workflow

## Generated reports

- ranked.html
- ranked.md
- ranked.csv
- ranked.json
- six example production blueprints

## Validation

- Python source compiles successfully
- `pytest`: **4 passed**
- demo ranking executed end-to-end

## Important interpretation notes

- Marketplace result/review counts are demand proxies, not sales counts.
- Commercial market-size studies are estimates.
- Target COGS/retail values are screening assumptions and require live POD quotes and fee/tax calculations before launch.
- The code does not scrape Etsy or violate marketplace access controls; marketplace snapshots are curated evidence inputs.
