# RECIPES.md — Probe Execution Recipes

**Status:** Active
**Last updated:** 2026-09-08

---

## What is a Recipe?

A recipe is a reusable, typed workflow for executing a specific task. Recipes combine multiple pipeline steps into a complete operation.

Each recipe has:
- **Name** (snake_case)
- **Input** (typed schemas)
- **Output** (typed schemas)
- **Steps** (sequential operations)
- **Failure modes** (what can go wrong)
- **Success criteria** (how to know it worked)

---

## Recipe 1: Import Probe Report

**Purpose:** Convert a raw email probe report into structured observations, update candidate state, and generate kernels.

**Input:** Email subject + body
**Output:** `ImportResult` (observations, state transitions, kernels)

```python
from schemas.observation import Observation
from schemas.candidate import Candidate
from schemas.hypothesis import Hypothesis
from pipelines.gmail_import import GmailImportPipeline
from pipelines.state_machine import StateMachinePipeline
from pipelines.hypothesis_ledger import HypothesisLedgerPipeline
from pipelines.kernel_generator import KernelGeneratorPipeline

def import_probe_report(
    email_subject: str,
    email_body: str,
    candidate: Candidate,
    hypothesis: Hypothesis,
    probe_id: str,
) -> dict:
    """Recipe: Import a probe report and update all state."""
    
    # Step 1: Extract observations from email
    gmail = GmailImportPipeline()
    observations = gmail.run(email_subject, email_body, probe_id=probe_id)
    
    # Step 2: Evaluate state transitions
    sm = StateMachinePipeline()
    state_result = sm.run(candidate, observations)
    
    # Step 3: Update hypothesis evidence
    hl = HypothesisLedgerPipeline()
    hypothesis_updates = hl.run([hypothesis], observations)
    
    # Step 4: Generate kernels
    kg = KernelGeneratorPipeline()
    kernels = kg.run(observations, [hypothesis])
    
    return {
        "observations": observations,
        "state_result": state_result,
        "hypothesis_updates": hypothesis_updates,
        "kernels": kernels,
    }
```

**Failure modes:**
- Email parsing fails → log and continue with partial observations
- State transition invalid → log and skip
- Hypothesis not found → create new hypothesis

**Success criteria:**
- At least 1 observation extracted
- State transition logged
- At least 1 kernel generated

---

## Recipe 2: Score Candidate

**Purpose:** Evaluate a candidate through the full scoring pipeline.

**Input:** `Candidate`, `List[Observation]`
**Output:** `ScoredCandidate` (score, gates, recommendation)

```python
from schemas.candidate import Candidate
from schemas.observation import Observation
from services.scoring.gates import run_all_gates
from services.scoring.score import score_candidate

def score_candidate_recipe(
    candidate: Candidate,
    observations: list[Observation],
) -> dict:
    """Recipe: Score a candidate through gates and scoring."""
    
    # Step 1: Run hard gates
    gate_report = run_all_gates(candidate)
    
    # Step 2: Calculate score (if gates pass)
    if gate_report.all_pass:
        score_report = score_candidate(candidate)
    else:
        score_report = None
    
    # Step 3: Generate recommendation
    recommendation = generate_recommendation(gate_report, score_report)
    
    return {
        "candidate": candidate,
        "gate_report": gate_report,
        "score_report": score_report,
        "recommendation": recommendation,
    }

def generate_recommendation(gate_report, score_report):
    """Generate ADVANCE/HOLD/KILL recommendation."""
    if not gate_report.all_pass:
        return "KILL"
    if score_report and score_report.total_score >= 70:
        return "ADVANCE"
    if score_report and score_report.total_score >= 50:
        return "HOLD"
    return "KILL"
```

**Failure modes:**
- Missing data → mark fields as UNKNOWN
- Score outlier → flag for manual review

**Success criteria:**
- All 7 gates evaluated
- Score calculated (if gates pass)
- Recommendation generated

---

## Recipe 3: Design and Execute Probe

**Purpose:** Design the cheapest test for a hypothesis and execute it.

