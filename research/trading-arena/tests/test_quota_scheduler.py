"""API-free fairness, rollover, provider cooldown and daily pacing tests."""
import datetime as dt
import unittest
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from quota_scheduler import (
    DAILY_REQUEST_TARGET, SUCCESS, MAX_BATCH, remaining_time_paced_credit,
    eligible_worker_order, read_provider_headers, cooldown_deadline,
    cooldown_active, seconds_for_duration, counted_provider_attempt,
    spacing_seconds)
from run_virtual import initial, UTC

class QuotaSchedulerTests(unittest.TestCase):
    def test_utc_credit_released_across_day_instead_of_spent_before_lunch(self):
        morning=dt.datetime(2026,10,28,0,0,tzinfo=UTC)
        midday=morning+dt.timedelta(hours=12)
        late=morning+dt.timedelta(hours=23,minutes=59)
        self.assertEqual(remaining_time_paced_credit(morning,[]),1)
        self.assertEqual(remaining_time_paced_credit(midday,[]),37)
        self.assertEqual(remaining_time_paced_credit(late,[]),DAILY_REQUEST_TARGET)
        events=[{"worker":"S01","cycle":"2026-10-28T01:00Z",
                 "status":"AI_UNAVAILABLE","ai_requests":1,
                 "safe_error":"GROQ_HTTP_429_rate_limit_exceeded"}]
        self.assertEqual(remaining_time_paced_credit(midday,events),36)
    def test_older_rate_limits_count_even_when_old_runner_wrongly_logged_zero(self):
        legacy={"cycle":"2026-10-28T01:00Z","status":"AI_UNAVAILABLE",
                "ai_requests":0,"safe_error":"GROQ_HTTP_429_rate_limit_exceeded"}
        self.assertTrue(counted_provider_attempt(legacy))
        self.assertFalse(counted_provider_attempt(
            {"cycle":"2026-10-28T01:00Z","status":"QUARANTINED_BAD_LEDGER",
             "ai_requests":0}))
    def test_failed_worker_is_first_in_line_after_gap_when_others_succeeded(self):
        now=dt.datetime(2026,10,28,14,0,tzinfo=UTC)
        accounts=initial()
        # S01 failed 50 minutes ago, while everyone else completed a session.
        history=[{"worker":"S01","cycle":"2026-10-28T13:05Z",
                  "status":"AI_UNAVAILABLE","ai_requests":1,
                  "safe_error":"GROQ_HTTP_429_rate_limit_exceeded"}]
        for i in range(2,11):
            accounts[f"S{i:02d}"]["groq_experiments"]=[{"id":"ok"}]
            history.append({"worker":f"S{i:02d}","cycle":"2026-10-28T12:00Z",
                            "status":"RESEARCHED","ai_requests":1})
        self.assertEqual(eligible_worker_order(accounts,history,now,1),["S01"])
    def test_repeated_failed_attempts_do_not_monopolize_entire_day(self):
        now=dt.datetime(2026,10,28,14,0,tzinfo=UTC)
        a=initial()
        past=[{"worker":"S01","cycle":f"2026-10-28T{h:02d}:00Z",
               "status":"AI_UNAVAILABLE","safe_error":"GROQ_HTTP_429",
               "ai_requests":1} for h in (6,8,10,12)]
        # No bot has succeeded today. S02 has never been given a chance.
        order=eligible_worker_order(a,past,now,5)
        self.assertNotIn("S01",order)
        self.assertEqual(order[0],"S02")

    def test_research_idea_counts_as_success_for_fair_rotation(self):
        now=dt.datetime(2026,10,28,14,0,tzinfo=UTC)
        a=initial()
        for id in a:
            a[id]["groq_experiments"]=[{"id":"example"}]
        events=[{"worker":"S01","cycle":"2026-10-28T12:00Z",
                 "status":"RESEARCH_IDEA_NEEDS_DATA","ai_requests":1},
                {"worker":"S02","cycle":"2026-10-28T12:00Z",
                 "status":"AI_UNAVAILABLE","ai_requests":1}]
        for number in range(3,11):
            events.append({"worker":f"S{number:02d}","cycle":"2026-10-28T12:00Z",
                           "status":"RESEARCHED","ai_requests":1})
        self.assertEqual(eligible_worker_order(a,events,now,1),["S02"])
        self.assertEqual(SUCCESS,{"RESEARCHED","RESEARCH_IDEA_NEEDS_DATA",
                                  "RESEARCH_IDEA_NEEDS_REVISION"})
    def test_immediate_duplicate_run_skips_recent_workers(self):
        a=initial()
        now=dt.datetime(2026,10,28,14,0,tzinfo=UTC)
        events=[{"worker":"S01","cycle":"2026-10-28T13:55Z","status":"RESEARCHED"}]
        self.assertNotIn("S01",eligible_worker_order(a,events,now,5))
    def test_multiple_consecutive_failures_trigger_finite_backoff(self):
        now=dt.datetime(2026,10,28,14,0,tzinfo=UTC)
        a=initial()
        failed=[{"worker":"S07","cycle":f"2026-10-28T{h}:00Z",
                 "status":"REJECTED_INVALID_MODEL_EXPERIMENT"} for h in ("10","11","13")]
        self.assertNotIn("S07",eligible_worker_order(a,failed,now,5))
        self.assertIn("S07",eligible_worker_order(a,failed,
            now+dt.timedelta(minutes=25),5))

    def test_only_provider_numeric_headers_are_stored(self):
        headers={"X-RateLimit-Remaining-Requests":"39",
                 "X-RateLimit-Remaining-Tokens":"2900",
                 "X-RateLimit-Reset-Tokens":"7.66s",
                 "Retry-After":"4",
                 "Authorization":"Bearer MUST_NOT_LEAK"}
        meta=read_provider_headers(headers)
        self.assertEqual(meta["remaining_daily_requests"],39)
        self.assertEqual(meta["remaining_minute_tokens"],2900)
        self.assertEqual(meta["retry_after_seconds"],4)
        self.assertNotIn("Authorization",str(meta))
        self.assertGreaterEqual(spacing_seconds(meta),40)
    def test_provider_cooldown_uses_retry_after_and_daily_reset(self):
        now=dt.datetime(2026,10,28,14,0,tzinfo=UTC)
        wait=cooldown_deadline(now,{"retry_after_seconds":140},429)
        self.assertTrue(cooldown_active({"cooldown_until":wait},now))
        self.assertFalse(cooldown_active({"cooldown_until":wait},now+dt.timedelta(minutes=4)))
        reset=cooldown_deadline(now,{"remaining_daily_requests":0,
                                    "reset_daily_seconds":3600},429)
        self.assertTrue(cooldown_active({"cooldown_until":reset},
                                         now+dt.timedelta(minutes=59)))
    def test_time_headers_support_mixed_units(self):
        self.assertAlmostEqual(seconds_for_duration("2m59.56s"),179.56)
        self.assertEqual(seconds_for_duration("7.66s"),7.66)
        self.assertIsNone(seconds_for_duration("garbage"))
    def test_bounded_batch_preserves_provider_limit(self):
        now=dt.datetime(2026,10,28,14,0,tzinfo=UTC)
        with self.assertRaises(ValueError):
            eligible_worker_order(initial(),[],now,MAX_BATCH+1)

if __name__=="__main__":
    unittest.main()
