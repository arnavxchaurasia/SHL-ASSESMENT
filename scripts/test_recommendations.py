from app.services.recommendation_service import RecommendationService


messages = [
    {
        "role": "user",
        "content": "Hiring a mid-level Java backend developer with stakeholder communication"
    }
]

service = RecommendationService()

results = service.recommend(messages)

print("\n=== RECOMMENDATIONS ===\n")

for idx, item in enumerate(results, start=1):
    print(f"{idx}. {item['name']}")
    print(f"   Types: {item['test_types']}")
    print()