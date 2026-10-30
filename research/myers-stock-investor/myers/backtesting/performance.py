from __future__ import annotations

import math

import pandas as pd


def max_drawdown(equity: pd.Series) -> float:
    if equity.empty:
        return float("nan")
    peak = equity.cummax()
    dd = equity / peak - 1.0
    return float(dd.min())


def cagr(equity: pd.Series) -> float:
    if len(equity) < 2 or float(equity.iloc[0]) <= 0:
        return float("nan")
    years = (equity.index[-1] - equity.index[0]).days / 365.25
    if years <= 0:
        return float("nan")
    return float((float(equity.iloc[-1]) / float(equity.iloc[0])) ** (1 / years) - 1)


def volatility(returns: pd.Series, periods_per_year: float = 252.0) -> float:
    if len(returns) < 2:
        return float("nan")
    return float(returns.std(ddof=1) * math.sqrt(periods_per_year))


def sharpe(returns: pd.Series, rf_annual: float = 0.0, periods_per_year: float = 252.0) -> float:
    vol = volatility(returns, periods_per_year)
    if vol is None or vol == 0 or math.isnan(vol):
        return float("nan")
    rf_period = rf_annual / periods_per_year
    ann = float((returns.mean() - rf_period) * periods_per_year)
    return ann / vol


def sortino(returns: pd.Series, rf_annual: float = 0.0, periods_per_year: float = 252.0) -> float:
    downside = returns[returns < 0]
    if len(downside) < 2:
        return float("nan")
    dd = float(downside.std(ddof=1) * math.sqrt(periods_per_year))
    if dd == 0:
        return float("nan")
    rf_period = rf_annual / periods_per_year
    ann = float((returns.mean() - rf_period) * periods_per_year)
    return ann / dd


def calendar_year_returns(equity: pd.Series) -> dict[int, float]:
    if equity.empty:
        return {}
    out: dict[int, float] = {}
    by_year = equity.groupby(equity.index.year)
    for year, series in by_year:
        if len(series) < 2:
            continue
        out[int(year)] = float(series.iloc[-1] / series.iloc[0] - 1.0)
    return out


def summarize_equity(equity: pd.Series, rf_annual: float = 0.0) -> dict[str, float]:
    if equity.empty:
        return {
            "terminal": float("nan"),
            "cumulative_return": float("nan"),
            "cagr": float("nan"),
            "max_drawdown": float("nan"),
            "volatility": float("nan"),
            "sharpe": float("nan"),
            "sortino": float("nan"),
            "best_calendar_year": float("nan"),
            "worst_calendar_year": float("nan"),
            "start_value": float("nan"),
            "end_value": float("nan"),
            "n_obs": 0.0,
        }
    rets = equity.pct_change().dropna()
    yrs = calendar_year_returns(equity)
    best = max(yrs.values()) if yrs else float("nan")
    worst = min(yrs.values()) if yrs else float("nan")
    start_v = float(equity.iloc[0])
    end_v = float(equity.iloc[-1])
    return {
        "terminal": end_v,
        "start_value": start_v,
        "end_value": end_v,
        "cumulative_return": end_v / start_v - 1.0 if start_v > 0 else float("nan"),
        "cagr": cagr(equity),
        "max_drawdown": max_drawdown(equity),
        "volatility": volatility(rets),
        "sharpe": sharpe(rets, rf_annual=rf_annual),
        "sortino": sortino(rets, rf_annual=rf_annual),
        "best_calendar_year": best,
        "worst_calendar_year": worst,
        "n_obs": float(len(equity)),
    }


def spy_total_return_audit(
    spy_close: pd.Series,
    start: pd.Timestamp,
    end: pd.Timestamp,
    initial_cash: float,
) -> dict[str, float | str]:
    """Independent SPY buy-and-hold on adjusted closes over [start, end]."""
    sub = spy_close.loc[(spy_close.index >= start) & (spy_close.index <= end)].dropna()
    if len(sub) < 2:
        return {"error": "insufficient SPY history"}
    eq = sub / float(sub.iloc[0]) * initial_cash
    m = summarize_equity(eq)
    m["first_date"] = str(sub.index[0].date())
    m["last_date"] = str(sub.index[-1].date())
    m["first_price"] = float(sub.iloc[0])
    m["last_price"] = float(sub.iloc[-1])
    m["price_return"] = float(sub.iloc[-1] / sub.iloc[0] - 1.0)
    return m
