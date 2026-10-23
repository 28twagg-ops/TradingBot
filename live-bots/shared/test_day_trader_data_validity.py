"""Regression tests: DayTrader S430–S432 reject stale / weekend / wrong-session bars."""
from __future__ import annotations

import sys
import unittest
from datetime import date, datetime, timedelta
from types import SimpleNamespace
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in (
    _ROOT / "live-bots" / "options-paper" / "strategies",
    _ROOT / "live-bots" / "options-paper" / "bot",
    _ROOT / "live-bots" / "options-paper" / "lab",
    _ROOT / "live-bots" / "shared",
):
    _s = str(_p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import options_signals as sig  # noqa: E402
import options_morning_bot as om  # noqa: E402

ET = ZoneInfo("America/New_York")
# Mid-session clock so incomplete-morning grace does not block unit tests.
_SESSION_NOW = datetime(2026, 10, 23, 10, 15, tzinfo=ET)


def _make_bars(end: date, n: int = 80, last_close_up: bool = True) -> pd.DataFrame:
    """Synthetic daily OHLCV ending on `end` with enough history for pattern prep."""
    idx = pd.bdate_range(end=end, periods=n, tz=ET)
    rng = np.random.default_rng(0)
    close = 100 + np.cumsum(rng.normal(0, 0.5, size=n))
    open_ = close - 0.2
    if last_close_up:
        open_[-1] = close[-1] - 1.0  # drive ~1%
        high = np.maximum(open_, close) + 0.5
        high[-1] = open_[-1] * 1.005
    else:
        high = np.maximum(open_, close) + 0.1
    low = np.minimum(open_, close) - 0.3
    vol = np.full(n, 1_000_000.0)
    return pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": vol},
        index=idx,
    )


class DayTraderBarValidityTests(unittest.TestCase):
    def tearDown(self):
        sig.clear_spy_context()

    def test_accepts_today_session_bar(self):
        today = date(2026, 10, 23)  # Friday
        bars = _make_bars(today)
        df, last = sig._day_trader_bar(bars, today, now=_SESSION_NOW)
        self.assertIsNotNone(df)
        self.assertIsNotNone(last)
        self.assertIsNone(
            sig._day_trader_bar_reject_reason(bars, today, now=_SESSION_NOW)
        )

    def test_rejects_yesterday_fallback(self):
        today = date(2026, 10, 23)
        yesterday = date(2026, 10, 22)
        bars = _make_bars(yesterday)
        df, last = sig._day_trader_bar(bars, today, now=_SESSION_NOW)
        self.assertIsNone(df)
        self.assertIsNone(last)
        reason = sig._day_trader_bar_reject_reason(bars, today, now=_SESSION_NOW)
        self.assertIsNotNone(reason)
        self.assertIn("stale_session", reason)

    def test_s430_no_signal_on_stale_bars(self):
        today = date(2026, 10, 23)
        bars = _make_bars(date(2026, 10, 22), last_close_up=True)
        hit = sig.scan_orb_opening_drive(bars, "AAPL", today, now=_SESSION_NOW)
        self.assertIsNone(hit)

    def test_s430_fires_on_valid_opening_drive(self):
        today = date(2026, 10, 23)
        bars = _make_bars(today, last_close_up=True)
        # Ensure prior close for mild gap (>= -0.5%)
        hit = sig.scan_orb_opening_drive(bars, "AAPL", today, now=_SESSION_NOW)
        self.assertIsNotNone(hit)
        self.assertEqual(hit.strategy_id, "S430")
        self.assertIn("ORB-drive", hit.detail)

    def test_weekend_session_rejected(self):
        saturday = date(2026, 10, 24)
        # bdate_range end=Saturday still ends Friday
        bars = _make_bars(date(2026, 10, 23))
        df, last = sig._day_trader_bar(bars, saturday, now=_SESSION_NOW)
        self.assertIsNone(df)
        self.assertIsNone(last)

    def test_rejects_incomplete_morning_observation(self):
        today = date(2026, 10, 23)
        bars = _make_bars(today, last_close_up=True)
        too_early = datetime(2026, 10, 23, 9, 32, tzinfo=ET)
        reason = sig._day_trader_bar_reject_reason(bars, today, now=too_early)
        self.assertIsNotNone(reason)
        self.assertIn("incomplete_morning_obs", reason)
        self.assertIsNone(
            sig.scan_orb_opening_drive(bars, "AAPL", today, now=too_early)
        )

    def test_rejects_future_bar_leakage(self):
        today = date(2026, 10, 23)
        bars = _make_bars(today, last_close_up=True)
        # Force last index into the future relative to session clock.
        idx = list(bars.index)
        idx[-1] = pd.Timestamp(datetime(2026, 10, 23, 15, 0, tzinfo=ET))
        bars = bars.copy()
        bars.index = pd.DatetimeIndex(idx, tz=ET)
        early = datetime(2026, 10, 23, 10, 0, tzinfo=ET)
        reason = sig._day_trader_bar_reject_reason(bars, today, now=early)
        self.assertIsNotNone(reason)
        self.assertIn("future_bar", reason)

    def test_spy_context_rejects_stale(self):
        today = date(2026, 10, 23)
        spy = _make_bars(date(2026, 10, 22))
        sig.set_spy_context(spy, today)
        self.assertIsNone(sig._SPY_CTX)

    def test_spy_context_accepts_today(self):
        today = date(2026, 10, 23)
        spy = _make_bars(today)
        sig.set_spy_context(spy, today)
        self.assertIsNotNone(sig._SPY_CTX)
        self.assertEqual(sig._SPY_CTX.get("session_date"), str(today))

    def test_s431_requires_spy_and_fresh_bar(self):
        today = date(2026, 10, 23)
        bars = _make_bars(today, last_close_up=True)
        sig.clear_spy_context()
        self.assertIsNone(sig.scan_rs_vs_spy(bars, "AAPL", today, now=_SESSION_NOW))
        # Stale stock with fresh SPY still rejects
        spy = _make_bars(today)
        sig.set_spy_context(spy, today)
        stale = _make_bars(date(2026, 10, 22), last_close_up=True)
        self.assertIsNone(sig.scan_rs_vs_spy(stale, "AAPL", today, now=_SESSION_NOW))

    def test_missing_bars(self):
        today = date(2026, 10, 23)
        self.assertEqual(
            sig._day_trader_bar_reject_reason(pd.DataFrame(), today, now=_SESSION_NOW),
            "missing_bars",
        )


