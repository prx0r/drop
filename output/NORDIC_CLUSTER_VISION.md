# Nordic Cluster Vision

*Finland should be Country Model v1. The machine-readable economic operating model of every country, continually refreshed.*

---

## The Core Insight

> **A machine-readable economic operating model of every country, continually refreshed, where every new campaign and outcome makes that model richer.**

That has compounding value even when an individual product hypothesis dies.

---

## The Hierarchy

```
Country Reality → Mechanisms → Needs → Products → Suppliers → Campaigns
```

Not products first.

---

## Finland Structural Features

| Signal | Value | Why It Matters |
|--------|-------|----------------|
| Heat pumps installed | 1.8M | Giant lifecycle graph (filters, remotes, controllers, replacement) |
| 2025 heat pump sales | 112,000 | Active replacement market |
| Cottages | 485,475 | Remote property monitoring opportunity |
| Average cottage distance | 91 km from home | Remote ownership changes failure economics |
| Online purchase rate | 84% | High ecommerce propensity |
| Cross-border purchases | 80% | Import-friendly, foreign supplier topology central |
| Hinta.fi products | ~1.5M | Continuously queryable merchant-gap sensor |
| Hinta.fi shops | ~49 | Merchant quality monitoring |
| Hinta.fi prices | ~4M | Price dispersion monitoring |
| VAT rate | 25.5% | Compiler rule, not agent memory |
| Parcel lockers | Most used/preferred | Shipping economics |
| Payment | Online bank + debit | Distinct from NO (Vipps) / DK (MobilePay) |

---

## Country Model v1 Structure

```
countries/FI/
├── profile.json           # Demographics, macro, language, currency
├── commerce_policy.json   # VAT, consumer law, checkout, returns, payments, consent
├── consumer.json          # Payment preferences, delivery preferences, trust
├── logistics.json         # Posti, Matkahuolto, lockers, shipping costs
├── cross_border.json      # Source countries, marketplaces, import propensity
├── installed_bases.json   # Heat pumps, cottages, EVs, heating, boats, saunas
├── lifecycle_events.json  # Replacement clocks, warranty, regulation, EOL
├── competition.json       # Hinta.fi, Prisjakt, Google Shopping, retailers
├── supply_graph.json      # Manufacturers, distributors, authorization
├── demand_surface.json    # Keywords, CPC, trends, query clusters
├── regional.json          # Population, income, cottages, climate
├── seasonality.json       # Temperature, snow, daylight, holidays
├── observations.jsonl     # Temporal measurements
├── snapshot.json          # Campaign compiler input
└── hypotheses.json        # Auto-generated from intersections
```

---

## Installed-Base Lifecycle Subsystem

For each installed base, track:
- Size (units)
- Growth rate
- Average age
- Replacement cycle
- Warranty period
- Failure modes
- Accessories/parts
- Compatibility requirements
- Service network

Example:
```
heat_pumps:
  installed_base: 1,800,000
  annual_sales: 112,000
  avg_age: 8 years
  replacement_cycle: 15-20 years
  filters: annual
  controllers: 5-7 years
  refrigerant: R32 transition
  service_network: limited
```

---

## Hinta.fi Merchant Census

Periodic snapshot:
```
GTIN → category → brand → model
  seller_count
  seller_count_change_30d
  median_price
  minimum_price
  price_dispersion
  shipping_inclusive_minimum
  delivery_days
  stocked_sellers
  popularity_rank
  popularity_rank_change
  merchant_quality_top_5
```

Discover:
- Demand stable, sellers fell 8 → 3
- Price dispersion widened 27%
- Popular product but only 2 sellers offer <3-day delivery

---

## Cross-Nordic Supplier Arbitrage

```
Manufacturer
  → EU/Nordic distributor
    → Sweden warehouse
    → Germany warehouse
    → Finland distributor
      → Finland customer
```

For each:
- Wholesale price
- Country
- Warehouse
- VAT treatment
- Shipping
- Lead time
- MOQ
- Dropship capability
- Reseller authorization
- MAP restrictions
- Warranty handling
- Returns destination

Discovery: Swedish wholesale supply can serve Finnish demand while Finnish retail competition remains fragmented.

---

## Nordic Cluster Sequence

1. **Norway** (current) — Campaign Zero, Davis lifecycle
2. **Finland** (next) — Country Model v1, installed-base laboratory
3. **Sweden** — Largest Nordic ecommerce, cross-border structure
4. **Denmark** — Compact, wealthy, distinct payment/logistics
5. **Iceland** — Eventually, small market

---

## Four Finland Probes

1. **Heat-pump lifecycle** — 1.8M installed, replacement/event rate
2. **Cottage/remote-property systems** — 485k cottages, remote monitoring
3. **Hinta.fi merchant-census time series** — Price dispersion, seller changes
4. **Nordic distributor topology** — Cross-border supply arbitrage

---

## The Two Tracks

**Track A — Execution:**
Push NO-DAVIS-LIFECYCLE-001 through Campaign Compiler.

**Track B — Intelligence:**
Build Finland Country Model v1, back-port Norway, clone to Sweden/Denmark.

They strengthen each other.
