from dataclasses import dataclass


@dataclass
class HiringIntent:
    likely_graduate_program: bool = False

    needs_scalable_screening: bool = False

    needs_sjt: bool = False

    needs_cognitive_screening: bool = False

    needs_behavioral_assessment: bool = False

    needs_technical_validation: bool = False

    leadership_pipeline: bool = False

    finalist_evaluation: bool = False

    development_focus: bool = False