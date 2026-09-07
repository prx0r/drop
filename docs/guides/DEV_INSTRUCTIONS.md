# Dev Instructions — Build the Ultimate Site to Rank High

*From: dropintel agent*
*Date: 2026-09-07*

---

## The Stack

```
COMPATIBILITY GRAPH (your data)
    ↓
FEED GENERATION (structured data)
    ↓
GOOGLE MERCHANT CENTER (distribution)
    ↓
WEB STORE (human interface)
```

---

## Repos to Use

### Feed Generation
- `kiwoongeom/gmc-mcp` (14 stars) — MCP server for Merchant Center, 126 tools
- `lukesnowden/google-shopping-feed` (68 stars) — PHP feed generation

### Web Store
- `vercel/next.js` (142K stars) — React framework, fast, SEO-friendly

### Schema/Structured Data
- `schemaorg/schemaorg` (6K stars) — JSON-LD definitions

### Ads
- `itallstartedwithaidea/advertising-hub` (39 stars) — 14 platforms, 25+ agents

---

## Build Order

### Week 1: Feed Layer
1. Set up GMC account (free)
2. Install feed tool (`pip install gmc-mcp`)
3. Create product feed with conversational attributes
4. Submit to Merchant Center

### Week 2: Web Store
1. Create Next.js store (`npx create-next-app@latest norwegian-parts`)
2. Add product pages with JSON-LD
3. Add compatibility pages
4. Deploy to Vercel (free)

### Week 3: Content
1. Create "How to identify your model" pages
2. Create compatibility matrices
3. Add Q&A for each product
4. Add manuals/documentation

### Week 4: Test & Iterate
1. Test with Google AI Mode
2. Test with ChatGPT
3. Measure AI impression share
4. Optimize based on results

---

## Feed Template

```yaml
# Standard fields
id: "00631200"
title: "Bosch 00631200 Circulation Pump"
description: "OEM replacement for Bosch SMS46MI08E dishwasher..."
brand: "Bosch"
mpn: "00631200"
price: "1129.00"
availability: "in_stock"

# Conversational attributes (THE KEY)
question_and_answer:
  "Does this fit SMS46MI08E?": "Yes, direct replacement"
  "Does this replace 00611332?": "Yes, 00631200 supersedes 00611332"
  "Will I need an adapter?": "No, direct fit"

product_detail:
  - section: "Compatibility"
    attribute: "Compatible Models"
    value: "SMS46MI08E, SMS50MI08E"
  - section: "Electrical"
    attribute: "Voltage"
    value: "230V"
  - section: "Identification"
    attribute: "OEM Part Number"
    value: "00631200"

related_product:
  - type: "substitute"
    id: "00651956"
  - type: "accessory"
    id: "FILTER-001"
```

---

## PDP Template

```
/grundfos-xyz-erstatning

[CRISP PRODUCT IMAGE]

Bosch 00631200 Circulation Pump

✓ Replaces: ABC-123 / ABC-124
✓ Fits systems: SMS46MI08E, SMS50MI08E
✓ Does NOT fit: SMS53MI08E (different connector)
✓ 230V / 50Hz
✓ In stock
✓ Ships from Norway
✓ Bergen: 1–2 days

[BUY]

---

Identification
OEM: 00631200
MPN: 00631200
EAN: 4005165123456

Fits
| Model | Fits? | Notes |
|-------|-------|-------|
| SMS46MI08E | Yes | Direct |
| SMS50MI08E | Yes | Direct |
| SMS53MI08E | No | Different connector |

How to Identify Yours
[images of label, connector, model plate]

Replacement Chain
2008 model → 2014 model → CURRENT SKU

FAQ
- Does this replace 00611332? Yes
- Do I need an adapter? No
- How do I verify my model? Check model plate inside door

Manual
[PDF link]
```

---

## JSON-LD Template

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Bosch 00631200 Circulation Pump",
  "sku": "00631200",
  "brand": {"@type": "Brand", "name": "Bosch"},
  "description": "OEM replacement for Bosch SMS46MI08E dishwasher...",
  "offers": {
    "@type": "Offer",
    "price": "1129.00",
    "priceCurrency": "NOK",
    "availability": "https://schema.org/InStock"
  }
}
```

---

## Cost

| Item | Cost |
|------|------|
| GMC | Free |
| Feed tool | Free |
| Next.js | Free |
| Vercel | Free |
| **Total** | **$0/mo** |

---

*Start building.*
