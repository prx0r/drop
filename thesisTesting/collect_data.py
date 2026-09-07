#!/usr/bin/env python3
"""
Roll the snowball around the garden.
Query BigQuery for each thesis and attach supporting/refuting data.
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

def collect_thesis_data(client, thesis_id):
    """Collect data for a specific thesis from BigQuery."""
    data = {}
    
    # General statistics
    data["total_case_studies"] = query_bigquery(client, "SELECT COUNT(*) as count FROM case_studies")[0].get("count", 0)
    data["total_products"] = query_bigquery(client, "SELECT COUNT(*) as count FROM products")[0].get("count", 0)
    data["total_demand_signals"] = query_bigquery(client, "SELECT COUNT(*) as count FROM demand_signals")[0].get("count", 0)
    data["total_competition_signals"] = query_bigquery(client, "SELECT COUNT(*) as count FROM competition_signals")[0].get("count", 0)
    
    # Country-specific data
    data["countries"] = query_bigquery(client, "SELECT DISTINCT country FROM country_data LIMIT 10")
    
    # Graph data
    data["graph_nodes"] = query_bigquery(client, "SELECT COUNT(*) as count FROM graph_nodes")[0].get("count", 0)
    data["graph_edges"] = query_bigquery(client, "SELECT COUNT(*) as count FROM graph_edges")[0].get("count", 0)
    
    # Probes
    data["probe_reports"] = query_bigquery(client, "SELECT COUNT(*) as count FROM probe_reports")[0].get("count", 0)
    
    # Economics
    data["economics_signals"] = query_bigquery(client, "SELECT COUNT(*) as count FROM economics_signals")[0].get("count", 0)
    
    return data

def main():
    client = get_client()
    
    # Load existing thesis files
    thesis_files = [
        "/root/drop/thesisTesting/01_agentic_broker.json",
        "/root/drop/thesisTesting/02_compatibility_dropship.json",
        "/root/drop/thesisTesting/03_photo_to_po.json",
        "/root/drop/thesisTesting/04_supplier_os.json"
    ]
    
    for thesis_file in thesis_files:
        if os.path.exists(thesis_file):
            with open(thesis_file, 'r') as f:
                thesis = json.load(f)
            
            # Collect data
            thesis_id = thesis.get("thesis_id", "UNKNOWN")
            print(f"Collecting data for {thesis_id}...")
            data = collect_thesis_data(client, thesis_id)
            
            # Attach data
            thesis["bigquery_data"] = data
            
            # Save
            with open(thesis_file, 'w') as f:
                json.dump(thesis, f, indent=2)
            
            print(f"  Saved {len(data)} data points to {thesis_file}")

if __name__ == "__main__":
    main()
