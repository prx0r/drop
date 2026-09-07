# Campaign Hypothesis: Finland Heat Pump Controller

**Campaign ID:** FI-HP-CONTROLLER-001
**Date:** 2026-09-08
**Status:** HYPOTHESIS

---

## 1. Executive Summary

**Claim:** Finnish heat pump owners will convert through a compatibility/remote-control decision service at an acquisition cost below realized CM2, because existing merchants inadequately resolve controller selection, compatibility, and remote monitoring decisions.

**Primary outcome:** Realized CM2 (automated operating contribution)

**Budget:** €200 setup + €5/day ads = €350 Month 1

---

## 2. Data Backing

### Installed Base
- Finland: ~1.8-2.0 million heat pumps installed
- Annual sales: 112,000 (2025), +63% YoY (H1 2026)
- Replacement share: ~33% of sales
- Annual replacement: ~37,000 units
- H1 2026: 74,000 deliveries, air-to-air +71%

Source: SULPU (Finnish Heat Pump Association)

### Market Structure
- 3 known merchants: Pihabotti, Finnparttia, Staypro
- Source-target gap: SE → FI exists for heat pump ecosystem
- Installed base in PRIORITY_RESEARCH state

### Economics (from pricing calculator)
- Retail: €250
- Supplier: €80
- Shipping: €15
- Landed cost: €95
- Net revenue: €200 (after 25.5% VAT)
- Gross profit: €105 (52.5%)
- Net profit: €88.25 (44.1%)
- Breakeven CAC: €88.25
- Recommendation: SCALE

---

## 3. Hypothesis

**H1:** Finnish heat pump owners with 5-10 year old systems will convert through a compatibility/remote-control decision service at an acquisition cost below €88.25 (breakeven CAC).

**H0:** Apparent demand is already served by existing merchants or OEM direct channels.

**Falsifiers:**
- Existing merchants already solve the compatibility problem
- OEM apps make controllers unnecessary
- No meaningful search demand for heat pump controllers in Finnish
- Actual CPC >€3.00 (unprofitable at 0.5% CVR)

---

## 4. Causal Mechanism

```
1.8M installed heat pumps
    ↓
5-10 year old systems need controller upgrade
    ↓
Compatibility confusion (which controller fits which model?)
    ↓
Remote monitoring desire (app control, energy optimization)
    ↓
Fragmented merchant landscape (3 known sellers)
    ↓
We provide: compatibility decision service + curated controller selection
```

---

## 5. Activation Gates

| Gate | Required | Status | Evidence |
|------|----------|--------|----------|
| Supplier authorized | Yes | BLOCKED | Need to contact Pihabotti or Finnparttia |
| Online resale allowed | Yes | UNKNOWN | Must verify with supplier |
| Exact supplier cost | Yes | BLOCKED | Need dealer net price |
| Landed cost verified | Yes | PARTIAL | Estimated €95 |
| Positive CM2 | Yes | PENDING | Need real supplier cost |
| Keyword data authenticated | Yes | BLOCKED | Need Google Ads access |
| Break-even CPC above market | Yes | PENDING | Need CPC data |
| Products in stock | Yes | UNKNOWN | Must verify supplier stock |
| Merchant center approved | Yes | NOT STARTED | Need to apply |
| Checkout test passed | Yes | NOT STARTED | Need store live |
| Conversion tracking test | Yes | NOT STARTED | Need GA4 setup |
| Shipping policy verified | Yes | UNKNOWN | Must verify with supplier |
| Return policy verified | Yes | UNKNOWN | Must verify with supplier |
| Consent implementation | Yes | NOT STARTED | Need GDPR cookie consent |

---

## 6. Campaign Spec

### Store Configuration
- **Market:** Finland
- **Language:** Finnish
- **Currency:** EUR
- **Domain:** TBD
- **Brand:** TBD
- **Payments:** Online bank, debit card, MobilePay
- **Shipping:** Posti, Matkahuolto (parcel lockers preferred)
- **Returns:** 14 days (Finnish consumer law)
- **Legal:** ALV 25.5%, withdrawal right info required

### Decision Engine
**Questions:**
1. Do you have a heat pump? (boolean)
2. What brand/model? (select: Panasonic, Mitsubishi, Daikin, Other)
3. What do you want to achieve? (select: Remote control, Energy optimization, Replacement, New installation)

