# Drop — Ecommerce Intelligence Platform

A monorepo for building evidence-selected, low-capital specialist ecommerce stores.

## Structure

```
drop/
├── apps/
│   ├── store/              # WooCommerce storefront
│   └── dashboard/          # Operator dashboard
├── services/
│   ├── research/           # Opportunity research engine
│   ├── catalog/            # Product catalog management
│   ├── supplier/           # Supplier integration
│   ├── merchant/           # Google Merchant API
│   ├── google-ads/         # Google Ads management
│   ├── analytics/          # Analytics & reporting
│   ├── merch-intel/        # Google Merch Intel (cloned)
│   ├── feedgen/            # Feed optimization (cloned)
│   ├── feedx/              # Experimental design (cloned)
│   ├── pretzel-feed/       # Feed automation example
│   ├── dropshipping-intel/ # Intelligence tools
│   └── profit-calc/        # Profit calculator
├── packages/
│   ├── economics/          # Economic models
│   ├── schemas/            # Data schemas
│   └── scoring/            # Scoring algorithms
├── corpus/
│   ├── strategies/         # Dev plan, millions docs
│   ├── case-studies/       # 12 enriched case studies
│   ├── sources/            # 52 sources with grades
│   ├── schemas/            # Data schemas
│   └── data/               # Strategy rules
├── data/
│   ├── raw/                # Raw data
│   ├── normalized/         # Cleaned data
│   └── snapshots/          # Point-in-time snapshots
├── infra/                  # Docker, nginx, backups
└── docs/                   # Documentation
```

## Key Repos Cloned

| Repo | Purpose |
|------|---------|
| merch-intel | Google Merchant Intelligence |
| feedgen | Feed optimization with AI |
| feedx | Experimental design toolkit |
| pretzel-feed | Feed automation example |
| dropshipping-intel | Intelligence tools |
| profit-calc | Profit calculator |

## Corpus

- 12 case studies (ZenoX, Robtronic, Johnny FD, etc.)
- 52 sources with evidence grades
- 16 strategy rules
- 6 data schemas
- Dev plan (2110 lines)

## Dev Plan

Read `corpus/strategies/dev-plan.md` for the master plan.

Core loop:
1. Search-demand first
2. Join demand to economics
3. Launch one market, lean catalog
4. Exploit free surfaces first
5. $0-10/day as probe only
6. Score contribution profit per click

## Next Steps

1. Set up PostgreSQL on VPS
2. Build opportunity research engine
3. Score candidate products
4. Launch first experiment
5. Iterate based on evidence
