# Balcony Door Hardware — Norway

## Campaign: GOLD_CAMPAIGN_A
## Status: ACTIVE
## Last Updated: 2026-09-07

---

## 1. MARKET OVERVIEW

### Installed Base
- 2.76 million Norwegian dwellings
- 1.31 million detached houses
- 483,150 holiday houses
- Hardware from 1970s-2010s still in use

### Lifecycle Trigger
- Mechanisms fail every 10-20 years
- Security upgrades (old locks → new standards)
- Wear parts (handles, strikers, cylinders)

### Buyer Journey
```
Customer: "This mechanism in my 1998 balcony door broke"
    ↓
IDENTIFICATION: photo + 3 measurements
    ↓
COMPATIBILITY: backset, centres, spindle, handing
    ↓
REPLACEMENT: exact part or successor
    ↓
PURCHASE: shippable, small parcel
```

---

## 2. COMPETITOR ANALYSIS

| Name | Type | Stock | Price | Gap |
|------|------|-------|-------|-----|
| SystemLaaS.no | Locksmith | Maybe | Unknown | "maybe we have the weird thing" |
| Ellefsensikkerhet.no | Locksmith | Old GU locks | NOK 1,246 ex VAT | No online resolver |
| GU (manufacturer) | OEM | Discontinued | N/A | No direct consumer sales |
| ASSA ABLOY | OEM | Current only | N/A | No legacy resolution |

### What They Do Well
- Ellefsensikkerhet has old GU stock
- SystemLaaS knows about discontinued hardware

### What They Don't Do
- No online compatibility resolver
- No photo-based identification
- No Norwegian-language agent
- No cross-generation compatibility graph

### Digital Merchant Gap: 10/10
Fragmented between locksmiths, wholesalers, PDFs. No single consumer-facing resolver.

---

## 3. PRODUCT CATALOG (Initial 75 SKUs)

### Lock Families
| Family | Generations | Components |
|--------|-------------|------------|
| GU | 1970-1985, 1985-2000, 2000-2010 | Espagnolette, lock body, handle, cylinder, gearbox, striker |
| ASSA | 1980-2010 | MK1, MK2, MK3 locks |
| TrioVing | 1990-2020 | Multipoint locks |
| Grorud | 1970-1990 | Legacy mechanisms |
| Fix | 1980-2000 | Budget mechanisms |

### Compatibility Dimensions
```
backset: 20mm, 25mm, 30mm, 35mm
centres: 32mm, 40mm, 48mm
strip_length: 600mm, 800mm, 1000mm, 1200mm
spindle: 7mm, 8mm
handing: left, right, reversible
```

### Identification Method
```
1. Photograph whole door
2. Photograph mechanism
3. Photograph stamped markings
4. Measure A / B / C
5. AI resolves hardware family
6. Show verified replacement
```

---

## 4. PRICING

| Product | Public Price | Our Margin | Notes |
|---------|--------------|------------|-------|
| GU espagnolette (old) | NOK 1,246 | 30% | Discontinued |
| ASSA lock cylinder | NOK 800 | 25% | Current |
| Handle set | NOK 500-1,200 | 30% | Generation-dependent |
| Gearbox | NOK 800-1,500 | 25% | Complex identification |

### Unit Economics
- Average order value: NOK 800-1,500
- Gross margin: 25-30%
- Shipping: NOK 50-100 (small parcel)
- Net per order: NOK 200-450
- Break-even: 15 orders/month

---

## 5. SUPPLIER STRATEGY

### Primary Suppliers
| Supplier | Type | Contact | Terms |
|----------|------|---------|-------|
| SystemLaaS.no | Locksmith | systemlaas.no | Unknown |
| Ellefsensikkerhet.no | Locksmith | ellefsensikkerhet.no | Unknown |
| Norwegian wholesalers | Trade | TBD | Unknown |

### Supplier Requirements
- Stock of legacy GU/ASSA/TrioVing parts
- Ability to ship to consumers
- Norwegian language support
- Willingness to work with us

### Action Items
1. Contact SystemLaaS.no — verify stock, pricing, dealer terms
2. Contact Ellefsensikkerhet.no — verify stock, pricing
3. Identify 2-3 Norwegian hardware wholesalers
4. Request net pricing and direct-ship capability

---

## 6. AD STRATEGY

