# Grounded Build Specs — What We Actually Build

*Combines visionary architecture, frontier research, and actual intel into executable builds.*
*Generated: 2026-09-08T06:00:00Z*

---

## The Principle

**Don't build what sounds impressive. Build what moves the next metric.**

Every build must answer:
1. What metric does this move?
2. What data do we need?
3. What code do we write?
4. What does success look like?
5. What's the kill condition?

---

## BUILD 1: Hypothesis Generator (from HypoGeniC)

### What
A Python script that reads BigQuery data and outputs candidate hypotheses.

### Why
We have 75 products, 7 ecosystems, 27 graph nodes, 25 probe reports. But no automated way to say "given all this data, what should we test next?"

### How
```python
# Read from BigQuery
products = query("SELECT * FROM products WHERE score > 50")
ecosystems = query("SELECT * FROM graph_nodes WHERE node_type = 'ecosystem'")
merchants = query("SELECT * FROM graph_nodes WHERE node_type = 'merchant'")

# For each product × ecosystem × country cell:
for product in products:
    for ecosystem in ecosystems:
        demand = compute_demand(product, ecosystem)
        merchant_gap = compute_merchant_gap(product, ecosystem)
        margin = estimate_margin(product, ecosystem)
        
        # Generate hypothesis
        hypothesis = {
            "statement": f"{product['name']} in {ecosystem['country']} will be profitable if merchant_gap > 50 and margin > 20%",
            "prediction": {"metric": "profit_per_click", "target": 0, "direction": ">"},
            "falsifier": "100 clicks, 0 orders",
            "expected_value": demand * merchant_gap * margin
        }
        
        # Rank by expected value
        hypotheses.append(hypothesis)

# Output ranked hypotheses
hypotheses.sort(key=lambda h: h["expected_value"], reverse=True)
print(json.dumps(hypotheses[:20], indent=2))
```

### Metrics
- **Input:** BigQuery tables (products, ecosystems, merchants, observations)
- **Output:** Ranked list of hypotheses with predictions
- **Success:** Top hypothesis has expected_value > 0.5
- **Kill:** No hypothesis has expected_value > 0.1

### Time: 2 hours to build, runs in seconds

---

## BUILD 2: Probe Generator (from POPPER)

### What
A Python script that takes a hypothesis and outputs the cheapest test.

### Why
We have hypotheses but no systematic way to design the cheapest experiment to test each one.

### How
```python
def design_probe(hypothesis):
    """Design the cheapest test for a hypothesis."""
    
    # What data do we need?
    if "demand" in hypothesis["falsifier"]:
        data_needed = "search_volume, cpc, competitor_count"
        cheapest_source = "Keyword Planner (free with Ads access)"
    
    if "merchant_gap" in hypothesis["falsifier"]:
        data_needed = "seller_count, good_seller_count"
        cheapest_source = "Prisjakt scrape (free)"
    
    if "profit" in hypothesis["falsifier"]:
        data_needed = "clicks, orders, revenue"
        cheapest_source = "Free listings ($0)"
    
    # Design the probe
    probe = {
        "hypothesis_id": hypothesis["id"],
        "test_type": "free_listing",
        "products": hypothesis["products"],
        "country": hypothesis["country"],
        "budget": 0,
        "duration_days": 14,
        "minimum_clicks": 100,
        "stopping_rule": "100 clicks OR 30 days",
        "data_to_collect": ["impressions", "clicks", "ctr", "conversions"],
        "falsification_threshold": 0.5  # P(profitable) < 0.5 = kill
    }
    
    return probe
```

### Metrics
- **Input:** Hypothesis from Build 1
- **Output:** Probe design with budget, duration, data targets
- **Success:** Probe costs $0 and produces interpretable data in 14 days
- **Kill:** Probe requires >$10/day to get signal

---

## BUILD 3: Merchant Quality Scorer (from AI.GENERATE)

### What
A BigQuery SQL query that scores every merchant page using AI.

### Why
We manually scored 8 Norwegian retailers. We need to score 100+ across all markets.

