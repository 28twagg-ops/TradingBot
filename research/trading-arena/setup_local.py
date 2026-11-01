"""One-time local install wizard for the isolated Trading Arena Ollama research service."""
import argparse
import ctypes
import json
import os
from pathlib import Path
import plistlib
import platform
import shutil
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parent
DATA = Path.home() / ".trading-arena"
TASK = "TradingArenaOvernightOllama"


def run(*args, check=True, timeout=150, quiet=False):
    try:
        p = subprocess.run([str(x) for x in args], timeout=timeout,
                           check=False, stdout=subprocess.PIPE if quiet else None,
                           stderr=subprocess.PIPE if quiet else None, text=True)
    except (subprocess.TimeoutExpired, OSError):
        raise RuntimeError("SETUP_COMMAND_UNAVAILABLE_OR_TIMED_OUT") from None
    if check and p.returncode != 0:
        raise RuntimeError("SETUP_COMMAND_FAILED: " + str(args[0]))
    return p.returncode == 0


def memory_gb():
    system = platform.system()
    try:
        if system == "Windows":
            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [("dwLength",ctypes.c_ulong),("dwMemoryLoad",ctypes.c_ulong),
                            ("ullTotalPhys",ctypes.c_ulonglong),
                            ("ullAvailPhys",ctypes.c_ulonglong),
                            ("ullTotalPageFile",ctypes.c_ulonglong),
                            ("ullAvailPageFile",ctypes.c_ulonglong),
                            ("ullTotalVirtual",ctypes.c_ulonglong),
                            ("ullAvailVirtual",ctypes.c_ulonglong),
                            ("ullAvailExtendedVirtual",ctypes.c_ulonglong)]
            stat=MEMORYSTATUSEX()
            stat.dwLength=ctypes.sizeof(stat)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
                return round(stat.ullTotalPhys/(1024**3),1)
        if system == "Darwin":
            raw=subprocess.check_output(["sysctl","-n","hw.memsize"],timeout=5)
            return round(int(raw)/(1024**3),1)
    except (OSError,subprocess.TimeoutExpired,ValueError,AttributeError):
        pass
    return None


def prerequisites():
    missing=[x for x in ("git","gh","ollama") if not shutil.which(x)]
    if missing:
        raise RuntimeError("MISSING_PROGRAMS: "+", ".join(missing)+
                           ". See docs/ARENA_LAPTOP_QUICKSTART.md")
    if sys.version_info < (3,11):
        raise RuntimeError("PYTHON_3_11_OR_NEWER_REQUIRED")


def register_windows(python, model, parallel=1):
    # The task is under the interactive user's account, not an administrator
    # service. Only local repo code runs; Windows sleep settings aren't changed.
    script = ROOT / "overnight_local.py"
    # Daily wall-clock 00:00 scheduled triggers can shift across the fall
    # DST transition on some Windows installations (seen as 11 PM the previous
    # day, with the midnight run missed). Use a repeating 15-minute watchdog;
    # overnight_local.py --scheduled checks America/Chicago independently and
    # immediately exits outside its permitted window without reading accounts,
    # running Ollama or overwriting yesterday's morning report.
    #
    # Keep the unattended service within its active user's session. Don't
    # clobber an existing active job, which might abort an overnight run.
    cmd = ('$old=Get-ScheduledTask -TaskName '+ps_quote(TASK)+
           ' -ErrorAction SilentlyContinue'+
           ';if($old -and $old.State -eq "Running"){ throw "ARENA_TASK_RUNNING_DEFER_SCHEDULE_UPDATE" }'+
           ';$a=New-ScheduledTaskAction -Execute '+ps_quote(str(python))+
           ' -Argument '+ps_quote('"' + str(script) + '" --model ' + model +
                                 ' --parallel ' + str(parallel) + ' --scheduled --log')+
           ';$t=New-ScheduledTaskTrigger -Once -At ((Get-Date).Date.AddDays(1)) '+
           '-RepetitionInterval (New-TimeSpan -Minutes 15) '+
           '-RepetitionDuration (New-TimeSpan -Days 3650)'+
           ';$s=New-ScheduledTaskSettingsSet -WakeToRun -StartWhenAvailable '+
           '-ExecutionTimeLimit (New-TimeSpan -Hours 12) -MultipleInstances IgnoreNew'+
           ';Register-ScheduledTask -TaskName '+ps_quote(TASK)+
           ' -Action $a -Trigger $t -Settings $s '+
           '-Description "Paper-only overnight local trading research, DST-safe checks" -Force | Out-Null')
    run("powershell.exe","-NoProfile","-NonInteractive","-Command",cmd,timeout=60)


