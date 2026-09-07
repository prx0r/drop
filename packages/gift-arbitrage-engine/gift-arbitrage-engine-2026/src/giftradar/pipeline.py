from __future__ import annotations
from pathlib import Path
from .config import load_opportunities, load_scoring, load_evidence
from .scoring import score_opportunity

class Radar:
    def __init__(self, config_dir: str, evidence_path: str):
        self.config_dir = Path(config_dir)
        self.opportunities = load_opportunities(config_dir)
        self.scoring = load_scoring(config_dir)
        self.evidence = load_evidence(evidence_path)

    def rank(self, slugs: list[str] | None = None):
        candidates = self.opportunities.values() if not slugs else [self.opportunities[x] for x in slugs]
        return sorted(
            [score_opportunity(o, self.evidence, self.scoring) for o in candidates],
            key=lambda s: s.total, reverse=True
        )
