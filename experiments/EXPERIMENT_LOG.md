# Experiment Log

*All experiments, reports, and insights from the Drop system.*
*Each experiment is a hypothesis test with receipts.*

---

## Experiment Index

| ID | Date | Type | Status | Receipt |
|----|------|------|--------|---------|
| EXP-001 | 2026-09-08 | Campaign Hypothesis | ACTIVE | FI-HP-CONTROLLER-001 |
| EXP-002 | 2026-09-08 | BigQuery Ingestion | COMPLETE | 314 rows |
| EXP-003 | 2026-09-08 | Cross-Country Query | COMPLETE | 10 tests passed |
| EXP-004 | 2026-09-08 | Pricing Calculator | COMPLETE | 5 products analyzed |

---

## EXP-001: Finland Heat Pump Controller Campaign

**Hypothesis:** Finnish heat pump owners convert through compatibility decision service at CAC < €88.25.

**Data:**
- 1.8M heat pumps installed
- 33% replacement share
- €88.25 net profit (44.1% margin)
- 3 known merchants

**Status:** ACTIVE — waiting for supplier contact

**Receipt:** FI-HP-CONTROLLER-001.md

---

## EXP-002: BigQuery Country Data Ingestion

**Hypothesis:** Country packs can be ingested into BigQuery for cross-country analysis.

**Data:**
- 314 rows ingested (157 NO + 157 FI)
- 16 data types per country
- All queries working

**Status:** COMPLETE

**Receipt:** 314 rows verified in BigQuery

---

## EXP-003: Cross-Country Query Testing

**Hypothesis:** Cross-country queries work on BigQuery.

**Data:**
- 10 tests passed
- Ecosystem comparison working
- Merchant comparison working
- Source-target gaps queryable

**Status:** COMPLETE

**Receipt:** All 10 tests passed

---

## EXP-004: Pricing Calculator Analysis

**Hypothesis:** The z2m pricing calculator can evaluate our candidates.

**Data:**
- 5 products analyzed across multiple markets
- Heat pump controller: BEST (44.1% margin, SCALE recommendation)
- Robot vacuum: GOOD (37.1% margin, SCALE recommendation)
- EV charger: GOOD (33.9% margin, SCALE recommendation)
- Air purifier: GOOD (33.7% margin, SCALE recommendation)
- Davis weather station: MARGINAL (3.7% margin, REJECT in NO)

**Status:** COMPLETE

**Receipt:** Pricing calculator output
