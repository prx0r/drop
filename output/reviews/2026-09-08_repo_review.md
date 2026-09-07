# Drop Repo Review — 2026-09-08

**Reviewed at:** HEAD `927b5fcbf177b58e037e51f67f35c47cf478a58f`

**Endgame being evaluated against:**

> Can every campaign become a rigorously preregistered economic hypothesis, can every action and cost be logged, can we predict profitability before launch, update that prediction as evidence arrives, explain why it won/lost, and progressively learn a policy that selects campaigns with extremely high calibrated probability of positive contribution?

**Answer:** The conceptual architecture is now strong, but the executable statistical pipeline is not yet trustworthy enough to learn from paid experiments. I would fix this before generating much real campaign data, because every campaign run with incomplete lineage is a partially wasted training example.

---

## Overall assessment

| Area | Current state | Assessment |
|---|---|---|
| Overall vision | 9/10 | Correct endgame |
| Country/market context | 8/10 | Strong GeoDrop primitive |
| Evidence/provenance philosophy | 8/10 | Very good |
| Typed pipeline architecture | 7/10 | Recent reset is correct |
| Economic model | 5/10 | Useful calculator, not probabilistic model |
| Bayesian inference | 4/10 | v2 promising but not genuinely hierarchical yet |
| Hypothesis engine | 3/10 | Evidence voting rather than statistical inference |
| Campaign experiment schema | 3/10 | Missing critical causal fields |
| BigQuery substrate | 4/10 | Right destination, current storage implementation incomplete |
| Point-in-time/backtest safety | 3/10 | Not enforced throughout |
| Offline policy-learning readiness | 2/10 | Missing propensities |
| Calibration infrastructure | 1/10 | Essentially absent |
| Potential after fixes | **extremely high** | The pieces are there |

The repo has crossed an important threshold. It is no longer missing the vision. **Its largest risk is now having several approximately-correct implementations of the vision whose statistical semantics disagree.**

---

## 1. The recent architectural reset is good

The new top-level architecture is substantially better:

```
schemas/
pipelines/
storage/
countries/
```

The new `Observation` explicitly separates a fact from an inference or decision, is immutable, records source grade, source identity, independence grouping, raw evidence and probe/hypothesis/candidate lineage. That is exactly the right primitive.

Likewise, the hypothesis contract forces:

```
claim
null hypothesis
falsifier
evidence for
evidence against
state
```

which is much better than having an agent simply produce an "opportunity score."

And the candidate lifecycle is directionally excellent:

```
DISCOVERED
→ DEMAND_VERIFIED
→ MERCHANT_GAP_VERIFIED
→ SUPPLY_PATH_VERIFIED
→ MARGIN_VERIFIED
→ SEARCH_ECONOMICS_VERIFIED
→ LAUNCHABLE
→ FREE_TRAFFIC_TEST
→ PAID_TEST
→ PROFITABLE / KILLED
```

This is exactly the kind of funnel that prevents agents from saying:

> "This looks cool; spend $10."

before supplier economics or real demand are established.

---

## 2. P0: there are currently multiple statistical universes in one repo

This is the biggest structural issue.

You currently have at least:

```
NEW:
schemas/
pipelines/
storage/

OLDER:
packages/schemas/
packages/scoring/
packages/economics/

OLDER AGAIN / SERVICES:
services/research/
services/analytics/
```

The older research tree still contains:

`pipeline.py`, `pipeline_v2.py`, `evoi.py`, `allocation.py`, `scoring_pipeline.py`, `hypothesis_tracker.py`, `opportunity_engine.py`, etc.

And the semantics are not identical.

For example, the old capital allocator operates on old `CandidateState` values and old package schemas, while the new canonical candidate defines a different lifecycle.

That is dangerous because six months from now you could have:

```
campaign A scored by algorithm 1
campaign B scored by algorithm 2
campaign C scored by algorithm 3
```

and then train a model as though those campaign-selection processes were equivalent.

They are not.

### Fix

There must be **one executable canonical route**:

```
schemas_v3
     ↓
feature builder
     ↓
belief model
     ↓
decision policy
     ↓
experiment
     ↓
economic outcome
```

Everything else goes under:

```
legacy/
```

or gets wrapped by explicit adapters.

Never allow old code to write new experiment records directly.

---

## 3. P0: the BigQuery storage implementation has a real query bug

This needs fixing immediately.

`storage/bigquery.py` constructs SQL such as:

```sql
WHERE candidate_id = @candidate_id
```

and builds:

```python
params["candidate_id"] = candidate_id
```

but does not actually attach those parameters to a BigQuery `QueryJobConfig`.

It then executes:

```python
self.client.query(query, job_config=None)
```

or simply:

```python
self.client.query(query)
```

The generic `query(sql, params)` method similarly accepts `params` and ignores them.

So the query layer looks parameterized but isn't.

That is not merely an implementation nuisance. This is the storage layer underneath the supposed canonical evidence graph.

Fix it before relying on filtered reads.

---

## 4. P0: your "Bayesian hypothesis ledger" is not Bayesian

This is probably the most important statistical correction.

The current canonical `Hypothesis` contains:

```python
confidence = 0.5
```

and its `support_ratio` is essentially:

```
number of FOR observations
──────────────────────────
FOR + AGAINST observations
```

The hypothesis pipeline then says approximately:

```
>70% evidence FOR → supported
>70% evidence AGAINST → falsified
```

after minimum observation counts.

That produces several failures.

Ten weak observations can outweigh one extremely strong measurement.

Ten observations copied from correlated sources can overwhelm one independent fact.

And the mapping is sometimes logically invalid:

```
good_sellers → AGAINST
```

regardless of whether the observed value is:

```
good_sellers = 0
```

or:

```
good_sellers = 40
```

Likewise:

```
contribution_margin → FOR
```

regardless of whether margin is positive or negative unless a separate special field happens to be emitted.

This should remain a **qualitative research ledger**, but it must not be confused with the economic posterior.

I would rename it conceptually:

```
ResearchHypothesisLedger
```

and create a separate:

```
EconomicBeliefState
```

that is actually probabilistic.

---

## 5. There is a good Bayesian v2 — but it isn't wired cleanly

One correction to my intermediate review: an initial GitHub search did not surface the files, but direct package inspection confirms that these do exist:

```
packages/scoring/bayesian_v2.py
packages/scoring/unified_scorer.py
packages/scoring/cross_border.py
```

`bayesian_v2.py` is substantially better than v1.

It uses an exact Beta distribution via SciPy and Monte Carlo profit-per-click simulation.

But there are still major problems.

### Its "hierarchical priors" are not hierarchical

They're currently static constants:

```python
high_ticket_technical = Beta(0.5, 150)
mid_range_consumer    = Beta(2, 200)
low_ticket_impulse    = Beta(5, 150)
default               = Beta(1, 200)
```

The function even accepts:

```python
country
```

but doesn't use it.

That is a **hand-authored prior lookup table**, not hierarchical empirical Bayes.

Eventually we want something like:

$$
\text{logit}(CVR_i)=
\mu+
\alpha_{\text{country}}+
\beta_{\text{category}}+
\gamma_{\text{query-intent}}+
\delta_{\text{AOV-band}}+
...
$$

with partial pooling.

Finland heat-pump probes then inform other Finnish technical products a little.

Finnish heat pumps inform Swedish heat pumps more.

Norwegian mugs inform them very little.

That is actual hierarchical transfer.

---

## 6. Worse: active analytics still import Bayesian v1

`services/analytics/funnel_classifier.py` imports:

```python
from packages.scoring.bayesian import ...
```

not `bayesian_v2`.

And the old `bayesian.py` still uses:

```
Beta(1,1)
```

plus normal approximations of Beta tails.

This matters enormously for ecommerce.

Beta(1,1) has prior mean:

$$
50\%
$$

when realistic ecommerce CVR might be:

$$
0.2\%-3\%.
$$

After 100 clicks and zero orders:

$$
Beta(1,101)
$$

still gives roughly a **60% probability that CVR exceeds 0.5%**.

That is wildly more optimistic than a realistic ecommerce prior.

So the v2 fix exists, but some operational paths still route through the bad model.

**Delete or hard-deprecate v1.**

Do not allow an import to reach it.

