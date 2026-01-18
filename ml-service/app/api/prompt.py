from fastapi import APIRouter
from app.models.request_response import PromptRequest, PromptResponse
from app.services.prompt_service import PromptService

router = APIRouter(prefix="/prompt", tags=["Prompt"])

prompt_service = PromptService()
@router.post("/score", response_model=PromptResponse)
def score_prompt(request: PromptRequest):
    result = prompt_service.score_prompt(request.prompt)
    return PromptResponse(response=result)

