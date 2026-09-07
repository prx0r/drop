# REDTEAM.md — Canonical Anti-Hallucination Protocol

*Based on: NabaOS (tool receipts), AgentVerify (formal verification), AutoResearch (audit-confirmed events)*
*The log is the ground truth. The agent cannot lie because the log exists.*

---

## Core Principle

> **Every action produces a receipt. Every claim must reference a receipt.**
> **If the receipt doesn't exist, the claim is a hallucination.**

---

## The Three-Layer Defense

### Layer 1: Tool Receipts (NabaOS pattern)

Every tool call produces a signed receipt:

```python
class ToolReceipt(BaseModel):
    receipt_id: str  # content hash
    tool_name: str  # e.g. "bigquery.insert"
    inputs: dict  # what was passed
    outputs: dict  # what was returned
    timestamp: datetime
    agent_id: str
    signature: str  # HMAC of receipt
```

**Rule:** Agent cannot claim "BigQuery write worked" without a receipt proving it.

### Layer 2: Claim Verification (AutoResearch pattern)

Every claim must be audit-confirmed:

```python
class ClaimVerification(BaseModel):
    claim: str  # What agent said
    receipt_id: str  # Proof receipt
    verification_method: str  # How to check
    actual_result: str  # What was actually found
    verdict: str  # "CONFIRMED" / "REFUTED" / "UNVERIFIABLE"
```

**Rule:** Agent cannot claim "tests pass" without showing test output.

### Layer 3: Formal Properties (AgentVerify pattern)

Define safety properties in temporal logic:

```python
# Property: Every write must be readable
"FORALL x: write(x) -> eventually read(x) == x"

# Property: No hallucinated test results
"FORALL claim: claim(tests_pass) -> exists log: log contains 'RESULT: PASS'"

# Property: No hallucinated data
"FORALL claim: claim(data_written) -> exists query: query.count > 0"
```

**Rule:** System must prove properties hold, not just check them once.

---

## The Protocol

### Step 1: Generate Receipt

```python
def generate_receipt(tool_name: str, inputs: dict, outputs: dict) -> ToolReceipt:
    """Generate a signed receipt for a tool call."""
    import hashlib, hmac
    
    receipt = ToolReceipt(
        receipt_id=hashlib.sha256(json.dumps(outputs).encode()).hexdigest()[:16],
        tool_name=tool_name,
        inputs=inputs,
        outputs=outputs,
        timestamp=datetime.now(timezone.utc),
        agent_id="agent-001",
        signature="",  # HMAC computed below
    )
    
    # Sign the receipt
    message = json.dumps(receipt.model_dump(exclude={"signature"})).encode()
    signature = hmac.new(b"secret-key", message, hashlib.sha256).hexdigest()[:16]
    receipt.signature = signature
    
    return receipt
```

### Step 2: Make Claim with Receipt

```python
# Agent cannot just say:
# "BigQuery write worked"

# Agent MUST say:
receipt = generate_receipt("bigquery.insert", inputs, outputs)
claim = "BigQuery write worked"
verification = "SELECT COUNT(*) FROM table WHERE id = receipt.outputs['id']"

# Store both
store_claim(claim, receipt, verification)
```

### Step 3: Verify Claim Against Reality

```python
def verify_claim(claim: str, receipt_id: str, verification_sql: str) -> ClaimVerification:
    """Verify a claim against actual BigQuery data."""
    
    # 1. Find the receipt
    receipt = get_receipt(receipt_id)
    if not receipt:
        return ClaimVerification(
            claim=claim,
            receipt_id=receipt_id,
            verification_method=verification_sql,
            actual_result="RECEIPT NOT FOUND",
            verdict="REFUTED"
        )
    
    # 2. Run verification query
    actual_result = bigquery.query(verification_sql)
    
    # 3. Compare
    if actual_result > 0:
        verdict = "CONFIRMED"
    else:
        verdict = "REFUTED"
    
    return ClaimVerification(
        claim=claim,
        receipt_id=receipt_id,
        verification_method=verification_sql,
        actual_result=str(actual_result),
        verdict=verdict
    )
```

### Step 4: Store Proof

```python
def store_proof(verification: ClaimVerification):
    """Store verification proof in BigQuery."""
    bigquery.insert("claim_verifications", verification.model_dump())
```

---

## Binary Validations (Impossible to Hallucinate)

### Test 1: Schema Import

```bash
python3 -c "from schemas.observation import Observation; print('PASS')" > /tmp/test.log 2>&1
```

**Binary check:** Exit code 0 AND output contains "PASS"
**Receipt:** File hash of test.log
**Claim reference:** "See receipt {hash}"

### Test 2: BigQuery Write

```python
receipt = storage.write_observation(obs)
verification = f"SELECT COUNT(*) FROM fact_market_observation WHERE observation_id = '{obs.observation_id}'"
```

**Binary check:** COUNT > 0
**Receipt:** Insert result
**Claim reference:** "See receipt {receipt_id}"

### Test 3: Pipeline End-to-End

```python
# Run pipeline
observations = gmail_import.run(subject, body)

# Write to BigQuery
for obs in observations:
    receipt = storage.write_observation(obs)

# Verify all written
for receipt in receipts:
    count = bigquery.query(f"SELECT COUNT(*) FROM ... WHERE id = '{receipt.outputs['id']}'")
    assert count > 0, f"Hallucination: receipt {receipt.receipt_id} not found in BigQuery"
```

**Binary check:** Every receipt has corresponding BigQuery row
**Receipt:** List of write receipts + verification queries
**Claim reference:** "See receipts {list}"

---

## Red Team Checklist

Before claiming "system works", verify:

- [ ] Every schema import has test output
- [ ] Every BigQuery write has verification query
- [ ] Every pipeline run has log file
- [ ] Every claim references a specific receipt
- [ ] Every receipt is verifiable against BigQuery
- [ ] No claim has "UNVERIFIABLE" verdict

---

## The Rule

> **If the receipt doesn't exist, the claim is a hallucination.**
> **If the verification fails, the claim is a hallucination.**
> **If the agent can't produce a receipt, it didn't do the work.**
