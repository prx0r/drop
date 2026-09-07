# Gold Campaign B — Norway Wallas Cabin Heater Parts

*Generated: 2026-09-07*
*Score: 91/100*
*Status: ATTACK*

---

## The Pitch

**452k–484k Norwegian recreational buildings. Wallas has decades of heater generations. Control panel 361062 fits 22Dt/22GB/26CC/26CC Winter/30Dt/30GB/40CC/40CC Winter/40Dt. Sunwind has dealer-only spare parts and accepts dealer applications.**

---

## Why This Is #2

| Factor | Data | Score |
|--------|------|-------|
| **Installed base** | 452k–484k recreational buildings | 9/10 |
| **Replacement frequency** | Heaters fail, controllers die | 8/10 |
| **Identity difficulty** | "Which Wallas do I have?" | 9/10 |
| **Compatibility complexity** | Model-dependent, generation-dependent | 9/10 |
| **Wrong part cost** | Wrong controller = doesn't work | 9/10 |
| **Purchase urgency** | High (cabin = no heat) | 9/10 |
| **Self-service resolution** | Consumer can photograph heater/panel | 9/10 |
| **Pre-SKU uncertainty** | High — consumer doesn't know model | 9/10 |
| **Digital merchant gap** | Sunwind dealer-only, Wallas parts database good but fragmented | 8/10 |
| **Language fragmentation** | Norwegian documentation | 9/10 |
| **Visual identifiability** | Photos of heater, panel, model plate | 9/10 |
| **Gross margin** | 25-35% on parts | 8/10 |
| **Shipping suitability** | Small parcel, lightweight | 9/10 |
| **Supplier accessibility** | Sunwind accepts dealer applications | 9/10 |

**Score: 123/140**

---

## The Evidence

### 1. 452k–484k recreational buildings

SSB data: 48% geographically scattered.

### 2. Wallas control panel 361062 fits 9 models

22Dt, 22GB, 26CC, 26CC Winter, 30Dt, 30GB, 40CC, 40CC Winter, 40Dt.

### 3. Real pricing

- Control panel: NOK 2,999
- FC2 pump: NOK 2,999
- Glow-plug kit: NOK 979
- Tank connector: NOK 795
- Control cable: NOK 799

### 4. Sunwind dealer-only spare parts

Sunwind explicitly has dealer-only spare parts and accepts dealer applications.

### 5. Wallas has good parts database

But fragmented across dealers.

---

## What We Build

### "Wallas Cabin Heater Resolver"

```
Wallas model families: M2600, M4000, M26, M40, 26CC, 40CC, 22Dt, 30Dt, 40Dt, 22GB, 30GB
Components: control panels, pumps, glow-plugs, tank connectors, cables
For every component:
  - compatible models
  - supersession chain
  - installation notes
```

---

## Unit Economics

| Metric | Value |
|--------|-------|
| Average order value | NOK 1000-3000 |
| Gross margin | 25-35% |
| Net per order | NOK 250-1050 |
| Break-even orders/month | 10 |

---

## Supplier Strategy

- Sunwind (dealer application)
- Wallas direct
- Norwegian cabin part distributors

---

## 30-Day Experiment

1. Enumerate 50-100 Wallas components
2. Apply as Sunwind dealer
3. Build compatibility graph
4. Test Norwegian query/photo flow
5. Launch Shopify + Merchant Center

**Success:** Dealer agreement, 50 SKUs live, first paid order.

**Falsifier:** Wallas/Sunwind already resolve identification adequately.
