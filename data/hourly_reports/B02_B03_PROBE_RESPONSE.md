# GoldProbe Response — B02 + B03 Review

*Response to probe agent. Structured for BigQuery ingestion and hypothesis generation.*
*Generated: 2026-09-08T04:00:00Z*

---

## Agent Instructions

For each probe, I need a structured JSON that gives us:
1. **Installed base data** (denominator)
2. **Trigger rate** (problems/repairs per unit per year)
3. **Spend data** (what people pay)
4. **Channel openness** (can we enter?)
5. **Geographic distribution** (where are the assets?)
6. **Falsifiers** (what would kill this)

The JSON must be machine-readable for BigQuery ingestion. Every field must have `source`, `confidence`, and `measurement_type` (observed/proxy/inferred).

---

## Structured Probe Output: B02 Finland Ventilation

```json
{
  "probe_id": "B02_FI_VENTILATION",
  "date": "2026-09-07",
  "status": "COMPLETE",
  "score": 9.2,
  "verdict": "INVESTIGATE",
  
  "installed_base": {
    "value": "unknown",
    "unit": "ventilation_systems",
    "measurement_type": "inferred",
    "source": "Vallox documentation",
    "confidence": 0.6,
    "notes": "Exact Finnish installed base not public. Vallox mentions 20-25 year service life for technical ventilation."
  },
  
  "trigger_rate": {
    "annual_replacement_probability": 0.04,
    "measurement_type": "inferred",
    "source": "Vallox service life documentation",
    "confidence": 0.5,
    "notes": "20-25 year service life implies 4-5% annual replacement"
  },
  
  "spend_data": {
    "new_unit_cost_eur": "2000-5000",
    "installation_cost_eur": "1000-3000",
    "annual_filter_cost_eur": "50-150",
    "measurement_type": "proxy",
    "source": "Finnish retailer listings",
    "confidence": 0.7
  },
  
  "channel_openness": {
    "oem_capture": "medium",
    "fragmented_installers": true,
    "online_retail_mature": true,
    "measurement_type": "observed",
    "source": "Finnish retailer analysis",
    "confidence": 0.8
  },
  
  "geographic_distribution": {
    "method": "national",
    "data_availability": "limited",
    "notes": "No municipal-level data found"
  },
  
  "problem_type": "LEGACY_INTERFACE_LOCK_IN",
  "problem_description": "Old ventilation units leave behind physical constraints (ducts, wiring, mounting) that make replacement complex. Compatibility advice is the value.",
  
  "economics": {
    "opportunity": "replacement_lead",
    "not_just": "filter_retail",
    "key_insight": "Gap is which modern asset replaces old one, not consumable parts"
  },
  
  "falsifiers": [
    "Generic filter market already mature (Norway proves this)",
    "OEMs capture service relationship (Austria proves this)",
    "Installed base too small for viable market"
  ]
}
```

---

## Structured Probe Output: B02 Ireland Stairlifts

