# Gold Campaign C — Nordic Hot-Tub Control Resolver

*Generated: 2026-09-07*
*Score: 90/100*
*Status: ATTACK*

---

## The Pitch

**Consumer has expensive physical asset. One little controller dies. Replacement identity is confusing. Component is often plug-and-play. Consumer brand ≠ component manufacturer. Balboa/Gecko systems under Vikingbad/Nordic/Sundance.**

---

## Why This Is #3

| Factor | Data | Score |
|--------|------|-------|
| **Installed base** | Large Nordic hot-tub installed base | 8/10 |
| **Replacement frequency** | Controllers fail, screens die | 8/10 |
| **Identity difficulty** | "Which Balboa system is in my Vikingbad?" | 10/10 |
| **Compatibility complexity** | Serial-number ranges, dealer-only panels | 10/10 |
| **Wrong part cost** | Wrong panel = doesn't fit controller | 9/10 |
| **Purchase urgency** | High (expensive asset, unusable) | 9/10 |
| **Self-service resolution** | Consumer can photograph panel/controller | 9/10 |
| **Pre-SKU uncertainty** | Very high — consumer doesn't know Balboa model | 10/10 |
| **Digital merchant gap** | Fragmented, some dealer-only | 9/10 |
| **Language fragmentation** | Finnish/Norwegian/Swedish | 9/10 |
| **Visual identifiability** | Photos of panel, controller, model plate | 9/10 |
| **Gross margin** | 25-35% on controls | 8/10 |
| **Shipping suitability** | Small parcel, lightweight | 9/10 |
| **Supplier accessibility** | Finnish/Norwegian spa part retailers | 8/10 |

**Score: 124/140**

---

## The Evidence

### 1. Consumer brand ≠ component manufacturer

Vikingbad / Nordic / Sundance → Balboa / Gecko / Spanet

### 2. Real pricing

- Balboa VL260: ~€199
- TP800: ~€349
- Gecko IN.K500: ~€425
- Norwegian panels: NOK 2,000–8,800
- Controller boxes/PCBs: NOK 5k–15k

### 3. Serial-number ranges matter

Some panels only fit given serial-number ranges. Some are dealer-only.

### 4. Reddit confirms pain

Hot-tub owners repeatedly describe obsolete control panels, unknown manufacturers, difficulty figuring out compatibility.

---

## What We Build

### "Nordic Hot-Tub Control Resolver"

```
Hot-tub brands: Vikingbad, Nordic, Sundance, etc.
Control systems: Balboa VL/TP, Gecko IN.K, Spanet
For every panel:
  - compatible controllers
  - serial-number ranges
  - installation notes
  - safety requirements
```

---

## Unit Economics

| Metric | Value |
|--------|-------|
| Average order value | EUR 200-700 |
| Gross margin | 25-35% |
| Net per order | EUR 50-245 |
| Break-even orders/month | 15 |

---

## Supplier Strategy

- AuraSpa (Finland)
- Viskan Spa (Norway)
- Folkpool (Sweden)
- Balboa/Gecko distributors

---

## 30-Day Experiment

1. Enumerate 50 Balboa/Gecko panels
2. Map serial-number compatibility
3. Find supplier with dealer access
4. Test photo identification flow
5. Launch Shopify + Merchant Center

**Success:** Supplier agreement, 30 SKUs live, first paid order.

**Falsifier:** Balboa/Gecko already resolve identification adequately.
