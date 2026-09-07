# Final Audit — GeoCommerce Premium Engine

Audit date: 2026-09-04

## Result

**PASS for kernel / handoff use.** The repository is a working, VPS-deployable application kernel. Live third-party integrations require the operator's own API credentials and commercial accounts; demo market observations are synthetic fixtures and must not be treated as spending guidance.

## Automated regression

Command:

```bash
pytest -q
```

Result: **20 passed**.

Covered behaviors include:
- contribution/CPC headroom economics;
- hard currency-normalization gate;
- regulated/high-liability product rejection;
- end-to-end opportunity evaluation;
- fact-bounded Merchant title generation;
- support refusal to invent unverified specifications;
- admin authentication;
- public advisor + premium storefront rendering;
- market-local checkout configuration;
- ECB FX parsing/cross conversion;
- conservative keyword-cluster aggregation;
- Shopping result median/seller-count normalization;
- fact-bounded localization manifest;
- real-frame requirement for 360 spins;
- premium supplier audit/sample requirement;
- best-seller normalization;
- intra-EU customs handling;
- prepaid-tax gate for premium imports;
- deterministic supplier-offer FX normalization.

## Static audit

Command:

```bash
python scripts/audit.py
```

Result:

```json
{"ok": true, "errors": [], "market_count": 9}
```

The audit compiles the Python package, parses every Python source file, checks market configuration completeness, and scans source for obvious hard-coded API/access-token patterns. A separate basic secret-pattern scan also returned no matches.

## HTTP boot smoke test

A fresh isolated SQLite database was seeded and Uvicorn was started on localhost. Observed results:

- `GET /health` -> 200
- `GET /fi/products/barista-dual-boiler-espresso` -> 200
- premium storefront contains `Find my best fit` and `Ask for a human callback`
- unauthenticated `POST /v1/evaluate` -> 401
- authenticated `POST /v1/evaluate` -> 200
- `POST /v1/advisor` -> 200

## CLI smoke test

Executed:

```bash
python scripts/seed_demo.py
python scripts/scan_demo.py
python scripts/compile_store.py FI premium-pet-ramp-oak --out output
```

The storefront compiler generated `output/premium-pet-ramp-oak-fi.html`. During the audit the compiler was hardened so `--out` accepts either an explicit HTML file or a directory.

## Dependency note

The host ChatGPT runtime reports an unrelated pre-existing `moviepy`/`Pillow` conflict under `pip check`. Neither package appears in this project's pinned `requirements.txt`; the GeoCommerce application, tests, static audit, CLI and Uvicorn smoke tests all ran successfully with the project's declared dependencies present.

## External integration boundary

The following adapters are implemented as kernels but cannot be end-to-end authenticated in this audit without the operator's credentials/accounts:

- Google Ads API;
- Google Merchant API / Market Insights eligibility;
- DataForSEO;
- SerpApi;
- CJ;
- Shopify Admin API;
- Runway;
- Veo / Gemini API;
- Photoroom;
- Twilio.

Kopy is deliberately represented as a manual handoff manifest rather than a fictional API integration.

## Production blockers before real ad spend

1. Connect live Google Ads + Merchant accounts and persist source observations with timestamps.
2. Replace synthetic demo signals with live observations.
3. Complete supplier identity/sample/order/warranty/returns audits for each SKU.
4. Resolve tax/duty by HS code or DDP/landed supplier quote for non-local customs markets.
5. Configure production authentication/secrets and HTTPS/reverse proxy.
6. Connect Shopify/payments/local checkout and verify checkout end-to-end in each target market.
7. Add real analytics/conversion imports and reconcile margin against processor/supplier/refund data.
8. QA all generated media against the physical sample before publishing.

The kernel is therefore **working and audited as software**, but it intentionally does not pretend that synthetic fixtures or unauthenticated external adapters constitute validated commercial market data.
