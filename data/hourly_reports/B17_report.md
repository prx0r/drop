# GoldProbe B17 — UK Fire-Door Inspection / Remediation

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled

## Executive result

**B17 falsifies the strong Germany-elevator mechanism at the routine inspection layer.**

The Fire Safety (England) Regulations require buildings over 11m to:
- check communal fire doors every **3 months**
- use best endeavours to check flat entrance doors every **12 months**.

But current government guidance deliberately says these checks should be **simple and basic**, require **no specialist**, and involve **no tools**.

Source:
https://www.gov.uk/government/publications/fire-safety-england-regulations-2022-fire-door-guidance/fire-safety-england-regulations-2022-fire-door-guidance

So unlike a German ZÜS elevator report, the normal Regulation 10 check is **not intended to be a technical purchase specification**.

The emerging structure is:

`mandatory simple screen -> access/evidence -> suspicious defect -> specialist assessment if needed -> mostly minor remediation`

That is a fundamentally different market.

## 1. Current broad building-stock context

MHCLG currently estimates:
- **39,000–59,000** residential buildings at 11–18m
- about **12,000** at 18m+.

Broad derived 11m+ stock context: **51,000–71,000 buildings**.

Source:
https://www.gov.uk/government/publications/building-safety-remediation-monthly-data-release-may-2026/building-safety-remediation-technical-note-may-2026

This is not a direct Regulation 10 building register.

## 2. The recurring compliance clock is hard law

From 23 January 2023, responsible persons for multi-occupied residential buildings over 11m must:
- quarterly check communal fire doors
- annually, on a best-endeavours basis, check flat entrance doors.

Source:
https://www.gov.uk/government/publications/fire-safety-england-regulations-2022

The checks include self-closing devices.

## 3. But government explicitly prevents over-engineering the check

Government guidance says:
- checks should be simple/basic
- caretakers, managing agents, housing officers or maintenance staff can do them with instruction
- no specialist is normally needed
- no tools are intended.

The deeper question of whether the door has adequate inherent fire performance belongs to the fire risk assessment / Fire Safety Order, not Regulation 10.

This is the crucial B17 distinction.

## 4. Access, not door technology, is a major bottleneck

Flat entrance doors must be seen from both sides.

Government says:
- arrange with residents in advance
- offer multiple times
- record every attempt
- document non-access
- persistent refusal may ultimately require legal action.

Source:
https://www.gov.uk/government/publications/fire-safety-england-regulations-2022-fire-door-guidance/fire-safety-england-regulations-2022-fire-door-guidance

Sentry's 2026 FOI study makes this measurable.

Across its local-authority dataset:
- only **46% of flat entrance doors** had been checked at least once since the rules began
- **89% of communal doors** had.

That is a **43-percentage-point gap**.

Source:
https://www.fia.uk.com/news/sentry-fire-safety-group-report-highlights-gaps-in-social-housing-fire-door-compliance.html

The study itself identifies dwelling access as a key barrier.

Important: "checked at least once since 2023" is not the same as annual compliance.

### New candidate: `ACCESS_FRICTION_BEFORE_TECHNICAL_FRICTION`

When the legal inspection sits inside someone's home, the scheduling/access proof can be harder than the physical inspection.

## 5. The social-housing backlog is real, but the source needs careful handling

Sentry sent FOIs to **296** English local authorities:
- **261** responded
- **176** provided usable information.

Its report says **106,718** fire doors were identified as non-compliant in the responding social-housing stock and only **37%** had been repaired/replaced, leaving **>66,000** outstanding.

The arithmetic 63% remainder is about **67,232** doors, but the report's own wording stays authoritative.

Source:
https://sentrydoors.co.uk/wp-content/uploads/2026/03/Fire-Safety-In-Social-Housing.pdf

FIA's independent summary confirms that **63% of identified non-compliant doors remained awaiting repair/replacement** and **51% of responding authorities lacked a formal remediation plan**.

Source:
https://www.fia.uk.com/news/sentry-fire-safety-group-report-highlights-gaps-in-social-housing-fire-door-compliance.html

But this is vendor-initiated FOI research and does not cover housing associations cleanly.

## 6. Professional inspections reveal a repair-heavy rather than replacement-heavy market

Latest FDIS 2025 inspection data:
- **72%** of professionally inspected doors did not pass
- **70% of those failures required only minor remedial works**.

Common issues:
- excessive gaps
- smoke sealing
- care/maintenance.

Source:
https://www.furnitureproduction.net/news/fdis-ltd-achieves-ukas-accreditation-for-inspector-certification

