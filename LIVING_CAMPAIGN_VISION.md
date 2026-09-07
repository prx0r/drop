# The Living Campaign — Production Line Vision

*Generated: 2026-09-07*
*Status: VISION — From schema to production line*

---

## The Concept

A campaign is not a static JSON file. It is a **living organism** that:

1. Gets created from research
2. Gets validated against a rubric
3. Gets enriched with go-to-market data
4. Gets tested with real ads
5. Gets mutated based on results
6. Gets cloned into new niches

The schema is the spine. BigQuery is the blood. GitGoblin is the nervous system. The ads are the muscle.

---

## The Production Line

```
STAGE 1: SEED
  Research → Campaign JSON → Binary Gate → Score Rubric
  Output: VALIDATED CAMPAIGN

STAGE 2: ENRICH
  BigQuery data → Go-to-market stats → Ad strategy → Supplier economics
  Output: ENRICHED CAMPAIGN

STAGE 3: BUILD
  Merchant Center feed → Shopify store → Landing pages → Agent-readable PDP
  Output: LIVE STORE

STAGE 4: TEST
  Google Ads → Free listings → Agent queries → Search terms
  Output: TRAFFIC DATA

STAGE 5: LEARN
  Search terms → New edges → New aliases → New Q&A → Graph improves
  Output: MUTATED CAMPAIGN

STAGE 6: SCALE
  Clone to new niches → New countries → New installed bases
  Output: PORTFOLIO
```

---

## Stage 2: Enrichment (What BigQuery Provides)

### For each campaign, query:

```sql
-- Installed base by country
SELECT ecosystem, installed_base, growth_rate, replacement_pressure
FROM drop.fact_series_installed_base
WHERE country_code = 'NO'

-- Products in category
SELECT product_family, brand, category, eco_system
FROM drop.dim_product
WHERE country_code = 'NO'

-- Competitor signals
SELECT * FROM drop.competition_signals
WHERE sector = 'agent_commerce'

-- Demand signals
SELECT * FROM drop.demand_signals
WHERE country = 'NO'

-- Market observations
SELECT * FROM drop.fact_market_observation
WHERE country_code = 'NO'

-- Graph relationships
SELECT * FROM drop.graph_edges
WHERE source LIKE '%NO%' OR target LIKE '%NO%'
```

### Enrichment adds:

```json
{
  "enrichment": {
    "market_size": {
      "installed_base": 483150,
      "replacement_rate": "2%/year",
      "source": "SSB"
    },
    "competitor_landscape": {
      "total_sellers": 5,
      "good_specialists": 2,
      "best_specialist_score": 7,
      "gap_exists": true
    },
    "demand_surface": {
      "native_queries": ["hva slags pumpe passer til min hytte?"],
      "search_volume": "UNKNOWN",
      "cpc": "UNKNOWN"
    },
    "supplier_economics": {
      "net_price": "UNKNOWN",
      "margin": "UNKNOWN",
      "shipping": "UNKNOWN"
    }
  }
}
```

---

## Stage 2: Ad Strategy (What to Run and Why)

### For each campaign, generate:

```json
{
  "ad_strategy": {
    "channels": [
      {
        "channel": "google_search",
        "budget": "EUR 10/day",
        "keywords": ["[brand] [model] deler", "[brand] [model] erstatning"],
        "match_type": "exact_phrase",
        "ad_group": "compatibility_replacement",
        "negative_keywords": ["service", "reparasjon", "installasjon"]
      },
      {
        "channel": "google_shopping",
        "budget": "EUR 5/day",
        "campaign_type": "standard_shopping",
        "product_filter": "only verified SKUs"
      },
      {
        "channel": "free_listings",
        "budget": "EUR 0",
        "merchant_center": true
      }
    ],
    "testing_plan": {
      "week_1": "Free listings only, measure impressions",
      "week_2": "Add exact/phrase Search, measure CTR",
      "week_3": "Add Shopping, measure CVR",
      "week_4": "Optimize based on search terms"
    }
  }
}
```

### Ad strategy rules:

1. **Never start with PMax** — use Standard Shopping + Search
2. **Test in native language** — Norwegian for Norway, Finnish for Finland
3. **Start with exact/phrase** — not broad
4. **Mine search terms** — every term becomes a graph edge
5. **Build negatives aggressively** — exclude non-commercial queries
6. **Budget from contribution** — not arbitrary

---

## Stage 3: Build (What Gets Created)

### For each campaign, generate:

```json
{
  "build_assets": {
    "merchant_center_feed": {
      "products": 75,
      "fields": ["brand", "mpn", "gtin", "product_detail", "question_and_answer", "document_link", "related_product", "images"],
      "status": "pending"
    },
    "shopify_store": {
      "products": 75,
      "metafields": ["compatibility", "supersession", "installation_notes"],
      "catalog_mapping": true,
      "status": "pending"
    },
    "landing_pages": {
      "model_pages": 15,
      "compatibility_pages": 75,
      "faq_pages": 10,
      "status": "pending"
    },
    "visual_corpus": {
      "product_images": 750,
      "type_plate_examples": 150,
      "connector_photos": 150,
      "status": "pending"
    }
  }
}
```

---

## Stage 4: Test (What Gets Measured)

### For each campaign, track:

```json
{
  "test_results": {
    "free_listings": {
      "impressions": 0,
      "clicks": 0,
      "ctr": 0,
      "status": "pending"
    },
    "search_ads": {
      "impressions": 0,
      "clicks": 0,
      "ctr": 0,
      "cpc": 0,
      "conversions": 0,
      "status": "pending"
    },
    "shopping_ads": {
      "impressions": 0,
      "clicks": 0,
      "ctr": 0,
      "cpc": 0,
      "conversions": 0,
      "status": "pending"
    },
    "agent_queries": {
      "queries_tested": 0,
      "correct_recommendations": 0,
      "our_entity_retrieved": 0,
      "status": "pending"
    }
  }
}
```

---

## Stage 5: Learn (What Gets Mutated)

### For each campaign, from test results:

```json
{
  "mutations": [
    {
      "field": "compatibility_graph.edges",
      "old_value": 75,
      "new_value": 85,
      "reason": "Search terms revealed 10 new compatibility edges",
      "source": "google_ads_search_terms"
    },
    {
      "field": "demand_surface.native_queries",
      "old_value": 5,
      "new_value": 15,
      "reason": "Search terms revealed 10 new query patterns",
      "source": "google_ads_search_terms"
    }
  ]
}
```

---

## Stage 6: Scale (Portfolio Growth)

### Track portfolio metrics:

```json
{
  "portfolio": {
    "total_campaigns": 20,
    "status_breakdown": {
      "ATTACK": 6,
      "VERIFY": 8,
      "WATCH": 4,
      "REJECT": 2
    },
    "total_skus": 1500,
    "total_revenue": 0,
    "total_orders": 0,
    "avg_margin": "UNKNOWN",
    "countries": ["NO", "FI", "SE", "DK", "DE"]
  }
}
```

---

## The Key Insight

The schema is not the product.

The **production line** is the product.

Each campaign is a unit in the production line. The production line:
1. Takes research as input
2. Validates against rubric
3. Enriches with data
4. Builds assets
5. Tests with real traffic
6. Learns from results
7. Mutates to improve
8. Clones to new niches

That is a repeatable company.
