# API.md — Public API Reference

**Status:** Active
**Last updated:** 2026-09-08

---

## Schemas

### Observation

```python
from schemas.observation import Observation, UnknownField, EvidenceGrade, EvidenceSource

# Create an observation
obs = Observation(
    entity_type="candidate",
    entity_id="NO-TESTO-001",
    field="dealer_price",
    value=5200.0,
    unit="NOK",
    source=EvidenceSource.RETAILER_SITE,
    source_grade=EvidenceGrade.C,
    source_name="Max Sievert",
    candidate_id="NO-TESTO-001",
)

# Fields
obs.observation_id  # "O-1ffe3506ecc5" (auto-generated)
obs.entity_type     # "candidate"
obs.entity_id       # "NO-TESTO-001"
obs.field           # "dealer_price"
obs.value           # 5200.0
obs.unit            # "NOK"
obs.source          # EvidenceSource.RETAILER_SITE
obs.source_grade    # EvidenceGrade.C
obs.observed_at     # datetime (auto-set)
obs.ingested_at     # datetime (auto-set)

# Unknown field
unknown = UnknownField(
    candidate_id="NO-TESTO-001",
    field="dealer_price",
    why_unknown="Need exact dealer price",
    decision_dependency="Cannot calculate margin",
    resolution_path="Email supplier",
    probability_of_resolve=0.7,
    decision_impact=0.9,
    candidate_value=0.6,
    research_cost=0.5,
)
unknown.evi  # 0.76 (calculated)
```

### Hypothesis

```python
from schemas.hypothesis import Hypothesis, HypothesisState

hypothesis = Hypothesis(
    claim="Norway has sparse specialist Testo 550s retail",
    null_hypothesis="Hidden B2B distribution explains scarcity",
    falsifier=">=3 competent Norwegian merchants found",
    candidate_id="NO-TESTO-001",
    product_family="Testo 550s",
    country_code="NO",
)

# Fields
hypothesis.hypothesis_id  # "H-9b4bdb51ddc2"
hypothesis.claim          # "Norway has sparse..."
hypothesis.state          # HypothesisState.OPEN
hypothesis.confidence     # 0.5
hypothesis.support_ratio  # 0.5 (for / total)

# Methods
hypothesis.add_evidence_for("O-001")
hypothesis.add_evidence_against("O-002")
hypothesis.support(confidence=0.7)
result = hypothesis.falsify("Evidence contradicts", confidence=0.9)
```

### Kernel

```python
from schemas.kernel import Kernel, KernelType, BeliefDelta

kernel = Kernel(
    hypothesis="Norway has sparse specialist Testo 550s retail",
    new_observation={"fact": "Max Sievert found", "source_grade": "A"},
    belief_delta=BeliefDelta.STRONGLY_AGAINST,
    mechanism="Hidden professional distribution",
    kernel_type=KernelType.HIDDEN_CHANNEL_DISCOVERY,
    generalisable_rule="Professional-product public SERP scarcity must be checked against trade/distributor networks",
)

# Fields
kernel.kernel_id  # "K-0d50bea209f6"
kernel.kernel_type  # KernelType.HIDDEN_CHANNEL_DISCOVERY
kernel.belief_delta  # BeliefDelta.STRONGLY_AGAINST
kernel.generalisable_rule  # "Professional-product..."
```

### Candidate

```python
from schemas.candidate import Candidate, CandidateState

candidate = Candidate(
    product_family="Testo 550s",
    country_code="NO",
    category="HVAC/R",
)

# Fields
candidate.candidate_id  # "C-79f7afe4e84f"
candidate.state         # CandidateState.DISCOVERED
candidate.progress      # 0.0

# Methods
result = candidate.transition(CandidateState.DEMAND_VERIFIED, "demand confirmed")
# result = True (valid transition)
candidate.state_history  # [{"from": "DISCOVERED", "to": "DEMAND_VERIFIED", ...}]
```

### ProbeResult

```python
from schemas.probe import ProbeResult, ProbeOutcome, ResearchEVI

probe = ProbeResult(
    probe_id="product-market-radar",
    probe_name="Product-Market Opportunity Radar",
    hypothesis_id="H-001",
    candidate_id="C-001",
    outcome=ProbeOutcome.HYPOTHESIS_WEAKENED,
    queries_made=15,
    material_information_gains=3,
)

# Fields
probe.run_id  # "RUN-c2faaf3a5585"
probe.efficiency  # 0.20 (material_gains / queries)
probe.duration_seconds  # None (until completed_at set)
```

