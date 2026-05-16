from typing import List

from pydantic import BaseModel


class CatalogAssessment(BaseModel):
    id: str
    name: str
    url: str
    description: str
    test_types: List[str]
    job_levels: List[str]
    languages: List[str]
    duration: str
    adaptive: bool
    remote: bool
    searchable_text: str