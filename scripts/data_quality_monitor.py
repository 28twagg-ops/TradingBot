"""
data_quality_monitor.py — Task 1.5: Daily data quality monitor.

Runs at 4:30 PM ET (triggered by options_collector.yml after market close).
Reads today's parquet files and produces:
  data/quality/YYYY-MM-DD_quality.md   — quality report (always written)
  data/quality/QUALITY_WARNINGS.md     — appended if completeness < 85%

Checks:
  1. Minutes collected vs expected (~390 for a full day, 65 for first-hour)
  2. % of universe with options data
  3. Average ATM bid-ask spread
  4. Zero-options symbols (candidates for universe removal)
  5. File size alert (>50 MB)
  6. First-hour completeness (65 1-min bars expected per symbol)
  7. Options file exists at all
"""

from __future__ import annotations

import logging
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_universe import get_universe

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ET = ZoneInfo("America/New_York")
_REPO_ROOT = Path(__file__).resolve().parent.parent
FIRST_HOUR_DIR = _REPO_ROOT / "data" / "first_hour"
STOCKS_DIR = _REPO_ROOT / "data" / "stocks_1min"
OPTIONS_DIR = _REPO_ROOT / "data" / "options_1min"
QUALITY_DIR = _REPO_ROOT / "data" / "quality"
QUALITY_DIR.mkdir(parents=True, exist_ok=True)

TODAY_STR = date.today().strftime("%Y-%m-%d")

EXPECTED_FULL_MINUTES = 390   # ~6.5 trading hours × 60 min
EXPECTED_FIRST_HOUR_BARS = 65 # 9:30–10:35 ET
COMPLETENESS_WARN_THRESHOLD = 0.85
FILE_SIZE_ALERT_MB = 50.0


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _file_size_mb(path: Path) -> float:
    return path.stat().st_size / 1e6 if path.exists() else 0.0


def _load_parquet_safe(path: Path) -> pd.DataFrame | None:
    if not path.exists():
        return None
    try:
        return pd.read_parquet(path)
    except Exception as exc:
        log.error("Could not read %s: %s", path, exc)
        return None


# ---------------------------------------------------------------------------
# Quality checks
# ---------------------------------------------------------------------------

def check_stocks_1min(today: str) -> dict:
    path = STOCKS_DIR / f"{today}.parquet"
    df = _load_parquet_safe(path)
    result: dict = {"file": str(path), "exists": df is not None}
    if df is None:
        result["error"] = "file missing"
        return result

    result["file_size_mb"] = _file_size_mb(path)
    result["size_alert"] = result["file_size_mb"] > FILE_SIZE_ALERT_MB
    result["total_rows"] = len(df)

    if "symbol" in df.columns and "timestamp" in df.columns:
        symbol_counts = df.groupby("symbol")["timestamp"].count()
        result["symbols_with_data"] = int(symbol_counts.gt(0).sum())
        result["avg_minutes_per_symbol"] = float(symbol_counts.mean())
        result["min_minutes_per_symbol"] = int(symbol_counts.min())
        result["max_minutes_per_symbol"] = int(symbol_counts.max())
        result["completeness_pct"] = float(
            (symbol_counts >= EXPECTED_FULL_MINUTES * 0.85).mean() * 100
        )
    return result


def check_first_hour(today: str) -> dict:
    path = FIRST_HOUR_DIR / f"{today}.parquet"
    summary_path = FIRST_HOUR_DIR / f"{today}_summary.parquet"
    df = _load_parquet_safe(path)
    result: dict = {"file": str(path), "exists": df is not None}
    if df is None:
        result["error"] = "file missing"
        return result

    result["file_size_mb"] = _file_size_mb(path)
    result["size_alert"] = result["file_size_mb"] > FILE_SIZE_ALERT_MB
    result["total_rows"] = len(df)
    result["summary_exists"] = summary_path.exists()

    if "symbol" in df.columns and "timestamp" in df.columns:
        symbol_counts = df.groupby("symbol")["timestamp"].count()
        result["symbols_with_data"] = int(symbol_counts.gt(0).sum())
        result["avg_bars_per_symbol"] = float(symbol_counts.mean())
        result["full_symbols"] = int(symbol_counts.ge(EXPECTED_FIRST_HOUR_BARS).sum())
        total_syms = len(symbol_counts)
        result["first_hour_completeness_pct"] = float(
            result["full_symbols"] / total_syms * 100 if total_syms else 0
        )

    return result