class DiskCacheFreshnessTests(unittest.TestCase):
    def test_disk_cache_fresh_respects_ttl(self):
        import tempfile
        from pathlib import Path
        import time as _time

        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "bars.parquet"
            p.write_bytes(b"x")
            old_ttl = om._BARS_CACHE_TTL_S
            try:
                om._BARS_CACHE_TTL_S = 60.0
                self.assertTrue(om._disk_cache_fresh(p))
                # Age the file beyond TTL
                past = _time.time() - 120
                import os
                os.utime(p, (past, past))
                self.assertFalse(om._disk_cache_fresh(p))
            finally:
                om._BARS_CACHE_TTL_S = old_ttl

    def test_rth_developing_flag(self):
        mid = datetime(2026, 10, 23, 11, 0, tzinfo=ET)
        self.assertTrue(om._in_rth_developing(mid))
        after = datetime(2026, 10, 23, 17, 0, tzinfo=ET)
        self.assertFalse(om._in_rth_developing(after))
        weekend = datetime(2026, 10, 24, 11, 0, tzinfo=ET)
        self.assertFalse(om._in_rth_developing(weekend))


class SnapshotFreshnessTests(unittest.TestCase):
    def test_bar_row_rejects_missing_timestamp(self):
        bar = SimpleNamespace(
            open=1, high=2, low=0.5, close=1.5, volume=100, timestamp=None,
        )
        self.assertIsNone(om._bar_row_from_snap_bar(bar, retrieval_ts=datetime.now(ET)))

    def test_bar_row_keeps_observation_not_retrieval(self):
        obs = datetime(2026, 10, 23, 9, 35, tzinfo=ET)
        retrieval = datetime(2026, 10, 23, 12, 0, tzinfo=ET)
        bar = SimpleNamespace(
            open=10, high=11, low=9, close=10.5, volume=1e6, timestamp=obs,
        )
        row = om._bar_row_from_snap_bar(bar, retrieval_ts=retrieval)
        self.assertIsNotNone(row)
        self.assertEqual(pd.Timestamp(row["timestamp"]), pd.Timestamp(obs))
        self.assertEqual(row["retrieval_ts"], retrieval)

    def test_backfill_rejects_stale_daily_bar(self):
        today = date(2026, 10, 23)
        # Empty base frame with MultiIndex columns expected by concat path
        base = pd.DataFrame(
            {"open": [100.0], "high": [101.0], "low": [99.0], "close": [100.5], "volume": [1e6]},
            index=pd.MultiIndex.from_tuples(
                [("ZZZ", pd.Timestamp(datetime(2026, 10, 22, 16, 0, tzinfo=ET)))],
                names=["symbol", "timestamp"],
            ),
        )
        stale_ts = datetime(2026, 10, 22, 16, 0, tzinfo=ET)
        daily = SimpleNamespace(
            open=50, high=51, low=49, close=50.5, volume=1e6, timestamp=stale_ts,
        )
        snap = SimpleNamespace(daily_bar=daily)
        stock = SimpleNamespace(
            get_stock_snapshot=lambda *a, **kw: {"AAPL": snap},
        )
        out = om._backfill_today_from_snapshots(stock, base, ["AAPL"], today)
        # Stale AAPL must not appear as today
        try:
            sub = out.xs("AAPL", level=0)
            last = pd.Timestamp(sub.index.max())
            if last.tzinfo:
                last = last.tz_convert(ET)
            self.assertNotEqual(last.date(), today)
        except KeyError:
            pass  # AAPL absent — also fine


if __name__ == "__main__":
    unittest.main()