def ps_quote(value):
    return "'" + value.replace("'", "''") + "'"


def register_mac(python, model, parallel=1):
    label="com.tradingarena.overnight"
    location=Path.home()/"Library"/"LaunchAgents"/(label+".plist")
    location.parent.mkdir(parents=True,exist_ok=True)
    plist={"Label":label,
           "ProgramArguments":[str(python),str(ROOT/"overnight_local.py"),
                               "--model",model,"--parallel",str(parallel),"--log"],
           "StartCalendarInterval":{"Hour":0,"Minute":0},
           "RunAtLoad":False,"KeepAlive":False,
           "WorkingDirectory":str(ROOT.parent.parent),
           "StandardOutPath":str(DATA/"launchd.log"),
           "StandardErrorPath":str(DATA/"launchd.log")}
    with location.open("wb") as f:
        plistlib.dump(plist,f)
    domain="gui/"+str(os.getuid())
    run("launchctl","bootout",domain+"/"+label,check=False,quiet=True)
    run("launchctl","bootstrap",domain,str(location),timeout=30)


def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("--model",default=None,help="Choose an installed local Ollama model")
    p.add_argument("--skip-task",action="store_true")
    p.add_argument("--parallel",type=int,choices=(1,2),default=None,
                   help="At most two local inference research lanes")
    a=p.parse_args(argv)
    system=platform.system()
    if system not in ("Windows","Darwin"):
        raise RuntimeError("ONE_CLICK_INSTALL_SUPPORTED_ON_WINDOWS_OR_MACOS")
    prerequisites()
    ram=memory_gb()
    if ram is not None and ram<5.5:
        raise RuntimeError("INSUFFICIENT_RAM_FOR_RELIABLE_UNATTENDED_LOCAL_AI")
    # RAM capacity alone does not predict inference throughput. Integrated GPU
    # / ultrabook-class Windows machines often run Ollama on CPU; choose a
    # smaller instruct model + one lane until a real hardware benchmark passes.
    # Explicit --model and --parallel override these conservative defaults.
    model=a.model or ("llama3.2:1b" if ram is not None and ram<9 else
                      "llama3.2:3b" if ram is None or ram<24 else
                      "qwen3:4b-instruct" if system=="Windows" else "qwen3:8b")
    parallel = a.parallel if a.parallel is not None else (
        2 if system=="Darwin" and ram is not None and ram>=24 else 1)
    if ram is not None and ram<16 and parallel>1:
        raise RuntimeError("TWO_PARALLEL_LANES_REQUIRE_AT_LEAST_16GB_RAM")
    from local_ollama import local_model_name
    adaptive = a.model == "auto"
    download_model = ("llama3.2:1b" if ram is not None and ram < 9
                      else "qwen3:4b-instruct") if adaptive else model
    download_model = local_model_name(download_model)
    model = "auto" if adaptive else local_model_name(model)
    if adaptive and a.parallel not in (None, 1):
        raise RuntimeError("ADAPTIVE_REQUIRES_ONE_LANE")
    print("Local-only Ollama model:",model,"; total RAM (GB):",ram or "unknown",
          "; research lanes:",parallel)
    if not run("gh","auth","status",check=False,quiet=True):
        print("Opening GitHub's official browser login (one-time).")
        run("gh","auth","login","--web","--git-protocol","https",timeout=300)
    run("gh","auth","setup-git")
    DATA.mkdir(parents=True,exist_ok=True)
    env=DATA/"venv"
    if not (env/("Scripts/python.exe" if system=="Windows" else "bin/python")).exists():
        print("Setting up isolated Python environment.")
        venv.EnvBuilder(with_pip=True).create(env)
    python=env/("Scripts/python.exe" if system=="Windows" else "bin/python")
    print("Installing isolated market-data libraries; no broker integrations.")
    run(python,"-m","pip","install","--disable-pip-version-check",
        "pandas>=2,<3","numpy>=1.24,<3","yfinance>=0.2,<2","tzdata>=2025.2",
        "psutil>=6,<9",
        timeout=600)
    # Ollama is local; first model download (~2.5GB on Windows 24+ GB
    # defaults) requires internet once. Model overrides can be larger.
    import overnight_local
    overnight_local.ensure_local_ollama()
    print("Downloading or verifying local model (only missing weights download).")
    run("ollama","pull",download_model,timeout=1500)
    if adaptive and ram is not None and ram >= 16 and shutil.disk_usage(DATA).free >= 10 * 1024**3:
        print("Trying optional larger 8B model; compact model remains fallback.")
        if not run("ollama","pull","qwen3:8b",check=False,timeout=1800):
            print("8B download unavailable; continuing with smaller local model.")
    elif adaptive:
        print("Hardware not confirmed for 8B; baseline-only adaptive model routing.")
    print("Checking the model responds locally.")
    overnight_local.smoke(download_model)
    print("Checking independent GitHub research ledger access.")
    overnight_local.init_ledger(DATA)
    overnight_local.refresh_ledger(DATA/"ledger")
    print("Checking separate upload branch access.")
    overnight_local.init_upload(DATA)
    overnight_local.refresh_upload(DATA/"upload")
    # Previous Windows versions could upload records successfully but leave
    # them pending due to CRLF/LF acknowledgement mismatch. Recover without
    # generating new hypotheses, reusing the existing isolated branch.
    pending_dir = DATA/"pending"
    if pending_dir.exists() and any(pending_dir.glob("*.json")):
        if (DATA/"overnight.lock").exists():
            print("Pending upload recovery deferred: overnight task lock exists.")
        else:
            print("Recovering prior unsent paper research records.")
            confirmed = overnight_local.sync_pending(DATA)
            remaining = len(list(pending_dir.glob("*.json")))
            print("Previous records confirmed:",confirmed,"; still pending:",remaining)
    (DATA/"settings.json").write_text(json.dumps(
        {"model":model,"baseline_model":download_model,"adaptive_models":adaptive,
         "parallel_research_lanes":parallel,"start_local":"00:00",
         "stop_local_weekday":"07:00","stop_local_weekend":"10:00",
         "timezone":"America/Chicago","research_only":True},indent=2)+"\n",
        encoding="utf-8")
    if not a.skip_task:
        if system=="Windows":
            register_windows(python,model,parallel)
            # Set the service's future concurrency to match the scheduled
            # worker count; don't terminate any running Ollama instance.
            run("powershell.exe","-NoProfile","-NonInteractive","-Command",
                '[Environment]::SetEnvironmentVariable("OLLAMA_NUM_PARALLEL","'
                +str(parallel)+'","User")', timeout=30)
            print("IMPORTANT: Quit Ollama from the Windows system tray and "
                  "reopen it once for the concurrency setting to take effect.")
        else:
            register_mac(python,model,parallel)
    print("\nSETUP COMPLETE.", "Window checks every 15 min; research only midnight Central." if not a.skip_task
          else "Scheduling skipped.")
    print("Keep laptop powered and awake, and Ollama running.")
    print("Research report:",DATA/"MORNING_REPORT.md")
    print("Unsent work is retained at:",DATA/"pending")
    return 0


if __name__=="__main__":
    try:
        sys.exit(main())
    except (RuntimeError,ValueError,OSError) as e:
        print("\nSetup stopped:",str(e),file=sys.stderr)
        print("Read docs/ARENA_LAPTOP_QUICKSTART.md, then retry.",file=sys.stderr)
        sys.exit(2)
