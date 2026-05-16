from app.agent.battery_plan import (
    BatteryPlan,
    BatterySlot,
)


class BatteryPlanner:
    def build_plan(
        self,
        frame,
        intent,
        policy,
        refinement=None,
    ):
        plan = BatteryPlan()

        refinement = (
            refinement or {}
        )

        # =========================
        # CORE TECHNICAL
        # =========================
        if (
            intent.needs_technical_validation
            and not refinement.get(
                "remove_technical",
                False,
            )
        ):
            plan.slots.extend(
                [
                    BatterySlot(
                        category="technical",
                        priority="core",
                    ),
                    BatterySlot(
                        category="technical",
                        priority="core",
                    ),
                ]
            )

        # =========================
        # SUPPORTING COGNITIVE
        # =========================
        if (
            intent.needs_cognitive_screening
            or refinement.get(
                "add_cognitive",
                False,
            )
        ):
            plan.slots.append(
                BatterySlot(
                    category="cognitive",
                    priority="supporting",
                )
            )

        # =========================
        # AUGMENT PERSONALITY
        # =========================
        if (
            intent.needs_behavioral_assessment
            or refinement.get(
                "add_personality",
                False,
            )
        ):
            plan.slots.append(
                BatterySlot(
                    category="personality",
                    priority="augment",
                )
            )

        # =========================
        # LEADERSHIP AUGMENTATION
        # =========================
        if refinement.get(
            "focus_leadership",
            False,
        ):
            plan.slots.append(
                BatterySlot(
                    category="personality",
                    priority="augment",
                )
            )

        # =========================
        # SIMULATION
        # =========================
        if (
            intent.needs_sjt
            or policy.prefer_simulation
        ):
            plan.slots.append(
                BatterySlot(
                    category="simulation",
                    priority="supporting",
                )
            )

        # =========================
        # SHORTER BATTERY
        # =========================
        if refinement.get(
            "shorter_battery",
            False,
        ):
            plan.slots = (
                plan.slots[:4]
            )

        return plan