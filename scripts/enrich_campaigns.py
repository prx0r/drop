#!/usr/bin/env python3
"""
Campaign Enrichment Engine — Query BigQuery for each campaign
"""

import json
import subprocess
from google.cloud import bigquery
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

def get_client():
    creds = Credentials(
        token=None,
        refresh_token=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_REFRESH_TOKEN', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_CLIENT_ID', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
        client_secret=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_CLIENT_SECRET', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
    )
    creds.refresh(Request())
    project = subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_CLOUD_PROJECT', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip()
    return bigquery.Client(project=project, credentials=creds)

def query_bigquery(client, query):
    try:
        result = client.query(query).result()
        return [dict(row) for row in result]
    except Exception as e:
        return [{"error": str(e)}]

def enrich_campaign(client, campaign_id, country_code):
    """Enrich a campaign with BigQuery data."""
    enrichment = {}
    
    # 1. Installed base
    enrichment["installed_base"] = query_bigquery(client, f"""
        SELECT ecosystem, metric_value, unit, source
        FROM drop.fact_series_installed_base
        WHERE country_code = '{country_code}'
        ORDER BY metric_value DESC
        LIMIT 10
    """)
    
    # 2. Products
    enrichment["products"] = query_bigquery(client, f"""
        SELECT product_family, brand, category
        FROM drop.dim_product
        LIMIT 50
    """)
    
    # 3. Competition signals
    enrichment["competition"] = query_bigquery(client, f"""
        SELECT product_id, country_code, shopping_seller_count, good_seller_count, median_merchant_quality
        FROM drop.competition_signals
        WHERE country_code = '{country_code}'
        LIMIT 20
    """)
    
    # 4. Demand signals
    enrichment["demand"] = query_bigquery(client, f"""
        SELECT product_id, country_code, keyword_volume, keyword_growth_3m
        FROM drop.demand_signals
        WHERE country_code = '{country_code}'
        LIMIT 20
    """)
    
    # 5. Market observations
    enrichment["market"] = query_bigquery(client, f"""
        SELECT entity_type, entity_id, field_name, field_value
        FROM drop.fact_market_observation
        LIMIT 20
    """)
    
    # 6. Graph relationships
    enrichment["graph"] = query_bigquery(client, f"""
        SELECT source_node, target_node, edge_type, weight
        FROM drop.graph_edges
        LIMIT 50
    """)
    
    return enrichment

def main():
    client = get_client()
    
    # Enrich Norway campaigns
    campaigns = [
        ("HCC-NOR-BALCONY-001", "NO"),
        ("HCC-NOR-WALLAS-001", "NO"),
        ("HCC-NOR-CABIN-WATER-001", "NO"),
    ]
    
    for campaign_id, country_code in campaigns:
        print(f"\nEnriching {campaign_id}...")
        enrichment = enrich_campaign(client, campaign_id, country_code)
        
        # Save to file
        filename = f"/root/drop/data/enrichment_{campaign_id}.json"
        with open(filename, 'w') as f:
            json.dump(enrichment, f, indent=2, default=str)
        
        print(f"  Installed base: {len(enrichment.get('installed_base', []))} rows")
        print(f"  Products: {len(enrichment.get('products', []))} rows")
        print(f"  Competition: {len(enrichment.get('competition', []))} rows")
        print(f"  Demand: {len(enrichment.get('demand', []))} rows")
        print(f"  Market: {len(enrichment.get('market', []))} rows")
        print(f"  Graph: {len(enrichment.get('graph', []))} rows")

if __name__ == "__main__":
    main()