### Economics

```python
from schemas.economics import (
    CostLedger, DecisionEvent, FeatureSnapshot,
    EconomicOutcome, PolicyAction, TreatmentAssignment,
)

# Cost ledger
ledger = CostLedger(
    gross_revenue=100.0,
    cogs=30.0,
    paid_acquisition=10.0,
    ai_tokens=5.0,
)
ledger.calculate()
ledger.cm0  # 70.0
ledger.cm2  # 55.0

# Decision event
event = DecisionEvent(
    agent_id="agent-001",
    country_code="NO",
    chosen_action="RESEARCH_SUPPLIER",
    available_actions=["RESEARCH_SUPPLIER", "KILL", "BUILD_FREE_PAGE"],
)
event.event_id  # "DE-27d50c88ca30"

# Feature snapshot
snapshot = FeatureSnapshot(
    candidate_id="NO-TESTO-001",
    country_code="NO",
    installed_base=1400000,
    search_volume=5000,
    cpc=0.72,
)
snapshot.snapshot_id  # "FS-bbb204acc63d"

# Policy action
action = PolicyAction(
    policy_id="thompson_v3",
    policy_version="1.0",
    candidate_id="C-001",
    country_code="NO",
    feature_snapshot_id="FS-001",
    available_actions=["RESEARCH_SUPPLIER", "KILL"],
    chosen_action="RESEARCH_SUPPLIER",
    chosen_action_probability=0.37,
)

# Treatment assignment
assignment = TreatmentAssignment(
    experiment_id="EXP-001",
    candidate_id="C-001",
    randomization_unit="user",
    control="control_creative",
    treatment="new_creative",
    assignment_probability=0.5,
    actual_assignment="treatment",
)
```

---

## Pipelines

### GmailImportPipeline

```python
from pipelines.gmail_import import GmailImportPipeline

gmail = GmailImportPipeline()
observations = gmail.run(
    email_subject="[GeoDrop Market Anomaly Probe] 2026-09-07 08:00",
    email_body="GoldProbe B05...",
    probe_id="B05-IE-wastewater",
    candidate_id="IE-WASTEWATER-001",
)
# Returns: List[Observation]
```

### StateMachinePipeline

```python
from pipelines.state_machine import StateMachinePipeline

sm = StateMachinePipeline()
result = sm.run(candidate, observations)
# Returns: StateTransitionResult
result.transitioned  # True/False
result.from_state    # CandidateState.DISCOVERED
result.to_state      # CandidateState.DEMAND_VERIFIED
result.summary       # "DISCOVERED → DEMAND_VERIFIED: demand confirmed"
```

### HypothesisLedgerPipeline

```python
from pipelines.hypothesis_ledger import HypothesisLedgerPipeline

hl = HypothesisLedgerPipeline()
updates = hl.run([hypothesis], observations)
# Returns: List[HypothesisUpdate]
updates[0].summary           # "+4 evidence updates"
updates[0].hypothesis.state  # HypothesisState.SUPPORTED
```

### EVIPlannerPipeline

```python
from pipelines.evi_planner import EVIPlannerPipeline

evi = EVIPlannerPipeline()
rankings = evi.run(unknowns, candidate)
# Returns: List[ResearchEVI] (ranked by EVI)
rankings[0].field                 # "dealer_price"
rankings[0].evi                   # 0.76
rankings[0].recommended_action    # "Email supplier with quote request"
```

### KernelGeneratorPipeline

```python
from pipelines.kernel_generator import KernelGeneratorPipeline

kg = KernelGeneratorPipeline()
kernels = kg.run(observations, [hypothesis])
# Returns: List[Kernel]
kernels[0].kernel_type  # KernelType.SUPPLIER_PATH_DISCOVERY
kernels[0].belief_delta  # BeliefDelta.MODERATELY_FOR
```

---

## Storage

### LocalStorage

```python
from storage.local import LocalStorage

storage = LocalStorage()

# Write
storage.write_observation(observation)
storage.write_candidate(candidate)
storage.write_hypothesis(hypothesis)
storage.write_kernel(kernel)

# Read
observations = storage.read_observations(candidate_id="NO-TESTO-001")
candidates = storage.read_candidates(state="DEMAND_VERIFIED")
hypotheses = storage.read_hypotheses(state="OPEN")
kernels = storage.read_kernels(kernel_type="HIDDEN_CHANNEL_DISCOVERY")
```

