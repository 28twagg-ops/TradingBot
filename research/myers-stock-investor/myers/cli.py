from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from myers.backtesting.engine import DEFAULT_UNIVERSE, compare_profiles, run_backtest
from myers.config import ROOT, load_config
from myers.strategy.engine import analyze_stock
from myers.strategy.profiles import PROFILES


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="myers",
        description="Myers-inspired stock research (paper/research only)",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_an = sub.add_parser("analyze", help="Analyze one or more tickers")
    p_an.add_argument("tickers", nargs="+")
    p_an.add_argument("--as-of", type=str, default=None, help="YYYY-MM-DD")
    p_an.add_argument("--out", type=Path, default=None)

    p_bt = sub.add_parser("backtest", help="Run quarterly decisions / daily MTM vs SPY")
    p_bt.add_argument("--start", type=str, default="2020-01-01")
    p_bt.add_argument("--end", type=str, default=None)
    p_bt.add_argument("--universe", type=str, default=None, help="Comma-separated tickers")
    p_bt.add_argument("--out", type=Path, default=ROOT / "outputs" / "backtest")
    p_bt.add_argument("--max-names", type=int, default=20)
    p_bt.add_argument(
        "--profile",
        type=str,
        default="conservative_acquirer",
        help="Strategy profile key (see `myers profiles`)",
    )

    p_cmp = sub.add_parser("compare", help="Compare strategy profiles A-F")
    p_cmp.add_argument("--start", type=str, default="2020-01-01")
    p_cmp.add_argument("--end", type=str, default=None)
    p_cmp.add_argument("--universe", type=str, default=None)
    p_cmp.add_argument("--max-names", type=int, default=10)
    p_cmp.add_argument("--out", type=Path, default=ROOT / "outputs" / "compare")
    p_cmp.add_argument(
        "--profiles",
        type=str,
        default="conservative_acquirer,balanced_value,quality_fair_value,deep_value,quality_value_ranking,simple_reference",
    )

    sub.add_parser("profiles", help="List strategy profiles")
    sub.add_parser("version", help="Print version / safety flags")

    args = parser.parse_args(argv)
    cfg = load_config()

    if args.cmd == "version":
        print(
            f"myers {cfg.model_version} live_trading_enabled={cfg.live_trading_enabled} "
            f"research_mode={cfg.backtest.research_mode}"
        )
        return 0

    if args.cmd == "profiles":
        for k, p in PROFILES.items():
            print(f"{k:28s}  {p.name}")
            print(f"  {p.description}")
        return 0

    if args.cmd == "analyze":
        as_of = date.fromisoformat(args.as_of) if args.as_of else date.today()
        reports = [analyze_stock(t, as_of_date=as_of, cfg=cfg) for t in args.tickers]
        payload = [r.model_dump(mode="json") for r in reports]
        text = json.dumps(payload if len(payload) != 1 else payload[0], indent=2)
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(text, encoding="utf-8")
            print(f"Wrote {args.out}")
        else:
            print(text)
        for r in reports:
            print(
                f"{r.ticker}: score={r.fundamental_score:.1f} "
                f"conf={r.data_confidence.value} rec={r.recommendation.value} "
                f"mos={r.valuation.base_margin_of_safety} "
                f"revDCF_g={r.valuation.reverse_dcf_implied_growth}"
            )
        return 0

    if args.cmd == "backtest":
        start = date.fromisoformat(args.start)
        end = date.fromisoformat(args.end) if args.end else date.today()
        if args.universe:
            universe = [x.strip().upper() for x in args.universe.split(",") if x.strip()]
        else:
            universe = DEFAULT_UNIVERSE[: max(5, args.max_names)]
        print(
            f"Backtest {start} -> {end} names={len(universe)} "
            f"profile={args.profile} mode={cfg.backtest.research_mode} "
            f"live_trading={cfg.live_trading_enabled}"
        )
        result = run_backtest(
            start,
            end,
            universe=universe,
            cfg=cfg,
            out_dir=args.out,
            profile=args.profile,
        )
        print(result.limitation)
        print("Strategy:", _brief(result.metrics))
        print("SPY:", _brief(result.benchmark_metrics))
        print("SPY audit cum:", result.spy_audit.get("cumulative_return"))
        print(
            f"Trades={result.n_trades} avg_cash={result.avg_cash_pct:.1%} "
            f"buys_diag={result.diagnostics.get('n_buy_candidate')} -> {args.out}"
        )
        return 0

    if args.cmd == "compare":
        start = date.fromisoformat(args.start)
        end = date.fromisoformat(args.end) if args.end else date.today()
        if args.universe:
            universe = [x.strip().upper() for x in args.universe.split(",") if x.strip()]
        else:
            universe = DEFAULT_UNIVERSE[: max(5, args.max_names)]
        profiles = [p.strip() for p in args.profiles.split(",") if p.strip()]
        print(f"Compare {profiles} on {len(universe)} names {start} -> {end}")
        results = compare_profiles(
            start, end, universe=universe, profiles=profiles, cfg=cfg, out_dir=args.out
        )
        for k, r in results.items():
            print(
                f"{k:28s} cum={r.metrics.get('cumulative_return', float('nan')):+.1%} "
                f"dd={r.metrics.get('max_drawdown', float('nan')):.1%} "
                f"trades={r.n_trades} cash={r.avg_cash_pct:.0%}"
            )
        print(f"Wrote {args.out}")
        return 0

    return 1


def _brief(m: dict) -> dict:
    keys = [
        "start_value",
        "end_value",
        "cumulative_return",
        "cagr",
        "max_drawdown",
        "sharpe",
    ]
    out = {}
    for k in keys:
        v = m.get(k)
        if isinstance(v, float):
            out[k] = round(v, 4)
        else:
            out[k] = v
    return out


if __name__ == "__main__":
    raise SystemExit(main())
