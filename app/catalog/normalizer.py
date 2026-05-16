import json
import re
from pathlib import Path
from typing import List

from app.catalog.models import CatalogAssessment


TEST_TYPE_MAPPING = {
    "Ability & Aptitude": "A",
    "Personality & Behavior": "P",
    "Knowledge & Skills": "K",
    "Biodata & Situational Judgment": "B",
    "Simulations": "S",
    "Competencies": "C",
    "Development & 360": "D",
    "Assessment Exercises": "E",
}


RAW_PATH = Path("data/raw/shl_product_catalog.json")
OUTPUT_PATH = Path("data/processed/catalog.json")


def clean_text(text: str) -> str:
    text = text or ""
    text = re.sub(r"[\r\n\t]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_test_types(keys: List[str]) -> List[str]:
    normalized = []

    for key in keys:
        if key in TEST_TYPE_MAPPING:
            normalized.append(TEST_TYPE_MAPPING[key])

    return normalized


def build_searchable_text(item: dict) -> str:
    parts = [
        item.get("name", ""),
        item.get("description", ""),
        " ".join(item.get("job_levels", [])),
        " ".join(item.get("keys", [])),
    ]

    return clean_text(" ".join(parts))


def load_malformed_json(path: Path):
    """
    Handles malformed control characters in the SHL dataset.
    """

    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    # Remove invalid control characters
    raw = re.sub(r"[\x00-\x1F\x7F]", " ", raw)

    return json.loads(raw)


def normalize_catalog():
    raw_catalog = load_malformed_json(RAW_PATH)

    normalized_catalog = []

    for item in raw_catalog:
        assessment = CatalogAssessment(
            id=str(item.get("entity_id")),
            name=clean_text(item.get("name", "")),
            url=item.get("link", ""),
            description=clean_text(item.get("description", "")),
            test_types=normalize_test_types(item.get("keys", [])),
            job_levels=item.get("job_levels", []),
            languages=item.get("languages", []),
            duration=item.get("duration", ""),
            adaptive=item.get("adaptive", "no") == "yes",
            remote=item.get("remote", "no") == "yes",
            searchable_text=build_searchable_text(item),
        )

        normalized_catalog.append(assessment.model_dump())

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(normalized_catalog, f, indent=2)

    print(f"Normalized {len(normalized_catalog)} assessments")


if __name__ == "__main__":
    normalize_catalog()