def check_options(today: str, universe: list[str]) -> dict:
    path = OPTIONS_DIR / f"{today}.parquet"
    df = _load_parquet_safe(path)
    result: dict = {"file": str(path), "exists": df is not None}
    if df is None:
        result["error"] = "file missing"
        return result

    result["file_size_mb"] = _file_size_mb(path)
    result["size_alert"] = result["file_size_mb"] > FILE_SIZE_ALERT_MB
    result["total_rows"] = len(df)

    if df.empty:
        result["warning"] = "empty dataframe"
        return result

    underlying_col = "underlying" if "underlying" in df.columns else None
    if underlying_col:
        underlyings_with_data = set(df[underlying_col].unique())
        result["underlyings_with_options_data"] = len(underlyings_with_data)
        result["universe_size"] = len(universe)
        result["pct_universe_with_options"] = float(
            len(underlyings_with_data) / len(universe) * 100 if universe else 0
        )
        zero_opts = [s for s in universe if s not in underlyings_with_data]
        result["zero_options_symbols_count"] = len(zero_opts)
        result["zero_options_symbols_sample"] = zero_opts[:20]

    # ATM spread analysis
    if "spread_pct" in df.columns and "delta" in df.columns:
        atm_mask = df["delta"].notna() & (df["delta"].abs().between(0.40, 0.60))
        atm = df[atm_mask]
        if not atm.empty:
            result["avg_atm_spread_pct"] = float(atm["spread_pct"].mean())
            result["median_atm_spread_pct"] = float(atm["spread_pct"].median())
            result["atm_sample_size"] = len(atm)
    elif "spread_pct" in df.columns:
        result["avg_spread_pct_all"] = float(df["spread_pct"].mean())

    # Skip log
    skip_path = OPTIONS_DIR / f"{today}_skips.csv"
    if skip_path.exists():
        try:
            skip_df = pd.read_csv(skip_path)
            result["total_skips"] = len(skip_df)
            result["skip_reasons"] = skip_df["reason"].value_counts().head(10).to_dict()
        except Exception:
            result["skip_log_read_error"] = True

    return result


# ---------------------------------------------------------------------------
# Report writer
# ---------------------------------------------------------------------------

def _fmt(val: object, precision: int = 1) -> str:
    if val is None:
        return "N/A"
    if isinstance(val, float):
        return f"{val:.{precision}f}"
    return str(val)


