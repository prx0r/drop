# Drop — Compatibility Commerce Compiler

*Last Updated: 2026-09-07*

---

## What Is This?

We build the machine-readable compatibility layer that AI agents need to transact with local service providers and specialist product merchants. Then we own the supply side by giving them a free AI front desk.

---

## Active Campaigns (25)

Located in `campaigns/active/`:

| Campaign | Country | Gap Score | Priority |
|----------|---------|-----------|----------|
| balcony-door-hardware | NO | 10/10 | HIGH |
| vallox-ventilation | FI | 10/10 | HIGH |
| heatpump-electronics | FI | 9/10 | HIGH |
| hottub-control-panels | NO/SE/FI | 9/10 | HIGH |
| marine-electronics-retrofit | NO | 8/10 | HIGH |
| window-hardware-scandinavia | SE | 8/10 | HIGH |
| pool-filters-scandinavia | SE | 8/10 | HIGH |
| recliner-controls-nordic | NO/SE/FI | 8/10 | HIGH |
| nilan-ventilation | DK | 8/10 | HIGH |
| ouman-heating-control | FI | 8/10 | HIGH |
| cinderella-toilet | NO | 8/10 | HIGH |
| garage-door-hardware-norway | NO | 8/10 | HIGH |
| fire-alarm | UK | 8/10 | HIGH |
| hvac-controls | UK | 8/10 | HIGH |
| helios-ventilation-germany | DE | 8/10 | HIGH |
| ireland-heat-pump | IE | 7/10 | MEDIUM |
| radon-mitigation | NO | 7/10 | MEDIUM |
| pipe-inspection | FI | 7/10 | MEDIUM |
| marine-pump | NO | 5/10 | LOW |
| uk-ev-charger | UK | 5/10 | LOW |
| automower-parts | SE | 6/10 | LOW |
| harvia-sauna | FI | 6/10 | LOW |
| wallas-cabin-heater | FI/NO | 6/10 | LOW |
| flexit-ventilation | NO | 7/10 | MEDIUM |
| cabin-water-filtration | NO | 9/10 | HIGH |

---

## Project Structure

```
drop/
├── AGENTS.md                 # Binding rules
├── THESIS.md                 # Core thesis
├── THESIS_REFINED.md         # Refined thesis
├── HCC_V2.md                 # 20 campaigns with corrected scoring
├── MARITIME_NORWAY.md        # Maritime opportunities
├── MARITIME_CAMPAIGN_AKVA.md # AKVA B2B campaign
├── README.md                 # This file
├── campaigns/
│   ├── active/               # 25 active campaigns
│   └── stale/                # Archived campaigns
├── data/
│   └── dropcomp/             # Competitor intelligence
├── intelligence/             # Research reports
├── thesisTesting/            # Thesis experiments
├── archive/                  # Stale files
└── bigquery/                 # BigQuery schemas
```

---

## What's Next

1. Build Norwegian balcony-door hardware store (75 SKUs)
2. Set up Merchant Center feed
3. Launch Google Ads test
4. Measure what happens

---

## Git Repos

| Repo | Purpose |
|------|---------|
| prx0r/drop | This repo — campaigns and intelligence |
| prx0r/cg | CG judge worldpack |
| prx0r/cge | CGE proposer |
| prx0r/dropcomp | Competitor intelligence |
| prx0r/gitgoblin | Opportunity discovery |
