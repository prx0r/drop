# [GeoDrop Channel Economics Probe] 2026-09-07 11:10 — Flak reseller path verified / dealer margin still gated

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Sun, 6 Sep 2026 21:11:06 -0700
**Gmail ID:** 1a07a100887efcfe

---

# GeoDrop Channel Economics Probe — 2026-09-07 11:10

## Material commercial delta

**NO-DAVIS-6313-001 — Davis WeatherLink Console 6313EU × Norway**

State change: **SUPPLY_PATH_BLOCKED → SUPPLY_PATH_PARTIALLY_VERIFIED + HUMAN_ACTION_REQUIRED**.

This run materially resolved the channel-access and fulfillment questions, but **did not verify margin**.

### What changed

Flak AS publicly confirms that it sells only to approved businesses, but it explicitly accepts applications from businesses/dealers. Approval requires company details plus a description of the business/reason for buying, and Flak may perform a credit check. This means reseller access is **selective/application-gated, not structurally denied**.

Flak also states it stocks more than 12,000 product lines in Kristiansand and can deliver quickly across Norway. Exact 6313EU stock depth still requires account access/confirmation.

Sources:
- https://www.flak.no/get-started
- https://www.flak.no/bliforhandler
- https://www.flak.no/produkter/fritid-og-fiske/vaerstasjoner/davis-weatherlink-console-p3003096

## Supply graph

**Davis Instruments → Flak AS (Norwegian wholesale/dealer channel) → Norwegian dealer/storefront → end customer**

Fulfillment/service graph:

**Flak Kristiansand warehouse → dealer account → optionally third-party end-customer shipment → Flak My Page claims/returns + manufacturer warranty**

The visible Norwegian sellers remain poor evidence of independent supply. Several storefronts appear to share the same Flak-fed product number/copy/stock signal. Public seller scarcity therefore does **not** survive hidden-channel inspection.

## Fields actually resolved this hour

### Reseller eligibility — RESOLVED PARTIALLY
Flak explicitly accepts business/dealer applications. Approval is discretionary and may include a credit check.

### Direct-to-customer shipment — RESOLVED
Flak's 2025 B2B terms explicitly allow shipment to a third party.

Important negative detail: **third-party freight is charged to the buyer**, and Flak disclaims responsibility for the shipment. This is not equivalent to free or riskless dropshipping.

### Payment terms — RESOLVED
Standard payment term: **20 days from invoice date**.

### Price mechanism — RESOLVED, actual cost still UNKNOWN
Flak's applicable customer price list is downloadable under My Page after login. Flak gives an additional **2% web-order discount** versus that price list.

This does not reveal the dealer net price.

### Returns / service burden — MATERIAL NEGATIVE RESOLUTION
Flak's current B2B terms say:
- non-defect returns require approval;
- only stocked products are considered for return;
- special-order items generally cannot be returned;
- buyer pays return freight;
- a 15% return fee can apply after 14 days;
- rejected warranty/reclamation checks can be billed for freight and labor;
- approved claims are generally credited or repaired depending on the applicable manufacturer/supplier warranty.

This means a low gross-margin offer is unsafe unless a service/returns reserve is explicitly modeled.

Terms source:
https://webserver.flak.no/vbilder/2025_Standard_Salgs_Og_leveringsbetingelser_Flak_AS_(SOL008)-1.pdf

Davis warranty source:
https://www.davisinstruments.com/pages/warranty-registration

## Economics / hard thresholds

Current Norwegian observed retail: **NOK 7,590 incl. 25% VAT**.

Net retail revenue:

`7,590 / 1.25 = NOK 6,072`

Maximum landed supplier cost before payment fees, outbound freight, returns/service reserve and CAC:

| Target merchandise margin | Max landed cost |
|---|---:|
| 10% | NOK 5,464.80 |
| 15% | NOK 5,161.20 |
| 20% | NOK 4,857.60 |
| 25% | NOK 4,554.00 |
| 30% | NOK 4,250.40 |

Flak's public RRP for 6313EU is **NOK 8,399 incl VAT**, or **NOK 6,719.20 ex VAT**.

Therefore, before third-party freight:
- a 20% merchandise-margin launch requires effective landed cost at least **27.7% below Flak public RRP net**;
- a 25% margin requires at least **32.2% below public RRP net**.

The known 2% web-order discount is nowhere near enough by itself. A substantial underlying dealer discount must exist.

**MARGIN_VERIFIED remains NO. No hidden dealer cost has been guessed.**

## Channel resilience / fragility

