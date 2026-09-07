import { BigQuery } from '@google-cloud/bigquery';

const bigquery = new BigQuery({
  projectId: process.env.GCP_PROJECT_ID || 'project-ff2366d2-8fda-4fcb-9ba',
});

export async function query(sql: string) {
  const [rows] = await bigquery.query(sql);
  return rows;
}

export async function getCountryData() {
  return query(`
    SELECT country_code, data_type, COUNT(*) as cnt
    FROM drop.country_data
    GROUP BY country_code, data_type
    ORDER BY country_code, cnt DESC
  `);
}

export async function getGraphNodes() {
  return query(`
    SELECT node_id, node_type, properties_json
    FROM drop.country_graph_nodes
    LIMIT 50
  `);
}

export async function getGraphEdges() {
  return query(`
    SELECT source_node, target_node, edge_type, weight
    FROM drop.country_graph_edges
    LIMIT 100
  `);
}

export async function getObservations() {
  return query(`
    SELECT observation_id, country_code, field_name, field_value, source_grade
    FROM drop.fact_market_observation
    ORDER BY observed_at DESC
    LIMIT 50
  `);
}

export async function getMechanisms() {
  return query(`
    SELECT 
      n1.node_id as mechanism_id,
      JSON_EXTRACT_SCALAR(n1.properties_json, '$.name') as mechanism_name,
      e.target_node as country,
      e.weight
    FROM drop.country_graph_edges e
    JOIN drop.country_graph_nodes n1 ON e.source_node = n1.node_id
    WHERE n1.node_type = 'mechanism'
    AND e.edge_type = 'OBSERVED_IN'
    ORDER BY e.weight DESC
  `);
}
