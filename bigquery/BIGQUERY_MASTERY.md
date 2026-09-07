# BigQuery Mastery — What's Possible

*Complete reference for BigQuery capabilities relevant to Drop Commerce Intelligence.*
*Source: Google Cloud docs (Sep 2026)*

---

## 1. Core Architecture

BigQuery is a **serverless, petabyte-scale data warehouse** with:
- **1 TiB query processing free/month**
- **10 GiB storage free**
- **Batch loading free**
- **On-demand pricing** for queries beyond free tier

### What We Use Now
- Dataset: `drop`
- Tables: 12 (sources, case_studies, products, operator_events, probe_reports, synthesis_reports, competitor_data, experiments, demand_signals, competition_signals, economics_signals, graph_nodes/edges/observations)
- 178+ rows loaded

### What We Can Do

| Capability | How | Cost |
|-----------|-----|------|
| Store unlimited data | BigQuery tables | ~$0.02/GiB/month |
| Run complex SQL | Standard SQL + GQL | Free up to 1 TiB/month |
| Time-series analysis | Partitioned tables + SQL functions | Free up to 1 TiB/month |
| Graph traversal | BigQuery Graph (GQL) | Free up to 1 TiB/month |
| ML models | BigQuery ML | Pay per training slot |
| Embeddings | AI.GENERATE_EMBEDDING | Pay per token |
| Vision analysis | AI.IMAGE | Pay per image |
| Text generation | AI.GENERATE | Pay per token |
| Forecasting | TimesFM, ARIMA_PLUS | Pay per training slot |
| Anomaly detection | AI.GL in BigQuery ML | Pay per training slot |

---

## 2. BigQuery Graph (GA September 2026)

**Native graph in BigQuery** — no separate database needed.

### What It Does
- **GQL (Graph Query Language)** alongside SQL
- **Native graph traversals** without ETL
- **Nodes + edges** modeled directly
- **Combined relational + graph** on single source of truth

### How We Use It
```sql
-- Find ecosystems with installed base > 100K
SELECT node_id, properties_json 
FROM graph_nodes 
WHERE node_type = 'ecosystem'
AND CAST(JSON_EXTRACT_SCALAR(properties_json, '$.installed_base') AS INT64) > 100000

-- Traverse: Country → Ecosystem → Problems
SELECT c.node_id, e.node_id, p.node_id
FROM graph_nodes c
JOIN graph_edges ce ON c.node_id = ce.source_node
JOIN graph_nodes e ON ce.target_node = e.node_id
JOIN graph_edges ep ON e.node_id = ep.source_node
JOIN graph_nodes p ON ep.target_node = p.node_id
WHERE c.node_type = 'country' AND ce.edge_type = 'HAS_ECOSYSTEM' AND ep.edge_type = 'HAS_PROBLEMS'
```

---

## 3. Time Series Analysis

### Functions Available
| Function | Purpose |
|----------|---------|
| `TIMESTAMP_DIFF` | Calculate time differences |
| `DATE_TRUNC` | Group by time period |
| `LAG` / `LEAD` | Compare to previous/next period |
| `FIRST_VALUE` / `LAST_VALUE` | Window functions |
| `PERCENTILE_CONT` | Percentile calculations |
| `RANK` / `DENSE_RANK` | Ranking within groups |
| `GGAP_FILL` | Fill gaps in time series |
| `CHANGES` | Detect changes over time |

### How We Use It
```sql
-- Installed base growth rate by ecosystem
SELECT 
  node_id,
  metric_value as current_base,
  LAG(metric_value) OVER (PARTITION BY node_id ORDER BY observed_at) as prev_base,
  (metric_value - LAG(metric_value) OVER (PARTITION BY node_id ORDER BY observed_at)) / 
   LAG(metric_value) OVER (PARTITION BY node_id ORDER BY observed_at) as growth_rate
FROM graph_observations
WHERE metric_name = 'installed_base'
ORDER BY node_id, observed_at
```

---

## 4. Machine Learning

