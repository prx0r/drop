# GoldProbe B23 — NYC Local Law 97 Open Emissions Compliance Graph

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled

## Executive result

**B23 improves on France DPE in one crucial dimension: the legal owner is publicly resolvable. But the hypothesis that statutory penalty exposure is deterministic is too simple.**

NYC Local Law 97 covers most:
- individual buildings >25,000 sq ft,
- qualifying multi-building lots >50,000 sq ft,
- certain condominium groups >50,000 sq ft.

Source:
https://www.nyc.gov/site/buildings/codes/ll97-greenhouse-gas-emissions-reductions.page

The law's headline penalty is unusually explicit:

**$268 per metric ton of annual emissions above the applicable limit.**

Source:
https://www.nyc.gov/site/buildings/codes/greenhouse-gas-emissions-reductions-violations.page

At first glance this looks like the perfect public B2B compliance lead graph.

It is not quite that simple.

---

## 1. First-year filing scale is now real

NYC's April 22, 2026 release says:

- **93% of covered privately owned properties** filed,
- representing **91% of covered buildings**,
- about **28,000 privately owned buildings** had reports submitted.

The first reports covered calendar-year 2024 performance and were due by 31 December 2025.

Source:
https://www.nyc.gov/site/hpd/news/023-26/new-compliance-data-shows-impact-local-law-97-improve-sustainability-new-york-city

By property type filing rates included:
- multifamily 94%
- offices 95%
- warehouses 90%
- stores 91%
- hotels 95%
- hospitals/health 92%
- factories/industrial 89%
- religious facilities 81%
- garages 80%.

That is a mature regulatory market, not hypothetical future compliance.

---

## 2. But final building-specific first-year compliance was still being audited

The same April 2026 city release says DOB was auditing the roughly 28,000 building reports and would publish additional **property-specific compliance data on NYC Open Data later in 2026**.

In this September 2026 research run, searches surfaced the aggregate first-year data, current covered-building list and LL84 benchmarking dataset, but **not a final audited property-level LL97 compliance dataset**.

So the graph currently has:

```text
building
→ energy benchmark
→ covered status
→ modeled limit/exposure
```

but the authoritative final state:

```text
audited compliance / violation / final liability
```

must remain null until sourced.

That matters enormously.

---

## 3. The public building-energy data is genuinely strong

NYC Open Data's LL84 dataset publishes annual building energy and water benchmarking data.

It contains building/tax-lot identifiers and is explicitly relevant to LL97 calculations.

Source:
https://data.cityofnewyork.us/Environment/NYC-Building-Energy-and-Water-Data-Disclosure-for-/5zyy-y8am/about_data

Current dataset metadata:
- updated 21 Apr 2026
- covers calendar-year 2022 onward in the current table
- supports OData/API-style access.

This lets us model building emissions and portfolio trends without scraping.

But:

> **benchmarking input is not the same as audited liability.**

That distinction is now encoded.

---

## 4. Owner identity is much more open than France residential DPE

PLUTO currently has roughly 858k tax-lot rows and was updated **24 August 2026**.

Source:
https://data.cityofnewyork.us/City-Government/Primary-Land-Use-Tax-Lot-Output-PLUTO-/64uk-42ks/about_data

The January 2026 data dictionary explicitly defines:

**OwnerName = name of the owner of the tax lot**

from the Department of Finance Property Tax System.

Source:
https://s-media.nyc.gov/agencies/dcp/assets/files/pdf/data-tools/bytes/pluto_datadictionary.pdf

So we can join:

```text
BBL
→ LL84 energy
→ LL97 covered path
→ PLUTO owner
→ building characteristics
```

This materially improves **entity addressability** over B22 France.

But OwnerName can still be:
- LLC
- condo association
- shell entity
- institutional owner.

It is not automatically the relevant decision-maker's email/phone.

---

# 5. The penalty formula is explicit but liability is not

Headline:

```text
(Actual emissions – legal emissions limit) × $268/year
```

looks beautifully deterministic.

But actual enforcement has pathways for:
- offsets
- adjustments
- good-faith efforts
- unforeseen events
- external/financial constraints
- building/property-type methodology.

Sources:
https://www.nyc.gov/assets/buildings/pdf/processing_faqs.pdf
https://www.nyc.gov/site/buildings/codes/ll97-buildings-emissions-limits.page

Therefore B23 creates:

# `NOMINAL_PENALTY_IS_NOT_REALIZED_LIABILITY`

The schema must store:

```text
statutory formula
modeled exposure
owner-filed exposure
audited exposure
offset
adjustment
GFE mitigation
violation
paid amount
```

separately.

---

## 6. Even the calculation methodology changes by filing year

DOB says owners could use original occupancy-group or ESPM property-type methodology for 2024–25 under specified rules.

Starting in **2026**, ESPM property types become mandatory.

Source:
https://www.nyc.gov/site/buildings/codes/ll97-buildings-emissions-limits.page

This independently reinforces B22's versioning lesson:

> legal classifications and thresholds must be time-versioned separately from the building's physical state.

---

## 7. Offsets are already a real transaction

The city reports **$1,460,048** raised through Affordable Housing Reinvestment Fund offset certificates.

Price:
**$268/t**, identical to the nominal excess-emissions penalty.

