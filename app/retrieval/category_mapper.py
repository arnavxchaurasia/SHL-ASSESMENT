def infer_assessment_category(item):
    name = item["name"].lower()

    # =========================
    # PERSONALITY / BEHAVIORAL
    # =========================
    personality_keywords = [
        "opq",
        "personality",
        "leadership",
        "hipo",
        "motivation",
        "mq",
        "competency",
        "behavior",
        "behavioral",
        "potential",
    ]

    if any(
        keyword in name
        for keyword in personality_keywords
    ):
        return "personality"

    # =========================
    # COGNITIVE
    # =========================
    cognitive_keywords = [
        "verify",
        "reasoning",
        "aptitude",
        "numerical",
        "inductive",
        "deductive",
        "cognitive",
    ]

    if any(
        keyword in name
        for keyword in cognitive_keywords
    ):
        return "cognitive"

    # =========================
    # SIMULATION / SJT
    # =========================
    simulation_keywords = [
        "simulation",
        "interactive",
        "situational",
        "scenario",
        "judgment",
    ]

    if any(
        keyword in name
        for keyword in simulation_keywords
    ):
        return "simulation"

    # =========================
    # TECHNICAL DEFAULT
    # =========================
    return "technical"


def infer_semantic_family(item):
    name = item["name"].lower()

    # =========================
    # OPQ FAMILY
    # =========================
    if "opq" in name:
        return "opq"

    # =========================
    # VERIFY FAMILY
    # =========================
    if "verify" in name:
        return "verify"

    # =========================
    # JAVA FAMILY
    # =========================
    if "java" in name:
        return "java"

    # =========================
    # HIPO FAMILY
    # =========================
    if "hipo" in name:
        return "hipo"

    # =========================
    # MQ FAMILY
    # =========================
    if (
        "motivation" in name
        or "mq" in name
    ):
        return "mq"

    # =========================
    # LEADERSHIP FAMILY
    # =========================
    if "leadership" in name:
        return "leadership"

    # =========================
    # DEFAULT
    # =========================
    return name