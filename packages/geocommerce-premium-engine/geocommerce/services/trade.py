from __future__ import annotations

EU27 = {
    'AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE'
}


def intra_eu(ship_from_country: str, destination_country: str) -> bool:
    return ship_from_country.upper() in EU27 and destination_country.upper() in EU27


def requires_import_clearance(ship_from_country: str, destination_country: str) -> bool:
    a=ship_from_country.upper(); b=destination_country.upper()
    if not a:
        return True
    if a == b:
        return False
    if intra_eu(a,b):
        return False
    return True


def estimated_duty_rate(ship_from_country: str, destination_country: str, default_rate: float, landed_cost_includes_duties: bool=False) -> float:
    if landed_cost_includes_duties:
        return 0.0
    if intra_eu(ship_from_country,destination_country) or ship_from_country.upper()==destination_country.upper():
        return 0.0
    return default_rate
