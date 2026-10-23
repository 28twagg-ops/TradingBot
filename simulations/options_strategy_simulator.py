"""Compatibility wrapper — canonical: research/options-strategies/backtests/options_strategy_simulator.py"""
from pathlib import Path
import runpy, sys
_ROOT = Path(__file__).resolve().parents[1]
_TARGET = _ROOT / 'research' / 'options-strategies' / 'backtests' / 'options_strategy_simulator.py'
sys.path.insert(0, str(_TARGET.parent))
sys.argv[0] = str(_TARGET)
runpy.run_path(str(_TARGET), run_name='__main__')
