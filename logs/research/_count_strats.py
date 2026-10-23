from collections import defaultdict
from scripts.options_signals import PAPER_STRATEGIES, ALL_KNOWN_STRATEGIES
from scripts.options_lab import MIRROR_STRATEGIES, effective_dropped_strategies, BUCKET_EXPERIMENTS

paper_ids = sorted({s.id for s in PAPER_STRATEGIES})
all_ids = sorted({s.id for s in ALL_KNOWN_STRATEGIES})
dropped = effective_dropped_strategies()
active = [i for i in paper_ids if i not in dropped]

print("PAPER_STRATEGIES unique:", len(paper_ids))
print("ALL_KNOWN unique:", len(all_ids))
print("effective dropped:", len(dropped))
print("paper still eligible:", len(active))
print("mirror twin strategies:", sorted(MIRROR_STRATEGIES))
print("buckets total:", len(BUCKET_EXPERIMENTS))

scopes = defaultdict(int)
for b in BUCKET_EXPERIMENTS:
    scopes[b.strategy_scope] += 1
scoped = {k: v for k, v in scopes.items() if k != "all"}
print("unique strategy_scope (!=all):", len(scoped))
print("buckets scope=all:", scopes.get("all", 0))

# try family map
SIGNAL_FAMILY = {}
try:
    from scripts.options_morning_bot import SIGNAL_FAMILY as SF
    SIGNAL_FAMILY = SF
except Exception:
    pass
if not SIGNAL_FAMILY:
    try:
        from scripts.options_signals import SIGNAL_FAMILY as SF2
        SIGNAL_FAMILY = SF2
    except Exception:
        pass

if SIGNAL_FAMILY:
    fams = defaultdict(list)
    for sid in paper_ids:
        fams[SIGNAL_FAMILY.get(sid, sid)].append(sid)
    print("signal families among paper:", len(fams))
    for f, ids in sorted(fams.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {f}: {len(ids)} {ids}")
else:
    print("no SIGNAL_FAMILY map found")
    print("paper ids:", ",".join(paper_ids))
