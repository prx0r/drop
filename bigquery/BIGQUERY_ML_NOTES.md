# BigQuery ML Notes — What We Can Do

*Machine learning capabilities for Drop's data*

---

## Available Models

| Model | Use Case | Our Application |
|-------|----------|-----------------|
| `LOGISTIC_REG` | Binary classification | Predict profitable campaigns |
| `LINEAR_REG` | Regression | Predict CPC, CVR, margin |
| `KMEANS` | Clustering | Group similar products/countries |
| `ARIMA_PLUS` | Time series forecasting | Forecast installed base growth |
| `TimesFM` | Foundation model forecasting | Zero-shot demand prediction |
| `BOOSTED_TREE_CLASSIFIER` | Classification | Predict launch success |
| `BOOSTED_TREE_REGRESSOR` | Regression | Predict revenue/profit |
| `MATRIX_FACTORIZATION` | Recommendations | Product recommendations |
| `PCA` | Dimensionality reduction | Feature engineering |

---

## What We Can Build

### 1. Profit Predictor (LOGISTIC_REG)

```sql
CREATE OR REPLACE MODEL `drop.profit_predictor`
OPTIONS(model_type='LOGISTIC_REG', input_label_cols=['reached_profit'])
AS SELECT
  installed_base,
  merchant_gap_score,
  cpc,
  cvr,
  aov,
  gross_margin,
  reached_profit
FROM `drop.campaign_outcomes`
WHERE reached_profit IS NOT NULL
```

**Input:** Installed base, merchant gap, CPC, CVR, AOV, margin
**Output:** P(profitable)

### 2. CPC Forecaster (ARIMA_PLUS)

```sql
CREATE OR REPLACE MODEL `drop.cpc_forecaster`
OPTIONS(
  model_type='ARIMA_PLUS',
  time_series_timestamp_col='observed_at',
  time_series_data_col='cpc'
)
SELECT observed_at, cpc, country_code
FROM `drop.keyword_metrics`
WHERE cpc IS NOT NULL
```

**Input:** Historical CPC data by country
**Output:** Forecasted CPC + confidence intervals

### 3. Installed Base Growth (TimesFM)

```sql
SELECT * FROM ML.FORECAST(
  MODEL `drop.installed_base_model`,
  STRUCT(12 AS horizon, 0.8 AS confidence_level)
)
```

**Input:** Historical installed base by ecosystem
**Output:** 12-month forecast with confidence

### 4. Product Similarity (Embeddings)

```sql
CREATE TABLE `drop.product_embeddings` AS
SELECT
  product_id,
  AI.GENERATE_EMBEDDING(
    CONCAT(product_name, ' ', category, ' ', features),
    connection_id => 'gemini'
  ) as embedding
FROM `drop.products`

-- Vector search for similar products
SELECT * FROM vector_search(
  TABLE `drop.product_embeddings`, 'embedding',
  (SELECT embedding FROM `drop.product_embeddings` WHERE product_id = 'TARGET'),
  top_k => 10
)
```

### 5. Merchant Quality Scorer (AI.GENERATE)

```sql
SELECT
  merchant_id,
  AI.GENERATE(
    CONCAT('Score 0-10: image_quality, decision_support, shipping_clarity, trust. ',
           'Merchant: ', merchant_name, '. Products: ', product_count),
    connection_id => 'gemini'
  ) as quality_score
FROM `drop.merchants`
```

### 6. Cross-Country Transfer (KMEANS)

```sql
CREATE OR REPLACE MODEL `drop.country_clusters`
OPTIONS(model_type='KMEANS', num_clusters=5)
AS SELECT
  gdp_per_capita,
  ecommerce_penetration,
  cross_border_rate,
  vat_rate,
  population
FROM `drop.country_profiles`
```

---

## ML Pipeline for Drop

```
1. DATA COLLECTION
   → observations, case_studies, outcomes
   ↓
2. FEATURE ENGINEERING
   → installed_base, merchant_gap, cpc, cvr, aov, margin
   ↓
3. MODEL TRAINING
   → logistic_reg (profit prediction)
   → arima_plus (CPC forecasting)
   → timesfm (demand forecasting)
   ↓
4. MODEL EVALUATION
   → ML.EVALUATE (accuracy, precision, recall)
   ↓
5. PREDICTION
   → ML.PREDICT (new candidates)
   ↓
6. FEEDBACK
   → outcomes → retrain models
```

---

## What's Immediately Useful

| Model | Data Needed | Timeline | Value |
|-------|-------------|----------|-------|
| Profit Predictor | 20+ campaign outcomes | 2 weeks | HIGH |
| CPC Forecaster | 3 months keyword data | 1 week | HIGH |
| Installed Base Growth | Historical installed base | 1 week | MEDIUM |
| Product Similarity | Product catalog | 1 day | MEDIUM |
| Merchant Quality | Product pages | 1 week | MEDIUM |

---

## The Killer Feature

**TimesFM** — Zero-shot forecasting.

We don't need 3 months of historical data to forecast demand. TimesFM can forecast from a single observation.

This means:
- New product? Forecast demand immediately.
- New country? Forecast CPC without historical data.
- New ecosystem? Forecast installed base growth.

That's the foundation model advantage.
