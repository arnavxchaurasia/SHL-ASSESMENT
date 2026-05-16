import json
from pathlib import Path

from app.catalog.models import CatalogAssessment


CATALOG_PATH = Path("data/processed/catalog.json")


def load_catalog():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [CatalogAssessment(**item) for item in data]