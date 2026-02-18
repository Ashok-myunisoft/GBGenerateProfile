import runpod
from app.core.prompt_builder import build_prompt
from app.core.openai_client import call_openai
from app.core.validator import validate
from app.utils.logger import audit

def handler(event):
    """
    RunPod Load Balancer handler function.
    """
    try:
        # Load balancer sends input directly
        job_input = event.get("input", {})

        if not job_input:
            return {
                "error": "No input provided"
            }

        # Audit incoming request
        audit("RUNPOD_REQUEST_RECEIVED", job_input)

        # 1. Build Prompt
        prompt = build_prompt(job_input)

        # 2. Call OpenAI
        ai_raw = call_openai(prompt)

        # 3. Validate Response
        result = validate(ai_raw)

        # Audit success
        audit("RUNPOD_PROFILE_GENERATED", result)

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        audit("RUNPOD_ERROR", str(e))
        return {
            "status": "error",
            "error": str(e)
        }

# IMPORTANT: required for RunPod Serverless
runpod.serverless.start({"handler": handler})
