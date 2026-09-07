# Visionary Architecture — BigQuery as the Commerce Intelligence Brain

*What becomes possible when you combine BigQuery Graph + BigQuery ML + AI.GENERATE + Time Series + Continuous Queries + Geospatial.*
*Generated: 2026-09-08T05:00:00Z*

---

## The Vision

**One BigQuery dataset that knows more about Nordic ecommerce than any human analyst could gather in a lifetime.**

Not a dashboard. Not a report. A living, queryable intelligence graph that:
1. Knows what every population owns
2. Knows how those populations are changing
3. Knows what goes wrong with those things
4. Knows what people search when it happens
5. Knows what mature markets sell to fix it
6. Knows which solutions are underserved locally
7. Knows what happened when we tested commerce against those gaps

---

## The Architecture

```
                    ┌─────────────────────────────────┐
                    │      BigQuery Commerce Brain     │
                    │                                   │
                    │  ┌─────────┐  ┌──────────────┐  │
                    │  │ Graph   │  │ Time Series  │  │
                    │  │ (GQL)   │  │ (SQL)        │  │
                    │  └────┬────┘  └──────┬───────┘  │
                    │       │              │          │
                    │  ┌────┴──────────────┴──────┐  │
                    │  │    Unified Schema         │  │
                    │  │  (nodes + observations)   │  │
                    │  └────────────┬──────────────┘  │
                    │               │                  │
                    │  ┌────────────┴──────────────┐  │
                    │  │    ML + AI Layer           │  │
                    │  │  (forecasting, scoring,    │  │
                    │  │   embeddings, generation)  │  │
                    │  └────────────┬──────────────┘  │
                    │               │                  │
                    │  ┌────────────┴──────────────┐  │
                    │  │    Decision Engine         │  │
                    │  │  (hypothesis → experiment  │  │
                    │  │   → outcome → learning)    │  │
                    │  └───────────────────────────┘  │
                    │                                   │
                    └─────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
              ┌─────┴─────┐                 ┌───────┴───────┐
              │ Probes    │                 │ Store Probes  │
              │ (discover)│                 │ (validate)    │
              └───────────┘                 └───────────────┘
```

---

## Layer 1: The Knowledge Graph

### Nodes
| Type | What It Represents |
|------|-------------------|
| Country | NO, FI, SE, DK, UK, CH, IE |
| Ecosystem | heat_pump, ev_charger, cabin, wastewater |
| Product | Davis 6242EU, Easee Home, etc. |
| Merchant | BestMarin, Kataikko, etc. |
| Supplier | DistriHUB, ELKO, etc. |
| Problem | frozen_pipe, overheat, septic_fail |
| Probe | B02_FI_VENTILATION, B03_FR_PELLET |
| Outcome | store_001_profitable, store_002_killed |

### Edges
| Type | What It Connects |
|------|-----------------|
| HAS_ECOSYSTEM | Country → Ecosystem |
| SOLD_IN | Product → Country |
| SOLD_BY | Product → Merchant |
| LOCATED_IN | Merchant → Country |
| HAS_PROBLEMS | Ecosystem → Problem |
| ORACLE_FOR | SourceCountry → TargetCountry |
| PRODUCES | Probe → Outcome |
| VALIDATES | Outcome → Hypothesis |

### The Query That Matters
```gql
MATCH (c:Country)-[:HAS_ECOSYSTEM]->(e:Ecosystem)
      -[r:HAS_PROBLEMS]->(p:Problem)
      (e)<-[:LOCATED_IN]-(m:Merchant)
WHERE c.code = 'FI'
  AND m.quality_score < 40
RETURN e.system, p.problem_type, COUNT(m) as weak_merchants
ORDER BY weak_merchants DESC
```

---

## Layer 2: Time Series Intelligence

### What We Track Over Time

