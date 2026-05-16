from typing import List, Optional, Dict, Any

from pydantic import BaseModel, Field


class Message(BaseModel):
    role: str = Field(
        ...,
        examples=["user"],
    )

    content: str


class ChatRequest(BaseModel):
    messages: List[Message]

    # =========================
    # OPTIONAL DEBUG MODE
    # =========================
    debug: bool = False


class Recommendation(BaseModel):
    name: str

    url: str

    test_type: str

    # =========================
    # EXPLANATION ENRICHMENT
    # =========================
    explanation: Optional[str] = None


class ChatResponse(BaseModel):
    reply: str

    recommendations: List[
        Recommendation
    ]

    end_of_conversation: bool

    # =========================
    # OPTIONAL DEBUG TRACE
    # =========================
    debug: Optional[
        Dict[str, Any]
    ] = None