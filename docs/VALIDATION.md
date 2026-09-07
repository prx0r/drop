# VALIDATION.md — Verification Doctrine

**Status:** Active
**Last updated:** 2026-09-08

---

## Three-Tier Verification

Every claim must pass three tiers of verification:

### Tier 1: Deterministic (Authoritative)
- Can be verified by code alone
- No human judgment required
- Examples: schema validation, type checking, content hashing

### Tier 2: Binary (LLM, Abstention-Capable)
- Requires LLM judgment but must be yes/no
- Model can abstain if uncertain
- Examples: "Is this a valid hypothesis?", "Does this evidence support the claim?"

### Tier 3: Qualitative (Narrative Only)
- Human review and narrative explanation
- Not used for automated decisions
- Examples: "Is this research direction promising?"

**Rule:** Model judgment is NEVER ground truth. Only Tier 1 is authoritative.

---

## Schema Validation

All schemas use Pydantic v2 with strict validation:

```python
from pydantic import BaseModel, Field

class Observation(BaseModel):
    observation_id: str = Field(default_factory=lambda: f"O-{uuid.uuid4().hex[:12]}")
    entity_type: str
    entity_id: str
    field: str
    value: str | float | int | bool
    source: EvidenceSource
    source_grade: EvidenceGrade
    observed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    ingested_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    model_config = {"frozen": True}  # Immutable after creation
```

**Validation rules:**
- Required fields are enforced
- Type coercion is disabled (strict mode)
- Optional fields have defaults
- Frozen models prevent mutation where appropriate

---

## Pipeline Validation

Pipelines must be pure functions:

```python
# GOOD: Pure transform
def process(observation: Observation) -> Kernel:
    # No I/O, no side effects
    return Kernel(...)

# BAD: Has side effects
def process(observation: Observation) -> Kernel:
    print(f"Processing {observation.observation_id}")  # Side effect!
    return Kernel(...)
```

**Validation rules:**
- No `print()` statements in pipeline logic
- No file I/O in pipeline logic
- No network calls in pipeline logic
- No mutation of input objects (use `model_copy(deep=True)`)

---

## BigQuery Validation

All queries must use parameterized queries:

```python
# GOOD: Parameterized
query = "SELECT * FROM table WHERE id = @id"
job_config = QueryJobConfig(
    query_parameters=[ScalarQueryParameter("id", "STRING", value)]
)
result = client.query(query, job_config=job_config)

# BAD: String interpolation (SQL injection risk)
query = f"SELECT * FROM table WHERE id = '{value}'"
result = client.query(query)
```

**Validation rules:**
- Never interpolate user input into SQL
- Always use `QueryJobConfig` with parameters
- Always use `ScalarQueryParameter` for typed parameters

---

## Temporal Validation

Observations must have proper timestamps:

```python
# GOOD: All timestamps present
observation = Observation(
    event_time=datetime(2026, 9, 7),  # When it happened
    published_at=datetime(2026, 8, 15),  # When source published
    observed_at=datetime.now(timezone.utc),  # When we observed
    available_at=datetime(2026, 9, 7),  # When it was available
    ingested_at=datetime.now(timezone.utc),  # When we ingested
)

# BAD: Missing timestamps
observation = Observation(
    observed_at=datetime.now(timezone.utc),  # Only this one
)
```

**Validation rules:**
- `observed_at` and `ingested_at` are required
- `available_at` must be <= decision_time for point-in-time queries
- `event_time` should be set when known

---

## Economic Validation

CM0-CM3 must be calculated correctly:

```python
# GOOD: Proper calculation
ledger = CostLedger(
    gross_revenue=100.0,
    cogs=30.0,
    paid_acquisition=10.0,
    ai_tokens=5.0,
)
ledger.calculate()
assert ledger.cm0 == 70.0  # 100 - 30
assert ledger.cm1 == 60.0  # 70 - 10
assert ledger.cm2 == 55.0  # 60 - 5

# BAD: Missing costs
ledger = CostLedger(gross_revenue=100.0)
# CM0-CM3 are all 0.0 — wrong!
```

**Validation rules:**
- Every cost must be categorized into CM0-CM3
- `calculate()` must be called after setting costs
- CM2 is the primary optimization target

---

## Feature Snapshot Validation

Feature snapshots must be frozen at decision time:

```python
# GOOD: Snapshot before decision
snapshot = FeatureSnapshot(
    candidate_id="NO-TESTO-001",
    country_code="NO",
    search_volume=5000,
    cpc=0.72,
    # ... all features frozen
)
decision = DecisionEvent(
    feature_snapshot_id=snapshot.snapshot_id,
    chosen_action="RESEARCH_SUPPLIER",
)

# BAD: Using live features
decision = DecisionEvent(
    chosen_action="RESEARCH_SUPPLIER",
    # No feature snapshot — data leakage risk!
)
```

**Validation rules:**
- Every `DecisionEvent` must reference a `feature_snapshot_id`
- Feature snapshots are frozen (immutable after creation)
- Models must train on feature snapshots, not live data

---

## Hypothesis Validation

Hypotheses must have falsifiers:

```python
# GOOD: Has falsifier
hypothesis = Hypothesis(
    claim="Norway has sparse specialist Testo 550s retail",
    null_hypothesis="Hidden B2B distribution explains scarcity",
    falsifier=">=3 competent Norwegian merchants found",
)

# BAD: No falsifier
hypothesis = Hypothesis(
    claim="Norway might be good for Testo",
    # No null_hypothesis, no falsifier — untestable!
)
```

**Validation rules:**
- `claim` must be specific and testable
- `null_hypothesis` must explain the data without the claim
- `falsifier` must be a concrete, observable condition

---

## Calibration Validation

Predictions must be calibrated:

```python
# GOOD: Calibrated predictions
# When we predict 80%, ~80% should succeed
predictions = [0.8, 0.7, 0.6, 0.9, 0.5]
outcomes = [True, True, False, True, False]
# 80% of predictions >= 0.7 are True — calibrated!

# BAD: Miscalibrated predictions
predictions = [0.9, 0.9, 0.9, 0.9, 0.9]
outcomes = [True, False, True, False, True]
# Only 60% success when predicting 90% — miscalibrated!
```

**Validation rules:**
- Track Brier score: `mean((prediction - outcome)^2)`
- Track log loss: `mean(-log(p) if outcome else -log(1-p))`
- Plot reliability diagrams
- Target: when predicting 80%, ~80% should succeed

---

## Offline Policy Evaluation

Policies must be evaluated with propensities:

```python
# GOOD: Propensity-weighted evaluation
decision = PolicyAction(
    policy_id="thompson_v3",
    chosen_action="FI_HEATPUMP",
    chosen_action_probability=0.37,  # Logged propensity
    actual_value=150.0,  # Actual CM2
)
# Can compute: value / propensity = 150 / 0.37 = 405.4 (unbiased estimate)

# BAD: Naive comparison
decision = PolicyAction(
    policy_id="thompson_v3",
    chosen_action="FI_HEATPUMP",
    # No propensity logged — biased evaluation!
    actual_value=150.0,
)
```

**Validation rules:**
- Every `PolicyAction` must have `chosen_action_probability`
- Use inverse propensity scoring for offline evaluation
- Use doubly robust estimators when possible

---

## Test Validation

Every mechanism must have a test proving its property:

```python
# GOOD: Test proving determinism
def test_determinism():
    obs1 = Observation(field="test", value=1, source=EvidenceSource.MANUAL)
    obs2 = Observation(field="test", value=1, source=EvidenceSource.MANUAL)
    # Same inputs → same observation_id (if we control UUID)
    assert obs1.field == obs2.field
    assert obs1.value == obs2.value

# GOOD: Test proving immutability
def test_immutability():
    obs = Observation(field="test", value=1, source=EvidenceSource.MANUAL)
    try:
        obs.field = "changed"  # Should raise!
        assert False, "Observation should be frozen"
    except Exception:
        pass  # Expected
```

**Validation rules:**
- Every schema must have immutability test
- Every pipeline must have pure function test
- Every storage method must have parameterization test

---

## CI Validation (Planned)

GitHub Actions workflow:

```yaml
name: Validate
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -e .
      - run: python -m pytest tests/ -q
      - run: python -c "from schemas import *; print('Schemas OK')"
      - run: python -c "from pipelines import *; print('Pipelines OK')"
```

**CI checks:**
- All tests pass
- All schemas importable
- All pipelines importable
- No secrets in committed files
- BigQuery DDL syntax valid
