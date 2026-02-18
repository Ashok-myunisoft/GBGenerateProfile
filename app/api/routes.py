from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.prompt_builder import build_prompt
from app.core.openai_client import call_openai
from app.core.validator import validate
from app.utils.logger import audit

router = APIRouter()


class ProfileRequest(BaseModel):

    position: str
    department: str
    level: str
    industry: str = ""
    context: str = ""


@router.post("/generate-profile")
def generate(req: ProfileRequest):

    data = req.dict()

    audit("REQUEST_RECEIVED", data)

    try:
        prompt = build_prompt(data)

        ai_raw = call_openai(prompt)

        result = validate(ai_raw)

        audit("PROFILE_GENERATED", result)

        return result

    except Exception as e:

        audit("ERROR", str(e))

        raise HTTPException(status_code=500, detail=str(e))
