import csv
from .models import Opportunity
from .db import upsert

NUMERIC = {
"verified_revenue_signal","wtp","recurrence","build_simplicity","data_access","distribution","localization",
"gross_margin","competition_gap","workflow_criticality","platform_risk","support_burden","regulatory_burden"
}


def import_csv(path: str, conn) -> int:
    count=0
    with open(path, newline='', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            for k in NUMERIC:
                row[k] = float(row[k])
            row.setdefault("notes", "")
            op = Opportunity(**{k: row[k] for k in Opportunity.__dataclass_fields__ if k != "id"})
            upsert(conn, op)
            count += 1
    return count
