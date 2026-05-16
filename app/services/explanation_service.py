from app.retrieval.category_mapper import (
    infer_assessment_category,
)


class ExplanationService:
    def generate_explanation(
        self,
        item,
        frame,
        intent,
    ):
        category = (
            infer_assessment_category(
                item
            )
        )

        name = item.get(
            "name",
            ""
        )

        explanation_parts = []

        # =====================
        # TECHNICAL
        # =====================
        if category == "technical":
            if (
                frame.role_family
            ):
                explanation_parts.append(
                    "Supports evaluation of "
                    f"{frame.role_family} "
                    "technical capabilities."
                )
            else:
                explanation_parts.append(
                    "Useful for validating "
                    "technical skills relevant "
                    "to the target role."
                )

        # =====================
        # COGNITIVE
        # =====================
        elif category == "cognitive":
            explanation_parts.append(
                "Helps assess reasoning, "
                "problem-solving, and "
                "learning agility."
            )

            if (
                intent.needs_scalable_screening
            ):
                explanation_parts.append(
                    "Well suited for scalable "
                    "high-volume screening."
                )

        # =====================
        # PERSONALITY
        # =====================
        elif category == "personality":
            explanation_parts.append(
                "Provides insight into "
                "behavioral tendencies and "
                "workplace style."
            )

            if (
                frame.leadership_scope
            ):
                explanation_parts.append(
                    "Particularly relevant "
                    "for leadership and "
                    "people-management roles."
                )

        # =====================
        # SIMULATION
        # =====================
        elif category == "simulation":
            explanation_parts.append(
                "Evaluates applied decision-making "
                "in realistic job scenarios."
            )

        # =====================
        # COMMUNICATION
        # =====================
        elif category == "behavioral":
            explanation_parts.append(
                "Useful for assessing "
                "communication and "
                "interpersonal effectiveness."
            )

        # =====================
        # HIGH POTENTIAL
        # =====================
        if (
            "hipo"
            in name.lower()
        ):
            explanation_parts.append(
                "Can support identification "
                "of future leadership potential."
            )

        # =====================
        # LEADERSHIP
        # =====================
        if (
            "leadership"
            in name.lower()
        ):
            explanation_parts.append(
                "Strong fit for leadership "
                "evaluation and succession planning."
            )

        # =====================
        # SHORT BATTERY
        # =====================
        if (
            frame.time_budget
            == "short"
        ):
            explanation_parts.append(
                "Useful in concise assessment "
                "battery configurations."
            )

        # =====================
        # FALLBACK
        # =====================
        if not explanation_parts:
            explanation_parts.append(
                "Relevant for evaluating "
                "candidate fit and hiring readiness."
            )

        return " ".join(
            explanation_parts
        )