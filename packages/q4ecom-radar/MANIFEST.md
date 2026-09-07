# Package Manifest

- `README.md` — setup, architecture, live adapters, scoring and operating instructions
- `RESEARCH_Q4_2026.md` — source-backed Q4 2026 research and creator synthesis
- `DEPLOYMENT.md` — production/deployment checklist
- `config/markets.yml` — UK, Norway, Denmark + 7 extensible markets
- `config/products.yml` — 20 seeded specialist product hypotheses
- `config/scoring.yml` — editable weights, penalties and thresholds
- `src/q4radar/` — scanner, database, scoring, API, CLI and source adapters
- `data/observation-template.csv` — normalized bridge for external/manual evidence
- `tests/` — scoring/economics/pipeline tests
- `Dockerfile`, `docker-compose.yml` — container deployment
- `.github/workflows/daily-radar.yml` — scheduled GitHub Actions scan template
- `reports/` — one deterministic synthetic demo run (explicitly not live market evidence)

Validation completed before packaging:

- unit/pipeline tests: PASS
- deterministic multi-market demo scan: PASS
- Python compilation: PASS
- CLI entry point: PASS
