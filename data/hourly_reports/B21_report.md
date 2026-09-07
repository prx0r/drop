# GoldProbe B21 — Germany Chimney-Sweep / Heating Compliance

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled

## Executive result

**B21 does not simply replicate Ireland NCT. It finds a much richer hybrid architecture.**

Germany has more than **32 million combustion installations** subject to chimney-sweep measurements/checks. Its 2025 national survey was built from data collected by about **7,600 appointed district chimney sweeps**.

Source:
https://www.schornsteinfeger.de/sites/default/files/downloads/Erhebungen_2025.pdf

The key market topology is unusual:

1. some duties are **sovereign/monopoly** and can only be done by the appointed district chimney sweep;
2. many routine measuring/cleaning/checking tasks are **competitive** and the owner can choose another qualified chimney-sweep business;
3. if another provider is used, legally defined proof has to flow back to the district sweep;
4. the district sweep maintains an electronic longitudinal **Kehrbuch**;
5. conflict-of-interest rules explicitly stop the district sweep using its official position/data to win private commercial work.

So B21's strongest finding is not a lead marketplace.

It is:

> **regulation has created a distributed, machine-readable installed-asset graph while simultaneously erecting a firewall around commercial use of the privileged data.**

---

## 1. The installed base is enormous and old

ZIV's 2025 survey says chimney sweeps carry out measurements/checks on **more than 32 million combustion installations**.

It separately identifies:
- around **14.8m gas combustion installations**
- **3,701,850** recurrently measurement-obliged oil installations
- **5,170,340** recurrently measurement-obliged gas installations.

The 2025 stock is extremely old:
- **>86%** of the recurrent oil population is over 20 years old
- around **66%** of recurrent gas installations are over 20 years old.

Source:
https://www.schornsteinfeger.de/sites/default/files/downloads/Erhebungen_2025.pdf

This is not just old hardware. Age changes the compliance frequency.

---

## 2. Age literally shortens the statutory inspection clock

1. BImSchV §15 requires qualifying oil/gas installations to be measured:

- **every 3 calendar years** when commissioning/material alteration was <=12 years ago
- **every 2 calendar years** once >12 years old
- every 5 years for certain self-calibrating continuous combustion-control systems.

Source:
https://www.gesetze-im-internet.de/bimschv_1_2010/__15.html

This independently replicates B20's ageing-car mechanism.

### `AGE_SHORTENS_COMPLIANCE_CLOCK`

The older asset:
- has more physical ageing risk,
- and regulation asks for it more often.

That compounds transaction frequency.

---

## 3. The 2025 safety/remediation surface is hard-measured

In 2025 chimney sweeps measured CO at **>9.2m gas combustion installations**.

The two KÜO tables contain:

### 500–1,000 ppm
- room-air dependent: 89,910
- independent: 15,860
- combined: **105,770**

### >1,000 ppm
- room-air dependent: 65,090
- independent: 11,160
- combined: **76,250**.

Source:
https://www.schornsteinfeger.de/sites/default/files/downloads/Erhebungen_2025.pdf

ZIV states:
- 500–1,000 ppm → maintenance recommended
- >1,000 ppm → defect notification/deadline; the installation **must be maintained and checked again**.

Source:
https://www.schornsteinfeger.de/informationen/leistungen/schornsteinfegerarbeiten

So there are at least **76,250 observed 2025 gas-measurement outcomes** with a hard maintenance/recheck trigger.

These are measurement outcomes, not guaranteed unique properties.

---

## 4. Nearly one million individual defects were recorded

2025 ZIV defect table:

- sovereign tasks: **570,300**
- general chimney-sweep tasks: **383,300**
- total: **953,600 individual defects**.

Largest categories:
- fireplace/equipment: **409,100**
- vertical flue: **197,700**
- connector: **128,800**
- combustion-air supply: **91,500**
- installation conditions: **78,200**.

Source:
https://www.schornsteinfeger.de/sites/default/files/downloads/Erhebungen_2025.pdf

Gas alone contributed **471,800 individual defects**.

Important epistemic guardrail:

> ZIV explicitly says these are individual defects, **not the number of defective installations**.

It also says the real defect count is likely somewhat higher because of 2025 software/evaluation limitations and excluded low-risk verbal findings.