---

## 7. `unified_scorer.py` currently contains hard correctness bugs

This was the most concerning file I inspected.

It advertises itself as:

> "ONE canonical scoring system."

But the CVR observation handling effectively does:

```python
if MEASURED:
    clicks += int(obs.value)

elif OBSERVED_ZERO:
    orders += 0
```

There is no clean representation of:

```
clicks = 174
orders = 3
```

and no functioning path for positive orders in that loop.

It also ignores:

```
confidence
independence_group
```

despite those being included in `EvidenceObservation`.

And `score_candidate()` calls:

```python
datetime.now()
```

while `datetime` is not imported in its normal module import path.

That scorer should not be used for production decisions until rewritten.

The right input isn't:

```
"CVR observations": [mystery scalar observations]
```

It is:

```
TrafficOutcome {
    qualified_clicks
    purchases
    sessions
    add_to_carts
    checkouts
    window_start
    window_end
    traffic_source
    treatment_id
}
```

---

## 8. Your funnel classifier contains a subtle statistical error

This one is important.

For clicks with no add-to-cart it calculates:

$$
P(0)=(1-\text{break-even CVR})^{clicks}
$$

and then assigns:

```python
probability_viable = 1 - p_zero
```

But:

$$
1-P(0 \mid viable)
$$

is **not**:

$$
P(viable \mid observed\ data)
$$

Those are different conditional probabilities.

It's essentially reversing Bayes' theorem.

And there's another mismatch: it's using **purchase break-even CVR** to reason about an **add-to-cart event**.

Those stages need different probabilities:

```
P(click | impression)
P(ATC | click)
P(checkout | ATC)
P(purchase | checkout)
P(return | purchase)
```

You could model the entire funnel probabilistically later.

For now, at minimum, never call that computed value `probability_viable`.

---

## 9. The current EVI system is a heuristic, not true economic value of information

The idea is excellent.

The implementation is not yet EVI.

Current new code roughly calculates:

$$
EVI =
\frac{
P(resolve)\times impact\times candidate\_value
}{
research\_cost
}
$$

But inputs such as:

```
email supplier → P(resolve)=0.7
SERP check → 0.9
dealer price decision impact → 0.9
```

are hand-coded.

And cost is a normalized:

```
0.1 / 0.2 / 0.5 / ...
```

rather than dollars.

Older `evoi.py` is even more explicit: many actions are given cost `$0` and then receive an arbitrary `×100` priority boost.

Proper economic value of information should be:

$$
EVSI(a)=
E[
\max_d E(CM2 \mid D,new\ evidence_a)
]
-
\max_d E(CM2 \mid D)
-
Cost(a)
$$

Now:

> Get distributor quote.

could be worth £14.80 of expected decision value and cost £0.07 in model/tool expense.

While:

> Run another generic web crawl.

might cost £0.11 and be worth £0.02.

**That eventually becomes learned from your own history.**

---

## 10. The economic model is still a scenario calculator

`packages/economics/model.py` is useful, but it's not the model you ultimately want.

It has hard defaults such as:

```
payment fee = 2.9% + 0.20
returns = 5%
CPC = 1.0

CVR pessimistic = 0.2%
CVR base        = 0.5%
CVR optimistic  = 1.0%
```

and then computes deterministic headroom bands.

That's fine for early screening.

But your actual question is:

> **What is the posterior probability that this campaign will generate positive mature CM2?**

That's a different object.

---

## 11. The canonical campaign should literally be a hypothesis

I would introduce a first-class:

```
CampaignHypothesis
```

with something close to this contract:

```
campaign_hypothesis_id
candidate_id

country_id
ecosystem_id
problem_id
product_id
sku_ids
query_cluster_id

strategy_id
strategy_version

created_at
decision_time

feature_snapshot_id
country_pack_version

CLAIM
expected_CM2_30d > 0

NULL
CM2_30d <= 0

PREDICTIONS AT T0
CPC_distribution
CTR_distribution
CVR_distribution
AOV_distribution
CM0_per_order_distribution
return_rate_distribution
traffic_volume_distribution

derived_expected_CM2
P_CM2_positive
CM2_p10
CM2_p50
CM2_p90

FALSIFICATION
economic condition
maximum spend
maximum acceptable CPC
minimum posterior probability

EXPERIMENT
campaign configuration
budget
target geography
traffic channel

treatment_id
control_id
assignment_probability

POLICY
policy_id
policy_version
candidate_action_set
chosen_action
chosen_action_probability

OUTCOMES
1d
7d
30d
60d
90d
```

