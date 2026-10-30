#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NEW = "research/options-strategies/backtests"
FILES = [
    "research/other-studies/run_historical_parallel.py",
    "research/other-studies/run_enrich_parallel.py",
    "research/other-studies/run_rank_top5_parallel.py",
    "research/other-studies/run_options_research.py",
    "research/other-studies/historical_data_fetcher.py",
    "live-bots/options-paper/reporting/generate_review_doc.py",
]

for rel in FILES:
    p = ROOT / rel
    t = p.read_text(encoding="utf-8")
    n = t
    n = n.replace('REPO / "simulations"', f'REPO / "{NEW}"')
    n = n.replace("REPO / 'simulations'", f"REPO / '{NEW}'")
    n = n.replace('REPO_ROOT / "simulations"', f'REPO_ROOT / "{NEW}"')
    n = n.replace('"simulations/results', f'"{NEW}/results')
    n = n.replace('"simulations/options_', f'"{NEW}/options_')
    n = n.replace('"simulations/', f'"{NEW}/')
    n = n.replace("simulations/options_strategy_simulator.py", f"{NEW}/options_strategy_simulator.py")
    n = n.replace("simulations/results/", f"{NEW}/results/")
    if n != t:
        p.write_text(n, encoding="utf-8", newline="\n")
        print("updated", rel)
    else:
        print("no-op", rel)
