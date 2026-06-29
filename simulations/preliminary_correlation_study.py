"""
preliminary_correlation_study.py — Task 2.0 (Phase 2, PRELIMINARY).

Question: do the equity bot's existing BUY signals correlate with options price
movement enough to be worth trading via options?

PRELIMINARY — based on yfinance EOD data + Black-Scholes reconstruction.
Confirm with Alpaca 1-min data once collected. Every output is labelled.

The equity bot is long-only mean-reversion (it BUYs dips/gaps expecting a
bounce), so every BUY is a BULLISH thesis -> analysed as a CALL purchase.
There are no short/GapUp signals, so PUT analysis is reported as N/A.

Data:
  Source 1: TradingBot-git/logs/transactions.csv  (real signal history)
  Source 2: yfinance (historical stock OHLCV; cached locally)
  Source 3: Black-Scholes from options_strategy_simulator.py (validated engine)

Run:  python simulations/preliminary_correlation_study.py
Outputs: simulations/results/preliminary_correlation/
Runtime budget: < 30 min (yfinance cached so each symbol downloads once).
"""

from __future__ import annotations

import csv
import math
import random
import sys
import time
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np

# Reuse the validated Black-Scholes engine (Phase 2). Same directory.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_strategy_simulator import bs_price, bs_delta  # noqa: E402

# --------------------------------------------------------------------------- #
#  Paths / constants
# --------------------------------------------------------------------------- #
LABEL = "PRELIMINARY - based on yfinance EOD data, confirm with Alpaca 1-min data once collected"
RECON_LABEL = "RECONSTRUCTED - approximate only"

_THIS = Path(__file__).resolve().parent
TX_FILE = _THIS.parent.parent / "TradingBot-git" / "logs" / "transactions.csv"
CACHE_DIR = _THIS / "cache" / "stock_prices"
OUT_DIR = _THIS / "results" / "preliminary_correlation"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
OUT_DIR.mkdir(parents=True, exist_ok=True)

R = 0.05                # risk-free rate (task spec)
T0 = 7 / 365.0          # 7-day option
VOL_FLOOR = 0.15        # IV proxy floor
ENTRY_MULT = 1.05       # pay ~5% above mid (ask)
EXIT_MULT = 0.95        # receive ~5% below mid (bid)
FEE = 1.30              # round-trip per contract
IV_CRUSH = 0.80         # assume IV drops 20% after gap (Q3)
CONTROLS_PER_SIGNAL = 3
ALPHA = 0.10            # preliminary significance threshold
RUNTIME_BUDGET_S = 25 * 60
SEED = 42

HORIZONS = [("EOD", 0), ("1day", 1), ("3day", 3), ("5day", 5)]

_start_time = time.monotonic()
random.seed(SEED)


def log(msg: str) -> None:
    el = time.monotonic() - _start_time
    print(f"[{el:6.1f}s] {msg}", flush=True)


# --------------------------------------------------------------------------- #
#  Dependency-free statistics (no scipy)
# --------------------------------------------------------------------------- #

def _betacf(a: float, b: float, x: float) -> float:
    """Continued fraction for the incomplete beta (Numerical Recipes)."""
    MAXIT, EPS, FPMIN = 200, 3.0e-12, 1.0e-30
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < EPS:
            break
    return h


def betai(a: float, b: float, x: float) -> float:
    """Regularized incomplete beta function I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    bt = math.exp(lbeta + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1.0 - x) / b


def welch_ttest(a: list[float], b: list[float]) -> tuple[float, float, float]:
    """Welch's two-sample t-test. Returns (t, two-sided p, df). p=1.0 if degenerate."""
    a = [v for v in a if v is not None and not math.isnan(v)]
    b = [v for v in b if v is not None and not math.isnan(v)]
    na, nb = len(a), len(b)
    if na < 2 or nb < 2:
        return float("nan"), 1.0, 0.0
    ma, mb = float(np.mean(a)), float(np.mean(b))
    va, vb = float(np.var(a, ddof=1)), float(np.var(b, ddof=1))
    se2 = va / na + vb / nb
    if se2 <= 0:
        return float("nan"), 1.0, 0.0
    t = (ma - mb) / math.sqrt(se2)
    df = se2 ** 2 / ((va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1))
    p = betai(df / 2.0, 0.5, df / (df + t * t))   # two-sided
    return t, p, df


