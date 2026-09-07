# Drop Thesis Testing — ML + BigQuery Integration Log

*Generated: 2026-09-07*

---

## BigQuery Tables (53 total)

### Populated Tables (with data)
| Table | Rows | Purpose |
|-------|------|---------|
| country_data | 1,661 | Country market data |
| country_graph_nodes | 80 | Country graph nodes |
| country_graph_edges | 239 | Country graph relationships |
| products | 75 | Product catalog |
| dropintel_signals | 653 | Intelligence signals |
| dropintel_crossref | 47 | Cross-references |
| sources | 52 | Data sources |
| information_sources | 9 | Info sources |
| x_accounts | 12 | X/Twitter accounts |
| operator_events | 21 | Operator events |
| opportunities | 8 | Opportunities |
| graph_nodes | 27 | Graph nodes |
| graph_edges | 20 | Graph edges |
| graph_observations | 7 | Graph observations |
| case_studies | 12 | Case studies |
| competitor_data | 7 | Competitor data |
| experiments | 5 | Experiments |
| probe_reports | 5 | Probe reports |
| probe_mechanisms | 3 | Probe mechanisms |
| probe_timeseries_v2 | 3 | Probe time series |
| probes_v2 | 1 | Probes |
| fact_market_observation | 42 | Market observations |

### Empty Tables (schema ready, no data)
- dim_country, dim_ecosystem, dim_product, dim_merchant, dim_supplier
- fact_cost_ledger, fact_decision_event, fact_economic_outcome
- fact_series_installed_base, fact_series_price, fact_series_search
- ml_predictions, keyword_data, popular_products
- demand_signals, competition_signals, economics_signals, supply_signals

---

## ML Capabilities Available

### 1. Profit Predictor (LOGISTIC_REG)
```sql
CREATE OR REPLACE MODEL `drop.profit_predictor`
OPTIONS(model_type='LOGISTIC_REG', input_label_cols=['reached_profit'])
AS SELECT
  installed_base, merchant_gap_score, cpc, cvr, aov, gross_margin, reached_profit
FROM `drop.campaign_outcomes`
WHERE reached_profit IS NOT NULL
```
**Use for:** Agentic Broker — predict which leads will convert

### 2. CPC Forecaster (ARIMA_PLUS)
```sql
CREATE OR REPLACE MODEL `drop.cpc_forecaster`
OPTIONS(model_type='ARIMA_PLUS', time_series_timestamp_col='observed_at', time_series_data_col='cpc')
SELECT observed_at, cpc, country_code
FROM `drop.keyword_metrics`
WHERE cpc IS NOT NULL
```
**Use for:** Compatibility Dropship — predict product pricing trends

### 3. Installed Base Growth (TimesFM)
```sql
SELECT * FROM ML.FORECAST(
  MODEL `drop.installed_base_model`,
  STRUCT(12 AS horizon, 0.8 AS confidence_level)
)
```
**Use for:** Installed-Base Graph — forecast demand by ecosystem

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
**Use for:** Photo-to-PO — find visually similar parts

### 5. Merchant Quality Scorer (AI.GENERATE)
```sql
SELECT
  merchant_id,
  AI.GENERATE(
    CONCAT('Score 0-10: image_quality, decision_support, shipping_clarity, trust. ', page_content),
    connection_id => 'gemini'
  ) as quality_score
FROM `drop.merchant_pages`
```
**Use for:** Supplier OS — score contractor quality

### 6. Anomaly Detection
```sql
CREATE MODEL `drop.anomaly_detector`
OPTIONS(model_type='ANOMALY_DETECTOR', time_series_timestamp_col='ts', time_series_data_col='value')
SELECT ts, value FROM `drop.time_series_data`
```
**Use for:** Verification Trust Graph — detect unusual supplier behavior

---

## How ML Maps to Theses

### 01_agentic_broker
- **Profit Predictor:** Score leads before sending to contractors
- **Anomaly Detection:** Detect unusual quote patterns
- **Data needed:** lead_source, job_type, postcode, contractor_acceptance_rate, conversion

### 02_compatibility_dropship
- **Product Similarity:** Find visually similar parts from photos
- **CPC Forecaster:** Predict pricing trends
- **Data needed:** product_embeddings, compatibility_graph, supplier_prices

### 03_photo_to_po
- **Product Similarity:** Identify parts from photos
- **Merchant Quality Scorer:** Score wholesale suppliers
- **Data needed:** part_photos, oem_numbers, supplier_inventory

### 04_supplier_os
- **Merchant Quality Scorer:** Score contractor quality
- **Anomaly Detection:** Detect unusual booking patterns
- **Data needed:** contractor_profiles, job_outcomes, customer_reviews

### 05_service_skus
- **Product Similarity:** Map service SKUs to product SKUs
- **Profit Predictor:** Predict service profitability
- **Data needed:** service_definitions, pricing, duration

### 06_api_virtualization
- **Anomaly Detection:** Detect when API responses are stale
- **Data needed:** api_responses, whatsapp_responses, response_times

### 07_installed_base_graph
- **Installed Base Growth:** Forecast demand by ecosystem
- **TimesFM:** Zero-shot demand prediction
- **Data needed:** installed_base_series, failure_rates, replacement_cycles

### 08_verification_trust_graph
- **Anomaly Detection:** Detect unusual supplier behavior
- **Profit Predictor:** Predict supplier reliability
- **Data needed:** job_outcomes, price_accuracy, time_accuracy

### 09_grants_compliance
- **Profit Predictor:** Predict grant eligibility
- **Data needed:** grant_rules, customer_eligibility, property_eligibility

---

## Next Steps

1. **Populate empty tables** with data from country packs, probes, case studies
2. **Create ML models** for each thesis
3. **Build embeddings** for product similarity
4. **Set up anomaly detection** for trust graph
5. **Create forecasting models** for installed base growth

---

## Data Collection Scripts

- `thesisTesting/collect_data.py` — Phase 1: General statistics
- `thesisTesting/collect_data_v2.py` — Phase 2: Thesis-specific queries
- `thesisTesting/collect_data_v3.py` — Phase 3: New thesis queries

Each script queries BigQuery and attaches data to thesis JSONs.
