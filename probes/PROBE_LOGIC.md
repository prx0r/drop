# Probe Logic

*The autonomous probe architecture for ecommerce market intelligence.*
*Every probe is a hypothesis test. Every output is a market-intelligence kernel.*
*Generated: 2026-09-08T11:00:00Z*

---

## The Core Principle

> **A good autonomous probe should not optimize for novelty. It should optimize for information gain.**

"New product" is weak novelty.
"A new fact that changes our posterior belief about an existing candidate" is strong novelty.

---

## The 10 Design Principles (from iteration)

### 1. Forced novelty destroys probe quality
Old: "find 20 new things every hour" → weak evidence, semantic duplicates.
New: "few results are acceptable, UNKNOWN is acceptable, NO CHANGE is acceptable, KILL is successful."

### 2. Novelty must mean belief update
Not: "another seller found"
But: "another seller found → proves public scarcity is false → merchant-gap score drops"

### 3. Every probe needs an explicit falsifier
Bad: "Investigate whether Finland is good for Tramex."
Good: "HYPOTHESIS: Finland has demand but weak Tramex supply. FALSIFY: No demand, hidden distributor, or >=3 competent local merchants."

### 4. Negative evidence is more valuable than positive
Finding "another seller" can kill a thesis. Finding "no seller" does not prove one.

### 5. Search absence is not market absence
For professional products: poor Google indexing ≠ no market. It may indicate trade portals, distributors, phone orders, dealer accounts.

### 6. Separate observation, inference, decision
- OBSERVATION: "CSMegastore lists 0564 5501 at NOK 6,532"
- INFERENCE: "Norway is less supply-empty than public search suggested"
- DECISION: "Do not advance MERCHANT_GAP_VERIFIED"

### 7. Persist unknowns as first-class objects
`dealer_price = UNKNOWN` tells downstream agents to stop pretending we know economics.

### 8. Every probe needs a stopping rule
States: RESOLVED, FALSIFIED, EXTERNALLY_BLOCKED, LOW_EVI, STALE, WATCH

### 9. Balance exploration and exploitation
60% high-EVI live hypotheses, 20% systematic mass scanning, 10% anomaly follow-up, 10% exploration.

### 10. Source selection as bandit problem
$$SourceUtility = \frac{MaterialInformationGain}{SearchCost}$$

---

## The Six Questions Every Probe Must Answer

1. WHAT EXACT HYPOTHESIS WAS TESTED?
2. WHAT NEW FACT WAS OBSERVED?
3. DID IT SUPPORT OR WEAKEN THE HYPOTHESIS?
4. WHAT DECISION CHANGED?
5. WHAT IS THE SINGLE MOST VALUABLE UNKNOWN NOW?
6. WHAT GENERAL RULE DID THIS TEACH US?

---

## The Kernel Format

```json
{
  "kernel_id": "K-20260907-TESTO-NO-003",
  "candidate_id": "NO-TESTO-550S-001",
  "hypothesis": "Norway has sparse specialist Testo 550s retail",
  "new_observation": {
    "fact": "Testo Norway routes through Max Sievert A-S",
    "source_grade": "A"
  },
  "belief_delta": "STRONGLY_AGAINST",
  "mechanism": "weak public exact-SKU indexing caused by hidden professional distribution",
  "state_before": "DEMAND_VERIFIED",
  "state_after": "HUMAN_ACTION_REQUIRED",
  "resolved_fields": ["national_distribution_channel"],
  "remaining_decisive_unknown": "dealer_net_price",
  "next_best_test": "request 1/5/10-unit Max Sievert reseller quote",
  "generalisable_rule": "professional-product public SERP scarcity must be checked against trade/distributor networks",
  "novelty_type": "MECHANISM_DISCOVERY",
  "information_gain": "HIGH"
}
```

---

## The Pipeline Architecture

```
Gmail → Import → Parse → BigQuery → Hypotheses → Probes → Outcomes → Learning
```

Each step is modular. Each step has inputs, outputs, and failure modes.

See `pipelines.md` for the complete flow.
