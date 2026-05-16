class SkillCanonicalizer:
    def __init__(self):
        self.skill_map = {
            # =====================
            # JAVA
            # =====================
            "java developer": "java",
            "core java": "java",
            "java backend": "java",

            # =====================
            # FRONTEND
            # =====================
            "reactjs": "react",
            "react.js": "react",
            "frontend": "frontend",
            "front-end": "frontend",

            # =====================
            # BACKEND
            # =====================
            "backend": "backend",
            "back-end": "backend",

            # =====================
            # MACHINE LEARNING
            # =====================
            "ml": "machine learning",
            "ai": "machine learning",

            # =====================
            # DEVOPS
            # =====================
            "k8s": "kubernetes",

            # =====================
            # COMMUNICATION
            # =====================
            "stakeholder management":
                "stakeholder communication",

            "communication skills":
                "communication",
        }

    def canonicalize(
        self,
        skills,
    ):
        canonicalized = []

        for skill in skills:
            normalized = (
                skill
                .strip()
                .lower()
            )

            canonicalized.append(
                self.skill_map.get(
                    normalized,
                    normalized,
                )
            )

        return list(
            set(canonicalized)
        )