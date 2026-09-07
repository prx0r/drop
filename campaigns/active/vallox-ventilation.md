# Vallox Ventilation Spare Parts — Finland

## Campaign: GOLD_CAMPAIGN_B
## Status: ACTIVE
## Last Updated: 2026-09-07

---

## 1. MARKET OVERVIEW

### Installed Base
- Large Finnish ventilation installed base
- Vallox systems installed in homes since 1970s
- Multiple generations of controllers, fans, sensors

### Lifecycle Trigger
- Fans fail every 10-15 years
- Controllers become obsolete
- Sensors drift/fail
- Bypass actuators seize

### Buyer Journey
```
Customer: "My Vallox fan stopped working"
    ↓
IDENTIFICATION: type plate + model number
    ↓
COMPATIBILITY: unit generation, handedness, controller type
    ↓
REPLACEMENT: exact fan/board/sensor
    ↓
PURCHASE: shippable, small parcel
```

---

## 2. COMPETITOR ANALYSIS

| Name | Type | Stock | Price | Gap |
|------|------|-------|-------|-----|
| Vallox | OEM | Distribution only | N/A | "cannot buy direct" |
| Finnish distributors | Trade | Large ranges | Trade pricing | Trade-oriented |
| Ventus-Finland | Specialist | Vallox parts | Retail pricing | Limited consumer UX |

### What They Do Well
- Finnish distributors have large Vallox ranges
- Vallox maintains old equipment documentation

### What They Don't Do
- No consumer direct sales
- No photo identification
- No compatibility resolver
- Trade-oriented, bad consumer UX

### Digital Merchant Gap: 10/10
Vallox explicitly tells consumers they cannot buy spare parts directly. Distribution has the stock.

---

## 3. PRODUCT CATALOG (Initial 75 SKUs)

### Component Families
| Family | Components | Price Range |
|--------|------------|-------------|
| Supply fans | 60/100/150 m3/h | EUR 100-300 |
| Extract fans | 60/100/150 m3/h | EUR 100-300 |
| Motherboards | Generation-specific | EUR 200-500 |
| NTC sensors | Resistance-based | EUR 20-50 |
| CO2/humidity sensors | Multi-type | EUR 50-150 |
| Control panels | Generation-specific | EUR 100-300 |
| Bypass actuators | 24V/230V | EUR 50-150 |
| Heating elements | kW-rated | EUR 50-200 |

### Compatibility Dimensions
```
unit_generation: 90/95/99/110
handedness: left/right
controller_type: manual/humidistat/CO2/timer
voltage: 24V/230V
airflow: supply/extract
duct_diameter: 100/125/150/160mm
```

---

## 4. PRICING

| Product | Public Price | Our Margin | Notes |
|---------|--------------|------------|-------|
| Supply fan 100 | EUR 150-250 | 25% | Generation-dependent |
| Motherboard | EUR 200-500 | 30% | High-value, complex ID |
| NTC sensor | EUR 20-50 | 40% | Simple, high-volume |
| Control panel | EUR 100-300 | 25% | Generation-specific |

### Unit Economics
- Average order value: EUR 100-300
- Gross margin: 25-35%
- Shipping: EUR 10-20
- Net per order: EUR 25-100
- Break-even: 20 orders/month

---

## 5. SUPPLIER STRATEGY

### Primary Suppliers
| Supplier | Type | Contact | Terms |
|----------|------|---------|-------|
| Vallox | OEM | vallox.com | Distribution only |
| Finnish distributors | Trade | TBD | Unknown |
| Ventus-Finland | Specialist | ventus-finland.fi | Unknown |

### Action Items
1. Contact Vallox — verify distribution channels
2. Contact Finnish distributors — verify stock and pricing
3. Identify 3-5 Vallox specialists
4. Request net pricing and direct-ship capability

---

## 6. AD STRATEGY

### Google Search
```
Budget: EUR 50/day
Keywords:
  - "Vallox ventilationsfläkt delar"
  - "Vallox motherboard replacement"
  - "Vallox sensor Finland"
Match type: exact/phrase
Negative: installation, service
```

### Google Shopping
```
Budget: EUR 25/day
Campaign: standard_shopping
Products: only verified SKUs
```

### Free Listings
```
Budget: EUR 0
Merchant Center: enabled
```

---

## 7. MERCHANT CENTER FEED

### Products (75 SKUs)
```json
{
  "id": "VALLOX_FAN_100Supply",
  "title": "Vallox Supply Fan 100 m3/h",
  "brand": "Vallox",
  "mpn": "FAN-100-S",
  "description": "Replacement supply fan for Vallox ventilation units",
  "product_detail": [
    {"name": "Airflow", "value": "100 m3/h"},
    {"name": "Duct Diameter", "value": "125mm"},
    {"name": "Voltage", "value": "230V"},
    {"name": "Generation", "value": "90/95/99/110"}
  ],
  "question_and_answer": [
    {"question": "Which fan fits my Vallox unit?", "answer": "Check unit generation and duct diameter"},
    {"question": "How do I find my Vallox model?", "answer": "Look for type plate on unit housing"}
  ],
  "related_product": [
    {"type": "accessory", "id": "VALLOX_SENSOR_NTC"},
    {"type": "accessory", "id": "VALLOX_BYPASS_ACTUATOR"}
  ]
}
```

---

## 8. LANDING PAGE STRUCTURE

### Hero Section
```
[CRISP PRODUCT IMAGE]

Vallox Supply Fan 100 m3/h
Ventilation Replacement Part

✓ Fits Vallox 90/95/99/110 units
✓ 125mm duct diameter
✓ 230V
✓ In stock, ships from Finland
✓ EUR 189

[BUY NOW]
```

### Identification Section
```
HOW TO IDENTIFY YOUR VALLOX UNIT

1. Find type plate on unit housing
2. Note model number
3. Check duct diameter
4. Verify voltage

[PHOTO EXAMPLES]
```

---

## 9. SUCCESS METRICS

| Metric | Target | Timeline |
|--------|--------|----------|
| SKUs live | 75 | Week 1 |
| First paid order | 1 | Week 4 |
| Orders/month | 20 | Month 3 |
| Revenue/month | EUR 3,000 | Month 3 |

---

## 10. NEXT STEPS

1. Contact Vallox — verify distribution channels
2. Contact Finnish distributors — verify stock
3. Identify 50 common Vallox components
4. Build compatibility graph
5. Create Merchant Center feed
6. Set up Shopify store
7. Launch Google Ads test