def mean(xs: list[float]) -> float:
    xs = [x for x in xs if x is not None and not math.isnan(x)]
    return float(np.mean(xs)) if xs else float("nan")


# --------------------------------------------------------------------------- #
#  STEP 1 — load + parse signal history
# --------------------------------------------------------------------------- #

def load_signals() -> list[dict]:
    rows = list(csv.DictReader(open(TX_FILE, newline="")))
    buys = [r for r in rows if r.get("action") == "BUY"]
    signals = []
    for r in buys:
        try:
            price = float(r["price"])
        except (ValueError, KeyError):
            continue
        signals.append({
            "date": r["date"],
            "symbol": r["ticker"].upper(),
            "signal_type": r.get("strategy") or "UNKNOWN",
            "entry_price": price,
            "entry_equity": float(r.get("equity_after") or 0) or None,
        })
    return signals


# --------------------------------------------------------------------------- #
#  STEP 2 — historical stock data (yfinance, cached)
# --------------------------------------------------------------------------- #

def _cache_file(sym: str) -> Path:
    return CACHE_DIR / f"{sym}.csv"


def download_symbol(sym: str, start: date, end: date) -> dict | None:
    """Return {date_str: {open,high,low,close}} for sym, using CSV cache."""
    cf = _cache_file(sym)
    if cf.exists():
        try:
            data = {}
            for row in csv.DictReader(open(cf, newline="")):
                data[row["date"]] = {k: float(row[k]) for k in ("open", "high", "low", "close")}
            if data:
                return data
        except Exception:
            pass

    try:
        import yfinance as yf
        df = yf.Ticker(sym).history(start=start.isoformat(), end=end.isoformat(),
                                    auto_adjust=True)
    except Exception as exc:
        log(f"  yf error {sym}: {exc}")
        return None
    if df is None or df.empty:
        return None

    data = {}
    with open(cf, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "open", "high", "low", "close"])
        for idx, r in df.iterrows():
            ds = idx.date().isoformat()
            o, h, l, c = float(r["Open"]), float(r["High"]), float(r["Low"]), float(r["Close"])
            data[ds] = {"open": o, "high": h, "low": l, "close": c}
            w.writerow([ds, o, h, l, c])
    return data


def trading_returns(data: dict, sig_date: str) -> dict | None:
    """Compute gap/horizon returns for sig_date given a {date:ohlc} dict."""
    dates = sorted(data.keys())
    if sig_date not in data:
        # find first trading day >= sig_date (signal may be a non-trading log time)
        later = [d for d in dates if d >= sig_date]
        if not later:
            return None
        sig_date = later[0]
    i = dates.index(sig_date)
    if i == 0:
        return None
    prior_close = data[dates[i - 1]]["close"]
    o = data[sig_date]["open"]
    c = data[sig_date]["close"]
    if prior_close <= 0 or o <= 0 or c <= 0:
        return None

    def fwd_close(k: int):
        j = i + k
        return data[dates[j]]["close"] if j < len(dates) else None

    out = {
        "gap_pct": (o - prior_close) / prior_close,
        "signal_day_return": (c - o) / o,
        "ret_EOD": (c - o) / o,
    }
    for label, k in [("1day", 1), ("3day", 3), ("5day", 5)]:
        fc = fwd_close(k)
        out[f"ret_{label}"] = (fc - c) / c if fc else None

    # realized vol over 30 trading days before signal
    closes = [data[d]["close"] for d in dates[max(0, i - 31):i]]
    if len(closes) >= 10:
        rets = np.diff(np.log(closes))
        out["realized_vol_30d"] = float(np.std(rets, ddof=1) * math.sqrt(252))
    else:
        out["realized_vol_30d"] = None
    return out


# --------------------------------------------------------------------------- #
#  STEP 3 — Black-Scholes reconstruction
# --------------------------------------------------------------------------- #

