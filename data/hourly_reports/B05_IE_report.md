# GoldProbe B05 — Ireland Domestic Wastewater / Septic Systems

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Sun, 6 Sep 2026 19:49:22 -0700
**Gmail ID:** 1a079c5377192e4d

---

# GoldProbe B05 — Ireland Domestic Wastewater / Septic Systems

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled  
**Primary hypothesis:** `H-CHANNEL-OPENNESS-INVERTED-U`  
**Core result:** directionally supported. The strongest whitespace is **failed inspection → remediation interpretation → grant eligibility → quote normalization → compliant contractor routing**, not routine emptying.

## Why B05 was selected
B04 Singapore AC suggested that channel openness may have an optimum: too closed is OEM-owned; too open is commodity competition. Ireland wastewater was chosen because it has unusually good official stock, inspection, grant and geography data, but a mixed commercial channel.

## Hard installed-base data
CSO reports **498,283 registered domestic wastewater treatment systems in 2024**, of which **483,481 (97%)** were household-owned. Registrations rose from **475,742 in 2020** to **498,283 in 2024**: **4.74% total growth**, about **1.16% CAGR**.

This is a large installed base, not a high-growth installation thesis.

Source: https://www.cso.ie/en/releasesandpublications/ep/p-dwwts/domesticwastewatertreatmentsystems2024/

### Geographic concentration
The seven largest counties contain **252,228 systems (50.62% of national registrations)**:

- Cork: **57,009**
- Galway: **44,073**
- Kerry: **34,672**
- Donegal: **32,041**
- Mayo: **30,406**
- Tipperary: **27,164**
- Wexford: **26,863**

The source dataset is directly available as CSV, JSON-stat, PX and XLSX:
https://data.gov.ie/dataset/dwa01-registrations-of-domestic-waste-water-treatment-systems

## Inspection outcomes: strong forcing event, but not population prevalence
EPA targeted inspection results:

| Year | Inspected | Failed | Failure rate |
|---|---:|---:|---:|
| 2023 | 1,189 | 532 | 45% |
| 2024 | 1,390 | 773 | 56% |
| 2025 | 1,466 | 863 | **59%** |

The 2025 EPA statement is exact: 1,466 inspected, 863 failed.

However, these inspections are deliberately risk-targeted. GoldProbe therefore **rejects** the inference that 59% of all Irish septic systems are defective.

EPA also reports **7,212 systems failed since 2013 and 84% had been fixed by end-2025**, which is commercially more useful: an official failure event often does lead to remediation.

Source:
https://www.epa.ie/news-releases/news-releases-2026/epa-finds-almost-six-out-of-ten-septic-tanks-fail-inspection-putting-drinking-water-wells-and-rivers-at-risk.php

## Grants: significant money plus substantial routing complexity
The maximum grant rose from **€5,000 to €12,000** from 1 Jan 2024.

Grant awards:
- 2023: **194**
- 2024: **265**
- 2025: **460**, totalling about **€4.77m**

2023→2025 award count increased **137.1%**.

Derived average 2025 award:
**€10,370**.

This is *not* project cost or consumer spend.

There are three separate grant routes:
1. National Inspection Plan
2. Prioritised Areas for Action
3. High Status Objective Catchment Areas

National Inspection Plan eligibility requires an inspection and Advisory Notice; other routes depend on geography and local-authority confirmation. Routine maintenance, servicing and desludging are explicitly excluded from grant support.

Sources:
https://www.gov.ie/en/department-of-housing-local-government-and-heritage/publications/domestic-waste-water-treatment-systems-septic-tanks/
https://www.gov.ie/en/department-of-housing-local-government-and-heritage/press-releases/minister-obrien-announces-increase-in-septic-tank-grants/

This is ideal intermediary friction: the homeowner does not merely need a contractor; they need the **right remediation path**.

## Routine emptying is already partly commoditized
EPA provides an explicit desludging responsibility framework based on tank size and household occupancy:
https://www.epa.ie/take-action/in-the-home/wastewater/

Kollect already aggregates licensed/registered emptying providers and supports on-demand or scheduled annual/biannual clearing:
https://kollect.ie/septic-tank/mayo/

Therefore generic “marketplace for septic emptying” is not the strong wedge.

## Technical repair is open but fragmented
Multiple independents advertise all-makes service and repair. Waste Water Maintenance explicitly handles pumps, air pumps, motors, parts, fault-finding and major brands/models:
https://www.wastewater.ie/services/septic-tank-maintenance-repair

