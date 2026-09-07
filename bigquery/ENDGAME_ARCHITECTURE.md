# The Endgame Architecture

*Dynamic graph with agent-driven probes, profit/economic metrics as RL targets.*
*Generated: 2026-09-08T08:00:00Z*

---

## The Vision

> **A dynamic graph that continually shifts weights as agents run probes, run queries, set up and test hypotheses, using profit and economic metrics as RL targets.**

Not a static dashboard. Not a one-time analysis. A living system that learns from every probe, every sale, every failure — and gets smarter about where to look next.

---

## The Graph Structure

### Countries as Nodes

```sql
-- Countries are first-class nodes in the graph
CREATE TABLE graph_nodes (
  node_id STRING,          -- "COUNTRY_NO", "COUNTRY_FI", etc.
  node_type STRING,        -- "country"
  properties JSON,         -- {code, name, currency, language, ecommerce_penetration, ...}
  confidence FLOAT64,
  source STRING,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
)

-- Ecosystems are child nodes
CREATE TABLE graph_nodes (
  node_id STRING,          -- "ECO_FI_HEAT_PUMP"
  node_type STRING,        -- "ecosystem"
  parent_node STRING,      -- "COUNTRY_FI"
  properties JSON,         -- {system, installed_base, growth_rate, ...}
  ...
)

-- Products are child nodes of ecosystems
CREATE TABLE graph_nodes (
  node_id STRING,          -- "PROD_MITSUBISHI_LN25"
  node_type STRING,        -- "product"
  parent_node STRING,      -- "ECO_FI_HEAT_PUMP"
  properties JSON,         -- {brand, model, category, price_band}
  ...
)

-- Merchants are child nodes of countries
CREATE TABLE graph_nodes (
  node_id STRING,          -- "MERCHANT_KATAIKKO"
  node_type STRING,        -- "merchant"
  parent_node STRING,      -- "COUNTRY_FI"
  properties JSON,         -- {domain, quality_score, specialization}
  ...
)

-- Problems are child nodes of ecosystems
CREATE TABLE graph_nodes (
  node_id STRING,          -- "PROB_HEAT_PUMP_FILTER"
  node_type STRING,        -- "problem"
  parent_node STRING,      -- "ECO_FI_HEAT_PUMP"
  properties JSON,         -- {component, trigger, urgency}
  ...
)
```

### Edges as Relationships

```sql
CREATE TABLE graph_edges (
  edge_id STRING,
  source_node STRING,
  target_node STRING,
  edge_type STRING,        -- HAS_ECOSYSTEM, SOLD_IN, LOCATED_IN, HAS_PROBLEMS, ORACLE_FOR
  weight FLOAT64,
  properties JSON,
  created_at TIMESTAMP
)
```

### The Key Queries

```sql
-- Find opportunities: ecosystems with high installed base + weak merchants
SELECT 
  e.node_id as ecosystem,
  JSON_EXTRACT_SCALAR(e.properties_json, '$.installed_base') as installed_base,
  JSON_EXTRACT_SCALAR(e.properties_json, '$.growth_rate') as growth,
  COUNT(m.node_id) as total_merchants,
  SUM(CASE WHEN CAST(JSON_EXTRACT_SCALAR(m.properties_json, '$.quality_score') AS FLOAT64) >= 70 THEN 1 ELSE 0 END) as good_merchants
FROM graph_nodes e
LEFT JOIN graph_edges ce ON e.node_id = ce.source_node AND ce.edge_type = 'LOCATED_IN'
LEFT JOIN graph_nodes m ON ce.target_node = m.node_id AND m.node_type = 'merchant'
WHERE e.node_type = 'ecosystem'
GROUP BY e.node_id, e.properties_json
HAVING good_merchants < 3
ORDER BY CAST(JSON_EXTRACT_SCALAR(e.properties_json, '$.installed_base') AS INT64) * CAST(JSON_EXTRACT_SCALAR(e.properties_json, '$.growth_rate') AS FLOAT64) DESC

-- Find source → target oracle relationships
SELECT 
  src.node_id as source,
  tgt.node_id as target,
  e.weight as oracle_strength
FROM graph_edges e
JOIN graph_nodes src ON e.source_node = src.node_id
JOIN graph_nodes tgt ON e.target_node = tgt.node_id
WHERE e.edge_type = 'ORACLE_FOR'
ORDER BY e.weight DESC
```

---

## 5 Country Schema Alternatives

### Alternative 1: The Nordic Focus (Current)

```
countries/
├── NO.md (primary probe)
├── FI.md (secondary probe)
├── SE.md (source market)
├── DK.md (clone market)
```

**Strength:** Deep expertise in one region. Shared supplier networks (DistriHUB, ELKO).
**Weakness:** Geographic concentration risk. Same季节ality patterns.

### Alternative 2: The Wealth Corridor

```
countries/
├── NO.md (high AOV, weak specialists)
├── CH.md (highest GDP/capita, trilingual)
├── SG.md (dense, year-round demand)
├── AE.md (high import dependency)
```

**Strength:** Maximum purchasing power per customer.
**Weakness:** Complex customs, VAT, language.

### Alternative 3: The EU Expansion

```
countries/
├── NO.md (primary)
├── FI.md (secondary)
├── HR.md (untapped, low competition)
├── PL.md (large market, low costs)
├── AT.md (DACH gateway)
```

**Strength:** Largest addressable market.
**Weakness:** More competition in mature markets.

