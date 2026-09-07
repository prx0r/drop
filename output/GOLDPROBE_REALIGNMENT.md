# GoldProbe Realignment Prompt

*For the next probe run: refocus on installed-base lifecycle commerce, not regulatory inspection.*

---

## The Drift

Recent probes (B20-B25) explored:
- B20: Ireland NCT vehicle inspection
- B21: Germany chimney sweep compliance
- B22: France DPE retrofit
- B23: NYC Local Law 97 emissions
- B24: NYC FISP facade
- B25: NYC parking structures

These are **regulatory/compliance inspection markets** — not our core thesis.

---

## Our Core Thesis

**Installed-base lifecycle commerce:**

```
existing equipment ages/fails
    ↓
replacement/upgrade/compatibility need
    ↓
fragmented merchant landscape
    ↓
specialist decision service
    ↓
localized storefront
    ↓
Google Search/Shopping
    ↓
qualified lead / managed transaction
```

---

## What We Should Be Exploring

### Tier 1: Highest Signal (from our data)

| Opportunity | Countries | Evidence |
|-------------|-----------|----------|
| Heat pump lifecycle | FI, NO, DE, DK | 1.8M FI heat pumps, 33% replacement |
| Cabin/remote property | NO, FI, DK | 484K NO cabins, absence mechanism |
| EV model aftermarket | All 5 | Growing fleet, warranty expiry |

### Tier 2: Good Signal (needs validation)

| Opportunity | Countries | Evidence |
|-------------|-----------|----------|
| Home diagnostics | GB, DE, DK | Problem incidence + specialist positioning |
| Solar retrofit | DE, DK | Installed base + regulation change |
| Smart meter transition | DE, DK | Regulatory mechanism |

### Tier 3: Weak Signal (needs more data)

| Opportunity | Countries | Evidence |
|-------------|-----------|----------|
| Davis weather | NO | High score but blocked on supplier |
| Building diagnostics | FI | Specialist positioning |
| Dynamic energy control | DK | Protocol gaps |

---

## The Problem Space for Autonomous Exploration

### 1. Heat Pump Lifecycle (FI/NO/DE/DK)

```
1.8M heat pumps installed in FI
    ↓
112,000 sold in 2025 (+63% YoY)
    ↓
33% are replacements
    ↓
8-year avg age → replacement wave starting
    ↓
Controllers, remotes, filters, Wi-Fi modules
    ↓
Compatibility confusion → specialist opportunity
```

**Queries to explore:**
- "lämpöpumppu ohjain" (heat pump controller)
- "varmepumppu kauko-ohjaus" (heat pump remote)
- "lämpöpumppu suodatin" (heat pump filter)
- "daikin lämpöpumppu ohjain" (Daikin heat pump controller)

### 2. Cabin Remote Property (NO/FI/DK)

```
484K cabins in NO
    ↓
48% outside densely built-up areas
    ↓
Remote ownership → absence amplifies damage
    ↓
Frost, leak, heating failure
    ↓
Need: monitoring, detection, shutoff, response
    ↓
Generic sensor = mature market
    ↓
Response orchestration = opportunity
```

**Queries to explore:**
- "hytte alarm" (cabin alarm)
- "fjernovervaking hytte" (remote monitoring cabin)
- "vannsensor hytte" (water sensor cabin)
- "varmestyring hytte" (heating control cabin)

### 3. EV Model Aftermarket (All Countries)

```
355K BEV registrations in UK (+28.6% YoY)
    ↓
3-year warranty → post-warranty channel
    ↓
Component-level repair (PCB)
    ↓
Local removal → national repair → local reinstall
    ↓
Model-specific fault diagnosis
    ↓
Specialist opportunity
```

**Queries to explore:**
- "zappi repair" (Zappi charger repair)
- "pod point no power" (Pod Point fault)
- "charger out of warranty" (post-warranty)
- "PCB mail-in repair" (component repair)

---

## The Huge Problem Space

### Installed-Base Lifecycle Commerce

```
COUNTRY × ECOSYSTEM × LIFECYCLE_STAGE × MERCHANT_GAP

= opportunity
```

For each country:
1. What large physical systems exist?
2. What lifecycle events do they generate?
3. Where is the merchant gap?
4. What's the supply topology?
5. What's the search demand?

Then intersect:

```
large installed base
× high replacement/event rate
× high ecommerce propensity
× low good-merchant count
× supplier available
× acceptable logistics
× high enough AOV
```

That's the formula.

### The Data We Have

| Data | Source | Value |
|------|--------|-------|
| Installed base sizes | Country packs | 1.8M FI heat pumps, 484K NO cabins |
| Replacement rates | GoldProbe reports | 33% FI heat pump replacement |
| Merchant counts | Country packs | 3-9 merchants per country |
| Hypotheses | Generated from probes | 36 across 7 countries |
| Mechanisms | GoldProbe reports | 5 discovered, 3 transferred |
| Case studies | 22 cases | Real economics from operators |

### What's Missing

| Gap | Impact | Fix |
|-----|--------|-----|
| Real CPC data | Can't validate economics | Wait for Google Ads API |
| Real merchant density | Can't measure competition | Use Places Insights |
| Real supplier costs | Can't calculate margins | Contact suppliers |
| Real CVR data | Can't validate conversion | Need actual store |

---

## The Autonomous Exploration Protocol

For each country × ecosystem combination:

1. **Load installed base data** from country pack
2. **Generate lifecycle hypotheses** from installed_base.py
3. **Check merchant density** from country data
4. **Calculate economics** with assumed margins
5. **Rank by EVI** (expected value of information)
6. **Select top opportunity** for deep research
7. **Run GoldProbe** to validate
8. **Update BigQuery** with new observations
9. **Repeat**

### The Query Forest

For each ecosystem, generate native-language queries:

```
heat_pump:
  FI: "lämpöpumppu ohjain", "lämpöpumppu kauko-ohjaus", "daikin lämpöpumppu"
  NO: "varmepumpe kontroller", "varmepumpe kjerne", "daikin varmepumpe"
  DE: "wärmepumpe controller", "wärmepumpe fernbedienung", "daikin wärmepumpe"
  DK: "varmepumpe controller", "varmepumpe fjernbetjening", "daikin varmepumpe"
```

### The Merchant Gap Detection

For each ecosystem × country:
1. Count total sellers
2. Count good sellers (quality score > 70)
3. Calculate merchant gap = (demand - good_sellers) / demand
4. Flag if merchant_gap > 0.5

### The Economics Check

For each product × country:
1. Get retail price from observations
2. Get supplier cost (if known)
3. Calculate margin
4. Check if margin > break-even
5. Flag if margin < 0

---

## The Next Probe Should Be

**Finland Heat Pump Controller**

Not another regulatory inspection market.

The evidence is strong:
- 1.8M installed heat pumps
- 33% replacement share
- 8-year avg age → replacement wave starting
- Controllers, remotes, filters needed
- Specialist opportunity exists

**Falsifier:** If Finnish heat pump controllers are already well-served by existing merchants, kill this hypothesis.

**Queries to test:**
- "lämpöpumppu ohjain" (heat pump controller)
- "varmepumppu kauko-ohjaus" (heat pump remote)
- "lämpöpumppu suodatin" (heat pump filter)

That's lifecycle commerce. Not regulatory inspection.
