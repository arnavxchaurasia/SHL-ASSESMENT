from dataclasses import dataclass, field
from typing import List


@dataclass
class RecommendationMemory:
    recommendations: List[dict] = field(
        default_factory=list
    )

    active_categories: List[str] = field(
        default_factory=list
    )

    refinement_history: List[str] = field(
        default_factory=list
    )