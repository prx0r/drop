# Gold Campaign #6 — Finland Harvia Sauna Controller Migration

*Generated: 2026-09-07*
*Score: 100/130*

---

## The Pitch

**~3 million saunas in Finland. Harvia has moved control stack from Xenio toward Fenix. Compatibility depends on heater generation, controller/power-unit generation, serial/board state, remote-start safety hardware. This is STATEFUL LEGACY SYSTEM → SAFE SUCCESSOR BUNDLE, not MODEL → SKU.**

---

## Why Harvia Sauna is #6

| Factor | Data | Score |
|--------|------|-------|
| **Installed base** | ~3 million saunas | 10/10 |
| **Replacement frequency** | Controllers fail, owners upgrade | 7/10 |
| **Identity difficulty** | "Which controller do I have?" "What Fenix fits?" | 9/10 |
| **Compatibility complexity** | Board revision, serial threshold, safety hardware | 10/10 |
| **Wrong part cost** | Wrong controller = doesn't work; safety issue | 9/10 |
| **Purchase urgency** | Low (sauna is luxury, not emergency) | 5/10 |
| **Supplier stock depth** | Finnish specialists have stock | 7/10 |
| **Supplier operational quality** | Good | 8/10 |
| **Digital merchant gap** | Specialists already explain upgrade | 6/10 |
| **Language fragmentation** | Finnish documentation | 8/10 |
| **Visual identifiability** | Controller photos, board photos, serial numbers | 8/10 |
| **Gross margin** | 25-35% | 8/10 |
| **Shipping suitability** | Small parcel, lightweight | 9/10 |

**Score: 100/130**

---

## The Evidence

### 1. ~3 million saunas in Finland

Order-of-magnitude evidence, not device-specific count.

### 2. Harvia has moved control stack

From Xenio → Fenix. Different upgrade requirements for FC/Fenix, XW/Xenio WiFi, XE systems.

### 3. Compatibility is stateful

Not MODEL → SKU, but:
- heater generation
- controller/power-unit generation
- serial/board state
- remote-start safety hardware
- desired functionality

### 4. Specialists already exist

Huolto Vuorio and PEQU publish explicit compatibility. Merchant gap is MEDIUM.

### 5. Opportunity is cross-generation decision engine

Not generic webshop. Decision layer that takes heater model + existing control unit + power-card/serial generation + remote-start requirement + safety hardware and returns exact supported migration bundle.

---

## What We Build

### "Harvia Fenix Migration Finder"

```
Harvia controller families: C90/C150, Xenio non-WiFi, Xenio WiFi, XE, Fenix
Components: control panels, power cards, door sensors, WiFi modules
For every migration path:
  - compatibility matrix
  - required components
  - safety requirements
  - installation notes
```

---

## Unit Economics

| Metric | Value |
|--------|-------|
| Average order value | EUR 200-400 |
| Gross margin | 25-35% |
| Net per order | EUR 50-140 |
| Break-even orders/month | 25 |

---

## The Flywheel

Same: 50-100 SKUs → feed → discovery → orders → enrich → clone
