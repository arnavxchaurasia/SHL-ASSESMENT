from app.agent.frame import ConversationFrame


TECH_KEYWORDS = {
    "java",
    "python",
    "aws",
    "cloud",
    "backend",
    "frontend",
    "react",
    "node",
    "sql",
    "devops",
    "kubernetes",
    "docker",
    "rest",
    "api",
}


SOFT_SKILLS = {
    "communication",
    "stakeholder",
    "leadership",
    "collaboration",
    "teamwork",
    "influence",
    "presentation",
}


class ConversationFrameExtractor:
    def extract(self, messages):
        frame = ConversationFrame()

        combined_text = " ".join(
            [
                msg["content"].lower()
                for msg in messages
            ]
        )

        # =========================
        # TECHNICAL SKILLS
        # =========================
        for skill in TECH_KEYWORDS:
            if skill in combined_text:
                frame.technical_skills.append(
                    skill
                )

        # =========================
        # BEHAVIORAL REQUIREMENTS
        # =========================
        for skill in SOFT_SKILLS:
            if skill in combined_text:
                frame.behavioral_requirements.append(
                    skill
                )

        # =========================
        # SENIORITY
        # =========================
        if "entry" in combined_text:
            frame.seniority = "entry"

        elif "junior" in combined_text:
            frame.seniority = "junior"

        elif "mid" in combined_text:
            frame.seniority = "mid"

        elif "senior" in combined_text:
            frame.seniority = "senior"

        elif "lead" in combined_text:
            frame.seniority = "lead"

        # =========================
        # ROLE FAMILY
        # =========================
        if (
            "developer" in combined_text
            or "engineer" in combined_text
        ):
            frame.role_family = (
                "software_engineering"
            )

        elif "sales" in combined_text:
            frame.role_family = "sales"

        elif "manager" in combined_text:
            frame.role_family = "management"

        # =========================
        # PERSONALITY NEEDS
        # =========================
        if (
            frame.behavioral_requirements
            or "personality" in combined_text
            or "leadership" in combined_text
        ):
            frame.needs_personality = True

        # =========================
        # COGNITIVE NEEDS
        # =========================
        if (
            "problem solving" in combined_text
            or "aptitude" in combined_text
            or "analytical" in combined_text
            or "reasoning" in combined_text
        ):
            frame.needs_cognitive = True

        # =========================
        # HIRING STAGE
        # =========================
        if "screening" in combined_text:
            frame.hiring_stage = "screening"

        elif "finalist" in combined_text:
            frame.hiring_stage = "finalist"

        # =========================
        # CANDIDATE VOLUME
        # =========================
        if (
            "high volume" in combined_text
            or "graduate hiring" in combined_text
            or "campus" in combined_text
        ):
            frame.candidate_volume = "high"

        # =========================
        # TIME BUDGET
        # =========================
        if (
            "short" in combined_text
            or "quick" in combined_text
        ):
            frame.time_budget = "short"

        # =========================
        # DEVELOPMENT VS SELECTION
        # =========================
        if "development" in combined_text:
            frame.selection_vs_development = (
                "development"
            )

        # =========================
        # LANGUAGE CONSTRAINTS
        # =========================
        if "bilingual" in combined_text:
            frame.language_constraints.append(
                "bilingual"
            )

        if "english" in combined_text:
            frame.language_constraints.append(
                "english"
            )

        # =========================
        # LEADERSHIP SCOPE
        # =========================
        if (
            "leadership" in combined_text
            or "executive" in combined_text
            or "manager" in combined_text
        ):
            frame.leadership_scope = True

        return frame