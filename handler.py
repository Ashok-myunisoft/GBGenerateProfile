import runpod
from app.core.prompt_builder import build_prompt
from app.core.openai_client import call_openai
from app.core.validator import validate
from app.utils.logger import audit

def handler(job):
    """
    RunPod handler function.
    """
    job_input = job.get("input", {})
    
    # Validate input presence
    if not job_input:
        return {"error": "No input provided"}

    try:
        # Audit the incoming request
        audit("RUNPOD_REQUEST_RECEIVED", job_input)

        # 1. Build Prompt
        prompt = build_prompt(job_input)

        # 2. Call OpenAI
        ai_raw = call_openai(prompt)

        # 3. Validate Response
        result = validate(ai_raw)
        
        # Audit success
        audit("RUNPOD_PROFILE_GENERATED", result)

        return result

    except Exception as e:
        audit("RUNPOD_ERROR", str(e))
        return {"error": str(e)}

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
