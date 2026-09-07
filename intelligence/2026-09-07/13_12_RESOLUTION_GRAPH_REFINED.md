# Resolution Graph — Refined with Merchant Center Intelligence

*Generated: 2026-09-07 13:12 UTC*
*Status: CORE THESIS — This is what we build*

---

## The One Sentence

> **Own the evidence-backed compatibility graph and live supplier state; use Merchant Center, Shopify Catalog, structured web data and eventually UCP/ACP as distribution rails.**

The feeds are extraordinarily well matched to this business, but **the feeds themselves are not the moat**. The moat is knowing, with unusually high certainty, *what the object is, what fits it, what does not fit it, what superseded it, and who actually has the correct replacement available now*.

---

## The Internal Object Model

```
INSTALLED ASSET
Bosch SMS46MI08E
        │
        ├── has_part ────── Bosch 00631200
        │                       │
        │                       ├── superseded_by → 00651956
        │                       ├── voltage → 230V
        │                       ├── connector → X
        │                       └── incompatible_with → ...
        │
        ├── model_plate_location
        ├── production_years
        └── visual signatures

                         ↓ flatten

GOOGLE
brand + MPN
product_detail
question_and_answer
document_link
related_product
images/video
availability
price
local inventory

SHOPIFY
rich PDP
structured variants
Catalog
machine-readable inventory

WEB
JSON-LD
crawlable compatibility pages
manual/evidence pages
```

---

## Market Ranking

| Rank | Market / Niche | Why It Fits | Verdict |
|------|----------------|-------------|---------|
| **1** | 🇫🇮 Allaway legacy central-vacuum parts | 250k+ Finnish homes, decades of legacy systems, serial/model dependence, huge local B2B parts inventories | **Exceptional** |
| **2** | 🇫🇮 Vallox legacy ventilation parts | Old installed units, model plates, fans/boards/sensors/controllers, manufacturer doesn't sell spares direct to consumers | **Exceptional** |
| **3** | 🇳🇴 Cabin water-system replacement graph | Enormous cottage base, pumps/pressure switches/diaphragms/strainers with voltage/pressure/thread compatibility | **Very strong** |
| **4** | 🇫🇮 Heat-pump lifecycle electronics | 1.8m cumulative heat pumps; aging replacement base; controls/sensors/receivers/boards | **Strong, but not remotes alone** |
| **5** | 🇳🇴/🇸🇪/🇫🇮 Automower legacy charging ecosystem | Year/generation/amp/pinout ambiguity, huge installed base | **Great benchmark** |
| **6** | 🇫🇮 Helo/Tylö/Harvia legacy controls | ~3m sauna installed base, obsolete controllers and adapters | **Strong but safety/competition penalty** |
| **7** | 🇳🇴 Jabsco/Johnson marine pump/impeller identity | Almost perfect "what is this?" photo problem | **Technically perfect** |
| **8** | 🇬🇧 EV charger aftersales parts + repair | Large installed base, new repair wave, compatibility + technician need | **Excellent hybrid** |

---

## Finland Is the Proving Ground

```text
~1.8m heat pumps
250k+ Allaway households
~3m saunas
large mechanical-ventilation installed base
long equipment lifetimes
Finnish-language documentation
excellent local logistics
lots of competent technical distributors
```

That is far more interesting for this thesis than generic "low ecommerce competition."

It is **installed-base density × technical fragmentation**.

Google's AI Mode currently supports both Finland and Norway, including Finnish and Norwegian language availability.

---

## The Screening Formula

```text
HIGH_CERTAINTY_COMMERCE_SCORE =

installed_base
× replacement_frequency
× identity_difficulty
× compatibility_complexity
× supersession_complexity
× wrong_part_cost
× purchase_urgency
× supplier_stock_depth
× supplier_operational_quality
× digital_merchant_gap
× language_fragmentation
× visual_identifiability
× gross_margin
× shipping_suitability

÷ OEM_DTC_quality
÷ best_specialist_quality
÷ return_risk
÷ installation/safety_risk
```

The killer feature: **Can we materially beat the single best seller on certainty?**

---

## Supplier Requirements — Priority Zero

Before a niche can go live:

```
stock access                PASS
stable supplier SKU         PASS
wholesale economics         PASS
blind/direct shipping       PASS
dispatch SLA                PASS
returns/RMA                 PASS
stock freshness             PASS
consumer-safe packaging     PASS
```

No warehouse, yes. No shipping operation, yes. No inventory capital, yes. No retail responsibility, **no**.

---

## What to Launch First

**Finland → Allaway legacy central-vacuum compatibility.**

```text
boring
old
large installed base
model-dependent
visual identity possible
many aliases/generations
consumables + failures + upgrades
small parcel goods
local stock
trade-oriented distribution
repeat demand
high informational value
low fashion risk
```

Build 50–100 SKUs insanely well instead of 5,000 mediocre SKUs.

---

## The Reusable Company

```
NICHE DISCOVERY
      ↓
OEM DOCUMENT INGEST
      ↓
ASSET/PART GRAPH
      ↓
VISUAL IDENTIFICATION DATASET
      ↓
SUPPLIER NORMALIZATION
      ↓
GMC + SHOPIFY + WEB
      ↓
TRANSACTION
      ↓
WRONG-PART / SUCCESS OUTCOME
      ↓
GRAPH IMPROVES
      ↓
CLONE INTO NEXT INSTALLED BASE
```

Every launch leaves behind a reusable **resolution engine**, and each sale produces compatibility evidence rather than merely revenue.

---

## Sources

1. Google Merchant Center — Related product
2. Allaway Finland
3. Vallox support
4. SSB holiday houses
5. SULPU heat pump sales
6. Innoair heat pump remotes
7. Husqvarna Automower power supplies
8. Google AI Mode supported countries
9. Shopify Catalog
10. Google Merchant Center local inventory
11. Google Merchant Center Q&A
12. Google Merchant Center video_link
13. EU consumer guarantees
