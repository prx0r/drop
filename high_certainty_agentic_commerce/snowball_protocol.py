#!/usr/bin/env python3
"""
Snowball Protocol — Run High-Certainty Agentic Commerce analysis for each country.
Query BigQuery for installed base, ecosystems, merchants, gaps.
"""

from google.cloud import bigquery
import subprocess
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import json
import os

def get_client():
    creds = Credentials(
        token=None,
        refresh_token=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_REFRESH_TOKEN', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_CLIENT_ID', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
        client_secret=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_CLIENT_SECRET', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
    )
    creds.refresh(Request())
    return bigquery.Client(project=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_CLOUD_PROJECT', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(), credentials=creds)

def query_bigquery(client, query):
    try:
        result = client.query(query).result()
        return [dict(row) for row in result]
    except Exception as e:
        return [{"error": str(e)}]

def collect_country_data(client, country_code):
    """Collect all available data for a country."""
    data = {}
    
    # Country data from country_data table (parse data_json)
    raw_country_data = query_bigquery(client, f"""
        SELECT data_type, data_json
        FROM drop.country_data
        WHERE country_code = '{country_code}'
        LIMIT 100
    """)
    
    # Group by data_type
    data_by_type = {}
    for row in raw_country_data:
        data_type = row.get('data_type', 'unknown')
        data_json = json.loads(row.get('data_json', '{}'))
        if data_type not in data_by_type:
            data_by_type[data_type] = []
        data_by_type[data_type].append(data_json)
    
    data["country_data"] = data_by_type
    
    # Installed base
    data["installed_base"] = query_bigquery(client, f"""
        SELECT * FROM drop.fact_series_installed_base
        WHERE country_code = '{country_code}'
        AND installed_base > 0
        ORDER BY installed_base DESC
        LIMIT 20
    """)
    
    # Ecosystems
    data["ecosystems"] = query_bigquery(client, f"""
        SELECT * FROM drop.dim_ecosystem
        WHERE country_code = '{country_code}'
        ORDER BY installed_base DESC
        LIMIT 20
    """)
    
    # Merchants
    data["merchants"] = query_bigquery(client, f"""
        SELECT * FROM drop.dim_merchant
        WHERE country_code = '{country_code}'
        ORDER BY quality_score DESC
        LIMIT 20
    """)
    
    # Products
    data["products"] = query_bigquery(client, f"""
        SELECT * FROM drop.dim_product
        WHERE country_code = '{country_code}'
        LIMIT 50
    """)
    
    # Graph nodes
    data["graph_nodes"] = query_bigquery(client, f"""
        SELECT node_type, node_id, properties_json
        FROM drop.graph_nodes
        WHERE node_id LIKE '%{country_code}%'
        LIMIT 50
    """)
    
    return data

def main():
    client = get_client()
    
    countries = ['NO', 'FI', 'SE', 'DK', 'DE', 'GB', 'CH', 'US']
    
    for country_code in countries:
        print(f"\n{'='*60}")
        print(f"Processing {country_code}...")
        print(f"{'='*60}")
        
        data = collect_country_data(client, country_code)
        
        # Save to country folder
        output_file = f"/root/drop/high_certainty_agentic_commerce/countries/{country_code}/bigquery_data.json"
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        # Print summary
        print(f"  Country data types: {list(data.get('country_data', {}).keys())}")
        for data_type, items in data.get('country_data', {}).items():
            print(f"    {data_type}: {len(items)} rows")
        print(f"  Installed base: {len(data.get('installed_base', []))} rows")
        print(f"  Ecosystems: {len(data.get('ecosystems', []))} rows")
        print(f"  Merchants: {len(data.get('merchants', []))} rows")
        print(f"  Products: {len(data.get('products', []))} rows")
        print(f"  Graph nodes: {len(data.get('graph_nodes', []))} rows")
        
        # Print segments
        segments = data.get('country_data', {}).get('segments', [])
        if segments:
            print(f"\n  Segments:")
            for seg in segments[:5]:
                print(f"    {seg.get('segment_id', 'N/A')}: {seg.get('name', 'N/A')}")
                print(f"      Thesis: {seg.get('thesis', 'N/A')[:100]}")
        
        # Print hypotheses
        hypotheses = data.get('country_data', {}).get('hypotheses', [])
        if hypotheses:
            print(f"\n  Hypotheses:")
            for hyp in hypotheses[:5]:
                print(f"    {hyp.get('hypothesis_id', 'N/A')}: {hyp.get('statement', 'N/A')[:100]}")
        
        # Print ecosystems
        ecosystems = data.get('country_data', {}).get('ecosystems', [])
        if ecosystems:
            print(f"\n  Ecosystems:")
            for eco in ecosystems[:5]:
                print(f"    {eco.get('ecosystem_id', 'N/A')}: {eco.get('name', 'N/A')}")
                print(f"      Installed base: {eco.get('installed_base', 'N/A')}")

if __name__ == "__main__":
    main()
