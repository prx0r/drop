from __future__ import annotations

import csv
import json

from .db import connect


def export_ranked(out_path: str, db_path: str | None = None, country: str | None = None) -> int:
    with connect(db_path) as conn:
        where = " WHERE c.country = ?" if country else ""
        params = (country.upper(),) if country else ()
        rows = conn.execute(
            f"""SELECT c.country,c.niche,c.product_name,c.competitor_price_local,c.landed_cost_local,c.target_price_local,
                      c.monthly_searches,c.cpc_local,c.assumed_cvr,c.match_quality,c.competitor_source,c.supplier_source,
                      s.score_total,s.gate,s.reason,s.economics_json,s.breakdown_json
               FROM candidates c JOIN scores s ON s.candidate_id=c.id{where} ORDER BY s.score_total DESC""", params
        ).fetchall()
    if not rows:
        return 0
    fields = rows[0].keys()
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in rows:
            w.writerow(dict(row))
    return len(rows)
