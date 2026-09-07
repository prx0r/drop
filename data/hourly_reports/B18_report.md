# GoldProbe B18 — England Rented-Sector EICR Inspection → Remediation

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled

## Executive result

**This is the technical positive control B17 was missing.**

An EICR is not a lightweight screen.

Government guidance requires a qualified person, and the report uses standardized classifications:

- **C1** — danger present
- **C2** — potentially dangerous
- **C3** — improvement recommended, not mandatory to make the report satisfactory
- **FI** — further investigation required without delay.

C1/C2/FI trigger qualified remedial/investigative work within **28 days or sooner if the report says so**.

Source:
https://www.gov.uk/government/publications/electrical-safety-standards-in-the-private-and-social-rented-sectors-guidance/electrical-safety-standards-in-the-private-and-social-rented-sectors-guidance

That makes the report a genuine time-bounded procurement object.

## 1. Scale

Official England dwelling stock at 31 March 2025:
- private rented: **5.030m**
- social/affordable rented: **4.201m**

Combined rented stock: **9,231,000 dwellings**.

Source:
https://www.gov.uk/government/statistics/dwelling-stock-estimates-in-england-2025/dwelling-stock-estimates-england-31-march-2025

This is not a count of inspections due today.

A purely mechanical 5-year cycle would imply roughly:
- PRS: **1,006,000/year**
- social: **840,200/year**

if dates were perfectly evenly distributed. They are not.

## 2. Social housing just entered the statutory regime

The 2025 amendment extended the electrical-safety regulations to the social rented sector.

Current government guidance says:
- regulations came into force for social housing on **1 Nov 2025**
- new social tenancies after **1 Dec 2025**
- existing social tenancies: **1 May 2026**
- transitional first checks for existing social tenancies before **1 Nov 2026**.

Source:
https://www.gov.uk/government/publications/electrical-safety-standards-in-the-private-and-social-rented-sectors-guidance/electrical-safety-standards-in-the-private-and-social-rented-sectors-guidance

But do **not** call 4.2m social dwellings a new inspection TAM. Government says most social landlords were already doing five-year checks.

## 3. The report carries standardized actionable semantics

Government explicitly maps:
- C1 → danger
- C2 → potentially dangerous
- C3 → recommendation only
- FI → investigate without delay.

If C1 or C2 appears, the installation is unsatisfactory for continued use.

That is far more machine-usable than the B17 fire-door routine checklist.

## 4. The report starts a clock

Landlords must:
1. complete required remedial/investigative work within **28 days**, or sooner if the report specifies;
2. use a qualified person;
3. obtain written confirmation;
4. provide the report and confirmation to tenant/council.

Acceptable evidence includes:
- satisfactory EICR
- EIC
- MEIWC
- other appropriate electrical certification.

A local council can serve remedial notices, arrange work itself in qualifying cases and recover costs.

Current central government guidance says financial penalties can reach **£40,000** for specified breaches from 1 May 2026.

This corrects older pages that still mention £30,000.

## 5. There are real enforcement transactions

West Suffolk's August 2026 case is unusually high resolution.

One landlord's EICR contained:
- **7 C1 defects**
- **14 C2 defects**.

The council took urgent action on immediate dangers and served a remedial notice for the remaining potentially dangerous work.

Source:
https://www.westsuffolk.gov.uk/news/pr20260820ws01.cfm

This is exactly:

`coded diagnosis -> deadline -> private/public remediation`.

## 6. The report is portable between suppliers

KLIC Electrical explicitly says:
- the landlord does **not** need the same electrician
- it will accept another electrician's EICR
- it can quote the required remedials from that report.

Source:
https://klic-electrical.co.uk/services/safety/remedial-works

EICR Pro goes further:

> If another contractor wrote the report, send it over and it will price against it.

Source:
https://eicr-pro.co.uk/remedial-works.html

That gives B18:

### `STANDARDIZED_DEFECT_CODES_ENABLE_PORTABLE_REMEDIATION`

This is the exact missing condition from B17.

## 7. But this business model already exists

EICR Compliant currently offers two paths:

- book a new EICR
- **upload an existing / failed EICR for remedial quote review**.

Current inspection offer starts around **£129 up to 10 circuits**.

Source:
https://eicrcompliant.co.uk/

So the mechanism is true, but "upload failed report → get electrician quote" is not undiscovered whitespace.

## 8. Current inspection pricing is fairly commoditized

Now Electrics current London fixed prices:
- studio/1–2 bed: **£130**
- 3 bed: **£150**
- 4 bed: **£175**
- 5 bed: from **£195**
- remedials quoted separately.

