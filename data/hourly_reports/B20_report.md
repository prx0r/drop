# GoldProbe B20 — Ireland NCT Failure → Open Repair Market

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled

## Executive result

**The Britain-vs-Ireland A/B works. Institutional separation materially changes transaction topology.**

Ireland's NCTS says it is:
- the **only nationwide NCT provider**
- **totally independent of the motor industry**
- and **does not engage in garage service or repair**.

It operates 50 locations, 600+ inspectors and expects >2m tests annually.

Source: https://www.ncts.ie/about-us/

That removes the B19 British mechanism where the test garage already possesses the vehicle and can immediately sell the fix.

## Hard 2024 demand export

RSA/NCTS 2024:
- **1,732,094 full tests**
- **50.57% first-pass**
- **128,548 dangerous failures (7.4%)**
- **607,467 lane retests**
- **250,575 non-lane retests**
- **2,590,136 total tests**.

Sources:
https://www.rsa.ie/road-safety/statistics/nct-statistics-and-annual-reviews
https://www.rsa.ie/docs/default-source/about/annual-reports/rsa-annual-report-2024.pdf?sfvrsn=2d5daa46_1

Using the rounded pass rate, roughly **856,174 full tests did not pass first time**.

Total retests were **858,042**.

This is a very large recurring repair-intent surface that NCTS itself is structurally unable to monetize.

## Failed report is explicitly handed out as a repair brief

NCTS now emails passing reports where customers opt in, but it deliberately still prints failed Vehicle Inspection Reports so the inspector can explain **remedial work** face to face.

Source: https://www.ncts.ie/about-us/news/

That is a literal demand handoff.

### `NONREMEDIATING_DIAGNOSER_EXPORTS_DEMAND`

Mandatory diagnosis
→ fail
→ standardized report
→ diagnoser cannot repair
→ customer must enter external repair market.

## Retest clock preserves urgency without rewarding one garage

Current rules:
- book retest within **21 days**
- complete within **30 days**
- full test **€60**
- lane retest **€40**
- minor visual-only retests free.

Source: https://www.ncts.ie/1123

Unlike GB MOT, there is no "leave it with the tester's workshop and get repaired there" option.

## Dangerous defects remain high-value

Dangerous result means a direct/immediate risk and the vehicle should not be used on-road until fixed.

Source: https://www.ncts.ie/1157/

In 2024 there were **128,548 dangerous full-test failures**.

This creates strong urgency, but because NCTS cannot repair, recovery/transport + garage choice become downstream concerns rather than tester capture.

## Ireland's fleet makes this increasingly structural

CSO says **3,246,651 vehicles were licensed in 2025**.

Source:
https://www.cso.ie/en/csolatestnews/pressreleases/2026pressreleases/pressstatement-snapshotoftransportstatisticsinirelandjune2026/

June 2026 private non-EV age distribution includes **1,307,957 vehicles aged 11+ years**.

Source:
https://www.cso.ie/en/releasesandpublications/ep/p-civf/compositionofirelandsvehiclefleet2026/

RSA says the overall fleet averages about **9.9 years**. More than 80% of four-year-old cars pass first time, while 10+ year cars fall below **40% first-pass** and are subject to annual testing.

Source:
https://www.rsa.ie/news-events/news/details/2025/10/14/rsa-marks-25-years-of-the-nct-with-winter-safety-warning-to-motorists

This gives a useful candidate:

### `AGEING_ASSET_PLUS_SHORTER_INSPECTION_CYCLE_COMPOUNDS_DEMAND`

The old vehicle:
1. fails more often
2. **and** gets inspected more often.

That creates multiplicative service intensity.

## Failure categories map naturally into real garage work

RSA 2024 visual-defect counts include:
- tyres: **231,212**
- front suspension: **191,481**
- steering linkage: **147,868**
- mechanical brake components: **126,444**
- bodywork: **106,286**.

These are defect observations, not unique jobs.

The repair intent is nevertheless highly concrete.

## But the obvious marketplace is not greenfield

Current Irish products already include:
- AutoGuru — sends repair requests to garages and compiles quotes
- BookMyCarService — compare local prices/book
- Escargo — verified garage/recovery/mobile-mechanic marketplace, currently building regional supply
- FixMyNCT — NCT defect guidance and vehicle-specific parts
- many individual NCT-failure specialists.

Sources:
https://autoguru.ie/
https://bookmycarservice.ie/
https://escargo.ie/
https://fixmynct.ie/nct-guide

So "upload NCT fail → get a mechanic" is **not a novel insight**.

The category looks less consolidated than Britain's FixMyCar, but provider market share is not transparently measurable, so the report does not score a made-up whitespace value.

## The better workflow

### Failed VIR → normalized remediation

Input:
- registration
- VIR photo/PDF
- location
- deadline.

Output:
1. exact fail items
2. dangerous/major separation
3. parts likely needed
4. whether visual-only free retest applies
5. comparable garage work packages
6. multiple local written quotes
7. recovery if dangerous
8. repair evidence
9. retest reminder.

This fits the institutional design.

## Even stronger: move upstream

Bosch currently charges roughly **€35–€70** for a pre-NCT check.

Source:
https://www.boschcarservice.com/ie/en/services/inspection-and-checks/pre-nct-check/

The official age/pass data suggests a better long-term asset:

`make × model × age × mileage × known defect pattern → predicted NCT failure set`

Then sell/route preventative work **before** the car reaches NCTS.

That avoids the 30-day failure scramble.

## B19 vs B20

### Great Britain MOT
private test garage can repair  
+ asset physically at garage  
+ same-site retest incentive  
→ strong capture.

### Ireland NCT
central independent tester  
+ no repair activity permitted  
+ failure report exported  
→ downstream transaction genuinely reopens.

So:

### `INSTITUTIONAL_SEPARATION_REOPENS_TRANSACTION_RIGHTS`
is now a serious candidate.

## Falsification review

Supported:
- huge fail/retest volume
- actionable report
- test-provider repair prohibition
- ageing fleet amplifies recurring repair demand.

Falsified:
- all roadworthiness systems exhibit test-station repair capture.
- generic NCT routing is untouched whitespace.

Unresolved:
- actual share of failed drivers using their existing mechanic vs shopping
- garage quote dispersion for identical VIR defects
- marketplace shares
- model-level longitudinal NCT defect data availability.

## Next autonomous probe — B21 Germany chimney-sweep/heating compliance

B20's highest-information new mechanism is not automotive.

It is:

> **What happens when a mandatory diagnoser is structurally separated from remediation?**

Germany's chimney-sweep / combustion-safety regime gives a different installed-asset test:
- heating systems
- recurring regulated checks
- emissions/flue/safety findings
- district chimney-sweep regulatory role
- downstream heating installers and repair firms
- unusual mix of regulated and competitive services.

The question is whether regulated diagnosis exports demand — or whether the chimney-sweep structure quietly recaptures it through adjacent commercial services.