So GoldProbe does not manufacture a "953k customers" TAM.

---

## 5. Emissions measurements create another quantified service trigger

2025 1.BImSchV results:

Oil:
- measured: **1,969,030**
- excessive soot: **18,200**
- oil derivatives: **2,150**
- CO >1,300 mg/kWh: **8,710**
- excessive flue loss: **31,720**.

Gas:
- measured: **2,323,200**
- excessive flue loss: **23,320**.

Source:
https://www.schornsteinfeger.de/sites/default/files/downloads/Erhebungen_2025.pdf

Again, these are observed compliance findings, not inferred search demand.

---

# 6. The crucial structural distinction: some tasks are monopoly, others are open

ZIV says the owner cannot freely select the provider for sovereign tasks such as:

- Feuerstättenschau
- issuing the Feuerstättenbescheid
- certain building-law acceptances.

These belong to the appointed district chimney sweep.

But activities such as:
- sweeping
- measurements
- specified checks

are competitive/non-sovereign, and another qualified chimney-sweep business may be chosen.

Sources:
https://www.schornsteinfeger.de/popup/kann-ich-mir-einen-schornsteinfeger-aussuchen
https://www.schornsteinfeger.de/popup/was-sind-freie-taetigkeiten

Competitive services have free-market pricing rather than the sovereign fee regime.

This is neither Britain MOT nor Ireland NCT.

It is a **partially liberalized compliance graph**.

---

# 7. The privileged inspector has an explicit commercial firewall

SchfHwG §18 requires the appointed district chimney sweep to perform official duties impartially.

It also creates conflict rules around certifying installations sold/installed by the sweep or related financially connected parties.

Source:
https://www.gesetze-im-internet.de/schfhwg/__18.html

The industry compliance guideline is even more explicit:

- the official position must not generate economic advantage
- sovereign and commercial work must not be mixed
- the sweep cannot advertise/acquire private work during a Feuerstättenschau
- official data cannot be used for private commercial activity
- official correspondence such as a Feuerstättenbescheid cannot advertise private services.

Source:
https://www.schornsteinfeger.de/ueber-uns/compliance-richtlinie-fuer-das-schornsteinfegerhandwerk

This produces:

## `REGULATORY_ROLE_FIREWALL_LIMITS_CROSS_SELL`

This is a new variable for GoldProbe.

A party can have extraordinary privileged access to a problem **without being legally allowed to monetize that information advantage freely**.

That can reopen downstream competition.

---

# 8. If the owner changes provider, the proof must come back

Under SchfHwG §4, if the owner uses someone other than the district sweep for the work specified in the Feuerstättenbescheid:

- proof is mandatory
- form/certificates generally need to be sent within the statutory time window
- the executing sweep fills them in
- where the district sweep offers suitable digital access, the executing provider must transmit them electronically in **machine-readable and evaluable form**
- the stable object number from the Feuerstättenbescheid is included.

Source:
https://www.gesetze-im-internet.de/schfhwg/__4.html

That is unusually strong data infrastructure.

The competitive provider can change.

The compliance identity of the asset does not.

---

# 9. The Kehrbuch is effectively a regulated installed-asset graph

SchfHwG §19 requires an electronic Kehrbuch.

Fields include:

- owner/manager
- address
- asset type
- fuel
- rated heat output
- age
- boiler type
- location and flue assignment
- prescribed works
- execution dates
- last two Feuerstättenschau results
- recorded defects
- date defect corrected
- inspection/verification results.

It must:
- be complete and chronological
- be checked at least quarterly
- close annually
- preserve continuity across district-sweep handover
- transfer electronic data machine-readably
- retain relevant history for seven years.

Source:
https://www.gesetze-im-internet.de/schfhwg/__19.html

This produces B21's biggest discovery:

# `COMPLIANCE_LEDGER_CREATES_ASSET_GRAPH`

> A recurring regulatory process can quietly create a longitudinal installed-base database with exact asset characteristics, service clocks, defects and remediation events.

This is almost exactly the kind of ground-truth asset graph we have been trying to assemble manually.

---

## 10. But the Kehrbuch is NOT a free lead database

The same statute limits personal-data transfer.

