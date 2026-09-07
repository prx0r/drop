# GoldProbe B05 — Ireland Domestic Wastewater / Septic Systems

**Run date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** deliberately disabled — no naked scores  
**Primary hypothesis:** H-CHANNEL-OPENNESS-INVERTED-U  
**Primary verdict:** **INVESTIGATE grant-eligibility + remediation-scope routing; HOLD generic quote marketplace / parts store.**

---

## 1. Why this probe was chosen

B04 Singapore residential air-conditioning produced a critical counterexample. An enormous installed base and very open independent service channel did **not** produce obvious generic middleman whitespace; the market was already competitive, digitally mature and routine dispatch was cheap. B03 Austria pellet heating showed the opposite failure mode: strong OEM service capture made the channel too closed.

That generated a testable market hypothesis:

> **Independent intermediary whitespace may peak in the middle: open enough that customers can switch/reroute, but fragmented enough that diagnosis, scope, compliance and provider selection remain costly.**

Ireland's domestic wastewater treatment market was selected because it gives unusually hard official data on registered systems, inspection failures, grants and geography while appearing to have neither full OEM capture nor Singapore-style service commoditization.

The key falsifier was simple: if generic provider discovery is already the only problem, or if government/local authorities effectively prescribe the remediation supplier, then the “middle” hypothesis adds little.

---

## 2. The installed base is real and unusually measurable

The Central Statistics Office recorded **498,283 registered domestic wastewater treatment systems in 2024**, up 1.2% year-on-year. **483,481 (97%)** were household-owned.

The register rose from **475,742 in 2020 to 498,283 in 2024**, a derived increase of **4.74%**. There were **5,926 new registrations in 2024**, up 8.6% from 2023 — but CSO explicitly warns that new registrations may include late registrations, so this is *not* a clean physical-installation growth series.

The top seven counties contain **252,228 systems**, or **50.62%** of the national register:

| County | Registered DWWTS 2024 |
|---|---:|
| Cork | 57,009 |
| Galway | 44,073 |
| Kerry | 34,672 |
| Donegal | 32,041 |
| Mayo | 30,406 |
| Tipperary | 27,164 |
| Wexford | 26,863 |

**Primary source:** Central Statistics Office, *Domestic Waste Water Treatment Systems 2024*  
https://www.cso.ie/en/releasesandpublications/ep/p-dwwts/domesticwastewatertreatmentsystems2024/

### Important denominator contradiction

The registration file counts physical registered systems. Census household reporting uses a different unit. CSO notes that Census 2022 reported **467,331 individual septic tanks plus 59,066 other individual treatment systems**, and explains that two family units sharing one tank can be two Census responses but one registered physical system.

This is exactly the kind of conflict GoldProbe should preserve rather than “resolve” into one installed-base number.

---

## 3. The 59% failure headline is dangerous if stripped of context

EPA reports that local authorities performed **1,466 inspections in 2025**, of which **863 (59%) failed**.

But EPA explicitly says the inspections target **areas of greatest environmental and health risk**. The National Inspection Plan distributes inspections by risk.

Against 498,283 registered systems, 1,466 inspections represent only:

**0.294% of the registered base in one year.**

And the 863 failed-inspection events are only:

**0.173% of the registered base.**

Neither metric is national prevalence.

### Hard rule produced by B05

> **TARGETED_FAILURE_RATE_IS_NOT_PREVALENCE**

It would be a severe analytical error to calculate:

`498,283 × 59% = 294,000 failing systems`

The source does not support that. The inspected cohort was deliberately enriched for risk.

EPA also reports **7,212 failures since 2013**, with **84% fixed by end-2025**.

**Primary source:** EPA, May 2026  
https://www.epa.ie/news-releases/news-releases-2026/epa-finds-almost-six-out-of-ten-septic-tanks-fail-inspection-putting-drinking-water-wells-and-rivers-at-risk.php

This distinction changes the business thesis: **failed inspections are an excellent high-intent lead trigger, but not a sufficiently large acquisition universe by themselves.**

