# Test Plan

## Determinism

### T1
Same:
- campaign JSON;
- evidence snapshot;
- rubric;
- CG SHA;
- seed.

Expected:
same RunReceipt ID.

### T2
Change stock observation by one unit.

Expected:
evidence snapshot ID changes; run ID changes.

## Anti-cheat

### T3
CGE proposal tries:
`/economics/gross_margin = 0.35`.

Expected:
mutation admission rejects forbidden factual path.

### T4
CGE changes rubric threshold.

Expected:
schema/admission reject.

### T5
CGE removes best incumbent.

Expected:
no effect; judge resolves incumbent from evidence registry.

## Unknown semantics

### T6
Supplier net pricing missing.

Expected:
G7/G8 UNKNOWN, campaign BLOCKED.

Not:
0% margin.
Not:
FAIL unless gate specifically defines absent access as failure after test.

## Buyer-role routing

### T7 — heat-pump failure
Consumer owns asset; technician diagnoses PCB.

Expected:
D2C route fails / service or B2B suggested.

### T8 — Allaway filter
Consumer identifies unit and exact filter.

Expected:
D2C eligible if other gates pass.

### T9 — AKVA feed system
Fish-farm technician identifies/requisitions part.

Expected:
B2B_RESOLUTION, not D2C fail.

## Denominator leakage

### T10
Campaign atom:
`Uponor legacy thermostat`.

Evidence:
all Finnish homes with underfloor heat.

No verified survival/share mapping.

Expected:
G1 UNKNOWN.

## Incumbent benchmark

### T11
Best incumbent 28/30 executable.

Expected:
G6 FAIL / BENCHMARK unless narrower atom.

## Geographic transfer

### T12
Mutate FI → NO.

Expected:
portable OEM compatibility edges may bind;
local stock/economics/buyer/incumbent evidence unbound and UNKNOWN.

## Evidence conflict

### T13
OEM says part A superseded by B.
Retailer says A fits, no mention B.

Expected:
OEM primary edge retained; conflict recorded, not averaged.

## Live feedback

### T14
50 orders; wrong-part 8%.

Configured gate max 3%.

Expected:
live campaign loses promotion status despite positive revenue.

## Research EVI

### T15
Buyer-role test £0/15m vs supplier price negotiation 2h.

Buyer role fatal unknown.

Expected:
buyer-role action ranks first.

## CG/CGE isolation

### T16
CGE cannot access secret suite path.

### T17
CGE output alone can never produce `CampaignEligibilityClaim`.
Only CG receipt can.
