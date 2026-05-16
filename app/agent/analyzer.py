from app.agent.frame_extractor import (
    ConversationFrameExtractor,
)


class ConversationAnalyzer:
    def __init__(self):
        self.frame_extractor = (
            ConversationFrameExtractor()
        )

    def analyze(
        self,
        messages,
    ):
        frame = (
            self.frame_extractor.extract(
                messages
            )
        )

        # =========================
        # ROLE NORMALIZATION
        # =========================
        role_family = (
            frame.role_family
        )

        technical_skills = list(
            frame.technical_skills
        )

        behavioral_requirements = list(
            frame.behavioral_requirements
        )

        latest_text = (
            messages[-1][
                "content"
            ]
            .lower()
        )

        # =========================
        # ENGINEERING MANAGER
        # =========================
        if (
            "engineering manager"
            in latest_text
        ):
            role_family = (
                "engineering_management"
            )

            frame.leadership_scope = (
                True
            )

            if (
                "leadership"
                not in behavioral_requirements
            ):
                behavioral_requirements.append(
                    "leadership"
                )

        # =========================
        # DATA SCIENCE
        # =========================
        if (
            "machine learning"
            in latest_text
            or "ml engineer"
            in latest_text
            or "data scientist"
            in latest_text
            or "data science"
            in latest_text
        ):
            role_family = (
                "data_science"
            )

            for skill in [
                "machine learning",
                "python",
            ]:
                if (
                    skill
                    not in technical_skills
                ):
                    technical_skills.append(
                        skill
                    )

        # =========================
        # FRONTEND
        # =========================
        if (
            "frontend"
            in latest_text
            or "react"
            in latest_text
        ):
            role_family = (
                "software_engineering"
            )

            for skill in [
                "frontend",
                "react",
                "javascript",
            ]:
                if (
                    skill
                    not in technical_skills
                ):
                    technical_skills.append(
                        skill
                    )

        # =========================
        # BACKEND
        # =========================
        if (
            "backend"
            in latest_text
        ):
            role_family = (
                "software_engineering"
            )

            if (
                "backend"
                not in technical_skills
            ):
                technical_skills.append(
                    "backend"
                )

        # =========================
        # SCALABLE HIRING
        # =========================
        if (
            "high-volume"
            in latest_text
            or "scalable"
            in latest_text
            or "graduate"
            in latest_text
        ):
            frame.candidate_volume = (
                "high"
            )

        # =========================
        # RETURN ANALYSIS
        # =========================
        return {
            # =====================
            # STRUCTURED FRAME
            # =====================
            "frame": frame,

            # =====================
            # BACKWARD COMPATIBILITY
            # =====================
            "tech_skills": (
                technical_skills
            ),

            "soft_skills": (
                behavioral_requirements
            ),

            "seniority": (
                frame.seniority
            ),

            "needs_personality": (
                frame.needs_personality
            ),

            "needs_cognitive": (
                frame.needs_cognitive
            ),

            # =====================
            # CONTEXT SIGNALS
            # =====================
            "role_family": (
                role_family
            ),

            "hiring_stage": (
                frame.hiring_stage
            ),

            "candidate_volume": (
                frame.candidate_volume
            ),

            "time_budget": (
                frame.time_budget
            ),

            "selection_vs_development": (
                frame.selection_vs_development
            ),

            "language_constraints": (
                frame.language_constraints
            ),

            "leadership_scope": (
                frame.leadership_scope
            ),
        }