**Input:** `Hypothesis`, `Candidate`
**Output:** `ProbeExecution` (probe design, execution plan, expected outcomes)

```python
from schemas.hypothesis import Hypothesis
from schemas.candidate import Candidate

def design_probe_recipe(
    hypothesis: Hypothesis,
    candidate: Candidate,
) -> dict:
    """Recipe: Design the cheapest test for a hypothesis."""
    
    # Step 1: Determine cheapest test
    test_type = determine_cheapest_test(hypothesis, candidate)
    
    # Step 2: Set budget and duration
    budget = set_budget(test_type)
    duration = set_duration(test_type)
    
    # Step 3: Set falsification threshold
    falsification_threshold = set_falsification_threshold(test_type)
    
    # Step 4: Generate execution plan
    execution_plan = generate_execution_plan(test_type, budget, duration)
    
    return {
        "hypothesis": hypothesis,
        "candidate": candidate,
        "test_type": test_type,
        "budget": budget,
        "duration": duration,
        "falsification_threshold": falsification_threshold,
        "execution_plan": execution_plan,
    }

def determine_cheapest_test(hypothesis, candidate):
    """Determine the cheapest test for a hypothesis."""
    # Free listing test
    if hypothesis.state == "DEMAND_VERIFIED":
        return "FREE_LISTING"
    
    # SERP check
    if hypothesis.state == "MERCHANT_GAP_VERIFIED":
        return "SERP_CHECK"
    
    # Supplier email
    if hypothesis.state == "SUPPLY_PATH_VERIFIED":
        return "SUPPLIER_EMAIL"
    
    # Paid probe
    return "PAID_PROBE_5"
```

**Failure modes:**
- Budget insufficient → escalate to human
- Test type invalid → fallback to cheapest option

**Success criteria:**
- Test type determined
- Budget set
- Execution plan generated

---

## Recipe 4: Evaluate Research Priority

**Purpose:** Rank unknowns by Expected Value of Information and select the best next action.

**Input:** `List[UnknownField]`, `Candidate`
**Output:** `ResearchPriority` (ranked actions, EVI scores)

```python
from schemas.observation import UnknownField
from schemas.candidate import Candidate
from pipelines.evi_planner import EVIPlannerPipeline

def evaluate_research_priority_recipe(
    unknowns: list[UnknownField],
    candidate: Candidate,
) -> dict:
    """Recipe: Rank research priorities by EVI."""
    
    # Step 1: Calculate EVI for each unknown
    evi = EVIPlannerPipeline()
    rankings = evi.run(unknowns, candidate)
    
    # Step 2: Select best next action
    best_action = rankings[0] if rankings else None
    
    # Step 3: Generate research plan
    research_plan = generate_research_plan(rankings)
    
    return {
        "candidate": candidate,
        "rankings": rankings,
        "best_action": best_action,
        "research_plan": research_plan,
    }

def generate_research_plan(rankings):
    """Generate a research plan from ranked unknowns."""
    plan = []
    for ranking in rankings[:3]:  # Top 3 actions
        plan.append({
            "field": ranking.field,
            "action": ranking.recommended_action,
            "evi": ranking.evi,
            "cost": ranking.research_cost,
        })
    return plan
```

**Failure modes:**
- No unknowns → return empty plan
- All unknowns blocked → escalate to human

**Success criteria:**
- All unknowns ranked by EVI
- Best action selected
- Research plan generated

---

## Recipe 5: Generate Market Intelligence

**Purpose:** Convert observations into market-intelligence kernels.

**Input:** `List[Observation]`, `List[Hypothesis]`, `ProbeResult`
**Output:** `List[Kernel]`

```python
from schemas.observation import Observation
from schemas.hypothesis import Hypothesis
from schemas.probe import ProbeResult
from pipelines.kernel_generator import KernelGeneratorPipeline

def generate_market_intelligence_recipe(
    observations: list[Observation],
    hypotheses: list[Hypothesis],
    probe_result: ProbeResult = None,
) -> list:
    """Recipe: Generate kernels from observations."""
    
    kg = KernelGeneratorPipeline()
    kernels = kg.run(observations, hypotheses, probe_result)
    
    # Filter for high-value kernels
    high_value_kernels = [
        k for k in kernels
        if k.information_gain in ["HIGH", "MEDIUM"]
    ]
    
    return high_value_kernels
```

