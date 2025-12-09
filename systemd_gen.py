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
    tlist = TimerList()
    define_timers(tlist)

    used_modes = set([mode for (_,mode) in tlist.timers])

    output_dir = Path("./systemd_out")
    output_dir.mkdir(exist_ok=True)

    filename_prefix = "miassages"

    for mode in used_modes:
        write(
            output_dir / f"{filename_prefix}-{mode}.service",
            gen_service(exec_path, mode)
        )
    timer_files: list[str] = []
    i = 0
    for (calender, mode) in tlist.timers:
        n = f"{filename_prefix}-{i}.timer"
        timer_files.append(n)
        write(
            output_dir / n,
            gen_timer(calender, f"{filename_prefix}-{mode}.service", filename_prefix)
        )
        i += 1
    write(
        output_dir / f"{filename_prefix}.service",
        gen_main(timer_files)
    )


def write(p: Path, content: str):
    with open(p, "w") as f:
        _ = f.write(content)

def gen_main(timers: list[str]) -> str:
    f = f"""
[Unit]
Description=App Service
""".strip()
    for t in timers:
        f += f"\nWants={t}"
    f += """
[Install]
WantedBy=default.target

[Service]
Type=oneshot
ExecStart=/bin/true
RemainAfterExit=yes
    """
    return f

def gen_service(exec: str, arg: MiassageModes) -> str:
    return f"""
[Unit]
Description=Send Mia-ssage ({arg})

[Service]
Type=oneshot
ExecStart={exec} {arg.value}
PrivateTmp=true
    """.strip()

def gen_timer(timer: str, unit: str, prefix: str) -> str:
    return f"""
[Unit]
Description=Timer for Mia-ssages
PartOf={prefix}

[Timer]
Unit={unit}
OnCalendar={timer}
AccuracySec=30s
Persistent=true

[Install]
WantedBy=timers.target
    """.strip()

if __name__ == "__main__":
    main()