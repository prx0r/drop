# Package Manifest

## Core
- `src/nordic_arbitrage/` — scanner engine, API and provider adapters.
- `pyproject.toml` — installable Python package / CLI.
- `Dockerfile`, `docker-compose.yml`, `Makefile` — VPS deployment helpers.

## Research/data
- `docs/MARKET_RESEARCH_2026-09-04.md` — Norway/Denmark research and product strategy.
- `docs/OPERATING_PLAYBOOK.md` — execution from discovery to campaign learning.
- `docs/SCORING.md` — formulas, score and hard gates.
- `docs/DATA_SOURCES.md` — data integrations and provenance policy.
- `docs/COUNTRY_EXPANSION.md` — Finland/Sweden/NZ/Australia/Gulf expansion logic.
- `docs/ARCHITECTURE.md` — system design/deployment.
- `data/live_screening_candidates.csv` — 50 live-market screening observations with scenario economics fields.
- `data/query_seeds.csv` — 64 NO/DK native commercial query seeds for validation.
- `data/source_registry.csv` — research-source registry.

## Ready-to-inspect outputs
- `outputs/demo_scanner.sqlite` — populated/scored demo SQLite DB.
- `outputs/ranked_demo.csv` — complete ranked seed export.
- `outputs/OFFLINE_DEMO.md` — top ranking with evidence caveats.
- `TEST_REPORT.md` — what was actually executed and what was not.