### Google Search
```
Budget: NOK 100/day
Keywords:
  - "[brand] [model] deler"
  - "[brand] [model] erstatning"
  - "balcony door lock replacement"
  - "espagnolette Norway"
Match type: exact/phrase
Ad group: compatibility_replacement
Negative: service, reparasjon, installasjon
```

### Google Shopping
```
Budget: NOK 50/day
Campaign: standard_shopping
Products: only verified SKUs
```

### Free Listings
```
Budget: NOK 0
Merchant Center: enabled
```

### Testing Plan
```
Week 1: Free listings only, measure impressions
Week 2: Add exact/phrase Search, measure CTR
Week 3: Add Shopping, measure CVR
Week 4: Optimize based on search terms
```

---

## 7. MERCHANT CENTER FEED

### Products (75 SKUs)
```json
{
  "id": "GU_ESPAGNOLETTE_1993",
  "title": "GU Espagnolette 1993-2004 Balcony Door Mechanism",
  "brand": "GU",
  "mpn": "ESP-1993",
  "description": "Replacement mechanism for Uldal balcony doors 1993-2004",
  "product_detail": [
    {"name": "Backset", "value": "20mm"},
    {"name": "Centres", "value": "40mm"},
    {"name": "Strip Length", "value": "800mm"},
    {"name": "Spindle", "value": "7mm"},
    {"name": "Handing", "value": "Reversible"}
  ],
  "question_and_answer": [
    {"question": "Does this fit my 1998 Uldal balcony door?", "answer": "Yes, if your door has 20mm backset and 40mm centres"},
    {"question": "What measurements do I need?", "answer": "Backset, centres, strip length, spindle diameter"},
    {"question": "Can I install this myself?", "answer": "Yes, basic DIY skills required"}
  ],
  "related_product": [
    {"type": "accessory", "id": "HANDLE_GU_CLASSIC"},
    {"type": "accessory", "id": "CYLINDER_GU_30MM"}
  ],
  "images": [
    "https://example.com/gu_espagnolette_front.jpg",
    "https://example.com/gu_espagnolette_back.jpg",
    "https://example.com/gu_espagnolette_connector.jpg"
  ]
}
```

---

## 8. LANDING PAGE STRUCTURE

### Hero Section
```
[CRISP PRODUCT IMAGE]

GU Espagnolette 1993-2004
Balcony Door Mechanism

✓ Fits Uldal doors 1993-2004
✓ 20mm backset, 40mm centres
✓ Does NOT fit: 2005+ models
✓ In stock, ships from Norway
✓ NOK 1,246

[BUY NOW]
```

### Identification Section
```
HOW TO IDENTIFY YOUR MECHANISM

1. Measure backset (A)
2. Measure centres (B)
3. Measure strip length (C)
4. Check spindle diameter

[PHOTO EXAMPLES]
```

### Compatibility Table
```
| Door Model | Fits? | Notes |
|------------|-------|-------|
| Uldal 1993-2004 | ✓ Yes | Direct fit |
| Uldal 2005-2010 | ✗ No | Different mechanism |
| NorDan 1990-2000 | ✓ Yes | With adapter |
```

### FAQ
```
Q: How do I know which mechanism I have?
A: Measure backset, centres, and strip length. See photos above.

Q: Can I install this myself?
A: Yes, basic DIY skills required. 30-minute job.

Q: What if it doesn't fit?
A: Return within 30 days for full refund.
```

---

## 9. SUCCESS METRICS

| Metric | Target | Timeline |
|--------|--------|----------|
| SKUs live | 75 | Week 1 |
| Merchant Center feed | Enabled | Week 1 |
| Free listing impressions | 100/day | Week 2 |
| Search ads CTR | >2% | Week 3 |
| First paid order | 1 | Week 4 |
| Orders/month | 15 | Month 3 |
| Revenue/month | NOK 15,000 | Month 3 |

---

## 10. RISKS

| Risk | Mitigation |
|------|------------|
| Supplier won't sell to us | Contact 3+ suppliers, find one who will |
| Wrong part returns | Build compatibility graph, verify before shipping |
| Low search volume | Expand to window hardware, garage doors |
| Competitor improves | Monitor with GitGoblin, adapt |

---

## 11. NEXT STEPS

1. Contact SystemLaaS.no — verify stock and pricing
2. Contact Ellefsensikkerhet.no — verify stock and pricing
3. Identify 50 common legacy mechanisms
4. Build compatibility graph
5. Create Merchant Center feed
6. Set up Shopify store
7. Launch Google Ads test
