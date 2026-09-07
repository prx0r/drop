# Canonical Country Schema

*The template for doing one country perfectly. Fill this out completely, then clone for others.*

---

## 1. Country Profile

```json
{
  "country_code": "FI",
  "country_name": "Finland",
  "currency": "EUR",
  "language": "fi",
  "population": 5.5,
  "gdp_per_capita": 55000,
  "ecommerce_market": 7.2,
  "ecommerce_penetration": 0.84,
  "cross_border_rate": 0.80,
  "online_shoppers_30d": 0.86,
  "mobile_shopping_preference": 0.65,
  "consumer_confidence": -3.0,
  "ecommerce_momentum": "strong",
  "localization_advantage": "very_high",
  "nearby_stock_advantage": "high"
}
```

---

## 2. Consumer Behaviour

```json
{
  "checkout_behavior": {
    "preferred_method": "bank_payment_debit",
    "mobile_share": 0.65,
    "abandonment_rate": 0.60,
    "top_abandonment_reason": "shipping_cost",
    "willing_to_pay_for_home_delivery": 0.50,
    "willing_to_pay_for_same_day": 0.40
  },
  "payment_methods": {
    "must_have": ["bank_payment", "mobile_wallet"],
    "nice_to_have": ["klarna", "cards"],
    "local_payment_supported": false
  },
  "delivery_preferences": {
    "preferred_method": "parcel_locker",
    "home_delivery_share": 0.50,
    "paid_for_delivery": 0.63,
    "same_day_willingness": 0.40,
    "key_frustration": "shipping_cost_and_options"
  },
  "cross_border_behaviour": {
    "rate": 0.80,
    "top_source_countries": ["SE", "DE", "CN"],
    "trend": "shifting toward nearby (SE, DE)",
    "temu_trend": "declining",
    "preference": "nearby for speed/returns/trust"
  },
  "circular_economy": {
    "second_hand_buyers_monthly": 0.33,
    "participation_rate": 0.50,
    "popular_categories": ["clothing", "electronics", "furniture"],
    "implication": "parts/accessories/maintenance > generic durables"
  },
  "social_commerce": {
    "social_influences_purchases": 0.50,
    "search_on_social_under30": 0.43,
    "bought_on_social": 0.25,
    "bought_on_social_under30": 0.38,
    "korean_beauty_trial_young_women": 0.50
  }
}
```

---

## 3. Structural Markets

```json
{
  "installed_base_ecosystems": [
    {
      "system": "heat_pump",
      "installed_base": 2000000,
      "annual_deliveries": 112000,
      "h1_2026_growth": 0.63,
      "replacement_share": 0.33,
      "dominant_type": "air_to_air",
      "aftermarket_opportunity": "very_high",
      "query_clusters": ["controller", "filter", "thermostat", "remote", "maintenance", "replacement_part", "cleaning", "drainage"]
    },
    {
      "system": "ev_vehicle",
      "installed_base": 1000000,
      "new_ev_share": 0.978,
      "aftermarket_opportunity": "very_high",
      "chinese_brand_share": 0.114,
      "query_clusters": ["charging", "cable", "adapter", "winter", "cabin", "load_management", "outdoor_mount"]
    },
    {
      "system": "cabin",
      "installed_base": 484108,
      "ownership_rate": 0.765,
      "aftermarket_opportunity": "very_high",
      "query_clusters": ["frost_protection", "remote_monitor", "water_leak", "moisture", "air_quality", "heating", "power", "connectivity", "security"]
    },
    {
      "system": "radon_monitoring",
      "measurement_rate": 0.23,
      "deaths_per_year": 300,
      "regulation_active": true,
      "aftermarket_opportunity": "high",
      "query_clusters": ["radonmåler", "radon_sensor", "radon_tiltak", "radon_kjeller", "radon_hytte"]
    },
    {
      "system": "indoor_air",
      "measurement_rate": 0.23,
      "products": ["radon", "co2", "humidity", "particulate", "ventilation", "mold"],
      "aftermarket_opportunity": "high",
      "query_clusters": ["luftkvalitet", "co2_måler", "fuktighet", "ventilasjon", "mold"]
    }
  ]
}
```

---

## 4. Demand Layer

```json
{
  "search_data": {
    "source": "google_keyword_planner",
    "status": "pending",
    "queries_to_run": [
      "heat pump controller",
      "heat pump remote",
      "heat pump filter",
      "radonmåler",
      "radon sensor",
      "cabin temperature monitor",
      "water leak detector",
      "ev charger winter",
      "ev charger cabin"
    ]
  },
  "trends_data": {
    "source": "google_trends",
    "status": "pending",
    "queries_to_run": [
      "heat pump",
      "radon",
      "ev charger",
      "cabin smart",
      "indoor air quality"
    ]
  },
  "merchant_center_data": {
    "source": "google_merchant_center",
    "status": "pending",
    "categories_to_check": [
      "heating_cooling",
      "air_quality",
      "smart_home",
      "ev_charging",
      "cabin_equipment"
    ]
  }
}
```

