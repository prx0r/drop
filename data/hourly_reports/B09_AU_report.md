# [GoldProbe B09] Australia Pool Equipment — Replacement Machine Confirmed, Climate-Shock Transfer Not Proven

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Mon, 7 Sep 2026 05:37:23 +0200
**Gmail ID:** 1a079f12b96d30dc

---

# GoldProbe B09 — Australia Residential Pool Equipment Aftermarket

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled  
**Primary test:** Can B08's `COHORT_READY_SHOCK_ACTIVATION` be replicated outside heating?

## Executive result

**The replacement thesis is strongly supported. The climate-shock sub-hypothesis is not.**

Australia has a very large mature pool installed base, a clearly measurable pump-replacement cycle, deep model-specific parts markets, and unusually strong energy-efficiency economics.

But after explicitly searching for it, I did **not** find sufficiently hard insurer, government, manufacturer-cohort or transaction data showing that Australian heatwaves directly cause a measurable spike in pool-pump/chlorinator hardware failures.

That is a useful falsification.

Do not transform:

> hotter weather → longer pump runtime

into:

> heatwave → X% more hardware failures

without data.

---

## 1. Installed-base scale

Australian Government energy guidance says **1.1 million Australian homes have a swimming pool**.

Source:
https://www.energy.gov.au/households

A separate NIEIR/Endeavour Energy demand model filed with the Australian Energy Regulator used approximately **1.2 million Australian households with a swimming pool or spa**, with about a third of pools in NSW.

Source:
https://www.aer.gov.au/system/files/Endeavour%20Energy%20-%20NIEIR%20-%207.02%20Post%20Modelling%20Adjustments%20for%20Demand%20Forecasts%20-%20June%202021%20-%20Public.pdf

Those are different denominators and remain separate.

---

## 2. The replacement machine is directly measurable

The AER/NIEIR model says Australian annual pool-pump sales are approximately **150,000–200,000 units/year**, with its forecast using an **8-year asset life** plus pool penetration/new-pool assumptions.

That does **not** mean 150k–200k annual failures—the sales figure also includes new pools.

But a national Energy Rating owner survey gives independent lifecycle evidence:

- **50%** of surveyed pool owners said they had already replaced a pool pump.
- Among Australian replaced pumps (n=721):
  - 0–2 years: **4%**
  - 2–5 years: **16%**
  - 5–10 years: **42%**
  - over 10 years: **23%**
  - unknown: **15%**

Source:
https://www.energyrating.gov.au/sites/default/files/2023-04/2016-Pool-Pump-Market-Research-Report_0.pdf

So the most common observed replacement age band was **5–10 years**, closely consistent with the separate 8-year modelling assumption.

That is considerably harder evidence than a vendor saying “pumps usually last eight years.”

---

## 3. Seasonality is real at the duty-cycle level

The same national survey reports:

- summer: **45%** said pumps ran 5–8 hours/day
- autumn: **52%** ran 1–4 hours/day
- winter: **63%** ran 1–4 hours/day.

This proves a materially heavier summer operating duty.

Government of Western Australia guidance separately says hot weather requires more frequent checking of saltwater chlorination and potentially additional chlorine.

Source:
https://www.ahs.health.wa.gov.au/sitecore/content/Healthy-WA/Articles/S_T/Swimming-pools-and-spas

But neither source measures hardware failure.

### Result for B08's shock hypothesis

`COHORT_READY_SHOCK_ACTIVATION` → **NOT REPLICATED IN B09**

Commercial repair firms claim summer callout spikes, but that is insufficient to turn the mechanism into a cross-sector pattern.

This is exactly how GoldProbe should behave.

---

## 4. Energy economics may be the much stronger trigger

Australian Government guidance says:

- pool pumps can account for about **18% of household electricity bills**
- an in-ground pool can account for up to **30% of household energy costs**
- a **5-star variable-speed pump uses 55% less energy** than a 1-star single-speed pump.

Source:
https://www.energy.gov.au/households/pool-pumps

South Australian government guidance estimates a pool typically consumes **2,000–3,000 kWh/year**, depending on equipment/run time/heating.

Source:
https://www.sa.gov.au/topics/energy-and-environment/using-saving-energy/swimming-pools-and-spas

