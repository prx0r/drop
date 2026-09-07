# GoldProbe B06 — UK Residential EV Charger Repair / Replacement

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Mon, 7 Sep 2026 04:52:03 +0200
**Gmail ID:** 1a079c7ad3abf245

---

# GoldProbe B06 — UK Residential EV Charger Repair / Replacement

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled  
**Core result:** strong evidence for a **post-warranty repair cell**, not generic EV-charger lead generation.

## Why B06
B05 showed that “channel openness” cannot remain a qualitative market label. UK EV chargers give us observable warranty rules, independent repair, installed replacement prices and a large ageing installed base.

## Installed base
Zapmap's latest estimate is **~1.4 million home EV chargers at UK homes with driveways by end-2025**. Zapmap explicitly states there is no central official home-charger register, so this is an estimate rather than A0 stock data.

Source:
https://www.zapmap.com/ev-stats/home-and-community-charging

OZEV/DfT separately reports **412,682 grant-funded home charging installations since 2013** as of 1 July 2026, including 340,222 under EVHS and 40,333 under the older DRS.

Source:
https://www.gov.uk/government/statistics/electric-vehicle-charging-infrastructure-statistics-1-july-2026/grant-schemes-for-electric-vehicle-charging-infrastructure-statistics-1-july-2026

Do not combine those as if both are current stock.

## Warranty creates an age-dependent channel
Observed standard warranties:
- myenergi Zappi: **3 years**
- Ohme ePod/Home Pro: **3 years**
- Hypervolt Home 3 Pro: **3 years**, with 5-year extension option

myenergi is especially useful because its current support terms say it performs remote assessment first, appoints an approved warranty installer if required, and warns that unauthorized repairs/replacements void manufacturer warranty.

Sources:
https://www.myenergi.com/Zappi-ev-charger/
https://support.myenergi.com/hc/en-gb/articles/23604754964625-How-to-Purchase-Extended-Warranty
https://ohme-ev.com/smart-charging-faqs/
https://hypervolt.co.uk/en-GB/products/home-3-pro/overview/

That means “channel openness” is not a market constant.

### During warranty
fault → OEM/support → approved installer

### After warranty
fault → local electrician / specialist → PCB repair / replacement

This is the first strong reason to make openness **lifecycle- and warranty-specific**.

## Repair economics
WSMFix currently advertises Zappi PCB repair at **£169 + shipping**, positioned for out-of-warranty units.

Source:
https://www.wsmfix.co.uk/zappi-charger-repair.php

Current installed examples from one cross-brand installer:
- Ohme Home Pro: from **£999**
- Zappi GLO: from **£999**
- Zappi v2.1: from **£1,100**
- Hypervolt Home 3 Pro: from **£999**

Source:
https://www.chilternenergygroup.co.uk/ev-charger-installation/our-chargers

Ohme itself estimates standard installs from **£949 ePod / £999 Home Pro**:
https://ohme-ev.com/support/5-things-you-should-know-about-your-ev-charger-installation/

Using a selected replacement median around **£1,037**, the £169 qualifying PCB repair is only about **16.3%** of the installed replacement figure—roughly **83.7% lower**.

This is not a universal EV-charger repair saving: it applies only when the failing component is repairable at PCB level.

## Independent channel evidence
This is not merely theoretical.

WSMFix advertises UK mail-in PCB repair across Pod Point, Zappi, Hypervolt, Wallbox and Ohme:
https://www.wsmfix.co.uk/ev-charging/

Putney Electrical advertises same-day all-major-brand local repair, including chargers it did not install:
https://www.putneyelectrical.co.uk/ev-charger-repair-putney/

A Birmingham specialist similarly advertises multi-brand repair across Zappi, Wallbox, Pod Point, EO, Andersen, Ohme, ABB and Alfen:
https://www.evchargerinstallationbirmingham.uk/services/ev-charger-maintenance

This is strong evidence of independent service openness **after/alongside OEM routes**.

## A particularly interesting topology: local removal, national repair, local reinstall
EV chargers are fixed electrical assets, but some faults sit on removable PCBs.

