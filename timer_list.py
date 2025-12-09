import re

from modes import MiassageModes


class TimerList:
    timers: list[tuple[str, MiassageModes]] = []

    def daily(self, time: str, arg: MiassageModes, seconds_offset: int = 0):
        m = re.match(r"(\d{1,2}):(\d{2})", time)
        if not m:
            raise Exception(f"Expected hh:mm, found '{time}'")
        s = str(seconds_offset)
        if len(s) == 1:
            s = "0"+s
        timer = f"*-*-* {m.group(1)}:{m.group(2)}:{s}"
        self.timers.append((timer, arg))