**Failure modes:**
- No observations → return empty list
- All kernels low information → log and continue

**Success criteria:**
- At least 1 kernel generated
- Kernel type classified
- Belief delta calculated

---

## Recipe 6: Full Candidate Evaluation

**Purpose:** Complete evaluation of a candidate from discovery to decision.

**Input:** `Candidate`, `List[Observation]`, `List[Hypothesis]`, `List[UnknownField]`
**Output:** `EvaluationResult` (full evaluation with all components)

```python
from schemas.candidate import Candidate
from schemas.observation import Observation, UnknownField
from schemas.hypothesis import Hypothesis
from pipelines.state_machine import StateMachinePipeline
from pipelines.hypothesis_ledger import HypothesisLedgerPipeline
from pipelines.evi_planner import EVIPlannerPipeline
from pipelines.kernel_generator import KernelGeneratorPipeline

def full_candidate_evaluation_recipe(
    candidate: Candidate,
    observations: list[Observation],
    hypotheses: list[Hypothesis],
    unknowns: list[UnknownField],
) -> dict:
    """Recipe: Full evaluation of a candidate."""
    
    # Step 1: State machine
    sm = StateMachinePipeline()
    state_result = sm.run(candidate, observations)
    
    # Step 2: Hypothesis updates
    hl = HypothesisLedgerPipeline()
    hypothesis_updates = hl.run(hypotheses, observations)
    
    # Step 3: Research priorities
    evi = EVIPlannerPipeline()
    research_rankings = evi.run(unknowns, candidate)
    
    # Step 4: Generate kernels
    kg = KernelGeneratorPipeline()
    kernels = kg.run(observations, hypotheses)
    
    # Step 5: Generate recommendation
    recommendation = generate_recommendation_from_evaluation(
        state_result, hypothesis_updates, research_rankings
    )
    
    return {
        "candidate": candidate,
        "state_result": state_result,
        "hypothesis_updates": hypothesis_updates,
        "research_rankings": research_rankings,
        "kernels": kernels,
        "recommendation": recommendation,
    }
```

**Failure modes:**
- Pipeline error → log and continue with partial results
- Missing data → mark as UNKNOWN

**Success criteria:**
- All pipeline steps complete
- Recommendation generated
- All results logged

---

## Recipe 7: Daily Morning Routine

**Purpose:** Execute the daily morning routine as defined in AGENTS.md.

**Input:** None
**Output:** `DailyStatus` (current state summary)

```python
def daily_morning_routine_recipe() -> dict:
    """Recipe: Execute daily morning routine."""
    
    # Step 1: Check blockers
    blockers = check_blockers()
    
    # Step 2: Check candidates
    candidates = check_candidates()
    
    # Step 3: Check what you last did
    last_actions = check_last_actions()
    
    # Step 4: Check probe freshness
    probe_freshness = check_probe_freshness()
    
    # Step 5: Check Gmail for new reports
    new_reports = check_gmail_for_reports()
    
    # Step 6: Check BigQuery for new data
    bigquery_status = check_bigquery_status()
    
    return {
        "blockers": blockers,
        "candidates": candidates,
        "last_actions": last_actions,
        "probe_freshness": probe_freshness,
        "new_reports": new_reports,
        "bigquery_status": bigquery_status,
    }
```

**Failure modes:**
- Gmail auth fails → skip and log
- BigQuery unavailable → skip and log

**Success criteria:**
- All checks complete
- Status summary generated
- Issues logged

---

## Recipe 8: Process Email Response

**Purpose:** Process an incoming email response from a supplier or partner.

**Input:** Email subject + body
**Output:** `EmailProcessingResult` (parsed data, actions taken)