That means the economic topology can be:

**customer**
→ local qualified electrician safely isolates/removes board
→ **national electronics specialist by post**
→ repaired board returns
→ local reinstall/test

The expensive specialist expertise no longer needs to travel to the house.

### Mechanism candidate: REMOVABLE_CONTROL_BOARD_DELOCALIZES_REPAIR

> If the high-value failure component is removable, field-service geography can collapse into parcel logistics.

This potentially applies far beyond EV charging:
- boilers
- heat pumps
- automatic gates
- pool controllers
- solar inverters
- industrial controls.

## Live transaction signal
An eBay UK Zappi “No Power” PCB repair listing was **£179.99** in the current snapshot, with watchers and a completed sale shown.

Source:
https://www.ebay.co.uk/itm/267644669035

That remains C0 commercial evidence, not national demand.

## The strongest new mechanism: WARRANTY_EXPIRY_CHANNEL_FLIP
We can now formulate:

> The same installed asset may be unattractive to an independent intermediary in years 0–3 and highly attractive in year 4+, without anything about the physical asset changing.

What changes is ownership of the service channel.

This suggests GoldProbe needs:

`installation_cohort × warranty_length × current_date`

as a standard aftermarket field.

## Installation-wave lag
The UK has hundreds of thousands of officially recorded grant-funded domestic charger installs stretching back to 2013, and the broader current home stock is estimated around 1.4m.

With common 3-year warranties, each installation cohort generates a lagged post-warranty cohort.

That creates another candidate:

### INSTALLATION_WAVE_LAGGED_AFTERMARKET

Instead of asking:
> how many chargers exist?

ask:
> **how many chargers cross warranty expiry this year?**

That is potentially a much better predictor of repair search demand.

## Current grants create another installation wave
From April 2026, eligible renters/flat owners, residential landlords and households using qualifying on-street cross-pavement solutions can receive up to **£500 per socket**, with schemes currently extended to 31 March 2027.

Source:
https://www.gov.uk/guidance/changes-to-electric-vehicle-chargepoint-grant-schemes-from-1-april-2026

Those 2026 installations are not immediate repair customers—but they are future aftermarket cohorts.

## What is already crowded
Generic installation is crowded. Current web results contain many local installers and city-specific EV-charger pages.

So B06 does **not** rehabilitate:
`EV charger installation Nottingham`

as the best wedge.

The stronger cells are:
- `Zappi output fault repair`
- `Pod Point no power repair`
- `charger out of warranty`
- `repair vs replace charger`
- `fault + model + postcode`
- `PCB mail-in repair`

## What B06 says about CHANNEL_OPENNESS_V1
A single market-level openness score is now clearly wrong.

Required grain:

**asset/model × lifecycle stage × warranty status × fault type**

Example:

`UK × Zappi × year 2 × output fault`
→ relatively OEM-controlled

`UK × Zappi × year 5 × output fault`
→ independent repair highly plausible

That is much more useful than “UK EV charging openness = 0.7”.

## Falsification
### Supported
- independent repair exists;
- component-level repair is materially cheaper for some faults;
- common warranty duration creates a clear lifecycle boundary;
- national mail-in repair can bypass local specialist scarcity.

### Not proven
- fraction of total faults repairable at PCB level;
- actual annual repair volume;
- model-specific failure rates;
- authenticated search volume/CPC;
- whether current specialist SERPs leave cheap acquisition room.

## Search demand
Monthly volume: **null**  
CPC: **null**

No SEO estimates substituted.

## Autonomous next probe: B07 Netherlands solar inverter aftermarket
Why: B06 generated **warranty-expiry** and **removable electronics** hypotheses. Dutch residential solar gives a very large, mature electronic installed base without repeating EV charging.

Hypothesis:
**aftermarket opportunity should correlate more strongly with installation cohorts crossing warranty/technical-life boundaries than with current installation growth.**

B07 will specifically search:
- historic annual installation cohorts;
- inverter warranty lengths;
- failure/technical-life evidence;
- repair vs replacement economics;
- OEM vs independent channels;
- whether removable electronics produce national repair services.

