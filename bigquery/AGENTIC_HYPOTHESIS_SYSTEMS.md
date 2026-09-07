# Agentic Hypothesis Systems — What Exists and How It Links to Drop

*Review of Co-Scientist, HypoGeniC, POPPER, AI Scientist v2, Arbor, Robin, and how they connect to our BigQuery commerce intelligence system.*
*Generated: 2026-09-08T05:30:00Z*

---

## The Landscape

| System | Type | Status | Stars | Key Insight |
|--------|------|--------|-------|-------------|
| Google Co-Scientist | Multi-agent hypothesis generation | Nature validated (May 2026) | N/A | Tournament of ideas for scientific discovery |
| HypoGeniC | Hypothesis generation from data | Open source (129 stars) | 129 | Data-driven hypothesis generation |
| POPPER | Automated hypothesis validation | Open source (288 stars) | 288 | Falsification-first approach |
| AI Scientist v2 | End-to-end scientific discovery | Preprint (Apr 2025) | N/A | Agentic tree search |
| Arbor | Persistent hypothesis tree | Preprint (Jun 2026) | N/A | Long-horizon research automation |
| Robin | Multi-agent biology discovery | Nature (May 2026) | N/A | Hypothesis + experimental data analysis |

---

## How They Link to Drop

### The Mapping

| Scientific System | Drop Equivalent |
|-------------------|-----------------|
| Research hypothesis | Product × Country hypothesis |
| Literature review | Prisjakt/Keyword Planner/competitor analysis |
| Wet-lab experiment | Store probe ($0 free listings → $5/day paid) |
| Measured outcome | Impressions, clicks, ATC, sales, profit |
| Scientific paper | Store launch (profitable or killed) |
| Peer review | Bayesian scoring against historical outcomes |
| Knowledge graph | BigQuery Graph (nodes: countries, ecosystems, products, merchants) |
| PubMed/ChEMBL | Prisjakt, Hinta.fi, Google Shopping, Keyword Planner |

### The Architecture We Should Build

```
                    ┌─────────────────────────────┐
                    │    Ecommerce Co-Scientist    │
                    │                               │
                    │  ┌─────────┐  ┌──────────┐  │
                    │  │Generate │  │Reflect   │  │
                    │  │hypotheses│  │(falsify) │  │
                    │  └────┬────┘  └────┬─────┘  │
                    │       │            │        │
                    │  ┌────┴────────────┴─────┐  │
                    │  │    BigQuery Brain      │  │
                    │  │  (graph + ML + AI)     │  │
                    │  └────────────┬──────────┘  │
                    │               │              │
                    │  ┌────────────┴──────────┐  │
                    │  │    Probe Generator     │  │
                    │  │  (cheapest test)       │  │
                    │  └────────────┬──────────┘  │
                    │               │              │
                    │  ┌────────────┴──────────┐  │
                    │  │    Store Probe         │  │
                    │  │  (real outcome)        │  │
                    │  └────────────┬──────────┘  │
                    │               │              │
                    │  ┌────────────┴──────────┐  │
                    │  │    Learning Loop       │  │
                    │  │  (hierarchical Bayes)  │  │
                    │  └───────────────────────┘  │
                    │                               │
                    └─────────────────────────────┘
```

---

## What We Can Steal

### From Co-Scientist
- **Tournament of ideas** — multiple agents debate and rank hypotheses
- **Reflection agent** — searches literature, verifies novelty, checks evidence
- **Meta-review agent** — ensures alignment with research goals
- **Application:** Our probe system should have multiple agents debating which product × country to test next

### From HypoGeniC
- **Data-driven hypothesis generation** — hypotheses come from data, not brainstorming
- **Hypothesis inference** — given a dataset, what hypotheses does it support?
- **Application:** Our BigQuery data should generate hypotheses automatically

### From POPPER
- **Falsification-first** — design experiments to DISPROVE, not prove
- **Sequential falsification** — keep testing until confidence is high enough
- **Application:** Our probe system should be designed to kill ideas fast, not defend them

### From Arbor
- **Persistent hypothesis tree** — track hypotheses, evidence, and decisions over time
- **Long-horizon research** — maintain state across multiple experiments
- **Application:** Our BigQuery Graph should track hypothesis states and evidence

### From Robin
- **Integrated hypothesis + experimental analysis** — one system that generates AND analyzes
- **Application:** Our probe system should generate hypotheses AND analyze outcomes in one loop

---

## What We Should Build

### Priority 1: Hypothesis Generator (from HypoGeniC)