---

## 4. The grant economics are genuinely high-ticket

EPA says **460 grants** were awarded in 2025, totalling **nearly €4.77 million**, compared with 265 awards in 2024.

The scheme pays **85% of eligible costs up to €12,000**.

Transparent derived metrics:

- approximate average 2025 award: **€10,370**
- approximate eligible-cost lower bound represented by €4.77m of awards: **€5,611,765**
- approximate lower-bound eligible cost per award: **€12,199**
- a job must contain at least **€14,118** of eligible cost to hit a €12,000 award at 85%, absent other limits.

These are **not average project invoices**. The grant total is approximate, some awards may hit the cap, and projects may contain non-eligible costs.

Still, this is the clearest economic distinction in the market:

> Routine emptying is a few-hundred-euro service. Grant-backed remediation is often a five-figure eligible-cost event.

Primary sources:
- https://www.epa.ie/environment-and-you/waste-water/inspections--repair/
- https://www.epa.ie/news-releases/news-releases-2026/epa-finds-almost-six-out-of-ten-septic-tanks-fail-inspection-putting-drinking-water-wells-and-rivers-at-risk.php

---

## 5. The grant itself is a diagnosis/routing problem

There are **three distinct grant routes**:

| Route | Trigger / eligibility |
|---|---|
| National Inspection Plan | Failed local-authority inspection + Advisory Notice |
| High Status Objective Catchment Area | Qualifying location; Eircode/catchment/local-authority process |
| Priority Area for Action | LAWPRO/local-authority identification and eligibility letter |

Routine maintenance, ordinary servicing and desludging **do not qualify**.

All schemes are administered through local authorities.

Source:  
https://www.epa.ie/environment-and-you/waste-water/inspections--repair/  
https://www.gov.ie/en/department-of-housing-local-government-and-heritage/publications/domestic-waste-water-treatment-systems-septic-tanks/

This means the commercial question isn't:

> “Who fixes septic tanks?”

It's:

> **“Given my Eircode, system, inspection/advisory notice, symptoms and property context, what exactly am I eligible for and what job should I request quotes for?”**

That is a much stronger information product.

---

## 6. Routine desludging is *not* the whitespace

EPA says householders **must use an authorised collector** for septic-tank desludging and directs them to the National Waste Collection Permit Office search, where they can choose “Septic Tank de-sludging” and county.

EPA also prescribes a tank-size × household-occupancy desludging schedule ranging roughly from yearly to five-year intervals and requires the homeowner to keep proof for five years.

Source:  
https://www.epa.ie/take-action/in-the-home/wastewater/

This is a classic example of **regulation improving market discoverability**.

Current commercial price signals are also relatively transparent:

- Kollect's 2026 guide: approximately **€230–€300** for a standard household tank; remote/difficult access +€50–€100; emergency +€50–€100.
- TanksEmptied.ie Leinster guide: approximately **€280–€400**, with a typical standard range around €300–€350.

Sources:
- https://kollect.ie/blog/how-much-does-septic-tank-emptying-cost-in-ireland/
- https://tanksemptied.ie/blog/septic-tank-emptying-cost-leinster-2026

These are commercial guides, not transaction ledgers. They are enough to conclude that **ordinary emptying is comparatively productized**, not enough to estimate national average spend.

Therefore generic “find a septic emptying company” is low-priority.

---

## 7. Parts commerce is also more mature than the broad thesis suggests

Tanks.ie currently exposes **225 in-stock sewage-treatment-plant accessories**, including blowers, diffusers, UV lamps and alarm panels. **217/225 are Kingspan parts** in the live snapshot.

Its blower/spares category contains **49 in-stock products** and explicitly says blowers are brand/model-specific in most cases.

Sources:
- https://tanks.ie/collections/sewage-treatment-plant-accessories
- https://tanks.ie/collections/blowers-spares

This produces a subtle result:

**Compatibility pain exists, but availability pain often does not.**

