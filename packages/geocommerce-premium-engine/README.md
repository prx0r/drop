# GeoCommerce Premium Engine

A VPS-friendly, modular kernel for **AI-powered geographic ecommerce arbitrage**: discover proven premium products, evaluate them per country using Google/supplier evidence, compile localized consultant storefronts, and learn from actual outcomes.

## What is implemented
- canonical product truth + provenance ledger;
- market configs for FI/NO/CH/AT/BE/DK/NZ/IE/PT;
- contribution/CPC-headroom/opportunity scoring with hard compliance/currency gates;
- Google Ads Keyword Planning REST adapter;
- Google Merchant Reports adapter;
- DataForSEO keyword adapter;
- SerpApi Shopping snapshot adapter;
- CJ product-search/detail adapter;
- Shopify Admin GraphQL shell adapter;
- Kopy manual handoff manifest (no invented API);
- Runway image-to-video adapter + Veo job-spec builder;
- guarded advisor/support/human-handoff kernel;
- Google Merchant TSV feed compiler;
- premium Jinja storefront demo;
- experiment ledger;
- Docker/VPS deployment;
- automated tests + static audit.
- final audit: 20/20 regression tests passing + fresh Uvicorn/CLI smoke tests; see `docs/FINAL_AUDIT.md`.

## Quick start
```bash
cp .env.example .env
python -m pip install -r requirements.txt
python scripts/seed_demo.py
python scripts/scan_demo.py
pytest -q
python scripts/audit.py
uvicorn geocommerce.app:app --host 0.0.0.0 --port 8080
```

Then open:
- `http://localhost:8080/docs`
- `http://localhost:8080/fi/products/barista-dual-boiler-espresso`
- `http://localhost:8080/v1/opportunities`

Admin mutation/integration endpoints use `X-Admin-Token`.

## Important
The demo market signals are synthetic fixtures shaped like real data for testing; they are **not current Google market facts**. Replace them with API observations before making a spending decision.

Read first:
- `docs/THESIS.md`
- `docs/MARKET_RESEARCH.md`
- `docs/ARCHITECTURE.md`
- `docs/AGENT_HANDOFF.md`
