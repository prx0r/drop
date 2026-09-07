# STALE — CANONICAL_CAMPAIGN_FORMAT.md

*This file is archived. See HCC_V2.md for current campaigns.*

# Canonical Campaign Format — The Standard

*Generated: 2026-09-07*
*Status: STANDARD — All future campaigns use this format*

---

## Why This Format

The test run format is the canonical format because:

1. **It can be queried in BigQuery** — every field is structured
2. **It enforces hard gates** — no UNKNOWN gets scored as fact
3. **It tracks evidence provenance** — every claim has a source URL
4. **It captures kills** — failures are research outcomes, not waste
5. **It builds the OEM successor graph** — machine-readable edges
6. **It's agent-readable** — agents can consume the structured JSON

---

## The Canonical Schema

```json
{
  "campaign_id": "HCC-FI-ALLAWAY-001",
  "track": "d2c_compatibility_commerce",

  "country": "FI",
  "language": "fi",
  "oem": "Allaway",
  "asset_family": "central_vacuum",
  "installed_asset": "KP-series",
  "generation": "1982-1990",
  "trigger": "filter_replacement",
  "component_family": "filter",

  "status": "ATTACK",

  "hard_gates": {
    "supplier_exists": true,
    "stock_fresh": true,
    "compatibility_proven": true,
    "legal_explicit": true
  },

  "installed_base": {
    "units": 300000,
    "source": "https://allaway.fi/en/",
    "confidence": "HIGH"
  },

  "identity": {
    "model_names": ["KP1000", "KP1200", "KP1500"],
    "aliases": ["KaikkiPois"],
    "oem_numbers": ["10810"],
    "type_plate_patterns": ["stamped on housing"]
  },

  "compatibility_graph": {
    "positive_edges": [
      {"from": "KP1200", "to": "10810", "relation": "FITS"}
    ],
    "negative_edges": [
      {"from": "KP2000", "to": "10810", "relation": "DOES_NOT_FIT"}
    ],
    "supersession_edges": []
  },

  "supplier": {
    "identified": true,
    "net_prices_verified": false,
    "stock_feed_verified": false,
    "direct_ship_verified": false,
    "rma_verified": false,
    "suppliers": [
      {
        "name": "Onninen",
        "sku_count": 143,
        "source": "https://www.onninen.fi/tuotemerkit/allaway",
        "net_price": "UNKNOWN"
      }
    ]
  },

  "economics": {
    "aov": 80,
    "aov_currency": "EUR",
    "supplier_cost": "UNKNOWN",
    "contribution_margin": "UNKNOWN",
    "cac": "UNKNOWN",
    "wrong_part_cost": "UNKNOWN"
  },

  "distribution": {
    "merchant_center": true,
    "shopify_catalog": true,
    "web_jsonld": true
  },

  "experiment": {
    "sku_count": 75,
    "resolver_test_cases": 100,
    "agent_queries": 20,
    "budget": "small",
    "success_rule": [
      "≥97% compatibility accuracy",
      "supplier agreement",
      "≥5 paid orders",
      "wrong-part rate <3%"
    ],
    "kill_rule": [
      "Finnish specialists answer ≥90% of test questions",
      "No supplier provides viable economics"
    ]
  },

  "evidence": [
    {
      "type": "installed_base",
      "source": "https://allaway.fi/en/",
      "date": "2026-09-07",
      "confidence": "HIGH"
    },
    {
      "type": "supplier_gap",
      "source": "https://www.onninen.fi/tuotemerkit/allaway",
      "date": "2026-09-07",
      "confidence": "MEDIUM"
    }
  ],

  "kill_reasons": [],
  "lessons": [],

  "state": "DISCOVERED"
}
```

---

## The State Machine

```
DISCOVERED
   ↓
INSTALLED_BASE_VERIFIED
   ↓
LIFECYCLE_TRIGGER_VERIFIED
   ↓
COMPATIBILITY_FRICTION_VERIFIED
   ↓
LOCAL_SUPPLY_VERIFIED
   ↓
OWNERSHIP_GAP_VERIFIED
   ↓
SUPPLIER_ECONOMICS_VERIFIED
   ↓
DEMAND_CAPTURE_VERIFIED
   ↓
PROBE_READY
   ↓
LAUNCHABLE
   ↓
FREE_LISTING_TEST
   ↓
PAID_SEARCH_TEST
   ↓
PROVEN
   ↓
OWNERSHIP_BUILD
```

Any `UNKNOWN` launch-critical field blocks promotion.

---

## BigQuery Tables

### `probe_runs`
- run_id, country, sector, status
- candidates_tested, candidates_killed, candidates_attack, candidates_verify
- human_action_required, started_at, finished_at

### `probe_kills`
- kill_id, country, oem, asset_family
- kill_reason, source_url, date, lesson

### `oem_successor_mappings`
- mapping_id, oem, legacy_model, successor_model
- mapping_type, adapter_required, commissioning_required
- source_url, verified

### `incumbent_strength`
- country, oem, asset_family
- specialist_count, oem_dtc_quality, merchant_gap_score

---

## Rules

1. **null ≠ zero** — never assume
2. **unknown margin ≠ 30%** — mark UNKNOWN
3. **unknown supplier access ≠ supplier quality 8/10** — mark UNKNOWN
4. **huge installed category ≠ huge addressable installed component base** — filter
5. **Every claim needs a source URL** — no unsourced facts
6. **Kills are research outcomes** — capture lessons
7. **Hard gates block promotion** — no skipping