def write_quality_report(
    today: str,
    stocks_chk: dict,
    fh_chk: dict,
    opts_chk: dict,
    universe_size: int,
) -> float:
    """Write quality report. Returns overall completeness (0–1)."""

    lines = [
        f"# Data Quality Report — {today}",
        f"Generated: {datetime.now(ET).strftime('%Y-%m-%d %H:%M ET')}",
        "",
        "## 1. Full-Day Stock 1-min Data",
    ]

    if stocks_chk.get("error"):
        lines.append(f"**STATUS: MISSING** — {stocks_chk['error']}")
        stocks_ok = False
    else:
        lines += [
            f"- File: `{Path(stocks_chk['file']).name}`",
            f"- File size: {_fmt(stocks_chk.get('file_size_mb'))} MB"
            + (" ⚠️ EXCEEDS 50MB" if stocks_chk.get("size_alert") else ""),
            f"- Total rows: {stocks_chk.get('total_rows', 'N/A')}",
            f"- Symbols with data: {stocks_chk.get('symbols_with_data', 'N/A')}",
            f"- Avg minutes/symbol: {_fmt(stocks_chk.get('avg_minutes_per_symbol'))} "
            f"(expected ~{EXPECTED_FULL_MINUTES})",
            f"- Completeness (≥85% full): {_fmt(stocks_chk.get('completeness_pct'))}%",
        ]
        stocks_ok = stocks_chk.get("completeness_pct", 0) >= COMPLETENESS_WARN_THRESHOLD * 100

    lines += ["", "## 2. First-Hour Stock Data"]
    if fh_chk.get("error"):
        lines.append(f"**STATUS: MISSING** — {fh_chk['error']}")
        fh_ok = False
        fh_completeness = 0.0
    else:
        fh_completeness = fh_chk.get("first_hour_completeness_pct", 0)
        lines += [
            f"- File: `{Path(fh_chk['file']).name}`",
            f"- File size: {_fmt(fh_chk.get('file_size_mb'))} MB"
            + (" ⚠️ EXCEEDS 50MB" if fh_chk.get("size_alert") else ""),
            f"- Total rows: {fh_chk.get('total_rows', 'N/A')}",
            f"- Symbols with data: {fh_chk.get('symbols_with_data', 'N/A')}",
            f"- Avg bars/symbol: {_fmt(fh_chk.get('avg_bars_per_symbol'))} "
            f"(expected {EXPECTED_FIRST_HOUR_BARS})",
            f"- Symbols with all 65 bars: {fh_chk.get('full_symbols', 'N/A')}",
            f"- First-hour completeness: {_fmt(fh_completeness)}%",
            f"- Summary file exists: {fh_chk.get('summary_exists', False)}",
        ]
        fh_ok = fh_completeness >= COMPLETENESS_WARN_THRESHOLD * 100

    lines += ["", "## 3. Options 1-min Data"]
    if opts_chk.get("error"):
        lines.append(f"**STATUS: MISSING** — {opts_chk['error']}")
        opts_ok = False
        opts_completeness = 0.0
    else:
        pct_univ = opts_chk.get("pct_universe_with_options", 0)
        opts_completeness = pct_univ
        lines += [
            f"- File: `{Path(opts_chk['file']).name}`",
            f"- File size: {_fmt(opts_chk.get('file_size_mb'))} MB"
            + (" ⚠️ EXCEEDS 50MB" if opts_chk.get("size_alert") else ""),
            f"- Total rows: {opts_chk.get('total_rows', 'N/A')}",
            f"- Underlyings with options data: {opts_chk.get('underlyings_with_options_data', 'N/A')} "
            f"/ {universe_size} ({_fmt(pct_univ)}%)",
            f"- Zero-options symbols: {opts_chk.get('zero_options_symbols_count', 'N/A')}",
            f"- Avg ATM spread %: {_fmt(opts_chk.get('avg_atm_spread_pct'), 2)}",
            f"- Median ATM spread %: {_fmt(opts_chk.get('median_atm_spread_pct'), 2)}",
            f"- ATM sample size: {opts_chk.get('atm_sample_size', 'N/A')}",
            f"- Total skips: {opts_chk.get('total_skips', 'N/A')}",
        ]
        if opts_chk.get("zero_options_symbols_sample"):
            lines.append(
                "- Zero-options sample: "
                + ", ".join(opts_chk["zero_options_symbols_sample"])
            )
        if opts_chk.get("skip_reasons"):
            lines.append("- Skip reasons:")
            for reason, count in opts_chk["skip_reasons"].items():
                lines.append(f"  - {reason}: {count}")
        opts_ok = pct_univ >= COMPLETENESS_WARN_THRESHOLD * 100

    overall_completeness = (
        (stocks_chk.get("completeness_pct", 0) / 100 +
         fh_completeness / 100 +
         opts_completeness / 100) / 3
    )

    lines += [
        "",
        "## 4. Summary",
        f"| Check | Status |",
        f"|-------|--------|",
        f"| Full-day stocks completeness | {'✅ PASS' if stocks_ok else '❌ FAIL'} |",
        f"| First-hour completeness | {'✅ PASS' if fh_ok else '❌ FAIL'} |",
        f"| Options universe coverage | {'✅ PASS' if opts_ok else '❌ FAIL'} |",
        f"| **Overall** | **{overall_completeness*100:.1f}%** |",
        "",
        f"Phase 1 exit gate target: >85% completeness on all 5 days.",
    ]

    report_path = QUALITY_DIR / f"{today}_quality.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    log.info("Quality report written: %s", report_path)

    return overall_completeness


def maybe_write_warning(today: str, overall_completeness: float) -> None:
    """Append to QUALITY_WARNINGS.md if completeness drops below 85%."""
    if overall_completeness >= COMPLETENESS_WARN_THRESHOLD:
        return

    warn_path = QUALITY_DIR / "QUALITY_WARNINGS.md"
    ts = datetime.now(ET).strftime("%Y-%m-%d %H:%M ET")
    warning_line = (
        f"\n## WARNING — {today}\n"
        f"Recorded: {ts}\n"
        f"Overall completeness: {overall_completeness*100:.1f}% "
        f"(threshold: {COMPLETENESS_WARN_THRESHOLD*100:.0f}%)\n"
        f"Action required: review collector logs for {today} and investigate gaps.\n"
    )
    with warn_path.open("a", encoding="utf-8") as f:
        f.write(warning_line)
    log.warning("LOW COMPLETENESS: %.1f%% — warning appended to %s", overall_completeness * 100, warn_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(today: str = TODAY_STR) -> None:
    now = datetime.now(ET)
    log.info("Data quality monitor starting for %s (now %s ET)", today, now.strftime("%H:%M"))

    universe = get_universe()
    log.info("Universe size: %d", len(universe))

    stocks_chk = check_stocks_1min(today)
    fh_chk = check_first_hour(today)
    opts_chk = check_options(today, universe)

    overall = write_quality_report(today, stocks_chk, fh_chk, opts_chk, len(universe))
    maybe_write_warning(today, overall)

    log.info(
        "Quality check complete. Overall: %.1f%% (%s)",
        overall * 100,
        "PASS" if overall >= COMPLETENESS_WARN_THRESHOLD else "FAIL",
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Data quality monitor")
    parser.add_argument("--date", default=TODAY_STR,
                        help="Date to check (YYYY-MM-DD, default=today)")
    args = parser.parse_args()
    main(today=args.date)
