# Boring Infra Opportunity Engine — 4 Sep 2026

This pack is a research report + runnable codebase for finding **overlooked software/infrastructure businesses with verified revenue**, then translating the *economic recipe* into a different niche rather than copying a product.

Hard exclusions applied in this research: **no bug bounties, no dropshipping, no gambling, no weapons, no medical diagnosis products**.

## What is inside

- `reports/00_EXECUTIVE_SUMMARY.md` — what actually works and what does not.
- `reports/01_VERIFIED_REVENUE_CASES.md` — payment-processor-verified examples, with current metrics and evidence grades.
- `reports/02_WINNER_LOSER_PAIRS.md` — the most important part: similar-looking products with radically different outcomes.
- `reports/03_RECIPE_LIBRARY.md` — reusable economic patterns.
- `reports/04_DEEP_NICHE_TRANSPLANTS.md` — concrete products to build by applying those patterns to narrower markets.
- `reports/05_VALIDATION_PROTOCOL.md` — how to kill bad ideas before spending weeks building.
- `reports/06_30_DAY_BUILD_PLAN.md` — execution sequence.
- `reports/07_GTM_PLAYBOOK.md` — distribution for boring B2B utilities.
- `reports/08_SOURCE_LOG.md` — source URLs and evidence notes.
- `data/verified_examples.csv` — structured case-study dataset.
- `data/opportunity_seeds.csv` — ranked transplant candidates.
- `engine/` — stdlib-only Python opportunity scoring/report engine.

## Run the engine

```bash
cd engine
python -m boringinfra.cli seed --db opportunities.db
python -m boringinfra.cli rank --db opportunities.db --limit 30
python -m boringinfra.cli report --db opportunities.db --out ranked_report.md
python -m boringinfra.cli transplant --pattern "workflow_adapter" --niche "UK property inventory clerks"
```

No paid API is required for the seeded version.

## Evidence policy

The core examples use revenue pages that explicitly state they are verified through Stripe, Paddle, RevenueCat or another payment processor. Revenue verification does **not** automatically verify every marketing claim, user count or profit figure. Those are labelled separately.

TrustMRR's official API terms prohibit using its API to clone businesses or bulk-republish its database. This engine therefore ships with a **curated research seed**, not an automated TrustMRR scraper. Use public/official sources lawfully and use the recipes to build differentiated products for other customers and workflows.
