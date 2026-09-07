# Gold Campaign A — Norway Balcony-Door Mechanisms

*Generated: 2026-09-07*
*Score: 94/100*
*Status: ATTACK FIRST*

---

## The Pitch

**2.76 million Norwegian dwellings. Old balcony-door locks and mechanisms from GU, ASSA, TrioVing, Grorud, Fix. Hardware from 1970s–2000s. Consumer-visible failure. Photo + 3 measurements = identification. Small shippable product. £50–£150+ replacement value.**

---

## Why This Is #1

| Factor | Data | Score |
|--------|------|-------|
| **Installed base** | 2.76 million dwellings, 1.31 million detached houses | 10/10 |
| **Replacement frequency** | Mechanisms fail every 10-20 years | 9/10 |
| **Identity difficulty** | "What mechanism is in my 1998 balcony door?" | 10/10 |
| **Compatibility complexity** | Backset, centres, strip length, spindle, handing | 10/10 |
| **Wrong part cost** | Wrong mechanism = doesn't fit door | 9/10 |
| **Purchase urgency** | High (security issue, door won't lock) | 9/10 |
| **Self-service resolution** | Consumer can photograph + measure | 10/10 |
| **Pre-SKU uncertainty** | Very high — consumer doesn't know SKU | 10/10 |
| **Digital merchant gap** | Fragmented between locksmiths, wholesalers, PDFs | 10/10 |
| **Language fragmentation** | Norwegian documentation | 9/10 |
| **Visual identifiability** | Photos + 3 measurements | 10/10 |
| **Gross margin** | 30-40% on hardware | 9/10 |
| **Shipping suitability** | Small parcel, lightweight | 10/10 |
| **Supplier accessibility** | Locksmiths advertise "maybe we have the weird thing" | 9/10 |

**Score: 136/140**

---

## The Evidence

### 1. 2.76 million Norwegian dwellings

SSB data: 2.76 million dwellings including 1.31 million detached houses.

### 2. Locksmiths advertise the pain

SystemLaaS: "We stock old/discontinued/unusual locks… maybe we have exactly what you need."

### 3. Real pricing

- Old GU lock for Uldal balcony doors (1993–2004): NOK 1,246 ex VAT
- Replacement reproduction door handle: NOK 1,125
- 300k-360k pairs per year historically

### 4. Current commerce is fragmented

Between window manufacturers, locksmiths, hardware wholesalers, legacy-hardware shops, PDFs/order forms.

### 5. ASSA ABLOY is OEM information surface

Not a consumer resolver. Site is predominantly information, not transaction.

---

## What We Build

### "Norwegian Door Hardware Resolver"

```
Door manufacturers: Uldal, NorDan, Gilje, Strømmen
Lock families: GU, ASSA, FIX, Grorud, TrioVing
Components: espagnolette mechanisms, handles, gearboxes, locking strips
For every mechanism:
  - front image
  - measurement guide (A/B/C)
  - compatible replacements
  - installation notes
```

---

## The Interface

```
1. Photograph whole door/window
2. Photograph mechanism
3. Photograph stamped markings
4. Measure A / B / C
5. AI resolves hardware family
6. Show verified replacement
```

---

## Unit Economics

| Metric | Value |
|--------|-------|
| Average order value | NOK 800-1500 |
| Gross margin | 30-40% |
| Net per order | NOK 240-600 |
| Break-even orders/month | 15 |

---

## Supplier Strategy

- Locksmiths with legacy inventory
- Hardware wholesalers
- ASSA ABLOY dealer network
- Direct: SystemLaaS, Ellefsen Sikkerhet

---

## 30-Day Experiment

1. Enumerate 100 common legacy mechanisms
2. Find every current seller + buy price
3. Identify wholesalers who can supply us
4. Test native Norwegian query/photo flow
5. Build 50 SKUs with full compatibility graph
6. Launch Shopify + Merchant Center

**Success:** ≥50 SKUs live, 1 supplier agreement, first paid order.

**Falsifier:** Norwegian locksmiths already answer ≥90% of test questions.
