from app.agent.policy import (
    RecommendationPolicy,
)


class PolicyEngine:
    def build_policy(self, frame):
        policy = RecommendationPolicy()

        # =========================
        # PERSONALITY
        # =========================
        if (
            frame.needs_personality
            or frame.leadership_scope
        ):
            policy.prefer_personality = True

        # =========================
        # COGNITIVE
        # =========================
        if (
            frame.candidate_volume == "high"
            or frame.seniority in [
                "mid",
                "senior",
                "lead",
            ]
        ):
            policy.prefer_cognitive = True

        # =========================
        # SIMULATION
        # =========================
        if (
            frame.role_family
            in [
                "sales",
                "management",
            ]
        ):
            policy.prefer_simulation = True

        # =========================
        # SHORTER ASSESSMENTS
        # =========================
        if (
            frame.time_budget == "short"
            or frame.candidate_volume == "high"
        ):
            policy.prefer_short_assessments = (
                True
            )

        # =========================
        # TARGET DIMENSIONS
        # =========================
        if frame.technical_skills:
            policy.target_dimensions.append(
                "technical"
            )

        if (
            frame.behavioral_requirements
            or frame.needs_personality
        ):
            policy.target_dimensions.append(
                "behavioral"
            )

        if policy.prefer_simulation:
            policy.target_dimensions.append(
                "situational"
            )

        return policy