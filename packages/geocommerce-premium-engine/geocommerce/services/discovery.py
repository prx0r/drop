from __future__ import annotations


def normalize_best_seller_rows(rows: list[dict]) -> list[dict]:
    """Normalize Merchant best-seller report rows into supplier-resolution candidates."""
    out = []
    for row in rows:
        v = row.get("bestSellersProductClusterView", row)
        rank = int(v.get("rank", 0) or 0)
        if not rank:
            continue
        gtins = v.get("variantGtins", []) or v.get("variant_gtins", []) or []
        demand = str(v.get("relativeDemand") or v.get("relative_demand") or "UNKNOWN")
        change = str(v.get("relativeDemandChange") or v.get("relative_demand_change") or "UNKNOWN")
        score = max(0, 100 - min(rank, 100))
        if demand == "VERY_HIGH": score += 15
        elif demand == "HIGH": score += 8
        if change == "RISER": score += 10
        out.append({
            "title": v.get("title", ""),
            "brand": v.get("brand", ""),
            "rank": rank,
            "relative_demand": demand,
            "relative_demand_change": change,
            "variant_gtins": gtins,
            "inventory_status": v.get("inventoryStatus") or v.get("inventory_status"),
            "research_priority": min(100, score),
            "next_actions": [
                "resolve GTIN/MPN against authorized EU/local suppliers",
                "compute landed contribution in each candidate country",
                "run local Keyword Planner query cluster",
                "inspect Shopping SERP and delivery/payment promise",
                "order sample before paid traffic",
            ],
        })
    return sorted(out, key=lambda x: (-x["research_priority"], x["rank"]))