This is a selected professional-inspection sample, **not** a national failure probability.

Still, it strongly changes the commercial workflow:

`inspection failure != replacement sale`

Most flagged doors in that sample were minor-remediation jobs.

## 7. Professional inspection itself is formalizing

FDIS has become the first UK scheme reported as UKAS-accredited for individual fire-door inspector competence under ISO/IEC 17024.

That supports a two-tier market:

**routine legal screen**
vs
**escalated competent professional inspection**.

## 8. Current price architecture reinforces the distinction

A current 2026 commercial market guide gives:
- routine check: **£15–£35/door**
- detailed certificated inspection: **£40–£90/door**
- typical minor remediation: **£40–£150/door**
- FD30 doorset replacement: **£800–£1,500 supplied/fitted**.

Source:
https://riskfire.org.uk/fire-door-inspection-cost-calculator

Another current provider guide prices annual flat-entrance inspection around **£35–£75/door**, explicitly including resident correspondence and no-access logging.

Source:
https://firedoorinspectionapp.starkcontracts.co.uk/blog/fire-door-inspection-cost-uk

Those are vendor/market-guide prices, not audited transaction averages.

## 9. Compliance precision can prevent expensive over-replacement

This is perhaps B17's most valuable conceptual finding.

Government explicitly says:
- existing flat entrance doors are **not** automatically required to satisfy current new-build standards
- a door that met the relevant standard when installed can remain adequate
- absence of intumescent strips/smoke seals or modern certification **does not by itself mean the door is unfit**.

Source:
https://www.gov.uk/government/publications/fire-safety-england-regulations-2022-fire-door-guidance/fire-safety-england-regulations-2022-fire-door-guidance

That matters when a replacement can cost around £800–£1,500 while many defects can be fixed for tens/hundreds.

### `COMPLIANCE_PRECISION_AVOIDS_CAPEX`

> Applying the wrong modern standard to a legacy asset can create unnecessary replacement spend. Correct regulatory interpretation is itself an economic service.

This is a better and more precise mechanism than "regulation creates demand."

## 10. Inspection and remediation are often commercially integrated

One current provider explicitly sells:
- standalone inspection report
- then separately itemized remedial quote
- refurbishment
- replacement.

Source:
https://dcsecurity.co.uk/fire-door-survey-cost

So even once a specialist inspection exists, the original inspector can capture remediation.

That weakens a neutral report marketplace.

## 11. Best B17 product cell

Not:
> Find me a fire-door inspector.

Potentially:

### Fire-Door Compliance Operations Layer

For managing agents/social landlords:

1. building/door register
2. resident communications
3. appointment windows
4. quarterly communal schedule
5. annual flat-door schedule
6. mobile visual checklist/photo evidence
7. no-access attempt log
8. rules for specialist escalation
9. minor-remedial work order
10. re-check evidence
11. correct building-era compliance context to prevent unnecessary replacement.

The key is **operations + triage + evidence**, not pretending every annual check needs an FDIS inspector.

## 12. What B17 falsified

- recurring legal inspection automatically creates a detailed purchase specification
- every Regulation 10 check needs a professional specialist
- professional sample failure rates equal national door failure rates
- missing modern certification means an old door must be replaced
- high failure rate means replacement-heavy economics.

## 13. What B17 supported

- recurring regulation creates substantial workflow
- resident access is a measurable compliance bottleneck
- suspect doors escalate into a specialist market
- most professional-inspection failures in the latest FDIS data are minor-remedial
- precise compliance interpretation can prevent unnecessary CAPEX.

## 14. Orchard update

### `REGULATORY_REPORT_BECOMES_PURCHASE_SPEC`
Now has a boundary condition:

> **inspection depth matters.**

Germany elevator ZÜS:
technical independent inspection → report directly quoteable.

UK fire-door Regulation 10:
simple screen → escalation may be required before a technical remediation scope exists.

New candidate:

### `REGULATION_CREATES_SCREENING_FUNNEL`

And:

### `ACCESS_FRICTION_BEFORE_TECHNICAL_FRICTION`

## 15. Autonomous next probe — B18 England private-rental EICR

This is selected as a direct contrast.

An EICR is a qualified technical inspection with standardized outcomes such as:
- C1
- C2
- FI

and statutory remediation deadlines.

B18 asks:

> **Does a technical regulatory inspection with standardized defect codes produce a much cleaner report-to-private-remediation market than simple fire-door screening?**

That is the exact uncertainty B17 created.
