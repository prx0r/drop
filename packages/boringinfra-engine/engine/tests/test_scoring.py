import unittest
from boringinfra.seeds import SEEDS
from boringinfra.scoring import score

class ScoreTests(unittest.TestCase):
    def test_vertical_beats_generic_baseline(self):
        by={o.name:o for o in SEEDS}
        self.assertGreater(score(by["Practice Statement Normalizer"]), score(by["Generic PDF Parser"]))
        self.assertGreater(score(by["Public Tender Change Radar"]), score(by["Generic Uptime Monitor"]))
        self.assertGreater(score(by["Xero Practice Ops Adapter"]), score(by["Generic Agent Hosting"]))

    def test_score_bounds(self):
        for op in SEEDS:
            self.assertGreaterEqual(score(op), 0)
            self.assertLessEqual(score(op), 100)

if __name__ == '__main__': unittest.main()