Manufacturers still retain channels. Tricel routes service enquiries to regional distributors:
https://tricel.ie/wastewater-treatment/wastewater-components/

That means Ireland is neither Austria-style OEM capture nor Singapore-style commodity hypercompetition.

## Recurring servicing is already productized
Ireland Waste Water current plans:
- €182/year
- €235/year
- €345/year
- €555/year

The tiers progressively transfer more repair/callout/parts risk to the provider:
https://www.irelandwastewater.ie/maintenance-contract/

Wastewater Solutions advertises three-year and five-year contracts equivalent to roughly **€227/year incl VAT**:
https://www.wastewatersolutions.ie/service-maintenance/

So recurring service itself is not untouched whitespace.

## Parts ecommerce is mature
Tanks.ie currently exposes **225 treatment-plant accessories** and **49 blower/spares SKUs**:
https://tanks.ie/collections/sewage-treatment-plant-accessories

IWTA provides the model ontology—Puraflo, Hydroclear, Bison, Klaro, Tricel, Biosafe, Biodisc, Oakstown BAF and more:
https://iwta.ie/wastewater-treatment/en-certification/

Again: generic parts store = weak.

## The real split
### More commoditized
- emptying
- regular cleaning
- routine annual service
- common replacement parts

### Less productized / higher value
- failed inspection
- Advisory Notice interpretation
- percolation/structural failure
- geology/site-specific remediation
- grant-route determination
- repair vs upgrade vs replacement
- getting truly comparable compliant quotes

This is a lifecycle-cell insight, not a sector-level one.

## Mechanism candidate 1 — PUBLIC_DIAGNOSIS_PRIVATE_REMEDIATION_HANDOFF
A public authority creates a standardized event:
**inspection → failure → Advisory Notice**.

But the homeowner still has to translate that into a private-market transaction:
**what work? what grant? which provider? which quote is actually compliant?**

Potential product:
### Failed Septic Inspection Resolver
Upload Advisory Notice + Eircode → classify remediation → identify grant route → create standardized contractor brief → obtain comparable quotes → retain completion evidence.

## Mechanism candidate 2 — GRANT_AMPLIFIES_FORCED_REMEDIATION
Maximum support rose from €5k to €12k; awards grew from 194 in 2023 to 460 in 2025 (**+137.1%**).

The data do not isolate causality, so the defensible claim is only:
**greater financial support coincided with materially higher remediation-grant throughput.**

## Mechanism candidate 3 — ROUTINE_LAYER_COMMODITY_COMPLEX_LAYER_WHITESPACE
The same ecosystem can simultaneously contain:
- a bad opportunity: scheduled emptying;
- a potentially excellent opportunity: failed-inspection remediation.

Therefore “competition” must be measured at:
**sector × lifecycle stage × trigger × problem**, not sector alone.

## Channel-openness hypothesis update
Observed sequence now:
- Austria pellet: OEM-heavy → weak independent whitespace
- France pellet: moderate fragmentation → narrow wedge
- Singapore AC: very open/mature → routine routing commoditized
- Ireland wastewater: mixed OEM + independents + regulatory complexity → strong narrow remediation wedge

This **supports the inverted-U hypothesis directionally**, but does not prove it because “channel openness” still lacks a normalized metric.

Future probes will collect raw dimensions rather than assigning high/medium/low:
- sampled all-makes provider share
- OEM exclusivity
- independent/OEM price gap
- aggregator presence
- service-area overlap
- parts accessibility
- review concentration
- right to choose remediation provider

## What B05 falsified
1. Routine septic maintenance is neglected — **false**.
2. Generic parts ecommerce is whitespace — **weak/false**.
3. Large installed base alone creates opportunity — **false**.
4. Forced, complex remediation has more whitespace than routine ownership — **supported**.

## Search demand
Monthly search volume: **null**  
CPC: **null**

No unauthenticated SEO estimates were substituted.

## Next autonomous probe — B06 UK EV charger repair/replacement
Why: B05 shows we now need measurable channel-openness variables. UK EV charging gives:
- large installed base
- model-specific faults
- identifiable OEMs
- independent electricians/repair specialists
- repair-vs-replace prices
- regulatory limits
- strong local-search visibility

Hypothesis:
**aftermarket value emerges where OEM capture is incomplete, independents can legally access the work, model-specific faults are searchable, and repair remains materially cheaper than replacement.**

B06 will be the first probe explicitly designed to build `CHANNEL_OPENNESS_V1` from raw observed features.

