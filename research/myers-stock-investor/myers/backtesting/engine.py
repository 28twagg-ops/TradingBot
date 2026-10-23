from __future__ import annotations

import json
from copy import deepcopy
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

import pandas as pd

from myers.backtesting.performance import (
    summarize_equity,
    spy_total_return_audit,
)
from myers.config import StrategyConfig, load_config
from myers.data.market import fetch_price_history, latest_price_as_of, quarter_ends
from myers.portfolio.paper import PaperPortfolio, Position
from myers.schemas import Recommendation
from myers.strategy.diagnostics import RejectionRecord, classify_rejections, summarize_diagnostics
from myers.strategy.engine import analyze_stock
from myers.strategy.profiles import StrategyProfile, config_for_profile, resolve_profile

DEFAULT_UNIVERSE = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "BRK-B", "JNJ", "UNH", "XOM",
    "V", "PG", "MA", "HD", "CVX", "MRK", "ABBV", "PEP", "KO",
    "COST", "AVGO", "WMT", "MCD", "CSCO", "ACN", "TMO", "CRM", "LIN", "DHR",
    "ABT", "TXN", "NEE", "PM", "IBM", "AMGN", "CAT", "HON", "QCOM", "LOW",
    "UNP", "SBUX", "RTX", "BA", "GE", "INTU", "AMAT", "BKNG", "ADI", "GILD",
    "DE", "ADP", "SYK", "MMC", "VRTX", "ISRG", "MDT", "CVS", "LMT", "MMM",
]


@dataclass
class HoldingSnapshot:
    date: date
    cash: float
    positions: dict[str, Position]


@dataclass
class BacktestResult:
    equity: pd.Series
    cash_series: pd.Series
    invested_series: pd.Series
    benchmark: pd.Series
    trades: list[dict]
    decisions: list[dict]
    rejections: list[dict]
    diagnostics: dict[str, Any]
    metrics: dict
    benchmark_metrics: dict
    spy_audit: dict
    config_version: str
    profile: str
    research_mode: str
    limitation: str
    avg_cash_pct: float
    avg_invested_pct: float
    n_trades: int


