# Test Run Results — Finland Probes

*Generated: 2026-09-07*
*Status: STRUCTURED DATA FOR BIGQUERY*

---

## Test Run Output

### Strongest New Candidate

**Ouman EH-105/EH-203 → S105/S203 controller migration**

Status: `HUMAN_ACTION_REQUIRED`

Reasons:
- Reseller access unknown
- Migration complexity unknown
- Commissioning burden unknown
- Economics unknown
- Ouman itself explicitly maintains legacy successor mappings

Source: https://kauppa.ouman.fi/myynnista-poistuneet-tuotteet/

---

### Hard Kills

| Niche | Kill Reason | Source |
|-------|-------------|--------|
| Vallox/ILTO/Swegon fan motors | Finnish specialists already expose detailed fitment and migration information | Bistrotec |
| Uponor/Wirsbo thermostats | Uponor directly provides replacement and wiring mapping | Uponor |
| Oras cartridges | OEM catalog already maps discontinued faucets to parts | Oras |
| Harvia C-series electronics | OEM/specialist coverage already strong | Harvia |

---

### Key Insight

**Finnish HVAC/LVI has unusually competent model-specific ecommerce and OEM documentation.**

Future runs should:
1. Kill mainstream ventilation/filter/plumbing/sauna cells much earlier
2. Spend more search budget on digitally neglected installed bases

---

## Structured Data for BigQuery

### Campaigns Table

```json
{
  "campaign_id": "FI_OUMAN_EH105_001",
  "country": "FI",
  "oem": "Ouman",
  "asset_family": "heating_controller",
  "installed_asset": "EH-105/EH-203",
  "generation": "legacy",
  "trigger": "controller_failure",
  "component_family": "controller",
  "status": "HUMAN_ACTION_REQUIRED",
  "kill_reasons": [],
  "hard_gates": {
    "supplier_exists": "UNKNOWN",
    "stock_fresh": "UNKNOWN",
    "compatibility_proven": "UNKNOWN",
    "legal_explicit": "UNKNOWN"
  },
  "evidence": [
    {
      "type": "oem_successor_mapping",
      "source": "https://kauppa.ouman.fi/myynnista-poistuneet-tuotteet/",
      "date": "2026-09-07",
      "confidence": "HIGH"
    }
  ]
}
```

### Kill Ledger

```json
{
  "kill_id": "KILL_FI_VALLOX_FAN_001",
  "country": "FI",
  "oem": "Vallox/ILTO/Swegon",
  "asset_family": "ventilation_fan_motor",
  "kill_reason": "Finnish specialists already expose detailed fitment and migration information",
  "source": "https://www.bistrotec.fi/product/33109/vallox-95-puhallinmoottori-185w",
  "date": "2026-09-07",
  "lesson": "Finnish HVAC/LVI has unusually competent model-specific ecommerce"
}
```

### OEM Successor Mappings

```json
{
  "oem": "Ouman",
  "legacy_model": "EH-105",
  "successor_model": "S105",
  "mapping_type": "direct_successor",
  "source": "https://kauppa.ouman.fi/myynnista-poistuneet-tuotteet/",
  "verified": true
}
```

---

## How to Use This Data

### 1. Track What We've Tested

Every test run produces:
- Candidates tested
- Status (ATTACK/VERIFY/KILL/HUMAN_ACTION_REQUIRED)
- Kill reasons
- Hard gate status
- Evidence URLs

### 2. Build OEM Successor Graph

Track:
- OEM → legacy model → successor model
- Migration complexity
- Adapter requirements
- Commissioning requirements

### 3. Understand Incumbent Strength

Track:
- Which niches have strong specialists
- Which OEMs have good direct documentation
- Which markets are digitally neglected

### 4. Inform Future Runs

The key insight: **Finnish HVAC/LVI has unusually competent model-specific ecommerce.**

This means future Finland runs should:
- Kill mainstream ventilation/filter/plumbing/sauna cells earlier
- Focus on digitally neglected installed bases
- Spend more search budget on non-HVAC niches

---

## BigQuery Tables to Create

### `probe_runs`
- run_id
- country
- sector
- status
- candidates_tested
- candidates_killed
- candidates_attack
- candidates_verify
- human_action_required
- started_at
- finished_at

### `probe_kills`
- kill_id
- country
- oem
- asset_family
- kill_reason
- source_url
- date
- lesson

### `oem_successor_mappings`
- mapping_id
- oem
- legacy_model
- successor_model
- mapping_type
- adapter_required
- commissioning_required
- source_url
- verified

### `incumbent_strength`
- country
- oem
- asset_family
- specialist_count
- oem_dtc_quality
- merchant_gap_score
