from __future__ import annotations

import csv
from pathlib import Path

# A deliberately small Merchant Center-ready export helper. It does not invent GTINs,
# brands or availability. Those must come from verified catalog data.
REQUIRED = ("id", "title", "description", "link", "image_link", "availability", "price")
OPTIONAL = ("brand", "gtin", "mpn", "condition", "google_product_category", "product_type", "shipping_label")


def validate_feed_row(row: dict[str, str]) -> list[str]:
    errors = []
    for field in REQUIRED:
        if not str(row.get(field, "")).strip():
            errors.append(f"missing {field}")
    if row.get("condition") and row["condition"] not in {"new", "refurbished", "used"}:
        errors.append("condition must be new/refurbished/used")
    return errors


def build_feed(input_csv: str, output_csv: str) -> int:
    src = Path(input_csv)
    out = Path(output_csv)
    rows: list[dict[str, str]] = []
    with src.open(newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            errs = validate_feed_row(row)
            if errs:
                raise ValueError(f"row {i}: " + "; ".join(errs))
            rows.append(row)
    fields = list(REQUIRED) + [f for f in OPTIONAL if any(r.get(f) for r in rows)]
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return len(rows)