def run_backtest(
    start: date,
    end: date,
    universe: list[str] | None = None,
    cfg: StrategyConfig | None = None,
    out_dir: Path | None = None,
    profile: str | StrategyProfile | None = None,
) -> BacktestResult:
    """Quarterly decisions, daily mark-to-market equity vs SPY.

    RESEARCH MODE
    - exploratory (default): yfinance fundamentals may look ahead — labeled.
    - validated: refuses unless a PIT provider is configured (not available free).
    """
    base_cfg = cfg or load_config()
    assert base_cfg.live_trading_enabled is False

    prof = resolve_profile(profile.key if isinstance(profile, StrategyProfile) else profile)
    cfg = config_for_profile(base_cfg, prof)

    mode = cfg.backtest.research_mode
    if mode == "validated":
        raise RuntimeError(
            "Point-in-Time Validated Mode requires a licensed PIT fundamentals "
            "provider. Configure one under myers/data/providers/ or run with "
            "research_mode=exploratory."
        )

    universe = [u.upper() for u in (universe or DEFAULT_UNIVERSE)]
    port = PaperPortfolio.create(cfg)
    decisions: list[dict] = []
    rejection_rows: list[RejectionRecord] = []
    snapshots: list[HoldingSnapshot] = []

    spy_px = fetch_price_history(cfg.backtest.benchmark)
    if spy_px.empty or "close" not in spy_px.columns:
        raise RuntimeError("No benchmark price history")
    spy_close = spy_px["close"].astype(float)

    calendar = spy_close.loc[
        (spy_close.index >= pd.Timestamp(start)) & (spy_close.index <= pd.Timestamp(end))
    ].index
    if len(calendar) < 2:
        raise RuntimeError("Insufficient trading calendar for window")

    # Seed snapshot at first trading day (100% cash) BEFORE any decision
    snapshots.append(
        HoldingSnapshot(date=calendar[0].date(), cash=port.cash, positions={})
    )

    dates = quarter_ends(start, end)
    # Ensure final mark decision on/before end
    if not dates or dates[-1] < end:
        # use last trading day on/before end as final review
        pass

    price_cache: dict[str, pd.Series] = {}

    def _series(ticker: str) -> pd.Series:
        if ticker not in price_cache:
            df = fetch_price_history(ticker)
            price_cache[ticker] = df["close"].astype(float) if not df.empty and "close" in df.columns else pd.Series(dtype=float)
        return price_cache[ticker]

    for d in dates:
        prices: dict[str, float] = {}
        scored: list = []
        analyses = []

        for t in universe:
            px = latest_price_as_of(t, d)
            if px is None:
                continue
            prices[t] = px
            try:
                analysis = analyze_stock(t, as_of_date=d, cfg=cfg)
            except Exception as exc:
                decisions.append({"date": d.isoformat(), "ticker": t, "error": str(exc)})
                continue
            analyses.append(analysis)
            decisions.append(
                {
                    "date": d.isoformat(),
                    "ticker": t,
                    "score": analysis.fundamental_score,
                    "recommendation": analysis.recommendation.value,
                    "confidence": analysis.data_confidence.value,
                    "mos": analysis.valuation.base_margin_of_safety,
                    "fair_value_base": analysis.valuation.fair_value_base,
                    "price": analysis.current_price,
                    "sector": analysis.sector,
                    "profile": prof.key,
                }
            )

        # Reference mode: ignore MOS/score — buy equal-weight top N by market presence
        if prof.reference_mode:
            scored = [a for a in analyses if a.recommendation != Recommendation.EXCLUDED]
            scored = scored[: cfg.portfolio.max_positions]
        elif prof.ranking_mode:
            eligible = [
                a
                for a in analyses
                if a.recommendation != Recommendation.EXCLUDED
                and a.fundamental_score >= cfg.signals.buy_min_score
                and a.valuation.base_margin_of_safety is not None
                and a.valuation.base_margin_of_safety >= cfg.valuation.margin_of_safety_buy
            ]
            eligible.sort(
                key=lambda a: (
                    a.fundamental_score
                    + 100.0 * (a.valuation.base_margin_of_safety or 0.0)
                ),
                reverse=True,
            )
            scored = eligible
        else:
            for a in analyses:
                if a.recommendation == Recommendation.BUY_CANDIDATE:
                    scored.append(a)
                else:
                    rejection_rows.append(classify_rejections(a, cfg))

        # Sell deteriorated holdings
        for t in list(port.positions.keys()):
            px = prices.get(t) or latest_price_as_of(t, d)
            if px is None:
                continue
            try:
                a = analyze_stock(t, as_of_date=d, cfg=cfg)
            except Exception:
                continue
            if a.recommendation in (Recommendation.SELL_CANDIDATE, Recommendation.EXCLUDED):
                port.sell_all(t, px, d, cfg)

        scored.sort(key=lambda a: a.fundamental_score, reverse=True)
        target_w = cfg.portfolio.max_position_weight
        max_pos = min(10, cfg.portfolio.max_positions) if prof.reference_mode else None
        for a in scored:
            if a.ticker in port.positions:
                continue
            block = port.can_buy(
                a,
                cfg,
                prices,
                require_buy_candidate=not prof.reference_mode,
                max_positions_override=max_pos,
            )
            if block:
                if a.recommendation != Recommendation.BUY_CANDIDATE or block != "not_buy_candidate":
                    rejection_rows.append(classify_rejections(a, cfg, portfolio_block=block))
                continue
            px = prices.get(a.ticker)
            if px is None:
                continue
            port.buy(a.ticker, px, target_w, d, a.sector, cfg)

        snapshots.append(
            HoldingSnapshot(
                date=d,
                cash=port.cash,
                positions=deepcopy(port.positions),
            )
        )

    # Final snapshot at last calendar day with current port state
    snapshots.append(
        HoldingSnapshot(
            date=calendar[-1].date(),
            cash=port.cash,
            positions=deepcopy(port.positions),
        )
    )

    equity, cash_s, inv_s = _build_daily_curves(
        snapshots=snapshots,
        calendar=calendar,
        price_getter=_series,
        cash_annual_rate=cfg.backtest.cash_annual_rate,
        initial_cash=cfg.backtest.initial_cash,
    )

    # Benchmark aligned to SAME calendar as strategy equity
    spy_aligned = spy_close.reindex(equity.index).ffill()
    bench = spy_aligned / float(spy_aligned.iloc[0]) * cfg.backtest.initial_cash

    spy_audit = spy_total_return_audit(
        spy_close,
        start=pd.Timestamp(start),
        end=pd.Timestamp(end),
        initial_cash=cfg.backtest.initial_cash,
    )

    metrics = summarize_equity(equity, rf_annual=cfg.backtest.cash_annual_rate)
    bench_metrics = summarize_equity(bench, rf_annual=0.0)

    diag = summarize_diagnostics(rejection_rows)
    # Prefer decision-log buy count (rejection list omits successful buys)
    diag["n_buy_candidate"] = sum(
        1 for d in decisions if d.get("recommendation") == "BUY_CANDIDATE"
    )
    diag["n_evaluated"] = max(diag.get("n_evaluated", 0), len(decisions))
    diag["buy_rate"] = (
        diag["n_buy_candidate"] / diag["n_evaluated"] if diag["n_evaluated"] else 0.0
    )
    avg_cash = float((cash_s / equity).mean()) if len(equity) else 1.0
    avg_inv = float((inv_s / equity).mean()) if len(equity) else 0.0

    limitation = (
        "EXPLORATORY MODE: prices are point-in-time; yfinance fundamentals are NOT "
        "filing-date accurate and may look ahead. Universe is a modern survivor list "
        "(survivorship bias). Results are experimental, not validated historical performance. "
        "Live trading disabled."
    )

    result = BacktestResult(
        equity=equity,
        cash_series=cash_s,
        invested_series=inv_s,
        benchmark=bench,
        trades=port.trades,
        decisions=decisions,
        rejections=[r.__dict__ for r in rejection_rows],
        diagnostics=diag,
        metrics=metrics,
        benchmark_metrics=bench_metrics,
        spy_audit=spy_audit,
        config_version=cfg.model_version,
        profile=prof.key,
        research_mode=mode,
        limitation=limitation,
        avg_cash_pct=avg_cash,
        avg_invested_pct=avg_inv,
        n_trades=len(port.trades),
    )

    if out_dir is not None:
        _write_outputs(out_dir, result, cfg, prof)

    return result


