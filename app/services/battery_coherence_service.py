from app.retrieval.category_mapper import (
    infer_assessment_category,
    infer_semantic_family,
)


class BatteryCoherenceService:
    def validate(
        self,
        recommendations,
        max_per_family=1,
        max_personality=2,
    ):
        validated = []

        family_counts = {}

        personality_count = 0

        seen_names = set()

        for item in recommendations:
            item_name = item.get(
                "name",
                ""
            )

            if item_name in seen_names:
                continue

            category = (
                infer_assessment_category(
                    item
                )
            )

            family = (
                infer_semantic_family(
                    item
                )
            )

            # =====================
            # FAMILY REDUNDANCY
            # =====================
            if (
                family_counts.get(
                    family,
                    0,
                )
                >= max_per_family
            ):
                continue

            # =====================
            # PERSONALITY LIMIT
            # =====================
            if (
                category
                == "personality"
            ):
                if (
                    personality_count
                    >= max_personality
                ):
                    continue

                personality_count += 1

            validated.append(item)

            seen_names.add(
                item_name
            )

            family_counts[
                family
            ] = (
                family_counts.get(
                    family,
                    0,
                )
                + 1
            )

        return validated