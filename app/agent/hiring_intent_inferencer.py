from app.agent.hiring_intent import (
    HiringIntent,
)


class HiringIntentInferencer:
    def infer(self, frame):
        intent = HiringIntent()

        # =========================
        # GRADUATE PROGRAM
        # =========================
        if (
            frame.candidate_volume == "high"
            and frame.seniority
            in [
                "entry",
                "junior",
                None,
            ]
        ):
            intent.likely_graduate_program = (
                True
            )

        # =========================
        # SCALABLE SCREENING
        # =========================
        if (
            frame.candidate_volume == "high"
        ):
            intent.needs_scalable_screening = (
                True
            )

        # =========================
        # SJT NEEDS
        # =========================
        if (
            frame.role_family
            in [
                "management",
                "sales",
            ]
            or frame.leadership_scope
        ):
            intent.needs_sjt = True

        # =========================
        # COGNITIVE SCREENING
        # =========================
        if (
            frame.candidate_volume == "high"
            or frame.seniority
            in [
                "mid",
                "senior",
                "lead",
            ]
        ):
            intent.needs_cognitive_screening = (
                True
            )

        # =========================
        # BEHAVIORAL ASSESSMENT
        # =========================
        if (
            frame.needs_personality
            or frame.behavioral_requirements
        ):
            intent.needs_behavioral_assessment = (
                True
            )

        # =========================
        # TECHNICAL VALIDATION
        # =========================
        if frame.technical_skills:
            intent.needs_technical_validation = (
                True
            )

        # =========================
        # LEADERSHIP PIPELINE
        # =========================
        if frame.leadership_scope:
            intent.leadership_pipeline = (
                True
            )

        # =========================
        # FINALIST EVALUATION
        # =========================
        if (
            frame.hiring_stage
            == "finalist"
        ):
            intent.finalist_evaluation = (
                True
            )

        # =========================
        # DEVELOPMENT FOCUS
        # =========================
        if (
            frame.selection_vs_development
            == "development"
        ):
            intent.development_focus = True

        return intent