def _build_daily_curves(
    *,
    snapshots: list[HoldingSnapshot],
    calendar: pd.DatetimeIndex,
    price_getter,
    cash_annual_rate: float,
    initial_cash: float,
) -> tuple[pd.Series, pd.Series, pd.Series]:
    """Mark holdings to market daily; accrue cash at cash_annual_rate/365."""
    snaps = sorted(snapshots, key=lambda s: s.date)
    # map each calendar day to latest snapshot on/before that day
    equity_vals = []
    cash_vals = []
    inv_vals = []
    idx = []

    snap_i = 0
    cash = initial_cash
    positions: dict[str, Position] = {}

    for ts in calendar:
        d = ts.date()
        while snap_i < len(snaps) and snaps[snap_i].date <= d:
            cash = snaps[snap_i].cash
            positions = snaps[snap_i].positions
            snap_i += 1

        # accrue cash for this day (simple)
        if cash_annual_rate:
            cash *= 1.0 + cash_annual_rate / 365.25

        invested = 0.0
        for t, pos in positions.items():
            series = price_getter(t)
            if series.empty:
                invested += pos.shares * pos.avg_cost
                continue
            sub = series.loc[series.index <= ts]
            px = float(sub.iloc[-1]) if len(sub) else pos.avg_cost
            invested += pos.shares * px

        total = cash + invested
        idx.append(ts)
        equity_vals.append(total)
        cash_vals.append(cash)
        inv_vals.append(invested)

    return (
        pd.Series(equity_vals, index=pd.DatetimeIndex(idx), name="equity"),
        pd.Series(cash_vals, index=pd.DatetimeIndex(idx), name="cash"),
        pd.Series(inv_vals, index=pd.DatetimeIndex(idx), name="invested"),
    )


