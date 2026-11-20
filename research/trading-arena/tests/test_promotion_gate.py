"""Unit tests for the fail-closed Arena paper promotion gate."""
import datetime as dt
import json
import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from promotion_gate import evaluate

NOW = dt.datetime(2026, 11, 20, tzinfo=dt.timezone.utc)
GOOD = dict(candidate_id="S03b", worker="S03", validated=True,
    data_provenance="independent point-in-time historical data",
    no_lookahead=True, point_in_time_universe=True,
    next_bar_execution=True, costs_included=True,
    out_of_sample_trades=50, out_of_sample_days=120,
    candidate_net_return_pct=5.0, baseline_net_return_pct=1.0,
    candidate_max_drawdown_pct=4.0, baseline_max_drawdown_pct=7.0,
    evaluated_at="2026-11-19T00:00:00+00:00")

class PromotionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "candidate_evidence").mkdir()
    def check(self, evidence):
        (self.root / "candidate_evidence" / "S03b.json").write_text(json.dumps(evidence))
        return evaluate(self.root, "S03", "S03b", NOW)
    def test_missing_proof_blocks(self):
        self.assertEqual(evaluate(self.root, "S03", "S03b", NOW)[0], False)
    def test_valid_proof_passes_paper_only(self):
        self.assertTrue(self.check(GOOD)[0])
    def test_lookahead_blocks(self):
        self.assertFalse(self.check(dict(GOOD, no_lookahead=False))[0])
    def test_missing_costs_blocks(self):
        self.assertFalse(self.check(dict(GOOD, costs_included=False))[0])
    def test_insufficient_sample_blocks(self):
        self.assertFalse(self.check(dict(GOOD, out_of_sample_trades=5))[0])
    def test_underperformance_blocks(self):
        self.assertFalse(self.check(dict(GOOD, candidate_net_return_pct=-1))[0])
    def test_worse_drawdown_blocks(self):
        self.assertFalse(self.check(dict(GOOD, candidate_max_drawdown_pct=9))[0])
    def test_wrong_identity_blocks(self):
        self.assertFalse(self.check(dict(GOOD, worker="S04"))[0])
    def test_stale_blocks(self):
        self.assertFalse(self.check(dict(GOOD, evaluated_at="2026-09-01T00:00:00+00:00"))[0])
    def test_nonfinite_blocks(self):
        self.assertFalse(self.check(dict(GOOD, candidate_net_return_pct=float("nan")))[0])

if __name__ == "__main__":
    unittest.main()
