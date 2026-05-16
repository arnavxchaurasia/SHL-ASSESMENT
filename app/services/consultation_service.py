class ConsultationService:
    def generate_follow_up(
        self,
        frame,
        intent,
    ):
        suggestions = []

        # =========================
        # SENIORITY
        # =========================
        if not frame.seniority:
            suggestions.append(
                "seniority level"
            )

        # =========================
        # HIRING SCALE
        # =========================
        if not frame.candidate_volume:
            suggestions.append(
                "hiring volume"
            )

        # =========================
        # LEADERSHIP
        # =========================
        if not frame.leadership_scope:
            suggestions.append(
                "leadership requirements"
            )

        # =========================
        # BATTERY DURATION
        # =========================
        suggestions.append(
            "assessment duration preferences"
        )

        # =========================
        # FINAL RESPONSE
        # =========================
        if not suggestions:
            return ""

        formatted = ", ".join(
            suggestions[:4]
        )

        return (
            "If you'd like, I can "
            "further tailor the "
            "recommendations based on "
            f"{formatted}."
        )