| Risk | Current assessment |
|---|---|
| single_supplier_dependency | MEDIUM-HIGH — Flak appears central in Norway |
| inventory_concentration | MEDIUM — exact 6313EU stock depth unknown |
| manufacturer_policy_risk | MEDIUM — Davis prefers international reseller/distributor channels |
| cross_border_dependency | LOW if Flak quote works |
| warranty_dependency | MEDIUM-HIGH — claims ultimately depend on manufacturer/supplier warranty |
| lead_time_volatility | UNKNOWN for exact 6313EU |
| substitute_supplier_count | LOW-MEDIUM locally; EU alternatives exist but warranty/freight/FX differ |
| EOL/successor risk | LOW currently; 6313 is the current replacement console |
| return/service burden | MEDIUM-HIGH |

## H1 / H0 ledger

**H1:** accessible Flak dealer channel + enough discount to support lifecycle-specialist economics.

Belief delta this run: **FOR channel accessibility, AGAINST easy economics**.

**H0:** hidden wholesale/service structure erases the apparent gap or leaves too little contribution after freight/RMA.

Belief delta this run: **FOR** because hidden channel access is real and B2B return/service terms are non-trivial.

**Decisive unknown:** actual Flak dealer net + single-order third-party freight.

**Falsifier:** landed authorized cost > NOK 4,857.60 at NOK 7,590 retail, or reseller/ecommerce approval denied.

## HUMAN_ACTION_REQUIRED — highest EVI

**external_action_id:** EA-NO-DAVIS-FLAK-001

Company: **Flak AS**
Application: https://www.flak.no/bliforhandler
Address: Skibåsen 37, 4636 Kristiansand, Norway

Exact SKU:
- Flak 3003096
- Davis 6313EU
- GTIN 0011698015153

Ask exactly:
1. Can a Norway-based ecommerce lifecycle specialist be approved as a Flak business/dealer customer?
2. Net ex-VAT price for 3003096 / 6313EU at **1 / 5 / 10 units**.
3. Is 6313EU currently stocked in Kristiansand, and what is normal replenishment/dispatch SLA?
4. What is freight for third-party shipment of one 6313EU to a Norwegian customer, and can paperwork/packaging be neutral?
5. Is stock/price data available as CSV/XML/API beyond the downloadable My Page price list?
6. Confirm first-line Davis RMA/warranty workflow and freight allocation in an approved warranty case.
7. Any ecommerce, marketplace, territory, advertised-price or Davis-brand restrictions?
8. Can the same account source 6357EU ISS, WeatherLink Live, and Vue/Pro2 service kits?

**Pass/fail:**
- 20% merchandise-margin ceiling: landed ≤ **NOK 4,857.60**
- preferred 25% ceiling: landed ≤ **NOK 4,554.00**
- these ceilings must be reduced further once payment fees, outbound freight and returns/service reserve are known.

Estimated human time: ~6 minutes.
Probability of useful response: HIGH.
Expected decision impact: HIGH.

Freeze this candidate after the application/quote request until Flak responds or a material stock/price/policy change appears.

## Candidate state consequence

**NO-DAVIS-6313-001 remains alive, but not launchable.**

The supply path is now substantially more concrete than in the upstream anomaly report, but the evidence cuts both ways:
- positive: reseller application exists, local wholesale infrastructure exists, third-party shipment is explicitly possible;
- negative: hidden wholesale competition is real, freight is charged on third-party shipment, and returns/RMA burden is meaningful.

The next useful information is a real dealer quote, not another supplier name.

## Dense kernels

**K-CE-20260907-1110-01 — AUTHORIZATION_RESULT**
OBSERVATION: Flak accepts approved-business/dealer applications; credit review may apply.
INFERENCE: reseller access is gated but not denied.
DECISION CONSEQUENCE: supply-path state advances to PARTIALLY_VERIFIED.

**K-CE-20260907-1110-02 — SUPPLY_PATH_DISCOVERY**
OBSERVATION: Flak explicitly permits third-party shipment; buyer pays freight and bears shipment risk.
INFERENCE: direct fulfillment is operationally possible but not free/neutral by default.
DECISION CONSEQUENCE: include third-party freight in landed-cost gate.

**K-CE-20260907-1110-03 — SERVICE_BURDEN**
OBSERVATION: returns require approval; buyer pays return freight; special orders are generally non-returnable; rejected claims may incur freight/labor.
INFERENCE: service reserve is material.
DECISION CONSEQUENCE: 20% merchandise margin alone is not sufficient evidence of launchability.

**K-CE-20260907-1110-04 — MARGIN_THRESHOLD**
OBSERVATION: Flak publishes NOK 8,399 RRP and offers 2% web-order discount versus login-gated price list; actual dealer net remains hidden.
INFERENCE: meaningful base dealer discount is required.
DECISION CONSEQUENCE: MARGIN_VERIFIED stays blocked.

Machine-readable supplier_offer, channel_graph, external_action, kernels and run manifest are attached.

