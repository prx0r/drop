# Drop Data Architecture — BigQuery Graph + Knowledge Graph

*Source: Research into graph databases, knowledge graphs, product KGs, BigQuery Graph GA.*
*Generated: 2026-09-08T03:00:00Z*
*Classification: System architecture — data model for scale*

---

## The Key Discovery: BigQuery Graph (GA September 2026)

Google just moved BigQuery Graph to general availability. It supports:
- **ISO-standard GQL** (Graph Query Language) alongside SQL
- **Native graph traversals** without ETL to a separate database
- **Nodes + edges** modeled directly in BigQuery
- **Combined relational + graph** on a single source of truth

This means we don't need Neo4j, TigerGraph, or any separate graph database. BigQuery is both our warehouse AND our graph.

---

## The Data Model

### Node Types

```text
Country          → {code, name, currency, language, ecommerce_penetration, cross_border_rate}
Ecosystem        → {ecosystem_id, system_type, installed_base, growth_rate, replacement_share}
Product          → {product_id, brand, model, mpn, gtin, category, price_band}
Merchant         → {merchant_id, domain, country, quality_score, specialization}
Supplier         → {supplier_id, name, country, products, dropship, moq}
InstalledBase    → {ecosystem_id, country, value, stock_definition, date}
Problem          → {problem_id, ecosystem, trigger, urgency, seasonality}
Observation      → {observed_at, product_id, country, seller_count, prices}
ProbeStore       → {store_id, candidate_id, hypothesis, started_at}
Outcome          → {store_id, impressions, clicks, conversions, revenue, profit}
Hypothesis       → {hypothesis_id, statement, metric, target, status}
GoldPattern      → {pattern_id, description, evidence, confidence}
```

### Edge Types

```text
Country -[HAS_ECOSYSTEM]-> Ecosystem
Ecosystem -[HAS_INSTALLED_BASE]-> InstalledBase
Ecosystem -[HAS_PROBLEMS]-> Problem
Product -[SOLD_IN]-> Country
Product -[SOLD_BY]-> Merchant
Merchant -[LOCATED_IN]-> Country
Merchant -[QUALITY_SCORED_BY]-> Observation
Supplier -[SUPPLIES_TO]-> Product
Supplier -[OPERATES_IN]-> Country
InstalledBase -[AGES_INTO]-> Problem
Problem -[TRIGGERS]-> SearchQuery
SearchQuery -[LEADS_TO]-> ProbeStore
ProbeStore -[PRODUCES]-> Outcome
Outcome -[VALIDATES]-> Hypothesis
Hypothesis -[SUPPORTS]-> GoldPattern
SourceMarket -[ORACLE_FOR]-> TargetMarket
```

---

## The Queries That Matter

### Discovery Query
```gql
MATCH (c:Country)-[:HAS_ECOSYSTEM]->(e:Ecosystem)
      -[r:HAS_INSTALLED_BASE]->(ib:InstalledBase)
WHERE ib.value > 100000
  AND e.growth_rate > 0.3
RETURN c.code, e.system_type, ib.value, e.growth_rate
ORDER BY ib.value * e.growth_rate DESC
LIMIT 20
```

### Gap Detection Query
```gql
MATCH (sm:Country)-[:ORACLE_FOR]->(tm:Country)
      (sm)<-[:LOCATED_IN]-(src_m:Merchant)-[:QUALITY_SCORED_BY]->(src_o:Observation),
      (tm)<-[:LOCATED_IN]-(tgt_m:Merchant)-[:QUALITY_SCORED_BY]->(tgt_o:Observation)
WHERE src_o.quality_score >= 70
  AND tgt_o.quality_score < 40
RETURN sm.code, tm.code, src_m.domain, tgt_m.domain, src_o.quality_score, tgt_o.quality_score
```

### Installed-Base Growth Query
```gql
MATCH (e:Ecosystem)-[:HAS_INSTALLED_BASE]->(ib1:InstalledBase)
      (e)-[:HAS_INSTALLED_BASE]->(ib2:InstalledBase)
WHERE ib1.date = '2025-01-01'
  AND ib2.date = '2026-01-01'
RETURN e.ecosystem_id, ib1.value, ib2.value, 
       (ib2.value - ib1.value) / ib1.value AS growth_rate
ORDER BY growth_rate DESC
```

---

## Why This Architecture Works

1. **Single source of truth** — no data silos between graph and relational
2. **GQL + SQL** — use graph for traversal, SQL for aggregation
3. **Native time-series** — BigQuery partitions by date, clustering by country/product
4. **Scalable** — petabyte-scale, serverless, no infrastructure management
5. **Cost-effective** — 1 TiB query free/month, 10 GiB storage free
6. **AI-ready** — BigQuery ML + conversational analytics on the same data

---

## The Asset We're Building

Not stores. Not reports. Not code.

> **A longitudinal knowledge graph connecting what populations own, how those populations change, what goes wrong, what people search, what mature markets sell, which solutions are underserved locally, and what happened when we tested commerce against those gaps.**

That's the moat. The stores are just experiments emitted by the graph.
