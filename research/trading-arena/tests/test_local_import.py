"""Offline tests of serialized GitHub import; no broker or network calls."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]/"scripts"/"overnight"))
from import_local_research import import_records, verified_event


class ImportLocalTests(unittest.TestCase):
    def record(self,folder,action="HOLD"):
        path=Path(folder)/"2026-10-31"/("S07_"+"a"*32+".json")
        path.parent.mkdir(parents=True,exist_ok=True)
        row={"kind":"local_research_only","research_only":True,
             "live_trading":False,"event_id":"a"*32,"worker":"S07",
             "cycle":"2026-10-31T05:00Z","model":"llama3.2:3b",
             "event":{"status":"RESEARCHED","action":action},
             "experiment":{"topic":"fresh hypothesis"}}
        path.write_text(json.dumps(row,indent=2)+"\n")
        return path

    def test_canonical_account_unchanged_and_import_idempotent(self):
        with tempfile.TemporaryDirectory() as root:
            root=Path(root)
            inbox=root/"inbox"
            ledger=root/"ledger"
            ledger.mkdir()
            original='{"S07":{"cash":100}}'
            (ledger/"ai_state.json").write_text(original)
            self.record(inbox)
            self.assertEqual(import_records(inbox,ledger),1)
            self.assertEqual(import_records(inbox,ledger),0)
            self.assertEqual((ledger/"ai_state.json").read_text(),original)
            self.assertIn("| S07 | 1 | 1 | 0 |",
                          (ledger/"LOCAL_NIGHTLY.md").read_text())

    def test_model_cannot_import_trade_or_conflicting_file(self):
        with tempfile.TemporaryDirectory() as root:
            root=Path(root)
            inbox=root/"inbox"
            ledger=root/"ledger"
            self.record(inbox,action="BUY BTC-USD")
            with self.assertRaisesRegex(ValueError,"TRADE_ACTION_REFUSED"):
                import_records(inbox,ledger)
            path=self.record(inbox,action="HOLD")
            self.assertEqual(import_records(inbox,ledger),1)
            x=json.loads(path.read_text())
            x["experiment"]["topic"]="altered"
            path.write_text(json.dumps(x)+"\n")
            with self.assertRaisesRegex(ValueError,"IMMUTABLE_EVENT_CONFLICT"):
                import_records(inbox,ledger)

    def test_worker_identity_and_date_verified(self):
        with tempfile.TemporaryDirectory() as root:
            path=self.record(root)
            _,event=verified_event(path)
            self.assertEqual(event["worker"],"S07")
            changed=path.with_name("S08_"+"a"*32+".json")
            path.rename(changed)
            with self.assertRaisesRegex(ValueError,"INVALID_WORKER_IDENTITY"):
                verified_event(changed)


if __name__=="__main__":
    unittest.main()
