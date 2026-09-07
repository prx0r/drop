from dataclasses import dataclass, asdict

@dataclass
class Opportunity:
    name: str
    pattern: str
    niche: str
    problem: str
    economic_event: str
    verified_revenue_signal: float
    wtp: float
    recurrence: float
    build_simplicity: float
    data_access: float
    distribution: float
    localization: float
    gross_margin: float
    competition_gap: float
    workflow_criticality: float
    platform_risk: float
    support_burden: float
    regulatory_burden: float
    notes: str = ""
    id: int | None = None

    def to_dict(self):
        return asdict(self)
