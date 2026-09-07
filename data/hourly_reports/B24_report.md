# GoldProbe B24 — NYC FISP Façade Safety → Remediation

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled

## Executive result

**FISP is a cleaner commercial trigger than Local Law 97 because the core state is a physical engineer finding, not a modeled liability. But the generic contractor marketplace is mature. The novel value is the clock.**

NYC Open Data currently exposes **87,023 façade compliance filing rows across 40 fields**, updated every weekday as of **1 September 2026**.

The dataset includes:
- cycle
- BIN
- block/lot
- filing date
- **CURRENT_STATUS**
- QEWI name
- QEWI business.

Source:
https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Safety-Facades-Compliance-Filings/xubg-57si/data

The regulatory condition states are:

```text
SAFE
SWARMP
UNSAFE
NO REPORT FILED
```

The crucial discovery is that **SWARMP is a future-demand state**.

## 1. FISP creates a recurring physical inspection clock

Buildings higher than six stories must have exterior walls/appurtenances inspected periodically and file a technical report.

Current Cycle 10:
- begins 21 Feb 2025
- ends 20 Feb 2030.

Source:
https://home4.nyc.gov/assets/buildings/pdf/cycle10-diagram.pdf

Unsafe conditions must be repaired within **90 days** after the unsafe filing, and an amended report follows after correction.

Source:
https://www.nyc.gov/assets/buildings/html/Facade_Filings_Cycle.html

This is materially more concrete than:
> building's calculated carbon emissions may imply a penalty after adjustment/offset review.

## 2. SWARMP is an explicit future-repair queue

For a SWARMP condition, the QEWI must identify when the condition is expected to become unsafe.

DOB says the completion horizon can be:
- no less than **1 year**
- no more than **5 years**.

And the same condition cannot simply remain SWARMP forever. If a prior-cycle SWARMP condition remains unrepaired and appears again, it must become **UNSAFE**.

Source:
https://home4.nyc.gov/site/buildings/safety/facade-compliance.page

This creates:

# `DEFECT_MATURITY_CLOCK_PRECOMPUTES_FUTURE_DEMAND`

We can know:

```text
safe now
but mandatory repair later
```

years before emergency status.

That is more useful than waiting for `"facade repair near me"` search intent.

## 3. The report is already close to a procurement specification

DOB requires reports to contain:
- current photographs
- location diagrams
- cause/description of deterioration
- repair timeframes
- which work needs a permit
- completion details
- public protection.

Source:
https://www.nyc.gov/site/buildings/safety/facade-report-guidelines.page

So this is another strong `REGULATORY_REPORT_BECOMES_PURCHASE_SPEC` case.

## 4. Unsafe status starts a hard cost clock

Current official filing penalties include:
- late initial filing: **$1,000/month**
- failure to file: **$5,000/year**
- unrepaired SWARMP: **$2,000**
- unsafe conditions: additional recurring schedule.

Source:
https://www.nyc.gov/site/buildings/safety/facade-fees-penalties.page

Under 1 RCNY 103-04, failure-to-correct unsafe penalties include:

Year 1:
**$1,000/month**

Year 2:
**$1,000/month + $10 per linear foot of shed/month**

then progressively larger linear-foot charges in later years.

Source:
https://www.nyc.gov/assets/buildings/pdf/fisp.pdf

## 5. But the more interesting carry cost is the protection itself

An UNSAFE condition often requires public protection:
- sidewalk shed
- fence
- structural netting.

That protection generally remains until the building is properly corrected/reclassified.

The city has now deliberately made long-lived sidewalk protection more expensive.

## 6. The rules changed materially in August 2026

As of 20 August 2026, NYC had **7,427 permitted sidewalk sheds**, more than **1,000 fewer than a year earlier**.

New current process:
- sidewalk-shed permits renew every **90 days**
- owner submits a report describing repair progress
- stronger penalties target sheds where underlying work stalls.

Source:
https://www.nyc.gov/mayors-office/news/2026/08/mamdani-administration-taking-down-sidewalk-sheds-and-improving-

The city says some of the new penalties are expected to begin being imposed in early 2027.

## 7. The statutory idle-shed penalty can become significant

Current NYC Administrative Code:

where qualifying shed work is not progressing during renewal periods:
- <3 years: **$10/linear foot/month**
- 3–4 years: **$100/linear foot/month**
- 4+ years: **$200/linear foot/month**, capped at **$6,000/month**.

Source:
https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-231461

That is separate from the traditional FISP unsafe-condition penalty structure.

## 8. There are also explicit repair milestones now

For qualifying unsafe-facade sheds, current code can impose **$5,000–$20,000** for missing each of these milestones:

