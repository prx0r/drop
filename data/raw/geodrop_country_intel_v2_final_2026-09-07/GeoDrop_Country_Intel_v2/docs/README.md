# GeoDrop Country Intelligence v2

## What GeoDrop is
GeoDrop is not a product-list generator. It is a longitudinal evidence graph and experiment system for answering:

> Find rapidly growing or enormous installed-base ecosystems in small, wealthy, ecommerce-heavy countries; identify the maintenance/replacement/problem queries those ecosystems create; use mature source markets as catalogue and business-model oracles; find target-country cells where local specialist commerce has not caught up; then test those cells with narrow localized ecommerce probes.

## Core state machine
`COUNTRY -> ECOSYSTEM -> INSTALLED_BASE/COHORT -> PROBLEM/JOB -> NATIVE QUERY -> SOURCE-MARKET ORACLE -> SOURCE/TARGET GAP -> PRODUCT/SKU -> SUPPLIER/ECONOMICS -> PROBE -> OUTCOME -> STRATEGY LEARNING`

## Two scores, two questions
1. `ECOSYSTEM_DISCOVERY_SCORE`: what ecosystem deserves research?
2. `PRODUCT_MARKET_LAUNCH_SCORE`: is an exact product-market ready for a commerce test?

Never use the launch score as a discovery score. Hard gates override scores.

## Non-negotiables
- Facts, interpretation, hypotheses, strategies, experiments and outcomes are separate objects.
- Missing data is `null`/`MISSING_REQUIRED`, never a plausible estimate.
- Every factual value has provenance, definition and time availability.
- Point-in-time backtests may only use evidence available at the historical decision timestamp.
- Raw snapshots are immutable and hashable.
- A content gap is not a merchant gap.
- Hidden B2B/dealer infrastructure counts as competition/supply and must be investigated.
- Exact GTIN/MPN/model identity is required before a product becomes launchable.
- Realized contribution, not revenue or ROAS, is the economic target.

## Country pack
See `docs/CANONICAL_SPEC.md` and `docs/DATA_DICTIONARY.md`.

## Reference
`countries/no/` contains Norway public evidence plus explicit private/authenticated blockers. The pack is designed to remain useful even when Google Ads/dealer net-cost credentials are unavailable: missing authenticated metrics block promotion rather than being inferred.