### Available Models
| Model | Use Case | Input | Output |
|-------|----------|-------|--------|
| `LOGISTIC_REG` | Binary classification | Features | Probability |
| `LINEAR_REG` | Regression | Features | Continuous value |
| `KMEANS` | Clustering | Features | Cluster ID |
| `BOOSTED_TREE_CLASSIFIER` | Classification | Features | Probability |
| `BOOSTED_TREE_REGRESSOR` | Regression | Features | Continuous value |
| `ARIMA_PLUS` | Time series forecasting | Historical series | Forecast + confidence |
| `TIMESFM` | Time series forecasting (foundation model) | Historical series | Forecast |
| `MATRIX_FACTORIZATION` | Recommendations | User-item interactions | Recommendations |
| `PCA` | Dimensionality reduction | Features | Reduced features |

### How We Use It
```sql
-- Predict profitable store launches
CREATE OR REPLACE MODEL `drop.profit_predictor`
OPTIONS(model_type='LOGISTIC_REG', input_label_cols=['reached_profit'])
AS SELECT
  demand_score,
  good_seller_gap,
  margin,
  supplier_quality,
  merchant_gap,
  reached_profit
FROM `drop.outcomes`
WHERE reached_profit IS NOT NULL

-- Predict installed base growth
CREATE OR REPLACE MODEL `drop.growth_forecaster`
OPTIONS(model_type='ARIMA_PLUS', time_series_timestamp_col='observed_at', time_series_data_col='metric_value')
SELECT observed_at, metric_value, node_id
FROM graph_observations
WHERE metric_name = 'installed_base'
```

---

## 5. AI/GenAI Functions

### Available in SQL
| Function | Purpose | Cost |
|----------|---------|------|
| `AI.GENERATE` | Text generation | Pay per token |
| `AI.GENERATE_TABLE` | Structured data generation | Pay per token |
| `AI.GENERATE_EMBEDDING` | Text/image embeddings | Pay per embedding |
| `AI.IMAGE` | Image analysis | Pay per image |
| `AI.ANNOTATE_IMAGE` | Image annotation | Pay per image |
| `AI.TRANSLATE` | Text translation | Pay per token |
| `AI.EXTRACT` | Document extraction | Pay per token |
| `AI.SUMMARIZE` | Text summarization | Pay per token |

### How We Use It
```sql
-- Score merchant quality from product page content
SELECT 
  domain,
  AI.GENERATE(
    CONCAT('Score this product page 0-10 on: image_quality, decision_support, shipping_clarity, trust. Return JSON.', 
           page_content),
    connection_id => 'gemini-connection'
  ) as merchant_score
FROM merchant_pages

-- Generate Norwegian product descriptions
SELECT
  product_id,
  AI.GENERATE(
    CONCAT('Write a product description in Norwegian for: ', product_name, '. Key features: ', features),
    connection_id => 'gemini-connection'
  ) as description_no
FROM products
WHERE country = 'NO'
```

---

## 6. Vector Search / Embeddings

### Available
- `AI.GENERATE_EMBEDDING` — text, image, video embeddings
- Vector indexes for similarity search
- Semantic search on embeddings

### How We Use It
```sql
-- Find similar products across markets
CREATE OR REPLACE TABLE `drop.product_embeddings` AS
SELECT 
  product_id,
  AI.GENERATE_EMBEDDING(product_description, connection_id => 'gemini') as embedding
FROM products

-- Vector search for similar products
SELECT * FROM vector_search(
  TABLE `drop.product_embeddings`, 'embedding',
  (SELECT embedding FROM `drop.product_embeddings` WHERE product_id = 'TARGET'),
  top_k => 10
)
```

---

## 7. Geospatial Analytics

### Available
- Geographic functions (ST_DISTANCE, ST_WITHIN, etc.)
- Raster data analysis
- Grid systems for spatial analysis

