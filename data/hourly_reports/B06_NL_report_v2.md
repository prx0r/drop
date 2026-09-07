# [GoldProbe B06] Netherlands Solar Inverter Aftermarket — full research + structured evidence

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Sun, 6 Sep 2026 22:33:10 -0400
**Gmail ID:** 1a079b660cacbab0

---

# GoldProbe B06 — Netherlands Rooftop Solar Inverter Aftermarket

**Run date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled — no naked scores  
**Primary experiment:** Can an ageing installed base + accessible channel create intermediary whitespace without mandatory inspection/remediation?

## Executive result

B06 weakens the idea that **channel openness itself** explains GoldProbe opportunities.

The Netherlands has almost ideal installed-base economics: nearly 3 million solar households by end-2024, a measurable early cohort now crossing the average inverter lifetime, and a policy change in 2027 that makes self-consumption more valuable. Yet generic inverter replacement and provider matching are already heavily productized.

The opportunity only becomes interesting one layer above generic replacement:

> **Identify the legacy system → determine warranty/orphan status → establish what replacement is technically compatible → decide whether 2027 economics make like-for-like, hybrid, battery-ready or EV-integrated replacement rational.**

The valuable variable is therefore **non-commoditized decision complexity at a transaction trigger**. Channel openness controls whether we can capture it; openness does not create the value.

---

## 1. Installed-base scale

CBS reports national solar installations across **all economic activity and homes**:

| Year | Installations |
|---|---:|
| 2021 | 1,730,285 |
| 2022 | 2,298,859 |
| 2023 | 2,818,720 |
| 2024 provisional | 3,167,299 |
| 2025 provisional | **3,313,355** |

2025 also records 29.426 GWp of panel capacity and 26.045 GW of inverter capacity.

Source: CBS  
https://www.cbs.nl/nl-nl/cijfers/detail/85005NED

Do not call 3.313m “solar households”: the table includes businesses and homes.

For households specifically, Netbeheer Nederland says there were **2.6 million households with solar at end-2023** and **just under 3 million by end-2024**, representing **over 35% of Dutch households**. It describes household growth slowing from roughly **30% in 2023 to 10% in 2024**.

Source:  
https://www.netbeheernederland.nl/artikelen/nieuws/groei-aantal-huishoudens-met-zonnepanelen-flink-afgenomen

That slowdown matters: primary-installation growth is maturing while the historic installed base keeps ageing.

---

## 2. We can quantify an actual ageing cohort

CBS preserved monthly **small-use** installation-flow data from the Productie Installatie Register.

Derived annual additions:

| Year | New small-use installations |
|---|---:|
| 2012 | 39,738 |
| 2013 | 71,503 |
| 2014 | 69,020 |
| 2015 | 89,981 |
| 2016 | 84,102 |

Therefore the 2012–2014 cohort contains:

# **180,261 small-use installations**

Source: CBS PIR  
https://www.cbs.nl/nl-nl/over-ons/onderzoek-en-innovatie/project/slim-zonnestroom-in-kaart-brengen

CBS explicitly warns this dataset covers **small-use only** and is not total national installation growth. That makes it good cohort evidence, not a national installed-stock series.

Milieu Centraal says:

- average inverter life: **12 years**
- panels: roughly **25+ years**
- replacing the inverter for an 8-panel set: around **€900**

Source:  
https://www.milieucentraal.nl/energie-besparen/zonnepanelen/zonnepanelen-onderhouden-vervangen-of-wegdoen/

So in 2026:

- 2012 cohort = 14 years old
- 2013 = 13
- 2014 = 12

That aligns **180,261 historic small-use installations** with the average inverter-life threshold.

### Critical interpretation

This does **not** mean 180,261 inverters are failing now.

We do not know:
- how many systems survived;
- architecture/make/model mix;
- exact failure distribution;
- previous inverter replacements.

What we do know is much harder and more useful than “solar is ageing”:

> A directly measured installation cohort has reached the age at which the shorter-lived critical component is expected, on average, to require replacement.

This becomes mechanism candidate **COHORT_CROSSING_COMPONENT_LIFETIME**.

---

## 3. Generic inverter replacement is already commoditized

Installatieplatform currently offers:

- postcode-led inverter replacement quotes;
- up to 3 installers;
- “often within 48 hours”;
- all major brands;
- advertised €300–€1,200 range;
- city-specific landing pages.

Source:  
https://www.installatieplatform.nl/diensten/omvormer-vervangen

Its city pages already discuss:
- error codes;
- monitoring loss;
- repair vs replacement;
- string vs micro vs optimizer;
- hybrid inverter/battery readiness;
- warranty handling.