| Metric | Frequency | Source |
|--------|-----------|--------|
| Installed base by ecosystem | Annual | National statistics |
| Search volume by product | Monthly | Keyword Planner |
| CPC by product × country | Monthly | Keyword Planner |
| Seller count by product | Weekly | Prisjakt/Hinta.fi |
| Merchant quality scores | Monthly | AI scoring |
| Import values by HS code | Quarterly | Eurostat Comext |
| Price by product × country | Weekly | Prisjakt/Hinta.fi |

### The Time-Series Query
```sql
-- Is Finnish heat pump aftermarket growing faster than merchant coverage?
SELECT 
  o.observed_at,
  o.metric_name,
  o.metric_value,
  LAG(o.metric_value) OVER (PARTITION BY o.node_id ORDER BY o.observed_at) as prev,
  (o.metric_value - LAG(o.metric_value) OVER (PARTITION BY o.node_id ORDER BY o.observed_at)) /
   LAG(o.metric_value) OVER (PARTITION BY o.node_id ORDER BY o.observed_at) as growth_rate
FROM graph_observations o
WHERE o.node_id = 'ECO_FI_HEAT_PUMP'
ORDER BY o.observed_at
```

**If installed_base growth > merchant_count growth → opportunity window is open.**

---

## Layer 3: ML-Powered Scoring

### Forecasting (ARIMA_PLUS / TimesFM)
```sql
-- Forecast Finnish heat pump installed base
CREATE OR REPLACE MODEL `drop.fi_heat_pump_forecast`
OPTIONS(model_type='ARIMA_PLUS', time_series_timestamp_col='date', time_series_data_col='value')
SELECT date, value FROM installed_base_series WHERE ecosystem = 'FI_HEAT_PUMP'
```

### Classification (LOGISTIC_REG)
```sql
-- Predict which probes will be profitable
CREATE OR REPLACE MODEL `drop.probe_profit_predictor`
OPTIONS(model_type='LOGISTIC_REG', input_label_cols=['reached_profit'])
AS SELECT demand_score, good_seller_gap, margin, supplier_quality, channel_openness, reached_profit
FROM outcomes WHERE reached_profit IS NOT NULL
```

### Clustering (KMEANS)
```sql
-- Cluster products by characteristics
CREATE OR REPLACE MODEL `drop.product_clusters`
OPTIONS(model_type='KMEANS', num_clusters=5)
AS SELECT price_band, complexity, return_risk, seasonal FROM products
```

### Embeddings (AI.GENERATE_EMBEDDING)
```sql
-- Find similar products across markets
CREATE TABLE product_embeddings AS
SELECT product_id, AI.GENERATE_EMBEDDING(description) as embedding FROM products
```

---

## Layer 4: AI-Powered Analysis

### Merchant Quality Scoring
```sql
-- Score every merchant page using AI
SELECT domain, country,
  AI.GENERATE(
    CONCAT('Score 0-10: image_quality, decision_support, shipping_clarity, trust. JSON.', content),
    connection_id => 'gemini'
  ) as scores
FROM merchant_pages
```

### Product Description Generation
```sql
-- Generate Norwegian descriptions
SELECT product_id,
  AI.GENERATE(
    CONCAT('Write Norwegian product description for: ', name, '. Features: ', features),
    connection_id => 'gemini'
  ) as description_no
FROM products WHERE country = 'NO'
```

### Installed Base Risk Index
```sql
-- Compute Hytte Remote-Risk Index
SELECT 
  municipality,
  leisure_property_density * frost_exposure * water_damage_incidence * power_outage_exposure 
  as risk_index
FROM norway_municipal_data
ORDER BY risk_index DESC
```

---

## Layer 5: The Decision Engine

### Hypothesis → Experiment → Outcome → Learning

