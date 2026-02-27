from pydantic import BaseModel
from typing import Optional, List


class FinancialContext(BaseModel):
    income: Optional[float] = None
    savings: Optional[float] = None
    loans: Optional[float] = None
    goals: Optional[str] = None


class QueryRequest(BaseModel):
    user_id: str
    query: str
    context: FinancialContext


class ExplanationResponse(BaseModel):
    explanation: str
    assumptions: List[str]
    risks: List[str]
    sources: List[str]
    advisory_blocked: bool