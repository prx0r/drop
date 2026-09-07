#!/usr/bin/env python3
"""
Hypothesis Generator — Generates hypotheses FROM data, not brainstorming.
Principle: HypoGeniC (ChicagoHAI) — hypotheses come from data.

Usage:
    python3 hypothesis_generator.py          # Generate from BigQuery
    python3 hypothesis_generator.py --file   # Generate from local JSON
"""

import json, os, sys
from pathlib import Path

DATA_DIR = Path("/root/drop/data")
OUTPUT_DIR = Path("/root/drop/data")

def load_candidates():
    """Load product candidates from BigQuery or local JSON."""
    json_file = DATA_DIR / "real_candidates.json"
    if json_file.exists():
        with open(json_file) as f:
            return json.load(f)
    return []

def compute_headroom(margin, cpc):
    """Compute economic headroom."""
    if margin <= 0 or cpc <= 0:
        return 0
    return (0.005 * margin) / cpc  # 0.5% CVR assumption

def generate_hypothesis(product):
    """Generate hypothesis from product data."""
    name = product.get("product_family", "Unknown")
    aov = product.get("selling_price", 0)
    margin = product.get("pre_ad_contribution", 0)
    cpc = product.get("expected_cpc", 0)
    headroom = product.get("headroom_base", 0)
    
    if not headroom:
        headroom = compute_headroom(margin, cpc)
    
    # Auto-kill based on economics
    if headroom < 1.0:
        return {
            "product": name,
            "statement": f"{name} has headroom {headroom:.2f}x — economics don't work",
            "prediction": "P(profitable) < 10%",
            "falsifier": "N/A — already killed by economics",
            "confidence": 0.9,
            "status": "KILLED",
            "headroom": headroom,
            "margin": margin,
            "cpc": cpc
        }
    
    # Generate testable hypothesis
    break_even_cvr = cpc / margin if margin > 0 else 1.0
    
    return {
        "product": name,
        "statement": f"{name} has headroom {headroom:.2f}x (margin €{margin:.0f} at CPC €{cpc:.2f}). Break-even CVR: {break_even_cvr*100:.2f}%",
        "prediction": f"P(profitable) > 50% if CVR > {break_even_cvr*100:.2f}%",
        "falsifier": f"100 clicks, 0 orders at CPC €{cpc:.2f}",
        "confidence": min(0.9, headroom / 3.0),
        "status": "TESTABLE",
        "headroom": headroom,
        "margin": margin,
        "cpc": cpc,
        "break_even_cvr": break_even_cvr
    }

def main():
    print("=== Hypothesis Generator ===\n")
    
    candidates = load_candidates()
    print(f"Loaded {len(candidates)} candidates")
    
    hypotheses = []
    for p in candidates[:15]:  # Top 15
        h = generate_hypothesis(p)
        hypotheses.append(h)
        status_symbol = "✓" if h["status"] == "TESTABLE" else "✗"
        print(f"  {status_symbol} {h['product']:30} → {h['status']:10} (confidence: {h['confidence']:.2f})")
    
    # Summary
    testable = sum(1 for h in hypotheses if h["status"] == "TESTABLE")
    killed = sum(1 for h in hypotheses if h["status"] == "KILLED")
    
    print(f"\nGenerated {len(hypotheses)} hypotheses:")
    print(f"  TESTABLE: {testable}")
    print(f"  KILLED: {killed}")
    
    # Save
    out_file = OUTPUT_DIR / "generated_hypotheses.json"
    with open(out_file, "w") as f:
        json.dump(hypotheses, f, indent=2)
    print(f"\nSaved to {out_file}")

if __name__ == "__main__":
    main()
