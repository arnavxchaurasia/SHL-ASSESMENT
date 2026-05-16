def skill_overlap_score(item, tech_skills):
    searchable = item["searchable_text"].lower()

    overlap = 0

    for skill in tech_skills:
        if skill.lower() in searchable:
            overlap += 1

    return overlap


def skill_overlap_score(item, tech_skills):
    searchable = item["searchable_text"].lower()

    overlap = 0

    for skill in tech_skills:
        if skill.lower() in searchable:
            overlap += 1

    return overlap


def passes_skill_filter(item, tech_skills):
    """
    Technical assessments require overlap.
    Personality/cognitive assessments are exempt.
    """

    if not tech_skills:
        return True

    test_types = item["test_types"]

    # Allow personality & ability tests
    if "P" in test_types or "A" in test_types:
        return True

    searchable = item["searchable_text"].lower()

    for skill in tech_skills:
        if skill.lower() in searchable:
            return True

    return False