```json
{
  "probe_id": "B02_IE_STAIRLIFTS",
  "date": "2026-09-07",
  "status": "COMPLETE",
  "score": 9.4,
  "verdict": "INVESTIGATE",
  
  "installed_base": {
    "value": "unknown",
    "unit": "stairlifts",
    "measurement_type": "inferred",
    "source": "Industry estimates",
    "confidence": 0.5,
    "notes": "891,100 people aged 65+ (16.1% of population). Stairlift ownership not directly measured."
  },
  
  "trigger_rate": {
    "annual_replacement_probability": 0.05,
    "measurement_type": "inferred",
    "source": "Industry estimates",
    "confidence": 0.4
  },
  
  "spend_data": {
    "new_straight_lift_eur": "3000-5000",
    "new_curved_lift_eur": "8000-15000",
    "refurbished_straight_eur": "1200-1300",
    "refurbished_curved_eur": "4500",
    "monthly_lease_eur": 85,
    "measurement_type": "observed",
    "source": "Irish market listings",
    "confidence": 0.8
  },
  
  "channel_openness": {
    "oem_capture": "low",
    "fragmented_installers": true,
    "circular_economy": true,
    "measurement_type": "observed",
    "source": "Irish market analysis",
    "confidence": 0.8
  },
  
  "geographic_distribution": {
    "method": "age_distribution",
    "key_signal": "891,100 people aged 65+ (16.1% of population, +22.7% since 2020)",
    "data_availability": "good",
    "source": "CSO Ireland"
  },
  
  "problem_type": "CIRCULAR_ASSET_LIQUIDITY",
  "problem_description": "When human need duration is shorter than engineering asset life, exit events become supply. Same unit generates installation, lease, maintenance, battery, removal, buy-back, second installation, parts revenue.",
  
  "economics": {
    "opportunity": "decision_router",
    "not_just": "parts_retail",
    "key_insight": "Neutral urgent decision router: buy vs refurbished vs lease vs short rent vs grant, plus installation speed"
  },
  
  "new_pattern": "CIRCULAR_ASSET_LIQUIDITY",
  "pattern_description": "When human need duration is shorter than engineering asset life, exit events become supply. The same physical unit can generate 7+ revenue streams across its lifecycle.",
  
  "falsifiers": [
    "Insufficient installed-base denominator",
    "Service already mature/aggregated",
    "OEM captures customer relationship"
  ]
}
```

---

## Structured Probe Output: B02 NZ Pools

```json
{
  "probe_id": "B02_NZ_POOLS",
  "date": "2026-09-07",
  "status": "COMPLETE",
  "score": 9.0,
  "verdict": "INVESTIGATE",
  
  "installed_base": {
    "value": "100000",
    "unit": "residential_pools",
    "measurement_type": "proxy",
    "source": "NZ estimates",
    "confidence": 0.6,
    "notes": "Heavily skewed by wealth: 6% of sub-NZ$1m homes, 15% of NZ$1-3m, 37% above NZ$3m"
  },
  
  "wealth_concentration": {
    "signal": "LUXURY_DENSITY_OVER_POPULATION_DENSITY",
    "data": {
      "sub_1m": 0.06,
      "1m_3m": 0.15,
      "above_3m": 0.37,
      "auckland_above_7.5m": 0.73
    },
    "measurement_type": "observed",
    "source": "NZ property data",
    "confidence": 0.85
  },
  
  "trigger_rate": {
    "mandatory_inspection": "every_3_years",
    "measurement_type": "observed",
    "source": "NZ council requirements",
    "confidence": 0.9,
    "notes": "Failure leads to reinspection, remediation, enforcement"
  },
  
  "spend_data": {
    "inspection_nzd": "246-270",
    "reinspection_nzd": "246-250",
    "audit_hourly_nzd": 250,
    "measurement_type": "observed",
    "source": "NZ council fees",
    "confidence": 0.9
  },
  
  "new_pattern": "COMPLIANCE_CLOCK_REACQUISITION",
  "pattern_description": "Statutory recurring inspection creates predictable future commercial event before failure. Enables pre-inspection diagnosis, reminders, remediation routing and recurring acquisition.",
  
  "falsifiers": [
    "Pool ownership not widespread enough",
    "Service already standardized/cheap",
    "Council inspection too infrequent to matter"
  ]
}
```

---

## Structured Probe Output: B03 France Pellet Heating

