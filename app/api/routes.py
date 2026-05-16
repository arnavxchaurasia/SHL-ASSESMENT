from fastapi import (
    APIRouter,
    HTTPException,
)

from app.api.schemas import (
    ChatRequest,
    ChatResponse,
)

from app.services.orchestrator import (
    Orchestrator,
)

router = APIRouter()

orchestrator = Orchestrator()


# =========================
# HEALTH CHECK
# =========================
@router.get("/health")
async def health():
    return {
        "status": "ok"
    }


# =========================
# MAIN CHAT ENDPOINT
# =========================
@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
):
    try:
        # =====================
        # SERIALIZE MESSAGES
        # =====================
        messages = [
            msg.model_dump()
            for msg
            in request.messages
        ]

        # =====================
        # ORCHESTRATION
        # =====================
        result = (
            orchestrator.process(
                messages,
                debug=request.debug,
            )
        )

        # =====================
        # RESPONSE VALIDATION
        # =====================
        return ChatResponse(
            **result
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=(
                "Internal server error: "
                f"{str(exc)}"
            ),
        )