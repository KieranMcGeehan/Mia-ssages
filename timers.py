from modes import MiassageModes
from timer_list import TimerList


def define_timers(timers: TimerList):
    timers.daily("08:00", MiassageModes.EYES_TABLET_SUPPLIMENT)
    timers.daily("08:00", MiassageModes.FOOD, seconds_offset=1)
    timers.daily("13:00", MiassageModes.EYES)
    timers.daily("18:00", MiassageModes.EYES_TABLET)
    timers.daily("18:00", MiassageModes.FOOD, seconds_offset=1)
    timers.daily("23:00", MiassageModes.EYES)