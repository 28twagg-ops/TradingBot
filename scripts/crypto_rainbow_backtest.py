#!/usr/bin/env python3
"""Walk-forward Bitcoin-style rainbow curve backtest for BTC-USD and ETH-USD.

Fits log10(price) = a * ln(days_since_start) + b with an expanding window
(no lookahead), assigns nine parallel log10 bands, and compares simple
buy-low / sell-high band rules to buy-and-hold.

Outputs under logs/research/:
  rainbow_btc_eth_summary.md
  rainbow_btc_bands.csv / rainbow_eth_bands.csv
  rainbow_btc_eth_equity.csv
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "logs" / "research"
OUT.mkdir(parents=True, exist_ok=True)

BAND_OFFSETS = np.array([-0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4])
BAND_LABELS = [
    "1 Fire sale",
    "2 Buy!",
    "3 Accumulate",
    "4 Still cheap",
    "5 HODL",
    "6 Is this a bubble?",
    "7 FOMO intensifies",
    "8 Sell. Seriously, sell",
    "9 Maximum bubble",
]
ROUND_TRIP_FEE = 0.001  # 0.1%
WARMUP_DAYS = 730  # ~2 years of price history before first signal
REFIT_EVERY = 1  # daily expanding-window fit (honest; a bit slower)


@dataclass(frozen=True)
class AssetSpec:
    ticker: str
    short: str
    start: date  # day-count origin for ln(days)


ASSETS = [
    AssetSpec("BTC-USD", "btc", date(2009, 1, 3)),
    AssetSpec("ETH-USD", "eth", date(2015, 8, 7)),
]


def _fetch_daily(ticker: str) -> pd.DataFrame:
    t = yf.Ticker(ticker)
    df = t.history(period="max", auto_adjust=True)
    if df is None or df.empty:
        raise RuntimeError(f"No yfinance history for {ticker}")
    df = df.rename(columns={c: c.lower() for c in df.columns})
    if "close" not in df.columns:
        raise RuntimeError(f"Missing close for {ticker}")
    out = df[["close"]].copy()
    out.index = pd.to_datetime(out.index).tz_localize(None).normalize()
    out = out[~out.index.duplicated(keep="last")].sort_index()
    out = out[out["close"] > 0].dropna()
    return out


def _days_since(idx: pd.DatetimeIndex, origin: date) -> np.ndarray:
    origin_ts = pd.Timestamp(origin)
    days = (idx - origin_ts).days.astype(float)
    # Guard against non-positive days (should not happen post-list).
    return np.maximum(days, 1.0)


def _ols_log10(ln_days: np.ndarray, log10_px: np.ndarray) -> tuple[float, float, float]:
    """Return (a, b, r2) for log10(price) = a * ln(days) + b."""
    if len(ln_days) < 30:
        return float("nan"), float("nan"), float("nan")
    x = np.column_stack([ln_days, np.ones(len(ln_days))])
    coef, _, _, _ = np.linalg.lstsq(x, log10_px, rcond=None)
    a, b = float(coef[0]), float(coef[1])
    pred = a * ln_days + b
    ss_res = float(np.sum((log10_px - pred) ** 2))
    ss_tot = float(np.sum((log10_px - log10_px.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return a, b, r2


def _band_from_residual(resid: float) -> int:
    """Map residual (log10 price - center) to band 1..9.

    Thresholds sit midway between offsets (−0.35, −0.25, …, +0.35).
    """
    if math.isnan(resid):
        return 0
    edges = BAND_OFFSETS[:-1] + 0.05  # -0.35 .. +0.35
    band = 1
    for e in edges:
        if resid >= e:
            band += 1
        else:
            break
    return int(min(9, max(1, band)))


def walk_forward_bands(px: pd.DataFrame, origin: date) -> pd.DataFrame:
    """Expanding-window rainbow bands; fit uses history through t-1 only."""
    closes = px["close"].astype(float)
    idx = closes.index
    days = _days_since(idx, origin)
    log10_px = np.log10(closes.values)
    ln_days = np.log(days)

    n = len(closes)
    a_arr = np.full(n, np.nan)
    b_arr = np.full(n, np.nan)
    r2_arr = np.full(n, np.nan)
    center = np.full(n, np.nan)
    resid = np.full(n, np.nan)
    bands = np.zeros(n, dtype=int)

    # Warm-up: need enough history before first classification.
    start_i = min(WARMUP_DAYS, n - 2)
    start_i = max(start_i, 60)

    last_a = last_b = last_r2 = float("nan")
    for i in range(start_i, n):
        # Fit on [0, i) — no lookahead.
        if (i - start_i) % REFIT_EVERY == 0 or math.isnan(last_a):
            last_a, last_b, last_r2 = _ols_log10(ln_days[:i], log10_px[:i])
        a_arr[i] = last_a
        b_arr[i] = last_b
        r2_arr[i] = last_r2
        if math.isnan(last_a):
            continue
        c = last_a * ln_days[i] + last_b
        center[i] = 10 ** c
        resid[i] = log10_px[i] - c
        bands[i] = _band_from_residual(resid[i])

    out = pd.DataFrame(
        {
            "close": closes.values,
            "days": days,
            "a": a_arr,
            "b": b_arr,
            "r2": r2_arr,
            "center": center,
            "residual_log10": resid,
            "band": bands,
            "band_label": [BAND_LABELS[b - 1] if 1 <= b <= 9 else "" for b in bands],
        },
        index=idx,
    )
    return out


@dataclass
class RuleResult:
    name: str
    equity: pd.Series
    trades: int
    terminal: float
    max_dd: float
    cagr: float


def _max_drawdown(eq: pd.Series) -> float:
    peak = eq.cummax()
    dd = eq / peak - 1.0
    return float(dd.min()) if len(dd) else float("nan")


def _cagr(eq: pd.Series) -> float:
    if len(eq) < 2 or eq.iloc[0] <= 0:
        return float("nan")
    years = (eq.index[-1] - eq.index[0]).days / 365.25
    if years <= 0:
        return float("nan")
    return float((eq.iloc[-1] / eq.iloc[0]) ** (1.0 / years) - 1.0)


def simulate_rule(
    bands: pd.DataFrame,
    name: str,
    enter_max: int | None,
    exit_min: int | None,
    *,
    long_when_band_lt: int | None = None,
) -> RuleResult:
    """Long-only full capital. enter_max: go long when band <= enter_max.
    exit_min: go flat when band >= exit_min.
    If long_when_band_lt set (center fade): long iff band < threshold (and band>0).
    """
    sub = bands[bands["band"] > 0].copy()
    if sub.empty:
        eq = pd.Series(dtype=float)
        return RuleResult(name, eq, 0, 1.0, 0.0, float("nan"))

    px = sub["close"].values
    bd = sub["band"].values
    n = len(sub)
    equity = np.ones(n)
    cash = 1.0
    shares = 0.0
    occupied = False
    trades = 0
    half_fee = ROUND_TRIP_FEE / 2.0

    for i in range(n):
        price = float(px[i])
        band = int(bd[i])
        # Mark-to-market first.
        if occupied and shares > 0:
            cash = shares * price
            equity[i] = cash
        else:
            equity[i] = cash

        want_long = False
        want_flat = False
        if long_when_band_lt is not None:
            want_long = band < long_when_band_lt
            want_flat = not want_long
        else:
            assert enter_max is not None and exit_min is not None
            if not occupied and band <= enter_max:
                want_long = True
            elif occupied and band >= exit_min:
                want_flat = True

        if want_long and not occupied:
            # Buy with fee.
            cash_after = cash * (1.0 - half_fee)
            shares = cash_after / price
            cash = shares * price
            occupied = True
            trades += 1
            equity[i] = cash
        elif want_flat and occupied:
            cash = shares * price * (1.0 - half_fee)
            shares = 0.0
            occupied = False
            trades += 1
            equity[i] = cash

    eq = pd.Series(equity, index=sub.index, name=name)
    return RuleResult(
        name=name,
        equity=eq,
        trades=trades,
        terminal=float(eq.iloc[-1]),
        max_dd=_max_drawdown(eq),
        cagr=_cagr(eq),
    )


def buy_and_hold(bands: pd.DataFrame) -> RuleResult:
    sub = bands[bands["band"] > 0].copy()
    if sub.empty:
        return RuleResult("buy_hold", pd.Series(dtype=float), 0, 1.0, 0.0, float("nan"))
    px = sub["close"]
    # Enter on first valid day with fee; hold.
    start = float(px.iloc[0])
    units = (1.0 * (1.0 - ROUND_TRIP_FEE / 2.0)) / start
    eq = units * px
    eq.iloc[0] = 1.0 * (1.0 - ROUND_TRIP_FEE / 2.0)  # after entry fee
    # No exit fee until end — charge exit fee on terminal for fair compare.
    eq = eq.copy()
    eq.iloc[-1] = float(eq.iloc[-1]) * (1.0 - ROUND_TRIP_FEE / 2.0)
    return RuleResult(
        name="buy_hold",
        equity=eq,
        trades=1,
        terminal=float(eq.iloc[-1]),
        max_dd=_max_drawdown(eq),
        cagr=_cagr(eq),
    )


def run_asset(spec: AssetSpec) -> tuple[pd.DataFrame, list[RuleResult], dict]:
    print(f"Fetching {spec.ticker} ...")
    px = _fetch_daily(spec.ticker)
    print(f"  {len(px)} days  {px.index[0].date()} -> {px.index[-1].date()}")
    bands = walk_forward_bands(px, spec.start)
    valid = bands[bands["band"] > 0]
    last = valid.iloc[-1] if len(valid) else None

    rules = [
        buy_and_hold(bands),
        simulate_rule(bands, "deep_value", enter_max=2, exit_min=8),
        simulate_rule(bands, "accumulate_distribute", enter_max=3, exit_min=7),
        simulate_rule(bands, "center_fade", enter_max=None, exit_min=None, long_when_band_lt=6),
    ]

    meta = {
        "ticker": spec.ticker,
        "short": spec.short,
        "n_days": len(px),
        "n_scored": int((bands["band"] > 0).sum()),
        "start": str(px.index[0].date()),
        "end": str(px.index[-1].date()),
        "last_close": float(last["close"]) if last is not None else float("nan"),
        "last_center": float(last["center"]) if last is not None else float("nan"),
        "last_residual": float(last["residual_log10"]) if last is not None else float("nan"),
        "last_band": int(last["band"]) if last is not None else 0,
        "last_label": str(last["band_label"]) if last is not None else "",
        "last_r2": float(last["r2"]) if last is not None else float("nan"),
        "last_a": float(last["a"]) if last is not None else float("nan"),
        "last_b": float(last["b"]) if last is not None else float("nan"),
    }
    return bands, rules, meta


def _fmt_pct(x: float) -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "n/a"
    return f"{x * 100:+.1f}%"


def _fmt_mult(x: float) -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "n/a"
    return f"{x:.2f}x"


def write_report(
    results: list[tuple[AssetSpec, pd.DataFrame, list[RuleResult], dict]],
) -> Path:
    lines: list[str] = []
    lines.append("# Rainbow Curve BTC/ETH Back Analysis")
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("## Method")
    lines.append("")
    lines.append(
        "- Model: `log10(price) = a · ln(days_since_origin) + b` (OLS), "
        "nine parallel bands at log10 offsets −0.4…+0.4."
    )
    lines.append(
        "- Walk-forward: each day fitted on history **through prior close only** "
        f"(warmup ~{WARMUP_DAYS} days)."
    )
    lines.append(
        f"- Costs: {ROUND_TRIP_FEE * 100:.1f}% round-trip fee; full capital long-only."
    )
    lines.append(
        "- Origins: BTC `2009-01-03`, ETH `2015-08-07`. ETH uses the same "
        "methodology on its own history (no canonical ETH rainbow)."
    )
    lines.append("")
    lines.append("### Rules")
    lines.append("")
    lines.append("| Rule | Entry | Exit |")
    lines.append("|---|---|---|")
    lines.append("| buy_hold | first valid day | end |")
    lines.append("| deep_value | band ≤ 2 | band ≥ 8 |")
    lines.append("| accumulate_distribute | band ≤ 3 | band ≥ 7 |")
    lines.append("| center_fade | band < 6 | band ≥ 6 |")
    lines.append("")

    equity_frames: list[pd.DataFrame] = []

    for spec, bands, rules, meta in results:
        band_path = OUT / f"rainbow_{spec.short}_bands.csv"
        bands.to_csv(band_path, float_format="%.6f")
        lines.append(f"## {spec.ticker}")
        lines.append("")
        lines.append(
            f"- History: **{meta['start']} → {meta['end']}** "
            f"({meta['n_days']} days, {meta['n_scored']} scored)"
        )
        lines.append(
            f"- **Now:** ${meta['last_close']:,.2f} | "
            f"center ${meta['last_center']:,.2f} | "
            f"residual {meta['last_residual']:+.3f} log10 | "
            f"**band {meta['last_band']} — {meta['last_label']}**"
        )
        lines.append(
            f"- Latest fit: a={meta['last_a']:.4f}, b={meta['last_b']:.4f}, "
            f"R²={meta['last_r2']:.4f}"
        )
        lines.append("")
        lines.append("| Rule | Terminal | vs BH | CAGR | Max DD | Trades |")
        lines.append("|---|---:|---:|---:|---:|---:|")
        bh = next(r for r in rules if r.name == "buy_hold")
        for r in rules:
            vs = (r.terminal / bh.terminal - 1.0) if bh.terminal else float("nan")
            lines.append(
                f"| {r.name} | {_fmt_mult(r.terminal)} | {_fmt_pct(vs)} | "
                f"{_fmt_pct(r.cagr)} | {_fmt_pct(r.max_dd)} | {r.trades} |"
            )
        lines.append("")
        best = max(rules, key=lambda r: r.terminal)
        beat = best.name != "buy_hold" and best.terminal > bh.terminal
        if beat:
            lines.append(
                f"**Best rule:** `{best.name}` "
                f"({_fmt_mult(best.terminal)} vs BH {_fmt_mult(bh.terminal)})."
            )
        else:
            lines.append(
                f"**Buy-and-hold wins** on terminal wealth "
                f"({_fmt_mult(bh.terminal)}); no band-timing rule beat it."
            )
        lines.append("")

        for r in rules:
            col = f"{spec.short}_{r.name}"
            equity_frames.append(r.equity.rename(col))

    if equity_frames:
        eq = pd.concat(equity_frames, axis=1).sort_index()
        eq_path = OUT / "rainbow_btc_eth_equity.csv"
        eq.to_csv(eq_path, float_format="%.6f")
        lines.append(f"Equity curves: `{eq_path.name}`")
        lines.append("")

    lines.append("## Caveats")
    lines.append("")
    lines.append(
        "- Rainbow is a **descriptive** long-cycle frame, not a proven alpha source; "
        "walk-forward reduces but does not eliminate fit instability early in history."
    )
    lines.append(
        "- Full capital in/out ignores position sizing, taxes, custody, and "
        "multi-year cash drag psychology."
    )
    lines.append(
        "- Past band timing that underperformed buy-hold is still useful as a "
        "risk dashboard (where we sit on the curve today)."
    )
    lines.append("")

    path = OUT / "rainbow_btc_eth_summary.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> None:
    results = []
    for spec in ASSETS:
        bands, rules, meta = run_asset(spec)
        results.append((spec, bands, rules, meta))
        print(
            f"  Now band {meta['last_band']} ({meta['last_label']})  "
            f"close={meta['last_close']:.0f} center={meta['last_center']:.0f}"
        )
        for r in rules:
            print(
                f"    {r.name:22s}  terminal={r.terminal:8.2f}x  "
                f"CAGR={r.cagr * 100:6.1f}%  DD={r.max_dd * 100:6.1f}%  trades={r.trades}"
            )

    summary = write_report(results)
    print(f"\nWrote {summary}")
    for p in sorted(OUT.glob("rainbow_*")):
        print(f"  {p.name}")


if __name__ == "__main__":
    main()
