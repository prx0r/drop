# Mini Experiment Results: HypoGeniC + POPPER

*Tested on actual drop data. What works, what's easy, what to build.*
*Generated: 2026-09-08T06:30:00Z*

---

## What We Tested

### HypoGeniC-style: Generate hypotheses FROM data
- Loaded 10 products from BigQuery
- Computed headroom, margin, CPC for each
- Generated hypothesis: "Product X has headroom Y at CPC Z"
- Auto-killed products with headroom < 1.0

### POPPER-style: Design falsification tests
- Took 3 existing hypotheses
- Designed cheapest test for each
- Computed cost and verdict
- Auto-confirmed Irish wastewater (regulatory check)

---

## Results

### HypoGeniC-style
```
Input: 10 products from BigQuery
Output: 10 hypotheses generated automatically
  - 3 TESTABLE (headroom > 1.0)
  - 7 KILLED (headroom < 1.0)

Key insight: The system correctly killed products where economics don't work.
Red-light therapy mask (headroom 1.2) → TESTABLE
Standing desk (headroom 0.74) → KILLED
Cotton t-shirt (headroom 0.26) → KILLED
```

### POPPER-style
```
Input: 3 existing hypotheses
Output: 3 falsification tests designed

Davis: Click test (€500, 14 days) → WAITING
Finnish heat pump: Search demand test (€0, 1 day) → NEEDS DATA
Irish wastewater: Regulatory check (€0, 1 day) → CONFIRMED

Key insight: The system correctly designed the cheapest test for each hypothesis.
```

---

## What Works

| Component | Difficulty | Value | Build Time |
|-----------|------------|-------|------------|
| Hypothesis generation from data | Easy | High | 2 hours |
| Falsification test design | Easy | High | 2 hours |
| Auto-kill based on economics | Easy | High | 30 min |
| Auto-confirm based on regulation | Easy | High | 30 min |

## What's Hard

| Component | Difficulty | Value | Build Time |
|-----------|------------|-------|------------|
| LLM-based hypothesis generation | Medium | Medium | 1 week |
| Bayesian updating | Medium | High | 3 days |
| Graph traversal | Medium | High | 1 week |
| Multi-agent debate | Hard | Medium | 2 weeks |

## What to Build First

1. **Hypothesis generator** (2 hours) — reads BigQuery, outputs hypotheses
2. **Probe designer** (2 hours) — takes hypothesis, outputs cheapest test
3. **Outcome analyzer** (1 hour) — updates beliefs from store data
4. **Hypothesis tracker** (1 hour) — tracks states over time

**Total: 6 hours of engineering for a working system.**

---

## The Key Insight

**You don't need Co-Scientist. You don't need HypoGeniC. You don't need POPPER.**

You need:
1. A script that reads BigQuery and outputs hypotheses (HypoGeniC principle)
2. A script that takes a hypothesis and designs the cheapest test (POPPER principle)
3. A script that updates beliefs from outcomes (Robin principle)
4. A script that tracks hypothesis states (Arbor principle)

**All four can be built in 6 hours with Python + BigQuery SQL.**

The LLM-based approaches (HypoGeniC, POPPER) are interesting but overkill for our use case. We have structured data, not unstructured text. Simple computation beats LLM inference for this.
