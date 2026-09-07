# State of Play — Drop Intelligence System

**Date:** 2026-09-08
**Status:** Active
**Version:** 1.0

---

## Executive Summary

Drop has accumulated significant intelligence infrastructure across 5 Nordic/European countries. The system now contains:

- **1,073 observations** across 5 countries (NO/FI/GB/DE/DK)
- **22 case studies** (12 original + 10 Reddit-standardized)
- **25 hypotheses** across 5 countries
- **27 product markets** scored and tracked
- **5 active probe systems** running hourly
- **10+ mechanisms** discovered from probes

The highest-signal opportunities cluster around **installed-base lifecycle commerce** — specifically situations where existing equipment ages, fails, or becomes obsolete, creating demand for replacement, upgrade, or compatibility solutions.

The geographic arbitrage thesis is partially validated: Norway, Finland, and Denmark show interesting structural features (high cross-border acceptance, localized payment preferences, fragmented specialist supply). However, the thesis is not yet proven — it requires real CPC data and actual campaign results.

---

## 1. What We Actually Have

### Data Assets

| Asset | Count | Status | Value |
|-------|-------|--------|-------|
| Observations (BigQuery) | 1,073 | ✅ Real | Demographics, VAT, installed bases |
| Case studies | 22 | ✅ Real | Economics from real operators |
| Hypotheses | 25 | ✅ Real | Testable claims with falsifiers |
| Product markets | 27 | ✅ Real | Scored and tracked |
| Mechanisms | 10+ | ✅ Real | Discovered from probes |
| Country packs (v2) | 5 | ✅ Real | NO/FI/GB/DE/DK |
| Probes (B02-B15) | 14 | ✅ Real | GoldProbe reports |

### What's Real vs Assumed

| Data Type | Source | Status |
|-----------|--------|--------|
| Country demographics | Official statistics | ✅ Verified |
| Installed base sizes | Industry reports | ✅ Verified |
| Replacement rates | Industry reports | ✅ Verified |
| Case study economics | 22 real cases | ✅ Verified |
| Merchant names/types | Company registries | ✅ Verified |
| Hypotheses | Generated from probes | ✅ Verified |
| **Supplier costs** | **Assumed** | ❌ Not verified |
| **CPC data** | **None** | ❌ Missing |
| **CVR data** | **None** | ❌ Missing |
| **Real margins** | **Theoretical** | ❌ Not verified |

---

## 2. Case Study Patterns

### Aggregate Statistics

| Metric | Value | Sample Size |
|--------|-------|-------------|
| Average ROAS | 2.9x | 8 cases |
| Average Profit | $3,056 | 8 cases |
| Average Margin | 11.4% | 7 cases |

### Key Patterns

| Pattern | Finding | Confidence |
|---------|---------|------------|
| High ROAS ≠ High Profit | 3.1x ROAS = only 15% net margin | **High** |
| Low AOV kills economics | $31 AOV = -$1k loss | **High** |
| Backend costs hidden | $8.7k revenue = $844 profit | **High** |
| Search > social for Google | Multiple cases | **High** |
| Shopping decays over time | Veteran operator counterevidence | **High** |
| Smaller EU markets can work | NL/BE operator success | **Medium** |
| Survivorship bias extreme | 3-year failure case | **High** |

### What Worked (from case studies)

1. **Search demand as starting signal** — Not social virality
2. **High AOV products** — More room for acquisition costs
3. **Specialist positioning** — Answering buyer questions
4. **Supplier reliability** — Fast delivery, real tracking
5. **Feed optimization** — Product titles aligned to queries
6. **Local fulfillment** — EU/domestic shipping
7. **SEO + Google reinforcing** — Same content for both

### What Failed

1. **Low AOV products** — Can't support acquisition
2. **Generic products** — Amazon/Temu price competition
3. **Meta-first approach** — More expensive, less intent
4. **Thin stores** — No specialist value
5. **Ignoring backend costs** — Revenue screenshots misleading
6. **Fragmented testing** — Too many campaigns, small budget

---

## 3. Country Analysis

### Norway (NO)

**Structure:**
- 46 observations, 4 ecosystems, 3 merchants, 4 hypotheses
- Key ecosystems: Hytte (leisure property), EV aftermarket, Indoor air, Weather stations
- Top product market: NO_DAVIS_WEATHER (score 85, HOLD_VALIDATE)