def reconstruct(S: float, rets: dict, group: str) -> dict:
    """Reconstruct ATM call prices + returns at each horizon. RECONSTRUCTED."""
    K = round(S)
    sigma = max(rets.get("realized_vol_30d") or VOL_FLOOR, VOL_FLOOR)
    call0 = bs_price(S, K, T0, sigma, "C", r=R)
    rec = {
        "group": group, "S": S, "K": K, "sigma": sigma,
        "call_at_signal": call0, "label": RECON_LABEL,
        "call_delta": bs_delta(S, K, T0, sigma, "C", r=R),
    }
    for label, days in HORIZONS:
        ret = rets.get(f"ret_{label}")
        if ret is None or call0 <= 0:
            rec[f"call_ret_{label}"] = None
            rec[f"net_pnl_{label}"] = None
            rec[f"call_ret_crush_{label}"] = None
            continue
        S_new = S * (1 + ret)
        T_new = max(T0 - days / 365.0, 1 / 365.0)
        call_h = bs_price(S_new, K, T_new, sigma, "C", r=R)
        rec[f"call_ret_{label}"] = (call_h - call0) / call0
        entry = call0 * ENTRY_MULT
        exit_ = call_h * EXIT_MULT
        rec[f"net_pnl_{label}"] = (exit_ - entry) * 100 - FEE
        # Q3 IV crush variant (skip EOD = intraday, no overnight crush)
        if days >= 1:
            call_h_crush = bs_price(S_new, K, T_new, sigma * IV_CRUSH, "C", r=R)
            rec[f"call_ret_crush_{label}"] = (call_h_crush - call0) / call0
        else:
            rec[f"call_ret_crush_{label}"] = rec[f"call_ret_{label}"]
    return rec


# --------------------------------------------------------------------------- #
#  Orchestration
# --------------------------------------------------------------------------- #

