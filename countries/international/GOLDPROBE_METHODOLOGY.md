# GoldProbe — Canonical Methodology

*The standardized process for discovering and evaluating installed-infrastructure opportunities.*
*Every probe starts from raw market evidence, produces opportunity cells, compares them, and only then emits distinct economic patterns.*

---

## The Constraint

> **Patterns come out of measured market differences. We do not start with patterns and go hunting for confirming examples.**

Every GoldProbe starts from raw market evidence, produces opportunity cells, compares them, and only then emits distinct economic patterns.

---

## The 13 Questions Every GoldProbe Must Answer

1. How much more are people willing to pay?
2. What specifically are they willing to pay extra for?
3. On which exact products/problems is that premium largest?
4. What options do they currently have?
5. What do those options cost, how fast are they, and where is the friction?
6. Is there actual room for us? Where precisely?
7. What is the best go-to-market for this cell?
8. Does the same behavior exist in another country?
9. How large is the difference between countries?
10. Why does that difference exist?
11. What does it tell us structurally about that country?
12. What macro pattern emerges only after comparing the statistics?
13. What evidence would falsify our conclusion?

---

## The Canonical Report Format

```json
{
  "goldprobe_version": "1.0",
  "probe": {
    "sector": "string",
    "target_country": "string",
    "oracle_markets": ["string"],
    "date": "ISO-8601"
  },
  "market": {
    "installed_base": {"value": 0, "unit": "string", "source": "string"},
    "growth_or_age_signal": {"value": "string", "source": "string"},
    "owner_income_signal": {"value": "string", "source": "string"},
    "ecommerce_penetration": {"value": "string", "source": "string"},
    "labour_cost_signal": {"value": "string", "source": "string"}
  },
  "cells": [{
    "id": "string",
    "object": "string",
    "lifecycle_stage": "string",
    "trigger": "string",
    "problem": "string",
    "geography": "string",
    "live_evidence": {
      "installed_base": "string",
      "search_demand": "string",
      "competitor_count": "string",
      "typical_price": "string",
      "lead_time": "string",
      "failure_cost": "string",
      "grant_value": "string",
      "sources": ["string"]
    },
    "current_options": [{"type": "string", "price": "string", "friction": "string", "service_level": "string"}],
    "willingness_to_pay": {
      "observed_premium": "string",
      "premium_for": ["string"],
      "confidence": 0.0,
      "evidence": ["string"]
    },
    "market_gap": {"exists": true, "where": ["string"], "severity": 0},
    "go_to_market": ["string"],
    "monetization": ["string"],
    "falsifiers": ["string"]
  }],
  "cross_market_comparison": [{
    "comparison": "string",
    "metric": "string",
    "market_a": "string",
    "market_b": "string",
    "difference": "string",
    "why": "string",
    "source_evidence": ["string"]
  }],
  "new_patterns": [{
    "pattern_id": "string",
    "observation": "string",
    "derived_from_cells": ["string"],
    "supporting_statistics": ["string"],
    "economic_mechanism": "string",
    "countries_observed": ["string"],
    "counterexample": "string",
    "confidence": 0.0
  }],
  "country_insights": [{
    "finding": "string",
    "statistics": ["string"],
    "interpretation": "string",
    "commercial_implication": "string"
  }],
  "probe_verdict": {
    "best_cell": "string",
    "best_business_model": "string",
    "next_experiment": "string",
    "what_we_learned": "string"
  }
}
```

---

## The 7-Stage Pipeline

### Stage 1 — Find installed-base ecosystems
Search official statistics for: country, asset, installed units, households owning, age distribution, annual installations.

### Stage 2 — Find forcing functions
Search: inspection, regulation, mandatory servicing, warranty expiry, grant, insurance, safety recall, seasonality, property sale.

### Stage 3 — Build mature-market ontology
Take Sweden/Germany/UK/US. Extract: brands, models, replacement parts, consumables, fault codes, symptoms, upgrade products, service types, retrofits, maintenance intervals.

### Stage 4 — Mine human confusion
Reddit, forums, manufacturer support, YouTube comments. Extract problem-language, not industry-language.