### How
```sql
-- Score merchant pages using AI
CREATE TABLE `drop.merchant_scores` AS
SELECT 
  domain,
  country,
  AI.GENERATE(
    CONCAT(
      'Score this merchant 0-10 on these dimensions: ',
      'image_quality, product_info, decision_support, shipping_clarity, ',
      'stock_availability, localization, reviews, trust, accessories, mobile_speed. ',
      'Return JSON with scores for each dimension. ',
      'Page content: ',
      SUBSTR(page_content, 1, 2000)
    ),
    connection_id => 'gemini-connection'
  ) as quality_scores,
  CURRENT_TIMESTAMP() as scored_at
FROM `drop.merchant_pages`
WHERE page_content IS NOT NULL
```

### Metrics
- **Input:** Merchant pages table (to be populated)
- **Output:** Quality scores for every merchant
- **Success:** Scores correlate with manual audit (r > 0.7)
- **Kill:** AI scores don't predict actual merchant quality

---

## BUILD 4: Installed Base Forecaster (from ARIMA_PLUS)

### What
A BigQuery ML model that forecasts installed base growth.

### Why
We need to predict which ecosystems will have growing aftermarket demand.

### How
```sql
-- Forecast Finnish heat pump installed base
CREATE OR REPLACE MODEL `drop.fi_heat_pump_forecast`
OPTIONS(
  model_type='ARIMA_PLUS',
  time_series_timestamp_col='observed_at',
  time_series_data_col='metric_value',
  auto_arima=TRUE
)
SELECT 
  observed_at,
  metric_value,
  node_id
FROM `drop.graph_observations`
WHERE metric_name = 'installed_base'
  AND node_id = 'ECO_FI_HEAT_PUMP'

-- Generate forecast
SELECT *
FROM ML.FORECAST(
  MODEL `drop.fi_heat_pump_forecast`,
  STRUCT(12 AS horizon, 0.95 AS confidence_level)
)
```

### Metrics
- **Input:** Time-series observations from graph
- **Output:** 12-month forecast with confidence intervals
- **Success:** Forecast RMSE < 10% of actual values
- **Kill:** Model can't capture seasonality or trend

---

## BUILD 5: Product Similarity Search (from Embeddings)

### What
A BigQuery table of product embeddings for similarity search.

### Why
We need to find similar products across markets (e.g., "what's the Finnish equivalent of this Swedish product?")

### How
```sql
-- Generate embeddings for all products
CREATE TABLE `drop.product_embeddings` AS
SELECT 
  product_id,
  AI.GENERATE_EMBEDDING(
    CONCAT(brand, ' ', model, ' ', category, ' ', description),
    connection_id => 'gemini-connection'
  ) as embedding
FROM `drop.products`

-- Vector search for similar products
SELECT 
  p1.product_id,
  p2.product_id as similar_product,
  p2.country as similar_country,
  VECTOR_SEARCH(
    TABLE `drop.product_embeddings`, 'embedding',
    (SELECT embedding FROM `drop.product_embeddings` WHERE product_id = p1.product_id),
    top_k => 5
  ) as similarity_score
FROM `drop.products` p1
WHERE p1.country = 'NO'
```

### Metrics
- **Input:** Products table
- **Output:** Embeddings table + similarity search
- **Success:** Similar products are actually similar (human evaluation)
- **Kill:** Embeddings don't capture product similarity

---

## BUILD 6: Opportunity Scorer (from our existing code)

### What
A Python script that scores every product × country cell using our existing economic model.

### Why
We have the economic model, gates, and scoring engine. We need to run it at scale.

### How
```python
# Read all candidates
candidates = query("SELECT * FROM products")

# Score each candidate
for cand in candidates:
    economics = calculate_economics(cand)
    gates = apply_gates(cand, economics)
    score = calculate_score(cand, economics, gates)
    
    # Update BigQuery
    update(f"""
        UPDATE products 
        SET score = {score['total']},
            headroom = {economics['headroom']},
            break_even_cvr = {economics['break_even_cvr']},
            status = '{"KILLED" if gates["killed"] else "SCORED"}'
        WHERE cand_id = '{cand['cand_id']}'
    """)
```

### Metrics
- **Input:** Products table (75 rows)
- **Output:** Scored products with economics
- **Success:** Top 10 products have score > 60
- **Kill:** No products score > 40 (market is too competitive)

