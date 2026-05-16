from dataclasses import dataclass, field
from typing import List


@dataclass
class RecommendationPolicy:
    prefer_cognitive: bool = False

    prefer_personality: bool = False

    prefer_simulation: bool = False

    prefer_short_assessments: bool = False

    target_dimensions: List[str] = field(
        default_factory=list
    )