from __future__ import annotations

import csv
import os
from pathlib import Path

from .db import connect


FIELDS = [
    "country","niche","product_name","competitor_price_local","supplier_price_usd_low","supplier_price_usd_high","supplier_moq","match_quality","competitor_source","supplier_source",
    "monthly_searches","cpc_local","assumed_cvr","merchant_count","dominant_merchant_share","creative_gap","title_gap","b2b_multiplier","bundle_multiplier","regulated_risk","fragility_risk","bulky_risk","expected_return_rate","estimated_delivery_days","has_local_payment","has_local_return_address","landed_cost_local","target_price_local","expected_units_per_order","notes"
]


def seed_from_csv(csv_path: str, db_path: str | None = None, replace: bool = True) -> int:
    with connect(db_path) as conn:
        if replace:
            conn.execute("DELETE FROM scores")
            conn.execute("DELETE FROM candidates")
        with open(csv_path, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        placeholders = ",".join("?" for _ in FIELDS)
        sql = f"INSERT INTO candidates ({','.join(FIELDS)}) VALUES ({placeholders})"
        for row in rows:
            vals = []
            for field in FIELDS:
                v = row.get(field, "")
                if field in {"country","niche","product_name","match_quality","competitor_source","supplier_source","notes"}:
                    vals.append(v)
                elif field in {"supplier_moq","merchant_count","estimated_delivery_days","has_local_payment","has_local_return_address"}:
                    vals.append(int(float(v or 0)))
                else:
                    vals.append(float(v) if v not in ("", None) else None)
            conn.execute(sql, vals)
        return len(rows)