Source:
https://www.nyc.gov/site/hpd/news/023-26/new-compliance-data-shows-impact-local-law-97-improve-sustainability-new-york-city

Simple arithmetic:

**$1,460,048 / $268 ≈ 5,447.9 tons**

of offset-certificate equivalent.

This is not total NYC noncompliance.

It proves that liability can convert into an alternative compliance transaction rather than a fine.

---

# 8. The 2030 transaction pool is potentially enormous

The city's 2023 LL97 strategy estimated:

- around **15,000 buildings** would need action for 2030,
- requiring roughly **$12–15bn investment**,
- potentially supporting up to 140,000 jobs.

Source:
https://www.nyc.gov/mayors-office/news/2023/09/mayor-adams-launches-getting-97-done-comprehensive-mobilization-strategy-reduce-building

This is a 2023 forecast, not a current 2026 audited need count.

But it demonstrates the order of magnitude.

---

# 9. Unfortunately for a generic middleman, NYC already built one

NYC Accelerator currently provides **free**:
- compliance help
- project planning
- financing guidance
- provider referrals
- building-specific energy support.

It says it has assisted **>30,000 buildings since 2015**.

Source:
https://accelerator.nyc/incentives-and-programs

Its Momentum tool can give:
- building-specific energy use
- LL97 status
- expected fine exposure
- upgrade/project recommendations.

Source:
https://accelerator.nyc/faq

So the naive product:

> “Enter address, see LL97 risk, get contractors and finance”

already exists as a publicly subsidized service.

This produces:

# `PUBLIC_ORCHESTRATOR_COMPRESSES_INTERMEDIARY_WHITESPACE`

The government can destroy a generic marketplace wedge without destroying the private service market.

---

# 10. Private market maturity is also substantial

Current private consultants offer:
- portfolio compliance dashboards
- emissions projections
- benchmarking
- professional-engineer/architect attestations
- decarbonization planning.

One current example, Cotocon, says it has an 8,000+ building proprietary database and a portfolio compliance product.

Source:
https://www.thecotocongroup.com/

This is not market-share evidence.

It is evidence that "LL97 dashboard + consultant" is already an established category.

---

# 11. Retrofit finance is similarly developed

NYCEEC currently offers:
- direct loans from **$200k**
- current displayed rates around **7–8%**
- up to **90% of project costs**
- up to 100% for some affordable multifamily projects.

Source:
https://nyceec.com/products/

NYC Accelerator also maintains a broad lender/finance network.

Again: not blank-market infrastructure.

---

# 12. So what survives?

Not:

> LL97 lead generator.

Potentially:

## Portfolio Liability / Opportunity Graph

For property managers, lenders, insurers, contractors and capital providers:

```text
BBL/BIN
owner entity
portfolio owner grouping
LL84 history
LL97 pathway
method version
modeled 2024 exposure
modeled 2030 exposure
filing state
audited result when public
adjustments
offsets
financing structure
capital project history
```

Then identify:

- portfolios with correlated 2030 exposure
- buildings where fossil equipment replacement timing aligns with compliance
- likely capital requirement bands
- building clusters underserved by specific retrofit providers
- lender exposure.

That is much stronger than forwarding contractor leads.

---

# 13. B22 vs B23

### France DPE
asset intelligence: extremely open  
owner/customer identity: weak  
public subsidy channel: centralized.

### NYC LL97
asset intelligence: open  
legal owner identity: substantially open  
penalty formula: explicit  
public project-routing channel: also highly developed.

So B23 demonstrates:

> Improving `ENTITY_ADDRESSABILITY` does increase commercial usefulness, but it does not automatically restore marketplace whitespace if orchestration is already mature.

---

# 14. New schema object: LIABILITY STATE

This should become mandatory for regulatory opportunities.

```text
statutory_formula
modeled_exposure
owner_filed_exposure
audited_exposure
offset
adjustment
mitigation
final_violation
paid_penalty
```

Otherwise an agent can turn "$268/t statutory maximum" into millions of fake "certain demand."

---

# 15. B23 falsification review

### Supported
- public joinable B2B property graph
- legal owner-name resolution
- statutory per-unit penalty
- very large future retrofit pool.

### Falsified/refined
- nominal penalty = actual liability
- owner-name availability = cheap customer acquisition
- public data + huge regulation = marketplace whitespace
- LL97 calculator/provider router = greenfield.

### Missing
- final audited first-year property-level LL97 compliance dataset
- realized penalty collection by building
- conversion from modeled exposure to retrofit spend
- building-specific provider award/project completion data.

---

# 16. Autonomous next probe — B24 NYC FISP façade remediation

B23's uncertainty was mainly **liability state**.

So B24 keeps:
- NYC public owner graph
- BBL/BIN
- B2B property owners

but switches to a direct safety condition:

```text
SAFE
SWARMP
UNSAFE
```

with:
- public filing map/download
- five-year inspection cycle
- unsafe repair deadline **90 days**
- escalating monthly penalties
- expensive physical repair
- sidewalk shed/public protection.

Hypothesis:

> **A directly observed public safety defect plus fixed remediation clock should be commercially more actionable than modeled emissions exposure.**

The crucial falsifier is whether QEWI + restoration contractor relationships already capture the job so completely that even a public UNSAFE status adds no routing value.
