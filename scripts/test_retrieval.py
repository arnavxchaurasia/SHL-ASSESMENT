from app.retrieval.hybrid_ranker import HybridRetriever

retriever = HybridRetriever()

query = "Java backend developer with stakeholder communication"

results = retriever.hybrid_search(query)

print("\n=== HYBRID RESULTS ===\n")

for idx, result in enumerate(results, start=1):
    item = result["item"]

    print(f"{idx}. {item['name']}")
    print(f"   Score: {result['score']:.4f}")
    print(f"   Types: {item['test_types']}")
    print()