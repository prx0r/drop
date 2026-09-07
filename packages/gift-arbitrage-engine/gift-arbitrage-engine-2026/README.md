# Gift Arbitrage Engine — Q4 2026

An evidence-weighted scanner and product-blueprint engine for **AI-native personalized gifting**.

The thesis is not “use AI to make Etsy art.” It is:

> Find gift categories where people already pay for personalization, identify the manual creative work that makes buying annoying or expensive, remove that work with AI, and sell a finished physical/digital artifact with a one-click preview and reliable fulfillment.

This package contains:

- `RESEARCH_PERSONALIZED_GIFTS_Q4_2026.md` — full market research and conclusions.
- `OPPORTUNITY_PLAYBOOK.md` — ranked opportunities with suggested tests.
- `TRANSMUTATION_RECIPES.md` — reusable formulas for generating new products across marketplaces.
- `MOONPIG_DISRUPTION.md` — a concrete “occasion OS” strategy rather than a cheap-card clone.
- `MARKETPLACE_PLAYBOOK.md` — Etsy / Shopify / Amazon Custom / TikTok / Pinterest / UK specialty-channel strategy.
- `Q4_2026_CALENDAR.md` — launch/test/cutoff calendar from September through Q5.
- `COMPLIANCE_AND_PRIVACY.md` — Etsy AI/POD rules, IP and sensitive-data guardrails.
- `SOURCES.md` — sourcebook with observed facts and links.
- `data/opportunities.csv` — 40 scored product hypotheses.
- `data/evidence.yml` — structured evidence registry.
- `reports/ranked.{html,md,csv,json}` — generated ranking outputs.
- `src/giftradar/` — runnable scanner/API.

## Current top 10 from the included evidence snapshot

Run `giftradar rank` to regenerate. At the 2026-09-04 research snapshot, the model ranks:

1. AI Memory Card / Mini-Book Card
2. Memory Card + Personalized Gift Attach
3. AI Family Annual / Christmas Newspaper
4. One-click Recipient Photo Book
5. Personalized Reusable Advent Calendar Refill
6. AI-curated Family Calendar
7. QR Story Ornament
8. 2027 Year-Ahead Astrology Hardcover
9. AI Family Game Night Deck
10. 12 Months of Us Card Set

These are **screening scores, not revenue forecasts**. Marketplace result counts and review counts are demand proxies, not unit-sales data. COGS ranges are planning assumptions until a live fulfillment quote is obtained.

## Quick start

Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
giftradar rank --root .
giftradar spec family-annual-newspaper --root .
uvicorn giftradar.api:app --reload
```

Open `reports/ranked.html` for the static opportunity dashboard.

### Run without installing

If dependencies are already available:

```bash
PYTHONPATH=src python -m giftradar.cli rank --root .
```

## API

- `GET /health`
- `GET /opportunities?limit=20`
- `GET /opportunities/{slug}`
- `POST /gift-spec`

`gift-spec` produces a production blueprint rather than hallucinating customer facts. The design rule is: **deterministic data first, generative prose/layout second**.

## Fulfillment adapters

`src/giftradar/adapters/prodigi.py` implements a non-ordering Prodigi quote client. It uses the documented v4 quote endpoint and supports multipage `pageCount` inputs. Add `PRODIGI_API_KEY` to use it.

`src/giftradar/adapters/openai_compatible.py` is an optional OpenAI-compatible text adapter. It is intentionally separated from deterministic calculations and customer facts.

## The test philosophy

Do not build 40 businesses. Use the engine to run **small marketplace-native tests**:

1. pick 3–5 BUILD candidates;
2. create 3 mockups and one 20–40 second transformation demo;
3. publish Etsy listings and/or a Shopify landing page;
4. measure clicks, favorites, add-to-cart, conversion, personalization completion, refund/support burden;
5. obtain real POD quote and delivery SLA;
6. only automate the winner further.

The AI advantage is not merely content generation. It is the ability to collapse 30–120 minutes of customer/designer work into a two-minute structured input flow.
