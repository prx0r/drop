# The Protocol Architecture

*The repo is the protocol. BigQuery is the graph. Agents are the execution layer.*
*Generated: 2026-09-08T08:30:00Z*

---

## The Key Insight

The user is right:

> **BigQuery is the graph. The repo stays messy and quantitative on purpose.**

The repo is not a polished product. It's the **source code, configuration, and intelligence** that tells agents what to do. The graph (BigQuery) is the living, queryable, time-series-enabled knowledge store.

### The Three Layers

```
┌─────────────────────────────────────────────┐
│           AGENT EXECUTION LAYER             │
│  (probes, emails, store builds, data pulls) │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────┴──────────────────────────┐
│           REPO PROTOCOL LAYER               │
│  (rules, schemas, intelligence, code)       │
│  - AGENTS.md (what to do)                   │
│  - active/ (what's happening)               │
│  - schemas/ (JSON, not markdown)            │
│  - services/ (code that does things)        │
│  - countries/ (market intelligence)         │
│  - critique.md (peer review)                │
│  - GOLD_REGISTRY.md (patterns)              │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────┴──────────────────────────┐
│           BIGQUERY GRAPH LAYER              │
│  (the living, queryable knowledge store)    │
│  - graph_nodes (countries, ecosystems, etc) │
│  - graph_edges (relationships)              │
│  - observations (time-series data)          │
│  - outcomes (store results)                 │
│  - hypotheses (what we're testing)          │
│  - probes_v2 (what we've tested)            │
│  - mechanisms (what we've learned)          │
└─────────────────────────────────────────────┘
```

---

## The Protocol: Rules for Agents

### Rule 1: BigQuery is the Source of Truth

