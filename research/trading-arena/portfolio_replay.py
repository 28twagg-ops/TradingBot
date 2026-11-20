"""Deterministic multi-asset Arena portfolio replay, research-only.

Decisions use prior completed hourly closes; orders fill at the next available
bar open. This is NOT executable-quote evidence or trusted promotion proof.
"""
import datetime as dt
import math
from zoneinfo import ZoneInfo
from run_virtual import COINS, TICKERS, signal, UTC

def replay(worker, generation, bars, start=None, end=None, cost=.0025):
    """bars: symbol -> ordered (UTC datetime, open, close) tuples."""
    if worker not in tuple("S%02d" % i for i in range(1, 11)):
        raise ValueError("UNKNOWN_WORKER")
    if not 0 <= cost < .1:
        raise ValueError("BAD_COST")
    universe = {s: rows for s, rows in bars.items()
                if s in TICKERS and (worker not in ("S09", "S10") or s in COINS)}
    if not universe:
        raise ValueError("NO_ELIGIBLE_BARS")
    by_time = {}
    for symbol, rows in universe.items():
        last = None
        for stamp, opening, close in rows:
            if not isinstance(stamp, dt.datetime) or stamp.tzinfo is None:
                raise ValueError("NAIVE_TIMESTAMP")
            stamp = stamp.astimezone(UTC)
            if last is not None and stamp <= last:
                raise ValueError("NON_MONOTONIC_BARS")
            if any(not isinstance(p, (float, int)) or not math.isfinite(p) or p <= 0
                   for p in (opening, close)):
                raise ValueError("BAD_PRICE")
            by_time.setdefault(stamp, {})[symbol] = (float(opening), float(close))
            last = stamp
    timeline = sorted(by_time)
    if len(timeline) < 100:
        raise ValueError("INSUFFICIENT_HISTORY")
    if start is None:
        start = timeline[60]
    if end is None:
        end = timeline[-1] + dt.timedelta(microseconds=1)
    cash, holdings = 100., {}
    closes = {s: [] for s in universe}
    marks, fills, peak, max_dd = [], 0, 100., 0.
    latest = {}
    for stamp in timeline:
        frame = by_time[stamp]
        eastern = stamp.astimezone(ZoneInfo("America/New_York"))
        stocks_open = eastern.weekday() < 5 and 9 <= eastern.hour < 16
        signals = {}
        for symbol, (opening, close) in frame.items():
            history = closes[symbol]
            if len(history) >= 60 and (symbol in COINS or stocks_open):
                signals[symbol] = signal(worker, history, generation)
        if start <= stamp < end:
            # Match live worker's sell-first, then first eligible buy ordering.
            acted = False
            for symbol in TICKERS:
                if symbol not in signals or signals[symbol] >= 0:
                    continue
                qty = holdings.get(symbol, 0.)
                if qty <= 1e-8:
                    continue
                opening = frame[symbol][0]
                proceeds = qty * opening * (1-cost)
                if proceeds <= 0:
                    continue
                cash += proceeds
                holdings[symbol] = 0.
                fills += 1
                acted = True
                break
            if not acted:
                for symbol in TICKERS:
                    if symbol not in signals or signals[symbol] <= 0:
                        continue
                    if holdings.get(symbol, 0.) > 1e-8:
                        continue
                    opening = frame[symbol][0]
                    budget = min(40., cash*.4)
                    qty = math.floor(budget/opening/1.01*1e6)/1e6
                    if qty*opening < 1 or qty*opening*(1+cost) > cash:
                        continue
                    cash -= qty*opening*(1+cost)
                    holdings[symbol] = qty
                    fills += 1
                    break
        for symbol, (_, close) in frame.items():
            closes[symbol].append(close)
            latest[symbol] = (stamp, close)
        if start <= stamp < end:
            # Never value a position from a stale or missing market mark.
            stale = [s for s, q in holdings.items() if q > 1e-8 and
                     (s not in latest or stamp-latest[s][0] > dt.timedelta(hours=3))]
            if stale:
                raise ValueError("STALE_POSITION_MARK")
            nav = cash + sum(q*latest[s][1] for s, q in holdings.items() if q > 1e-8)
            peak = max(peak, nav)
            max_dd = max(max_dd, 100*(1-nav/peak))
            marks.append((stamp.isoformat(), round(nav, 6)))
    if not marks:
        raise ValueError("NO_TEST_MARKS")
    return {"net_return_pct": round(marks[-1][1]-100, 4),
            "max_drawdown_pct": round(max_dd, 4),
            "fills": fills, "observations": len(marks),
            "equity_curve": marks, "status": "RESEARCH_ONLY"}

def compare_all(bars, registry):
    """Every active Arena worker, including crypto-only S09 and S10."""
    output = {}
    for i in range(1, 11):
        wid = "S%02d" % i
        generation = registry["workers"][wid]["index"]
        try:
            dates = sorted({stamp for rows in bars.values() for stamp, _, _ in rows})
            if len(dates) < 300:
                raise ValueError("INSUFFICIENT_OUT_OF_SAMPLE")
            split = dates[int(len(dates)*.7)]
            output[wid] = {
                "incumbent": replay(wid, generation, bars, start=split),
                "candidate": replay(wid, generation+1, bars, start=split),
                "status": "RESEARCH_ONLY_NO_PROMOTION"}
        except (ValueError, KeyError, TypeError) as exc:
            output[wid] = {"status": "UNAVAILABLE", "reason": str(exc)}
    return output
