# GoldProbe Schema v2 — Optimized for BigQuery + Hypothesis Generation

*The probe is the atomic unit of market intelligence. Its structure determines what we can learn.*

---

## Design Principles

1. **Every field must be machine-readable** — no prose in data fields
2. **Every value must have provenance** — source, confidence, measurement_type
3. **Time-series ready** — every metric can be tracked over time
4. **Cross-country comparable** — same schema, different values
5. **Hypothesis-linked** — every probe tests specific hypotheses
6. **Falsifiable** — every probe has explicit kill conditions

---

## The Canonical Probe Schema

```json
{
  "meta": {
    "probe_id": "B03_FR_PELLET",
    "batch": "B03",
    "date": "2026-09-07",
    "status": "COMPLETE",
    "score": 8.8,
    "verdict": "INVESTIGATE_NARROW",
    "hypothesis_tested": "H1",
    "agent": "goldprobe-agent-v1"
  },

  "installed_base": {
    "value": 1800000,
    "unit": "pellet_heated_households",
    "stock_definition": "households using pellet heating",
    "measurement_type": "observed",
    "source": "Propellet/ADEME",
    "source_url": "https://...",
    "confidence": 0.9,
    "date": "2023",
    "notes": "1.047M stoves + 180K boilers + 77K inserts",
    "breakdown": {
      "stoves": 1047000,
      "boilers": 180000,
      "inserts": 77000
    }
  },

  "installed_base_timeseries": {
    "series_id": "FR_PELLET_INSTALLED_BASE",
    "frequency": "annual",
    "data_points": [
      {"year": 2020, "value": 1600000, "source": "Propellet"},
      {"year": 2023, "value": 1800000, "source": "Propellet"}
    ]
  },

  "trigger_rate": {
    "annual_replacement_probability": 0.04,
    "annual_maintenance_probability": 1.0,
    "measurement_type": "observed",
    "source": "Legifrance JORFTEXT00004786728",
    "confidence": 0.95,
    "legal_requirement": "maintenance every 12 months",
    "enforcement": "qualified professionals required"
  },

  "spend_data": {
    "currency": "EUR",
    "low_season_service": 135,
    "high_season_service": 156,
    "seasonal_premium_pct": 15.6,
    "saturday_emergency_surcharge_pct": 50,
    "sunday_emergency_surcharge_pct": 100,
    "express_appointment_surcharge_pct": 58,
    "remote_diagnostic": 29,
    "physical_diagnostic": 79,
    "repair_visit": 119,
    "measurement_type": "observed",
    "source": "Docteur Pellet, RDC Confort, Sécu'Flamme",
    "confidence": 0.85,
    "notes": "Listed tariffs, not proven conversion elasticity"
  },

  "channel_openness": {
    "oem_capture_level": "low",
    "fragmented_installers": true,
    "online_parts_mature": true,
    "specialist_catalogue_sku_count": 1520,
    "measurement_type": "observed",
    "source": "French market analysis",
    "confidence": 0.85
  },

  "competitive_landscape": {
    "total_sellers": 50,
    "good_sellers": 12,
    "excellent_sellers": 3,
    "dominant_player": null,
    "fragmentation_score": 0.8,
    "measurement_type": "observed",
    "source": "French market research",
    "confidence": 0.7
  },

  "search_demand": {
    "primary_queries": ["poele granule maintenance", "entretien poele granule", "ramonage granule"],
    "monthly_search_volume": 12000,
    "cpc_estimate_eur": 1.80,
    "competition": "medium",
    "measurement_type": "proxy",
    "source": "Google Keyword Planner",
    "confidence": 0.7
  },

  "supplier_availability": {
    "eu_distributor": true,
    "local_distributor": true,
    "dropship_capable": false,
    "lead_time_days": 3,
    "measurement_type": "observed",
    "source": "Market research",
    "confidence": 0.7
  },

  "regulatory_landscape": {
    "mandatory_maintenance": true,
    "maintenance_interval_months": 12,
    "compliance_requirement": "qualified professionals",
    "penalty_for_non_compliance": null,
    "measurement_type": "observed",
    "source": "Legifrance",
    "confidence": 0.95
  },

  "geographic_distribution": {
    "method": "national",
    "concentration_signal": "rural_areas_higher",
    "data_availability": "limited",
    "municipal_level_data": false,
    "measurement_type": "inferred",
    "source": "Industry reports",
    "confidence": 0.6
  },

  "problem_types": [
    {
      "problem_id": "FR_PELLET_IGNITION",
      "component": "ignition_element",
      "trigger": "FAILURE",
      "urgency": "high",
      "seasonality": "winter",
      "failure_rate_annual": 0.05,
      "typical_cost_eur": 120,
      "measurement_type": "proxy",
      "confidence": 0.7
    },
    {
      "problem_id": "FR_PELLET_PCB",
      "component": "control_board",
      "trigger": "FAILURE",
      "urgency": "critical",
      "seasonality": "winter",
      "failure_rate_annual": 0.02,
      "typical_cost_eur": 350,
      "measurement_type": "proxy",
      "confidence": 0.6
    }
  ],

  "economics": {
    "opportunity_type": "diagnosis_routing",
    "not_just": "parts_retail",
    "key_insight": "Dispatch cost 2.7-4.1x information layer",
    "recommended_action": "Pre-triage + model identification + likely part prediction + technician routing",
    "estimated_revenue_per_lead_eur": 49,
    "estimated_conversion_rate": 0.05,
    "measurement_type": "inferred",
    "confidence": 0.6
  },

  "cross_country_comparison": {
    "FR": {"score": 8.8, "channel_openness": "high", "oem_capture": "low"},
    "AT": {"score": 6.9, "channel_openness": "low", "oem_capture": "high"},
    "IT": {"score": 7.5, "channel_openness": "medium", "regulation_veto": true}
  },

  "new_patterns": [
    {
      "pattern_id": "DISPATCH_COST_DOMINATES",
      "description": "Physical dispatch costs 2.7-4.1x information layer",
      "evidence_source": "B03_FR_PELLET"
    }
  ],

  "falsifiers": [
    {
      "condition": "Generic parts already mature",
      "status": "CONFIRMED",
      "evidence": "1520+ SKUs in French specialist catalogue"
    },
    {
      "condition": "Seasonal premium doesn't convert",
      "status": "UNTESTED",
      "next_test": "Booking/conversion data needed"
    }
  ],

  "next_probe": {
    "probe_id": "B04_SG_AC",
    "rationale": "Remove seasonality variable. Test if high-frequency maintenance alone creates subscription economics.",
    "falsifiers_stored": true
  }
}
```