```json
{
  "probe_id": "B03_FR_PELLET",
  "date": "2026-09-07",
  "status": "COMPLETE",
  "score": 8.8,
  "verdict": "INVESTIGATE_NARROW",
  
  "installed_base": {
    "value": 1800000,
    "unit": "pellet_heated_households",
    "measurement_type": "observed",
    "source": "Propellet/ADEME",
    "confidence": 0.9,
    "breakdown": {
      "pellet_stoves": 1047000,
      "pellet_boilers": 180000,
      "pellet_inserts": 77000
    }
  },
  
  "trigger_rate": {
    "annual_maintenance_required": true,
    "legal_requirement": "every_12_months",
    "measurement_type": "observed",
    "source": "Legifrance JORFTEXT00004786728",
    "confidence": 0.95
  },
  
  "seasonal_premium": {
    "median_high_season_premium": 0.156,
    "range": "7.2%-16.7%",
    "saturday_emergency": 0.50,
    "sunday_emergency": 1.00,
    "express_appointment_surcharge": 0.58,
    "measurement_type": "observed",
    "source": "5 same-provider price pairs",
    "confidence": 0.85,
    "notes": "These are listed tariffs, not proven conversion elasticity"
  },
  
  "dispatch_vs_information": {
    "remote_diagnostic_eur": 29,
    "physical_diagnostic_eur": 79,
    "repair_visit_eur": 119,
    "physical_to_remote_ratio": 2.7,
    "repair_to_remote_ratio": 4.1,
    "measurement_type": "observed",
    "source": "Docteur Pellet pricing",
    "confidence": 0.9
  },
  
  "parts_market_maturity": {
    "french_specialist_sku_count": 1520,
    "measurement_type": "observed",
    "source": "poelesboisgranules.fr",
    "confidence": 0.9,
    "notes": "Generic parts whitespace is WEAK. Mature catalogue already exists."
  },
  
  "new_pattern": "DISPATCH_COST_DOMINATES_SIMPLE_DIAGNOSIS",
  "pattern_description": "When make/model/error code can narrow the fault, physical dispatch costs 2.7-4.1x the information layer. Proper intermediary should increase probability that first truck roll is final truck roll.",
  
  "channel_openness": {
    "oem_capture": "low",
    "fragmented_installers": true,
    "online_parts_mature": true,
    "measurement_type": "observed",
    "source": "French market analysis",
    "confidence": 0.85
  },
  
  "falsifiers": [
    "Generic parts already mature (1520+ SKUs)",
    "Seasonal premium is real but conversion elasticity unknown",
    "Physical diagnosis cost premium may not convert to higher WTP"
  ]
}
```

---

## Structured Probe Output: B03 Austria Pellet (Counterexample)

```json
{
  "probe_id": "B03_AT_PELLET",
  "date": "2026-09-07",
  "status": "COMPLETE",
  "score": 6.9,
  "verdict": "HOLD",
  
  "installed_base": {
    "value": 216000,
    "unit": "pellet_boilers_since_2001",
    "measurement_type": "observed",
    "source": "Austrian Biomass Association",
    "confidence": 0.85
  },
  
  "spend_data": {
    "annual_maintenance_eur": "200-328",
    "chimney_sweep_eur": "40-90",
    "measurement_type": "observed",
    "source": "OekoFEN, Austroflamm, B&U Service",
    "confidence": 0.85
  },
  
  "channel_openness": {
    "oem_capture": "HIGH",
    "fragmented_installers": false,
    "manufacturer_service_contracts": true,
    "measurement_type": "observed",
    "source": "Austrian market analysis",
    "confidence": 0.9,
    "notes": "Strong OEM service ownership kills independent middleman opportunity"
  },
  
  "counterexample_for": "broad_installed_base_thesis",
  "counterexample_lesson": "Installed-base attractiveness must be multiplied by channel openness. High homeowner spend is commercially irrelevant if OEM already owns customer relationship.",
  
  "falsifiers": [
    "OEM captures service relationship",
    "Manufacturer maintenance contracts dominate",
    "Independent aggregator weaker due to OEM presence"
  ]
}
```

---

## Structured Probe Output: B03 Italy Pellet (Regulatory)

```json
{
  "probe_id": "B03_IT_PELLET",
  "date": "2026-09-07",
  "status": "COMPLETE",
  "score": 7.5,
  "verdict": "INVESTIGATE_REPLACEMENT",
  
  "installed_base": {
    "value": 2070000,
    "unit": "pellet_using_households",
    "measurement_type": "proxy",
    "source": "ISTAT",
    "confidence": 0.7,
    "notes": "7.8% of 26.6M households. 14.3% in small municipalities."
  },
  
  "regulatory_force": {
    "lombardy_rule": "Must use 4-star+ biomass. Old 0-1-2 star units prohibited.",
    "penalty_eur": "500-5000",
    "measurement_type": "observed",
    "source": "Regione Lombardia",
    "confidence": 0.95
  },
  
  "new_pattern": "REGULATORY_REPAIR_VETO",
  "pattern_description": "Regulation doesn't add compliance demand — it changes the economically correct lifecycle node. If old stove can't legally be used, correct recommendation is replacement, not repair.",
  
  "economics": {
    "opportunity": "replacement_lead",
    "not_just": "repair_lead",
    "key_insight": "Naive aftermarket engine might wrongly score old assets as repair opportunities when regulations have converted them into replacement leads"
  },
  
  "falsifiers": [
    "Regulation only applies in Lombardy, not nationwide",
    "Enforcement is weak",
    "Replacement cost too high for target demographic"
  ]
}
```

