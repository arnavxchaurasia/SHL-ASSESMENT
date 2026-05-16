import re

from app.catalog.loader import (
    load_catalog,
)


class ComparisonService:
    def __init__(self):
        self.catalog = (
            load_catalog()
        )

    def compare(
        self,
        message,
    ):
        message_lower = (
            message.lower()
        )

        # =========================
        # DIRECT VS PARSING
        # =========================
        patterns = [
            r"compare (.+) vs (.+)",
            r"compare (.+) versus (.+)",
        ]

        extracted_names = []

        for pattern in patterns:
            match = re.search(
                pattern,
                message_lower,
            )

            if match:
                extracted_names = [
                    match.group(1).strip(),
                    match.group(2).strip(),
                ]

                break

        matched = []

        # =========================
        # CATALOG MATCHING
        # =========================
        for item in self.catalog:
            item_name = (
                item.name.lower()
            )

            if extracted_names:
                for extracted in (
                    extracted_names
                ):
                    if (
                        extracted
                        in item_name
                    ):
                        matched.append(
                            item
                        )
            else:
                if (
                    item_name
                    in message_lower
                ):
                    matched.append(
                        item
                    )

        # =========================
        # VALIDATION
        # =========================
        unique_matches = []

        seen = set()

        for item in matched:
            if item.name not in seen:
                unique_matches.append(
                    item
                )

                seen.add(
                    item.name
                )

        if (
            len(unique_matches)
            < 2
        ):
            return (
                "Please specify two SHL "
                "assessments you would "
                "like compared."
            )

        first = (
            unique_matches[0]
        )

        second = (
            unique_matches[1]
        )

        comparison = []

        # =========================
        # TEST TYPE COMPARISON
        # =========================
        comparison.append(
            f"{first.name} focuses on "
            f"{', '.join(first.test_types)} "
            "assessments."
        )

        comparison.append(
            f"{second.name} focuses on "
            f"{', '.join(second.test_types)} "
            "assessments."
        )

        # =========================
        # DURATION
        # =========================
        if (
            first.duration
            and second.duration
        ):
            comparison.append(
                f"{first.name} duration: "
                f"{first.duration}. "
                f"{second.name} duration: "
                f"{second.duration}."
            )

        # =========================
        # URLS
        # =========================
        comparison.append(
            f"{first.name}: "
            f"{first.url}"
        )

        comparison.append(
            f"{second.name}: "
            f"{second.url}"
        )

        return " ".join(
            comparison
        )