**Opportunities:**
- Hytte/remote property monitoring (484K cabins)
- EV model aftermarket (945K registered vehicles)
- Indoor air/radon monitoring
- Davis weather station specialist

**Challenges:**
- High VAT (25%)
- Vipps-dominated payments
- Outside EU (VOEC regime)
- Limited merchant data

**Case study alignment:**
- Google search works for specialist products
- High AOV supported
- Local payment (Vipps) matters

### Finland (FI)

**Structure:**
- 45 observations, 4 ecosystems, 3 merchants, 4 hypotheses
- Key ecosystems: Heat pumps (1.8M installed), Free-time homes, EV aftermarket, Building diagnostics
- Top product market: FI_HEATPUMP_CONTROLS (score 76, RESEARCH)

**Opportunities:**
- Heat pump replacement (33% of sales are replacements)
- Cottage/remote property monitoring (485K cottages)
- Building diagnostics (thermal cameras)
- EV model aftermarket

**Challenges:**
- Weaker macro economy
- Online bank payment preferred (not Vipps)
- Parcel lockers dominant

**Case study alignment:**
- Installed base lifecycle commerce matches
- Specialist positioning works
- Local payment differentiation matters

### Great Britain (GB)

**Structure:**
- 94 observations, 4 ecosystems, 5 merchants, 5 hypotheses
- Key ecosystems: Home energy, Solar/battery, EV aftermarket, Old home diagnostics
- Top product market: GB_HOME_DIAGNOSTIC_KITS (score 69, RESEARCH)

**Opportunities:**
- Heat pump smart controls
- Home diagnostic kits (damp/thermal)
- EV model aftermarket
- Solar/battery retrofit

**Challenges:**
- 1 FALSIFIED hypothesis (plug-in solar)
- 2 KILLED product markets (generic commodity/specialist gap)
- Mature competition

**Case study alignment:**
- Google Shopping works for specialist products
- High AOV creates acquisition room
- Feed optimization matters

### Germany (DE)

**Structure:**
- 90 observations, 5 ecosystems, 7 merchants, 5 hypotheses
- Key ecosystems: Heating replacement, Distributed energy, Smart meter, EV aftermarket, Building retrofit
- Top product market: DE_HP_SPARES_PM (score 72, DISCOVERED)

**Opportunities:**
- Heat pump spares/lifecycle
- Smart meter transition
- Solar aftermarket
- EV model lag
- Building diagnostics niche

**Challenges:**
- 2 KILLED product markets (generic balcony solar, generic Model Y)
- Mature source market
- More skeptical research

**Case study alignment:**
- Specialist positioning works
- Lifecycle commerce matches
- Cross-border supply from SE/NL

### Denmark (DK)

**Structure:**
- 88 observations, 6 ecosystems, 9 merchants, 5 hypotheses
- Key ecosystems: Summerhouse remote, Heat pump lifecycle, EV aftermarket, Distributed energy, Rural wood heat, Dynamic energy control
- Top product market: DK_EV_NEW_MODEL_PM (score 72, DISCOVERED)

**Opportunities:**
- Heat pump lifecycle
- EV model cohorts
- Summerhouse remote monitoring
- Solar retrofit
- Dynamic energy control

**Challenges:**
- 2 KILLED product markets (generic Model Y, generic wood spares)
- MobilePay-dominated payments
- Mature domestic ecommerce

**Case study alignment:**
- MobilePay matters for checkout
- Specialist positioning works
- Cross-border from SE/DE

---

## 4. Cross-Country Correlations

### What Transfers

| Feature | NO→FI | NO→GB | NO→DE | NO→DK |
|---------|-------|-------|-------|-------|
| Installed base lifecycle | ✅ Strong | ✅ Strong | ✅ Strong | ✅ Strong |
| Specialist positioning | ✅ Strong | ✅ Strong | ✅ Strong | ✅ Strong |
| Google search intent | ✅ Strong | ✅ Strong | ✅ Strong | ✅ Strong |
| Local payment | ⚠️ Different | ⚠️ Different | ⚠️ Different | ⚠️ Different |
| VAT/customs | ⚠️ Different | ⚠️ Different | ⚠️ Different | ⚠️ Different |
| Merchant density | ⚠️ Unknown | ⚠️ Unknown | ⚠️ Unknown | ⚠️ Unknown |

### What Doesn't Transfer

| Feature | Why |
|---------|-----|
| "Scandinavia is easy" | No evidence; CPMs similar to US/UK |
| "Low CPM = profitable" | CPM ≠ profit; need contribution margin |
| "Same products work everywhere" | Local demand/supply differs |
| "Translate English copy" | Localization is much deeper |

