# Scanner Architecture

## Modules

- `models.py` — normalized candidate model.
- `config.py` — country deployment profiles.
- `economics.py` — contribution/CPA/break-even equations.
- `scoring.py` — 100-point ranking + hard/soft gates.
- `compliance.py` — product/country risk flags.
- `db.py` — SQLite persistence for candidates, scores and observations.
- `providers/` — swappable Shopping/keyword data sources.
- `serp_analysis.py` — competitor/price concentration analysis.
- `live_scan.py` — live query observation and metric packaging.
- `pipeline.py` — scores all database candidates.
- `reporting.py` — export ranked evidence.
- `api.py` — read API for dashboards/agents.
- `cli.py` — local operator interface.

## Why SQLite first

SQLite is zero-cost, auditable and perfectly adequate for tens of thousands to millions of screening rows on one VPS. When multiple workers need concurrent writes, migrate the same tables to Postgres. The decision engine is kept independent of the persistence layer so this migration is straightforward.

## Production data flow

```
query generator
    ↓
Shopping provider ──→ raw observations ──→ SERP features
    ↓                                      ↓
keyword provider ─────────────────────────→ candidate
supplier quote/importer ──────────────────→ candidate
country compliance profile ───────────────→ candidate
                                           ↓
                                    economics engine
                                           ↓
                                      scoring/gates
                                           ↓
                            TEST / RESEARCH / REJECT
                                           ↓
                                 campaign observations
                                           ↺
```

## Deployment

On a small VPS:

```bash
pip install -e .
export ECSCAN_DB=/var/lib/ecomscan/scanner.sqlite
uvicorn nordic_arbitrage.api:app --host 0.0.0.0 --port 8080
```

Run ingestion/scoring via cron or your existing agent scheduler. Keep API credentials in environment variables/secrets, never in the repo.

## Docker

```bash
docker compose up -d --build
```

The container stores SQLite at `/data/scanner.sqlite`, mounted from `./runtime` by the included compose file. The API exposes `/health`, `/countries`, `/opportunities?country=NO&gate=TEST`, and per-candidate compliance flags.
