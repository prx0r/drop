# Build Guide — Custom Stack (No Shopify)

*Generated: 2026-09-07*
*Status: REFERENCE — How to build without Shopify*

---

## The Stack

| Layer | What You Need | Cost |
|-------|---------------|------|
| Google Merchant Center | Product feed with conversational attributes | Free |
| Feed Management | Tool to generate/optimize feed | Free-$50/mo |
| Web Store | Simple PDP for humans | $0-30/mo |
| Payments | Stripe | 2.9% + $0.30 |
| Hosting | Cloudflare Pages | Free |
| Domain | ~$15/year | ~$15/year |

**Total: ~$15/year + Stripe fees**

---

## The Alternatives

| Platform | Pros | Cons |
|----------|------|------|
| Shopify | Auto-enables Catalog, UCP built-in | Fees, dependency |
| WooCommerce | Free, full control, good feed plugins | More setup |
| Laravel + Feedify | Free, developer control, open source | Need dev skills |
| Direct GMC feed | No platform needed | Manual feed management |

---

## The Best Path

**Don't use Shopify. Use Google Merchant Center directly.**

1. Create Merchant Center account (free)
2. Use Feedify (Laravel) or EasyFeedManager (WooCommerce)
3. Fill conversational attributes (related_product, product_detail, Q&A)
4. Submit feed to Merchant Center
5. Products appear in AI Mode, Lens, Shopping

**Cost: $0-50/mo for feed tool. No Shopify fees.**

---

## Why This Is Better

| Shopify | Direct GMC |
|---------|------------|
| 2.9% + $0.30 per transaction | No transaction fees |
| Dependent on Shopify | You own the feed |
| Auto-enables Catalog | Manual but full control |
| Limited customization | Full attribute control |

---

## The Feed Tools

| Tool | Price | Best For |
|------|-------|----------|
| Feedify (Laravel) | Free | Developers |
| EasyFeedManager (WooCommerce) | Free-$50/mo | WordPress users |
| Feedmaster | Paid | Multi-channel |
| Direct GMC feed | Free | Full control |

---

## The 10 Highest Alpha Insights

### 1. Google literally built the fields you need
`related_product` supports `required_part`, `substitute`, `accessory`. `product_detail` supports 100 technical specs. `question_and_answer` supports 30 Q&As. Google explicitly says these are for AI Mode. You fill them. Agents pick you.

### 2. The feed is the product page now
Google treats Merchant Center as a "deep product database." The old game was "optimize the PDP." The new game is "optimize the feed." Your feed IS your ranking.

### 3. MPN is the killer for replacement parts
Google specifically says brand + MPN identifies products without GTINs. Replacement parts often don't have GTINs. MPN is your edge. "Bosch 00631200" beats "pump-123.jpg" every time.

### 4. Related_product is the compatibility graph (partially)
Google's `related_product` supports `required_part` and `substitute`. But it only links products YOU sell. The dishwasher→pump edge lives in YOUR graph, your Q&A, your PDP. That's the moat.

### 5. The engineers who matter are practitioners, not builders
@AndrewLolk tests AI Max Shopping. @mikeryanretail tests AI Mode ads. @FeedArmy identified the 8 attributes. They're on Twitter, not GitHub. They have the empirical data.

### 6. The star graph finds hidden infrastructure
Multiple Shopify/Google engineers star the same repos: boundaryml/baml (agent programming), stanfordnlp/dspy (LLM ranking), universal-commerce-protocol/ucp (commerce protocol). That's where the infrastructure is converging.

### 7. Probook proved the Supplier OS works
2,542 jobs in month one, zero human intervention. 58,000 daily interactions. The free AI front desk → data flywheel is real. UK/European market is empty.

### 8. Allaway Finland is the cleanest first campaign
250,000 homes, 30 years of legacy, terrible consumer UX, small parcel goods, 30-40% margin. Build 50-100 SKUs insanely well. Not 5,000 mediocre ones.

### 9. The non-English angle is real but nuanced
Norwegian is fully supported for Merchant Center. AI Max title customization is English-only (temporarily). Build the feed manually in Norwegian. That's the moat while competitors wait for AI to do it.

### 10. The moat is certainty, not discovery
Agents can find products. They can't verify compatibility. They can't confirm stock. They can't guarantee fitment. Your graph provides certainty. That's what agents pay for.

---

## Implementation Steps

### Step 1: Create Google Merchant Center Account
1. Go to merchants.google.com
2. Create account
3. Verify website
4. Add business information

### Step 2: Build Product Feed
Use Feedify (Laravel) or direct CSV/JSONL:

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

### Step 3: Submit to Merchant Center
1. Upload feed via API or CSV
2. Fix any disapprovals
3. Enable free listings

### Step 4: Build Simple PDP
Next.js or simple HTML:
- Product image
- Compatibility table
- Q&A
- Buy button (Stripe)

### Step 5: Apply for ChatGPT
1. Go to chatgpt.com/merchants
2. Apply for merchant access
3. Submit ACP product feed

### Step 6: Test
Ask ChatGPT, Perplexity, Google AI Mode:
- "GU espagnolette 1993-2004 replacement"
- "Balcony door mechanism 20mm backset"
- "Does this fit Uldal door 1998?"

---

## The Feed is the Product Page

Google treats Merchant Center as a "deep product database." Your feed IS your ranking.

**Key fields:**
- `product_detail` — 100 technical specs
- `question_and_answer` — 30 Q&As
- `related_product` — compatibility graph
- `mpn` — the killer for replacement parts
- `brand` + `mpn` — identifies without GTIN

---

## Bottom Line

Build the feed. Submit to Merchant Center. Skip Shopify entirely.

**Cost: $0-50/mo for feed tool. No Shopify fees.**
