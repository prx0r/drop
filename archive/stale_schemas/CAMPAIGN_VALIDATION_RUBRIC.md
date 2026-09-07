# STALE — CAMPAIGN_VALIDATION_RUBRIC.md

*This file is archived. See HCC_V2.md for current campaigns.*

# Campaign Validation Rubric — Binary Gate + Score

*Generated: 2026-09-07*
*Status: STANDARD — All campaigns must pass before entry*

---

## How It Works

1. **Binary Gate** — 10 statements, all must be YES to proceed
2. **Score Rubric** — 20 statements, each +10/0/-10
3. **Total Score** — Sum of rubric scores (max 200)
4. **Threshold** — ≥120 to proceed, ≥160 to ATTACK

---

## BINARY GATE (All must be YES)

| # | Statement | Verdict |
|---|-----------|---------|
| B1 | Installed base exists with evidence | YES/NO |
| B2 | Real lifecycle purchase trigger exists | YES/NO |
| B3 | Nontrivial compatibility/identity problem exists | YES/NO |
| B4 | Real local supply exists | YES/NO |
| B5 | Consumer can self-identify the problem | YES/NO |
| B6 | Product is shippable without technician | YES/NO |
| B7 | No single specialist already owns the full decision path | YES/NO |
| B8 | Supplier exists and will sell to us | YES/NO |
| B9 | Compatibility can be proven, not guessed | YES/NO |
| B10 | Legal/installation responsibility is explicit | YES/NO |

**If any NO → REJECT immediately. No score.**

---

## SCORE RUBRIC (Each +10/0/-10)

### Information Rent (3 statements, max +30)

| # | Statement | YES | NO |
|---|-----------|-----|-----|
| S1 | Identity requires photo + measurements (not just text search) | +10 | 0 |
| S2 | Wrong part has meaningful cost (time, money, safety) | +10 | 0 |
| S3 | Supersession/legacy graph is complex (not simple SKU lookup) | +10 | 0 |

### Installed-Base Economics (2 statements, max +20)

| # | Statement | YES | NO |
|---|-----------|-----|-----|
| S4 | Installed base > 100,000 units in target country | +10 | 0 |
| S5 | Replacement frequency > 1 event per 10 years per unit | +10 | 0 |

### Supplier Arbitrage (3 statements, max +30)

| # | Statement | YES | NO |
|---|-----------|-----|-----|
| S6 | Multiple independent suppliers exist (not single source) | +10 | 0 |
| S7 | Supplier has stock feed or API (not just phone/email) | +10 | 0 |
| S8 | Supplier can direct-ship or blind-ship to consumer | +10 | -10 |

### Distribution Fit (2 statements, max +20)

| # | Statement | YES | NO |
|---|-----------|-----|-----|
| S9 | Product is small parcel, lightweight (< 5kg) | +10 | 0 |
| S10 | Product can be photographed for visual identification | +10 | 0 |

### Economics (3 statements, max +30)

| # | Statement | YES | NO |
|---|-----------|-----|-----|
| S11 | Average order value > €50 / NOK 500 / SEK 500 | +10 | -10 |
| S12 | Gross margin > 25% (with verified supplier net price) | +10 | 0 |
| S13 | Wrong-part return rate < 5% (with evidence) | +10 | -10 |

### Market Position (3 statements, max +30)

| # | Statement | YES | NO |
|---|-----------|-----|-----|
| S14 | Best specialist covers < 70% of compatibility decisions | +10 | -10 |
| S15 | OEM DTC does not directly compete for same SKU | +10 | -10 |
| S16 | Marketplace (Amazon/eBay) does not already dominate | +10 | -10 |

### Language/Native Advantage (2 statements, max +20)

| # | Statement | YES | NO |
|---|-----------|-----|-----|
| S17 | Target country has native language not well-served by English competitors | +10 | 0 |
| S18 | Local terminology/aliases are non-trivial (not just translations) | +10 | 0 |

### Agent/Distribution Leverage (2 statements, max +20)

| # | Statement | YES | NO |
|---|-----------|-----|-----|
| S19 | Product fits Google Merchant Center conversational attributes | +10 | 0 |
| S20 | Product fits Shopify Catalog for AI shopping | +10 | 0 |

---

## SCORING

```
TOTAL = sum(S1..S20)

MAXIMUM = 200
MINIMUM = -80

THRESHOLDS:
  ≥ 160  →  ATTACK (proceed to supplier validation)
  ≥ 120  →  VERIFY (needs more evidence)
  ≥ 80   →  SCAN (interesting but not ready)
  < 80   →  REJECT
```

