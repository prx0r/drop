# GoldProbe B03 — Pellet heating: seasonal capacity, mandatory maintenance, failure-parts and service capture

## Why this probe was chosen

I chose pellet/wood heating over shutters/awnings and domestic pumps because it gives unusually clean evidence for a new question: **does seasonal dependence on an installed asset create a measurable service premium, and does that premium leave room for an independent intermediary?**

This was deliberately selected for information gain. We already knew compatibility, regulation and fragmented trades can matter. Here we can measure installed base, annual legal maintenance, live low-season/high-season tariffs, urgent-service markups, model-specific spare parts, and compare three countries with different service-channel structures.

Hypothesis being tested:

> When a home depends on a complex heating asset during a constrained season, customers face a measurable availability/dispatch premium on top of parts cost. Annual maintenance and model-specific failures then create recurring monetization. The best intermediary opportunity should therefore be diagnosis + capacity routing, not generic parts retail.

Falsifiers were recorded before analysis: no seasonal premium; remote diagnosis not materially cheaper than physical dispatch; OEMs already own the whole service relationship; installed base too small; or parts too generic to create compatibility friction.

---

# 1. France: the hypothesis is real, but the opportunity is narrower than expected

France has a huge pellet installed base. Propellet reported more than **1.8 million pellet-heated households in 2023**. A separate end-2023 appliance breakdown sourced from ADEME/SER counted roughly **1.047 million pellet stoves, 180,000 pellet boilers and 77,000 pellet inserts**. These are different denominators, so GoldProbe does not sum them. France also has about 7.8 million domestic wood-heating appliances overall.

Sources:
https://concertation-strategie-energie-climat.gouv.fr/sites/default/files/2024-12/N%C2%B0114%20-%20Propellet%20-%20Cahier%20d%27acteur%20SNBC-PPE.pdf
https://www.geothermies.fr/sites/default/files/inline-files/2025_02_06_PanoramaChaleur2024_W.pdf

France also provides a true recurring forcing function. Current law requires periodic maintenance of combustion heating appliances at least every 12 months, and flue sweeping at least every 12 months, with qualified professionals involved.

Source:
https://www.legifrance.gouv.fr/jorf/id/JORFTEXT00004786728

## The seasonal premium is observable

I found five same-provider low-season vs high-season price pairs for pellet/wood-heating service in 2026:

- Maison Line pellet sweeping: €135 low season -> €156 high season: **+15.6%**
- Docteur Pellet stove maintenance: €195 -> €209: **+7.2%**
- Atre Decoration / Godin Isère maintenance: €240 -> €280: **+16.7%**
- RDC Confort sweeping: €69 -> €79: **+14.5%**
- Confort de Flamme sweeping: €60 -> €70: **+16.7%**

Across those five matched pairs, the median observed high-season list-price premium is **15.6%**.

That is already a much stronger statement than “people value urgency.” Capacity itself becomes more expensive as heating demand rises.

The tails are even stronger:

- Sécu'Flamme publishes **+50% on Saturday and +100% on Sunday** for emergency/repair work.
- RDC Confort adds **€40 for an express appointment** on a €69 low-season base service, about a **58% surcharge**.

Sources:
https://www.ramonage-var.fr/fumisterie-diagnostic/autre-prestation-tarifs-a-la-carte
https://www.docteurpellet.com/maintenance-entretien-poele-a-granules/nos-tarifs/
https://rdcconfort.fr/
https://www.secuflamme-ramoneur-fumiste.fr/nos-tarifs/

Important methodological point: these are **offered price premiums**, not verified conversion elasticity. We still need booking/conversion evidence before calling them proven willingness-to-pay.

---

# 2. The real gold: the information layer is dramatically cheaper than the truck roll

Docteur Pellet publishes:

- remote telephone diagnostic: **€29**
- physical fault diagnostic: **€79**
- repair visit: **€119**, excluding parts

So the physical diagnostic costs roughly **2.7×** the remote information layer, and the repair visit roughly **4.1×**.

Another French specialist sells immediate video diagnosis for **€49**. In Austria, B&U Service publishes a **€159 nationwide travel flat** before repair labour, then €27.50 per 15 minutes.

Sources:
https://www.docteurpellet.com/maintenance-entretien-poele-a-granules/nos-tarifs/
https://www.b-energie.fr/
https://www.bu-service.at/services

This creates a new GoldProbe pattern:

## `DISPATCH_COST_DOMINATES_SIMPLE_DIAGNOSIS`

When make/model/error code/photo/video can narrow the fault, the physical dispatch layer may cost several times the information layer.

That gives a very concrete business objective:

> Do not merely generate a lead. Increase the probability that the first truck roll is the final truck roll.

A proper intermediary should collect:

- manufacturer
- exact model
- serial/nameplate photo
- error code
- video of startup
- fan/extractor noise
- pellet feed behavior
- last maintenance
- ignition behavior
- likely component
- part availability

