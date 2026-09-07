#!/usr/bin/env python3
"""
Simple Hypothesis Tracker
=========================
Not over-engineered. Not Bayesian forecasting. Not tournament evolution.

Just: hypothesis → metric → threshold → decision.

Usage:
    python3 hypothesis_tracker.py --status          # Show all hypotheses
    python3 hypothesis_tracker.py --update H1.1 1.5 # Update metric for hypothesis
    python3 hypothesis_tracker.py --decide           # Auto-decide based on data
"""

import json, os, sys
from datetime import datetime, timedelta

HYPOTHESES_FILE = "/root/drop/data/hypotheses.json"
METRICS_FILE = "/root/drop/data/metrics.json"

# Default hypotheses from TEN_THESES.md
DEFAULT_HYPOTHESES = [
    {
        "id": "H1.1",
        "thesis": "GeoDrop",
        "statement": "Language localization converts 2x+ better",
        "metric": "cvr_ratio",
        "target": 1.5,
        "direction": ">",
        "window_days": 30,
        "status": "active",
        "data_points": []
    },
    {
        "id": "H1.3",
        "thesis": "GeoDrop",
        "statement": "Free listings validate before paid",
        "metric": "impressions_per_day",
        "target": 100,
        "direction": ">",
        "window_days": 14,
        "status": "active",
        "data_points": []
    },
    {
        "id": "H2.1",
        "thesis": "GeoDrop",
        "statement": "Specialist positioning beats generic",
        "metric": "ctr",
        "target": 3.0,
        "direction": ">",
        "window_days": 30,
        "status": "active",
        "data_points": []
    },
    {
        "id": "H3.1",
        "thesis": "GeoDrop",
        "statement": "Finnish robot vacuum market has merchant gap",
        "metric": "good_seller_count",
        "target": 5,
        "direction": "<",
        "window_days": 7,
        "status": "active",
        "data_points": []
    },
    {
        "id": "H5.1",
        "thesis": "GeoDrop",
        "statement": "High ticket solves small budgets",
        "metric": "profit_per_click",
        "target": 0,
        "direction": ">",
        "window_days": 30,
        "status": "active",
        "data_points": []
    },
    {
        "id": "H6.1",
        "thesis": "GeoDrop",
        "statement": "Good seller gap predicts success",
        "metric": "revenue_per_click",
        "target": 5,
        "direction": ">",
        "window_days": 30,
        "status": "active",
        "data_points": []
    },
    {
        "id": "H10.1",
        "thesis": "GeoDrop",
        "statement": "Free listings generate real signal",
        "metric": "impressions_per_day",
        "target": 100,
        "direction": ">",
        "window_days": 14,
        "status": "active",
        "data_points": []
    },
]

def load_hypotheses():
    if os.path.exists(HYPOTHESES_FILE):
        with open(HYPOTHESES_FILE) as f:
            return json.load(f)
    return DEFAULT_HYPOTHESES

def save_hypotheses(hypotheses):
    with open(HYPOTHESES_FILE, "w") as f:
        json.dump(hypotheses, f, indent=2)

def show_status(hypotheses):
    print("\n=== Hypothesis Status ===\n")
    print(f"{'ID':8} {'Status':10} {'Metric':20} {'Target':10} {'Current':10} {'Decision':10}")
    print("-" * 70)
    for h in hypotheses:
        data = h.get("data_points", [])
        if data:
            current = data[-1].get("value", "N/A")
        else:
            current = "NO DATA"
        
        # Auto-decide
        if len(data) >= 3:
            recent = [d["value"] for d in data[-3:]]
            avg = sum(recent) / len(recent)
            if h["direction"] == ">":
                decision = "PASS" if avg > h["target"] else "FAIL"
            else:
                decision = "PASS" if avg < h["target"] else "FAIL"
        else:
            decision = "WAITING"
        
        print(f"{h['id']:8} {h['status']:10} {h['metric']:20} {h['direction']}{h['target']:<9} {str(current):10} {decision:10}")

def update_metric(hypotheses, hypothesis_id, value):
    for h in hypotheses:
        if h["id"] == hypothesis_id:
            h["data_points"].append({
                "value": value,
                "timestamp": datetime.now().isoformat()
            })
            print(f"Updated {hypothesis_id}: {value}")
            return
    print(f"Hypothesis {hypothesis_id} not found")

def decide(hypotheses):
    print("\n=== Auto-Decisions ===\n")
    for h in hypotheses:
        data = h.get("data_points", [])
        if len(data) < 3:
            print(f"{h['id']}: WAITING (need {3 - len(data)} more data points)")
            continue
        
        recent = [d["value"] for d in data[-3:]]
        avg = sum(recent) / len(recent)
        
        if h["direction"] == ">":
            passed = avg > h["target"]
        else:
            passed = avg < h["target"]
        
        if passed:
            h["status"] = "passed"
            print(f"{h['id']}: PASS ({h['statement'][:50]}...)")
        else:
            h["status"] = "failed"
            print(f"{h['id']}: FAIL ({h['statement'][:50]}...)")
    
    save_hypotheses(hypotheses)

def main():
    hypotheses = load_hypotheses()
    
    if "--status" in sys.argv:
        show_status(hypotheses)
    elif "--update" in sys.argv:
        idx = sys.argv.index("--update")
        if idx + 2 < len(sys.argv):
            update_metric(hypotheses, sys.argv[idx + 1], float(sys.argv[idx + 2]))
            save_hypotheses(hypotheses)
        else:
            print("Usage: --update H1.1 1.5")
    elif "--decide" in sys.argv:
        decide(hypotheses)
    else:
        show_status(hypotheses)

if __name__ == "__main__":
    main()
