# EV Installation Service Campaign — The Real Plan

*From the user's analysis. This is what we're actually building.*

---

## The Business Model

**Managed local-service exchange:**

> buyer with high-intent local problem → structured intake → verified local supply → normalized quote → booking/payment → evidence of completion → dispute/aftercare layer → platform fee

**Lead generation is only V0.** The real asset is learning how to turn an unstructured job into a standardized transaction.

---

## The Value Progression

| Stage | What We Sell | Price | Complexity |
|-------|--------------|-------|------------|
| V0 | Qualified lead | £20-50 | Low |
| V1 | Booked installation | £75-150 | Medium |
| V2 | Managed transaction | £80-120 (8-12%) | High |
| V3 | Procurement network | Dynamic | Very High |

---

## UK EV Installation Market

**Demand:**
- 355,746 BEV registrations through August 2026 (+28.6% YoY)
- 29.8% of August registrations were BEVs
- 412,000+ home charging installations historically
- Grants worth up to £500/socket through March 2027

**Customer pain:**
- £800-£1,500 for domestic installation
- £800 vs £1,400 quotes for same job
- "Standard installation" turning into £500+ extras
- Electricians ghosting enquiries
- Confusion around charger choice, tariffs, cable length

**Supply:**
- ~2,074 OZEV-approved installers
- GOV.UK postcode-searchable installer directory
- Fragmented market

---

## Google Infrastructure Available NOW

| Resource | What It Provides | Cost |
|----------|------------------|------|
| Places Insights BigQuery | Supply density + history by H3 | Sample datasets free |
| Maps Grounding Lite MCP | Live supplier investigation | Free prototype |
| Places API IDs-only | Stable supplier identity | Free/unlimited |
| Keyword Planner UI | Search volumes, CPC estimates | Free with Ads account |
| Companies House API | UK business validation | Free |
| OZEV directory | EV installer truth set | Free |

**Key insight:** Google launched exactly the infrastructure we need. Places Insights exposes H3 density, Place IDs, ratings, and historical snapshots back to January 2024.

---

## The 13-Step Build

```
1. Connect Places Insights London sample
2. Import DVLA plug-in ownership by LSOA
3. Import DfT EV charging infrastructure
4. Import/resolve OZEV installers
5. Build H3 buyer-demand × supplier-density map
6. Run EV keyword universe through Keyword Planner UI
7. Capture Google SERP competitors and quote offers
8. Recruit 5-10 installers in one underserved geography
9. Build canonical AI photo-survey intake
10. Run £5-10/day exact/phrase Google Search
11. Sell qualified leads initially
12. Measure every transition
13. Update posterior
```

---

## Canonical Service Campaign Schema

```json
{
  "schema_version": "geodrop.service_campaign.v1",
  "identity": {...},
  "hypothesis": {...},
  "demand": {...},
  "paid_search": {...},
  "supply": {...},
  "supplier": {...},
  "competition": {...},
  "job_economics": {...},
  "funnel_prior": {...},
  "forecast": {...},
  "operations": {...},
  "regulation": {...},
  "experiment": {...},
  "actuals": {...},
  "learning": {...}
}
```

---

## Forecasting Equations

```
Expected completed jobs =
  searches × impression_share × CTR × click_to_lead ×
  lead_to_qualified × qualified_to_booking × booking_to_completion

platform_margin_per_job =
  platform_fee - payment_cost - variable_support_cost -
  expected_refund_loss - expected_dispute_loss

expected_value_per_click =
  P(lead|click) × P(qualified|lead) × P(book|qualified) ×
  P(complete|booked) × platform_margin_per_job

break_even_CPC = expected_value_per_click
```

---

## What Makes This Different

1. **Not just lead generation** — V0 is leads, V2 is managed transactions
2. **Google Maps as supply intelligence** — Places Insights gives us H3 density, historical snapshots, Place IDs
3. **AI photo-survey intake** — Standardized job specs from photos
4. **Stripe Connect for payments** — Split payments, delayed seller payouts
5. **Repeatable across categories** — EV → solar → heat pumps → boilers → electrical

---

## The Moat

> **A real-time graph of who can perform what service, where, at what price, with what capacity and completion quality.**

That asset transfers across categories.
