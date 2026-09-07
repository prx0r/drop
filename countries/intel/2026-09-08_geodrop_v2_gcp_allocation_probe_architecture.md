# GeoDrop v2 — GCP Allocation, Store Probe Architecture, and Commerce Observation Factory

*Source: Deep system review, 2026-09-08. Comprehensive architecture revision.*
*Generated: 2026-09-08T02:30:00Z*
*Classification: System architecture revision — GCP allocation, probe design, dataset strategy*

---

## Core Insight

> **The most valuable thing Google Cloud can buy us is not product descriptions. It is orders of magnitude more observations.**

---

## GCP Allocation (Revised)

| Use | Share | Why |
|-----|-------|-----|
| Market observation / crawling compute | 40-50% | The observation factory is the moat |
| Raw snapshot + screenshot archive | 10-15% | Historical observations are unrepeatable |
| Multimodal merchant-quality scoring | 15-20% | Gemini for structured merchant audit |
| Product/spec normalization | 5-10% | Deterministic extraction first |
| Experimental models / analysis | 5-10% | BigQuery ML on labeled outcomes |
| Contingency | 5-10% | Unexpected needs |

**NOT:** 50% generating Finnish product descriptions. Descriptions are cheap and reproducible later. Historical observations aren't.

---

## The Commerce Observation Factory

```text
PRODUCT UNIVERSE
      ↓
country × SKU queue
      ↓
Cloud Run workers
      ↓
retailer / comparison / supplier observations
      ↓
raw immutable snapshots in Cloud Storage
      ↓
normalized facts in BigQuery
      ↓
candidate scoring
      ↓
probe store
      ↓
impressions / clicks / carts / sales
      ↓
BigQuery
      ↓
learn what predicts actual outcomes
```

---

## The Dataset Schema

### `product`
```text
product_id, brand, model, mpn, gtin, category, sub_category,
specification_vector, release_date, product_complexity, price_band,
physical_size, return_risk, service_risk
```

### `market_observation` (one row per SKU/country/time)
```text
observed_at, product_id, country, currency,
seller_count, good_seller_count,
price_min, price_median, price_max, price_dispersion,
in_stock_count, fast_dispatch_count,
amazon_present, manufacturer_dtc_present,
comparison_rank, popularity_proxy
```

### `merchant` (per seller)
```text
retailer_id, domain, country,
product_count, specialization_depth,
image_quality, pdp_quality, comparison_quality, compatibility_quality,
stock_clarity, shipping_clarity, returns_clarity,
payment_localization, trust_quality, review_strength,
chooser_present, video_present, faq_quality, mobile_quality,
merchant_quality_score
```

### Raw evidence archive
```text
gs://commerce-observatory/
    raw/country/domain/YYYY/MM/DD/
        page.html, metadata.json, screenshot.webp
    normalized/
    derived/
```

---

## Key Metric: SATURATION_VELOCITY

History is more valuable than today's value.

```text
Davis 6252EU × Norway:
  Sep: seller_count=5, good_sellers=1
  Oct: seller_count=6, good_sellers=1
  Nov: seller_count=7, good_sellers=2
```

vs saturating market:
```text
  Sep: 5 sellers → Oct: 9 → Nov: 18 → Dec: 31
```

---

## VISUAL_MERCHANT_GAP

$$
VMG = Demand \times (1 - VisualQuality) \times (1 - VisualDiversity)
$$

Use Gemini Vision at $0.0001/image to embed seller hero images and calculate visual differentiation.

---

## The Store Probe Architecture

### Canonical Template (keep constant between probes)
```text
theme, checkout, analytics, technical SEO, feed structure,
product page skeleton, trust pages, shipping presentation,
AI advisor framework, analytics event schema
```

### Deliberate Variables (change per probe)
```text
product, country, supplier, pricing, merchandising treatment, content strategy
```

### Experiment Schema
```text
experiment_id, candidate_id, store_id,
hypothesis, treatment, control,
started_at, ended_at,
traffic_source, country,
impressions, clicks, sessions, pdp_views, atc, checkout, purchase,
revenue, gross_margin, contribution,
supplier_latency, delivery_latency, refund, return,
result, confidence
```

---

## The Two-Score System

### ECOSYSTEM_DISCOVERY_SCORE (Stage A)
Installed-base magnitude (20) + Growth (15) + Problem incidence (15) + Search demand (15) + Merchant lag (15) + Source proof (10) + Localization (10) = 100

### PRODUCT_MARKET_LAUNCH_SCORE (Stage B)
Existing v1 scoring: demand + merchant gap + economics + supplier + localization

---

## The State Machine

```text
COUNTRY → ECOSYSTEM → INSTALLED-BASE COHORTS → PROBLEMS/JOBS/REPLACEMENTS →
NATIVE QUERY FOREST → SOURCE-MARKET ORACLE → SOURCE↔TARGET GAP →
PRODUCT/SKU → SUPPLIER+ECONOMICS → PROBE STORE → REAL OUTCOME → LEARNED GEO MODEL
```

---

## What NOT to Spend Credits On

- Generating product descriptions (cheap later)
- Generating thousands of blog posts (wrong asset)
- Fine-tuning a model (premature)
- Vector databases everywhere (not needed)
- Always-on Kubernetes/GKE (overengineering)
- Huge Vertex endpoints running continuously (no)
- Training custom vision models (no labels yet)

---

## Information Per Dollar

$$
ROI_{research} = \frac{\text{candidate uncertainty reduced}}{\text{cost}}
$$

- Scrape 10,000 prices for $2: HIGH
- Generate 10,000 descriptions for $2: NEAR ZERO
- Score 10,000 merchant pages for $5: HIGH
- Preserve 6 months of history for $3: EXTREMELY HIGH
- Train fancy model on 30 stores for $20: LOW

---

## Sources

[1] Google Cloud BigQuery pricing
[2] Google Cloud Run pricing
[3] Google Cloud Scheduler pricing
[4] Google Cloud Pub/Sub pricing
[5] Google Cloud Storage pricing
[6] Vertex AI pricing
[7] Cloud Vision pricing
[8] BigQuery ML documentation
[9] Google Cloud free tier