---

## BUILD 7: Continuous Market Monitor (from Continuous Queries)

### What
A BigQuery continuous query that monitors market changes in real-time.

### Why
We need to know when installed base grows faster than merchant coverage — that's the opportunity window.

### How
```sql
-- Monitor installed base vs merchant coverage
CREATE CONTINUOUS QUERY `drop.market_monitor`
AS SELECT 
  ecosystem_id,
  country,
  metric_name,
  metric_value,
  observed_at,
  -- Compare to previous observation
  LAG(metric_value) OVER (
    PARTITION BY ecosystem_id, country, metric_name 
    ORDER BY observed_at
  ) as prev_value,
  -- Calculate growth rate
  (metric_value - LAG(metric_value) OVER (
    PARTITION BY ecosystem_id, country, metric_name 
    ORDER BY observed_at
  )) / NULLIF(LAG(metric_value) OVER (
    PARTITION BY ecosystem_id, country, metric_name 
    ORDER BY observed_at
  ), 0) as growth_rate
FROM `drop.graph_observations`
WHERE observed_at > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
```

### Metrics
- **Input:** Graph observations (continuous)
- **Output:** Real-time growth rates
- **Success:** Detects installed_base growth > merchant_count growth
- **Kill:** No significant growth detected in any ecosystem

---

## BUILD 8: Hypothesis Tracker (from POPPER + Arbor)

### What
A Python script that tracks hypothesis states and makes decisions.

### Why
We have 24 hypotheses. We need to know which are confirmed, which are refuted, and which need more data.

### How
```python
# Load hypotheses
hypotheses = load_json("/root/drop/data/hypotheses.json")

# For each hypothesis, check outcomes
for h in hypotheses:
    outcomes = query(f"""
        SELECT result, COUNT(*) as cnt
        FROM outcomes
        WHERE hypothesis_id = '{h['id']}'
        GROUP BY result
    """)
    
    profitable = sum(o['cnt'] for o in outcomes if o['result'] == 'PROFITABLE')
    killed = sum(o['cnt'] for o in outcomes if o['result'] == 'KILLED')
    total = profitable + killed
    
    # Update status
    if profitable >= 3:
        h['status'] = 'CONFIRMED'
    elif killed >= 2:
        h['status'] = 'REFUTED'
    elif total >= 5:
        h['status'] = 'UNCERTAIN'
    
    # Calculate confidence
    if total > 0:
        h['confidence'] = profitable / total
    else:
        h['confidence'] = 0.5  # Prior

# Save updated hypotheses
save_json("/root/drop/data/hypotheses.json", hypotheses)
```

### Metrics
- **Input:** Hypotheses + outcomes
- **Output:** Updated hypothesis statuses
- **Success:** All hypotheses have status CONFIRMED/REFUTED/UNCERTAIN
- **Kill:** >50% of hypotheses remain UNTESTED after 90 days

---

## The Build Order

| Priority | Build | Time | Moves |
|----------|-------|------|-------|
| 1 | Hypothesis Generator | 2h | "What should we test?" |
| 2 | Probe Generator | 2h | "How should we test it?" |
| 3 | Opportunity Scorer | 1h | "Which products are viable?" |
| 4 | Merchant Quality Scorer | 1h | "Which merchants are weak?" |
| 5 | Installed Base Forecaster | 1h | "Which ecosystems are growing?" |
| 6 | Product Similarity Search | 1h | "What's similar across markets?" |
| 7 | Continuous Market Monitor | 2h | "What's changing right now?" |
| 8 | Hypothesis Tracker | 1h | "What have we learned?" |

**Total: 11 hours of engineering.**

---

## The Loop

```
1. Hypothesis Generator → "Test Finnish heat pump aftermarket"
2. Probe Generator → "Free listings, 14 days, 100 clicks"
3. Store Probe → $0 spend, collect data
4. Outcome Analyzer → Update beliefs
5. Hypothesis Tracker → CONFIRMED/REFUTED/UNCERTAIN
6. Learning Loop → Feed back to Hypothesis Generator
7. Repeat
```

**That's the system. It's buildable today.**
