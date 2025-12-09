from enum import StrEnum
import enum

@enum.unique
class MiassageModes(StrEnum):
    EYES = "eyes"
    EYES_TABLET = "eyes-tablet"
    EYES_TABLET_SUPPLIMENT = "eyes-tablet-suppliments"
    FOOD = "food"