# GoldProbe B25 — NYC Parking Structures Inspection / Repair

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled

## Executive result

**B25 weakens the idea that a new regulation automatically creates temporary marketplace whitespace.**

NYC's Periodic Inspection of Parking Structures program only became effective in **2022** under Local Law 126 of 2021.

Yet by August 2026 the city's own proposed-rule statement reported **188 approved QPSIs**. Existing structural engineers, concrete-restoration specialists, waterproofing firms and large contractors were already able to supply the technical work.

Source:
https://www.nyc.gov/assets/dcas/downloads/pdf/cityrecord/2026/cityrecord-08-10-26.pdf

So the more important mechanism is:

> **`ADJACENT_PROFESSIONAL_NETWORK_ABSORBS_NEW_REGULATION`**

A new law does not necessarily create a new supplier market.

If the work is close enough to an established profession, capability transfers immediately.

---

# 1. The compliance architecture

DOB requires covered owners to hire a New York State Professional Engineer designated as a **Qualified Parking Structure Inspector (QPSI)**.

Current Cycle 1:
- 1A — Manhattan CDs 1–7: 2022–2023
- 1B — Manhattan CDs 8–12 + Brooklyn: 2024–2025
- 1C — Bronx, Queens, Staten Island: 2026–2027.

Source:
https://www.nyc.gov/site/buildings/safety/parking-structure.page

Unsafe conditions must be repaired within **90 days** and an amended report follows within two weeks.

---

# 2. But the six-year clock is already obsolete for the future

The current DOB program page still describes the first cycle through six-year logic.

Local Law 71 of 2024 tightened the actual future statute:

- all structures must have a condition assessment by **1 January 2028**
- **after 1 January 2028, every structure must be assessed at least once every 4 years**
- SREM reassessment was shortened to **no more than 2 years**.

Source:
https://www.nyc.gov/assets/buildings/local_laws/ll71of2024.pdf

This produces:

# `REGULATORY_RATCHET_SHORTENS_INSPECTION_CYCLE`

The installed base did not grow.

The mandated recurring service frequency did.

A compliance engine that stores simply:

```text
inspection interval = 6 years
```

will already be wrong.

It needs:

```text
interval
effective date
rule version
```

---

# 3. A real failure pulled the inspection clock forward

After the 2023 fatal Ann Street parking-garage collapse, DOB added a one-time **initial observation requirement** for parking structures in later subcycles.

Owners in 1B/1C had to obtain and file an initial structural observation by **1 August 2024**, while their full PIPS reports were still due on the original 2025/2027 schedules.

Source:
https://www.nyc.gov/site/buildings/dob/pr-penalties-for-late-parking-structure.page

DOB says explicitly that the purpose was to put more owners onto an **accelerated timeline** to catch potential problems before incidents.

The city later said that since Aug 1 2024 every covered structure citywide had to have either a full PIPS engineering report or an initial observation report.

Source:
https://www.nyc.gov/site/buildings/dob/pr-parking-structure-collapse.page

This gives:

# `FAILURE_EVENT_ACCELERATES_COMPLIANCE_CLOCK`

A catastrophe can create an unforecast compliance cohort:

```text
normal due date = 2027
        ↓
major failure elsewhere
        ↓
regulator adds interim inspection
        ↓
new spend required in 2024
```

That is commercially important.

---

# 4. The early-inspection status itself is public

DOB has a public map with a downloadable CSV for initial observations.

Status layers include:

- Initial Observation / PIPS Report On-Time
- Late
- Report Not Submitted
- Report Not Required.

Source:
https://www.nyc.gov/assets/buildings/html/parking_structure_initial_observations_map.html

So a regulatory shock can generate a new public demand cohort very quickly.

---

# 5. The condition model independently replicates B24

PIPS classifications are:

```text
SAFE
SREM
UNSAFE
```

SREM means:

> safe now, but needs repair/investigation/engineering monitoring to prevent future unsafe condition.

Sources:
https://www.nyc.gov/site/buildings/safety/ps-classification-and-reporting.page
https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-159232

The professional report includes:
- photographs
- defect location
- deterioration cause
- proposed work
- whether permits are needed
- **month/year when the condition is expected to become hazardous**.

So B24's key insight replicates:

# `DEFECT_MATURITY_CLOCK_PRECOMPUTES_FUTURE_DEMAND`

