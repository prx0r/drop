# GeoDrop v2 — Installed-Base Graph Architecture

*Source: Peer review of v1, 2026-09-08. Major architectural upgrade.*
*Generated: 2026-09-08T02:00:00Z*
*Classification: System architecture revision*

---

## Core Insight

> **GeoDrop v1 is good at "should we launch this named product-market?"**
> **GeoDrop v2 must be good at "which installed-base ecosystem should we investigate first?"**

The asset is not stores. The asset is:

> **A longitudinal graph connecting what populations own, how those populations change, what goes wrong, what people search, what mature markets sell, which solutions are underserved locally, and what happened when we tested commerce against those gaps.**

---

## The v1 → v2 Upgrade

| Component | v1 Grade | v2 Change |
|-----------|----------|-----------|
| Structural-demand discovery | C+ | **Installed-base cohorts + lifecycle modeling** |
| Installed-base modeling | C | **First-class population/age/replacement data** |
| Problem/replacement modeling | C | **First-class failures, maintenance, replacement cycles** |
| Geographic opportunity | C | **Municipality/region/climate as first-class** |
| Source-market oracle | B- | **Machine-driven, not manual** |
| Longitudinal intelligence | B- | **Time-series datasets with deltas** |
| Search-intent generation | B- | **Automated via Keyword Ideas API** |

---

## The New Schema

### `ecosystems.jsonl` — Central Discovery Table

```json
{
  "ecosystem_id": "FI_HEAT_PUMPS",
  "country": "FI",
  "system": "heat_pump",
  "installed_base_current": {"value": 2000000, "stock_definition": "active estimated heat pumps", "source": "SULPU", "date": "2026"},
  "annual_additions": {"series_ref": "series/annual_heat_pump_deliveries_fi.csv"},
  "growth_1y": 0.63,
  "age_cohorts": {"series_ref": "series/heat_pump_age_fi.csv"},
  "replacement_share": 0.33,
  "expected_lifetime": "15-20 years",
  "geography": {"series_ref": "series/heat_pump_by_municipality_fi.csv"},
  "regulatory_drivers": ["energy efficiency mandates", "renovation incentives"],
  "climate_drivers": ["heating degree days", "frost exposure"],
  "confidence": 0.85,
  "sources": ["SULPU", "Statistics Finland PX Data"]
}
```

### `problems.jsonl` — The Missing Object

```json
{
  "ecosystem_id": "FI_HEAT_PUMPS",
  "component": "controller",
  "problem": "wifi_remote_control",
  "trigger_type": "COMPATIBILITY",
  "incidence": "medium",
  "urgency": "medium",
  "seasonality": "winter",
  "affected_cohort": "pre-2020 installations",
  "affected_geography": "all",
  "native_query_seeds": ["panasonic lämpöpumppu wifi", "mitsubishi etäohjain"],
  "solution_categories": ["replacement_controller", "wifi_module", "compatibility_guide"],
  "evidence": ["Reddit discussions", "merchant category depth"]
}
```

### `source_archetypes.jsonl` — Machine-Readable Oracle

```json
{
  "source_country": "SE",
  "ecosystem_id": "FI_HEAT_PUMPS",
  "domain": "shop.sverigepumpen.se",
  "merchant_type": "specialist",
  "brand_count": 8,
  "exact_sku_count": 184,
  "accessory_sku_count": 43,
  "replacement_part_count": 43,
  "compatibility_guides": 11,
  "comparison_pages": 5,
  "selector_tools": 2,
  "repair_service": true,
  "subscription_replenishment": true
}
```

### `series/` — Time-Series Datasets

```text
series/
├── installed_base_by_model_fi.csv
├── annual_deliveries_fi.csv
├── age_cohorts_fi.csv
├── replacement_share_fi.csv
├── search_volume_3m.csv
├── search_volume_12m.csv
├── seller_count_by_product.csv
├── merchant_quality_by_product.csv
├── import_value_by_hs_code.csv
├── price_by_product.csv
└── source_target_delta.csv
```

---

## The Two-Score Architecture

### Stage A: `ECOSYSTEM_DISCOVERY_SCORE` (0-100)

