from modes import MiassageModes
from timer_list import TimerList


def define_timers(timers: TimerList):
    timers.daily("11:00", MiassageModes.TABLET_SUPPLIMENT)
    timers.daily("11:00", MiassageModes.FOOD, seconds_offset=1)
    timers.daily("18:00", MiassageModes.TABLET)
    timers.daily("18:00", MiassageModes.FOOD, seconds_offset=1)