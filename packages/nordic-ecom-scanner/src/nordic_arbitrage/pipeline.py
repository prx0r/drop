from __future__ import annotations

import json
from dataclasses import asdict

from .config import COUNTRIES
from .db import connect
from .economics import calculate_economics
from .models import Candidate
from .scoring import score_candidate


def _candidate(row) -> Candidate:
    d = dict(row)
    for key in ("has_local_payment", "has_local_return_address"):
        d[key] = bool(d[key])
    return Candidate(**d)


def score_all(path: str | None = None) -> int:
    n = 0
    with connect(path) as conn:
        rows = conn.execute("SELECT * FROM candidates ORDER BY id").fetchall()
        for row in rows:
            c = _candidate(row)
            profile = COUNTRIES[c.country]
            try:
                econ = calculate_economics(c, profile)
                score = score_candidate(c, econ, profile)
            except ValueError as exc:
                continue
            conn.execute(
                """INSERT INTO scores(candidate_id,score_total,gate,reason,economics_json,breakdown_json)
                   VALUES (?,?,?,?,?,?)
                   ON CONFLICT(candidate_id) DO UPDATE SET
                   score_total=excluded.score_total, gate=excluded.gate, reason=excluded.reason,
                   economics_json=excluded.economics_json, breakdown_json=excluded.breakdown_json,
                   scored_at=CURRENT_TIMESTAMP""",
                (c.id, score.total, score.gate, score.reason, json.dumps(asdict(econ)), json.dumps(asdict(score))),
            )
            n += 1
    return n


def ranked(path: str | None = None, limit: int = 20, country: str | None = None, gate: str | None = None):
    clauses = []
    params: list[object] = []
    if country:
        clauses.append("c.country = ?")
        params.append(country.upper())
    if gate:
        clauses.append("s.gate = ?")
        params.append(gate.upper())
    where = (" WHERE " + " AND ".join(clauses)) if clauses else ""
    params.append(limit)
    with connect(path) as conn:
        return conn.execute(
            f"""SELECT c.*, s.score_total, s.gate, s.reason, s.economics_json, s.breakdown_json
               FROM candidates c JOIN scores s ON s.candidate_id=c.id
               {where} ORDER BY s.score_total DESC LIMIT ?""", tuple(params)
        ).fetchall()