GDPR applies, and private third-party disclosure requires legal authority/interest conditions.

Therefore:

**Do not scrape/repurpose Kehrbuch data into commercial prospecting.**

The opportunity is owner-authorized workflow/data portability, aggregated lawful data, or finding analogous regimes where the ledger is legitimately open.

That is why B22 is going directly after **public compliance ledgers**.

---

## 11. The downstream private supply market is enormous

Germany's SHK trade currently comprises around:

- **48,000 businesses**
- **390,000 employees**
- **€59.1bn 2025 revenue**.

Source:
https://www.zvshk.de/presse/medien-center/pressemitteilungen/shk-handwerk-2025-umsatz-und-auftraege-ruecklaeufig-investitionsstau-bremst-branche

This is broader than heating repair, so GoldProbe does not call it a heating-maintenance TAM.

But it establishes a huge fragmented downstream technical supply base.

The chimney-sweep profession itself has around:
- **7,300 guild businesses**
- >11,000 energy advisers
- >16,000 employees/trainees
- >200,000 customer contacts **per day**.

Source:
https://www.schornsteinfeger.de/ueber-uns/branche/branchenzahlen-und-anlagenbestand

---

# 12. What business actually survives the evidence?

Not:

> Schornsteinfeger near me.

Not:

> scrape Kehrbuch and sell boiler leads.

Potentially:

## Heating Compliance Passport — portfolio version

Owner/property manager supplies:
- Feuerstättenbescheide
- equipment records
- prior forms/certificates
- defect notices.

System extracts:

```text
asset
fuel
age
power
district
sovereign tasks
competitive tasks
deadline
last completion
defects
repeat measurement
heating-maintenance requirement
```

Then:

1. distinguish monopoly task from open task
2. calendar compliance
3. obtain qualified competitive quotes where legal
4. route CO/technical defects to appropriate SHK firm
5. collect completion certificate
6. return proof to district sweep
7. retain auditable owner copy.

That is substantially more defensible than a directory.

---

# 13. B20 vs B21

### Ireland NCT
diagnoser **cannot repair**
→ high-intent demand exported.

### Germany chimney sweep
district diagnoser can also participate in some private market activities
→ but role/data are legally firewalled
→ owner can choose alternate providers for free tasks
→ proof flows back into regulatory ledger.

So:

`DIAGNOSER_CAN_REPAIR`

was still too coarse.

We now need:

### `REGULATORY_ROLE_FIREWALL`
as a separate dimension.

---

# 14. Age/compliance compounding independently replicates

B20:
cars 10+ years
→ lower first-pass
→ annual NCT.

B21:
oil/gas system >12 years
→ statutory measurement every 2 rather than 3 years.

And the relevant German fossil-heating stock is extraordinarily old.

So:

### `AGE_SHORTENS_COMPLIANCE_CLOCK`
is now independently replicated outside automotive.

This is becoming a robust lifecycle mechanism.

---

# 15. Highest-value new data insight

The market opportunity from B21 is decent.

The **data architecture insight is exceptional**.

For future GoldProbes, ask:

> Does regulation already maintain the asset graph we are trying to reconstruct?

Look for:

- stable object ID
- install date
- model/technology
- inspection events
- defects
- repairs
- next due date
- certified provider
- evidence
- public/private access.

If public, that could be massively better than Google Trends.

If private, owner-authorized workflow may still be viable.

---

# 16. Autonomous next probe — B22 France DPE

B21's novel mechanism is `COMPLIANCE_LEDGER_CREATES_ASSET_GRAPH`.

The most informative next test is not another private compliance system.

France's DPE energy-certificate system is a direct accessibility experiment:

- mandatory standardized property assessment
- public/open database
- address/building attributes
- energy/heating information
- legal rental thresholds
- known future dates
- renovation subsidies/trades.

Hypothesis:

> **If the compliance ledger is publicly accessible, address-level, and connected to future legal deadlines, it can become a predictive demand graph rather than merely an internal compliance record.**

The falsifier is equally important: if DPE algorithm changes, data quality, privacy/direct-marketing rules, incumbent France Rénov' infrastructure or weak conversion make the open data commercially unusable, then `public ledger = gold` is too simplistic.
