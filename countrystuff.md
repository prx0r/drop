# Country Stuff — The Complete Framework

*Word for word from the operator's analysis. Save this. Build from this.*
*Generated: 2026-09-08T09:00:00Z*

---

## The Core Insight

> **Country packs are not the model. They are the immutable contextual memory from which the model derives state.**

The economic system should sit above them.

A country such as Norway is simultaneously:

- `countries/no/` → human/auditable canonical evidence pack
- `dim_country[country_id=NO]` → warehouse identity
- `country:NO` → a logical graph entity
- `country_state_vector(NO, t)` → ML context

BigQuery should be the economic truth store. The graph is a temporal view generated from it.

---

## The Five Architectures

| Architecture | What It Means | Strength | Weakness | Endgame |
|-------------|---------------|----------|----------|---------|
| 1. Country Pack Warehouse | Standardized packs → BigQuery tables | Simple, robust | Descriptive | Great V1 |
| 2. Temporal Commerce Graph | Countries/products/queries as nodes + time-varying edges | Discovery/transplant | Poor accounting | Opportunity engine |
| 3. Economic Event Ledger | Every observation/action/cost append-only | Perfect learning/audit | Less intuitive | Best causal foundation |
| 4. Contextual Portfolio Allocator | Agent chooses probes based on state + learned returns | Directly optimizes capital | Needs experimental history | Autonomous portfolio |
| 5. Commerce World Model | Learn transition/reward models, simulate before spending | Enormous leverage | Most data hungry | Long-term autonomous |

**Correct architecture: 1 + 3 underneath, 2 as derived, 4 as first learned policy, 5 only when data volume justifies it.**

---

## BigQuery as Canonical Economic Substrate

```text
geodrop_raw          → raw observations
geodrop_core         → normalized facts
geodrop_commerce     → economic calculations
geodrop_experiments  → probe outcomes
geodrop_features     → ML features
geodrop_ml           → trained models
geodrop_policy       → learned actions
```

### Dimensions (who/what/where)
country, geo, ecosystem, problem, product, sku, query, merchant, supplier, strategy, agent, creative, store, campaign

### Facts (what happened)
market_observation, installed_base_snapshot, query_metric_snapshot, merchant_snapshot, supplier_snapshot, price_snapshot, ad_auction_metric, web_event, order_line, return_refund, cost_event, agent_action, decision, experiment_assignment, experiment_outcome, prediction, policy_action

---

## The Economic Ledger

### CM0 — Product Contribution
```
net_revenue_excl_tax - COGS - supplier_freight - fulfilment - merchant_borne_duty
- payment_processing - refunds - return_shipping - warranty_chargeback_reserve
```

### CM1 — Acquisition Contribution
```
CM0 - paid_acquisition
```

### CM2 — Automated Operating Contribution
```
CM1 - AI_tokens - scraping_api_spend - image_video_generation - agent_compute
-per_order_software_costs
```

### CM3 — Fully Loaded Experimental Contribution
```
CM2 - allocated_domain_software - human_intervention - samples - setup_expenses
```

**Primary optimization target: CM2.** Prevents: "Agent made £23 gross margin while consuming £31 of Gemini."

---

## Every Agent Action = Economic Action

```text
action_id, agent_id, policy_id, model, prompt_version,
context_snapshot,
action_type, country, ecosystem,
input_tokens, output_tokens, token_cost,
web_queries, search_cost, api_calls, api_cost,
wall_clock_seconds, human_minutes,
expected_information_value, expected_cash_cost,
result_quality, decision_changed, hypothesis_affected,
downstream_experiment_ids
```

After 10,000 actions: "Which research actions actually create economically useful information?"

---

## The Six Nested Control Loops

```text
PORTFOLIO    → choose country / ecosystem / strategy
DISCOVERY    → choose hypothesis / research action
BUSINESS     → choose product / supplier / offer
ACQUISITION  → choose query / channel / bid / creative
FUNNEL       → choose page / price / payment / bundle
OPERATIONS   → choose supplier / stock / fulfilment
```

Every level: state → actions → economic consequences → uncertainty.
Every level rolls up to: **incremental contribution**.

---

## The Value of Information Engine

```text
EVI(a) = E[best decision after observing a] - value of best decision with current information - cost(a)
```

Agent spends information budget where uncertainty is economically material, not where data is easy to collect.

---

## Feature Snapshot (Anti-Leakage)

Every decision gets a frozen feature snapshot:

```text
feature_snapshot_id, as_of, entity,
country_cross_border_rate, country_mobile_payment_rate,
installed_base, installed_base_growth, replacement_share,
search_volume, search_growth, CPC, seller_count, good_seller_count,
price_gap, source_target_gap, supplier_margin, delivery_days...
```

Model only trains on snapshots that existed **before** the decision. Prevents leakage.

---

## The Reward Function

**Primary reward = realized economic contribution (CM2/CM3).**

Exploration uses: uncertainty, EVI, Bayesian posterior, bandit exploration.

Keep these separate. Don't let "information reward" corrupt economic optimization.

---

## The Deepest Metric

```text
Expected incremental economic value per dollar at risk
= E[ΔCM2] / cash_at_risk
```

With uncertainty. Then compare:

```
Spend £0.04 getting another statistic?
Spend £0.30 running a better agent?
Spend £5 testing a keyword?
Spend £100 stocking inventory?
Spend £1,000 scaling Norway?
```

One economic language for everything.

---

## The Endgame

> **An autonomous geographic commerce allocator that discovers fragmented demand, tests it with nearly zero inventory, and moves capital progressively into whichever businesses demonstrate the highest risk-adjusted economic return.**

Not automated dropshipping. Autonomous capital allocation.