### Stage 5 — Search target-country SERPs
Generate [problem] × [brand] × [model] × [city] queries. Classify SERP quality 0-5. We want: high demand × SERP quality ≤2–3.

### Stage 6 — Separate four monetization classes
- A: Ecommerce (parts, consumables)
- B: Qualified service lead
- C: High-ticket replacement lead
- D: Recurring relationship

### Stage 7 — Look for public datasets
Official statistics for installed base, inspection failures, grant activity, well locations, supplier registries.

---

## New Pattern Rules

- **Append-only and novelty checked.** If a future probe merely rediscovers "people pay for convenience," that is not a new pattern.
- **Every claimed pattern must contain at least one counterexample.**
- **Pattern must be specific:** Not "wealthy countries value convenience" but "In regulated rural-home infrastructure, consumers pay a premium for intermediaries that translate diagnostic evidence into correctly specified local contractor jobs because incorrect self-selection has high expected failure cost."

---

## Validated Patterns (append-only)

| ID | Pattern | Evidence | Confidence |
|----|---------|----------|------------|
| P001 | Maintenance graph > installation wave | EV, heat pump, cabin, well, wastewater | 0.95 |
| P002 | Good Seller Gap predicts opportunity | Finnish heat pump, Norwegian Davis | 0.80 |
| P003 | Localized transaction quality > cosmetic presentation | PostNord Nordic data | 0.85 |
| P004 | Installed base lifecycle creates recurring demand | Swedish heat pump, Finnish sauna | 0.90 |
| P005 | Forcing-function score correlates with conversion | Ireland inspection failures | 0.85 |
| P006 | Knowledge gap predicts middleman value | Septic, well water, EV charger | 0.80 |
| P007 | Government grants multiply lead value | Ireland €12k septic grants | 0.90 |
| P008 | Mature-market oracle generates target-country ontology | Germany→Finland heat pump parts | 0.85 |
| P009 | Lab report / model plate = compatibility key | Well water, heat pump, EV charger | 0.90 |
| P010 | Public datasets outperform scraping | Ireland CSO, EPA, DSB registry | 0.85 |

---

## Probes Completed

| ID | Sector | Country | Best Cell | Verdict | Report |
|----|--------|---------|-----------|---------|--------|
| GP-001 | Heat pumps / EV / Cabins | FI/NO | FI heat pump parts | 9.7/10 | countries/intel/2026-09-07_installed_base_maintenance_graph_arbitrage.md |
| GP-002 | Private water / wastewater | IE | IE well iron Galway | 9.2/10 | countries/intel/2026-09-08_installed_infrastructure_intelligence_ireland_water_wastewater.md |

---

## Next Probes (Priority Order)

| Priority | Sector | Target | Oracle | Why |
|----------|--------|--------|--------|-----|
| 1 | Automatic gates / garage doors | CH/NO/IE/UK | DE | Extreme model incompatibility, urgent repair, fragmented installers |
| 2 | Swimming pools / spas | AU/NZ/CH/FR | US/UK | Pumps, filters, chemistry, leaks, local techs |
| 3 | Home ventilation / MVHR | Nordics | DE/UK | Filters recurring, motors, sensors, upgrade |
| 4 | Residential lifts / stairlifts | Wealthy property | UK/DE | Batteries, PCBs, high lead value |
| 5 | Wood/pellet stoves | Nordics/Alpine | DE/SE | Fans, igniters, controllers, chimney service |

---

## Counterexamples (every pattern needs one)

| Pattern | Counterexample | Lesson |
|---------|---------------|--------|
| P001 Maintenance graph | Finland sauna parts — local commerce already caught up | Mature local specialists can fill the gap before we arrive |
| P002 Good Seller Gap | Finnish robot vacuums — 22 sellers, many weak but 5+ good | "Few sellers" ≠ "few GOOD sellers" — must score quality |
| P003 Localized transaction | Finland social commerce — 38% of under-30s buy on social | Different markets need different channels, not just localized Google |
| P007 Grant multiplier | UK EV grants — complex eligibility, many don't qualify | Grants create complexity but also confusion; must be simple to explain |
