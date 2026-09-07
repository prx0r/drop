# RECIPES.md — Agentic Workflow Recipes

*How to combine primitives into higher-order agentic workflows.*
*Each recipe is a complete, tested workflow that an agent can execute.*

---

## Why Recipes Matter

A schema is a noun. A pipeline is a verb. A recipe is a sentence.

Recipes show agents how to combine primitives into meaningful work. They are the vocabulary of autonomous commerce.

---

## Recipe 1: Morning Intelligence Briefing

**Purpose:** Start the day with complete situational awareness.
**Primitives:** Gmail fetch → parse → BigQuery read → synthesis

```python
def morning_briefing():
    """What happened overnight? What needs attention?"""
    
    # 1. Check for new probe reports
    emails = fetch_gmail("to:tradesprior@gmail.com subject:GeoDrop")
    new_reports = [e for e in emails if e.date > last_check]
    
    # 2. Parse each report
    for email in new_reports:
        observations = gmail_import.run(email.subject, email.body)
        bigquery.write_observations(observations)
    
    # 3. Read current state
    candidates = bigquery.read_candidates(state!="KILLED")
    hypotheses = bigquery.read_hypotheses(state="OPEN")
    
    # 4. Generate briefing
    return {
        "new_reports": len(new_reports),
        "active_candidates": len(candidates),
        "open_hypotheses": len(hypotheses),
        "top_priority": select_highest_evi(candidates, hypotheses),
    }
```

**Output:** "3 new reports, 5 active candidates, 2 need attention."

---

## Recipe 2: Candidate Evaluation

**Purpose:** Evaluate a candidate from discovery to decision.
**Primitives:** Gmail import → state machine → hypothesis ledger → kernel generator → BigQuery

```python
def evaluate_candidate(email_subject, email_body, candidate_id):
    """Full evaluation of a candidate from a probe report."""
    
    # 1. Extract observations
    observations = gmail_import.run(email_subject, email_body, candidate_id=candidate_id)
    
    # 2. Create or load candidate
    candidate = get_or_create_candidate(candidate_id)
    
    # 3. State transition
    sm_result = state_machine.run(candidate, observations)
    
    # 4. Update hypotheses
    hypotheses = bigquery.read_hypotheses(candidate_id=candidate_id)
    hl_result = hypothesis_ledger.run(hypotheses, observations)
    
    # 5. Generate kernels
    kernels = kernel_generator.run(observations, hypotheses)
    
    # 6. Store everything
    bigquery.write_observations(observations)
    for kernel in kernels:
        bigquery.write_kernel(kernel)
    
    return {
        "candidate": candidate,
        "state_transition": sm_result.summary,
        "hypothesis_updates": hl_result,
        "kernels": len(kernels),
        "next_action": determine_next_action(candidate, observations),
    }
```

**Output:** "Candidate advanced to DEMAND_VERIFIED. 3 kernels generated. Next: verify supplier."

---

## Recipe 3: Research Priority Ranking

**Purpose:** Determine the most valuable next research action.
**Primitives:** UnknownField → EVI planner → BigQuery read

```python
def rank_research_priorities(candidate_id):
    """What should we research next?"""
    
    # 1. Get candidate
    candidate = bigquery.read_candidate(candidate_id)
    
    # 2. Get unknowns
    unknowns = bigquery.read_unknowns(candidate_id=candidate_id)
    
    # 3. Rank by EVI
    rankings = evi_planner.run(unknowns, candidate)
    
    # 4. Return top 3
    return [
        {
            "field": r.field,
            "evi": r.evi,
            "action": r.recommended_action,
            "cost": r.research_cost,
        }
        for r in rankings[:3]
    ]
```

**Output:** "1. dealer_price (EVI=0.76, email supplier), 2. reseller_eligibility (EVI=0.45, check website)"

---

## Recipe 4: Market Intelligence Synthesis

**Purpose:** Synthesize observations across multiple candidates into market intelligence.
**Primitives:** BigQuery read → kernel aggregation → insight generation

