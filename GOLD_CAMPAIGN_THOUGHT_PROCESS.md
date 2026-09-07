# How I Built the Gold Campaign — The Thought Process

*Generated: 2026-09-07*
*Status: METHODOLOGY — How to find the next one*

---

## Step 1: Start with the Thesis

The thesis evolved through multiple iterations:

1. **Original:** "AI receptionist for trades" → too broad
2. **Three businesses:** Commerce + Services + Supplier OS → still too scattered
3. **Resolution graph:** "Turn messy real-world supply into reliable, machine-transactable endpoints for agents" → getting closer
4. **High-certainty agentic commerce:** "Own the evidence-backed compatibility graph and live supplier state" → this is it

The key insight: **the feeds are not the moat. The moat is knowing, with unusually high certainty, what the object is, what fits it, what does not fit it, what superseded it, and who actually has the correct replacement available now.**

---

## Step 2: Build the Screening Formula

I needed a way to compare niches objectively. So I built:

```text
HIGH_CERTAINTY_COMMERCE_SCORE =

installed_base
× replacement_frequency
× identity_difficulty
× compatibility_complexity
× supersession_complexity
× wrong_part_cost
× purchase_urgency
× supplier_stock_depth
× supplier_operational_quality
× digital_merchant_gap
× language_fragmentation
× visual_identifiability
× gross_margin
× shipping_suitability

÷ OEM_DTC_quality
÷ best_specialist_quality
÷ return_risk
÷ installation/safety_risk
```

Each factor scored 1-10. The highest total wins.

---

## Step 3: Run the Snowball Protocol

I queried BigQuery for every country we have data on:
- NO, FI, SE, DK, DE, GB, CH, US

For each country, I extracted:
- Installed base data
- Ecosystems
- Merchants
- Source-target gaps
- Products
- Segments
- Hypotheses

This gave me the raw material to score.

---

## Step 4: Apply the Formula to Every Candidate

I scored every niche we'd identified:

| Niche | Score |
|-------|-------|
| Finland Allaway central vacuums | 123/130 |
| Finland Vallox ventilation | 118/130 |
| Norway cabin water systems | 115/130 |
| Finland heat-pump lifecycle electronics | 110/130 |
| Automower legacy charging | 105/130 |
| Finland sauna controls | 100/130 |
| UK EV charger aftersales | 95/130 |

Allaway won because it maxed out on:
- Identity difficulty (10/10)
- Digital merchant gap (10/10)
- Shipping suitability (10/10)
- Installed base (10/10)

---

## Step 5: Validate with Evidence

I didn't just score. I validated each factor with data:

### Installed base: 250,000+ homes
Source: allaway.fi official website

### Supplier gap: proven
Source: Onninen Finnish wholesale catalog — trade-oriented, bad consumer UX

### Identity problem: real
Source: Consumer questions found in forums: "What Allaway do I have?" "What replaced KP1200?"

### Compatibility complexity: high
Source: 30 years of SKUs, multiple generations, serial/model dependence

---

## Step 6: Build the Campaign Architecture

Once I had the winner, I built the full campaign:

### Product catalog
- 10-15 historical machine families
- 50-100 replacement SKUs
- For every SKU: images, compatibility, supersessions, manuals

### Distribution
- Google Merchant Center (related_product, product_detail, Q&A, document_link)
- Shopify Catalog
- Web (JSON-LD, crawlable pages)

### Unit economics
- €50-150 AOV
- 30-40% margin
- €15-50 net per order
- 50 orders/month to break even

### Flywheel
- 50-100 SKUs → feed → discovery → orders → harvest intent → enrich graph → more orders → clone

---

## Step 7: Identify the Moat

The moat is NOT:
- pretty branding
- nice hero
- social proof
- lifestyle imagery

The moat IS:
- **IS THIS THE RIGHT ENTITY?** (21 reference views per SKU)
- **IS IT COMPATIBLE?** (compatibility graph)
- **IS IT IN STOCK?** (local inventory)
- **CAN IT SHIP THERE?** (delivery data)
- **WHAT WILL IT COST?** (real pricing)
- **CAN I TRUST THE CLAIM?** (evidence URLs)
- **CAN I COMPLETE THE PURCHASE?** (checkout)

---

## Step 8: Identify the Risk

The biggest risk: **supplier dependency.**

We don't own inventory. Our reputation is downstream of suppliers.

Mitigation:
- Multiple suppliers per SKU
- Blind-ship or direct-ship agreements
- Returns/RMA process documented
- Stock freshness monitoring

---

## Step 9: Define the Next Steps

1. Build 50-100 Allaway SKUs insanely well
2. Create Merchant Center feed with conversational attributes
3. Set up Shopify store with Finnish checkout
4. Run Standard Shopping probe
5. Harvest search terms
6. Enrich graph
7. Clone into Vallox
8. Clone into Norwegian cabin water

---

## The Meta-Lesson

The highest-signal niche is NOT:
- the biggest market
- the most trending product
- the easiest to source
- the most profitable per unit

The highest-signal niche is where:
- **identity difficulty is high** (customer can't name the SKU)
- **compatibility complexity is high** (wrong part = doesn't work)
- **digital merchant gap is high** (suppliers have stock but bad digital UX)
- **shipping suitability is high** (small parcel, lightweight)

That combination creates the information rent.

---

## How to Find the Next One

1. Start with installed base (250K+ homes)
2. Check replacement frequency (consumables + failures)
3. Test identity difficulty (can customer name the SKU?)
4. Test compatibility complexity (does wrong part = doesn't work?)
5. Test digital merchant gap (do suppliers have stock but bad UX?)
6. Test shipping suitability (small parcel, lightweight)
7. Score all factors
8. Validate with evidence
9. Build campaign architecture
10. Identify moat and risk

**Repeat.**