A generic wastewater-parts store therefore fails the GoldProbe whitespace test, at least for the major Kingspan/Klargester ecosystem represented here.

A narrower model/photo/fault identification layer could still be valuable, but only if it captures queries upstream of existing specialist retailers.

---

## 8. OEM capture exists, but it does not dominate the whole market

Tricel sells one- to ten-year Puraflo service agreements starting at **€195**, covering travel and routine servicing labour while excluding parts and other labour. It recommends yearly service.

Source:  
https://tricel.ie/wastewater-treatment/puraflo-maintenance/

That establishes an OEM service relationship. But the broader Irish market also contains all-makes independents, desludging contractors, installers and general wastewater professionals.

This looks materially different from Austria pellet heating, where manufacturer service networks appeared much more central to customer capture.

So Ireland passes one part of the inverted-U test: **the channel is open enough that an independent router could participate.**

---

## 9. But generic aggregation already exists

Two obvious examples:

**QuoteHub** advertises comparison of up to four local septic professionals and quotes within 24 hours.

https://quotehub.ie/get-quotes/septic-tank/

**OnlineTradesmen** lets homeowners post a septic job, receive replies, compare provider profiles/ratings and hire.

https://www.onlinetradesmen.ie/drain-and-sewer-services/septic-tank-services

That falsifies:

> “Ireland needs a septic contractor marketplace.”

It already has those.

More interestingly, QuoteHub's current page contains stale regulatory information — including wording around “Irish Water” inspections and older grant information — while the current official regime is local-authority implemented and the maximum grant is €12,000.

That is exactly the distinction between:

**lead marketplace**

and

**high-quality regulatory/diagnostic intelligence layer**.

---

## 10. Directory supply looks fragmented, but do not turn search counts into provider counts

Golden Pages currently returns **304 national results** for “Septic Tanks and nearby.”

Selected county snapshots include:

| County | Registered systems | Golden Pages returned results | Systems / result proxy |
|---|---:|---:|---:|
| Cork | 57,009 | 39 | 1,462 |
| Galway | 44,073 | 21 | 2,099 |
| Donegal | 32,041 | 6 | 5,340 |
| Wexford | 26,863 | 21 | 1,279 |

Sources:
- https://www.goldenpages.ie/septic-systems/ireland/
- https://www.goldenpages.ie/septic-systems/cork-county/
- https://www.goldenpages.ie/septic-systems/galway-county/
- https://www.goldenpages.ie/septic-systems/donegal-county/
- https://www.goldenpages.ie/septic-systems/wexford-county/

The final column is deliberately labelled a **directory visibility proxy**, not supplier density.

Donegal's apparent ratio is interesting, but we cannot conclude that Donegal literally has only six relevant providers. Directory pages include category overlap, serves-area firms and incomplete listings.

This is exactly the kind of observation the downstream BigQuery agent should be able to revisit with a better supplier registry later.

---

## 11. Geographic concentration is still commercially useful

The top seven counties contain **50.62%** of all registered systems.

Risk-targeted 2025 inspection observations also generated substantial failure-event counts in several of those same counties. The official EPA table reports, for example:

| County | 2025 inspections | Targeted sample fail rate | Approx failed inspections |
|---|---:|---:|---:|
| Cork | 136 | 56% | 76 |
| Galway | 106 | 53% | 56 |
| Donegal | 126 | 67% | 84 |
| Wexford | 125 | 64% | 80 |
| Mayo | 71 | 66% | 47 |
| Kerry | 75 | 61% | 46 |
| Tipperary | 44 | 52% | 23 |

Again: those fail percentages are **risk-targeted sample outcomes**, not county-wide prevalence.

For acquisition, county installed-base density is hard evidence; targeted failure events are a second, distinct signal.

---

## 12. Private wells make some failure states unusually high consequence

EPA says there are about **165,000 Irish households with both a septic tank system and a private well**.

Source:  
https://www.epa.ie/environment-and-you/waste-water/septic-tanks/

