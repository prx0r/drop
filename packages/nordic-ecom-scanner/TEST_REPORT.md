# Internal Test Report

**Run date:** 2026-09-04

## Automated test suite

Command:

```bash
PYTHONPATH=src python -m pytest -q
```

Result at packaging time: **11 passed**.

Coverage includes:
- VAT/contribution/CPA/break-even economics;
- relative scoring behavior;
- multi-unit basket economics (CPA paid once per order);
- unverified supplier-match gating;
- electrical/rechargeable-lamp compliance gating;
- seed → SQLite → score → rank end-to-end pipeline;
- Shopping SERP feature extraction;
- Merchant feed validation/export;
- CSV Shopping + CSV keyword provider → observation → SQLite persistence.

## Offline integration demo

The seeded database was initialized, 50 candidates were imported, all 50 were scored and a ranked CSV was exported to `outputs/ranked_demo.csv`.

Important: the seed's retail prices and supplier-category quotes come from live September 2026 observations, but CPC, search volume and landed-cost numbers are intentionally scenario values. They exist so the complete system runs without paid API credentials. Replace them before making a commercial decision.

## Live connectors

Code adapters are present for Serper Shopping and DataForSEO keyword metrics. They were **not called during packaging because no user API credentials were provided**. They use the same provider interface exercised by the CSV integration test.

## Deliberate failure behavior

- missing landed cost → economics not scored;
- negative pre-ad contribution → reject;
- implausibly high break-even CVR → research;
- slow delivery → research;
- missing preferred local payment in Nordic priority markets → research;
- electrical/battery lighting → compliance review before test.