---

## 5. Competition Layer

```json
{
  "competition_sources": [
    {
      "name": "Prisjakt.fi",
      "type": "price_comparison",
      "coverage": "all_categories",
      "data_available": ["seller_count", "prices", "stock", "reviews"],
      "api": true,
      "status": "pending"
    },
    {
      "name": "Google Shopping",
      "type": "marketplace",
      "coverage": "broad",
      "data_available": ["sellers", "prices", "shipping", "reviews"],
      "api": true,
      "status": "pending"
    },
    {
      "name": "Store Leads",
      "type": "store_census",
      "coverage": "shopify_stores",
      "data_available": ["store_count", "category", "platform", "apps"],
      "api": true,
      "status": "pending"
    }
  ],
  "seller_quality_scoring": {
    "dimensions": [
      "image_quality",
      "product_info",
      "decision_support",
      "shipping_clarity",
      "stock_availability",
      "localization",
      "reviews",
      "trust",
      "accessories",
      "mobile_speed"
    ],
    "good_seller_threshold": 70,
    "methodology": "manual audit of top 10 sellers per product category"
  }
}
```

---

## 6. Supply Layer

```json
{
  "suppliers": [
    {
      "name": "DistriHUB",
      "type": "multi_brand_distributor",
      "coverage": "eu_wide",
      "products": ["dreame", "roborock", "philips", "xiaomi"],
      "dropship": true,
      "moq": 0,
      "min_order_value": 300,
      "delivery_days": 3,
      "status": "email_sent",
      "contact": "hello@distrihub.eu"
    },
    {
      "name": "ELKO Group",
      "type": "nordic_distributor",
      "coverage": "nordics_baltics",
      "products": ["dreame", "xiaomi", "400_brands"],
      "dropship": false,
      "b2b_webshop": true,
      "status": "email_sent",
      "contact": "info@elkogroup.com"
    },
    {
      "name": "Gandalf Distribution",
      "type": "xiaomi_nordic",
      "coverage": "nordics",
      "products": ["xiaomi_air_purifier", "xiaomi_robot_vacuum"],
      "dropship": false,
      "b2b_webshop": true,
      "status": "email_sent",
      "contact": "info@gandalf.se"
    }
  ],
  "fulfillment": {
    "preferred": "distrihub_dropship",
    "backup": "elko_b2b",
    "local_3pl": "dhl_helsinki_oslo_2026"
  }
}
```

---

## 7. Localization Layer

```json
{
  "language": "fi",
  "currency": "EUR",
  "payment": {
    "must_have": ["mobile_wallet", "bank_payment"],
    "nice_to_have": ["klarna", "cards"],
    "integration": "pending"
  },
  "content_requirements": {
    "product_pages": "finnish",
    "comparison_pages": "finnish",
    "buying_guides": "finnish",
    "customer_service": "finnish",
    "seo_content": "finnish"
  },
  "trust_signals": {
    "local_phone": true,
    "local_address": true,
    "local_reviews": true,
    "return_policy_local": true,
    "warranty_local": true
  }
}
```

---

## 8. Scoring Model

```json
{
  "scoring_rubric": {
    "demand": {
      "weight": 20,
      "signals": ["keyword_volume", "keyword_growth", "best_seller_rank", "pinterest_growth", "import_value"],
      "data_sources": ["google_keyword_planner", "google_trends", "merchant_center", "pinterest"]
    },
    "economics": {
      "weight": 20,
      "signals": ["retail_median", "supplier_cost", "shipping_cost", "vat", "gross_contribution", "break_even_cpc"],
      "data_sources": ["prisjakt", "supplier_quotes", "pricing_calculator"]
    },
    "merchant_gap": {
      "weight": 15,
      "signals": ["good_seller_count", "merchant_quality_score", "decision_support_gap"],
      "data_sources": ["prisjakt", "manual_audit"]
    },
    "installed_base": {
      "weight": 15,
      "signals": ["installed_base_size", "replacement_growth", "aftermarket_maturity"],
      "data_sources": ["national_statistics", "industry_reports"]
    },
    "supply": {
      "weight": 15,
      "signals": ["supplier_available", "delivery_days", "dropship", "stock_level"],
      "data_sources": ["distrihub", "elko", "manufacturer"]
    },
    "localization": {
      "weight": 10,
      "signals": ["content_quality", "local_payment", "local_shipping", "reviews"],
      "data_sources": ["manual_audit", "prisjakt"]
    },
    "barrier_to_entry": {
      "weight": 5,
      "signals": ["foreign_language", "specialist_knowledge", "technical_complexity"],
      "data_sources": ["manual_assessment"]
    }
  },
  "kill_rules": [
    "break_even_cvr > 0.03",
    "headroom < 1.0",
    "gtin_sellers > 20",
    "delivery_days > 7",
    "no_eu_supplier",
    "b2b_complexity",
    "content_gap_only_no_merchant_gap"
  ],
  "score_interpretation": {
    "80_100": "LAUNCH",
    "60_79": "INVESTIGATE",
    "40_59": "MONITOR",
    "0_39": "KILL"
  }
}
```