### Alternative 4: The Climate-Driven

```
countries/
├── NO.md (cabin heating, frost)
├── FI.md (heat pumps, indoor air)
├── CH.md (alpine, multilingual)
├── AU.md (pool maintenance, cooling)
```

**Strength:** Products tied to climate = predictable demand.
**Weakness:** Seasonality in some categories.

### Alternative 5: The English-First

```
countries/
├── UK.md (largest English market)
├── IE.md (English + low competition)
├── SG.md (English + dense)
├── AU.md (English + climate)
├── NZ.md (English + regulation)
```

**Strength:** No localization cost. Easiest to start.
**Weakness:** Higher competition. Less geographic advantage.

---

## The Feedback Loop Architecture

### Stage 1: Probe → Data

```text
Agent runs probe
  → Collects search volume, CPC, seller count, merchant quality
  → Stores in BigQuery (graph_nodes, graph_edges, observations)
  → Timestamps everything
```

### Stage 2: Data → Hypothesis

```text
BigQuery data
  → Hypothesis generator (reads data, outputs hypotheses)
  → Each hypothesis has: statement, prediction, falsifier, confidence
  → Ranked by expected value
```

### Stage 3: Hypothesis → Probe

```text`
Hypothesis
  → Probe designer (takes hypothesis, designs cheapest test)
  → Output: test type, budget, duration, data targets
  → Agent executes probe
```

### Stage 4: Probe → Outcome

```text`
Probe executes
  → Collects impressions, clicks, conversions, revenue
  → Stores in BigQuery (outcomes table)
  → Calculates actual profit per click
```

### Stage 5: Outcome → Learning

```text`
Outcome data
  → Bayesian updating (Beta-binomial for CVR, normal for CPC/margin)
  → Updates hypothesis confidence
  → Promotes/deprioritizes hypotheses
  → Feeds back to hypothesis generator
```

### Stage 6: Learning → Graph Update

```text`
Updated beliefs
  → Graph node properties updated
  → Edge weights recalculated
  → New opportunities surfaced
  → Next probe selected by highest expected information gain
```

### The Loop

```
Graph → Hypotheses → Probes → Outcomes → Learning → Graph
  ↑                                                              │
  └──────────────────────────────────────────────────────────────┘
```

---

## The RL Target Architecture

### What We Optimize

The system optimizes for **expected profit per qualified click**, not revenue, not ROAS, not impressions.

### The Reward Function

```python
def reward(outcome):
    """Calculate reward for a probe outcome."""
    
    # Direct profit
    profit = outcome["revenue"] - outcome["ad_spend"] - outcome["cogs"]
    
    # Information value (did we learn something?)
    information_value = calculate_information_gain(outcome)
    
    # Total reward
    reward = profit + information_value * 0.1  # Weight information at 10%
    
    return reward
```

### The State Space

```python
state = {
    "ecosystem_id": "ECO_FI_HEAT_PUMP",
    "installed_base": 2000000,
    "growth_rate": 0.63,
    "good_sellers": 5,
    "avg_merchant_quality": 72,
    "demand_score": 80,
    "supplier_quality": 85,
    "channel_openness": "medium",
    "current_profits": 0,
    "total_probes": 0,
    "successful_probes": 0
}
```

### The Action Space

```python
actions = [
    "probe_demand",           # Check search volume, CPC
    "probe_competition",      # Score merchant quality
    "probe_supplier",         # Contact suppliers, get prices
    "probe_economics",        # Calculate margins
    "probe_free_listing",     # Test with $0
    "probe_paid_test",        # Test with $5-10/day
    "launch_store",           # Build and launch
    "scale_store",            # Increase budget
    "kill_candidate",         # Abandon hypothesis
    "explore_new_market",     # Move to next country
]
```

### The Training Signal

After each probe, the agent receives:

```python
signal = {
    "action_taken": "probe_free_listing",
    "cost": 0,
    "impressions": 150,
    "clicks": 12,
    "ctr": 0.08,
    "conversions": 0,
    "revenue": 0,
    "information_value": 0.3,  # We learned something
    "next_action_recommendation": "probe_paid_test",
    "confidence_change": +0.05  # Beliefs updated
}
```

The agent learns: "Free listing gave 12 clicks but 0 conversions. Next step: paid test to see if traffic converts at higher intent."

---

## The Endgame

### Year 1: Prove the Model
- 10 probes across 3 countries
- 3-5 stores launched
- 1-2 profitable stores
- Dataset: 500+ product × country observations
- Hypotheses: 20 confirmed, 30 killed

### Year 2: Scale the Model
- 50 probes across 10 countries
- 15-20 stores live
- 5-8 profitable stores
- Dataset: 5,000+ observations
- ML models trained on outcomes
- Automated probe recommendation

### Year 3: The Compound Machine
- 200 probes across 20 countries
- 50+ stores live
- 15-20 profitable stores
- Dataset: 50,000+ observations
- Graph knows which ecosystems are most profitable
- Agents run probes autonomously
- New countries added by algorithm

### The Asset

Not stores. Not reports. Not code.

> **A dynamic knowledge graph that knows which product × country combinations produce profit, and why. It gets smarter with every probe, every sale, every failure.**

After 10,000 observations, the system knows:
- Which installed-base ecosystems are most profitable
- Which countries have the best channel openness
- Which product characteristics predict success
- Which failure patterns to avoid
- How to allocate $10/day for maximum learning

**That's the endgame. The stores are just experiments emitted by the graph.**
