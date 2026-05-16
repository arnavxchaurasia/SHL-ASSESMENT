import pickle
from pathlib import Path

from rank_bm25 import BM25Okapi

from app.catalog.loader import load_catalog


BM25_PATH = Path("data/indexes/bm25.pkl")


def tokenize(text: str):
    return text.lower().split()


def build_bm25():
    catalog = load_catalog()

    corpus = [
        tokenize(item.searchable_text)
        for item in catalog
    ]

    bm25 = BM25Okapi(corpus)

    BM25_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(BM25_PATH, "wb") as f:
        pickle.dump(
            {
                "bm25": bm25,
                "catalog": catalog,
            },
            f,
        )

    print("BM25 index built")


if __name__ == "__main__":
    build_bm25()