Then route to a technician who supports that brand **with the likely part already available**.

This can save the technician a wasted journey and save the homeowner days without heat.

That is materially more defensible than an “AI stove chatbot.”

---

# 3. Generic spare-parts ecommerce is already mature

France fails one part of our initial thesis in a useful way.

One current French specialist catalogue exposes **1,520 pellet-stove spare products**. Another exposes **1,050**.

The taxonomy is already deep:

- ignition elements
- burn pots
- PCBs
- displays/remotes
- smoke extractors
- auger motors
- convection fans
- thermostats
- probes
- doors/glass
- seals
- refractory panels
- pressure switches

Example live price ranges:

- pressure switches: roughly **€15–€78+**
- ignition elements: commonly **€30–€175+**
- smoke extractors: roughly **€88–€560+**

Sources:
https://www.poelesboisgranules.fr/75-pieces-detachees-poeles-a-granules-de-bois
https://www.poelediscount.com/18-pieces
https://www.poelediscount.com/133-pressostat

This means:

> **The French pellet opportunity is not “discover spare parts no one sells.”**

The catalogue exists.

The unsolved problem is closer to:

> “Which of these 1,500 parts explains my exact fault, is compatible with my exact model, and who can install it tomorrow?”

That is diagnosis + compatibility + logistics + local capacity.

---

# 4. Italy: regulation can literally veto the repair business model

Italy provides a useful cross-country contrast.

ISTAT reports that **7.8% of Italian households used pellets in 2023**, up from 4.1% in 2013. Italy currently has roughly 26.6 million households, implying a rough proxy of **~2.07 million pellet-using households**. This is not an exact pellet-stove installed-base count, but it is a useful comparable demand denominator.

Pellet use is geographically concentrated:

- national: 7.8%
- municipalities below 10,000 inhabitants: **14.3%**
- small mountain municipalities: **16.2%**

So small mountain municipalities show pellet usage at about **2.08× the national household rate**.

Sources:
https://www.istat.it/en/press-release/household-energy-equipment-year-2024/
https://www.istat.it/en/press-release/demographic-indicators-year-2025/

This updates our existing asset-density insight; it is not emitted as a duplicate recurring pattern.

More importantly, Lombardy changes the lifecycle economics entirely. Current regional rules prohibit use of biomass generators rated 0, 1 or 2 stars and require at least 4-star performance for new installations. Pellet appliances below 35 kW must use certified A1 fuel. The cited regional sanction can run from **€500 to €5,000**.

Source:
https://www.regione.lombardia.it/ambiente-e-territorio/energia/impianti-termici-edilizia-sostenibile-e-certificazione-energeti/red-informazioni-uso-corretto-generatori-di-calore-a-biomassa-legnosa

This creates another new pattern:

## `REGULATORY_REPAIR_VETO`

Regulation does not merely add compliance demand. It can change the economically correct lifecycle node.

If an old stove cannot legally be used, the correct recommendation is no longer:

> repair fan -> €X

It becomes:

> do not spend €300 repairing a unit whose compliance class makes continued use uneconomic or unlawful; route directly to replacement.

That is hugely important for GoldProbe. A naive aftermarket engine might wrongly score old installed assets as repair opportunities when regulations have actually converted them into replacement leads.

---

# 5. Austria: a high-spend market that is much less attractive to an independent middleman

Austria is the counterexample we needed.

The Austrian Biomass Association reports roughly **216,000 pellet boilers installed since 2001** and about **400,000 biomass central-heating systems under 100 kW** over the same period.

Source:
https://www.biomasseverband.at/wp-content/uploads/Basisdaten-Bioenergie-2025.pdf

Maintenance spend is healthy:

- ÖkoFEN: roughly **€200–€300 annually** for a single-family-home pellet system
- chimney sweep: another **€40–€90**
- ETA published a €300 maintenance price for pellet boilers up to 32 kW in its referenced contract schedule
- Austroflamm publishes an annual pellet/duo stove maintenance package around **€328**
- independent B&U Service charges €269 for maintenance without contract

Sources:
https://www.oekofen.com/de-at/pelletheizung-wartung/
https://www.austroflamm.com/de/service/wartungsvertraege
https://www.bu-service.at/services

Yet I score Austria only about **6.9/10 for an independent GoldProbe middleman**.

Why?

The manufacturers are much more visibly embedded in the service relationship:

- postcode service routing
- branded maintenance contracts
- OEM technical partners
- recurring service ownership

So we discovered an important macro constraint:

> **Installed-base attractiveness must be multiplied by channel openness.**

High homeowner spend is commercially irrelevant to us if the OEM already owns the customer relationship.

This partially falsifies the broad version of our thesis.

“Rich owner + expensive asset + maintenance” is not enough.

We need:

> rich owner + expensive asset + recurring/problem demand + **open/fragmented acquisition channel**.

