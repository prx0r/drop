#!/usr/bin/env python3
"""
Drop Report Ingestion Pipeline
==============================
Pulls data from Google APIs, scores candidates, generates reports.

Usage:
    python3 pipeline.py --step merchant热门      # Pull Merchant Center Popular Products
    python3 pipeline.py --step keywords          # Pull Keyword Planner data
    python3 pipeline.py --step score             # Re-score all candidates
    python3 pipeline.py --step report            # Generate reports
    python3 pipeline.py --step all               # Full pipeline
"""

import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("/root/drop")
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
SECRETS_DIR = BASE_DIR / "secrets"

# --- Config ---

MERCHANT_CENTER_ID = "5849184805"
GOOGLE_ADS_CUSTOMER_ID = "3775149829"

TARGET_COUNTRIES = [
    {"code": "NO", "name": "Norway", "language": "no", "currency": "NOK"},
    {"code": "FI", "name": "Finland", "language": "fi", "currency": "EUR"},
    {"code": "SE", "name": "Sweden", "language": "sv", "currency": "SEK"},
    {"code": "DK", "name": "Denmark", "language": "da", "currency": "DKK"},
    {"code": "NL", "name": "Netherlands", "language": "nl", "currency": "EUR"},
    {"code": "DE", "name": "Germany", "language": "de", "currency": "EUR"},
    {"code": "AT", "name": "Austria", "language": "de", "currency": "EUR"},
    {"code": "CH", "name": "Switzerland", "language": "de", "currency": "CHF"},
]


def load_tokens():
    """Load OAuth tokens from secrets."""
    token_file = SECRETS_DIR / "oauth-tokens.json"
    if not token_file.exists():
        raise FileNotFoundError(f"Tokens not found: {token_file}")
    with open(token_file) as f:
        return json.load(f)


def refresh_token_if_needed(tokens):
    """Refresh access token if expired (simple check)."""
    # In production, check expires_in timestamp
    return tokens


def api_get(url, tokens, params=None):
    """Make authenticated GET request to Google API."""
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {tokens['access_token']}",
        "Content-Type": "application/json"
    })
    try:
        resp = urllib.request.urlopen(req)
        return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"  API Error {e.code}: {e.read().decode()[:200]}")
        return None


def step_merchant_popular(tokens):
    """Pull Popular Products from Merchant Center for each target country."""
    print("\n=== Step 1: Merchant Center Popular Products ===")
    all_products = []

    for country in TARGET_COUNTRIES:
        print(f"\n  Fetching {country['name']} ({country['code']})...")
        # Note: This endpoint may need adjustment based on actual API
        url = f"https://merchantapi.googleapis.com/analytics/v2/accounts/{MERCHANT_CENTER_ID}/reports/popularProducts"
        params = {
            "countryCode": country["code"],
            "pageSize": 100
        }
        data = api_get(url, tokens, params)
        if data and "popularProducts" in data:
            products = data["popularProducts"]
            print(f"  Found {len(products)} popular products")
            for p in products:
                p["_country"] = country["code"]
                p["_country_name"] = country["name"]
            all_products.extend(products)
        else:
            print(f"  No data or API not ready for {country['code']}")

    # Save
    out_file = DATA_DIR / "merchant_popular_products.json"
    with open(out_file, "w") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "countries": [c["code"] for c in TARGET_COUNTRIES],
            "total_products": len(all_products),
            "products": all_products
        }, f, indent=2)
    print(f"\n  Saved {len(all_products)} products to {out_file}")
    return all_products


def step_keywords(tokens):
    """Pull Keyword Planner data for top candidates."""
    print("\n=== Step 2: Keyword Planner Data ===")

    # Load existing candidates
    candidates_file = DATA_DIR / "real_candidates.json"
    if candidates_file.exists():
        with open(candidates_file) as f:
            candidates = json.load(f)
        print(f"  Loaded {len(candidates)} existing candidates")
    else:
        print("  No candidates found. Run merchant step first.")
        return []

    # For each candidate, query Keyword Planner
    keyword_data = []
    for cand in candidates[:20]:  # Top 20
        product_name = cand.get("name", cand.get("title", "unknown"))
        print(f"\n  Researching: {product_name}")

        for country in TARGET_COUNTRIES[:4]:  # NO, FI, SE, DK
            # Generate search queries
            queries = [
                product_name,
                f"{product_name} {country['language']}",
                f"buy {product_name}",
                f"best {product_name}",
            ]

            for query in queries:
                # Note: Keyword Planner API requires specific endpoint
                # This is a placeholder for the actual implementation
                print(f"    Query: {query} ({country['code']})")

            keyword_data.append({
                "product": product_name,
                "country": country["code"],
                "queries": queries,
                "timestamp": datetime.now().isoformat()
            })

    # Save
    out_file = DATA_DIR / "keyword_data.json"
    with open(out_file, "w") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "entries": keyword_data
        }, f, indent=2)
    print(f"\n  Saved keyword data to {out_file}")
    return keyword_data


def step_score():
    """Re-score all candidates using the scoring engine."""
    print("\n=== Step 3: Score Candidates ===")

    candidates_file = DATA_DIR / "real_candidates.json"
    if not candidates_file.exists():
        print("  No candidates to score.")
        return

    with open(candidates_file) as f:
        candidates = json.load(f)

    # Import scoring modules
    sys.path.insert(0, str(BASE_DIR / "packages"))
    from economics.model import calculate_economics
    from scoring.gates import apply_gates
    from scoring.score import calculate_score

    scored = []
    for cand in candidates:
        try:
            economics = calculate_economics(cand)
            gates = apply_gates(cand, economics)
            score = calculate_score(cand, economics, gates)

            scored.append({
                **cand,
                "_economics": economics,
                "_gates": gates,
                "_score": score,
                "_scored_at": datetime.now().isoformat()
            })
        except Exception as e:
            print(f"  Error scoring {cand.get('name', '?')}: {e}")

    # Sort by score
    scored.sort(key=lambda x: x.get("_score", {}).get("total", 0), reverse=True)

    # Save
    out_file = DATA_DIR / "scored_candidates.json"
    with open(out_file, "w") as f:
        json.dump(scored, f, indent=2)
    print(f"\n  Scored {len(scored)} candidates. Top 3:")
    for s in scored[:3]:
        print(f"    {s.get('name', '?')}: {s.get('_score', {}).get('total', 0):.1f}")


def step_report():
    """Generate reports from scored data."""
    print("\n=== Step 4: Generate Reports ===")

    scored_file = DATA_DIR / "scored_candidates.json"
    if not scored_file.exists():
        print("  No scored candidates. Run score step first.")
        return

    with open(scored_file) as f:
        candidates = json.load(f)

    # Generate TOP_CANDIDATES.json
    top = candidates[:10]
    out_file = OUTPUT_DIR / "TOP_CANDIDATES_LIVE.json"
    with open(out_file, "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "total_candidates": len(candidates),
            "top_10": top
        }, f, indent=2)
    print(f"  Generated {out_file}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Drop Report Pipeline")
    parser.add_argument("--step", default="all",
                       choices=["merchant", "keywords", "score", "report", "all"],
                       help="Pipeline step to run")
    args = parser.parse_args()

    # Ensure directories exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    tokens = load_tokens()
    tokens = refresh_token_if_needed(tokens)

    steps = {
        "merchant": lambda: step_merchant_popular(tokens),
        "keywords": lambda: step_keywords(tokens),
        "score": step_score,
        "report": step_report,
    }

    if args.step == "all":
        for name, func in steps.items():
            func()
    else:
        steps[args.step]()


if __name__ == "__main__":
    main()