---

## Killer Additions (What's Missing in Current Probes)

### 1. Time-Series Fields
Every metric should have a `timeseries` companion:
```json
"installed_base_timeseries": {
  "series_id": "FR_PELLET_INSTALLED_BASE",
  "data_points": [{"year": 2020, "value": 1600000}, {"year": 2023, "value": 1800000}]
}
```
This lets BigQuery compute growth rates, seasonality, and trends automatically.

### 2. Competitive Landscape (per probe)
```json
"competitive_landscape": {
  "total_sellers": 50,
  "good_sellers": 12,
  "excellent_sellers": 3,
  "fragmentation_score": 0.8
}
```
Currently we manually count sellers. This should be a standard field.

### 3. Search Demand (per probe)
```json
"search_demand": {
  "primary_queries": ["poele granule maintenance"],
  "monthly_search_volume": 12000,
  "cpc_estimate_eur": 1.80,
  "competition": "medium"
}
```
This is the most actionable field — it tells us what people are actually searching for.

### 4. Supplier Availability (per probe)
```json
"supplier_availability": {
  "eu_distributor": true,
  "local_distributor": true,
  "dropship_capable": false,
  "lead_time_days": 3
}
```
Can we actually source products? This must be explicit.

### 5. Regulatory Landscape (per probe)
```json
"regulatory_landscape": {
  "mandatory_maintenance": true,
  "maintenance_interval_months": 12,
  "penalty_for_non_compliance": "500-5000 EUR"
}
```
Regulation creates demand. This must be tracked.

### 6. Cross-Country Comparison (per probe)
```json
"cross_country_comparison": {
  "FR": {"score": 8.8, "channel_openness": "high"},
  "AT": {"score": 6.9, "channel_openness": "low"},
  "IT": {"score": 7.5, "regulation_veto": true}
}
```
Every probe should compare at least 2-3 countries.

### 7. Problem Types Array (per probe)
Instead of one problem, list all relevant problems with failure rates and costs:
```json
"problem_types": [
  {"problem_id": "IGNITION", "failure_rate_annual": 0.05, "typical_cost_eur": 120},
  {"problem_id": "PCB", "failure_rate_annual": 0.02, "typical_cost_eur": 350}
]
```

### 8. Hypothesis Linkage (per probe)
Every probe must explicitly state which hypothesis it tests:
```json
"hypothesis_tested": "H1",
"falsifiers": [
  {"condition": "...", "status": "CONFIRMED/UNTESTED", "evidence": "..."}
]
```

---

## BigQuery Table Design

### Table: probes
```sql
CREATE TABLE `drop.probes` (
  probe_id STRING,
  batch STRING,
  date DATE,
  status STRING,
  score FLOAT64,
  verdict STRING,
  hypothesis_tested STRING,
  installed_base_value INT64,
  installed_base_unit STRING,
  measurement_type STRING,
  confidence FLOAT64,
  seasonal_premium_pct FLOAT64,
  dispatch_cost_ratio FLOAT64,
  oem_capture_level STRING,
  fragmented_installers BOOLEAN,
  specialist_sku_count INT64,
  search_volume INT64,
  cpc_estimate FLOAT64,
  new_pattern_id STRING,
  next_probe_id STRING
)
PARTITION BY date
CLUSTER BY hypothesis_tested, verdict
```

### Table: probe_timeseries
```sql
CREATE TABLE `drop.probe_timeseries` (
  probe_id STRING,
  series_id STRING,
  date DATE,
  metric_name STRING,
  metric_value FLOAT64,
  source STRING,
  confidence FLOAT64
)
PARTITION BY date
CLUSTER BY probe_id, series_id
```

### Table: probe_problems
```sql
CREATE TABLE `drop.probe_problems` (
  probe_id STRING,
  problem_id STRING,
  component STRING,
  trigger_type STRING,
  urgency STRING,
  failure_rate_annual FLOAT64,
  typical_cost_eur FLOAT64,
  measurement_type STRING,
  confidence FLOAT64
)
```

---

## The Query That Matters

```sql
-- Which probes produced the most useful new patterns?
SELECT 
  p.probe_id,
  p.score,
  p.verdict,
  p.hypothesis_tested,
  COUNT(DISTINCT np.pattern_id) as new_patterns,
  AVG(p.confidence) as avg_confidence,
  MAX(p.installed_base_value) as installed_base
FROM `drop.probes` p
LEFT JOIN `drop.probe_new_patterns` np ON p.probe_id = np.probe_id
WHERE p.status = 'COMPLETE'
GROUP BY p.probe_id, p.score, p.verdict, p.hypothesis_tested
ORDER BY new_patterns DESC, p.score DESC
```

This tells us: **which probes produce the most reusable intelligence?**