That is what turns a Google Shopping campaign into a **scientific economic experiment**.

---

## 12. Freeze all features at decision time

This is absolutely mandatory.

The most important missing table may be:

```
feature_snapshot
```

For campaign `X` at `t0`, freeze:

```
country pack version
installed base
installed-base growth
replacement pressure
search volume
search growth
Keyword Planner CPC
seller count
good seller count
source-target catalogue gap
median market price
our price
supplier cost
delivery days
local payment support
merchant-quality gap
seasonality
competitor density
```

Later, none of those values can change retrospectively for that decision.

The prediction must always be reconstructable as:

```
model version M
+
feature snapshot F
+
policy version P
=
prediction Y
```

Without that, you cannot legitimately backtest.

---

## 13. Add `available_at`, not just `observed_at`

The new `Observation` has:

```
observed_at
```

which is good.

But for point-in-time analysis, we need at least:

```
event_time
published_at
observed_at
available_at
ingested_at
```

Example:

```
SSB statistic refers to:
2026-06-30

published:
2026-08-15

GeoDrop discovered:
2026-09-07
```

A backtest pretending to make a July 2026 decision **cannot use that observation**.

Canonical rule:

```sql
WHERE available_at <= decision_time
```

everywhere.

---

## 14. The graph should not be the primary statistical store

The current endgame document treats nodes and weighted edges as central.

Keep the graph.

But do not make:

```
edge.weight = 0.87
```

the truth.

The truth should be append-only facts.

Something more like:

| Warehouse object | Purpose |
|---|---|
| `dim_country` | Norway, Finland, etc. |
| `dim_ecosystem` | Heat pumps, cabins, Model Y |
| `dim_problem` | replacement, frost, leak |
| `dim_product` | canonical product |
| `dim_sku` | exact sellable item |
| `dim_query` | search term/query cluster |
| `dim_supplier` | supply entity |
| `dim_merchant` | competitor |
| `dim_strategy` | installed-base lag etc. |
| `fact_market_observation` | external facts |
| `fact_feature_snapshot` | frozen ML state |
| `fact_decision_event` | every agent decision |
| `fact_campaign_day` | ad performance |
| `fact_search_term_day` | query-level performance |
| `fact_funnel_event` | GA4 events |
| `fact_order_line` | actual sales |
| `fact_return` | refund/return/warranty |
| `fact_cost_event` | every economic cost |
| `fact_experiment_assignment` | treatment/control |
| `fact_prediction` | forecasts |
| `fact_outcome_maturity` | 1/7/30/60/90d labels |

The graph becomes a **derived representation over those facts**.

That prevents dynamic edge updates from destroying history.

---

## 15. Your old replay schema already points in this direction

The older `bootstrap_schema.sql` actually has good primitives:

```
market_product_week
keyword_month
product_day
action_log
experiment
store_day
```

Don't discard these concepts.

Rebuild them into the new typed architecture.

The old schema is missing the precise fields needed for ML, but its dimensional thinking is correct.

---

## 16. Google Ads needs to become much more granular

Your current GAQL query retrieves:

```
date
product item
title
brand
category
impressions
clicks
cost
conversions
conversion value
revenue
COGS
gross profit
```

That's a useful dashboard query.

It is insufficient as a scientific event stream.

Google Ads' current API exposes actual search-term data, with campaign/ad-group context, device, match source/type and conversion dimensions.

It also exposes economically useful auction-state signals including:

- search impression share;
- rank-lost impression share;
- budget-lost impression share;
- top/absolute-top share.

And importantly it exposes **conversion-lag buckets** and conversion-date metrics, which matter because today's apparent campaign profit is not mature profit.

So capture at minimum:

```
date/hour
campaign
ad_group / asset_group
product
query/search_term
match type
device
geo

impressions
clicks
cost

search impression share
lost by rank
lost by budget

conversion action
conversion lag
conversions
conversion value

bidding strategy
budget

store version
page version
offer version
price snapshot
feed title/image snapshot
```

---

## 17. Use the native Google → BigQuery streams

Don't build all of this around custom daily scripts.

Google's BigQuery Data Transfer Service now supports recurring daily Google Ads transfers using Google Ads reporting.

GA4 exports **raw unsampled events** to BigQuery once daily and can also stream intraday events. Standard properties support up to 1 million events/day in daily export.

That gives you:

```
view_item
add_to_cart
begin_checkout
purchase
session context
traffic context
items
```

as raw events.

Then join:

```
Google Ads
     ↓
click/query
     ↓
GA4 funnel
     ↓
order
     ↓
supplier cost
     ↓
return/refund
     ↓
CM2
```

That is the full chain you need.

---

## 18. The central forecast should be decomposed

Don't immediately train:

```
XGBoost(country features) → profitable yes/no
```

First model the actual economic mechanism.

For a campaign:

$$
I \sim \text{traffic availability model}
$$

$$
Clicks \sim Binomial(I, CTR)
$$

$$
Orders \sim Binomial(Clicks, CVR)
$$

$$
Return_i \sim Bernoulli(r)
$$

and then:

$$
CM2 =
\sum_i CM0_i
-
AdSpend
-
AgentCost
-
APICost
-
GenerationCost
$$

Each term has uncertainty.

I would initially use approximately:

| Quantity | Starting model |
|---|---|
| impressions/search supply | NegBin / empirical |
| CPC | log-normal or Gamma |
| CTR | Beta-Binomial / hierarchical logistic |
| CVR | Beta-Binomial / hierarchical logistic |
| AOV | empirical/log-normal |
| gross contribution/order | empirical distribution |
| return probability | Beta-Binomial |
| fulfilment delay | empirical survival model |
| API/token cost | measured deterministic/empirical |
| ad spend | observed/planned |

Monte Carlo gives:

```
E[CM2_30]
P(CM2_30 > 0)
CM2_p05
CM2_p10
CM2_p50
CM2_p90
expected maximum loss
```

That is far more meaningful than:

```
opportunity = 81/100
```

---

## 19. Then "why did it fail?" becomes mathematically decomposable

Suppose predicted:

```
P(profitable) = 78%
```

and the campaign loses.

Don't ask an LLM why.

Compare predicted versus realized components:

```
CPC       predicted  €0.54   realized €0.93
CVR       predicted  0.82%   realized 0.76%
CM0/order predicted €118     realized €121
returns   predicted  4%      realized 3%
traffic   predicted  800     realized 690
```

Answer:

> The product thesis was approximately right; auction cost was wrong. 86% of forecast error came from CPC.

Another:

```
CPC right
CTR right
ATC right
checkout right
purchase CVR collapsed
```

Then investigate:

```
delivery
payment
trust
shipping charge
```

This is the distinction between:

**economic forecast error**

and

**causal diagnosis**.

---

## 20. Causal "why" requires experiments, not feature attribution

Predictive models can tell you:

> Local payment availability is associated with profitable campaigns.

They cannot prove:

> Adding Vipps caused the higher conversion.

For causal answers, randomize where practical.

The experiment record needs:

```
randomization_unit
eligible_population
treatment
control
assignment_probability
start
end
primary outcome
guardrails
```

Then you can eventually estimate heterogeneous effects:

```
effect of local payment
    conditional on country/product type

effect of 2-day delivery
    conditional on urgency

effect of comparison pages
    conditional on technical complexity
```

This will be incredibly valuable.

---

## 21. Log the probability of every agent action

This is one of the highest-leverage fields missing today.

Suppose the policy sees ten opportunities and chooses:

```
Finland heat pump controller
```

Store:

```
candidate_action_set = [...]
chosen_action = FI_HEATPUMP_CONTROLLER
chosen_action_probability = 0.37

policy = ThompsonSamplingV3
policy_version = abc123
```

Why?

Because later your dataset becomes **selectively sampled**.

The agent tends to test things it already thinks will succeed.