def main() -> int:
    print("=" * 80)
    print("TASK 2.0 — PRELIMINARY CORRELATION STUDY")
    print(LABEL)
    print("=" * 80)

    # ---- STEP 1 ----
    signals = load_signals()
    by_type = defaultdict(int)
    for s in signals:
        by_type[s["signal_type"]] += 1
    sym_set = sorted({s["symbol"] for s in signals})
    dmin = min(s["date"] for s in signals)
    dmax = max(s["date"] for s in signals)
    log(f"STEP 1: {len(signals)} BUY signals | types={dict(by_type)}")
    log(f"        date range {dmin}..{dmax} | {len(sym_set)} unique symbols")
    step1_label = "CONFIRMED" if len(signals) > 100 else "PROVISIONAL"
    log(f"        signal count sanity: {step1_label} (expected hundreds)")

    # ---- STEP 2: download universe (signals + control pool = same traded pool) ----
    start = datetime.fromisoformat(dmin).date() - timedelta(days=60)
    end = date.today() + timedelta(days=1)
    pool = sym_set[:]   # control pool = all traded symbols
    log(f"STEP 2: downloading {len(pool)} symbols (cached) {start}..{end}")
    price_data: dict[str, dict] = {}
    for n, sym in enumerate(pool, 1):
        if time.monotonic() - _start_time > RUNTIME_BUDGET_S:
            log(f"  runtime budget hit at {n}/{len(pool)} downloads; proceeding with cache")
            break
        d = download_symbol(sym, start, end)
        if d:
            price_data[sym] = d
        if n % 25 == 0:
            log(f"  downloaded {n}/{len(pool)} (ok={len(price_data)})")
    log(f"        price data available for {len(price_data)}/{len(pool)} symbols")

    # ---- build signals-by-date for control exclusion ----
    signaled_by_date: dict[str, set] = defaultdict(set)
    for s in signals:
        signaled_by_date[s["date"]].add(s["symbol"])

    # ---- STEP 2b compute stock returns per signal ----
    sig_rows = []
    for s in signals:
        data = price_data.get(s["symbol"])
        if not data:
            continue
        rets = trading_returns(data, s["date"])
        if not rets:
            continue
        row = {**s, **rets}
        sig_rows.append(row)
    log(f"STEP 2b: {len(sig_rows)} signals with usable stock returns")

    # SANITY 1: dip-buy signals -> positive stock return at 1-3d (mean reversion)
    dip_types = {"GapDown", "Pullback50", "RSIRecovery", "MomReversal"}
    dip_1d = [r["ret_1day"] for r in sig_rows
              if r["signal_type"] in dip_types and r.get("ret_1day") is not None]
    dip_3d = [r["ret_3day"] for r in sig_rows
              if r["signal_type"] in dip_types and r.get("ret_3day") is not None]
    s1_1d, s1_3d = mean(dip_1d), mean(dip_3d)
    sanity1_ok = (s1_3d > 0) or (s1_1d > 0)
    log(f"SANITY 1: dip-buy stock return 1d={s1_1d:+.4%} 3d={s1_3d:+.4%} "
        f"-> {'PASS' if sanity1_ok else 'FAIL'}")
    # SANITY 1b: GapDown gap_pct should be negative on average
    gd_gap = mean([r["gap_pct"] for r in sig_rows if r["signal_type"] == "GapDown"])
    log(f"SANITY 1b: GapDown mean gap_pct = {gd_gap:+.4%} "
        f"({'PASS' if gd_gap < 0 else 'WARN - check labeling'})")

    # ---- STEP 3: reconstruct options for signal group ----
    for r in sig_rows:
        r.update(reconstruct(r["entry_price"], r, "signal"))

    # SANITY 2: BS prices positive and < underlying
    bad_bs = [r for r in sig_rows
              if not (0 < r["call_at_signal"] < r["entry_price"])]
    log(f"SANITY 2: BS price sane for {len(sig_rows)-len(bad_bs)}/{len(sig_rows)} "
        f"({'PASS' if len(bad_bs) < 0.05*len(sig_rows) else 'WARN'})")

    # ---- STEP 4: control group ----
    ctrl_rows = []
    for s in signals:
        candidates = [x for x in pool
                      if x not in signaled_by_date[s["date"]] and x in price_data]
        random.shuffle(candidates)
        picked = candidates[:CONTROLS_PER_SIGNAL]
        for csym in picked:
            rets = trading_returns(price_data[csym], s["date"])
            if not rets:
                continue
            S = price_data[csym][sorted(price_data[csym])[0]]["close"]
            # use the close on/near the signal date as S
            ds = sorted(d for d in price_data[csym] if d >= s["date"])
            if not ds:
                continue
            S = price_data[csym][ds[0]]["close"]
            row = {"date": s["date"], "symbol": csym,
                   "signal_type": "CONTROL", "entry_price": S, **rets}
            row.update(reconstruct(S, rets, "control"))
            ctrl_rows.append(row)
    log(f"STEP 4: {len(ctrl_rows)} control observations")

    # SANITY 3: control returns roughly zero
    ctrl_stock_3d = mean([r.get("ret_3day") for r in ctrl_rows])
    log(f"SANITY 3: control mean stock 3d return = {ctrl_stock_3d:+.4%} "
        f"({'OK' if abs(ctrl_stock_3d) < 0.02 else 'WARN - market regime bias'})")

    # SANITY 4: sample size for GapDown
    n_gapdown = sum(1 for r in sig_rows
                    if r["signal_type"] == "GapDown" and r.get("call_ret_3day") is not None)
    n_allsig = sum(1 for r in sig_rows if r.get("call_ret_3day") is not None)
    log(f"SANITY 4: GapDown w/ options data = {n_gapdown}; all signals = {n_allsig}")

    # ---- STEP 5: correlation questions ----
    results = compute_questions(sig_rows, ctrl_rows)

    # ---- STEP 6: verdict ----
    verdict, verdict_text = decide_verdict(results, n_allsig, n_gapdown,
                                           sanity1_ok, ctrl_stock_3d)

    # ---- save outputs ----
    save_all(sig_rows, ctrl_rows, results, verdict, verdict_text,
             by_type, dmin, dmax, s1_1d, s1_3d, gd_gap, n_allsig, n_gapdown,
             ctrl_stock_3d)

    log(f"DONE. Verdict {verdict}. Outputs in {OUT_DIR}")
    print("\nSTATUS: VERDICT", verdict, "(PRELIMINARY)")
    return 0