---

## 9. Hypotheses

```json
{
  "hypotheses": [
    {
      "id": "FI-HP-001",
      "category": "heat_pump_aftermarket",
      "statement": "Finnish heat pump replacement parts/accessories are underserved online",
      "metric": "good_seller_count",
      "target": "<3",
      "direction": "<",
      "window_days": 14,
      "budget": 0,
      "failure_criteria": "good_seller_count >= 5 OR search_volume < 100/month"
    },
    {
      "id": "FI-HP-002",
      "category": "heat_pump_aftermarket",
      "statement": "Heat pump controller compatibility guide converts better than product listings",
      "metric": "cvr",
      "target": ">1.5%",
      "direction": ">",
      "window_days": 30,
      "budget": 50,
      "failure_criteria": "cvr < 0.5% after 100 clicks"
    },
    {
      "id": "FI-AQ-001",
      "category": "indoor_air_quality",
      "statement": "Finnish indoor air quality market has merchant gap",
      "metric": "good_seller_count",
      "target": "<4",
      "direction": "<",
      "window_days": 14,
      "budget": 0,
      "failure_criteria": "good_seller_count >= 6"
    },
    {
      "id": "FI-EV-001",
      "category": "ev_aftermarket",
      "statement": "Finnish EV aftermarket accessories are underserved",
      "metric": "good_seller_count",
      "target": "<5",
      "direction": "<",
      "window_days": 14,
      "budget": 0,
      "failure_criteria": "good_seller_count >= 8"
    }
  ]
}
```

---

## 10. Launch Plan

```json
{
  "phase_1_validate": {
    "duration_days": 14,
    "budget": 0,
    "tasks": [
      "Run Keyword Planner for top 50 queries",
      "Score 10 product × country cells",
      "Audit top 10 sellers per cell",
      "Verify supplier availability",
      "Calculate real economics"
    ],
    "decision": "kill or advance top 5 cells"
  },
  "phase_2_build": {
    "duration_days": 7,
    "budget": 200,
    "tasks": [
      "Register domain",
      "Set up Shopify/WooCommerce",
      "Create 10 Finnish product pages",
      "Upload feed to Merchant Center",
      "Enable free listings",
      "Create 5 comparison/buying guide pages"
    ],
    "decision": "launch with free listings"
  },
  "phase_3_test": {
    "duration_days": 30,
    "budget": 150,
    "tasks": [
      "Monitor free listing impressions daily",
      "Track CTR, CVR, AOV",
      "After 100+ clicks: start $5/day paid test",
      "Score hypotheses against targets"
    ],
    "decision": "promote or kill"
  },
  "phase_4_optimize": {
    "duration_days": 30,
    "budget": 150,
    "tasks": [
      "Optimize product feed",
      "A/B test comparison pages",
      "Expand catalog if profitable",
      "Document playbook for replication"
    ],
    "decision": "scale or replicate"
  }
}
```

---

## 11. Metrics Dashboard

```json
{
  "daily_metrics": [
    "impressions",
    "clicks",
    "ctr",
    "cpc",
    "conversions",
    "cvr",
    "revenue",
    "ad_spend",
    "contribution_profit"
  ],
  "weekly_metrics": [
    "total_impressions",
    "total_clicks",
    "avg_ctr",
    "avg_cpc",
    "total_conversions",
    "avg_cvr",
    "total_revenue",
    "total_ad_spend",
    "total_contribution_profit",
    "avg_order_value",
    "return_rate"
  ],
  "monthly_metrics": [
    "organic_traffic_share",
    "paid_traffic_share",
    "email_subscribers",
    "repeat_purchase_rate",
    "customer_satisfaction",
    "supplier_delivery_time"
  ],
  "sources": {
    "traffic": "google_search_console",
    "conversions": "shopify_analytics",
    "ads": "google_ads",
    "revenue": "shopify_payouts",
    "delivery": "distrihub_tracking"
  }
}
```

---

## 12. Replication Checklist

When this country is profitable, clone by:

1. **Copy schema** → change country_code, language, currency
2. **Copy supplier relationships** → DistriHUB works for all Nordics
3. **Copy content templates** → translate to new language
4. **Copy scoring model** → adjust weights for new market
5. **Run demand layer** → Keyword Planner for new country
6. **Run competition layer** → Prisjakt/PriceRunner for new country
7. **Build store** → 7 days with templates
8. **Launch** → free listings first, then paid

**Estimated clone time:** 7-14 days (vs 30+ days for first country)