If you don't know the probability under which actions were selected, comparing future policies offline becomes badly biased.

Contextual-bandit research uses inverse-propensity and doubly robust estimators precisely for evaluating new policies using data generated under another logging policy.

This should be implemented **before autonomous campaign selection**.

Not afterward.

---

## 22. Markets are nonstationary, so time matters even for policy learning

This is also why I would avoid the language "eventually probability 1."

Norwegian CPCs change.

Competitors enter.

Google changes bidding systems.

Suppliers change prices.

Trends decay.

Policies improve.

Research on off-policy evaluation explicitly treats reusing historical data in **nonstationary environments** as a separate challenge because naive reuse creates bias.

So every context needs time.

And recent samples may be weighted differently from old samples.

---

## 23. The goal is not literally probability 1

You can absolutely drive the **success rate of campaigns you choose to launch** increasingly high.

But forcing predictions toward:

```
0.99
```

is not the objective.

The objective is:

> When GeoDrop predicts 80%, approximately 80% of comparable campaigns should succeed.

When it predicts 95%, about 95% should succeed.

That is **calibration**.

Track:

```
Brier score
log loss
reliability curves
calibration slope
calibration intercept
```

The holy-grail chart becomes:

| Predicted `P(CM2>0)` | Actual success |
|---|---|
| 0–10% | ~5% |
| 10–30% | ~21% |
| 30–50% | ~39% |
| 50–70% | ~61% |
| 70–90% | ~81% |
| 90–100% | ~94% |

Then you can simply change your capital threshold.

Maybe:

```
research freely: P > 0.3
free listing:    P > 0.5
$5 probe:        P > 0.65
$50 validation:  P > 0.8
scale:           lower credible bound > 0
```

Those thresholds should eventually themselves be optimized economically.

---

## 24. Country data becomes a prior, not a score

This is where GeoDrop becomes much better than a normal ad optimizer.

Imagine we have never sold:

> Mitsubishi heat-pump Wi-Fi controllers in Finland.

But we've run:

- Finnish heat-pump products;
- Swedish heat-pump products;
- Finnish technical replacement products;
- Swedish controller products;
- Norway HVAC replacement products.

A hierarchical model can partially pool all of these.

So before campaign #1, it may already know:

$$
P(CVR \mid FI, heatpump, replacement, technical, exact-query)
$$

much better than a generic ecommerce prior.

That is the huge synergy between country intelligence and live commerce data.

---

## 25. Don't train one "winner model"

Train a causal/economic model stack.

Eventually I'd want:

| Model | Target |
|---|---|
| Gate model | `P(supplier/economics gates pass)` |
| CPC model | distribution of CPC |
| CTR model | `P(click | impression)` |
| CVR model | `P(order | qualified click)` |
| contribution model | CM0/order |
| return model | `P(return | sale)` |
| traffic model | reachable qualified clicks |
| campaign model | `P(CM2_30 > 0)` |
| profit model | `E[CM2_30]` |
| downside model | CM2 p10/CVaR |
| research model | `P(action changes decision)` |
| EVI model | value of resolving unknown |
| policy model | best next action |

The final `P(profitable)` should emerge from the components.

That gives you explanations.

---

## 26. Outcome maturity needs to be first-class

A sale isn't final profit.

You need:

```
CM2_1d
CM2_7d
CM2_30d
CM2_60d
CM2_90d
```

because:

```
day 0  purchase
day 12 return
day 17 refund
day 35 warranty
```

Google Ads itself exposes conversion lag buckets out to long horizons, reinforcing why the interaction date and final conversion outcome can't be treated as instantaneous.

GA4 also updates daily export data for late-arriving events.

Train against **mature labels**, not whatever profit BigQuery showed on day two.

---

## 27. CM2 needs to become an event ledger, not a formula in Markdown

The handover correctly defines CM0–CM3.

But it is mostly documentation today.

Implement:

```
fact_cost_event
```

with:

```
event_id
timestamp
candidate_id
campaign_id
experiment_id

cost_class
cost_subclass

amount
currency
amount_base_currency

supplier_id
agent_id
model_id
api_id

usage_quantity
usage_unit

allocation_method
source_transaction_id
```

