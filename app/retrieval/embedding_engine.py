import json
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from app.catalog.loader import load_catalog


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

FAISS_PATH = Path("data/indexes/faiss.index")
METADATA_PATH = Path("data/indexes/faiss_metadata.json")


def build_faiss_index():
    catalog = load_catalog()

    model = SentenceTransformer(MODEL_NAME)

    texts = [item.searchable_text for item in catalog]

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True,
    )

    embeddings = embeddings.astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    FAISS_PATH.parent.mkdir(parents=True, exist_ok=True)

    faiss.write_index(index, str(FAISS_PATH))

    metadata = [
        item.model_dump()
        for item in catalog
    ]

    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(metadata, f)

    print(f"FAISS index built with {len(metadata)} vectors")


if __name__ == "__main__":
    build_faiss_index()