# Probe Specifications

*Reusable specs for probes that can be swapped in when current probes saturate.*

---

## Spec 1: Market Gap Scanner

```json
{
  "probe_id": "market-gap-scanner",
  "type": "discovery",
  "description": "Scans product × country cells for merchant gaps using Prisjakt/Hinta.fi data",
  "data_sources": ["Prisjakt Partner API", "Hinta.fi", "Google Shopping"],
  "output": "Ranked list of product × country cells with GOOD_SELLER_GAP scores",
  "refresh_frequency": "daily",
  "prerequisites": ["Prisjakt Partner API access"],
  "estimated_novelty": 0.85,
  "estimated_cost": "€0",
  "lifecycle": "initial 20 runs → novelty 0.85, then declining as market is mapped",
  
  "prompt": """
You are a market gap scanner. Your job is to find product × country cells where:
1. Demand exists (product is searched for)
2. Few GOOD sellers exist (not just few sellers)
3. Price dispersion is high (opportunity for margin)

For each cell, compute:
  GOOD_SELLER_GAP = demand × (1 / (1 + good_sellers))
  
Rank cells by GOOD_SELLER_GAP.
Output: Top 20 cells with scores.
""",
  
  "output_schema": {
    "cells": [{
      "product_id": "string",
      "country_code": "string",
      "demand_score": "float",
      "total_sellers": "integer",
      "good_sellers": "integer",
      "price_dispersion": "float",
      "good_seller_gap": "float",
      "confidence": "float"
    }]
  }
}
```

---

## Spec 2: Installed Base Monitor

```json
{
  "probe_id": "installed-base-monitor",
  "type": "monitoring",
  "description": "Tracks installed base growth vs merchant coverage over time",
  "data_sources": ["National statistics", "Industry reports", "Google Trends"],
  "output": "Time-series of installed_base vs merchant_count per ecosystem",
  "refresh_frequency": "monthly",
  "prerequisites": ["None"],
  "estimated_novelty": 0.80,
  "estimated_cost": "€0",
  "lifecycle": "continually fresh — new data every month",
  
  "prompt": """
You are an installed-base monitor. Your job is to track how installed bases grow and how merchant coverage changes.

For each ecosystem:
1. Pull latest installed_base data from national statistics
2. Pull latest merchant_count from Google Shopping / comparison sites
3. Compute growth_rate = (current - previous) / previous
4. Compute gap = installed_base × growth_rate / max(1, merchant_count)
5. Flag ecosystems where gap is increasing (opportunity window)

Output: Time-series update with gap scores.
""",
  
  "output_schema": {
    "ecosystem_id": "string",
    "country_code": "string",
    "observed_at": "timestamp",
    "installed_base": "integer",
    "merchant_count": "integer",
    "growth_rate": "float",
    "gap_score": "float",
    "trend": "increasing | stable | decreasing"
  }
}
```

---

## Spec 3: Price Dispersion Scanner

```json
{
  "probe_id": "price-dispersion-scanner",
  "type": "discovery",
  "description": "Finds products with high price dispersion across markets",
  "data_sources": ["Prisjakt API", "Google Shopping"],
  "output": "Products with high price dispersion = margin opportunity",
  "refresh_frequency": "daily",
  "prerequisites": ["Prisjakt API access"],
  "estimated_novelty": 0.70,
  "estimated_cost": "€0",
  
  "prompt": """
You are a price dispersion scanner. Your job is to find products where the price varies significantly across sellers or markets.

For each product:
1. Pull prices from Prisjakt for all sellers
2. Compute price_dispersion = (max - min) / median
3. Compute margin_opportunity = (median - supplier_cost) / median
4. Flag products with high dispersion AND high margin opportunity

Output: Top 20 products with dispersion scores.
""",
  
  "output_schema": {
    "product_id": "string",
    "country_code": "string",
    "seller_count": "integer",
    "price_min": "float",
    "price_median": "float",
    "price_max": "float",
    "price_dispersion": "float",
    "margin_opportunity": "float"
  }
}
```

---

## Spec 4: Regulatory Compliance Tracker

```json
{
  "probe_id": "regulatory-compliance-tracker",
  "type": "monitoring",
  "description": "Tracks regulatory changes that create/destroy opportunities",
  "data_sources": ["Government websites", "Industry associations"],
  "output": "Alerts on regulatory changes affecting installed base ecosystems",
  "refresh_frequency": "weekly",
  "prerequisites": ["None"],
  "estimated_novelty": 0.75,
  "estimated_cost": "€0",
  "lifecycle": "continually fresh — regulations change periodically",
  
  "prompt": """
You are a regulatory compliance tracker. Your job is to find regulatory changes that affect installed base ecosystems.

For each ecosystem:
1. Check government websites for new regulations
2. Check industry associations for compliance updates
3. Classify: CREATES_OPPORTUNITY | DESTROYS_OPPORTUNITY | NEUTRAL
4. Flag high-impact changes immediately

Output: Regulatory alerts with impact assessment.
""",
  
  "output_schema": {
    "ecosystem_id": "string",
    "country_code": "string",
    "regulation_type": "string",
    "change_description": "string",
    "impact": "CREATES_OPPORTUNITY | DESTROYS_OPPORTENCY | NEUTRAL",
    "confidence": "float",
    "source_url": "string"
  }
}
```