All queryable data lives in BigQuery. The repo stores:
- **Schemas** (JSON, not markdown)
- **Code** (Python scripts that read/write BigQuery)
- **Intelligence** (what we've learned)
- **Configuration** (what to do next)

Never invent data. Never store fake numbers. If you don't know something, it's `null` in BigQuery.

### Rule 2: Schemas Are JSON, Not Markdown

```json
{
  "node_type": "ecosystem",
  "required_fields": ["node_id", "system", "country", "installed_base"],
  "optional_fields": ["growth_rate", "replacement_share", "expected_lifetime"],
  "validation": {
    "installed_base": "must be > 0 if observed",
    "growth_rate": "must be numeric, null if not measured",
    "confidence": "must be 0-1, null if not from authenticated source"
  }
}
```

### Rule 3: Every Observation Has Provenance

```sql
-- Good: source, quality, confidence
INSERT INTO observations VALUES (
  'obs_001', 'ECO_FI_HEAT_PUMP', 'installed_base', 2000000,
  'SULPU', 'official_statistics', 0.85, CURRENT_TIMESTAMP()
)

-- Bad: just a number
INSERT INTO observations VALUES ('obs_001', ..., 2000000, ...)
```

### Rule 4: Scores Are Null Unless Formulaic

```sql
-- Bad
score = 8.8  -- Where did this come from?

-- Good
score = NULL  -- Unless computed from stored metrics via versioned formula
```

### Rule 5: Probes Are Designed to Kill

Every probe must have:
- **Falsification criterion:** "If X happens, hypothesis is false"
- **Stopping rule:** "100 clicks OR 30 days"
- **Cost:** "€0 (free listings)"

### Rule 6: Every Action Has an Outcome

```sql
-- Every probe produces an outcome
INSERT INTO outcomes VALUES (
  'outcome_001', 'probe_001', 'store_001',
  'PROFITABLE', 1500.00, 300.00, 30, 150, 3,
  CURRENT_TIMESTAMP()
)
```

### Rule 7: Learning Updates the Graph

```sql
-- After every outcome, update beliefs
UPDATE hypotheses
SET confidence = CASE
  WHEN (SELECT COUNT(*) FROM outcomes WHERE hypothesis_id = hypotheses.id AND result = 'PROFITABLE') >= 3
  THEN 0.9
  WHEN (SELECT COUNT(*) FROM outcomes WHERE hypothesis_id = hypotheses.id AND result = 'KILLED') >= 2
  THEN 0.1
  ELSE confidence
  END
WHERE status = 'TESTING'
```

---

## Why the Repo Stays Messy

The repo is not a product. It's a **working lab**. It should be:

- **Quantitative** — numbers, not prose
- **Actionable** — every file tells an agent what to do
- **Messy** — experiments fail, data changes, schemas evolve
- **Protocol-driven** — rules, not recommendations

BigQuery is the **polished, queryable, time-series-enabled** store. The repo is the **messy, experimental, evolving** source code.

### What Belongs in the Repo

| Type | Format | Example |
|------|--------|---------|
| Rules | JSON | `schemas/node_types.json` |
| Code | Python | `services/research/hypothesis_generator.py` |
| Intelligence | Markdown + JSON | `output/WINNING_FORMULA.md` |
| Configuration | JSON | `data/hypotheses.json` |
| Registries | Markdown | `active/BLOCKERS.md` |

### What Belongs in BigQuery

| Type | Format | Example |
|------|--------|---------|
| Nodes | Rows | `graph_nodes` (countries, ecosystems, products) |
| Edges | Rows | `graph_edges` (relationships) |
| Observations | Rows | `observations` (time-series data) |
| Outcomes | Rows | `outcomes` (store results) |
| Hypotheses | Rows | `hypotheses` (what we're testing) |
| Probes | Rows | `probes_v2` (what we've tested) |

---

## The Feedback Loop with Google Ads

### When Google Ads Access is Approved

```sql
-- 1. Pull keyword data
INSERT INTO keyword_data
SELECT
  keyword_text as keyword,
  'NO' as country,
  metrics.average_monthly_searches as volume,
  metrics.competition as competition,
  metrics.low_top_of_page_bid_micros / 1000000 as bid_low,
  metrics.high_top_of_page_bid_micros / 1000000 as bid_high,
  CURRENT_TIMESTAMP() as fetched_at
FROM `google-ads-api keyword_plan_ideas`
WHERE customer_id = '3775149829'

-- 2. Update hypotheses with real CPC data
UPDATE hypotheses
SET cpc = (SELECT AVG(bid_high) FROM keyword_data WHERE keyword LIKE '%' || product_name || '%')
WHERE cpc IS NULL

-- 3. Recalculate break-even CVR
UPDATE hypotheses
SET break_even_cvr = cpc / margin
WHERE cpc IS NOT NULL AND margin IS NOT NULL

-- 4. Update graph edges with real demand data
UPDATE graph_edges
SET properties = JSON_SET(properties, '$.search_volume', 
  (SELECT SUM(volume) FROM keyword_data WHERE keyword LIKE '%' || product_name || '%'))
WHERE edge_type = 'HAS_DEMAND'
```

### The Feedback Loop

```
Google Ads Data → BigQuery → Hypothesis Update → Probe Redesign → New Probes → Outcomes → Graph Update
```

### What Changes When We Get Real CPC Data

| Before (estimated) | After (measured) |
|--------------------|------------------|
| CPC = €1.50 (guess) | CPC = €0.85 (Keyword Planner) |
| Break-even CVR = 0.33% | Break-even CVR = 0.19% |
| Headroom = 1.5x | Headroom = 2.6x |
| Decision = "interesting" | Decision = "launch" |

---

## The Dynamic Graph

### What Shifts

The graph is not static. Every probe shifts weights:

```
Before probe:
  ECO_FI_HEAT_PUMP: installed_base=2M, growth=0.63, good_sellers=5

After probe (100 clicks, 3 orders):
  ECO_FI_HEAT_PUMP: installed_base=2M, growth=0.63, good_sellers=5
  + observed_cvr = 3.0%
  + observed_cpc = €0.85
  + headroom = 2.6x
  + P(profitable) = 0.78
```

### What the Agent Does

1. **Queries the graph** → "Which ecosystem has the highest expected information gain?"
2. **Designs a probe** → "Free listing, 14 days, 100 clicks"
3. **Executes the probe** → Collects data
4. **Updates the graph** → New observations, updated beliefs
5. **Selects next probe** → Highest expected information gain

### The RL Target

```python
def reward(outcome):
    profit = outcome["revenue"] - outcome["ad_spend"] - outcome["cogs"]
    information = calculate_information_gain(outcome)
    return profit + information * 0.1
```

The agent maximizes: **expected profit per qualified click + information value**.

---

## The Endgame

After 10,000 observations:
- The graph knows which ecosystems produce profit
- The graph knows which countries have the best channel openness
- The graph knows which product characteristics predict success
- The graph knows which failure patterns to avoid
- Agents run probes autonomously
- New countries added by algorithm
- The asset is the graph, not the stores

**That's the endgame. The stores are experiments. The graph is the asset.**
