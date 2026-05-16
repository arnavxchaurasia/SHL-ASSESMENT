from dataclasses import dataclass, field
from typing import List


@dataclass
class BatterySlot:
    category: str

    priority: str


@dataclass
class BatteryPlan:
    slots: List[BatterySlot] = field(
        default_factory=list
    )