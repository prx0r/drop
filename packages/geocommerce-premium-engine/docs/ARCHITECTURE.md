# Architecture

```text
                           ┌────────────────────┐
 Google Ads API ──────────>│ Market Evidence    │<──────── DataForSEO
 Merchant API ────────────>│ + provenance       │<──────── SerpApi
                           └─────────┬──────────┘
                                     │
 Supplier APIs/CSV ───────> Canonical Product Truth <──── samples / QA
 AutoDS / CJ / dealer feeds          │
                                     ▼
                           Opportunity Engine
                  demand × auction × margin × risk
                                     │
                    ┌────────────────┴───────────────┐
                    ▼                                ▼
              Market Compiler                 Experiment Engine
         feed/pages/price/support          free listings → paid test
                    │                                │
                    ▼                                ▼
      Shopify/headless storefront             outcome events
                    │                                │
          ┌─────────┼──────────┐                     │
          ▼         ▼          ▼                     │
      Advisor     Media      Human escalation ───────┘
                  Runway/    ticket/Twilio
                  Veo
```

## Design rules
1. Facts are immutable observations; marketing is derived.
2. Every external observation has source + timestamp + hash.
3. Monetary evidence must be normalized to the market currency before scoring.
4. AI can rewrite/translate verified facts but may not create product claims.
5. Commission/supplier incentives never enter recommendation ranking.
6. High-risk/regulatory categories hard-fail before launch.
7. Paid ads are an experiment stage, not product discovery from zero.
8. Category storefronts remain coherent; backend is universal.

## Modules
- `services/economics.py`: contribution, break-even CPC/ROAS and opportunity score.
- `services/catalog.py`: canonical product records.
- `services/signals.py`: append-only market/supplier observations.
- `services/feed.py`: Merchant TSV generation from verified facts.
- `services/storefront.py`: premium page compiler.
- `services/advisor.py`: deterministic first-pass product recommendations.
- `services/support.py`: guarded support with refusal-to-invent behavior.
- `services/media.py`: reference-preserving media briefs.
- `services/experiments.py`: budget/click/conversion/revenue ledger.
- `adapters/*`: optional external providers.

## Production upgrades
- Postgres instead of SQLite once multiple workers write concurrently.
- Redis/queue for long-running Google scans/media renders.
- OAuth credential broker for Google/Shopify.
- real FX service with stored source/timestamp;
- event ingestion from Shopify/Google Ads webhooks;
- embedding/LLM advisor only after deterministic product filters;
- storefront CDN and image/video asset store.