That does not tell us how many currently have contamination.

It does tell us why the diagnosis/remediation problem has unusually high stakes: wastewater and drinking water infrastructure can be colocated on the same property.

This should affect messaging and urgency models but not be converted into a failure-rate estimate.

---

## 13. Property transactions create another non-inspection trigger

EPA has a dedicated buying/selling checklist for homes with private wastewater systems. It asks about:

- registration;
- tank/system location and access;
- fitness for purpose;
- maintenance and desludging records;
- system/percolation information;
- whether assessment or upgrade works are needed;
- previous inspection;
- local authority requirements.

Source:  
https://www.epa.ie/publications/compliance--enforcement/waste-water/septic-tanks--wastewater-systems-when-buying-or-selling-a-house.php

This matters because NIP inspections alone provide only hundreds of failure events per year. A scalable acquisition engine needs additional triggers.

A property transaction is economically interesting because the customer needs **certainty about an unknown future liability**, not merely a repair.

Potential product:

> **Wastewater Property Passport** — identify the system, gather registration/service/desludging evidence, flag missing information, route an assessment if needed, preserve everything for the buyer/seller/solicitor.

The probe does not yet contain an official count of annual DWWTS-linked property sales, so this remains an opportunity cell rather than a quantified TAM.

---

## 14. The strongest product is not “SepticDoctor” as originally imagined

The research narrows it substantially.

### Weak wedges

**Generic quote marketplace** — already exists.

**Routine desludging directory** — official NWCPO search already exists.

**Generic parts store** — mature specialist ecommerce exists.

**Inspection-failure-only lead generation** — only 863 targeted failures in 2025.

### Stronger wedge

A single routing flow:

`Eircode + trigger + advisory notice / document + system/model/photo + symptoms`

then classify:

**A. routine maintenance/desludging**  
→ authorised collector / straightforward service

**B. mechanical/model-specific fault**  
→ correct likely part / specialist technician

**C. NIP grant remediation**  
→ interpret advisory notice → competent professional → normalized quotes

**D. HSOCA/PAA grant route**  
→ eligibility → documentation → remediation scope

**E. property purchase/sale**  
→ system passport / assessment / compliance evidence

The key product output isn't the supplier list.

It's:

> **“This is the job you actually need to buy, this is why, this is the relevant grant route, and these suppliers are quoting on the same scope.”**

That is a much better intermediary.

---

## 15. New mechanism candidate: ELIGIBILITY_GATED_SUBSIDY_ROUTING

The Irish grant regime creates a clean candidate mechanism:

> When a large subsidy is conditional on one of several externally defined eligibility routes, correct classification becomes a valuable information layer before the underlying purchase.

Hard evidence:
- 85% of eligible costs;
- maximum €12,000;
- three distinct eligibility routes;
- 460 awards in 2025;
- nearly €4.77m distributed.

This is **not yet a recurring pattern**. It needs an independent sector/country replication.

---

## 16. New mechanism candidate: REGULATED_TASK_SPLIT

This probe also finds:

> Regulation can make one narrow service easy to discover while leaving the higher-value decision layer fragmented.

In Ireland:

**desludging**
→ official authorised-collector registry  
→ recurring, comparatively standardized

while:

**remediation**
→ diagnose problem  
→ understand local-authority/advisory notice  
→ determine grant eligibility  
→ choose competent professional  
→ specify correct works  
→ compare quotations.

This is a more precise form of “fragmented trades.”

The fragmentation exists **between task layers**, not necessarily inside every task.

---

## 17. Did B05 support the inverted-U channel-openness hypothesis?

### Directionally: yes.

We now have three contrasting structures:

| Market | Channel condition | Observed consequence |
|---|---|---|
| Austria pellet | relatively OEM-captured | independent route weak |
| Singapore AC | very open + highly competed | ordinary routing commoditized |
| Ireland DWWTS | open, but high-value decision layer fragmented | eligibility/scope routing remains plausible |

That is exactly what the inverted-U predicted.

