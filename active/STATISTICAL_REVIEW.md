# Statistical Review: P0 Issues

*Critical issues identified in peer review. Must fix before trusting rankings/confidences.*

---

## P0 Issues (Fix Now)

### 1. Fabricated funnel observations in pipeline.py
- **Status:** NOT IN CURRENT CODEBASE (was in planned integration)

### 2. Missing data encoded as zeros
- **Status:** FIXED in unified_scorer.py (EvidenceType enum: UNKNOWN vs OBSERVED_ZERO)

### 3. Beta(1,1) prior for sub-1% CVR
- **Status:** FIXED in bayesian_v2.py (hierarchical empirical priors)

### 4. Gaussian approximations
- **Status:** FIXED in bayesian_v2.py (exact Beta via scipy.stats.beta)

### 5. Multiple scoring pipelines
- **Status:** FIXED in unified_scorer.py (ONE canonical path)

### 6. contribution/contribution_margin mismatch
- **Status:** FIXED in unified_scorer.py (standardized field names)

### 7. Country CPC formula bug
- **Status:** FIXED (removed static country CPC assumptions)

### 8. Norway/EU tax logic wrong
- **Status:** FIXED in cross_border.py (5 distinct regimes)

## P1 Issues (Fix Soon)

- Implement EvidenceObservation objects with provenance
- Introduce hierarchical CVR/CPC priors
- Replace confidence multiplier with probabilistic uncertainty
- Replace heuristic EVOI with posterior-predictive EVSI
- Store prediction snapshots for calibration

## P2 Issues (Fix Later)

- Build Good Seller Gap as frozen feature model
- Implement randomized visitor-level experiments
- Model free listings as low-fidelity observations

## Key Quote

> Don't build a machine that says "Weather stations are 74/100, confidence 85%, therefore launch."
> Build a machine that says "Posterior probability of positive fulfilled contribution is 61%. Uncertainty is primarily supplier discount and paid CVR. Next experiment: ask distributor for dealer pricing."
