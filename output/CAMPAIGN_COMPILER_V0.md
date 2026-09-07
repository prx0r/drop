# Campaign Compiler v0 — The Vertical Slice

*The product is now: evidence → hypothesis → store → campaign → economics → learning.*
*This document defines Campaign Zero and the compiler architecture.*

---

## The Core Thesis

> **Davis Norway = lifecycle decision commerce**

Not "Norwegian people want weather stations."
But: "Norwegian Davis owners/prospects with complicated compatibility, replacement, migration decisions will convert through a localized decision service."

---

## The Architecture

```
PROBES → OBSERVATIONS → COUNTRY SNAPSHOT + CANDIDATE SNAPSHOT
    ↓
HYPOTHESIS → CAMPAIGN COMPILER → LAUNCH SPEC
    ↓
VALIDATORS → DEPLOYERS → PAUSED CAMPAIGN
    ↓
PREFLIGHT → ACTIVATE → OBSERVATIONS → ECONOMIC OUTCOME
    ↓
BELIEF UPDATE → NEXT EXPERIMENT
```

---

## Campaign Zero: NO-DAVIS-LIFECYCLE-001

### Hypothesis

Norwegian high-intent Davis buyers and existing Davis owners will convert through a localized compatibility/lifecycle decision service at an acquisition cost below realized CM2, because existing merchants inadequately resolve replacement, compatibility, migration and system-selection decisions.

### Causal Mechanism

1. Installed base (498K weather systems in NO)
2. Replacement/upgrade event (console lifecycle)
3. Technical compatibility complexity
4. Fragmented decision support
5. Localized specialist service
6. High purchase intent

### Falsifiers

- No meaningful lifecycle/search demand
- Existing merchants already satisfy decision problem
- Supplier economics fail
- Online resale prohibited
- Actual CPC implies impossible break-even CVR
- Compatibility users engage but do not progress commercially

### Store Structure

```
/
├── Davis system chooser
├── Existing Davis owner?
├── Replace / upgrade
├── Console vs WeatherLink Live
├── Vantage Vue vs Pro2
├── Compatibility
├── Cabin monitoring
├── Winter operation
├── Home Assistant / API
└── Products
```

### Activation Gates

- supplier_authorized: true
- online_resale_allowed: true
- exact_supplier_cost: true
- landed_cost_verified: true
- positive_cm1: true
- positive_cm2_at_test_assumptions: true
- keyword_data_authenticated: true
- break_even_cpc_above_market_cpc: true
- products_in_stock: true
- merchant_center_approved: true
- checkout_test_passed: true
- conversion_tracking_test_passed: true
- shipping_policy_verified: true
- return_policy_verified: true
- consent_implementation_verified: true

---

## The Three New Objects

### A. CampaignHypothesis

Scientific proposition with explicit falsifiers.

### B. LaunchSpec

Complete desired external configuration (store, merchant, ads, measurement, economics).

### C. Deployment

What actually exists externally (diff from LaunchSpec).

---

## Commands

```bash
drop campaign compile NO-DAVIS-LIFECYCLE-001
drop campaign plan NO-DAVIS-LIFECYCLE-001
drop campaign apply NO-DAVIS-LIFECYCLE-001 --paused
drop campaign preflight NO-DAVIS-LIFECYCLE-001
drop campaign activate NO-DAVIS-LIFECYCLE-001
drop campaign observe NO-DAVIS-LIFECYCLE-001
drop campaign pause NO-DAVIS-LIFECYCLE-001
```

---

## The Acceptance Test

> Starting only with the frozen country/candidate/evidence snapshots for Davis Norway, can a fresh agent invoke one command and produce the exact same complete, validated, paused ecommerce experiment without inventing any business fact?

If yes: reusable machine.
If no: what required improvisation becomes another schema field.
