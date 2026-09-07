#!/usr/bin/env python3
"""
Probe Designer — Designs cheapest test for a hypothesis.
Principle: POPPER (Stanford) — falsification-first.

Usage:
    python3 probe_designer.py                    # Design probes for all testable hypotheses
    python3 probe_designer.py --hypothesis H1    # Design probe for specific hypothesis
"""

import json, os, sys
from pathlib import Path

DATA_DIR = Path("/root/drop/data")

def load_hypotheses():
    """Load generated hypotheses."""
    hyp_file = DATA_DIR / "generated_hypotheses.json"
    if hyp_file.exists():
        with open(hyp_file) as f:
            return json.load(f)
    return []

def design_probe(hypothesis):
    """Design the cheapest test for a hypothesis."""
    product = hypothesis["product"]
    headroom = hypothesis.get("headroom", 0)
    margin = hypothesis.get("margin", 0)
    cpc = hypothesis.get("cpc", 0)
    
    # Determine what data we need
    if "headroom" in hypothesis.get("statement", "").lower():
        test_type = "free_listing"
        data_needed = "impressions, clicks, ctr, conversions"
        budget = 0
        duration = 14
        min_clicks = 100
    elif "margin" in hypothesis.get("statement", "").lower():
        test_type = "keyword_research"
        data_needed = "search_volume, cpc, competitor_count"
        budget = 0
        duration = 1
        min_clicks = 0
    else:
        test_type = "free_listing"
        data_needed = "impressions, clicks, ctr, conversions"
        budget = 0
        duration = 14
        min_clicks = 100
    
    # Compute break-even
    break_even_cvr = cpc / margin if margin > 0 else 1.0
    
    probe = {
        "hypothesis_id": hypothesis.get("product", "unknown"),
        "test_type": test_type,
        "products": [product],
        "country": "FI",  # Default to Finland
        "budget": budget,
        "duration_days": duration,
        "minimum_clicks": min_clicks,
        "data_to_collect": data_needed.split(", "),
        "break_even_cvr": break_even_cvr,
        "falsification_threshold": 0.5,
        "stopping_rule": f"{min_clicks} clicks OR {duration} days",
        "expected_cost": f"€{budget}",
        "notes": f"Headroom: {headroom:.2f}x, Margin: €{margin:.0f}, CPC: €{cpc:.2f}"
    }
    
    return probe

def main():
    print("=== Probe Designer ===\n")
    
    hypotheses = load_hypotheses()
    testable = [h for h in hypotheses if h.get("status") == "TESTABLE"]
    
    print(f"Loaded {len(hypotheses)} hypotheses, {len(testable)} testable")
    
    probes = []
    for h in testable:
        probe = design_probe(h)
        probes.append(probe)
        print(f"\n  {probe['hypothesis_id']}:")
        print(f"    Test: {probe['test_type']}")
        print(f"    Budget: {probe['expected_cost']}")
        print(f"    Duration: {probe['duration_days']} days")
        print(f"    Min clicks: {probe['minimum_clicks']}")
        print(f"    Break-even CVR: {probe['break_even_cvr']*100:.2f}%")
    
    # Save
    out_file = DATA_DIR / "designed_probes.json"
    with open(out_file, "w") as f:
        json.dump(probes, f, indent=2)
    print(f"\nSaved {len(probes)} probes to {out_file}")

if __name__ == "__main__":
    main()
