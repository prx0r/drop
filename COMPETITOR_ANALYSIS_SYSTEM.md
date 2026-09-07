# Competitor Analysis System

*Generated: 2026-09-07*
*Status: ARCHITECTURE — How competitor analysis feeds into CGE*

---

## The Role of Competitor Analysis

Competitor analysis is **input to CGE**, not output from CG.

```
COMPETITOR ANALYSIS
        ↓
feeds into
        ↓
CGE (proposer)
        ↓
proposes mutations
        ↓
CG (judge)
        ↓
verdict
```

---

## What Competitor Analysis Provides

### 1. Incumbent Benchmark

For each campaign, identify the strongest incumbent and measure their resolution rate.

```json
{
  "incumbent_id": "haustechnik_binder",
  "name": "Haustechnik Binder",
  "url": "https://haustechnik-binder.de",
  "resolution_rate": 0.75,
  "coverage": "ELs fan inserts 1984-2008",
  "gaps": ["no compatibility graph", "no negative fitment", "no supersession chain"]
}
```

### 2. Market Position Map

For each campaign, map all competitors:

```json
{
  "competitors": [
    {
      "id": "helios_direct",
      "name": "Helios Direct",
      "type": "OEM",
      "strength": "authoritative parts database",
      "weakness": "not consumer-facing"
    },
    {
      "id": "haustechnik_binder",
      "name": "Haustechnik Binder",
      "type": "specialist",
      "strength": "good product pages",
      "weakness": "no compatibility graph"
    },
    {
      "id": "skybad",
      "name": "skybad.de",
      "type": "retailer",
      "strength": "good prices",
      "weakness": "no compatibility guidance"
    }
  ]
}
```

### 3. Gap Analysis

For each campaign, identify what incumbents DON'T do:

```json
{
  "gaps": [
    {
      "type": "compatibility_graph",
      "description": "No merchant compiles old identifier + control interface + adapter + current offer",
      "evidence": "Haustechnik Binder sells parts but doesn't explain which old housing fits which new insert"
    },
    {
      "type": "negative_fitment",
      "description": "No merchant explains what DOESN'T fit",
      "evidence": "ELs NFC requires technician; this is not communicated"
    },
    {
      "type": "supersession_chain",
      "description": "No merchant shows full old→new replacement path",
      "evidence": "ESBE 84→94 chain exists in OEM docs but not in merchant pages"
    }
  ]
}
```

---

## How CGE Uses Competitor Analysis

CGE receives competitor analysis as input and proposes mutations:

```json
{
  "mutation_type": "INCUMBENT_IMPROVEMENT",
  "target_gate": "G6",
  "action": "ADD_COMPATIBILITY_GRAPH",
  "description": "Add compatibility edges that incumbents lack",
  "expected_information_value": "HIGH",
  "expected_cash_cost": "LOW",
  "expected_human_minutes": 120
}
```

---

## How to Collect Competitor Data

### Manual (current)
1. Search web for competitors
2. Visit their sites
3. Assess their resolution rate
4. Identify gaps
5. Log to BigQuery

### Automated (future)
1. GitGoblin monitors competitor sites
2. Detects new products/features
3. Logs changes to BigQuery
4. CGE proposes mutations based on changes

---

## BigQuery Tables for Competitor Analysis

```sql
CREATE TABLE drop_graph.competitors (
  competitor_id STRING,
  campaign_id STRING,
  name STRING,
  type STRING,  -- OEM/SPECIALIST/RETAILER/MARKETPLACE
  url STRING,
  strength STRING,
  weakness STRING,
  resolution_rate FLOAT64,
  created_at TIMESTAMP
)

CREATE TABLE drop_graph.competitor_gaps (
  gap_id STRING,
  campaign_id STRING,
  competitor_id STRING,
  gap_type STRING,
  description STRING,
  evidence STRING,
  created_at TIMESTAMP
)
```

---

## The Flow

```
1. COLLECT competitor data (manual or automated)
2. LOG to BigQuery (competitors, gaps)
3. CGE reads competitor data
4. CGE proposes mutations to close gaps
5. CG evaluates mutated campaign
6. Repeat until ATTACK
```

---

## Key Insight

Competitor analysis is not a one-time activity. It's a **continuous feed** into CGE.

As competitors improve, CGE proposes mutations to stay ahead.

As competitors decline, CGE proposes mutations to capture their position.

That's how the system stays alive.