| Dimension | Weight | Source |
|-----------|--------|--------|
| Installed-base magnitude | 20 | National statistics |
| Growth / replacement pressure | 15 | Time-series deltas |
| Problem incidence / urgency | 15 | Insurance data, inspection data, Reddit |
| Native observable search demand | 15 | Keyword Planner, Trends |
| Target merchant/service lag | 15 | Merchant census vs source oracle |
| Mature-source catalogue proof | 10 | Swedish/German merchant audit |
| Localization/geographic advantage | 10 | Language, labour costs, regulations |

**Output:** "Investigate Finnish heat pumps before Finnish golf simulators."

### Stage B: `PRODUCT_MARKET_LAUNCH_SCORE` (0-100)

Existing v1 scoring: demand + merchant gap + economics + supplier + localization + structural demand.

**Output:** "This specific SKU in this specific municipality is launchable."

---

## The Geography Layer

```json
{
  "country": "NO",
  "region": "Innlandet",
  "municipality": "Trysil",
  "postal_prefix": null,
  "ecosystem_id": "NO_HYTTE",
  "brand": null,
  "model": null,
  "component": "water_system",
  "cohort": null
}
```

Derived metrics:
- Leisure-property density
- Frost exposure (from MET Norway Frost API)
- Water-damage incidence (from VASK)
- Power-outage exposure (from NVE/RME)
- Connectivity constraints (from Nkom)
- Distance/remoteness

---

## The Source→Target Delta

The key metric for comparison:

```text
assortment_gap_ratio = source_relevant_skus / target_relevant_skus
merchant_gap_ratio = source_good_merchants / target_good_merchants
content_gap = source_decision_assets - target_decision_assets
problem_demand_density = native_problem_searches / max(1, good_target_merchants)
replacement_pressure = active_installed_base × estimated_replacement_probability
```

---

## The State Machine

```text
COUNTRY → ECOSYSTEM → INSTALLED-BASE COHORTS → PROBLEMS/JOBS/REPLACEMENTS →
NATIVE QUERY FOREST → SOURCE-MARKET ORACLE → SOURCE↔TARGET GAP →
PRODUCT/SKU → SUPPLIER+ECONOMICS → PROBE STORE → REAL OUTCOME → LEARNED GEO MODEL
```

---

## What's New in v2

| Feature | v1 | v2 |
|---------|----|----|
| Discovery dimension | Country-level | Ecosystem-level |
| Installed base | Headline number | Cohorts, age, lifecycle |
| Problems | Ad hoc | First-class object |
| Source oracle | Manual | Machine-driven |
| Geography | Country | Municipality/region/climate |
| Time | Snapshots | Time-series with deltas |
| Search intent | LLM brainstorming | Keyword Ideas API + DataForSEO |
| Scoring | One score | Two scores (discovery + launch) |

---

## Data Sources Added

| Source | Data | Use |
|--------|------|-----|
| MET Norway Frost API | Climate observations by station | Frost exposure per municipality |
| VASK | Insurance water-damage statistics | Real problem incidence |
| NVE/RME | Outage statistics | Power reliability per region |
| Nkom | Broadband/connectivity coverage | Connectivity constraints |
| EPREL | EU product registry | Model/component lookup |
| Brønnøysundregistrene | Norwegian company data | Merchant/service density |
| PRH/YTJ | Finnish company data | Merchant/service density |
| DataForSEO | Keyword ideas, questions, autocomplete | Automated search-intent generation |
| Eurostat Comext | International trade data | Import patterns by HS code |
| UN Comtrade | Global trade data | Bilateral commodity flows |

---

## The Hytte Remote-Risk Index (Example)

```text
leisure_property_density
× frost_exposure
× water_damage_incidence
× power_outage_exposure
× connectivity_constraints
× distance_remoteness
```

Data sources:
- SSB: 484k leisure properties + construction year
- MET Norway Frost API: frost days, min temperatures
- VASK: water-damage incidents by type and region
- NVE/RME: outage frequency per grid company
- Nkom: broadband coverage by municipality

This produces a **proprietary need/risk dataset** that generic ecommerce tools won't have.
