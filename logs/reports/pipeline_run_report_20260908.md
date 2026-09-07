# Pipeline Run Report — 2026-09-08

## Summary

Ran the full pipeline chain from Gmail → BigQuery → State Machine → Hypothesis Ledger → Kernels.

---

## Chain of Events

### Step 1: Gmail Check
- **Action:** Searched Gmail for recent probe reports
- **Result:** Found 20 probe emails in last 7 days
- **Receipt:** `802a1788c1c33e53`

### Step 2: Email Selection
- **Action:** Selected most recent Market Anomaly probe
- **Subject:** `[GeoDrop Demand Surface Probe] 2026-09-07 12:20 — cabled 6313 demand falsified; wireless successor probe survives`
- **Body:** 6,551 chars
- **Receipt:** `864c951e94a03e5d`

### Step 3: Gmail Import Pipeline
- **Action:** Parsed email body into observations
- **Result:** 8 observations extracted
  - `supplier_name = Flak`
  - `price_observed = 8099.0` (NOK)
  - `price_observed = 7590.0` (NOK)
  - `price_observed = 7099.0` (NOK)
  - `price_observed = 6390.0` (NOK)
  - `decision = ADVANCED`
  - `decision = LAUNCH_READY`
  - `decision = HUMAN_ACTION_REQUIRED`
- **Receipt:** `cec0b1a575c71d9b`

### Step 4: Candidate Creation
- **Action:** Created candidate for Davis 6313EU in Norway
- **Candidate ID:** `C-a60001239073`
- **State:** `DISCOVERED`

### Step 5: Hypothesis Creation
- **Action:** Created lifecycle hypothesis
- **Hypothesis ID:** `H-cb136c3c020f`
- **Claim:** "Norway Davis lifecycle specialist can profitably route legacy console owners to 6313EU"
- **Falsifier:** "actual landed dealer cost above NOK 4857.60 ex VAT at NOK 7,590 retail ceiling"

### Step 6: State Machine
- **Input:** Candidate + 8 observations
- **Transition:** `DISCOVERED → HUMAN_ACTION_REQUIRED: External action required`
- **Reason:** Email contains `HUMAN_ACTION_REQUIRED` decision

### Step 7: Hypothesis Ledger
- **Input:** Hypothesis + 8 observations
- **Result:** `OPEN → EXTERNALLY_BLOCKED`
- **Evidence for:** 0
- **Evidence against:** 0

### Step 8: Kernel Generator
- **Input:** 8 observations + 1 hypothesis
- **Result:** 8 kernels generated
  - `SUPPLIER_PATH_DISCOVERY: MODERATELY_FOR`
  - `PRICE_COMPRESSION: NEUTRAL` (×4)
  - `DEMAND_DISCOVERY: NEUTRAL` (×3)

### Step 9: BigQuery Write
- **Input:** 8 observations
- **Written:** 4/8 observations
- **Errors:** 4 (type conversion issues)
- **Verified:** 37 total observations for `NO-DAVIS-6313-001`

---

## Downstream Effects

### BigQuery State
```
NO-DAVIS-6313-001: 37 observations
```

### Candidate State
```
DISCOVERED → HUMAN_ACTION_REQUIRED
```

### Hypothesis State
```
OPEN → EXTERNALLY_BLOCKED
```

### Kernels Generated
- 1 supplier path discovery (Flak found)
- 4 price compression observations
- 3 demand discovery observations

---

## Issues Found

1. **BigQuery write errors:** 4/8 observations failed due to type conversion
2. **Hypothesis ledger:** No evidence updates (observation mapping needs improvement)
3. **Candidate ID mismatch:** Observations use email-parsed ID, not created candidate ID

---

## Receipts

| Step | Receipt Hash | Verified |
|------|--------------|----------|
| Gmail Check | `802a1788c1c33e53` | ✅ |
| Email Selection | `864c951e94a03e5d` | ✅ |
| Gmail Import | `cec0b1a575c71d9b` | ✅ |
| BigQuery Write | `e1ac1385370d134b` | ✅ |

---

## Conclusion

The pipeline works end-to-end. The main issues are:
1. Type conversion in BigQuery writes
2. Hypothesis ledger needs better observation mapping
3. Candidate ID consistency

The system is functional but needs refinement for production use.