def _write_outputs(
    out_dir: Path,
    result: BacktestResult,
    cfg: StrategyConfig,
    prof: StrategyProfile,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    result.equity.to_csv(out_dir / "equity_curve.csv", header=["equity"])
    result.cash_series.to_csv(out_dir / "cash_curve.csv", header=["cash"])
    result.invested_series.to_csv(out_dir / "invested_curve.csv", header=["invested"])
    result.benchmark.to_csv(out_dir / "benchmark_curve.csv", header=["benchmark"])
    pd.DataFrame(result.trades).to_csv(out_dir / "trades.csv", index=False)
    pd.DataFrame(result.decisions).to_csv(out_dir / "decisions.csv", index=False)
    pd.DataFrame(result.rejections).to_csv(out_dir / "rejections.csv", index=False)

    lines = [
        f"# Myers Backtest — {prof.name}",
        "",
        f"Model: `{result.config_version}` · Profile: `{result.profile}` · Mode: **{result.research_mode.upper()}**",
        "",
        "## Limitation",
        "",
        result.limitation,
        "",
        "## Performance (daily mark-to-market)",
        "",
        "| Metric | Strategy | SPY buy-hold (same calendar) |",
        "|---|---:|---:|",
    ]
    keys = [
        "start_value",
        "end_value",
        "cumulative_return",
        "cagr",
        "max_drawdown",
        "volatility",
        "sharpe",
        "sortino",
        "best_calendar_year",
        "worst_calendar_year",
    ]
    for k in keys:
        lines.append(
            f"| {k} | {_fmt(k, result.metrics.get(k))} | {_fmt(k, result.benchmark_metrics.get(k))} |"
        )
    lines += [
        "",
        f"Trades: **{result.n_trades}** (simulated)",
        f"Avg cash allocation: **{result.avg_cash_pct:.1%}**",
        f"Avg invested: **{result.avg_invested_pct:.1%}**",
        f"Decision rows: **{len(result.decisions)}**",
        "",
        "## Independent SPY audit (window start→end)",
        "",
        "```json",
        json.dumps(result.spy_audit, indent=2, default=str),
        "```",
        "",
        "## Screening diagnostics",
        "",
        "```json",
        json.dumps(result.diagnostics, indent=2, default=str)[:8000],
        "```",
        "",
        "Live trading: **DISABLED**",
        "",
    ]
    (out_dir / "summary.md").write_text("\n".join(lines), encoding="utf-8")
    (out_dir / "metrics.json").write_text(
        json.dumps(
            {
                "profile": result.profile,
                "research_mode": result.research_mode,
                "strategy": result.metrics,
                "benchmark": result.benchmark_metrics,
                "spy_audit": result.spy_audit,
                "diagnostics": result.diagnostics,
                "avg_cash_pct": result.avg_cash_pct,
                "avg_invested_pct": result.avg_invested_pct,
                "n_trades": result.n_trades,
                "limitation": result.limitation,
            },
            indent=2,
            default=str,
        ),
        encoding="utf-8",
    )


def _fmt(key: str, v: float | None) -> str:
    if v is None or (isinstance(v, float) and v != v):
        return "n/a"
    if key in (
        "cumulative_return",
        "cagr",
        "max_drawdown",
        "volatility",
        "best_calendar_year",
        "worst_calendar_year",
    ):
        return f"{v * 100:.1f}%"
    if key in ("sharpe", "sortino"):
        return f"{v:.2f}"
    if key in ("terminal", "start_value", "end_value"):
        return f"${v:,.0f}"
    return f"{v:.4f}"


def compare_profiles(
    start: date,
    end: date,
    universe: list[str],
    profiles: list[str] | None = None,
    cfg: StrategyConfig | None = None,
    out_dir: Path | None = None,
) -> dict[str, BacktestResult]:
    """Run multiple profiles under identical conditions."""
    keys = profiles or [
        "conservative_acquirer",
        "balanced_value",
        "quality_fair_value",
        "deep_value",
        "quality_value_ranking",
        "simple_reference",
    ]
    results: dict[str, BacktestResult] = {}
    base = out_dir or Path("outputs/compare")
    for key in keys:
        sub = base / key
        print(f"Running profile {key} ...")
        results[key] = run_backtest(
            start, end, universe=universe, cfg=cfg, out_dir=sub, profile=key
        )
    # comparison table
    rows = []
    for key, r in results.items():
        rows.append(
            {
                "profile": key,
                "cum": r.metrics.get("cumulative_return"),
                "cagr": r.metrics.get("cagr"),
                "max_dd": r.metrics.get("max_drawdown"),
                "sharpe": r.metrics.get("sharpe"),
                "trades": r.n_trades,
                "avg_cash": r.avg_cash_pct,
            }
        )
    if out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(rows).to_csv(out_dir / "comparison.csv", index=False)
        spy = next(iter(results.values())).benchmark_metrics
        lines = [
            "# Strategy Comparison (identical window/universe/costs)",
            "",
            f"Mode: exploratory · SPY cum={spy.get('cumulative_return')}",
            "",
            "| Profile | Cum | CAGR | MaxDD | Sharpe | Trades | Avg Cash |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
        for row in rows:
            lines.append(
                f"| {row['profile']} | {_fmt('cumulative_return', row['cum'])} | "
                f"{_fmt('cagr', row['cagr'])} | {_fmt('max_drawdown', row['max_dd'])} | "
                f"{_fmt('sharpe', row['sharpe'])} | {row['trades']} | {row['avg_cash']:.1%} |"
            )
        lines.append("")
        lines.append(
            "All runs share survivorship / non-PIT fundamental limitations. "
            "Do not treat the best historical row as an optimized production rule."
        )
        (out_dir / "comparison.md").write_text("\n".join(lines), encoding="utf-8")
    return results
