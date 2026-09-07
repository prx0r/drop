# GeoDrop v2 Canonical Country Contract

Every country contains the same objects. Country evidence is immutable historical state; global strategy logic is versioned separately so a scoring-theory change cannot rewrite the past.

## Required files
```
manifest.json
profile.json
sources.jsonl
raw_snapshot_manifest.jsonl
observations.jsonl
ecosystems.jsonl
problems.jsonl
queries.jsonl
merchants.jsonl
source_archetypes.jsonl
source_target_gaps.jsonl
trade_code_map.jsonl
product_markets.jsonl
business_hypotheses.jsonl
hypotheses.jsonl
candidate_universes.jsonl
score_snapshots.jsonl
decisions.jsonl
experiments.jsonl
outcomes.jsonl
backtests.jsonl
connectors/*.json
series/_manifest.json
series/*.csv
reports/01_market_overview.json
reports/02_consumer_behavior.json
reports/03_structural_demand.json
reports/04_acquisition_query_forest.json
reports/05_competition_merchant_census.json
reports/06_supply_logistics_compliance.json
reports/07_source_market_oracle.json
reports/08_opportunity_summary.json
reports/09_geographic_opportunity.json
reports/10_experiment_backtest_learning.json
```

## Evidence objects
`source` = publisher/resource identity. `raw_snapshot_manifest` = immutable acquired artefact metadata. `observation` = normalized fact or explicit missing field. `series` = repeated measurements where row-level CSV is more efficient.

## Discovery objects
`ecosystem` represents an installed-base/service ecosystem, not a store idea. `problem` links owned systems to failure/maintenance/replacement/upgrade/compliance/seasonal jobs. `query` maps those jobs to native-language observable intent. `source_archetype` records mature merchants/business models. `source_target_gap` measures the delta between source-market maturity and target-market commerce.

## Commerce objects
`product_market` is exact target-country commerce validation. `hypothesis` declares a falsifiable strategy-specific claim before testing. `experiment` freezes treatment, candidate universe and evidence snapshot. `outcome` stores actual funnel/economic results. `backtest` stores evaluation of a frozen strategy version.

## Time semantics
Every point-in-time fact should record `observed_at`, `published_at`, `available_at`, `retrieved_at` where known. `available_at` means the earliest timestamp GeoDrop could reasonably have known the value. True historical backtests require `available_at <= as_of`; unknown availability is not point-in-time-safe.

## Scope
Facts can be scoped to country, region, municipality, postal prefix, ecosystem, brand, model, component, cohort or product market. Definition fields are required for ambiguous installed-base statistics.

## Evidence tiers
A = official exact/administrative; B = primary industry data with methodology; C = triangulated/estimated proxy; D = market/SERP/merchant/community evidence; E = private/unknown. Tier is not confidence: an official table can still have coverage/definition caveats.

## Hard launch gates
At minimum: exact SKU identity; resale rights; supplier path; landed cost; returns/warranty/RMA; target delivery feasibility; local checkout; exact native demand/CPC where paid acquisition is proposed; >=3 viable anchor SKUs for a narrow specialist launch; positive pre-ad contribution. Unknown required gate = no launch.

## Backtest classes
- `TRUE_HISTORICAL`: only evidence genuinely available at decision time.
- `RECONSTRUCTED_HISTORICAL`: archives/retrospective datasets; label leakage risk and confidence reduction.
- `PROSPECTIVE_SHADOW`: hypotheses are frozen now and evaluated later; preferred for causal strategy learning.

## Learning logs
`candidate_universes.jsonl` prevents survivor bias by freezing everything eligible before ranking. `score_snapshots.jsonl` is append-only; never overwrite old scores after new evidence arrives. `decisions.jsonl` records research/kill/test decisions, including rejected candidates. `business_hypotheses.jsonl` stores the proposed commerce model separately from the falsifiable strategy hypothesis.
