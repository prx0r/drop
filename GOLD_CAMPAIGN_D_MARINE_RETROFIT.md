# Gold Campaign D — Nordic Marine Electronics Retrofit Adapters

*Generated: 2026-09-07*
*Score: 88/100*
*Status: ATTACK*

---

## The Pitch

**Millions of recreational boats. Marine electronics generations change connectors while expensive installed transducers remain useful. Garmin documents 6→4→8→12-pin transition. Adapter €75. NMEA 2000 adapter NOK 2,569.**

---

## Why This Is #4

| Factor | Data | Score |
|--------|------|-------|
| **Installed base** | Millions of Nordic recreational boats | 9/10 |
| **Replacement frequency** | Electronics upgrade cycles | 7/10 |
| **Identity difficulty** | "What cable do I need for this transducer?" | 9/10 |
| **Compatibility complexity** | Cross-brand, multi-generation, protocol changes | 10/10 |
| **Wrong part cost** | Wrong adapter = doesn't connect | 9/10 |
| **Purchase urgency** | Medium (upgrade, not emergency) | 7/10 |
| **Self-service resolution** | Consumer can photograph device/connector | 9/10 |
| **Pre-SKU uncertainty** | High — consumer doesn't know protocol | 9/10 |
| **Digital merchant gap** | Specialist marine retailers exist but fragmented | 7/10 |
| **Language fragmentation** | Norwegian/Swedish/Finnish | 8/10 |
| **Visual identifiability** | Photos of connector, device, label | 9/10 |
| **Gross margin** | 20-30% on adapters | 7/10 |
| **Shipping suitability** | Small parcel, lightweight | 9/10 |
| **Supplier accessibility** | Marine electronics distributors | 7/10 |

**Score: 119/140**

---

## The Evidence

### 1. Garmin documents the transition

6-pin → 4-pin → 8-pin → 12-pin. Old transducers can sometimes be reused with adapters.

### 2. Real pricing

- 6→8-pin adapter: ~€75
- Analogue→NMEA 2000 adapter: NOK 2,569

### 3. Cross-brand value

Garmin, Raymarine, Simrad all have different connectors. Knowledge graph valuable beyond any one merchant.

### 4. Query is fantastic

"I have this old Garmin transducer. I bought this new chartplotter. What cable do I need?"

---

## What We Build

### "Marine Electronics Retrofit Resolver"

```
Old device → port/protocol/generation → new device → adapter chain → correct SKU
Cross-brand: Garmin, Raymarine, Simrad, etc.
For every adapter:
  - compatible devices
  - installation notes
  - protocol requirements
```

---

## Unit Economics

| Metric | Value |
|--------|-------|
| Average order value | NOK 500-2500 |
| Gross margin | 20-30% |
| Net per order | NOK 100-750 |
| Break-even orders/month | 20 |

---

## Supplier Strategy

- Marine electronics distributors
- Garmin/Raymarine dealer networks
- Specialist marine retailers

---

## 30-Day Experiment

1. Enumerate 100 common adapter combinations
2. Map old device → new device → adapter
3. Find supplier with stock
4. Test photo identification flow
5. Launch as migration resolver + affiliate

**Success:** 50 adapter SKUs mapped, 1 supplier, first referral.

**Falsifier:** Specialist marine retailers already resolve ≥90% of queries.
