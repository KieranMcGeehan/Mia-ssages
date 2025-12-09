#!/bin/env python3

from pathlib import Path
import sys

from modes import MiassageModes
from timer_list import TimerList
from timers import define_timers

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [exec]")
        sys.exit(1)
    
    exec_path = sys.argv[1]
    list = TimerList()
    define_timers(list)

    used_modes = set([mode for (_,mode) in list.timers])

    output_dir = Path("./systemd_out")
    output_dir.mkdir(exist_ok=True)

    filename_prefix = "miassages"

    for mode in used_modes:
        write(
            output_dir / f"{filename_prefix}-{mode}.service",
            gen_service(exec_path, mode)
        )
    i = 0
    for (calender, mode) in list.timers:
        write(
            output_dir / f"{filename_prefix}-{i}.timer",
            gen_timer(calender, f"{filename_prefix}-{mode}.service")
        )
        i += 1


def write(p: Path, content: str):
    with open(p, "w") as f:
        _ = f.write(content)

def gen_service(exec: str, arg: MiassageModes) -> str:
    return f"""
[Unit]
Description=Send Mia-ssage ({arg})

[Service]
Type=oneshot
ExecStart={exec} {arg.value}
PrivateTmp=true
    """.strip()

def gen_timer(timer: str, unit: str) -> str:
    return f"""
[Unit]
Description=Timer for Mia-ssages

[Timer]
Unit={unit}
OnCalender={timer}
AccuracySec=30s
Persistent=true

[Install]
WantedBy=timers.target
    """.strip()

if __name__ == "__main__":
    main()