```python
def process_email_response_recipe(
    email_subject: str,
    email_body: str,
    sender: str,
) -> dict:
    """Recipe: Process an incoming email response."""
    
    # Step 1: Classify email
    email_type = classify_email(email_subject, email_body, sender)
    
    # Step 2: Extract data
    extracted_data = extract_data_from_email(email_body, email_type)
    
    # Step 3: Update relevant entities
    updates = update_entities_from_email(extracted_data)
    
    # Step 4: Log email
    log_email(sender, email_subject, email_type)
    
    # Step 5: Schedule follow-up if needed
    followup = schedule_followup_if_needed(email_type, updates)
    
    return {
        "email_type": email_type,
        "extracted_data": extracted_data,
        "updates": updates,
        "followup": followup,
    }
```

**Failure modes:**
- Email parsing fails → log and manual review
- Unknown sender → classify as UNKNOWN

**Success criteria:**
- Email classified
- Data extracted
- Entities updated
- Email logged

---

## Recipe 9: Update Knowledge Graph

**Purpose:** Update the BigQuery knowledge graph with new observations.

**Input:** `List[Observation]`, `List[Kernel]`
**Output:** `GraphUpdate` (nodes and edges updated)

```python
from storage.bigquery import BigQueryStorage

def update_knowledge_graph_recipe(
    observations: list[Observation],
    kernels: list[Kernel],
) -> dict:
    """Recipe: Update knowledge graph with new data."""
    
    storage = BigQueryStorage()
    
    # Step 1: Identify affected nodes
    affected_nodes = identify_affected_nodes(observations, kernels)
    
    # Step 2: Update node properties
    for node in affected_nodes:
        storage.write_graph_node(
            node_id=node["id"],
            node_type=node["type"],
            properties=node["properties"],
        )
    
    # Step 3: Update edges
    edges = extract_edges_from_kernels(kernels)
    for edge in edges:
        storage.write_graph_edge(
            source=edge["source"],
            target=edge["target"],
            edge_type=edge["type"],
            weight=edge["weight"],
        )
    
    # Step 4: Insert observations
    for obs in observations:
        storage.write_graph_observation(
            node_id=obs.entity_id,
            metric_name=obs.field,
            metric_value=obs.value if isinstance(obs.value, (int, float)) else 0,
            evidence_type=obs.source_grade.value,
            source=obs.source_name or "",
        )
    
    return {
        "nodes_updated": len(affected_nodes),
        "edges_updated": len(edges),
        "observations_inserted": len(observations),
    }
```

**Failure modes:**
- BigQuery insert fails → retry with backoff
- Node not found → create new node

**Success criteria:**
- Nodes updated
- Edges updated
- Observations inserted

---

## Recipe 10: End-to-End Probe Pipeline

**Purpose:** Complete end-to-end probe processing from email to stored results.

**Input:** Email subject + body
**Output:** `ProbePipelineResult` (full pipeline output)

def end_to_end_probe_pipeline_recipe(
    email_subject: str,
    email_body: str,
    probe_id: str,
) -> dict:
    """Recipe: End-to-end probe processing."""
    
    # Step 1: Import probe report
    import_result = import_probe_report(
        email_subject, email_body,
        candidate=None,  # Will be created
        hypothesis=None,  # Will be created
        probe_id=probe_id,
    )
    
    # Step 2: Score candidate (if exists)
    if import_result["state_result"].candidate:
        score_result = score_candidate_recipe(
            import_result["state_result"].candidate,
            import_result["observations"],
        )
    else:
        score_result = None
    
    # Step 3: Evaluate research priorities
    if import_result["observations"]:
        research_result = evaluate_research_priority_recipe(
            unknowns=[],  # Extract from observations
            candidate=import_result["state_result"].candidate,
        )
    else:
        research_result = None
    
    # Step 4: Generate kernels
    kernels = import_result["kernels"]
    
    # Step 5: Update knowledge graph
    graph_update = update_knowledge_graph_recipe(
        import_result["observations"],
        kernels,
    )
    
    return {
        "import_result": import_result,
        "score_result": score_result,
        "research_result": research_result,
        "kernels": kernels,
        "graph_update": graph_update,
    }