```sql
-- Which hypotheses are supported by evidence?
SELECT 
  h.hypothesis_id,
  h.statement,
  COUNT(CASE WHEN o.result = 'PROFITABLE' THEN 1 END) as profitable_count,
  COUNT(CASE WHEN o.result = 'KILLED' THEN 1 END) as killed_count,
  COUNT(CASE WHEN o.result = 'PROFITABLE' THEN 1 END) * 1.0 / 
    NULLIF(COUNT(*), 0) as success_rate
FROM hypotheses h
LEFT JOIN outcomes o ON h.hypothesis_id = o.hypothesis_id
GROUP BY h.hypothesis_id, h.statement
ORDER BY success_rate DESC
```

### What Probe Should We Run Next?
```sql
-- Find the probe with highest expected information gain
SELECT 
  p.probe_id,
  p.score,
  p.installed_base,
  p.channel_openness,
  (p.installed_base * p.channel_openness * p.search_demand) / 
    NULLIF(p.existing_competition, 1) as expected_value
FROM probe_candidates p
WHERE p.status = 'PENDING'
ORDER BY expected_value DESC
LIMIT 5
```

---

## The Feedback Loop

```
Market Data → BigQuery → Graph → Probes → Stores → Outcomes → Learning
     ↑                                                            │
     └────────────────────────────────────────────────────────────┘
```

### What Makes This Compound

1. **Each probe produces labeled data** — "this product in this country at this time = profitable/killed"
2. **The graph learns which features predict success** — installed_base × channel_openness × demand × margin
3. **The ML models improve** — more data = better predictions
4. **The next probe is smarter** — highest expected information gain, not random
5. **The stores are experiments** — not businesses, but hypothesis tests

### The Asset

Not stores. Not reports. Not code.

> **A longitudinal knowledge graph that learns which geographic-product combinations produce profit, and why.**

After 100 probes, the system knows:
- Which installed-base ecosystems are most profitable
- Which countries have the best channel openness
- Which product characteristics predict success
- Which failure patterns to avoid
- How to allocate $10/day for maximum learning

That's the moat. The stores are just experiments emitted by the graph.

---

## What We Can Build Right Now

### Immediate (This Week)
1. Load all probe JSONs into BigQuery
2. Create time-series views for installed base
3. Build merchant quality scoring with AI.GENERATE
4. Set up continuous queries for live monitoring

### Short-term (This Month)
1. Train LOGISTIC_REG on probe outcomes
2. Build ARIMA_PLUS forecasting for installed base
3. Create product embeddings for similarity search
4. Build automated probe recommendation engine

### Medium-term (This Quarter)
1. Integrate real-time Prisjakt/Hinta.fi data
2. Build conversational analytics agent
3. Create cross-country transfer learning model
4. Launch 10 store probes with full tracking

---

## The Budget

| Use | Weekly | Monthly |
|-----|--------|---------|
| Query processing | $0 (free tier) | $0 |
| Storage | $0 (free tier) | $0 |
| BigQuery ML | $5 | $20 |
| AI.GENERATE | $5 | $20 |
| Cloud Run | $3 | $12 |
| Cloud Storage | $2 | $8 |
| Compute Engine | $3 | $12 |
| **Total** | **$18** | **$72** |

**Under $20/week budget.** Free tier covers the rest.

---

## The Bottom Line

BigQuery is not just a data warehouse. It's:

1. **A graph database** — BigQuery Graph (GQL + SQL)
2. **A time-series database** — partitioned by date, clustered by country
3. **A machine learning platform** — ARIMA, LOGISTIC_REG, KMEANS, embeddings
4. **An AI analysis engine** — AI.GENERATE, AI.IMAGE, AI.GENERATE_EMBEDDING
5. **A real-time streaming platform** — continuous queries
6. **A geospatial analytics platform** — ST_DISTANCE, grid systems

All in one. No separate databases. No ETL. No infrastructure management.

**The architecture is:**
```
Graph + Time Series + ML + AI + Continuous Queries + Geospatial
= Commerce Intelligence Brain
```

That's what becomes possible.
