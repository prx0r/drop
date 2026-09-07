# Gold Campaign H — Finland Ouman Heating Control Migration

*Generated: 2026-09-07*
*Score: 84/100*
*Status: ATTACK*

---

## The Pitch

**Ouman explicitly says EH-8 and EH-80 are discontinued. EH-800/EH-800B are successors. Migration is not one-to-one: EH-8 may require all parts changed, EH-80 needs different adapter. System state → migration bundle.**

---

## Why This Is #8

| Factor | Data | Score |
|--------|------|-------|
| **Installed base** | Large Finnish heating installed base | 8/10 |
| **Replacement frequency** | Controllers fail, owners upgrade | 7/10 |
| **Identity difficulty** | "Which Ouman controller do I have?" | 9/10 |
| **Compatibility complexity** | EH-8/EH-80 → EH-800, adapter-dependent | 10/10 |
| **Wrong part cost** | Wrong adapter = doesn't work | 9/10 |
| **Purchase urgency** | Medium (heating system, not emergency) | 7/10 |
| **Self-service resolution** | Consumer can photograph controller/wiring | 8/10 |
| **Pre-SKU uncertainty** | High — consumer doesn't know version | 9/10 |
| **Digital merchant gap** | Ouman sells direct but migration is complex | 7/10 |
| **Language fragmentation** | Finnish documentation | 8/10 |
| **Visual identifiability** | Photos of controller, wiring, valve | 8/10 |
| **Gross margin** | 20-30% on migration bundles | 7/10 |
| **Shipping suitability** | Small parcel, lightweight | 9/10 |
| **Supplier accessibility** | Ouman direct + distributors | 7/10 |

**Score: 111/140**

---

## The Evidence

### 1. Ouman explicitly says EH-8/EH-80 discontinued

EH-800/EH-800B are named successors.

### 2. Migration is not one-to-one

EH-8 may require all parts changed. EH-80 needs different adapter. Some sensors can be reused.

### 3. Ouman sells current equipment directly

Moat is not distribution. It is the migration decision layer.

### 4. Discontinued-product catalog exposes old→new relationships

Extraordinary dataset.

---

## What We Build

### "Ouman Migration Engine"

```
Input: controller model, existing valve, firmware/version, photos of wiring, desired connectivity
Output: EH-800/EH-800B + correct valve adapter + sensor replacement/reuse decision + installation instructions
```

---

## Unit Economics

| Metric | Value |
|--------|-------|
| Average order value | EUR 200-500 |
| Gross margin | 20-30% |
| Net per order | EUR 40-150 |
| Break-even orders/month | 15 |

---

## 30-Day Experiment

1. Enumerate 50 EH-8/EH-80 configurations
2. Map migration paths
3. Find supplier or affiliate with Ouman
4. Test migration resolver
5. Launch as decision engine

**Success:** 30 verified migration paths, 1 supplier/affiliate, first transaction.

**Falsifier:** Ouman's own tools already resolve migration adequately.
