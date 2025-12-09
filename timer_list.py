import re

from modes import MiassageModes


class TimerList:
    timers: list[tuple[str, MiassageModes]] = []

    def daily(self, time: str, arg: MiassageModes):
        m = re.match(r"(\d{1,2}):(\d{2})", time)
        if not m:
            raise Exception(f"Expected hh:mm, found '{time}'")
        timer = f"*-*-* {m.group(1)}:{m.group(2)}"
        self.timers.append((timer, arg))