That decisively falsifies:

> “Build Dutch `omvormer vervangen + city` pages and route leads.”

Someone already industrialized that exact SEO/leadgen pattern.

Generic inverter-replacement leadgen = **HOLD**.

---

## 4. Installer insolvency creates a real orphaned installed base

ACM ConsuWijzer explicitly explains the warranty problem when a seller/installateur or manufacturer goes bankrupt, and uses the example of a solar inverter failing after four years.

Source:  
https://consument.acm.nl/energietransitie/wat-zijn-mijn-rechten-bij-verduurzaming-van-mijn-huis

This creates several ownership problems:

- Who is now responsible?
- Does factory warranty survive?
- Who can take over the monitoring portal?
- Which replacement is compatible?
- Who will process manufacturer warranty?
- Who has the old system documentation?

And the market has already started responding.

Zonnepanelen Servicepunt advertises:
- monitoring;
- warranty handling;
- service;
- repairs;
- demount/remount;
- battery upgrades;
- taking over monitoring portals.

It claims **6,000+ solar installations taken over since 2024**.

Source:  
https://contact.zonnepanelenservicepunt.nl/monitoringspakket-zsp-copy

That 6,000 figure is a **vendor claim**, not audited national statistics. It proves a specialist business model exists; it does not quantify orphan TAM.

This is an important GoldProbe distinction:

> Installer attrition creates a genuine ownership discontinuity, but the Netherlands is already productizing it.

So “orphaned solar service” is a valid market, but not obvious whitespace.

---

## 5. The 2027 policy transition changes the replacement decision

The Dutch government will end net metering on **1 January 2027**.

Owners can still feed electricity to the grid and receive compensation, but the government explicitly wants households to use more of their solar electricity directly.

Through 2030, feed-in compensation must be at least 50% of the bare electricity supply tariff.

Source:  
https://www.rijksoverheid.nl/themas/klimaat-milieu-en-natuur/energie-thuis/salderingsregeling

Milieu Centraal gives a useful illustrative example using average **30% direct self-consumption**:

| 8-panel system | Annual savings |
|---|---:|
| 2026 with net metering | €540 |
| 2027+ without net metering | €170 |

That is an illustrative reduction of about **68.5%** under its assumptions.

It also estimates ways to increase direct use:
- shift appliances: roughly +5 percentage points;
- heat-pump hot-water timing: +10–20;
- smart EV charging: +20.

Source:  
https://www.milieucentraal.nl/energie-besparen/zonnepanelen/kosten-en-opbrengst-zonnepanelen/

This does not make batteries automatically rational.

It changes the decision tree.

---

## 6. Replacement in 2026/27 is no longer just “which new inverter?”

A homeowner whose 12-year-old inverter fails is already paying approximately €900 in Milieu Centraal's 8-panel example.

At that exact moment they can ask:

### A. Like-for-like string inverter
Lowest incremental complexity.

### B. Hybrid/battery-ready inverter
Potential option value if a battery may be added later.

### C. Different architecture / optimizers / microinverters
Dependent on existing roof/system topology.

### D. EV smart charging
Potentially increases self-consumption without purchasing a stationary battery.

### E. Home energy management / heat-pump integration
Again potentially increases direct use.

This means the **objective function changed** between original installation and replacement.

That gives mechanism candidate:

# `POLICY_TRANSITION_CHANGES_REPLACEMENT_OBJECTIVE`

The policy does not force replacement.

But when natural component replacement occurs, policy changes what “optimal replacement” means.

That is a significantly subtler opportunity than grant leadgen.

---

## 7. Home batteries are high-ticket — and trust is already damaged

Consumentenbond currently puts an average installed home-battery system at around:

# **€4,000–€6,000**

It says the payback period is long and uncertain and that many systems do not recoup their cost during the battery's average ~15-year life.

Source:  
https://www.consumentenbond.nl/zonnepanelen/thuisbatterij

And in August 2026, Consumentenbond demanded that Groen Adviespunt stop misleading sales practices around energy advice, home batteries and other sustainability products. Consumers reported being pressured into **€249–€299** home energy advice appointments.

Source:  
https://www.consumentenbond.nl/energie-vergelijken/consumentenbond-eist-einde-aan-misleidende-verkooppraktijken-groen-adviespunt

Other 2025–26 warnings document aggressive home-battery selling, exaggerated paybacks and misleading claims.

This tells us something commercially interesting:

> The scarce layer may not be battery suppliers. It may be **credible independent decision quality**.

A marketplace that gets paid only when it sells a battery has an incentive problem.

An independent replacement optimizer could explicitly output:

> **Do not buy a battery. Your best option is X.**

That trust may itself be the product.

But GoldProbe does not yet have actual WTP for independent advice, so this remains a testable hypothesis.

---

## 8. The strongest proposed product

Not:

> “Find an inverter installer.”

Build:

# Legacy Solar Passport / Replacement Optimizer

Inputs:

- address/postcode;
- installation year;
- original installer;
- current inverter brand/model;
- panel brand/count;
- optimizers/microinverters;
- single/three phase;
- current monitoring;
- error code / symptom;
- EV / heat pump;
- battery intent.

Then:

### Step 1 — Establish ownership state
Original installer alive?
Factory warranty?
Monitoring portal access?
Documentation?

### Step 2 — Diagnose lifecycle
Monitoring/network issue?
Repairable fault?
Actual inverter replacement?
Optimizer/panel/string problem?

### Step 3 — Generate technically compatible options

### Step 4 — Optimize replacement objective for 2027
Like-for-like?
Hybrid-ready?
Smart-EV integration?
Battery?
No battery?

### Step 5 — Send identical scope to suppliers

That is an intelligence product rather than an SEO wrapper.

---

## 9. B06 outcome on the channel-openness hypothesis

B06 weakens the hypothesis as a standalone causal model.

### Austria
Complex installed asset, but OEM/service ownership blocks capture.

### Singapore
Open service channel, but routine decision/dispatch is commoditized.

### Ireland
Open enough, while grant/scope/eligibility decision remains complex.

### Netherlands
Open independent ecosystem, but generic inverter replacement is also commoditized.

So:

> **Intermediate channel openness does not itself generate the opportunity.**

Better model:

\[
Opportunity
 pprox
TriggerIntensity
	imes
NonCommoditizedDecisionComplexity
	imes
Spend
	imes
CaptureAccessibility
\]

Then subtract incumbent commoditization.

`Channel openness` belongs inside **CaptureAccessibility**.

That is a much better causal model.

---

## 10. New candidate: COHORT_CROSSING_COMPONENT_LIFETIME

Evidence chain:

1. CBS directly measures 180,261 small-use solar installations added 2012–2014.
2. Those installations are 12–14 years old in 2026.
3. Milieu Centraal gives average inverter life = 12 years.
4. Panels last much longer.

This predicts a **timing regime change** from installation market → inverter aftermarket.

Again:

**not a replacement-volume forecast.**

To promote this to a recurring pattern we need another unrelated installed asset where:
- historical sales/installation cohorts are measurable;
- component/system lifetime is measurable;
- an independently observed replacement market can verify the cohort prediction.

---

## 11. Search/CPC data remain null

No authenticated Google Keyword Planner source was available.

We do not fill the field from an SEO blog.

---

## 12. B06 verdict

| Cell | Verdict |
|---|---|
| Generic inverter replacement lead-gen | **HOLD** |
| Generic solar-service subscription | **HOLD** |
| Orphaned-system takeover | **VALID, already forming** |
| Legacy-system passport | **INVESTIGATE NARROW** |
| 2027 replacement optimizer | **INVESTIGATE** |
| Generic home-battery leadgen | **HOLD** |
| Independent battery/EV/hybrid compatibility decision | **INVESTIGATE NARROW** |

---

## 13. Why the original experiment was useful

B06 was deliberately chosen to remove Ireland's strong compliance/grant forcing.

It answered the question well.

There is clearly aftermarket timing pressure without mandatory remediation.

But generic routing still gets commoditized quickly.

Therefore the strongest cross-probe statement is now:

> **Installed-base scale tells us where transactions can exist. Trigger timing tells us when. Decision complexity tells us whether information has value. Channel openness tells us whether we can capture that value.**

That's a much stronger kernel than “fragmented local trades.”

---

## 14. Autonomous next probe: B07 Finland heat-pump replacement

B06 generated a quantitative mechanism candidate worth attempting to replicate:

`COHORT_CROSSING_COMPONENT_LIFETIME`

Finland heat pumps are the highest-information next experiment because we already know:
- the installed base is enormous;
- there is long annual-sales history;
- the Finnish industry explicitly reports that a replacement market has begun.

So B07 will test:

> **Do historic heat-pump installation cohorts reaching plausible system lifetime correspond to an independently observed replacement wave?**

If yes, cohort-crossing becomes far more credible as a general forecasting mechanism.

If no, it tells us the solar alignment may be accidental or too weak to operationalize.

B07 will then ask where the replacement transaction is actually monetizable:
- legacy model → successor compatibility;
- controls/remotes;
- service;
- filters/cleaning;
- condensate/frost accessories;
- installation routing.