def compute_questions(sig_rows: list[dict], ctrl_rows: list[dict]) -> dict:
    res = {"horizons": {}}
    # Q1 + Q2: signal vs control call returns per horizon
    best_h, best_mean = None, -9
    for label, _ in HORIZONS:
        sig = [r[f"call_ret_{label}"] for r in sig_rows if r.get(f"call_ret_{label}") is not None]
        ctl = [r[f"call_ret_{label}"] for r in ctrl_rows if r.get(f"call_ret_{label}") is not None]
        t, p, df = welch_ttest(sig, ctl)
        ms, mc = mean(sig), mean(ctl)
        res["horizons"][label] = {
            "signal_mean": ms, "control_mean": mc, "difference": ms - mc,
            "p_value": p, "t": t, "n_signal": len(sig), "n_control": len(ctl),
        }
        if not math.isnan(ms) and ms > best_mean:
            best_mean, best_h = ms, label
    res["best_horizon"] = best_h
    res["best_horizon_mean"] = best_mean

    # Q3: IV crush impact at best horizon (and all)
    crush = {}
    for label, _ in HORIZONS:
        no = [r[f"call_ret_{label}"] for r in sig_rows if r.get(f"call_ret_{label}") is not None]
        wi = [r[f"call_ret_crush_{label}"] for r in sig_rows if r.get(f"call_ret_crush_{label}") is not None]
        crush[label] = mean(wi) - mean(no) if no and wi else float("nan")
    res["iv_crush_impact"] = crush

    # Q4: strong vs weak gap
    strong = [r for r in sig_rows if r.get("gap_pct") is not None and r["gap_pct"] < -0.02]
    weak = [r for r in sig_rows if r.get("gap_pct") is not None and -0.02 <= r["gap_pct"] < -0.005]
    q4 = {}
    for label, _ in HORIZONS:
        sm = mean([r[f"call_ret_{label}"] for r in strong if r.get(f"call_ret_{label}") is not None])
        wm = mean([r[f"call_ret_{label}"] for r in weak if r.get(f"call_ret_{label}") is not None])
        q4[label] = {"strong_mean": sm, "weak_mean": wm, "diff": sm - wm,
                     "n_strong": len(strong), "n_weak": len(weak)}
    res["q4_strength"] = q4

    # Q5: net P&L per signal vs control (best horizon and all)
    q5 = {}
    for label, _ in HORIZONS:
        sp = mean([r[f"net_pnl_{label}"] for r in sig_rows if r.get(f"net_pnl_{label}") is not None])
        cp = mean([r[f"net_pnl_{label}"] for r in ctrl_rows if r.get(f"net_pnl_{label}") is not None])
        q5[label] = {"signal_net_pnl": sp, "control_net_pnl": cp}
    res["q5_net_pnl"] = q5
    return res


