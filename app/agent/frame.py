from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ConversationFrame:
    role_family: Optional[str] = None

    seniority: Optional[str] = None

    technical_skills: List[str] = field(
        default_factory=list
    )

    behavioral_requirements: List[str] = field(
        default_factory=list
    )

    needs_personality: bool = False

    needs_cognitive: bool = False

    hiring_stage: Optional[str] = None

    candidate_volume: Optional[str] = None

    time_budget: Optional[str] = None

    selection_vs_development: str = (
        "selection"
    )

    language_constraints: List[str] = field(
        default_factory=list
    )

    leadership_scope: bool = False