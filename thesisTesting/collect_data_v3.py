#!/usr/bin/env python3
"""
Roll the snowball around the garden - Phase 3.
Collect data for new theses.
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

def collect_thesis_data_v3(client, thesis_id):
    """Collect more specific data for a thesis."""
    data = {}
    
    # Service SKUs specific
    if thesis_id == "SERVICE_SKUS_005":
        data["service_products"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM products 
            WHERE LOWER(category) LIKE '%service%' OR LOWER(category) LIKE '%installation%'
        """)[0].get("count", 0)
        
        data["ev_products"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM products 
            WHERE LOWER(description) LIKE '%ev%' OR LOWER(description) LIKE '%charger%'
        """)[0].get("count", 0)
        
        data["service_categories"] = query_bigquery(client, """
            SELECT category, COUNT(*) as count 
            FROM products 
            WHERE LOWER(category) LIKE '%service%' OR LOWER(category) LIKE '%installation%'
            GROUP BY category 
            ORDER BY count DESC 
            LIMIT 10
        """)
    
    # API Virtualization specific
    elif thesis_id == "API_VIRTUALIZATION_006":
        data["api_signals"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM competition_signals 
            WHERE LOWER(type) LIKE '%api%' OR LOWER(type) LIKE '%integration%'
        """)[0].get("count", 0)
        
        data["integration_patterns"] = query_bigquery(client, """
            SELECT type, COUNT(*) as count 
            FROM competition_signals 
            GROUP BY type 
            ORDER BY count DESC 
            LIMIT 10
        """)
    
    # Installed-Base Graph specific
    elif thesis_id == "INSTALLED_BASE_GRAPH_007":
        data["installed_base_data"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM fact_series_installed_base
        """)[0].get("count", 0)
        
        data["ecosystem_data"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM fact_ecosystems
        """)[0].get("count", 0)
        
        data["household_patterns"] = query_bigquery(client, """
            SELECT category, COUNT(*) as count 
            FROM fact_series_installed_base 
            GROUP BY category 
            ORDER BY count DESC 
            LIMIT 10
        """)
    
    # Verification Trust Graph specific
    elif thesis_id == "VERIFICATION_TRUST_GRAPH_008":
        data["merchant_data"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM fact_merchants
        """)[0].get("count", 0)
        
        data["economic_outcomes"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM fact_economic_outcome
        """)[0].get("count", 0)
        
        data["merchant_metrics"] = query_bigquery(client, """
            SELECT category, COUNT(*) as count 
            FROM fact_merchants 
            GROUP BY category 
            ORDER BY count DESC 
            LIMIT 10
        """)
    
    # Grants Compliance specific
    elif thesis_id == "GRANTS_COMPLIANCE_009":
        data["policy_data"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM fact_policy_action
        """)[0].get("count", 0)
        
        data["policy_actions"] = query_bigquery(client, """
            SELECT action_type, COUNT(*) as count 
            FROM fact_policy_action 
            GROUP BY action_type 
            ORDER BY count DESC 
            LIMIT 10
        """)
    
    # Cross-cutting data
    data["graph_metrics"] = query_bigquery(client, """
        SELECT 
            COUNT(DISTINCT source) as unique_sources,
            COUNT(DISTINCT target) as unique_targets,
            COUNT(*) as total_edges
        FROM graph_edges
    """)[0] if True else {}
    
    return data

def main():
    client = get_client()
    
    thesis_files = [
        ("/root/drop/thesisTesting/05_service_skus.json", "SERVICE_SKUS_005"),
        ("/root/drop/thesisTesting/06_api_virtualization.json", "API_VIRTUALIZATION_006"),
        ("/root/drop/thesisTesting/07_installed_base_graph.json", "INSTALLED_BASE_GRAPH_007"),
        ("/root/drop/thesisTesting/08_verification_trust_graph.json", "VERIFICATION_TRUST_GRAPH_008"),
        ("/root/drop/thesisTesting/09_grants_compliance.json", "GRANTS_COMPLIANCE_009")
    ]
    
    for thesis_file, thesis_id in thesis_files:
        if os.path.exists(thesis_file):
            with open(thesis_file, 'r') as f:
                thesis = json.load(f)
            
            print(f"Collecting v3 data for {thesis_id}...")
            data = collect_thesis_data_v3(client, thesis_id)
            
            # Merge with existing data
            if "bigquery_data" in thesis:
                thesis["bigquery_data"].update(data)
            else:
                thesis["bigquery_data"] = data
            
            with open(thesis_file, 'w') as f:
                json.dump(thesis, f, indent=2)
            
            print(f"  Saved {len(data)} additional data points")

if __name__ == "__main__":
    main()