```python
def synthesize_market_intelligence(country_code, ecosystem):
    """What do we know about this market?"""
    
    # 1. Get all observations for this market
    observations = bigquery.read_observations(
        candidate_id=f"{country_code}-{ecosystem}"
    )
    
    # 2. Get all kernels
    kernels = bigquery.read_kernels(
        candidate_id=f"{country_code}-{ecosystem}"
    )
    
    # 3. Aggregate by type
    kernel_counts = {}
    for k in kernels:
        kernel_counts[k.kernel_type] = kernel_counts.get(k.kernel_type, 0) + 1
    
    # 4. Find generalizable rules
    rules = [k.generalisable_rule for k in kernels if k.generalisable_rule]
    
    return {
        "observations": len(observations),
        "kernels": len(kernels),
        "kernel_types": kernel_counts,
        "generalizable_rules": rules,
        "market_maturity": assess_maturity(observations, kernels),
    }
```

**Output:** "12 observations, 8 kernels, 3 generalizable rules. Market is DEMAND_VERIFIED."

---

## Recipe 5: Hypothesis Testing Workflow

**Purpose:** Test a hypothesis through the full pipeline.
**Primitives:** Hypothesis → probe design → execution → evaluation

```python
def test_hypothesis(hypothesis_id):
    """Test a hypothesis end-to-end."""
    
    # 1. Load hypothesis
    hypothesis = bigquery.read_hypothesis(hypothesis_id)
    
    # 2. Design cheapest test
    test_design = design_probe(hypothesis)
    
    # 3. Execute test (free listing, SERP check, etc.)
    results = execute_test(test_design)
    
    # 4. Extract observations
    observations = extract_observations(results)
    
    # 5. Update hypothesis
    updates = hypothesis_ledger.run([hypothesis], observations)
    
    # 6. Generate kernels
    kernels = kernel_generator.run(observations, [hypothesis])
    
    # 7. Store
    bigquery.write_observations(observations)
    for kernel in kernels:
        bigquery.write_kernel(kernel)
    
    return {
        "hypothesis": hypothesis.claim,
        "old_state": hypothesis.state,
        "new_state": updates[0].hypothesis.state,
        "kernels": len(kernels),
        "falsified": updates[0].hypothesis.state == "FALSIFIED",
    }
```

**Output:** "Hypothesis SUPPORTED → STRONGLY_SUPPORTED. 2 kernels generated."

---

## Recipe 6: Daily Probe Processing

**Purpose:** Process all probe reports from the last 24 hours.
**Primitives:** Gmail fetch → batch parse → BigQuery write → synthesis

```python
def daily_probe_processing():
    """Process all overnight probe reports."""
    
    # 1. Fetch all reports from last 24h
    emails = fetch_gmail("to:tradesprior@gmail.com subject:GeoDrop newer_than:1d")
    
    results = []
    for email in emails:
        # 2. Parse
        observations = gmail_import.run(email.subject, email.body)
        
        # 3. Write to BigQuery
        bigquery.write_observations(observations)
        
        # 4. Track result
        results.append({
            "subject": email.subject,
            "observations": len(observations),
            "candidate": extract_candidate_id(email.subject),
        })
    
    # 5. Generate daily summary
    return {
        "reports_processed": len(results),
        "total_observations": sum(r["observations"] for r in results),
        "candidates_affected": list(set(r["candidate"] for r in results if r["candidate"])),
    }
```

**Output:** "5 reports processed, 47 observations, 3 candidates affected."

---

## Recipe 7: Anomaly Detection

**Purpose:** Detect unusual patterns in market data.
**Primitives:** BigQuery query → statistical analysis → alert

```python
def detect_anomalies():
    """Find unusual patterns in our data."""
    
    # 1. Query for price anomalies
    price_anomalies = bigquery.query("""
        SELECT candidate_id, field_name, 
               AVG(field_value_numeric) as avg_price,
               STDDEV(field_value_numeric) as std_price
        FROM drop.fact_market_observation
        WHERE field_name = 'price_observed'
        GROUP BY candidate_id, field_name
        HAVING STDDEV(field_value_numeric) > AVG(field_value_numeric) * 0.3
    """)
    
    # 2. Query for demand spikes
    demand_spikes = bigquery.query("""
        SELECT candidate_id, field_name, field_value_numeric
        FROM drop.fact_market_observation
        WHERE field_name = 'search_volume'
        AND field_value_numeric > 10000
    """)
    
    return {
        "price_anomalies": len(price_anomalies),
        "demand_spikes": len(demand_spikes),
        "alerts": generate_alerts(price_anomalies, demand_spikes),
    }
```

**Output:** "2 price anomalies, 1 demand spike. Alert: Davis Norway price dispersion."

