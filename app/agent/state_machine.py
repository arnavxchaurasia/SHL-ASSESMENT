COMPARE_KEYWORDS = {
    "compare",
    "difference",
    "vs",
    "versus",
}

REFUSAL_KEYWORDS = {
    "ignore previous instructions",
    "system prompt",
    "bypass",
    "hack",
    "legal advice",
    "salary advice",
}

REFINE_KEYWORDS = {
    "actually",
    "instead",
    "also",
    "add",
    "change",
    "remove",
    "focus",
    "include",
    "shorter",
    "fewer",
    "more leadership",
    "less technical",
}


class ConversationStateMachine:
    def detect_state(
        self,
        messages,
        analysis,
    ):
        latest_message = messages[
            -1
        ]["content"].lower()

        # =========================
        # REFUSAL DETECTION
        # =========================
        for keyword in (
            REFUSAL_KEYWORDS
        ):
            if keyword in latest_message:
                return "REFUSE"

        # =========================
        # COMPARISON DETECTION
        # =========================
        for keyword in (
            COMPARE_KEYWORDS
        ):
            if keyword in latest_message:
                return "COMPARE"

        # =========================
        # REFINEMENT DETECTION
        # =========================
        for keyword in (
            REFINE_KEYWORDS
        ):
            if keyword in latest_message:
                return "REFINE"

        # =========================
        # SOFT CLARIFICATION POLICY
        # =========================
        # Only clarify when:
        # - role/domain unclear
        # - no technical/domain signal
        # =========================
        if not analysis.get(
            "tech_skills"
        ):
            return "CLARIFY"

        # =========================
        # DEFAULT RECOMMENDATION
        # =========================
        return "RECOMMEND"