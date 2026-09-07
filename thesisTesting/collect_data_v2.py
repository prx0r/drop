#!/usr/bin/env python3
"""
Roll the snowball around the garden - Phase 2.
More specific queries for each thesis.
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

def collect_thesis_data_v2(client, thesis_id):
    """Collect more specific data for a thesis."""
    data = {}
    
    # Agentic Broker specific
    if thesis_id == "AGENTIC_BROKER_001":
        data["ev_installers"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM case_studies 
            WHERE LOWER(description) LIKE '%ev%' OR LOWER(description) LIKE '%charger%'
        """)[0].get("count", 0)
        
        data["service_providers"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM case_studies 
            WHERE LOWER(description) LIKE '%installer%' OR LOWER(description) LIKE '%electrician%'
        """)[0].get("count", 0)
        
        data["uk_market"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM case_studies 
            WHERE LOWER(country) = 'uk' OR LOWER(country) = 'united kingdom'
        """)[0].get("count", 0)
        
        data["demand_by_category"] = query_bigquery(client, """
            SELECT category, COUNT(*) as count 
            FROM demand_signals 
            GROUP BY category 
            ORDER BY count DESC 
            LIMIT 10
        """)
    
    # Compatibility Dropship specific
    elif thesis_id == "COMPATIBILITY_DROPSHIP_002":
        data["products_with_compatibility"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM products 
            WHERE LOWER(description) LIKE '%compatible%' OR LOWER(description) LIKE '%replacement%'
        """)[0].get("count", 0)
        
        data["appliance_parts"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM products 
            WHERE LOWER(category) LIKE '%part%' OR LOWER(category) LIKE '%spare%'
        """)[0].get("count", 0)
        
        data["product_categories"] = query_bigquery(client, """
            SELECT category, COUNT(*) as count 
            FROM products 
            GROUP BY category 
            ORDER BY count DESC 
            LIMIT 10
        """)
        
        data["competition_by_type"] = query_bigquery(client, """
            SELECT type, COUNT(*) as count 
            FROM competition_signals 
            GROUP BY type 
            ORDER BY count DESC 
            LIMIT 10
        """)
    
    # Photo-to-PO specific
    elif thesis_id == "PHOTO_TO_PO_003":
        data["wholesale_distributors"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM case_studies 
            WHERE LOWER(description) LIKE '%wholesale%' OR LOWER(description) LIKE '%distributor%'
        """)[0].get("count", 0)
        
        data["trade_suppliers"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM case_studies 
            WHERE LOWER(description) LIKE '%screwfix%' OR LOWER(description) LIKE '%trade%'
        """)[0].get("count", 0)
        
        data["procurement_patterns"] = query_bigquery(client, """
            SELECT signal_type, COUNT(*) as count 
            FROM supply_signals 
            GROUP BY signal_type 
            ORDER BY count DESC 
            LIMIT 10
        """)
    
    # Supplier OS specific
    elif thesis_id == "SUPPLIER_OS_004":
        data["contractors"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM case_studies 
            WHERE LOWER(description) LIKE '%contractor%' OR LOWER(description) LIKE '% tradesman%'
        """)[0].get("count", 0)
        
        data["ai_receptionist"] = query_bigquery(client, """
            SELECT COUNT(*) as count 
            FROM case_studies 
            WHERE LOWER(description) LIKE '%receptionist%' OR LOWER(description) LIKE '%ai%'
        """)[0].get("count", 0)
        
        data["service_categories"] = query_bigquery(client, """
            SELECT category, COUNT(*) as count 
            FROM demand_signals 
            GROUP BY category 
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
    
    data["probe_insights"] = query_bigquery(client, """
        SELECT insight_type, COUNT(*) as count 
        FROM probe_reports 
        GROUP BY insight_type 
        ORDER BY count DESC 
        LIMIT 5
    """)
    
    return data

def main():
    client = get_client()
    
    thesis_files = [
        ("/root/drop/thesisTesting/01_agentic_broker.json", "AGENTIC_BROKER_001"),
        ("/root/drop/thesisTesting/02_compatibility_dropship.json", "COMPATIBILITY_DROPSHIP_002"),
        ("/root/drop/thesisTesting/03_photo_to_po.json", "PHOTO_TO_PO_003"),
        ("/root/drop/thesisTesting/04_supplier_os.json", "SUPPLIER_OS_004")
    ]
    
    for thesis_file, thesis_id in thesis_files:
        if os.path.exists(thesis_file):
            with open(thesis_file, 'r') as f:
                thesis = json.load(f)
            
            print(f"Collecting v2 data for {thesis_id}...")
            data = collect_thesis_data_v2(client, thesis_id)
            
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
