# STALE — RED_TEAM_AUDIT.md

*This file is archived. See HCC_V2.md for current campaigns.*

# Red Team: Campaign Format Audit

*Generated: 2026-09-07*
*Status: CRITICAL REVIEW*

---

## Where the Format Hallucinates or Bullshits

### 1. Installed base numbers are often unsourced

Many campaigns state "250,000+ Finnish homes" or "483,631 Norwegian cabins" without verifying the exact number in the campaign JSON itself. The test run format requires `source` but we often put the source in the markdown, not the JSON.

**Fix:** Every `installed_base.units` must have a `source` URL and `confidence` level.

### 2. Economics are stated as fact when UNKNOWN

Previous campaigns said "30-40% margin" or "€15-50 net per order" without actual supplier net pricing. The test run format marks these as UNKNOWN, but the markdown campaigns still state them as fact.

**Fix:** Never state margin without actual distributor net price. Mark `UNKNOWN` until verified.

### 3. Compatibility graphs are assumed, not proven

We assume "KP1200 fits filter 10810" without verifying against OEM documentation or actual fitment tests. The test run format requires `verified: true/false` but we often don't verify.

**Fix:** Every compatibility edge needs `source` and `verified: true/false`.

### 4. Supplier accessibility is assumed

We assume "Onninen has stock" without checking if they'll sell to us, what the net price is, or if they do direct shipping. The test run format has `net_prices_verified: false` but we often skip this gate.

**Fix:** Hard gate: `supplier_exists AND will_sell_to_us` must be verified before ATTACK status.

### 5. Self-service resolution is assumed

We assume "consumer can photograph + measure" without testing whether the identification actually works. The test run format doesn't have a field for this.

**Fix:** Add `self_service_resolution_tested: true/false` field.

### 6. Pre-SKU uncertainty is assumed

We assume "consumer doesn't know SKU" without testing whether they actually search for the SKU or describe the problem. The test run format doesn't have a field for this.

**Fix:** Add `pre_sku_uncertainty_tested: true/false` field.

### 7. Kill reasons are often vague

We say "Finnish specialists already expose detailed fitment" without specifying which specialist, what they cover, and what they miss. The test run format has `kill_reason` but it's often too vague.

**Fix:** Every kill reason must name the specialist, what they cover, and what they miss.

### 8. Evidence URLs are sometimes broken or outdated

We cite sources without checking if they're still live. The test run format requires `source` but doesn't require `accessed_date`.

**Fix:** Every evidence URL must have `accessed_date`.

### 9. Status transitions are not tracked

We don't track when a campaign moves from DISCOVERED to INSTALLED_BASE_VERIFIED to etc. The test run format has `state` but we don't update it.

**Fix:** Track state transitions with timestamps.

### 10. Cross-campaign dependencies are not tracked

We don't track that "Norwegian cabin water" depends on "Allaway Finland" for the resolution engine. The test run format doesn't have a `depends_on` field.

**Fix:** Add `depends_on: []` field.

---

## What's Missing from the Format

### 1. Self-Service Resolution Ratio

```json
"self_service_resolution": {
  "tested": false,
  "ratio": null,
  "test_cases": 0,
  "source": null
}
```

### 2. Pre-SKU Uncertainty

```json
"pre_sku_uncertainty": {
  "tested": false,
  "level": null,
  "test_cases": 0,
  "source": null
}
```

### 3. Best Specialist Benchmark

```json
"best_specialist": {
  "name": null,
  "url": null,
  "coverage": null,
  "our_target_delta": 0.20,
  "tested": false
}
```

### 4. State Transitions

```json
"state_transitions": [
  {"state": "DISCOVERED", "at": "2026-09-07", "source": "manual"},
  {"state": "INSTALLED_BASE_VERIFIED", "at": "2026-09-07", "source": "SSB"}
]
```

### 5. Cross-Campaign Dependencies

```json
"depends_on": [],
"enables": ["HCC-FI-VALLOX-001"]
```

### 6. Mutation History

```json
"mutations": [
  {"at": "2026-09-07", "field": "status", "old": "DISCOVERED", "new": "ATTACK", "reason": "supplier verified"}
]
```

---

## BigQuery Graph Review

### What We Have

| Table | Rows | Purpose |
|-------|------|---------|
| country_data | 1,661 | Country market data |
| country_graph_nodes | 80 | Country graph nodes |
| country_graph_edges | 239 | Country graph relationships |
| dropintel_signals | 676 | Intelligence signals |
| products | 75 | Product catalog |
| graph_nodes | 27 | Graph nodes |
| graph_edges | 20 | Graph edges |
| case_studies | 12 | Case studies |
| experiments | 5 | Experiments |
| probe_reports | 5 | Probe reports |

### What's Missing

1. **OEM successor mappings** — we created the table but haven't loaded data
2. **Incumbent strength** — we created the table but haven't loaded data
3. **Probe runs** — we created the table but haven't loaded data
4. **Probe kills** — we created the table but haven't loaded data
5. **Compatibility edges** — no table for this yet
6. **Supplier access** — no table for this yet

### What Needs to Be Built

1. Load OEM successor mappings from all campaigns
2. Load incumbent strength from all campaigns
3. Load probe runs and kills from test runs
4. Build compatibility edge table
5. Build supplier access table

---

## The Role of Campaigns

Campaigns are not just "store ideas." They are:

1. **Research objects** — each campaign is a hypothesis to test
2. **Data collection mechanisms** — each transaction produces compatibility evidence
3. **Graph builders** — each sale adds edges to the compatibility graph
4. **Score mutation targets** — each campaign can be mutated to improve its score

### The Scoring Rubric

```
CAMPAIGN_SCORE =

25% information rent
    identity difficulty (tested)
    compatibility complexity (verified)
    supersession complexity (verified)

15% installed-base economics
    installed units (sourced)
    replacement frequency (evidence)
    urgency (evidence)

20% supplier arbitrage
    stock depth (verified)
    operational quality (verified)
    obtainable net price (verified)
    stock feed (verified)
    direct ship (verified)

15% distribution fit
    parcel suitability (tested)
    GMC eligibility (verified)
    visual search suitability (tested)
    structured-data potential (verified)

15% economics
    contribution/order (verified)
    AOV (verified)
    repeat purchase (evidence)
    adjacency expansion (evidence)

10% evidence quality
    first-party installed-base evidence (verified)
    actual supplier evidence (verified)
    actual merchant-gap evidence (verified)

MINUS:
0–15 best-specialist penalty (tested)
0–15 safety/install penalty (verified)
0–10 supplier uncertainty (verified)
0–10 return/liability penalty (evidence)
```

### The Mutation System

Each campaign can be mutated to improve its score:

```json
{
  "mutation_id": "MUT_001",
  "campaign_id": "HCC-FI-ALLAWAY-001",
  "field": "supplier.net_prices_verified",
  "old_value": false,
  "new_value": true,
  "reason": "Onninen confirmed net pricing",
  "score_impact": "+5",
  "at": "2026-09-07"
}
```

Mutations are tracked in BigQuery and used to:
1. Prove progress
2. Identify bottlenecks
3. Optimize research allocation

---

## Next Steps

1. Port all 20 campaigns to canonical format
2. Load OEM successor mappings into BigQuery
3. Load incumbent strength into BigQuery
4. Build compatibility edge table
5. Build supplier access table
6. Run test on Norwegian balcony-door hardware
7. Track mutations