Cost classes:

```
COGS
SUPPLIER_SHIPPING
DUTY
PAYMENT_FEE
RETURN
REFUND
WARRANTY
CHARGEBACK

AD_SPEND

LLM_TOKENS
WEB_SEARCH
SCRAPER
DATA_API
IMAGE_GEN
VIDEO_GEN
COMPUTE

DOMAIN
SOFTWARE
HUMAN
SAMPLE
```

Now CM0–CM3 are **SQL views over an immutable ledger**.

Much safer.

---

## 28. Fix the reward contradiction

The documentation currently contains both:

```python
reward = profit + information_gain * 0.1
```

and:

> primary reward = CM2; information/EVI should remain separate.

The second is right.

I would enforce:

$$
terminal\ reward = matured\ CM2
$$

Potentially portfolio policy can eventually optimize CM3.

Information gain is not reward.

It changes whether we choose to **buy information**.

Otherwise agents can learn that research is rewarding in itself and endlessly probe interesting things.

---

## 29. The pipeline I would make canonical

This is the key architecture:

```
COUNTRY PACK / WORLD DATA
         │
         ▼
MARKET OBSERVATIONS
         │
         ▼
POINT-IN-TIME FEATURE SNAPSHOT
         │
         ▼
HYPOTHESIS GENERATOR
         │
         ▼
PRIOR / POSTERIOR ECONOMIC MODEL
         │
         ▼
DECISION EVENT
   ┌─────┴──────────────┐
   │ available actions  │
   │ action probability │
   │ expected EVI       │
   │ expected CM2       │
   └─────┬──────────────┘
         ▼
CAMPAIGN EXPERIMENT
         │
         ├── GOOGLE ADS
         ├── GA4
         ├── ORDERS
         ├── SUPPLIER
         ├── RETURNS
         └── COST LEDGER
         │
         ▼
MATURED CM2 OUTCOME
         │
         ▼
PREDICTION EVALUATION
         │
         ├── forecast error
         ├── calibration
         ├── causal treatment estimate
         ├── posterior update
         └── strategy performance
         │
         ▼
UPDATED PRIORS / POLICY
         │
         └───────────────→ NEXT DECISION
```

That is the core Drop machine.

---

## 30. Backtesting needs to be brutally strict

A campaign-selection model should pass four distinct tests.

### Temporal holdout

Train through month \(T\).

Predict \(T+1\).

Never shuffle future observations backward.

### Leave-country-out

Train excluding Finland.

Predict Finland.

This measures whether standardized country features actually transfer.

### Leave-ecosystem-out

Train excluding heat pumps.

Predict heat pumps.

Measures whether product/market structure generalizes.

### Policy replay

Given only state available at historical decision time:

```
what would Policy V4 have chosen?
```

Compare against what was actually chosen.

For adaptive policies, propensity-aware/off-policy evaluation is required rather than naive outcome comparison.

---

## 31. Preserve every rejected candidate

This is fundamental.

Do not train on:

```
20 campaigns we launched
```

alone.

You need:

```
3,000 discovered
1,200 killed on demand
600 killed on competition
400 killed on supplier
300 killed on economics
100 built
50 advertised
15 profitable
```

Otherwise the model has severe survivorship/selection bias.

The candidate universe at each decision epoch must be snapshotted.

---

## 32. Eventually campaign selection becomes a contextual bandit

Once enough clean data exists:

**Context**

```
country
ecosystem
product
query
supplier
installed-base signals
competition
seasonality
economic posterior
```

**Actions**

```
kill
research X
free list
launch
spend $5
spend $10
change query
change price
change landing page
switch supplier
scale
```

**Reward**

```
matured CM2
```

**Constraint**

```
cash risk
token budget
human effort
supplier/inventory risk
```

Start with Thompson sampling.

Not deep RL.

You already have posterior distributions, so Thompson sampling maps beautifully onto this problem.

---

## 33. Then the "approach probability 1" phenomenon emerges naturally

What will actually happen is not:

```
the model magically knows all stores
```

It will look more like:

