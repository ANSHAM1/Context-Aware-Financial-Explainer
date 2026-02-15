from fastapi import APIRouter
from backend.models import QueryRequest, ExplanationResponse
from backend.services.intent import classify_intent
from backend.services.generator import generate_explanation
from backend.services.compliance import compliance_check
from backend.utils.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)


@router.post("/explain", response_model=ExplanationResponse)
def explain_query(request: QueryRequest):
    logger.info(f"Received query: {request.query}")

    intent = classify_intent(request.query)
    logger.info(f"Detected intent: {intent}")

    if intent == "advisory":
        logger.warning("Advisory intent detected. Blocking response.")

        return ExplanationResponse(
            explanation="This system does not provide financial advice. I can explain financial concepts instead.",
            assumptions=[],
            risks=[],
            sources=[],
            advisory_blocked=True
        )

    result = generate_explanation(request.query, request.context.dict())

    # Updated tuple unpacking
    is_blocked, checked_text = compliance_check(result["explanation"])

    if is_blocked:
        logger.warning("Compliance filter blocked generated response.")

    return ExplanationResponse(
        explanation=checked_text,
        assumptions=result["assumptions"],
        risks=result["risks"],
        sources=result["sources"],
        advisory_blocked=is_blocked
    )