- complete construction documents within **5 months**
- diligently pursue permit issuance by roughly **8 months**
- complete repair within **2 years**, absent an approved extension.

Source:
https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-231493

So the regulatory architecture is moving from:

```text
put up shed
→ leave it there
```

to:

```text
shed installed
→ progress clock
→ permit clock
→ construction clock
→ recurring proof
```

## 9. A shed has commercial externalities as well

A city/Mastercard study cited by the Mayor's Office found sidewalk sheds can reduce nearby Manhattan business consumer spending by around:

**$3,900–$9,500 per month.**

Source:
https://www.nyc.gov/mayors-office/news/2025/11/mayor-adams-unveils-new-designs-for-sidewalk-sheds-and-scaffoldi

Important:
this is **not automatically the building owner's direct cash cost**.

It may fall on commercial tenants/neighbors.

But it establishes a real economic externality from slow remediation.

## 10. Current private cost context

One current 2026 NYC restoration contractor guide places:

- mid-rise full façade repointing: **$50k–$200k**
- mid-rise full restoration: **$100k–$500k**
- high-rise full restoration: **$300k–$1.5m+**
- shed install: **$1.5k–$6k**
- shed rental: **$500–$2,000/month**.

Source:
https://nyrestoration.com/facade-repair-cost-nyc/

This is one contractor's guide, not audited market pricing.

Use only for magnitude.

## 11. This produces a new economic mechanism

# `PROTECTION_CARRY_COST_ACCELERATES_REMEDIATION`

The owner isn't comparing only:

```text
repair now
vs
repair later
```

They may be comparing:

```text
repair now
```

against:

```text
repair later
+ shed rental
+ unsafe penalties
+ inactivity penalties
+ milestone penalties
+ permit renewals
+ public/tenant externality
```

Therefore **time-to-remediation** itself has measurable financial value.

## 12. Current open data is extremely useful

The FISP dataset has:
- 87k filing records
- named QEWI professionals/businesses
- condition history
- filing dates
- building IDs.

This creates another possible asset:

## QEWI / condition-transition graph

Potential analysis:

```text
QEWI
× building type
× condition
× filing date
× amended filing
× SAFE transition
```

We must control for building complexity before ranking providers.

But it is a rare public compliance dataset where both asset and diagnosing professional are explicit.

## 13. Generic FISP intermediation is mature

FISP dates to 1980, and NYC has a mature ecosystem of:
- QEWIs
- engineering firms
- façade contractors
- scaffold/shed firms
- expediters
- property managers.

Current private industry estimates put the covered universe above 12,500 buildings.

Source:
https://www.locallaw11.com/

That number is not official current universe data.

So:

> FISP contractor marketplace

is not the discovery.

## 14. Better product

### Façade Condition Clock

For owner/property manager portfolio:

```text
BIN
current FISP state
last state
QEWI
SWARMP expected unsafe date
repair due date
unsafe day 0
extension state
shed permit age
permit renewal clock
repair-document milestone
permit milestone
completion milestone
amended filing
```

Then:

1. forecast future mandatory repairs
2. prioritize by carry cost
3. normalize QEWI scopes
4. obtain comparable bids
5. monitor permits/progress
6. calculate likely direct delay cost
7. alert before SWARMP→UNSAFE transition.

This is substantially stronger than waiting for emergency jobs.

## 15. B23 vs B24

### B23 LL97
condition = calculated emissions exposure  
liability = adjustable/mitigable  
final property audit data still emerging.

### B24 FISP
condition = engineer-observed physical safety state  
repair clock = explicit  
public protection = physical  
delay = increasingly priced.

So:

> **Direct defect state > modeled penalty state for immediate transaction predictability.**

## 16. Falsification review

Supported:
- public direct safety status
- report-to-repair scope
- repair deadline
- future SWARMP demand clock
- escalating delay economics.

Falsified:
- direct public violation automatically means greenfield marketplace.
- penalty itself is the only urgency source.

Missing:
- deduplicated current SAFE/SWARMP/UNSAFE building counts
- actual matched repair bid dispersion
- actual shed rental by building
- time from UNSAFE to accepted amended SAFE/SWARMP by QEWI/building type.

Those are excellent future BigQuery analyses.

# 17. Autonomous next probe — B25 NYC Parking Structure Inspections

B24 raises a very useful causal question:

> Is the coordination market mature mainly because FISP has existed for ~45 years?

NYC's Parking Structures Inspection Program is much newer.

Same city means we hold constant:
- PLUTO owner resolution
- DOB infrastructure
- public compliance culture
- engineering market.

But vary:
- **regime age**
- asset economics
- operating-revenue loss.

B25 tests whether new regulation temporarily creates more intermediation whitespace before service networks fully adapt.
