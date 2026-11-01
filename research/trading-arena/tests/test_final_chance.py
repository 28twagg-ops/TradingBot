"""Zero-API tests of one-day final-chance research priority and expiry."""
import datetime as dt
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from groq_research import (choose_due_workers, FINAL_CHANCE_WORKERS,
                           FINAL_CHANCE_START, FINAL_CHANCE_END)
from quota_scheduler import eligible_worker_order
from run_virtual import initial, UTC


class FinalChanceTests(unittest.TestCase):
    def test_exact_cohort_and_time_window(self):
        self.assertEqual(FINAL_CHANCE_WORKERS,
                         ("S09","S02","S07","S10","S06"))
        self.assertEqual(FINAL_CHANCE_START,dt.datetime(2026,11,1,18,tzinfo=UTC))
        self.assertEqual(FINAL_CHANCE_END,dt.datetime(2026,11,2,5,30,tzinfo=UTC))

    def test_prioritizes_eligible_losers_only_inside_window(self):
        accounts=initial()
        # Before and after the challenge, ordinary ties break in ID order.
        before=FINAL_CHANCE_START-dt.timedelta(minutes=1)
        during=FINAL_CHANCE_START+dt.timedelta(minutes=1)
        after=FINAL_CHANCE_END
        self.assertEqual(choose_due_workers(accounts,[],before,5),
                         ["S01","S02","S03","S04","S05"])
        self.assertEqual(choose_due_workers(accounts,[],during,5),
                         list(sorted(FINAL_CHANCE_WORKERS)))
        self.assertEqual(choose_due_workers(accounts,[],after,5),
                         ["S01","S02","S03","S04","S05"])

    def test_recent_call_and_failure_backoff_cannot_be_bypassed(self):
        accounts=initial()
        now=FINAL_CHANCE_START+dt.timedelta(hours=2)
        history=[{"worker":"S09","cycle":(now-dt.timedelta(minutes=5)).isoformat(),
                  "status":"AI_UNAVAILABLE","ai_requests":1}]
        order=choose_due_workers(accounts,history,now,5)
        self.assertNotIn("S09",order)
        self.assertEqual(set(order),set(FINAL_CHANCE_WORKERS)-{"S09"}|{"S01"})

    def test_existing_default_fairness_is_unchanged(self):
        accounts=initial()
        now=FINAL_CHANCE_START+dt.timedelta(minutes=5)
        self.assertEqual(eligible_worker_order(accounts,[],now,5),
                         ["S01","S02","S03","S04","S05"])
        self.assertEqual(choose_due_workers(accounts,[],now,5),
                         list(sorted(FINAL_CHANCE_WORKERS)))


if __name__=="__main__":
    unittest.main()
