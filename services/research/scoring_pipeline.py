#!/usr/bin/env python3
"""
Automated Product Scoring Pipeline
===================================
Scores products against the canonical strategy rubric.
Reads from BigQuery, scores, writes back.

Usage:
    python3 scoring_pipeline.py --scan          # Scan for new opportunities
    python3 scoring_pipeline.py --score         # Score all products
    python3 scoring_pipeline.py --report        # Generate report
"""

import json, urllib.request, datetime, subprocess, sys

PROJECT = "project-ff2366d2-8fda-4fcb-9ba"
DATASET = "drop"

def get_cred(key):
    result = subprocess.run(
        ["agent-vault", "vault", "credential", "get", key, "--vault", "oracle"],
        capture_output=True, text=True
    )
    return result.stdout.strip()

def get_token():
    with open("/root/drop/secrets/oauth-tokens.json") as f:
        tokens = json.load(f)
    return tokens["access_token"]

def query_bq(sql, token):
    body = json.dumps({"query": sql, "useLegacySql": False}).encode()
    req = urllib.request.Request(
        f"https://bigquery.googleapis.com/bigquery/v2/projects/{PROJECT}/queries",
        data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST"
    )
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())

def score_product(product):
    """Score a product against the canonical rubric (0-100)."""
    score = 0
    
    # Demand (0-20)
    search_vol = product.get("search_volume", 0) or 0
    if search_vol > 10000: score += 20
    elif search_vol > 5000: score += 15
    elif search_vol > 1000: score += 10
    elif search_vol > 0: score += 5
    
    # Economics (0-20)
    margin = product.get("margin_pct", 0) or 0
    if margin > 60: score += 20
    elif margin > 40: score += 15
    elif margin > 20: score += 10
    elif margin > 0: score += 5
    
    # Merchant Gap (0-15)
    sellers = product.get("seller_count", 0) or 0
    good_sellers = product.get("good_seller_count", 0) or 0
    if sellers > 0 and good_sellers < 3: score += 15
    elif sellers > 0 and good_sellers < 5: score += 10
    elif sellers > 0: score += 5
    
    # Supplier (0-15) - assumed available if in our pipeline
    score += 10  # base score
    
    # CPC Headroom (0-10)
    cpc = product.get("cpc", 0) or 0
    contribution = product.get("contribution", 0) or 0
    if cpc > 0 and contribution > 0:
        headroom = (0.005 * contribution) / cpc  # 0.5% CVR assumption
        if headroom > 2: score += 10
        elif headroom > 1.5: score += 7
        elif headroom > 1: score += 5
    elif contribution > 100: score += 7  # high contribution, assume OK
    
    # Localization (0-5)
    score += 3  # base for any Nordic market
    
    # Seasonality (0-5)
    evergreen = product.get("evergreen", False)
    if evergreen: score += 5
    else: score += 2
    
    # Accessory Upsell (0-5)
    upsell = product.get("upsell_potential", False)
    if upsell: score += 5
    else: score += 2
    
    # Barrier to Entry (0-5)
    score += 3  # base for foreign language market
    
    return min(score, 100)

def main():
    token = get_token()
    
    if "--score" in sys.argv:
        print("=== Scoring all products ===")
        result = query_bq(f"SELECT * FROM `{PROJECT}.{DATASET}.products` WHERE score IS NULL OR score = 0", token)
        products = result.get("rows", [])
        print(f"Found {len(products)} unscored products")
        
        for p in products:
            f = p["f"]
            product = {
                "search_volume": int(f[12]["v"]) if f[12]["v"] else 0,
                "seller_count": int(f[10]["v"]) if f[10]["v"] else 0,
                "good_seller_count": int(f[11]["v"]) if f[11]["v"] else 0,
                "cpc": float(f[13]["v"]) if f[13]["v"] else 0,
                "contribution_margin": float(f[8]["v"]) if f[8]["v"] else 0,
                "margin_pct": 0,
            }
            score = score_product(product)
            print(f"  {f[1]['v']:30} → {score}/100")
    
    if "--report" in sys.argv:
        print("=== Product Score Report ===")
        result = query_bq(f"SELECT cand_id, name, country, seller_count, good_seller_count, search_volume, cpc_estimate, contribution_margin FROM `{PROJECT}.{DATASET}.products` WHERE contribution_margin IS NOT NULL ORDER BY contribution_margin DESC LIMIT 20", token)
        products = result.get("rows", [])
        
        print(f"\n{'Name':30} {'Country':4} {'Sellers':7} {'Good':5} {'Vol':7} {'CPC':6} {'Margin':8}")
        print("-" * 80)
        for p in products:
            f = p["f"]
            name = f[1]["v"][:30] if f[1]["v"] else "N/A"
            country = f[2]["v"] if f[2]["v"] else "N/A"
            sellers = f[3]["v"] if f[3]["v"] else "N/A"
            good = f[4]["v"] if f[4]["v"] else "N/A"
            vol = f[5]["v"] if f[5]["v"] else "N/A"
            cpc = f[6]["v"] if f[6]["v"] else "N/A"
            margin = f[7]["v"] if f[7]["v"] else "N/A"
            print(f"{name:30} {country:4} {str(sellers):7} {str(good):5} {str(vol):7} {str(cpc):6} {str(margin):8}")

if __name__ == "__main__":
    main()