---

# 6. SREM cannot be ignored indefinitely

Current law requires:

- reassessment no later than **2 years**
- amended report
- the same condition cannot repeatedly stay SREM without certification that the prior required repair was corrected.

Sources:
https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-159236
https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-159240

So:

```text
SREM today
```

is a forecastable capital-maintenance cohort.

This may be much more commercially useful than today's UNSAFE count.

---

# 7. UNSAFE remains the urgent state

Current law:
- immediately secure/remove danger
- repair within **90 days**
- file amended report within two weeks
- extensions can be requested under defined conditions.

Source:
https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-159223

Current DOB fees/penalties include:
- initial filing $485
- amended $940
- late filing $1,000/month
- failure to file $5,000/year
- failure to correct unsafe: $1,000/month
- failure to correct SREM: $2,000 one-time.

Source:
https://home4.nyc.gov/site/buildings/safety/ps-fees-penalties.page

Another DOB page surfaces older filing-fee values; the dedicated fees page is therefore treated as current and this inconsistency is explicitly recorded.

---

# 8. We have a useful historical condition snapshot — but it needs careful interpretation

New York Law Journal reported that in **September 2025**:

Subcycle 1A:
- 939 structures

Subcycle 1B:
- 2,297

Combined:
- **3,236**

Among them:
- 548 SREM
- 235 UNSAFE
- 1,897 had not filed a full condition assessment.

Source:
https://assets.alm.com/58/c3/cb058cd84dbfb383153ce6f84dc1/nylj100125a.pdf

Contextual ratios:

- SREM: **16.9%**
- UNSAFE: **7.3%**
- no full report: **58.6%**

But the last number must **not** be called a delinquency rate.

At the September snapshot, Subcycle 1B did not have its final full-report deadline until **31 December 2025**.

Likewise, only 52 of the 2,738 1C structures had full reports at that time — but 1C wasn't due until end-2027.

This is exactly the kind of context preservation GoldProbe needs.

---

# 9. Approximate current universe

A current 2026 industry analysis explicitly says it reads the live DOB PIPS map as:

- total **6,078**
- Queens 2,032
- Brooklyn 1,793
- Manhattan 1,497
- Bronx 701
- Staten Island 55.

Source:
https://www.skylinesnews.com/post/nyc-parking-structures-under-ll126-structural-risk-compliance-strategy-long-term-repair-planning

This remains **C1**, not our official denominator, until the downloadable DOB CSV is ingested directly.

Against 188 QPSIs, the crude ratio is roughly:

**32.3 structures / approved QPSI**

but this is emphatically **not a workload ratio** because inspection years and engineer/firms' capacities differ.

---

# 10. PIPS did not need a completely new contractor species

This is the controlled-regime-age result.

The actual physical work is familiar to existing structural contractors:

- concrete repair
- steel repair
- corrosion
- waterproofing
- drainage
- lighting
- membranes
- structural rehabilitation.

An entirely new post-2022 construction industry did not need to appear.

A new regulatory transaction attached itself to an old physical service network.

That explains how the ecosystem can mature quickly.

---

# 11. Current projects show the capital scale

## One Penn Plaza

EDG describes an eight-level, 160,000 sqft underground garage restoration:

- **$4m project**
- structural concrete slab repair
- steel beam repair/replacement
- waterproofing
- 14 repair sections
- 7 waterproofing phases.

Source:
https://edgnyc.com/work/one-penn-plaza-parking-structure-restoration/

Most importantly:

> the project was phased specifically so garage operations could remain uninterrupted.

That is an enormous clue.

---

# 12. Repair sequencing itself becomes a product

A parking structure is often not just an inert building component.

It can generate operating revenue.

Therefore:

```text
lowest construction quote
```

is not necessarily optimal.

The objective can be:

```text
repair cost
+
lost parking revenue
+
tenant/customer disruption
+
safety
+
schedule
```

This creates:

# `REVENUE_PRESERVING_REPAIR_PHASING`

The One Penn team split a $4m repair into 14 zones specifically to keep operations running.

For these assets, **construction sequence is an economic parameter**.

---

# 13. Public-institutional projects demonstrate the upper tail

DASNY's Queens College parking-ramp reconstruction included:

- structural concrete deck repair
- water/storm systems
- electrical/lighting
- surface work
- drainage.