```python
# Given BigQuery data, generate hypotheses
def generate_hypotheses(data):
    """
    Input: BigQuery tables (ecosystems, merchants, products, observations)
    Output: List of hypotheses with predictions
    
    For each product × country cell:
    1. Compute demand_score, merchant_gap, margin, supplier_quality
    2. Generate hypothesis: "Product X in Country Y will be profitable if Z"
    3. Generate prediction: "P(profitable) = 0.XX"
    4. Generate falsification: "If 100 clicks produce 0 sales, hypothesis is false"
    """
    pass
```

### Priority 2: Probe Generator (from POPPER)

```python
# Given a hypothesis, design the cheapest test
def design_probe(hypothesis):
    """
    Input: Hypothesis with predictions
    Output: Cheapest valid experiment
    
    For each hypothesis:
    1. What's the minimum data needed?
    2. What's the cheapest way to get it?
    3. What's the stopping rule?
    """
    pass
```

### Priority 3: Outcome Analyzer (from Robin)

```python
# Given store outcomes, update beliefs
def analyze_outcomes(outcomes, hypotheses):
    """
    Input: Store outcomes + current hypotheses
    Output: Updated beliefs with posterior distributions
    
    For each outcome:
    1. Update CVR posterior (Beta-binomial)
    2. Update margin posterior (normal)
    3. Update supplier reliability (Beta)
    4. Recalculate P(profitable)
    5. Update hypothesis status (CONFIRMED/REFUTED/UNCERTAIN)
    """
    pass
```

### Priority 4: Hypothesis Tree (from Arbor)

```python
# Track hypothesis states over time
class HypothesisTree:
    """
    Persistent tree of hypotheses, evidence, and decisions.
    
    Each node:
    - hypothesis_id
    - statement
    - predictions
    - evidence[]
    - status (UNTESTED/TESTING/CONFIRMED/REFUTED)
    - children (derived hypotheses)
    """
    pass
```

---

## The BigQuery Integration

### Tables We Need

```sql
-- Hypothesis table
CREATE TABLE hypotheses (
    hypothesis_id STRING,
    statement STRING,
    target_population STRING,
    estimand STRING,
    minimum_effect FLOAT64,
    prior_model STRING,
    status STRING,  -- UNTESTED/TESTING/CONFIRMED/REFUTED
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Prediction table
CREATE TABLE predictions (
    prediction_id STRING,
    hypothesis_id STRING,
    metric STRING,
    target_value FLOAT64,
    window_days INT64,
    status STRING  -- PENDING/RESOLVED
);

-- Evidence table
CREATE TABLE evidence (
    evidence_id STRING,
    hypothesis_id STRING,
    evidence_type STRING,  -- MEASURED/ESTIMATED/INFERRED
    metric_name STRING,
    metric_value FLOAT64,
    source STRING,
    confidence FLOAT64,
    observed_at TIMESTAMP
);

-- Outcome table
CREATE TABLE outcomes (
    outcome_id STRING,
    hypothesis_id STRING,
    store_id STRING,
    result STRING,  -- PROFITABLE/KILLED/UNCERTAIN
    revenue FLOAT64,
    profit FLOAT64,
    days_active INT64,
    total_clicks INT64,
    total_orders INT64,
    completed_at TIMESTAMP
);
```

### The Learning Query

```sql
-- Update hypothesis status based on outcomes
UPDATE hypotheses
SET status = CASE
    WHEN (SELECT COUNT(*) FROM outcomes WHERE hypothesis_id = hypotheses.hypothesis_id AND result = 'PROFITABLE') >= 3
    THEN 'CONFIRMED'
    WHEN (SELECT COUNT(*) FROM outcomes WHERE hypothesis_id = hypotheses.hypothesis_id AND result = 'KILLED') >= 2
    THEN 'REFUTED'
    ELSE status
    END,
    updated_at = CURRENT_TIMESTAMP()
WHERE status = 'TESTING'
```

---

## The Key Insight

**We don't need to build Co-Scientist from scratch.** We need to:

1. **Use BigQuery as the knowledge graph** — already built
2. **Use HypoGeniC-style generation** — hypotheses come from data
3. **Use POPPER-style falsification** — probes are designed to kill, not prove
4. **Use Robin-style analysis** — outcomes update beliefs automatically
5. **Use Arbor-style tracking** — persistent hypothesis tree in BigQuery

The architecture is:
```
BigQuery Graph (what we know)
  → Hypothesis Generator (what we should test)
  → Probe Generator (cheapest test)
  → Store Probe (real outcome)
  → Outcome Analyzer (update beliefs)
  → Hypothesis Tree (track states)
  → Learning Loop (compound knowledge)
```

**That's the system. It's buildable with what we have.**