MEPS and mandatory Energy Rating labels for covered pool pumps were introduced in **2022**.

Sources:
https://www.energy.gov.au/households/pool-pumps  
https://www.legislation.gov.au/F2022L00025/asmade

This creates a new mechanism candidate:

### `OPERATING_COST_OBSOLESCENCE_BEFORE_FAILURE`

> A functioning asset can become economically obsolete before it mechanically fails when a successor has a large measurable operating-cost advantage.

This is distinct from B07's Dutch policy-obsolescence mechanism.

There, policy changes the economics around solar export/self-consumption.

Here, the **device itself** has a huge recurring operating-cost delta.

---

## 5. The public product registry is a major data asset

The Australian Government's Energy Rating dataset now contains swimming-pool pumps and was updated **7 February 2026**.

It includes structured fields such as:

- brand
- model
- availability
- star rating
- performance/energy fields.

Source:
https://data.gov.au/data/dataset/energy-rating-for-household-appliances

This is fantastic GoldProbe infrastructure.

We can potentially join:

```text
old pump model
→ production generation
→ parts compatibility
→ current replacement models
→ star rating
→ annual running-cost delta
→ repair price
→ replacement price
```

That's much better than generating generic articles about pool pumps.

---

## 6. Replacement choice has hard evidence of interface lock-in

The 2016 Australian survey asked owners who replaced **like-for-like** why.

Among Australian respondents (n=133):

- installer/pool-shop advice: **62%**
- size / available space: **32%**
- existing piping: **22%**
- warranty: **7%**
- simply easier: **3%**.

This is exceptional GoldProbe data.

It directly validates the earlier `LEGACY_INTERFACE_LOCK_IN` mechanism:

> Existing plumbing and physical dimensions measurably affect successor choice.

And it adds something new:

### `SERVICE_ADVISOR_REPLACEMENT_GATEKEEPER`

62% cited the installer/pool shop.

For a technical replacement product, **who advises the customer may control the successor brand/model more strongly than the customer independently shopping the market**.

That is a completely different economic variable from SEO competition.

---

## 7. Compatibility becomes nastier below the model level

Astral/Hurlcon CTX is a perfect example.

Current parts specialists distinguish at least:

- Series 1 — pre-August 2014
- Series 2 — August 2014 onward
- MkII — around 2020 onward.

A Series 2 seal plate and volute must be paired; retailers explicitly warn that generations do not mix correctly.

Source:
https://heaterandspaparts.com.au/en-nz/products/seal-plate-series2-ctx-aug14-o

Pool Supermarket currently lists separate:

- old/new volutes
- old/new seal-plate seals
- old/new seal plates
- multiple impellers by CTX model
- motors from roughly **A$980 to A$1,355**.

Source:
https://www.poolsupermarket.com.au/astral-hurlcon-ctx-pump-spares

So even:

> Astral CTX

isn't enough information.

The atomic compatibility key may be:

> **brand × model × production generation × subcomponent**

This is much richer than “model number.”

---

## 8. The pool is actually a nested installed-base stack

AstralPool's current 2026 residential warranty schedule is unusually revealing.

Examples:

| Component | Current warranty clock |
|---|---:|
| Pump mechanical seal | **1–2 years** |
| Pool pump | **2–3 years** |
| Chlorinator | **2–3 years** |
| Chlorinator sensors/wear components | **~1 year** |
| Replacement salt cell | **2–3 years** |
| Pool controller | **2 years** |
| Filter tank | **5–10 years** |
| Heat pump | **3 years** |
| Heat-pump compressor | **5 years** |
| Heat exchanger | **5–25 years** |
| Robot wear components | **1 year** |

Source:
https://www.astralpool.com.au/warranty

Warranty ≠ technical lifetime.

But the structure proves something important:

### `STACKED_COMPONENT_CLOCKS`

A homeowner does not own “a pool.”

They own:

```text
pool
├─ pump
│  ├─ motor
│  ├─ seal
│  ├─ impeller
│  └─ controller
├─ chlorinator
│  ├─ cell
│  ├─ sensor
│  └─ dosing hardware
├─ filter
├─ heater
│  ├─ compressor
│  └─ heat exchanger
├─ robot
└─ automation
```