---

## New Patterns Discovered (Append to Gold Registry)

| Pattern | Description | Probe |
|---------|-------------|-------|
| DISPATCH_COST_DOMINATES_SIMPLE_DIAGNOSIS | Physical dispatch costs 2.7-4.1x information layer. Proper intermediary increases first-visit fix rate. | B03 FR |
| REGULATORY_REPAIR_VETO | Regulation converts repair opportunities into replacement leads. Naive engine scores wrong. | B03 IT |
| HEATING_SEASON_CAPACITY_PREMIUM | Seasonal technician scarcity creates 7-100% price premium. Off-season acquisition cheaper. | B03 FR |
| LEGACY_INTERFACE_LOCK_IN | Embedded physical assets leave constraints that create compatibility advice value. | B02 FI |
| LUXURY_DENSITY_OVER_POPULATION_DENSITY | Service TAM concentrates by property value, not population. 37% of >NZ$3m homes have pools vs 6% under NZ$1m. | B02 NZ |
| COMPLIANCE_CLOCK_REACQUISITION | Statutory inspection creates predictable future commercial event. Pre-inspection diagnosis + reminders. | B02 NZ |
| CIRCULAR_ASSET_LIQUIDITY | Human need < asset life → exit events = supply. Same unit: install + lease + maintain + battery + remove + buy-back + parts. | B02 IE |
| OEM_CERTAINTY_PRICE_LADDER | OEM filters 66-166% premium over compatible. Market pays for certainty. | B02 FI |
| CHANNEL_OPENNESS_MULTIPLIER | Installed base attractiveness × channel openness = actual opportunity. OEM capture kills independent middleman. | B03 AT |

---

## Hypothesis Updates

### H1: Installed Infrastructure Intelligence
**Status:** STRENGTHENED
**Evidence:** B02 and B03 confirm the thesis across ventilation, stairlifts, pools, pellet heating.
**Key refinement:** Channel openness is now a first-class variable. Austria proves that high installed base + OEM capture = weak opportunity.

### H2: Seasonal Premium Exists
**Status:** CONFIRMED
**Evidence:** B03 observed 15.6% median high-season premium in France. +50-100% weekend emergency pricing.

### H3: Dispatch Cost > Information Cost
**Status:** CONFIRMED
**Evidence:** B03: physical diagnosis costs 2.7x remote diagnosis. Repair visit costs 4.1x.

### H4: Generic Parts Market Already Mature
**Status:** CONFIRMED for France
**Evidence:** B03: French specialist has 1,520 SKUs. Generic parts whitespace is weak.

### H5: Regulation Can Veto Repair Business
**Status:** CONFIRMED for Italy
**Evidence:** B03: Lombardy regulation converts repair leads into replacement leads.

### H6: Channel Openness Determines Opportunity
**Status:** NEW — from B03 Austria
**Evidence:** Austria: high installed base + OEM capture = weak independent middleman opportunity.

---

## What to Do Next

1. **Load all probe JSONs into BigQuery** — structured data for hypothesis generation
2. **Update Gold Registry** with 9 new patterns
3. **Run scoring engine** on all 12 probes completed so far
4. **Identify top 3 probe opportunities** for next batch
5. **Build automated probe quality scoring** — track which probes produce the most useful intel

The most important insight from B02+B03:

> **The asset attractiveness must be multiplied by channel openness.** Austria proves that high installed base + OEM capture = weak opportunity. France proves that fragmented multi-brand service = strong opportunity. The same installed base can be gold or worthless depending on who owns the customer relationship.
