# TESTING.md — Testing Protocol

*The only primitive is a successful test of greater complexity.*
*Never sleep. Always be running tests or starting the next one.*
*Never timeout. Never pkill. Always be available.*

---

## Rule: Tests Are The Only Progress

Code that hasn't been tested doesn't exist. Documentation without test evidence is fiction. The only way to prove something works is to run it against real infrastructure and show the output.

---

## Resource Check (Before Every Test)

Check RAM and CPU before running. Never go below 500MB available RAM.

```bash
# Check available RAM (must be > 500MB)
free -m | awk '/^Mem:/{print $7}'  # available column
# If < 500MB: stop and wait

# Check CPU load
uptime | awk -F'load average:' '{print $2}'
# If load > 4.0: wait before starting heavy tests
```

**Rule:** If available RAM < 500MB, do not start new tests. Wait for current tests to finish.

---

## Starting Tests (nohup + PID)

Always start tests in background with nohup. Never sleep after starting. Always be available to user.

```bash
# Start test, capture PID
nohup python3 test_script.py > /tmp/test_logs/test_YYYYMMDD_HHMMSS.log 2>&1 &
TEST_PID=$!
echo "Test started, PID: $TEST_PID"

# NEVER: sleep, wait, timeout
# ALWAYS: continue with other work, check back later

# Check results later
cat /tmp/test_logs/test_*.log | tail -20
```

**Kill by PID, never pkill:**
```bash
# Kill specific test by PID
kill $TEST_PID

# NEVER: pkill -f test_script
# pkill is dangerous - it can kill unrelated processes
```

---

## Test Log Storage

All test logs go to `/tmp/test_logs/` with timestamped filenames.

```bash
mkdir -p /tmp/test_logs

# Log format: test_YYYYMMDD_HHMMSS.log
# After test completes, move to persistent storage:
cp /tmp/test_logs/test_*.log /root/drop/logs/
```

After test completes, read the log and write a machine-readable report.

---

## Test Report Format

After every test run, write a report to `/root/drop/logs/reports/`:

```json
{
  "test_id": "test_schemas_20260908_120000",
  "test_file": "tests/test_schemas.py",
  "started_at": "2026-09-08T12:00:00Z",
  "completed_at": "2026-09-08T12:00:05Z",
  "duration_seconds": 5,
  "resource_check": {
    "ram_available_mb": 1200,
    "cpu_load": 0.5
  },
  "tests_run": 11,
  "tests_passed": 11,
  "tests_failed": 0,
  "result": "PASS",
  "test_results": [
    {"name": "test_observation_import", "result": "PASS", "duration_ms": 12},
    {"name": "test_observation_instantiate", "result": "PASS", "duration_ms": 8}
  ]
}
```

---

## Test Complexity Ladder

Every capability must pass all lower levels before claiming higher levels.

### Level 1: Import Test
```bash
python3 -c "from schemas.observation import Observation; print('OK')"
```
**Passes if:** Module imports without error.

### Level 2: Instantiate Test
```python
obs = Observation(
    entity_type="test",
    entity_id="TEST-001",
    field="price",
    value=100.0,
    source=EvidenceSource.MANUAL,
    source_grade=EvidenceGrade.C,
)
assert obs.entity_id == "TEST-001"
```
**Passes if:** Object created with correct values.

### Level 3: Pipeline Test (Mock Data)
```python
from pipelines.gmail_import import GmailImportPipeline
gmail = GmailImportPipeline()
obs = gmail.run("[Test] 2026-09-07 08:00", "Total sellers: 5", probe_id="test")
assert len(obs) > 0
```
**Passes if:** Pipeline produces output from mock input.

### Level 4: Storage Write Test (Real BigQuery)
```python
storage.write_observation(obs)
result = storage.client.query("SELECT COUNT(*) as cnt FROM drop.fact_market_observation").result()
for row in result:
    assert row.cnt > 0
```
**Passes if:** Data written to BigQuery and verifiable.

### Level 5: Storage Read Test (Real BigQuery)
```python
observations = storage.read_observations(candidate_id="TEST-001")
assert len(observations) > 0
assert observations[0]["field_name"] == "price"
```
**Passes if:** Data read from BigQuery matches what was written.

### Level 6: End-to-End Test (Real Email → BigQuery)
```python
# 1. Fetch real email from Gmail
# 2. Parse through Gmail import pipeline
# 3. Write observations to BigQuery
# 4. Read back and verify
# 5. Clean up
```
**Passes if:** Full chain works with real data.

### Level 7: Multi-Step Pipeline Test
```python
# 1. Gmail import → observations
# 2. State machine → transition
# 3. Hypothesis ledger → evidence update
# 4. Kernel generator → kernels
# 5. All results in BigQuery
```
**Passes if:** Multiple pipeline steps compose correctly.

---

## What Counts as "Tested"

| Claim | Required Test |
|-------|---------------|
| "Schema works" | Level 1 + 2 |
| "Pipeline works" | Level 3 |
| "BigQuery works" | Level 4 + 5 |
| "End-to-end works" | Level 6 |
| "System works" | Level 7 |

**Never claim "it works" without showing test output.**

---

## Anti-Cheat Measures

Agents cannot claim work is done without verifiable proof.

### Evidence Gates

Every claim must pass an evidence gate:

| Claim | Required Proof |
|-------|----------------|
| "Tests pass" | Test log output showing "RESULT: PASS" |
| "BigQuery works" | BigQuery query showing row count > 0 |
| "Pipeline works" | End-to-end test output with timestamps |
| "Code committed" | Git diff showing actual changes |

### Behavioral Analysis

Detect anomalies:
- Agent claims "11 observations" but BigQuery has 0
- Agent claims "tests pass" but log shows failures
- Agent claims "BigQuery works" but connection test fails

### Content-Addressed Verification

Hash test output, store in BigQuery, verify hash matches claimed output.

### Cross-Reference Checking

Agent says X, reality shows Y:
```python
# Agent claims:
assert observations_written == 11

# Reality check:
result = bigquery.query("SELECT COUNT(*) FROM ... WHERE candidate_id = '...'")
assert result == observations_written  # Must match
```

### Verification Script

```python
from tests.anti_cheat import AntiCheatVerifier

verifier = AntiCheatVerifier()

# Add gates
verifier.add_gate("test_pass", "Tests pass", "Test output shows PASS", "check log", "RESULT: PASS")
verifier.add_gate("bq_write", "BigQuery write", "Data written", "query BigQuery", "count > 0")

# Verify
verifier.verify_test_output("test_schemas", 11, test_log_output)
verifier.verify_bigquery_write("TEST-001", 11)

# Generate report
report = verifier.generate_report()
assert report["verdict"] == "PASS"
```

---

## The Rule

> **If you didn't test it, you didn't build it.**
> **If you didn't log it, you didn't test it.**
> **If you didn't verify it, you didn't prove it.**
> **If the proof doesn't match the claim, you cheated.**
> **If you didn't log it, you didn't test it.**
> **If you didn't report it, you didn't learn from it.**