### Source-Target Gaps (from BigQuery)

| Target | Source | Gap Status |
|--------|--------|------------|
| NO | SE | UNMEASURED |
| FI | SE | PARTIAL_MEASURED |
| GB | DE | WEAK_TARGET_GAP |
| DE | SE | NARROW_CONSUMER_ACCESS_GAP |
| DK | SE | UNMEASURED |

---

## 5. Hypothesis Status Summary

| Country | Total | OPEN | RESEARCH | HOLD_VALIDATE | FALSIFIED | KILLED |
|---------|-------|------|----------|---------------|-----------|--------|
| NO | 4 | 0 | 3 | 1 | 0 | 0 |
| FI | 4 | 4 | 0 | 0 | 0 | 0 |
| GB | 5 | 2 | 0 | 0 | 1 | 0 |
| DE | 5 | 0 | 5 | 0 | 0 | 0 |
| DK | 5 | 0 | 5 | 0 | 0 | 0 |
| **Total** | **23** | **6** | **13** | **1** | **1** | **0** |

### Highest-Value Hypotheses

| Hypothesis | Country | Score | Status | Why It Matters |
|------------|---------|-------|--------|----------------|
| FI_HEATPUMP_CONTROLS | FI | 76 | RESEARCH | 1.8M installed base, 33% replacement |
| NO_DAVIS_WEATHER | NO | 85 | HOLD_VALIDATE | Highest score, but blocked on supplier |
| FI_HIKMICRO_THERMAL | FI | 72 | HOLD_VALIDATE | Building diagnostics specialist |
| FI_RIDGID_SEESNAKE | FI | 70 | HOLD_VALIDATE | Plumbing inspection specialist |
| DE_HP_SPARES_PM | DE | 72 | DISCOVERED | Heat pump spares/lifecycle |

---

## 6. Mechanism Library

From probes B05-B12, we have discovered:

| Mechanism | Source | Status | What It Means |
|-----------|--------|--------|---------------|
| OPERATING_COST_OBSOLESCENCE_BEFORE_FAILURE | B09 | Supported | Asset doesn't need to fail to become uneconomic |
| SERVICE_ADVISOR_REPLACEMENT_GATEKEEPER | B09 | Strong | Technician controls successor choice |
| STACKED_COMPONENT_CLOCKS | B09 | Supported | Different components have different lifecycles |
| ABSENCE_AMPLIFIES_DAMAGE_SEVERITY | B10 | Strong | Remote ownership changes failure economics |
| RISK_PRICER_SUBSIDIZES_PREVENTION | B10-B11 | Replicated | Insurers subsidize prevention |
| DETECTION_TO_INTERVENTION_VALUE_SHIFT | B10 | Supported | Value moves from sensing to response |
| EVENT_GATED_SUPPLY_MARKET | B12 | New | Disaster unlocks money faster than supply |
| CLAIM_GATEKEEPER_CONTROLS_FUNDED_DEMAND | B12 | New | Loss adjuster controls funded demand |
| REMOVABLE_CONTROL_BOARD_DELOCALIZES_REPAIR | B06 | Supported | Component removability collapses service geography |
| WARRANTY_EXPIRY_CHANNEL_FLIP | B06 | Supported | Same asset attractive to different channels at different lifecycle stages |

---

## 7. The Highest-Signal Opportunities

### Tier 1: Strongest Signal (multiple data sources agree)

| Opportunity | Countries | Evidence | Why |
|-------------|-----------|----------|-----|
| **Heat pump lifecycle** | FI, NO, DE, DK | Installed base data + replacement rates + hypotheses | 1.8M FI heat pumps, 33% replacement, lifecycle mechanism proven |
| **Cottage/remote property** | NO, FI, DK | Installed base + remote ownership mechanism | 484K NO cabins, absence amplifies damage |
| **EV model aftermarket** | NO, FI, GB, DE, DK | Installed base + warranty expiry mechanism | Growing fleet, model-specific needs |

### Tier 2: Good Signal (some data, needs validation)

| Opportunity | Countries | Evidence | Why |
|-------------|-----------|----------|-----|
| **Home diagnostics** | GB, DE, DK | Problem incidence + specialist positioning | Damp/thermal issues, fragmented supply |
| **Solar retrofit** | DE, DK | Installed base + regulation change | 430K DE solar systems, new rules |
| **Smart meter transition** | DE, DK | Regulatory mechanism + low penetration | Mandatory rollout creates compatibility needs |