Source:
https://nowelectrics.co.uk/

A current broader price guide gives:
- 1–2 bed flat: **£100–£180**
- 2–3 bed house: **£150–£250**
- 4 bed: **£200–£320**
- HMO: **£300–£500+**
- re-test: **£50–£100**
- bonding: **£120–£200**
- RCBO circuit work: **£120–£160**
- consumer unit: **£450–£800**.

Source:
https://www.dominicbowkett.com/journal/eicr-cost/

These are commercial guide prices, not audited transaction averages.

## 9. The neutral opportunity, if any, is above basic routing

Because same-company inspection/remediation is convenient and already common, the independent layer needs to do more than forward a PDF.

Potentially:

### EICR Remediation Normalizer

Upload report.

System extracts:
- C1
- C2
- FI
- C3
- circuit
- observation text
- deadline.

Then:
1. separate mandatory vs optional items
2. convert observations into comparable work packages
3. get multiple qualified remedial quotes
4. flag scope differences
5. track 28-day deadline
6. collect EIC/MEIWC completion evidence
7. maintain tenant/council record.

The real value is **comparison + evidence + time control**, not "find electrician."

## 10. Access friction replicates from B17

Government explicitly addresses tenants refusing access and tells landlords to retain communications showing reasonable steps.

Source:
https://www.gov.uk/government/publications/electrical-safety-standards-in-the-private-and-social-rented-sectors-guidance/electrical-safety-standards-in-the-private-and-social-rented-sectors-guidance

Oxford City Council's May 2026 data says its remaining EICR exceptions were primarily associated with **no-access** situations, alongside rewiring/certificate-processing issues.

Source:
https://www.oxford.gov.uk/landlord-performance/council-housing-service-performance-2026/2

So `ACCESS_FRICTION_BEFORE_TECHNICAL_FRICTION` now has a second safety regime.

## 11. There is no honest national EICR failure rate in this run

One London provider says **38%** of its rental EICRs failed initially in 2024.

Source:
https://londoneicrcertificates.co.uk/blog/eicr-certificate-cost-for-landlords-london/

Useful vendor sample.

Not national evidence.

Sandwell's November 2025 portfolio snapshot had:
- 24,778 satisfactory
- 1,586 unsatisfactory
- **5.9% unsatisfactory** stock status.

That's not an inspection failure rate either.

So GoldProbe keeps national unsatisfactory probability = **null**.

## 12. Regulatory expansion is interesting but easy to overstate

Government estimated social-sector inspection cost around:
- **£170.67/property** for private registered providers
- **£164.80/property** for local authorities.

Source:
https://www.gov.uk/government/calls-for-evidence/electrical-safety-in-social-housing-consultation-and-call-for-evidence/consultation-and-call-for-evidence-on-electrical-safety-in-the-social-rented-sector

But the same government analysis says most social landlords already checked every five years.

### `REGULATORY_SCOPE_EXPANSION_CREATES_COMPLIANCE_COHORT`
remains a **weak candidate**, not a proven market boom.

## 13. B18 vs B17 gives us a clean causal distinction

### Fire door Regulation 10
simple visual check  
no specialist  
no tools  
flags concern  
→ specialist may be needed.

### EICR
qualified electrical testing  
standard C1/C2/C3/FI semantics  
mandatory deadline  
completion certification  
→ another qualified supplier can directly remediate.

So the real predictor is:

### `INSPECTION_DEPTH × REPORT_STANDARDIZATION`

not "regulated market".

## 14. Orchard update

### `REGULATORY_REPORT_BECOMES_PURCHASE_SPEC`
Now has:

**positive:** Germany elevator ZÜS  
**negative/simple-screen control:** UK fire doors  
**positive:** England EICR.

The mechanism is becoming legitimate.

### `ACCESS_FRICTION_BEFORE_TECHNICAL_FRICTION`
**replicated directionally**:
- flat entrance doors
- occupied rented-home EICRs.

## 15. Autonomous next probe — B19 UK MOT vehicle defects

This is intentionally outside building services.

MOT gives us:
- annual mandatory technical inspection
- standardized defect severity
- enormous installed base
- owner can choose repair garage
- retest workflow
- mature same-site test/repair market.

The question:

> **If standardized defect codes make a report portable, does the test station's same-site convenience capture the remediation transaction so efficiently that a neutral report marketplace becomes worthless?**

That tests whether report portability is merely necessary—not sufficient—for middleman economics.
