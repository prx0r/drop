# BigQuery Graph Queries — Drop Commerce Intelligence

*These queries use BigQuery Graph (GA September 2026) with GQL + SQL.*
*Run against: project-ff2366d2-8fda-4fcb-9ba.drop*

---

## Query 1: Find All Ecosystems by Installed Base

```sql
-- Which ecosystems have the largest installed bases?
SELECT 
  node_id,
  JSON_EXTRACT_SCALAR(properties_json, '$.system') as system,
  JSON_EXTRACT_SCALAR(properties_json, '$.country') as country,
  CAST(JSON_EXTRACT_SCALAR(properties_json, '$.installed_base') AS INT64) as installed_base,
  CAST(JSON_EXTRACT_SCALAR(properties_json, '$.growth_rate') AS FLOAT64) as growth_rate,
  confidence
FROM `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes`
WHERE node_type = 'ecosystem'
ORDER BY CAST(JSON_EXTRACT_SCALAR(properties_json, '$.installed_base') AS INT64) DESC
```

## Query 2: Find Growth Opportunities (High Installed Base × High Growth)

```sql
-- Which ecosystems are growing fastest with large installed bases?
SELECT 
  node_id,
  JSON_EXTRACT_SCALAR(properties_json, '$.system') as system,
  JSON_EXTRACT_SCALAR(properties_json, '$.country') as country,
  CAST(JSON_EXTRACT_SCALAR(properties_json, '$.installed_base') AS INT64) as installed_base,
  CAST(JSON_EXTRACT_SCALAR(properties_json, '$.growth_rate') AS FLOAT64) as growth_rate,
  CAST(JSON_EXTRACT_SCALAR(properties_json, '$.installed_base') AS INT64) * 
    CAST(JSON_EXTRACT_SCALAR(properties_json, '$.growth_rate') AS FLOAT64) as growth_signal
FROM `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes`
WHERE node_type = 'ecosystem'
ORDER BY growth_signal DESC
```

## Query 3: Find Source → Target Oracle Relationships

```sql
-- Which countries can serve as oracles for which targets?
SELECT 
  src.properties_json as source_country,
  tgt.properties_json as target_country,
  e.weight as oracle_strength
FROM `project-ff2366d2-8fda-4fcb-9ba.drop.graph_edges` e
JOIN `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes` src ON e.source_node = src.node_id
JOIN `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes` tgt ON e.target_node = tgt.node_id
WHERE e.edge_type = 'ORACLE_FOR'
ORDER BY e.weight DESC
```

## Query 4: Find Ecosystems with Most Problems

```sql
-- Which ecosystems have the most problems?
SELECT 
  e.node_id,
  JSON_EXTRACT_SCALAR(e.properties_json, '$.system') as system,
  JSON_EXTRACT_SCALAR(e.properties_json, '$.country') as country,
  COUNT(p.node_id) as problem_count,
  SUM(CASE WHEN JSON_EXTRACT_SCALAR(p.properties_json, '$.urgency') = 'critical' THEN 1 ELSE 0 END) as critical_problems
FROM `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes` e
JOIN `project-ff2366d2-8fda-4fcb-9ba.drop.graph_edges` ed ON e.node_id = ed.source_node
JOIN `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes` p ON ed.target_node = p.node_id
WHERE e.node_type = 'ecosystem' AND ed.edge_type = 'HAS_PROBLEMS'
GROUP BY e.node_id, e.properties_json
ORDER BY problem_count DESC, critical_problems DESC
```

## Query 5: Merchant Quality by Country

```sql
-- Average merchant quality score by country
SELECT 
  JSON_EXTRACT_SCALAR(m.properties_json, '$.country') as country,
  COUNT(*) as merchant_count,
  AVG(CAST(JSON_EXTRACT_SCALAR(m.properties_json, '$.quality_score') AS FLOAT64)) as avg_quality,
  MIN(CAST(JSON_EXTRACT_SCALAR(m.properties_json, '$.quality_score') AS FLOAT64)) as min_quality,
  MAX(CAST(JSON_EXTRACT_SCALAR(m.properties_json, '$.quality_score') AS FLOAT64)) as max_quality
FROM `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes` m
WHERE m.node_type = 'merchant'
GROUP BY country
ORDER BY avg_quality DESC
```

## Query 6: Installed Base Growth Over Time

```sql
-- Track installed base changes over time
SELECT 
  o.node_id,
  JSON_EXTRACT_SCALAR(n.properties_json, '$.system') as system,
  o.observed_at,
  o.metric_name,
  o.metric_value,
  o.evidence_type,
  o.source
FROM `project-ff2366d2-8fda-4fcb-9ba.drop.graph_observations` o
JOIN `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes` n ON o.node_id = n.node_id
WHERE o.metric_name = 'installed_base'
ORDER BY o.observed_at DESC
```

## Query 7: Find Countries with Weak Merchants + Strong Ecosystems

```sql
-- Target countries where ecosystem demand exceeds merchant supply
SELECT 
  c.node_id as country,
  JSON_EXTRACT_SCALAR(c.properties_json, '$.name') as country_name,
  e.node_id as ecosystem,
  JSON_EXTRACT_SCALAR(e.properties_json, '$.system') as system,
  CAST(JSON_EXTRACT_SCALAR(e.properties_json, '$.installed_base') AS INT64) as installed_base,
  CAST(JSON_EXTRACT_SCALAR(e.properties_json, '$.growth_rate') AS FLOAT64) as growth_rate,
  (SELECT COUNT(*) FROM `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes` m 
   WHERE m.node_type = 'merchant' 
   AND JSON_EXTRACT_SCALAR(m.properties_json, '$.country') = JSON_EXTRACT_SCALAR(c.properties_json, '$.code')
   AND CAST(JSON_EXTRACT_SCALAR(m.properties_json, '$.quality_score') AS FLOAT64) >= 70) as good_merchants
FROM `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes` c
JOIN `project-ff2366d2-8fda-4fcb-9ba.drop.graph_edges` e ON c.node_id = e.source_node
WHERE c.node_type = 'country' AND e.edge_type = 'HAS_ECOSYSTEM'
HAVING good_merchants < 3
ORDER BY installed_base * growth_rate DESC
```

## Query 8: Cross-Country Gap Analysis

```sql
-- Compare same ecosystem across countries
SELECT 
  e1.node_id as ecosystem,
  JSON_EXTRACT_SCALAR(e1.properties_json, '$.country') as country1,
  CAST(JSON_EXTRACT_SCALAR(e1.properties_json, '$.installed_base') AS INT64) as base1,
  JSON_EXTRACT_SCALAR(e2.properties_json, '$.country') as country2,
  CAST(JSON_EXTRACT_SCALAR(e2.properties_json, '$.installed_base') AS INT64) as base2,
  ABS(CAST(JSON_EXTRACT_SCALAR(e1.properties_json, '$.installed_base') AS INT64) - 
      CAST(JSON_EXTRACT_SCALAR(e2.properties_json, '$.installed_base') AS INT64)) as gap
FROM `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes` e1
JOIN `project-ff2366d2-8fda-4fcb-9ba.drop.graph_nodes` e2 
  ON JSON_EXTRACT_SCALAR(e1.properties_json, '$.system') = JSON_EXTRACT_SCALAR(e2.properties_json, '$.system')
  AND e1.node_id < e2.node_id
WHERE e1.node_type = 'ecosystem' AND e2.node_type = 'ecosystem'
ORDER BY gap DESC
```