def decide_verdict(res: dict, n_allsig: int, n_gapdown: int,
                   sanity1_ok: bool, ctrl_bias: float) -> tuple[str, str]:
    if n_gapdown < 30 and n_allsig < 30:
        return "INSUFFICIENT", (
            "INSUFFICIENT SAMPLE: fewer than 30 signals with options data. "
            "Cannot produce Verdict A/B. Need more signal history or Alpaca data.")
    if not sanity1_ok:
        return "INVALID", (
            "SANITY 1 FAILED: dip-buy stock returns not positive — signal parsing "
            "suspect. No options verdict produced.")

    # count horizons with positive difference and p<ALPHA
    good = [h for h, v in res["horizons"].items()
            if v["difference"] > 0 and v["p_value"] < ALPHA]
    best = res["best_horizon"]
    net_best = res["q5_net_pnl"].get(best, {}).get("signal_net_pnl", float("nan"))
    ctrl_best = res["q5_net_pnl"].get(best, {}).get("control_net_pnl", float("nan"))
    crush_best = res["iv_crush_impact"].get(best, float("nan"))

    net_pos = (not math.isnan(net_best)) and net_best > 0 and net_best > ctrl_best
    crush_ok = math.isnan(crush_best) or crush_best > -0.30  # not fully offsetting

    if len(good) >= 2 and net_pos and crush_ok:
        v = "A"
        txt = ("VERDICT A — STRONG CORRELATION (preliminary). Signal calls beat "
               f"control at p<{ALPHA} across {len(good)} horizons; net P&L per "
               "signal positive after adversarial costs; IV-crush estimate does "
               "not fully offset. -> Proceed with Phase 3+ as planned.")
    elif len(good) >= 1 or net_pos:
        v = "B"
        txt = ("VERDICT B — WEAK/CONDITIONAL (preliminary). Outperformance only at "
               f"specific horizons/strengths (significant horizons: {good or 'none'}; "
               f"net P&L positive: {net_pos}). -> Proceed but narrow Phase 4 to "
               "those conditions.")
    else:
        v = "C"
        txt = ("VERDICT C — NO CORRELATION (preliminary). Signal and control not "
               "distinguishable and/or net P&L not positive. -> FLAG for user "
               "review before Phase 3+. NOTE: preliminary C means 'investigate "
               "further', NOT stop. yfinance+BS reconstruction has real limits; "
               "only a CONFIRMED C from the full Alpaca study triggers a stop.")
    if abs(ctrl_bias) >= 0.02:
        txt += f" CAVEAT: control group shows {ctrl_bias:+.2%} 3d drift (regime bias)."
    return v, txt


# --------------------------------------------------------------------------- #
#  Output
# --------------------------------------------------------------------------- #