### How We Use It
```sql
-- Find merchants near a given location
SELECT 
  merchant_id,
  ST_DISTANCE(
    ST_GEOGPOINT(longitude, latitude),
    ST_GEOGPOINT(10.7522, 59.9139)  -- Oslo
  ) as distance_meters
FROM merchants
WHERE country = 'NO'
ORDER BY distance_meters
LIMIT 10
```

---

## 8. Continuous Queries (Streaming)

### What It Does
- Real-time data processing
- Stream-to-stream joins
- Window aggregation

### How We Use It
```sql
-- Monitor live market observations
CREATE CONTINUOUS QUERY `drop.live_market_monitor`
AS SELECT 
  product_id,
  country,
  COUNT(*) as observation_count,
  AVG(price_median) as avg_price
FROM `drop.graph_observations`
WHERE observed_at > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR)
GROUP BY product_id, country
```

---

## 9. Data Loading

### Methods
| Method | Use Case | Cost |
|--------|----------|------|
| Batch load (CSV/JSON/Parquet) | Large historical data | Free |
| Storage Write API | Streaming inserts | Free up to quota |
| Data Transfer Service | Scheduled imports | Free up to quota |
| Pub/Sub integration | Real-time events | Free up to 10 GiB/month |

### How We Use It
```python
# Load CSV feed to BigQuery
from google.cloud import bigquery

client = bigquery.Client()
table_id = "project-ff2366d2-8fda-4fcb-9ba.drop.products"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
)

with open("products.csv", "rb") as f:
    job = client.load_table_from_file(f, table_id, job_config=job_config)
    job.result()
    print(f"Loaded {job.output_rows} rows")
```

---

## 10. Cost Optimization

### Free Tier
| Resource | Free Allowance |
|----------|----------------|
| Query processing | 1 TiB/month |
| Storage | 10 GiB |
| Batch loading | Unlimited |
| Streaming inserts | 1 GiB/day |

### Cost-Saving Patterns
1. **Partition by date** — reduces scanned bytes
2. **Cluster by country/product** — improves query performance
3. **Use approximate aggregations** — APPROX_COUNT_DISTINCT, APPROX_QUANTILES
4. **Materialized views** — pre-compute common queries
5. **BI Engine** — in-memory acceleration for dashboards

### Our $20/week Budget Allocation
| Use | Estimated Cost | Notes |
|-----|---------------|-------|
| Query processing | $0 (free tier) | 1 TiB free |
| Storage | $0 (free tier) | 10 GiB free |
| BigQuery ML | ~$5 | Forecasting models |
| AI.GENERATE | ~$5 | Merchant scoring |
| Cloud Run | $3 | Data collection jobs |
| Cloud Storage | $2 | Raw evidence archive |
| Compute Engine | $3 | Scheduled scrapers |
| **Total** | **~$16/week** | Under $20 budget |

---

## 11. What We Should Build Next

### Priority 1: Merchant Quality Scoring with AI
```sql
-- Score every merchant page using AI
CREATE TABLE `drop.merchant_scores` AS
SELECT 
  domain,
  country,
  AI.GENERATE(
    CONCAT('Score this merchant 0-10 on: image_quality, decision_support, shipping_clarity, trust, specialization. Return JSON with scores.', page_content),
    connection_id => 'gemini'
  ) as quality_scores
FROM merchant_pages
```

### Priority 2: Installed Base Forecasting
```sql
-- Forecast installed base growth
CREATE OR REPLACE MODEL `drop.installed_base_forecast`
OPTIONS(model_type='ARIMA_PLUS', time_series_timestamp_col='date', time_series_data_col='value')
SELECT date, value, ecosystem_id
FROM installed_base_series
```

### Priority 3: Product Similarity Search
```sql
-- Find similar products across markets
CREATE TABLE `drop.product_embeddings` AS
SELECT product_id, AI.GENERATE_EMBEDDING(description) as embedding
FROM products
```

### Priority 4: Opportunity Scoring
```sql
-- Score every product × country cell
SELECT 
  product_id, country,
  demand_score * (1 - good_seller_count/10) * margin * supplier_quality as opportunity_score
FROM candidates
ORDER BY opportunity_score DESC
```