```
All discovered opportunities
success rate: 5%

        ↓ filters

research-passed candidates
success rate: 15%

        ↓

economic-gate candidates
success rate: 30%

        ↓

high posterior candidates
success rate: 55%

        ↓

free-signal validated
success rate: 72%

        ↓

paid micro-probe validated
success rate: 86%

        ↓

scale candidates
success rate: 94%
```

That is what you really mean.

Each cheap information layer removes failure mass.

The final campaigns you're willing to scale can approach an extremely high success probability.

But the predictions stay calibrated rather than being artificially forced toward 1.

---

## 34. The really powerful downstream model is "cost to certainty"

You eventually know:

```
candidate X:
P(profitable) 0.48

£0.03 Google query pull
→ expected posterior variance reduction 2%

£0.12 merchant crawl
→ 8%

£0.08 supplier API check
→ 13%

£0.40 dealer outreach
→ 31%

£5 paid experiment
→ 44%
```

Now agents learn:

> **What is the cheapest sequence of actions that pushes a candidate above the scale threshold or below the kill threshold?**

That is an extremely powerful optimization problem.

It is not simply dropshipping anymore.

It is sequential capital-efficient hypothesis resolution.

---

## 35. Concrete repo changes I would make now

In order:

1. **Declare one canonical code path.** Move/deprecate old scoring, allocation and pipeline implementations; prevent them from writing production data.

2. **Fix `storage/bigquery.py` parameterization** and add integration tests against BigQuery syntax.

3. **Create one temporal evidence contract** with `event_time`, `published_at`, `observed_at`, `available_at`, `ingested_at`.

4. **Replace multiple missingness conventions** with one typed observed/estimated/unknown representation.

5. **Replace the current generic hypothesis vote with two layers:** qualitative ResearchHypothesis + quantitative EconomicBelief.

6. **Repair `unified_scorer`**, including explicit clicks/orders records, positive conversions, imports, observation weights and tested wiring to Bayesian v2.

7. **Make `bayesian_v2` genuinely hierarchical.** Initially learn empirical priors offline from country × product archetype × intent; later fit hierarchical logistic/Bayesian models.

8. **Delete runtime use of `bayesian.py` v1.** One inference implementation only.

9. **Replace `funnel_classifier` pseudo-posterior calculations** with proper stage-specific posteriors.

10. **Implement `feature_snapshot`, `decision_event`, `campaign_hypothesis`, `experiment_assignment`, `prediction`, `outcome_maturity`, `cost_event`.**

11. **Add action propensity and treatment-assignment probability before autonomous experimentation.**

12. **Expand Google Ads ingestion** to campaign/query/device/geo/auction/conversion-lag level; activate daily Ads→BigQuery and GA4→BigQuery.

13. **Join orders, supplier invoices, refunds and compute/API costs into the economic ledger.**

14. **Build calibration + replay CI tests** before allowing policy models to control larger budgets.

That is the sequence I would give the coding agent.

---

## The most important principle

Every actual paid click from this point forward should eventually be traceable backward to:

```
WHY DID WE BUY THIS CLICK?

country snapshot
↓
market state
↓
hypothesis
↓
feature vector
↓
economic prediction
↓
policy
↓
chosen action
↓
campaign configuration
↓
search term
↓
click
```

and forward to:

```
WHAT ECONOMIC CONSEQUENCE DID IT HAVE?

session
↓
funnel state
↓
purchase
↓
COGS
↓
shipping
↓
refund/return
↓
agent/API cost
↓
mature CM2
```

Once you have that chain, **every dollar becomes a labeled training example**.

That is the point at which the vision becomes real.

The destination isn't a model saying "Davis Norway = 83/100."

It is a calibrated statement like:

> **Given the market state known on September 7, this campaign configuration has a 78% posterior probability of positive 30-day CM2, expected CM2 of NOK 2,140, p10 loss of NOK 610, with 63% of predictive uncertainty attributable to CVR and 24% to supplier margin. The highest-EVI next action is dealer-price verification; expected cost NOK 3.40-equivalent and expected decision value NOK 186.**

Then the campaign runs.

Thirty or sixty days later Drop grades that prediction.

After enough such predictions across products and countries, it learns **which observable structures actually predict money**.

That is the system capable of making the success rate of *selected* campaigns approach very high levels.
