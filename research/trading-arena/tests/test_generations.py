"""API-free regressions for immutable, versioned paper Arena generations."""
import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from arena import PaperAccount
from generation_manager import (alias, suffix, record_snapshot, audit_and_rotate,
                                decision, MIN_AGE_DAYS, FINAL_FIVE)
from run_virtual import initial, signal, UTC


class PaperGenerationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def seed(self, timestamp="2026-11-01T20:00:00+00:00"):
        state = initial()
        ai = initial()
        (self.root / "state.json").write_text(json.dumps(state))
        (self.root / "ai_state.json").write_text(json.dumps(ai))
        results = {}
        for worker in state:
            amount = 97.5 if worker in FINAL_FIVE else 100.0
            results[worker] = {
                "action": "HOLD", "cash": amount, "equity": amount,
                "ledger_events": 0, "council": "REVIEW_REQUIRED",
                "missing_quotes": []}
        (self.root / "last_run.json").write_text(json.dumps({
            "timestamp": timestamp, "results": results}))
        return state

    def test_names_progress_through_alphabet_without_recycling(self):
        self.assertEqual([alias("S07", k) for k in (0, 1, 25, 26, 27, 51)],
                         ["S07a", "S07b", "S07z", "S07aa", "S07ab", "S07az"])
        with self.assertRaises(ValueError):
            suffix(-1)

    def test_final_chance_mints_independent_virtual_books_and_archives_all(self):
        self.seed()
        # A held paper position must be preserved rather than fake-closed.
        state = json.loads((self.root / "state.json").read_text())
        old = PaperAccount("S07")
        old.trade(timestamp="2026-11-01T12:00:00Z", asset_class="crypto",
                  symbol="BTC/USD", side="BUY", qty=0.0001, price=50000,
                  fee=0.01, source_id="YAHOO:BTC-USD:PROXY")
        state["S07"].update(events=old.events, cash=old.cash, positions=old.holdings)
        (self.root / "state.json").write_text(json.dumps(state))
        self.assertTrue(record_snapshot(self.root))
        self.assertFalse(record_snapshot(self.root))
        review = audit_and_rotate(
            self.root, dt.datetime(2026, 11, 2, 5, 45, tzinfo=UTC))
        self.assertEqual(review["rotations"], 5)
        new_state = json.loads((self.root / "state.json").read_text())
        new_ai = json.loads((self.root / "ai_state.json").read_text())
        registry = json.loads((self.root / "generation_registry.json").read_text())
        self.assertEqual(new_state["S07"]["generation_index"], 1)
        self.assertEqual(new_state["S07"]["cash"], 100)
        self.assertEqual(new_state["S07"]["events"], [])
        self.assertEqual(new_ai["S07"]["previous_generation_context"][
                         "previous_generation"], "S07a")
        self.assertEqual(registry["workers"]["S07"]["active"], "S07b")
        self.assertEqual(registry["workers"]["S04"]["active"], "S04a")
        self.assertEqual(len(list((self.root / "generations").glob("*.json"))), 5)
        archived = json.loads((self.root / "generations" / "S07a.json").read_text())
        self.assertEqual(archived["rule_book"]["cash"], old.cash)
        self.assertEqual(archived["rule_book"]["events"], old.events)
        self.assertTrue(archived[
            "includes_open_paper_positions_without_fictitious_closing"])
        self.assertEqual(archived["last_indicative_equity"], 97.5)
        # Re-run is idempotent and must not overwrite immutable archives.
        old_text = (self.root / "generations" / "S07a.json").read_text()
        again = audit_and_rotate(self.root, dt.datetime(2026, 11, 2, 5, 46, tzinfo=UTC))
        self.assertEqual(again["rotations"], 0)
        self.assertEqual(old_text, (self.root / "generations" / "S07a.json").read_text())

    def test_bad_cash_cannot_be_laundered_by_rotation(self):
        self.seed()
        state = json.loads((self.root / "state.json").read_text())
        state["S09"]["cash"] = -2.0
        (self.root / "state.json").write_text(json.dumps(state))
        record_snapshot(self.root)
        result = audit_and_rotate(
            self.root, dt.datetime(2026, 11, 2, 5, 40, tzinfo=UTC))
        flagged = next(r for r in result["results"] if r["generation"] == "S09a")
        self.assertEqual(flagged["decision"], "QUARANTINE_NO_RESET")
        self.assertFalse((self.root / "generations" / "S09a.json").exists())
        self.assertEqual(json.loads((self.root / "state.json").read_text())[
                         "S09"]["cash"], -2.0)

    def test_regular_rotation_has_age_and_evidence_requirements(self):
        now = dt.datetime(2026, 12, 10, tzinfo=UTC)
        start = now - dt.timedelta(days=29)
        slot = {"started_at": start.isoformat()}
        record = {"events": [{"side": "SELL"}] * 6}
        samples = [(start + dt.timedelta(hours=8 * i),
                    {"equity": 97.0, "action": "HOLD", "missing_quotes": False})
                   for i in range(87)]
        samples[-1] = (now, samples[-1][1])
        self.assertEqual(decision(record, slot, samples, now),
                         "ROTATE_PERSISTENT_PAPER_LOSS")
        self.assertEqual(decision(record, {"started_at": (
            now-dt.timedelta(days=4)).isoformat()}, samples, now),
                         "DEFER_MINIMUM_28_DAYS")
        self.assertEqual(decision(record, slot, samples[:20], now),
                         "DEFER_STALE_OR_BAD_EQUITY")

    def test_successor_paper_rule_is_not_just_old_rule_with_new_name(self):
        values = [100.0] * 90
        values[-7] = 98.5
        self.assertEqual(signal("S07", values, 0), 1)
        self.assertNotEqual(signal("S07", values, 1),
                            signal("S07", values, 0))

    def test_no_fake_equity_if_mark_is_missing(self):
        self.seed()
        last = json.loads((self.root / "last_run.json").read_text())
        last["results"]["S09"]["equity"] = None
        (self.root / "last_run.json").write_text(json.dumps(last))
        record_snapshot(self.root)
        review = audit_and_rotate(
            self.root, dt.datetime(2026, 11, 2, 5, 45, tzinfo=UTC))
        found = next(r for r in review["results"] if r["generation"] == "S09a")
        self.assertEqual(found["decision"], "DEFER_MISSING_EQUITY")
        self.assertFalse((self.root / "generations" / "S09a.json").exists())


if __name__ == "__main__":
    unittest.main()
