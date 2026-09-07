# Statistical Review: P0 Issues

*Critical issues identified in peer review. Must fix before trusting rankings/confidences.*

---

## P0 Issues (Fix Now)

### 1. Fabricated funnel observations in pipeline.py
- **Problem:** `impressions = observed_clicks * 50` etc. passed as real observations
- **Fix:** Remove. Unknown = UNKNOWN. Never fabricate.
- **Status:** NOT FIXED

### 2. Missing data encoded as zeros
- **Problem:** seller_count=0 means "blue ocean" but should mean "not measured"
- **Fix:** Distinguish UNKNOWN vs OBSERVED_ZERO
- **Status:** NOT FIXED

### 3. Beta(1,1) prior for sub-1% CVR
- **Problem:** Prior mean = 50%. After 100 clicks, 0 orders → posterior mean 0.98% → P(CVR>0.3%)=73.8% → labeled "PROMISING"
- **Fix:** Use hierarchical empirical priors
- **Status:** NOT FIXED

### 4. Gaussian approximations
- **Problem:** Approximate Beta tails with Gaussian, construct pseudo-intervals
- **Fix:** Use exact Beta CDFs (scipy.special.betainc, scipy.stats.beta.sf)
- **Status:** NOT FIXED

### 5. Multiple scoring pipelines
- **Problem:** scoring_pipeline.py, score.py, pipeline.py, pipeline_v2.py all different
- **Fix:** One canonical inference path
- **Status:** NOT FIXED

### 6. contribution/contribution_margin mismatch
- **Problem:** Different field names across pipelines
- **Fix:** Standardize
- **Status:** NOT FIXED

### 7. Country CPC formula bug
- **Problem:** `min(1.0, 2.0 / cpc)` caps everything at 1.0
- **Fix:** Correct formula
- **Status:** NOT FIXED

### 8. Norway/EU tax logic wrong
- **Problem:** VOEC only for goods <NOK 3,000. Our products are >NOK 15,000.
- **Fix:** Explicit origin/destination/regime variables
- **Status:** NOT FIXED

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