---

# 6. New pattern: `HEATING_SEASON_CAPACITY_PREMIUM`

This probe gives us the cleanest evidence yet that seasonal technician capacity itself carries a price.

Observed same-provider high-season premiums across five French examples:

- minimum: ~7.2%
- median: **15.6%**
- maximum: ~16.7%

Plus:

- Saturday emergency: +50%
- Sunday emergency: +100%
- one express-booking surcharge: ~58%

Again, these are listed/observed tariffs, not proven booking elasticity.

Economic mechanism:

> The scarce asset is not only the replacement component. It is **qualified technician time at the moment failure matters**.

This means we can potentially manufacture value by moving demand in time:

### April–August
Acquire owner cheaply -> identify model -> book maintenance -> inspect likely wear items -> build asset passport.

### September–February
Customer already belongs to us -> no frantic acquisition auction -> pre-triaged repair -> technician gets likely parts list -> priority routing.

That is much stronger than entering the paid-search auction only after the stove has failed during a cold week.

---

# 7. Exact GoldProbe questions answered

## How much more will they pay for speed/convenience?

Observed offered premiums include ~7–17% for high-season service, +50/+100% weekend emergency pricing, and ~58% for an express appointment in one example. Physical diagnosis can cost 2.7× remote diagnosis before a replacement part is added.

## On what problems is the premium strongest?

No-heat / failure states during heating season, especially when the problem requires physical attendance. Ignition, smoke extraction, pressure sensing, auger/feed, electronic control and airflow are high-friction component classes.

## What options exist now?

France already has authorized stations, independent multi-brand technicians, specialist ecommerce, remote diagnosis, maintenance contracts and lead-generation services. Austria has even stronger OEM service ownership.

## Is there room for us?

Yes in France, but **not as a generic directory or spare-parts shop**. The strongest gap is pre-triage + model/error identification + likely-part prediction + technician capacity routing + regulation-aware repair-vs-replace logic.

Austria has substantially less independent whitespace because OEMs capture service. Italy may offer interesting regional replacement-routing opportunities because regulation changes the economics of older equipment.

## Best go-to-market?

- model + error-code SEO
- symptom + department/locality SEO
- spring/summer maintenance/reminder acquisition
- technician partnerships
- white-label triage for local service companies
- part affiliate/ecommerce only after diagnosis

## Is this the same in every country?

No. That is the most important result.

The asset economics are similar. **Channel economics are not.**

France: fragmented multi-brand service -> orchestration opportunity.
Austria: stronger OEM service ownership -> independent aggregator weaker.
Italy: regional environmental rules -> compliance/replacement intelligence more important.

---

# 8. Probe verdict

**Score: 8.8/10 France opportunity, but not for the original generic interpretation.**

The original hypothesis was **PARTIALLY SUPPORTED**.

Supported:
- seasonal capacity premium exists
- mandatory recurring maintenance exists
- model-specific failure parts exist
- remote triage has clear economic value

Weakened/falsified:
- generic parts whitespace is weak; mature French catalogues already exceed 1,000 SKUs
- the middleman opportunity is not universal; Austria demonstrates strong manufacturer capture

How well did this probe answer the reason it was selected?

**9.3/10.** It gave actual same-provider seasonal price deltas, urgent markups, remote-vs-dispatch pricing, official installed-base evidence, legal recurring demand, deep parts-market evidence and a cross-country counterexample.

Still unresolved:
- actual conversion elasticity for urgent/high-season premiums
- search volume/CPC by model + error code + geography
- measured first-visit fix-rate improvement from pre-identifying likely parts

---

# 9. Autonomous decision: next GoldProbe

The next probe is **Singapore residential air-conditioning servicing**.

Why this follows from B03:

Pellet heating proved that seasonal scarcity and truck rolls matter, but it mixed together several mechanisms: cold-season urgency, annual regulation, rural travel and complex parts.

Singapore lets us remove several of those variables.

It is:
- wealthy
- compact and geographically dense
- extremely cooling-dependent
- humid
- ecommerce/service-app native
- high run-hours
- no winter heating season

So the next hypothesis is:

> **High usage intensity + humidity + recurring maintenance can create subscription economics even without a winter scarcity event; however dense geography may collapse dispatch friction enough that value shifts away from routing and toward trust, bundled maintenance, response time and repeat servicing.**

That will tell us whether the pellet result was fundamentally about **seasonality**, **dispatch cost**, or simply **high-frequency maintenance of essential installed infrastructure**.

Falsifiers for the Singapore probe are already stored in the JSON:
- AC ownership/usage not sufficiently widespread
- servicing already standardized/cheap enough that convenience premium disappears
- dense geography makes routing commoditized
- major brands/landlords capture demand before consumer search

That is the next experiment because it maximizes information gain rather than merely finding another heating-adjacent opportunity.