Initial estimate:
**$18m–$19m**

Winning construction award:
**$14.84m**, April 29 2026.

Source:
https://www.dasny.org/opportunities/rfps-bids/2025/cuny-queens-college-parking-ramp-reconstruction

This is not a typical garage repair.

It simply confirms that deferred structural parking work can become a major capital project.

---

# 14. New-regulation whitespace hypothesis: weakened

B24 FISP has existed since around 1980.

B25 PIPS has existed only since 2022.

Yet PIPS already has:
- specialist approved engineers
- filing/extension workflows
- public maps
- violation handling
- private engineering market
- mature restoration contractors.

Therefore:

```text
NEW LAW
≠
NEW MARKET
```

if the physical work can be absorbed by nearby professions.

This produces:

# `ADJACENT_PROFESSIONAL_NETWORK_ABSORBS_NEW_REGULATION`

Potential GoldProbe fields:

```text
required professional skill
nearest existing profession
capability overlap
new license/training burden
existing customer relationship
existing contractor network
```

This may predict opportunity better than `years_since_regulation`.

---

# 15. Best B25 product

Not:

> Find a QPSI.

Potentially:

## Parking Structure Condition / Capital Clock

For operators/owners/portfolios:

```text
parking structure ID
owner
subcycle
initial observation
full PIPS report
SAFE / SREM / UNSAFE
QPSI
hazard projection
SREM reassessment date
repair status
extension
amended report
next 4-year inspection
```

Then overlay:

```text
parking capacity
rate/revenue
partial closure
construction phasing
project CAPEX
```

Output:
- future inspection cohorts
- SREM repair queue
- capital schedule
- QPSI demand peaks
- phasing scenarios
- missed-deadline warnings
- repair scope normalization.

This is a useful data/operations product.

It is not a generic marketplace.

---

# 16. Batch-level causal result: B23 → B24 → B25

This was a useful controlled three-probe sequence.

### B23 — LL97
Public asset + owner graph  
but liability is modeled/mitigable.

**Finding:** nominal penalty != realized liability.

### B24 — FISP
Public physical safety state + direct repair clock.

**Finding:** defect maturity + delay carry costs are stronger transaction predictors.

### B25 — PIPS
Same city/safety architecture, but very new regulation.

**Finding:** regime age does not guarantee marketplace whitespace because existing structural professionals can absorb the rule almost immediately.

So the emerging relationship is:

```text
CommercialOpportunity
≈
ConditionObservability
×
ClockUrgency
×
TransactionOpenness
×
OperatingImpact
×
CustomerAddressability
÷
ExistingCoordinationMaturity
```

where:

```text
ExistingCoordinationMaturity
```

can be inherited from an **adjacent profession**, even if the regulation itself is brand new.

---

# 17. New mechanisms from B25

### `FAILURE_EVENT_ACCELERATES_COMPLIANCE_CLOCK`

Catastrophe elsewhere can create surprise interim inspections before ordinary due dates.

### `REGULATORY_RATCHET_SHORTENS_INSPECTION_CYCLE`

The regulator can increase recurring service intensity after observing early implementation.

### `ADJACENT_PROFESSIONAL_NETWORK_ABSORBS_NEW_REGULATION`

New law does not imply greenfield supplier opportunity.

### `REVENUE_PRESERVING_REPAIR_PHASING`

For operating assets, uptime can dominate simple repair-price comparison.

---

# 18. Autonomous next probe — B26 England Higher-Risk Building Safety Cases

B25 leaves one especially useful unanswered question.

If adjacent professionals absorb the **technical** work of a new regulation quickly, where does durable new opportunity actually remain?

The clean next experiment is England's post-Grenfell higher-risk building regime.

It created:
- Accountable Person / Principal Accountable Person roles
- higher-risk building registration
- building safety cases
- safety-case reports
- mandatory occurrence reporting
- resident engagement
- regulator evidence/submission workflows.

This is different from simply mandating "hire a structural engineer."

Hypothesis:

> **New regulation creates limited technical marketplace whitespace when adjacent engineers can absorb the work, but can create durable orchestration/software whitespace when it creates a genuinely new cross-disciplinary evidence + governance + resident + regulator workflow that no prior profession owned end-to-end.**

That directly tests the mechanism B25 generated.
