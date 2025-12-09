import re


class TimerList:
    timers: list[tuple[str, str]] = []
    def daily(self, time: str, arg: str):
        m = re.match(r"(\d{1,2}):(\d{2})", time)
        if not m:
            raise Exception(f"Expected hh:mm, found '{time}'")
        timer = f"*-*-* {m.group(1)}:{m.group(2)}"
        self.timers.append((timer, arg))