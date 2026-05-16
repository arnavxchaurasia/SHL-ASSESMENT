import json
import pickle
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


BM25_PATH = Path("data/indexes/bm25.pkl")
FAISS_PATH = Path("data/indexes/faiss.index")
METADATA_PATH = Path("data/indexes/faiss_metadata.json")

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


class HybridRetriever:
    def __init__(self):
        with open(BM25_PATH, "rb") as f:
            bm25_data = pickle.load(f)

        self.bm25 = bm25_data["bm25"]
        self.catalog = bm25_data["catalog"]

        self.index = faiss.read_index(str(FAISS_PATH))

        with open(METADATA_PATH, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        self.model = SentenceTransformer(MODEL_NAME)

    def bm25_search(self, query, top_k=20):
        tokens = query.lower().split()

        scores = self.bm25.get_scores(tokens)

        ranked_indices = np.argsort(scores)[::-1][:top_k]

        results = []

        for idx in ranked_indices:
            results.append(
                {
                    "id": self.catalog[idx].id,
                    "name": self.catalog[idx].name,
                    "score": float(scores[idx]),
                    "item": self.catalog[idx].model_dump(),
                }
            )

        return results

    def semantic_search(self, query, top_k=20):
        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True,
        ).astype("float32")

        distances, indices = self.index.search(
            query_embedding,
            top_k,
        )

        results = []

        for distance, idx in zip(distances[0], indices[0]):
            similarity = 1 / (1 + float(distance))

            results.append(
                {
                    "id": self.metadata[idx]["id"],
                    "name": self.metadata[idx]["name"],
                    "score": similarity,
                    "item": self.metadata[idx],
                }
            )

        return results

    def hybrid_search(self, query, top_k=10):
        bm25_results = self.bm25_search(query)
        semantic_results = self.semantic_search(query)

        combined_scores = {}

        # BM25 weight
        for rank, result in enumerate(bm25_results):
            item_id = result["id"]

            weighted_score = result["score"] * 0.65

            if item_id not in combined_scores:
                combined_scores[item_id] = {
                    "score": 0,
                    "item": result["item"],
                }

            combined_scores[item_id]["score"] += weighted_score

        # Semantic weight
        for rank, result in enumerate(semantic_results):
            item_id = result["id"]

            weighted_score = result["score"] * 0.35

            if item_id not in combined_scores:
                combined_scores[item_id] = {
                    "score": 0,
                    "item": result["item"],
                }

            combined_scores[item_id]["score"] += weighted_score

        final_results = sorted(
            combined_scores.values(),
            key=lambda x: x["score"],
            reverse=True,
        )

        return final_results[:top_k]