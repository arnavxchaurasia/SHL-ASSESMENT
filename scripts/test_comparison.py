from app.services.comparison_service import ComparisonService


service = ComparisonService()

query = "Compare OPQ Leadership Report and SHL Verify Interactive – Numerical Reasoning"

result = service.compare(query)

print(result)