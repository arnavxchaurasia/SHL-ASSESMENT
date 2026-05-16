class DomainRouter:
    def get_domain_config(
        self,
        frame,
    ):
        technical_skills = [
            skill.lower()
            for skill in (
                frame.technical_skills
            )
        ]

        role_family = (
            (
                frame.role_family
                or ""
            ).lower()
        )

        # =========================
        # FRONTEND
        # =========================
        if (
            "frontend"
            in technical_skills
            or "react"
            in technical_skills
        ):
            return {
                "boost_keywords": [
                    "javascript",
                    "react",
                    "angular",
                    "html",
                    "css",
                    "ui",
                    "web",
                    "frontend",
                    "selenium",
                    "node",
                    "express",
                ],
                "suppress_keywords": [
                    "cobol",
                    "siebel",
                    "sap",
                    "abap",
                    "mainframe",
                    "peoplesoft",
                    "chemical",
                    "polymer",
                    "mechanical",
                    "manufacturing",
                    "civil",
                ],
            }

        # =========================
        # BACKEND
        # =========================
        if (
            "backend"
            in technical_skills
        ):
            return {
                "boost_keywords": [
                    "java",
                    "spring",
                    "api",
                    "microservices",
                    "backend",
                    "j2ee",
                ],
                "suppress_keywords": [
                    "frontend",
                    "ui",
                    "css",
                    "html",
                ],
            }

        # =========================
        # DATA SCIENCE
        # =========================
        if (
            role_family
            == "data_science"
        ):
            return {
                "boost_keywords": [
                    "python",
                    "machine learning",
                    "analytics",
                    "statistics",
                    "sql",
                    "data science",
                ],
                "suppress_keywords": [
                    "sap",
                    "frontend",
                    "mechanical",
                ],
            }

        # =========================
        # ENGINEERING MANAGEMENT
        # =========================
        if (
            role_family
            == "engineering_management"
            or frame.leadership_scope
        ):
            return {
                "boost_keywords": [
                    "leadership",
                    "stakeholder",
                    "strategy",
                    "communication",
                    "management",
                ],
                "suppress_keywords": [],
            }

        # =========================
        # DEFAULT
        # =========================
        return {
            "boost_keywords": [],
            "suppress_keywords": [],
        }