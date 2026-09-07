from __future__ import annotations

import csv
from pathlib import Path

from .base import KeywordMetric, ShoppingResult


class CSVKeywordProvider:
    def __init__(self, path: str):
        self.path = Path(path)

    def metrics(self, *, keywords: list[str], country: str, language: str) -> list[KeywordMetric]:
        wanted = {k.lower() for k in keywords}
        out = []
        with self.path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("keyword", "").lower() in wanted and (not row.get("country") or row["country"] == country):
                    out.append(KeywordMetric(row["keyword"], float(row.get("monthly_searches") or 0), float(row.get("cpc") or 0), float(row.get("competition") or 0)))
        return out


class CSVShoppingProvider:
    def __init__(self, path: str):
        self.path = Path(path)

    def search(self, *, query: str, country: str, language: str) -> list[ShoppingResult]:
        out = []
        with self.path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("country") != country or row.get("query", "").lower() != query.lower():
                    continue
                out.append(ShoppingResult(
                    title=row.get("title", ""), price=float(row["price"]) if row.get("price") else None,
                    currency=row.get("currency"), merchant=row.get("merchant"), link=row.get("link"),
                    image_url=row.get("image_url"), position=int(row.get("position") or len(out)+1),
                ))
        return out