---

## Recipe 8: Candidate Lifecycle Management

**Purpose:** Manage candidates through their lifecycle.
**Primitives:** State machine → decisions → actions

```python
def manage_lifecycle():
    """Advance, hold, or kill candidates based on current state."""
    
    # 1. Get all active candidates
    candidates = bigquery.read_candidates(state!="KILLED")
    
    actions = []
    for candidate in candidates:
        # 2. Check state
        if candidate.state == "HUMAN_ACTION_REQUIRED":
            # Check if action was taken
            if check_human_action(candidate):
                actions.append({"candidate": candidate.candidate_id, "action": "RESUME"})
        
        elif candidate.state == "FROZEN":
            # Check if freeze reason resolved
            if check_freeze_resolved(candidate):
                actions.append({"candidate": candidate.candidate_id, "action": "UNFREEZE"})
        
        elif candidate.state in ["DEMAND_VERIFIED", "MERCHANT_GAP_VERIFIED"]:
            # Check if ready to advance
            if ready_to_advance(candidate):
                actions.append({"candidate": candidate.candidate_id, "action": "ADVANCE"})
    
    return actions
```

**Output:** "2 candidates ready to advance, 1 frozen candidate resolved."

---

## Recipe 9: Economic Ledger Update

**Purpose:** Update the economic ledger with new cost/revenue data.
**Primitives:** CostLedger → BigQuery write → CM0-CM3 calculation

```python
def update_economic_ledger(experiment_id, cost_data, revenue_data):
    """Update the economic ledger for an experiment."""
    
    # 1. Create cost ledger
    ledger = CostLedger(
        gross_revenue=revenue_data["total"],
        cogs=cost_data["cogs"],
        supplier_freight=cost_data["shipping"],
        paid_acquisition=cost_data["ads"],
        ai_tokens=cost_data["ai"],
        agent_compute=cost_data["compute"],
    )
    ledger.calculate()
    
    # 2. Write to BigQuery
    bigquery.write_cost_ledger(ledger, experiment_id=experiment_id)
    
    # 3. Return CM breakdown
    return {
        "cm0": ledger.cm0,
        "cm1": ledger.cm1,
        "cm2": ledger.cm2,
        "cm3": ledger.cm3,
        "cm2_margin": ledger.cm2_margin,
    }
```

**Output:** "CM0=70, CM1=60, CM2=55. CM2 margin=55%."

---

## Recipe 10: Full Autonomous Research Cycle

**Purpose:** Complete autonomous research cycle from hypothesis to decision.
**Primitives:** All pipelines combined

```python
def autonomous_research_cycle(candidate_id):
    """Full autonomous research cycle."""
    
    # 1. Load current state
    candidate = bigquery.read_candidate(candidate_id)
    hypotheses = bigquery.read_hypotheses(candidate_id=candidate_id)
    unknowns = bigquery.read_unknowns(candidate_id=candidate_id)
    
    # 2. Rank research priorities
    rankings = evi_planner.run(unknowns, candidate)
    
    # 3. Execute top priority research
    if rankings:
        top_action = rankings[0]
        results = execute_research_action(top_action)
        
        # 4. Extract observations
        observations = extract_observations(results)
        
        # 5. Update state machine
        sm_result = state_machine.run(candidate, observations)
        
        # 6. Update hypotheses
        hl_result = hypothesis_ledger.run(hypotheses, observations)
        
        # 7. Generate kernels
        kernels = kernel_generator.run(observations, hypotheses)
        
        # 8. Store everything
        bigquery.write_observations(observations)
        for kernel in kernels:
            bigquery.write_kernel(kernel)
        
        # 9. Decision
        decision = make_decision(candidate, observations, kernels)
        
        return {
            "action_taken": top_action.recommended_action,
            "observations_gained": len(observations),
            "state_changed": sm_result.transitioned,
            "kernels_generated": len(kernels),
            "decision": decision,
        }
    
    return {"action_taken": "none", "reason": "no unresolved unknowns"}
```

**Output:** "Researched dealer_price. 5 observations. State advanced. 3 kernels. Decision: ADVANCE."

---

## The Pattern

Every recipe follows the same pattern:

```
INPUT (data)
    ↓
TRANSFORM (pipeline)
    ↓
OUTPUT (insight + action)
```

The primitives are the atoms.
The recipes are the molecules.
The agent is the chemist.
