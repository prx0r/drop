# HCC V2 — Compatibility Commerce Compiler

*Generated: 2026-09-07*
*Status: REFINED — 20 campaigns with corrected scoring*

---

## The Corrected Scoring Formula

```text
HCC_V2 =

25% information rent
    identity difficulty
    compatibility complexity
    supersession complexity

15% installed-base economics
    installed units
    replacement frequency
    urgency

20% supplier arbitrage
    stock depth
    operational quality
    obtainable net price
    stock feed
    direct ship / fulfilment

15% distribution fit
    parcel suitability
    GMC eligibility
    visual search suitability
    structured-data potential

15% economics
    contribution/order
    AOV
    repeat purchase
    adjacency expansion

10% evidence quality
    first-party installed-base evidence
    actual supplier evidence
    actual merchant-gap evidence

MINUS:
0–15 best-specialist penalty
0–15 safety/install penalty
0–10 supplier uncertainty
0–10 return/liability penalty
```

---

## Hard Gates Before Scoring

```text
SUPPLIER EXISTS AND WILL SELL TO US
STOCK CAN BE KEPT FRESH
COMPATIBILITY CAN BE PROVEN, NOT GUESSED
LEGAL/INSTALLATION RESPONSIBILITY IS EXPLICIT
```

---

## The Three Variants

```text
A. REPLACEMENT
broken thing → identify → exact compatible part

B. MIGRATION
obsolete thing → identify current state → exact successor bundle

C. REPAIR ORCHESTRATION
failed thing → identify → decide repair vs replace → part + technician
```

All three use the same kernel:

```
PHYSICAL ASSET
    ↓
IDENTITY
    ↓
STATE / GENERATION
    ↓
COMPATIBILITY GRAPH
    ↓
SUPPLIER STATE
    ↓
PRODUCT / MIGRATION / REPAIR
    ↓
TRANSACTION
    ↓
OBSERVED OUTCOME
```

---

## The 20 Campaigns

### Launch Now

| # | Campaign | Score | Type |
|---|----------|-------|------|
| 1 | Finland Allaway Central-Vacuum | 92/100 | ATTACK |
| 2 | Finland Vallox Legacy Ventilation | 89/100 | ATTACK |
| 3 | Ireland BioCycle Wastewater Parts | 90/100 | ATTACK (NEW) |
| 4 | Norway Cabin Pressure-Water | 84/100 | ATTACK |
| 5 | Finland Ouman Legacy Heating Migration | 84/100 | ATTACK (NEW) |
| 6 | Denmark Nilan Legacy Ventilation Migration | 83/100 | ATTACK (NEW) |

### Supplier/Compatibility Validation Immediately

| # | Campaign | Score | Type |
|---|----------|-------|------|
| 7 | Norway Cinderella Comfort Components | 81/100 | ATTACK |
| 8 | Finland/Sweden NIBE F-Series Lifecycle | 80/100 | VERIFY |
| 9 | Denmark Danfoss Underfloor-Heating Migration | 80/100 | ATTACK (NEW) |
| 10 | Finland Heat-Pump Electronics (narrowed) | 76/100 | VERIFY |
| 11 | UK EV Charger PCB Repair + Technician Orchestration | 78/100 | PIVOT (NEW) |
| 17 | Nordic Garage-Door Radio & Controller Migration | 72/100 | ATTACK (NEW) |

### Only Launch After Incumbent-Gap Test

| # | Campaign | Score | Type |
|---|----------|-------|------|
| 12 | Finland Harvia Legacy Controller Migration | 66/100 | VERIFY |
| 13 | Norway Flexit Legacy Ventilation Type-Plate Resolver | 68/100 | VERIFY |
| 14 | Netherlands Brink Obsolescence Router | 75/100 | ATTACK (NEW) |
| 15 | Nordic Alde/Primus Hydronic Heating Lifecycle | 75/100 | VERIFY (NEW) |
| 16 | UK Boiler Repair Decision Router | 68/100 | VERIFY (NEW) |

### Engine Benchmarks

| # | Campaign | Score | Type |
|---|----------|-------|------|
| 18 | Finland Metos Professional-Kitchen Photo-to-PO | 84/100 B2B | BENCHMARK (NEW) |
| 19 | Nordic Automower Compatibility Benchmark | 56/100 | BENCHMARK |
| 20 | Norway Jabsco Impeller Visual Benchmark | 58/100 | BENCHMARK |

---

## The Reclassification

| Original Campaign | Original Score | Revised Score | Decision |
|-------------------|----------------|---------------|----------|
| Allaway Finland | 123 | 92/100 | ATTACK |
| Vallox Finland | 118 | 89/100 | ATTACK |
| Norway cabin water | 115 | 84/100 | ATTACK after supplier check |
| Finland heat-pump electronics | 110 | 76/100 | VERIFY / narrow |
| Automower | 105 | 56/100 | BENCHMARK |
| Harvia controls | 100 | 66/100 | VERIFY |
| UK EV aftersales | 95 | 78/100 | PIVOT to PCB repair |
| Norway radon | 90 | 83/100 service | Separate Services track |
| Ireland lead pipe | 85 | 77/100 service | Separate Services track |
| Finland pipe inspection | 80 | 43/100 | KILL from HCC |
| Norway Jabsco | 75 | 58/100 | BENCHMARK |

---

## The Key Insight

The highest-priority commercial action is no longer generating campaign #21. It is **supplier validation across campaigns 1–6 in parallel**. The first one that produces actual net pricing + live inventory access + direct fulfilment should immediately become the first live store.

The intelligence system has now generated enough candidates; **supplier reality is the next information bottleneck**.

---

## Sources

1. Husqvarna — power supply fitment tables
2. DSA — radon action threshold 100 Bq/m³
3. Gov.ie — lead pipe grant €5,000
4. Shopify — agentic storefronts product exclusions
5. Allaway — 250,000+ Finnish homes
6. Google Merchant Center — related_product
7. Vallox — consumers cannot buy direct
8. BioCycle — "Online Shop Coming Soon!!"
9. BioCycle — FPS system components
10. SSB — 483,631 holiday houses
11. Ouman — EH-8/EH-80 discontinued
12. Ouman — EH-800 direct sales
13. Ouman — discontinued products list
14. Nilan — parts through partners only
15. Nilan — CTS602 HMI upgrade kit
16. Cinderella — service parts manual
17. NIBE — serial number locations
18. Danfoss — Icon2 application guide
19. SULPU — 1.8M heat pumps Finland
20. eBay UK — Pod Point PCB repair service
21. GOV.UK — 412,682 home charger installations
22. Byggventilasjon — 1,000+ Flexit spare products
23. Byggventilasjon — Flexit spare pricing
24. Brink Air Shop — discontinued models list
25. Vaillant UK — £399 fixed-price repair
26. Garage-door-remotes.co.uk — Hörmann migration
27. Somfy — RTS receiver
28. Metos — 15,000+ spare parts
29. Metos — phone/email spare parts
30. Xylem — Jabsco impeller identification