---

## EXAMPLE: Norway Balcony-Door Hardware

### Binary Gate

| # | Statement | Verdict |
|---|-----------|---------|
| B1 | Installed base exists | YES — 2.76M dwellings |
| B2 | Lifecycle trigger exists | YES — mechanisms fail every 10-20 years |
| B3 | Compatibility problem exists | YES — backset, centres, spindle, handing |
| B4 | Local supply exists | YES — SystemLaaS, Ellefsen Sikkerhet |
| B5 | Consumer can self-identify | YES — photo + 3 measurements |
| B6 | Shippable without technician | YES — small hardware |
| B7 | No single specialist owns decision | YES — fragmented between locksmiths, wholesalers, PDFs |
| B8 | Supplier will sell to us | UNKNOWN — need to verify |
| B9 | Compatibility can be proven | YES — OEM documentation exists |
| B10 | Legal responsibility explicit | YES — no regulated work |

**Result: B8 UNKNOWN → CANNOT PROCEED TO SCORE. Must verify supplier first.**

### Score (if B8 verified)

| # | Statement | Score |
|---|-----------|-------|
| S1 | Photo + measurements required | +10 |
| S2 | Wrong part = door won't lock | +10 |
| S3 | 1970s-2000s legacy graph | +10 |
| S4 | 2.76M dwellings | +10 |
| S5 | 10-20 year replacement | +10 |
| S6 | Multiple locksmiths + wholesalers | +10 |
| S7 | No stock feed yet | 0 |
| S8 | Direct ship unknown | -10 |
| S9 | Small parcel | +10 |
| S10 | Photo identifiable | +10 |
| S11 | NOK 800-1500 AOV | +10 |
| S12 | Margin unknown | 0 |
| S13 | Wrong-part rate unknown | 0 |
| S14 | No single specialist | +10 |
| S15 | ASSA ABLOY is OEM, not retailer | +10 |
| S16 | Marketplaces don't dominate | +10 |
| S17 | Norwegian native language | +10 |
| S18 | Lock terminology non-trivial | +10 |
| S19 | Fits GMC | +10 |
| S20 | Fits Shopify | +10 |

**Total: 150/200 → VERIFY (needs supplier verification to reach ATTACK)**

---

## How to Use This

### 1. Before Creating a Campaign

Run the Binary Gate. If any NO → stop. Don't create the campaign.

### 2. After Creating a Campaign

Run the Score Rubric. If ≥160 → ATTACK. If ≥120 → VERIFY. If <80 → REJECT.

### 3. For Mutations

Track which field changed and how it affected the score:

```json
{
  "mutation_id": "MUT_001",
  "campaign_id": "HCC-NOR-BALCONY-001",
  "field": "supplier.net_prices_verified",
  "old_value": false,
  "new_value": true,
  "score_impact": "+10 (S8 went from -10 to +10)",
  "new_total": 160,
  "new_status": "ATTACK",
  "at": "2026-09-07"
}
```

### 4. For Red Teaming

Use the rubric to audit existing campaigns:

```json
{
  "audit_id": "AUDIT_001",
  "campaign_id": "HCC-FI-ALLAWAY-001",
  "auditor": "agent",
  "date": "2026-09-07",
  "binary_gate": {
    "B1": "YES",
    "B8": "UNKNOWN",
    "B9": "YES"
  },
  "score": 150,
  "status": "VERIFY",
  "findings": [
    "B8 supplier not verified",
    "S12 margin not verified"
  ],
  "recommended_mutations": [
    "Verify Onninen net pricing",
    "Verify direct ship capability"
  ]
}
```

---

## BigQuery Table

```sql
CREATE TABLE drop.campaign_rubric (
  audit_id STRING,
  campaign_id STRING,
  auditor STRING,
  date DATE,
  binary_gate JSON,
  score INTEGER,
  status STRING,
  findings ARRAY<STRING>,
  recommended_mutations ARRAY<STRING>
)
```

---

## The Key Insight

The rubric enforces:

1. **No UNKNOWN gets scored as fact** — binary gate blocks it
2. **Every claim needs evidence** — score requires verification
3. **Mutations are tracked** — progress is measurable
4. **Red teaming is systematic** — not ad-hoc
5. **Rejections are research outcomes** — capture lessons

This is how we avoid hallucination and bullshit.