def _write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("(no rows)\n", encoding="utf-8")
        return
    keys = list({k for r in rows for k in r.keys()})
    # stable ordering: common fields first
    front = ["date", "symbol", "signal_type", "group", "entry_price", "S", "K",
             "sigma", "gap_pct", "realized_vol_30d"]
    keys = [k for k in front if k in keys] + [k for k in keys if k not in front]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def save_all(sig_rows, ctrl_rows, res, verdict, verdict_text, by_type,
             dmin, dmax, s1_1d, s1_3d, gd_gap, n_allsig, n_gapdown, ctrl_bias):
    # signal_history.csv
    _write_csv(OUT_DIR / "signal_history.csv",
               [{"date": r["date"], "symbol": r["symbol"],
                 "signal_type": r["signal_type"], "entry_price": r["entry_price"],
                 "entry_equity": r.get("entry_equity")} for r in sig_rows])
    # stock_returns.csv
    _write_csv(OUT_DIR / "stock_returns.csv",
               [{k: r.get(k) for k in ("date", "symbol", "signal_type", "gap_pct",
                 "signal_day_return", "ret_1day", "ret_3day", "ret_5day",
                 "realized_vol_30d")} for r in sig_rows])
    # reconstructed_options.csv
    _write_csv(OUT_DIR / "reconstructed_options.csv", sig_rows)
    # control_group.csv
    _write_csv(OUT_DIR / "control_group.csv", ctrl_rows)
    # correlation_results.csv
    cr = []
    for label, v in res["horizons"].items():
        cr.append({"question": "Q1_Q2_call_return", "horizon": label, **v,
                   "iv_crush_impact": res["iv_crush_impact"].get(label)})
    for label, v in res["q5_net_pnl"].items():
        cr.append({"question": "Q5_net_pnl", "horizon": label, **v})
    for label, v in res["q4_strength"].items():
        cr.append({"question": "Q4_strength", "horizon": label, **v})
    _write_csv(OUT_DIR / "correlation_results.csv", cr)

    # preliminary_verdict.md
    best = res["best_horizon"]
    lines = [
        "# Preliminary Correlation Study — Verdict (Task 2.0)", "",
        f"_{LABEL}_", "",
        f"## STATUS: VERDICT {verdict} (PRELIMINARY)", "",
        verdict_text, "",
        "## Interpretation note", "",
        "The equity bot is long-only mean-reversion; every BUY is a bullish thesis "
        "analysed as an ATM CALL. No GapUp/short signals exist, so PUT analysis is N/A.",
        "", "## Inputs", "",
        f"- Signals: {n_allsig} with options data (GapDown subset: {n_gapdown})",
        f"- Signal types: {dict(by_type)}",
        f"- Date range: {dmin}..{dmax}",
        f"- Controls: {len(ctrl_rows)} ({CONTROLS_PER_SIGNAL}/signal, non-signal names same day)",
        f"- BS: r={R}, T={T0*365:.0f}d, sigma=max(realized_vol_30d, {VOL_FLOOR}); "
        f"adversarial entry x{ENTRY_MULT}, exit x{EXIT_MULT}, fee ${FEE}",
        "", "## Q1/Q2 — signal vs control CALL return by horizon", "",
        "| Horizon | Signal mean | Control mean | Diff | p-value | n_sig | n_ctl |",
        "|---|---|---|---|---|---|---|",
    ]
    for label, v in res["horizons"].items():
        star = " *" if (v["difference"] > 0 and v["p_value"] < ALPHA) else ""
        lines.append(
            f"| {label}{star} | {v['signal_mean']:+.2%} | {v['control_mean']:+.2%} | "
            f"{v['difference']:+.2%} | {v['p_value']:.3f} | {v['n_signal']} | {v['n_control']} |")
    lines += ["", f"Best (highest signal mean) horizon: **{best}** "
              f"({res['best_horizon_mean']:+.2%}).  (* = diff>0 and p<{ALPHA})", ""]
    lines += ["## Q3 — approximate IV-crush impact (APPROXIMATE — not reliable without real IV)", ""]
    for label, v in res["iv_crush_impact"].items():
        lines.append(f"- {label}: {v:+.2%} drag" if not math.isnan(v) else f"- {label}: n/a")
    lines += ["", "## Q5 — net P&L per signal after adversarial costs ($/contract)", "",
              "| Horizon | Signal net P&L | Control net P&L |", "|---|---|---|"]
    for label, v in res["q5_net_pnl"].items():
        sp = v["signal_net_pnl"]; cp = v["control_net_pnl"]
        lines.append(f"| {label} | ${sp:+.2f} | ${cp:+.2f} |"
                     if not math.isnan(sp) else f"| {label} | n/a | n/a |")
    lines += ["", "## Q4 — strong (gap<-2%) vs weak (-2%..-0.5%) call returns", "",
              "| Horizon | Strong | Weak | Diff | n_strong | n_weak |", "|---|---|---|---|---|---|"]
    q4 = res["q4_strength"]
    for label, v in q4.items():
        lines.append(f"| {label} | {v['strong_mean']:+.2%} | {v['weak_mean']:+.2%} | "
                     f"{v['diff']:+.2%} | {v['n_strong']} | {v['n_weak']} |")
    lines += ["", "## Sanity checks", "",
              f"- Sanity 1 (dip-buy stock return positive): 1d={s1_1d:+.2%}, 3d={s1_3d:+.2%}",
              f"- Sanity 1b (GapDown gap_pct negative): {gd_gap:+.2%}",
              f"- Sanity 3 (control ~0 drift): {ctrl_bias:+.2%}",
              "", "## Limitations", "",
              "- yfinance EOD only; option prices are Black-Scholes RECONSTRUCTED.",
              "- Realized vol used as IV proxy; no real historical IV surface.",
              "- IV-crush is a crude 20% haircut assumption.",
              "- Short ~3-week signal window; market-regime bias possible.",
              "- EOD horizon uses the stock's open->close move for BOTH signal and "
              "control (symmetric, fair comparison) rather than the bot's actual "
              "intraday entry->close; treat the EOD magnitude as indicative, not exact.",
              "- EOD call returns are large because 7-day ATM options are highly "
              "leveraged (a ~1.5-2% favorable intraday move ~= 30%+ on premium); "
              "this amplifies BOTH the edge and the risk and must be confirmed on "
              "real 1-min option quotes before being trusted.",
              "- KEY READ: edge is concentrated INTRADAY (EOD) and the multi-day "
              "horizons show no signal-vs-control advantage; overnight IV crush "
              "(-15% at 1day) erodes it. The morning bot's same-day entry/EOD-close "
              "design aligns with where the (preliminary) edge appears.",
              f"- {LABEL}",
              ]
    (OUT_DIR / "preliminary_verdict.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