### Causally: not yet.

Ireland also contains powerful co-variables:

- regulation;
- targeted inspections;
- public-health/environmental consequences;
- grants;
- local-authority processes;
- property due diligence.

Therefore we cannot say:

> “Intermediate openness caused the opportunity.”

The more defensible refinement is:

> **Channel openness is an accessibility constraint. Opportunity appears strongest when customers can switch providers but the decision/scope layer has not yet been commoditized.**

The next probe must remove the forcing variable.

---

## 18. GoldProbe data-quality findings

Three hard rules become permanent:

### TARGETED_FAILURE_RATE_IS_NOT_PREVALENCE

Never multiply risk-targeted inspection failures by national installed stock.

### PHYSICAL_SYSTEM_COUNT_IS_NOT_HOUSEHOLD_COUNT

Register and Census can both be correct while using different units.

### GRANT-AWARD-COUNT_IS_NOT_SAME-YEAR_CONVERSION

Do not divide 460 awards by 863 2025 failed inspections. Cohorts and grant routes do not align.

These methodological findings are as valuable as the business ideas because they prevent downstream agents from manufacturing false TAM.

---

## 19. Search-volume fields remain null

No authenticated Google Keyword Planner / Ads dataset was available in this run.

Therefore:

- monthly query volume: `null`
- CPC: `null`

GoldProbe did not substitute SEO-blog estimates.

The downstream agent can fill these later from an authenticated source without corrupting the research layer.

---

## 20. B05 verdict

| Cell | Verdict | Reason |
|---|---|---|
| Generic septic quote marketplace | **HOLD** | Existing QuoteHub / OnlineTradesmen |
| Routine desludging lead-gen | **LOW PRIORITY** | Official authorised-provider discovery + relatively standardized spend |
| Generic parts store | **HOLD** | 225+ stocked accessories at one specialist |
| Grant eligibility + remediation scope router | **INVESTIGATE** | Large subsidy + three routes + high-ticket spend + nontrivial scope |
| Property-transaction wastewater passport | **INVESTIGATE** | EPA explicitly identifies transaction due-diligence workload |
| Model-specific plant fault triage | **INVESTIGATE NARROW** | Compatibility remains hard although parts availability is mature |

---

## 21. Next probe selected autonomously: B06 Netherlands solar inverter aftermarket

Why not another septic market?

Because B05 cannot isolate channel openness from regulation/grants.

The highest-information next experiment is **Netherlands residential rooftop solar inverter / monitoring / battery-retrofit aftermarket**.

The Netherlands has a huge rooftop-solar installed base and an ageing early cohort, but much weaker mandatory remediation forcing than Ireland's wastewater systems.

### B06 hypothesis

> If intermediate channel openness itself is important, a large ageing rooftop-solar base should still produce model-specific diagnosis, inverter replacement and upgrade-routing whitespace without inspections forcing the homeowner to act.

### Falsifiers

- OEM/installer warranties capture replacement demand.
- Generic installers already solve model identification and normalized replacement quoting.
- Inverter faults/monitoring generate low-value demand.
- policy uncertainty destroys rather than redirects retrofit spend.
- battery/EV/dynamic-tariff integration is already dominated by mature platforms.

If B06 is weak while B05 is strong, the orchard learns something major:

> **forcing functions + subsidy complexity may matter more than channel openness itself.**

If B06 is strong, the inverted-U hypothesis survives a much cleaner test.

---

## 22. Bottom line

B05 is a strong probe because it **narrows** rather than merely confirms the original thesis.

Ireland does not need another septic directory, quote board or parts shop.

The actual intelligence gap is the layer immediately before a high-value transaction:

> **What is wrong? Which regulatory/grant route applies? What exact work should be bought? Is this maintenance, repair, remediation or replacement? And how do I compare suppliers on the same scope?**

That is the high-signal opportunity.

More importantly, B05 directionally supports the channel-openness hypothesis while also exposing its confounder. B06 is selected specifically to remove that confounder.