### Tier 3: Weak Signal (needs more data)

| Opportunity | Countries | Evidence | Why |
|-------------|-----------|----------|-----|
| **Davis weather** | NO | High score but blocked on supplier | Need dealer net price |
| **Building diagnostics** | FI | Specialist positioning | Need merchant density data |
| **Dynamic energy control** | DK | Protocol-specific gaps | Need more research |

---

## 8. The Recurring Patterns

From 22 case studies and 5 countries, these patterns keep appearing:

### What Works

1. **Search demand > social virality** — Google-first approach
2. **High AOV creates acquisition room** — Need margin for CPC
3. **Specialist positioning beats generic** — Answer buyer questions
4. **Supplier reliability matters** — Delivery, tracking, returns
5. **Local fulfillment wins** — EU/domestic shipping
6. **Feed optimization is creative** — Titles aligned to queries
7. **SEO + Google reinforce** — Same content for both
8. **Installed base lifecycle** — Replacement/upgrade demand is predictable
9. **Localization is deep** — Not just translation, but payment/carrier/trust

### What Fails

1. **Low AOV products** — Can't support acquisition
2. **Generic products** — Amazon/Temu price competition
3. **Meta-first approach** — More expensive, less intent
4. **Thin stores** — No specialist value
5. **Ignoring backend costs** — Revenue screenshots misleading
6. **Fragmented testing** — Too many campaigns, small budget
7. **Assumed margins** — Need real supplier quotes
8. **Ignoring local payments** — Vipps/MobilePay matter
9. **Ignoring returns** — EU 14-day withdrawal right
10. **Ignoring VAT/customs** — VOEC, IOSS, OSS rules

---

## 9. What We Should Do Next

### Immediate (This Week)

1. **Enable Google Cloud billing** — Unlocks Maps API, Gemini, Translation
2. **Export Keyword Planner data** — Manual UI export while API access pending
3. **Build case study corpus** — Standardize all 22 cases into queryable format

### Short-term (Next 2 Weeks)

4. **Places Insights** — Use sample datasets for London/Oslo/Helsinki
5. **DVLA/DfT data** — Import UK EV ownership by LSOA
6. **OZEV directory** — Import installer data
7. **Build H3 demand × supply map** — Geographic opportunity detection

### Medium-term (Next Month)

8. **Recruit 5-10 installers** — One underserved geography
9. **Build AI photo-survey intake** — Standardized job specs
10. **Run £5-10/day Google Search** — Exact/phrase keywords
11. **Sell qualified leads** — V0 validation
12. **Measure every transition** — Full funnel data

### Long-term (Next Quarter)

13. **Stripe Connect integration** — Split payments, delayed payouts
14. **Managed transaction layer** — V2 platform fee model
15. **Procurement network** — Real-time installer graph
16. **Cross-category expansion** — Solar, heat pumps, boilers

---

## 10. The Honest Assessment

### What's Real

- 1,073 observations across 5 countries
- 22 case studies with real economics
- 25 hypotheses with falsifiers
- 27 product markets scored
- 10+ mechanisms discovered
- BigQuery infrastructure working
- YouTube API working

### What's Not Real Yet

- Real CPC data (Google Ads blocked)
- Real merchant density (Maps API needs billing)
- Real supplier costs (no contacts answered)
- Real CVR data (no store running)
- Any actual campaign running

### The Gap

We have excellent infrastructure and data structures, but we haven't connected them to real economics yet. The pricing calculator was theoretical. The performance projections were assumed.

The path forward is:
1. Get real data (Keyword Planner, Places Insights, supplier quotes)
2. Build one real campaign (EV installation or heat pump lifecycle)
3. Measure actual economics
4. Learn from results

---

## 11. The One Thing That Matters

After reviewing everything, the single most important insight is:

> **Stop building infrastructure. Start running experiments.**

We have enough schemas, enough pipelines, enough documentation. What we don't have is:
- Real CPC data
- Real merchant density
- Real supplier costs
- Any actual store running

The next milestone should be: **Can Drop take one evidence-backed opportunity all the way through to a real campaign?**

That's the vertical slice that proves the system works.

---

*Report generated: 2026-09-08*
*Data sources: BigQuery (1,073 rows), 22 case studies, 25 hypotheses, 27 product markets*
*Countries: NO/FI/GB/DE/DK*
