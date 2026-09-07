# Shopify + Agentic Shopify Setup Guide

*Generated: 2026-09-07*
*Status: REFERENCE — How to set up Shopify and agentic Shopify*

---

## Quick Answer

**Yes, you need a new Shopify for each niche.** One store = one catalog = one language = one agent discovery path. Multiple stores = multiple focused niches = better agent discovery.

---

## Step 1: Create Shopify Store

1. Go to shopify.com → Start free trial
2. Choose plan: **Basic $39/month** (fine to start)
3. Set store name, currency (NOK for Norway)
4. Connect domain (e.g., `balconydel.no`)
5. Choose theme: **Dawn** (free, fast, mobile-optimized)

**Cost:** $39/month + domain ~$15/year

---

## Step 2: Enable Agentic Storefronts

**Already auto-enabled** for most stores since March 24, 2026.

Check status:
- Go to **Sales Channels > Agentic** in Shopify admin
- See which AI channels are Active/Inactive
- Accept Supplemental Terms if needed

**Channels:**
| Channel | Status | Checkout |
|---------|--------|----------|
| ChatGPT | Live (US) | Referral to store |
| Microsoft Copilot | Live | Embedded via UCP |
| Google AI Mode | Early access | Embedded via UCP |
| Gemini | Rolling out | Embedded via UCP |
| Perplexity | Supported | Referral to store |
| Shop app | Always active | In-app purchase |

---

## Step 3: Set Up Google Merchant Center

1. Go to merchants.google.com
2. Create account (or use existing)
3. Connect to Shopify: **Sales Channels > Google**
4. Install Google & YouTube channel app (free)
5. Verify product feed syncs
6. Enable free listings
7. Run diagnostics and fix any issues

**Key fields to optimize:**
- Title (brand + product type + key trait)
- Description (main features in plain language)
- Brand and GTIN
- Google product category
- Variant attributes (color, size, material)
- Images, price, availability

---

## Step 4: Optimize Product Data

### For AI Agents
- Complete titles with specific attributes
- Detailed descriptions with matchable keywords
- Alt text on all images
- Accurate pricing and inventory
- Structured metafields (compatibility, dimensions, specs)

### For Google Shopping
- Unique ID per product
- Clear title (brand + product + trait + color + size)
- GTIN/UPC where available
- Google product category (numeric ID)
- Custom labels for campaign segmentation
- Accurate shipping weight

### For Our Niche (Compatibility Products)
```json
{
  "product_detail": [
    {"name": "Backset", "value": "20mm"},
    {"name": "Centres", "value": "40mm"},
    {"name": "Strip Length", "value": "800mm"}
  ],
  "question_and_answer": [
    {"question": "Does this fit my door?", "answer": "Yes if 20mm backset"}
  ],
  "related_product": [
    {"type": "accessory", "id": "HANDLE_GU_CLASSIC"}
  ]
}
```

---

## Step 5: Install Knowledge Base App

Free Shopify app that customizes FAQs for AI agents.

- Install from Shopify App Store
- Review pre-populated FAQs
- Add specific answers for your niche
- Shipping, returns, compatibility questions

---

## Step 6: Add Structured Data

Add Product schema (JSON-LD) to product pages:

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "GU Espagnolette 1993-2004",
  "brand": "GU",
  "mpn": "ESP-1993",
  "description": "Replacement mechanism for Uldal balcony doors",
  "offers": {
    "@type": "Offer",
    "price": "1246",
    "priceCurrency": "NOK",
    "availability": "https://schema.org/InStock"
  }
}
```

---

## Step 7: Verify Agent Discovery

Check these files are live:
- `/agents.md`
- `/llms.txt`
- `/llms-full.txt`
- `/.well-known/ucp`

These tell AI agents what you sell and how to interact with your store.

---

## Step 8: Test in AI Platforms

Ask these questions and see if your products appear:

1. ChatGPT: "Find GU balcony door mechanisms in Norway"
2. Perplexity: "Replacement espagnolette for Uldal door 1998"
3. Google AI Mode: "Balcony door lock Norway compatibility"
4. Gemini: "GU lock mechanism 20mm backset"

If your products don't appear, fix the data issues.

---

## Multiple Stores vs One Store

### Recommended: One Store, Multiple Collections

```
Store: hyttekomponenter.no
├── Collection: balcony-door (Norwegian)
├── Collection: vallox (Finnish)
├── Collection: heatpump (Finnish)
├── Collection: hottub (Nordic)
└── Markets: Norway, Finland, Sweden
```

**Why:**
- One admin to manage
- One Merchant Center feed
- One Shopify Catalog
- Each collection = one niche
- Local currency per market
- Unified analytics

---

## Timeline

| Task | Time |
|------|------|
| Create Shopify store | 30 minutes |
| Enable Agentic Storefronts | 5 minutes |
| Set up Merchant Center | 1 hour |
| Add 75 products | 1-2 days |
| Optimize product data | 1-2 days |
| Add structured data | 1 day |
| Install Knowledge Base | 30 minutes |
| Test in AI platforms | 1 hour |
| **Total** | **3-5 days** |

---

## Cost

| Item | Cost |
|------|------|
| Shopify Basic | $39/month |
| Domain | ~$15/year |
| Google Ads | £10/day to start |
| **Total** | **~$350/month** |

---

## Sources

1. Shopify Help Center — Agentic Storefronts
2. Craftshift — Shopify Agentic Storefronts Complete Guide 2026
3. Shopify Blog — How Agentic Commerce Works
4. Google Merchant Center — Product Data Specification
5. Lake House Group — Shopify Agentic Commerce Setup Guide