### BigQueryStorage

```python
from storage.bigquery import BigQueryStorage

storage = BigQueryStorage()

# Write
storage.write_observation(observation)
storage.write_candidate(candidate)
storage.write_kernel(kernel)

# Read (with parameterized queries)
observations = storage.read_observations(candidate_id="NO-TESTO-001")
candidates = storage.read_candidates(state="DEMAND_VERIFIED")

# Graph
storage.write_graph_node("NO", "country", {"name": "Norway"})
storage.write_graph_edge("NO", "HEAT_PUMP", "HAS_ECOSYSTEM", weight=0.8)
storage.write_graph_observation("NO", "gdp_per_capita", 82000)

# Generic query
results = storage.query("SELECT * FROM drop.candidates WHERE country_code = 'NO'")
```

---

## Enums

### EvidenceGrade

```python
from schemas.observation import EvidenceGrade

EvidenceGrade.A  # Direct measurement (our own data)
EvidenceGrade.B  # Multiple independent sources agree
EvidenceGrade.C  # Single credible source
EvidenceGrade.D  # Weak source (forum, social media)
```

### EvidenceSource

```python
from schemas.observation import EvidenceSource

EvidenceSource.SERP
EvidenceSource.RETAILER_SITE
EvidenceSource.COMPARISON_SITE
EvidenceSource.SUPPLIER
EvidenceSource.MARKETPLACE
EvidenceSource.FORUM
EvidenceSource.NEWS
EvidenceSource.REGULATORY
EvidenceSource.OUR_STORE
EvidenceSource.SEARCH_CONSOLE
EvidenceSource.MERCHANT_CENTER
EvidenceSource.MANUAL
```

### CandidateState

```python
from schemas.candidate import CandidateState

CandidateState.DISCOVERED
CandidateState.DEMAND_VERIFIED
CandidateState.MERCHANT_GAP_VERIFIED
CandidateState.SUPPLY_PATH_VERIFIED
CandidateState.MARGIN_VERIFIED
CandidateState.SEARCH_ECONOMICS_VERIFIED
CandidateState.LAUNCHABLE
CandidateState.FREE_TRAFFIC_TEST
CandidateState.PAID_TEST
CandidateState.PROFITABLE
CandidateState.KILLED
CandidateState.HUMAN_ACTION_REQUIRED
CandidateState.FROZEN
CandidateState.RESEARCHING
CandidateState.BUILD_READY
```

### HypothesisState

```python
from schemas.hypothesis import HypothesisState

HypothesisState.OPEN
HypothesisState.SUPPORTED
HypothesisState.STRONGLY_SUPPORTED
HypothesisState.FALSIFIED
HypothesisState.INCONCLUSIVE
HypothesisState.EXTERNALLY_BLOCKED
HypothesisState.SUPERSEDED
```

### KernelType

```python
from schemas.kernel import KernelType

KernelType.DEMAND_DISCOVERY
KernelType.DEMAND_FALSIFICATION
KernelType.MERCHANT_GAP_DISCOVERY
KernelType.MERCHANT_GAP_FALSIFICATION
KernelType.HIDDEN_CHANNEL_DISCOVERY
KernelType.SUPPLIER_PATH_DISCOVERY
KernelType.SUPPLIER_PATH_FAILURE
KernelType.MARGIN_THRESHOLD
KernelType.PRICE_COMPRESSION
KernelType.SATURATION_ACCELERATION
KernelType.CONTENT_NOT_COMMERCE
KernelType.SUPPORT_BURDEN
KernelType.RETURN_RISK
KernelType.WARRANTY_RISK
KernelType.SOURCE_MARKET_PROOF
KernelType.TARGET_MARKET_ASYMMETRY
KernelType.REGULATORY_BLOCKER
KernelType.HUMAN_ACTION_REQUIRED
KernelType.STORE_PROBE_RESULT
KernelType.GENERALISABLE_MECHANISM
```

### BeliefDelta

```python
from schemas.kernel import BeliefDelta

BeliefDelta.STRONGLY_FOR
BeliefDelta.MODERATELY_FOR
BeliefDelta.NEUTRAL
BeliefDelta.MODERATELY_AGAINST
BeliefDelta.STRONGLY_AGAINST
```
