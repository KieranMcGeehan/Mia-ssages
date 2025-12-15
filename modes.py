from enum import StrEnum
import enum

@enum.unique
class MiassageModes(StrEnum):
    TABLET = "tablet"
    TABLET_SUPPLIMENT = "tablet-suppliments"
    FOOD = "food"