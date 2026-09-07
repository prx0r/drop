# High-Certainty Agentic Commerce — The Real Thesis

*Generated: 2026-09-07*
*Status: CORE THESIS — This is what we build*

---

## The Opportunity

> **Find neglected, locally stocked, compatibility-heavy installed-base niches where existing suppliers are operationally competent but digitally terrible. Build the definitive visual + compatibility + technical product graph, syndicate it through Shopify Catalog and Google Merchant Center, and let agents route high-certainty replacement demand to us.**

---

## The Screening Criterion

Not: "Can we make this Shopify listing better?"

But: **"Does purchasing this item involve an information problem that AI can solve but current retailers represent badly?"**

---

## Four Categories

### Bad Niche
- portable blender
- LED strip
- dog bed
- standing desk

Agent adds little. Amazon/product reviews solve it adequately.

### Interesting
- replacement remote
- filter
- charger
- battery
- seal
- belt
- controller

### Excellent
- old HVAC control board
- heat-pump remote generation
- Norwegian cabin pump component
- garage-door control module
- commercial dishwasher component
- robot mower PSU
- obsolete sauna controller
- coffee-machine solenoid

### Exceptional
Where the user begins with **"What is this?"** rather than "Where's the cheapest one?"

---

## The Funnel

```
USER HAS PHYSICAL THING
          ↓
    takes photograph
          ↓
┌─────────┴─────────┐
▼                   ▼
ChatGPT          Gemini/Lens
▼                   ▼
vision             vision
▼                   ▼
intent             Shopping Graph
▼                   ▼
shopping        Merchant Center
retrieval           │
│                   │
├── Shopify Catalog │
├── ACP             │
├── web             │
│                   │
└─────────┬─────────┘
          ▼
     PRODUCT ENTITY
          │
          ▼
    MERCHANT CHOICE
          │
          ▼
        OURS
```

We want to exist in **all retrieval routes**.

---

## The Distribution Stack

```
SHOPIFY
→ Shopify Catalog
→ ChatGPT

GOOGLE MERCHANT CENTER
→ Lens
→ Images
→ Shopping
→ AI Mode
→ Shopping Ads

WEB
→ crawlable PDP
→ JSON-LD
→ search

OPTIONAL LATER
→ direct ACP
→ UCP
→ MCP
```

MCP is **not remotely priority #1**. The feeds are.

---

## Google Merchant Center — 2026 Conversational Attributes

### `related_product`
Supports: `required_part`, `substitute`, `different_brand`, `accessory`
- Designed for AI Mode
- **Spare parts** explicitly mentioned as use case
- Works in all countries

Example:
```
MAIN ASSET
Bosch dishwasher SMS46MI08E

related_product:
    required_part:
        Bosch 00631200 pump

MAIN PART
Bosch 00631200

related_product:
    substitute:
        Bosch 00651956
```

### `product_detail`
- Up to 100 structured technical details per product
- Designed for AI-driven surfaces like AI Mode

Example:
```
Compatibility:
  Manufacturer: Bosch
  Appliance type: Dishwasher
  Compatible model: SMS46MI08E
  Compatible model: SMS50MI08E

Electrical:
  Voltage: 230 V
  Frequency: 50 Hz

Physical:
  Connector count: 3
  Diameter: 82 mm

Identification:
  OEM part number: 00631200
  Previous part number: ...
  Supersedes: ...

Fitment:
  Direct replacement: Yes
  Adapter required: No
```

### `question_and_answer`
- Up to 30 Q&As
- Designed for conversational AI surfaces

Example:
```
Q: Does Bosch 00631200 fit SMS46MI08E?
A: Yes. Bosch 00631200 is compatible with SMS46MI08E...

Q: Does this replace Bosch 00611332?
A: ...

Q: Will I need an adapter?
A: ...

Q: How can I verify my model?
A: Check the model plate inside...
```

### `document_link`
- Manuals, assembly instructions, guides
- Used primarily in conversational AI experiences

### MPN
- Critical for replacement parts
- Google explicitly says: replacement parts, OEM parts, replacements for OEM parts may not have GTINs
- Brand + MPN can identify the product

---

## The Image Strategy

### Set A — Identification Images
Designed to answer: "Is this the same thing?"

```
1. front — clean light background
2. back
3. left
4. right
5. connector close-up
6. mounting points
7. manufacturer label
8. OEM/MPN label
9. dimensional reference
10. old/superseded version comparison
```

### Set B — Explanatory/Human Images
```
installed position
where to find model plate
connector diagram
dimensions
old vs new
package contents
compatible machine
```

### Video
Google introduced `video_link` field in April 2026, serving began June 30.

---

## The Business Model: Supplier Digital Arbitrage

We find suppliers who are:

```
GOOD AT
buying
stock
warehousing
trade relationships
shipping

BAD AT
catalog structure
content
SEO
AI
images
translation
fitment
consumer service
```

We become the missing retail frontend.

No inventory. No manufacturing. No fulfillment.

Just:

```
SUPPLIER STOCK
      ↓
OUR DATA ENGINE
      ↓
AI-NATIVE RETAIL FRONTEND
      ↓
DEMAND
```

---

## The Niche Down Strategy

Don't create: spareparts.fi

Create:
- Mitsubishi heat-pump remotes for Finland
- Nordic heat-pump control electronics
- Norwegian cabin water-system replacement parts
- Husqvarna Automower power supplies / charging systems generations 2010–2025

That's the kind of niche where we can have:
- better photos
- more compatibility knowledge
- better documentation
- more complete aliases
- better translations
- better current offers

...than everyone else.

---

## The Agent-Commerce Standard

Agents have a fundamentally different standard for what constitutes a great merchant.

Humans reward:
- pretty branding
- nice hero
- social proof
- lifestyle imagery
- storytelling

Machines care about:
- IS THIS THE RIGHT ENTITY?
- IS IT COMPATIBLE?
- IS IT IN STOCK?
- CAN IT SHIP THERE?
- WHAT WILL IT COST?
- CAN I TRUST THE CLAIM?
- CAN I COMPLETE THE PURCHASE?

The winning store satisfies **both**.

```
beautiful human storefront
          +
absurdly structured machine backend
```

---

## The Discovery Engine Fields

Instead of only identifying:
- demand
- competition
- price
- margin

Add:
- agent_opportunity_score
- visual_identification_need
- model_identification_need
- compatibility_complexity
- supersession_complexity
- current_feed_quality
- competitor_image_quality
- competitor_attribute_completeness
- competitor_manual_coverage
- competitor_related_product_coverage
- merchant_center_competition
- local_supplier_quality
- supplier_digital_quality
- language_fragmentation
- installed_base
- replacement_frequency
- purchase_urgency
- wrong_part_cost
- return_risk

The **best market**: lots of capable suppliers + terrible product data + recurring exact-fit demand.

Not necessarily: few sellers.

---

## Sources

1. OpenAI — Powering Product Discovery in ChatGPT
2. OpenAI Help Center — Shopping with ChatGPT Search
3. Google Blog — Google Lens shopping product details
4. Google Merchant Center — Conversational attributes
5. Google Merchant Center — Related product
6. Google Merchant Center — Product detail
7. Google Merchant Center — Question and answer
8. Google Merchant Center — Document link
9. Google Merchant Center — Image link
10. Google Merchant Center — Local product data specification
11. Google Merchant Center — Additional image link
12. Google Merchant Center — Product data specification update 2026
13. Google Merchant Center — MPN
14. Google Merchant Center — Unique product identifiers
15. Google Ads — Shopping ads
16. Google Ads — AI Max for Shopping
17. Google Merchant Center — Related product
