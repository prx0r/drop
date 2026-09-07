from __future__ import annotations

import json
from fastapi import FastAPI, HTTPException, Query

from .compliance import compliance_flags
from .config import COUNTRIES
from .db import connect
from .models import Candidate
from .pipeline import ranked

app = FastAPI(title="Nordic Ecom Scanner", version="0.2.0")


@app.get("/health")
def health():
    return {"ok": True, "countries": len(COUNTRIES)}


@app.get("/countries")
def countries():
    return [
        {
            "code": p.code,
            "name": p.name,
            "currency": p.currency,
            "language": p.language,
            "vat": p.standard_vat_rate,
            "local_payments": p.local_payments,
            "target_delivery_days": p.target_delivery_days,
            "max_acceptable_delivery_days": p.max_acceptable_delivery_days,
            "import_scheme": p.import_scheme,
            "notes": p.notes,
        }
        for p in COUNTRIES.values()
    ]


@app.get("/opportunities")
def opportunities(
    limit: int = Query(20, ge=1, le=200),
    country: str | None = Query(None, min_length=2, max_length=2),
    gate: str | None = None,
):
    out = []
    for row in ranked(limit=limit, country=country, gate=gate):
        d = dict(row)
        d["economics"] = json.loads(d.pop("economics_json"))
        d["score"] = json.loads(d.pop("breakdown_json"))
        out.append(d)
    return out


@app.get("/candidates/{candidate_id}/compliance")
def candidate_compliance(candidate_id: int):
    with connect() as conn:
        row = conn.execute("SELECT * FROM candidates WHERE id=?", (candidate_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="candidate not found")
    d = dict(row)
    d["has_local_payment"] = bool(d["has_local_payment"])
    d["has_local_return_address"] = bool(d["has_local_return_address"])
    candidate = Candidate(**d)
    return {"candidate_id": candidate_id, "flags": compliance_flags(candidate)}