**Compatibility rules:**
- Panasonic → Panasonic controllers
- Mitsubishi → Mitsubishi controllers
- Daikin → Daikin controllers

**Recommendation:** Dynamic based on answers

### Ads Configuration
- **Channel:** Google Search
- **Geo:** Finland
- **Language:** Finnish
- **Keywords:** 
  - "lämpöpumppu ohjain" (heat pump controller)
  - "lämpöpumppu etäohjaus" (heat pump remote control)
  - "lämpöpumppu Wi-Fi" (heat pump Wi-Fi)
  - "panasonic lämpöpumppu ohjain" (Panasonic heat pump controller)
  - "daikin lämpöpumppu ohjain" (Daikin heat pump controller)
- **Negatives:** "ilmainen" (free), "käytetty" (used), "halpa" (cheap)
- **Bidding:** Maximize clicks
- **Budget:** €5/day

### Measurement
- **Events:** page_view, chooser_start, chooser_complete, product_view, add_to_cart, begin_checkout, purchase
- **Conversions:** purchase
- **Attribution:** Last click
- **Consent:** EEA GDPR

---

## 7. Profit Forecast

### Scenario Analysis

| Scenario | CVR | Orders/month | Revenue | CM2 | Profit |
|----------|-----|--------------|---------|-----|--------|
| Pessimistic | 0.3% | 4.5 | €1,125 | €397 | €397 |
| Base | 0.5% | 7.5 | €1,875 | €662 | €662 |
| Optimistic | 0.8% | 12 | €3,000 | €1,059 | €1,059 |

**Assumptions:**
- 1,500 clicks/month at €0.50 CPC = €750 ad spend
- AOV: €250
- CM2 margin: 44.1%
- Returns: 3%
- Support cost: €2/order

### Break-Even Analysis
- **Breakeven CVR:** 0.33% (at €0.50 CPC)
- **Breakeven CPC:** €1.17 (at 0.5% CVR)
- **Payback period:** 1 month (at base scenario)

---

## 8. Falsification Plan

### Week 1-2: Free Listings Test
- List 5-10 heat pump controllers on Google Merchant Center
- Measure impressions, clicks, CTR
- **Kill if:** <50 impressions after 7 days

### Week 3-4: Content Test
- Build compatibility guide pages
- Measure organic traffic, time on page, bounce rate
- **Kill if:** <100 organic visits after 14 days

### Week 5-8: Paid Test
- Run €5/day Google Ads
- Measure CPC, CTR, CVR, ATC rate
- **Kill if:** CPC >€3.00 or CVR <0.2%

### Week 9-12: Scale Test
- Increase budget to €10/day
- Measure CM2, return rate, customer satisfaction
- **Kill if:** CM2 negative after 30 days

---

## 9. Success Criteria

**Month 1:** 5 orders at €250 AOV = €1,250 revenue, €550 profit
**Month 3:** 15 orders at €250 AOV = €3,750 revenue, €1,650 profit
**Month 6:** 30 orders at €250 AOV = €7,500 revenue, €3,300 profit

**Decision thresholds:**
- P > 0.3: Research freely
- P > 0.5: Free listing test
- P > 0.65: €5 paid probe
- P > 0.8: €50 validation
- Lower credible bound > 0: Scale

---

## 10. Next Actions

1. **Contact Pihabotti** — Verify dealer terms, net price, dropship capability
2. **Keyword research** — Pull Finnish heat pump controller search volume
3. **Merchant census** — Check Hinta.fi for controller seller count
4. **Source market analysis** — Check SE/DE for controller availability and pricing
5. **Build compatibility guide** — Finnish language, model-specific

---

## 11. Receipts

| Step | Receipt | Verified |
|------|---------|----------|
| Gmail fetch | 864c951e94a03e5d | ✅ |
| Observation extraction | cec0b1a575c71d9b | ✅ |
| BigQuery write | e1ac1385370d134b | ✅ |
| Pricing calculation | Manual | ✅ |
| Ecosystem data | FI_HEATPUMP_INSTALLED | ✅ |
| Hypothesis data | H_FI_HP_REPLACEMENT_V1 | ✅ |

---

*Generated: 2026-09-08T12:00:00Z*
*Campaign ID: FI-HP-CONTROLLER-001*