Every branch has a different warranty, wear profile, repair path and replacement cost.

That's a much richer lifecycle graph than a single `installed_asset_age`.

---

## 9. Current repair vs replacement economics

Commercial 2026 indicative ranges found:

- callout/diagnosis: **A$80–180**
- pump repair: **A$150–400**
- installed pump replacement: **A$800–2,200**
- chlorinator/salt-cell replacement: **A$600–1,500**
- pool heat-pump repair: **A$300–900**
- pool heat-pump replacement: **A$3,000–8,000**.

Source:
https://thepoolquotes.com/guides/how-much-does-pool-repairs-cost-in-australia-2026-guide

Because these aren't matched model-level transactions, I do **not** calculate one fake “repair saves 78%” statistic.

A direct Perth provider is more useful for labour architecture:

Waterworks currently advertises:
- standard service: **A$69 ex GST**
- deluxe: **A$105**
- callout: **A$135**
- pump overhaul labour: **A$135**
- same-model or suitable pump replacement labour: **A$135**
- salt chlorinator replacement labour: **A$135**
- heat-pump replacement labour: **A$135**.

Source:
https://waterworks.net.au/service-price/

That tells us the interesting price variation often lies in the **equipment/parts/specification decision**, not merely the truck roll.

---

## 10. Generic parts ecommerce is already mature

This sector emphatically falsifies:

> “hard compatibility = simply open a spare-parts shop.”

The parts ecosystem is deep.

The stronger interface is:

> **Upload pump photo/data plate → identify exact production generation → show repairable subcomponents → compare repair cost against an efficient correctly-sized replacement.**

That's diagnostic commerce.

---

## 11. Best initial B09 product

### Pool Equipment Passport / Pump Doctor

Input:
- pump photo + data plate
- chlorinator/controller photo
- pool volume
- plumbing diameter
- filter model
- cleaner/heater dependencies
- electricity tariff / rooftop solar
- symptoms.

Output:
1. exact model/generation
2. likely failure subsystem
3. exact compatible parts
4. repairable vs full replacement
5. electrical-licence requirement
6. successor pump that fits plumbing/space
7. current government energy rating
8. projected electricity delta
9. local repair/replacement quotes.

The energy comparison is especially strong because Australia supplies a government machine-readable model database.

---

## 12. What B09 proved and falsified

### Strongly supported
- Australia has a huge mature pool installed base.
- Pool pump replacement is recurrent and empirically measured.
- 5–10 years was the modal replacement band in the national owner survey.
- Physical space/plumbing affect like-for-like replacement.
- Advisor channel has strong measured influence.
- Model-generation-specific compatibility is real.
- Energy efficiency creates a separate replacement clock.
- Pools are nested systems with many component clocks.

### Falsified / unresolved
- **No hard replication of “heatwave causes hardware replacement spike.”**
- Routine pool maintenance is not whitespace.
- Generic pool-parts ecommerce is not whitespace.
- One “pool equipment lifetime” variable is meaningless.

---

## 13. Orchard update

### `LEGACY_INTERFACE_LOCK_IN`
Further strengthened with unusually good quantitative evidence:

**32% size/space + 22% existing plumbing** among Australian like-for-like pump replacers.

### `MULTI_CLOCK_AFTERMARKET_TRIGGER`
Further supported:
- mechanical age
- component warranty
- energy-cost obsolescence
- product efficiency regulation
- interface compatibility.

### `COHORT_READY_SHOCK_ACTIVATION`
**Not replicated.**

This is important.

The next probe should not go looking for another example that supports it. It should go where direct loss data can settle it.

---

## 14. Autonomous next probe — B10 Norway cabins

Norway cabin water/frost/remote monitoring is selected specifically because B09 couldn't validate the shock mechanism.

The intended test is stronger:

> **Does a weather shock create directly measurable economic loss in remote properties, and does delayed detection create enough extra loss that monitoring + automatic intervention becomes economically valuable?**

This moves the economic problem one step upstream:

```text
failure
→ detect
→ respond
```

instead of merely:

```text
failure
→ repair
```

If Norwegian insurer data show frost/water losses and delayed discovery are material, we will have a properly evidence-backed shock/prevention mechanism rather than extrapolating from summer runtime.

