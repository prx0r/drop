import { query } from '@/lib/bigquery';

export default async function Dashboard() {
  // Fetch data
  const countryData = await query(`
    SELECT country_code, data_type, COUNT(*) as cnt
    FROM drop.country_data
    GROUP BY country_code, data_type
    ORDER BY country_code, cnt DESC
  `);

  const graphStats = await query(`
    SELECT 
      (SELECT COUNT(*) FROM drop.country_graph_nodes) as nodes,
      (SELECT COUNT(*) FROM drop.country_graph_edges) as edges,
      (SELECT COUNT(*) FROM drop.fact_market_observation) as observations
  `);

  const mechanisms = await query(`
    SELECT 
      n1.node_id as mechanism_id,
      JSON_EXTRACT_SCALAR(n1.properties_json, '$.name') as name,
      e.target_node as country,
      e.weight
    FROM drop.country_graph_edges e
    JOIN drop.country_graph_nodes n1 ON e.source_node = n1.node_id
    WHERE n1.node_type = 'mechanism'
    AND e.edge_type = 'OBSERVED_IN'
    ORDER BY e.weight DESC
    LIMIT 10
  `);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-8">Drop Intelligence Dashboard</h1>
      
      {/* Stats */}
      <div className="grid grid-cols-4 gap-4 mb-8">
        {graphStats.map((stat: any) => (
          <div key="stats" className="bg-white p-6 rounded-lg shadow">
            <div className="text-2xl font-bold">{stat.nodes}</div>
            <div className="text-gray-500">Graph Nodes</div>
            <div className="text-2xl font-bold">{stat.edges}</div>
            <div className="text-gray-500">Graph Edges</div>
            <div className="text-2xl font-bold">{stat.observations}</div>
            <div className="text-gray-500">Observations</div>
          </div>
        ))}
      </div>

      {/* Country Data */}
      <div className="mb-8">
        <h2 className="text-xl font-semibold mb-4">Country Data</h2>
        <div className="bg-white rounded-lg shadow overflow-hidden">
          <table className="w-full">
            <thead>
              <tr className="bg-gray-50">
                <th className="px-4 py-2 text-left">Country</th>
                <th className="px-4 py-2 text-left">Data Type</th>
                <th className="px-4 py-2 text-right">Count</th>
              </tr>
            </thead>
            <tbody>
              {countryData.map((row: any, i: number) => (
                <tr key={i} className="border-t">
                  <td className="px-4 py-2">{row.country_code}</td>
                  <td className="px-4 py-2">{row.data_type}</td>
                  <td className="px-4 py-2 text-right">{row.cnt}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Mechanisms */}
      <div className="mb-8">
        <h2 className="text-xl font-semibold mb-4">Top Mechanisms</h2>
        <div className="bg-white rounded-lg shadow overflow-hidden">
          <table className="w-full">
            <thead>
              <tr className="bg-gray-50">
                <th className="px-4 py-2 text-left">Mechanism</th>
                <th className="px-4 py-2 text-left">Country</th>
                <th className="px-4 py-2 text-right">Weight</th>
              </tr>
            </thead>
            <tbody>
              {mechanisms.map((row: any, i: number) => (
                <tr key={i} className="border-t">
                  <td className="px-4 py-2">{row.name}</td>
                  <td className="px-4 py-2">{row.country}</td>
                  <td className="px-4 py-2 text-right">{row.weight}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Graph Stats */}
      <div className="mb-8">
        <h2 className="text-xl font-semibold mb-4">Knowledge Graph</h2>
        <div className="grid grid-cols-3 gap-4">
          {graphStats.map((stat: any) => (
            <div key="graph" className="bg-white p-4 rounded-lg shadow">
              <div className="text-lg font-bold">{stat.nodes} nodes</div>
              <div className="text-lg font-bold">{stat.edges} edges</div>
              <div className="text-lg font-bold">{stat.observations} observations</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
