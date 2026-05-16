class RefinementEngine:
    def detect_refinement(
        self,
        latest_message,
    ):
        text = latest_message.lower()

        refinement = {
            "add_personality": False,
            "add_cognitive": False,
            "focus_leadership": False,
            "shorter_battery": False,
            "remove_technical": False,
        }

        if (
            "personality" in text
            or "behavioral" in text
        ):
            refinement[
                "add_personality"
            ] = True

        if (
            "cognitive" in text
            or "reasoning" in text
        ):
            refinement[
                "add_cognitive"
            ] = True

        if (
            "leadership" in text
            or "leader" in text
        ):
            refinement[
                "focus_leadership"
            ] = True

        if (
            "shorter" in text
            or "fewer" in text
            or "quick" in text
        ):
            refinement[
                "shorter_battery"
            ] = True

        if (
            "remove technical" in text
            or "less technical" in text
        ):
            refinement[
                "remove_technical"
            ] = True

        return refinement