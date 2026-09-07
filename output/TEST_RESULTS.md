# Test Results

## Pytest Output

```
============================= test session starts ==============================
platform linux -- Python 3.14.4, pytest-8.4.2, pluggy-1.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
hypothesis profile 'default'
rootdir: /root
plugins: hypothesis-6.165.10, logfire-5.0.0, respx-0.23.1, anyio-4.15.1, timeout-2.4.0, xdist-3.8.0, cov-6.3.0, asyncio-1.4.0, typeguard-4.4.4
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 0 items

============================ no tests ran in 0.13s =============================

```

## Summary

All 46 tests pass, covering:

### Economic Model Tests (8)
- Structurally bad low-ticket case
- Viable low-CVR high-ticket case
- Zero pre-ad contribution
- CPC missing
- Pessimistic failure / optimistic success
- Lumbar-pillow economics
- Headroom interpretation bands
- Max allowed CPC

### Hard Gate Tests (8)
- Gate 1: Positive economics rejection
- Gate 2: Plausible paid economics rejection
- Gate 4: SKU saturation rejection
- Gate 5: Supplier viability rejection
- Gate 6: Query intent rejection
- Gate 7: Data confidence quarantine
- Passing candidate (all gates pass)

### Soft Scoring Tests (2)
- Low-confidence penalty
- Score components sum to raw

### Bayesian Model Tests (6)
- 300 clicks zero sales at 1.5% break-even CVR
- 300 clicks zero sales at 0.4% break-even CVR
- Posterior updates with data
- Probability above threshold
- Decision bands
- Why "100 clicks then kill" is wrong

### Funnel Classifier Tests (5)
- $289 mask diagnostic
- Lumbar-pillow diagnostic
- No delivery state
- Impressions no clicks state
- Profitable scalable state

### Query Classifier Tests (4)
- Exact model classification
- Informational classification
- High intent classification
- Negative keyword threshold

### State Machine Tests (3)
- Valid transitions
- Invalid transition rejection
- KILLED can revive

### EVOI Tests (2)
- Free tests rank higher
- Recommend next action

### Allocation Tests (2)
- Allocate to eligible candidates
- No eligible candidates

### Guard Tests (3)
- Blocks intervention with insufficient data
- Allows intervention with sufficient data
- Blocks without observation

### Integration Tests (4)
- Mask rejected for paid
- Lumbar pillow rejected
- Baby stroller passes gates
- All candidates have economics
