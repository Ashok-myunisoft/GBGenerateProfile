import runpod
from app.core.prompt_builder import build_prompt
from app.core.openai_client import call_openai
from app.core.validator import validate
from app.utils.logger import audit


def handler(event):
    """
    RunPod Load Balancer handler function.
    Load balancer sends JSON body directly as event.
    """

    print("LOAD BALANCER EVENT RECEIVED:", event)

    try:
        # FIX: Use event directly (NOT event.get("input"))
        job_input = event

        if not job_input:
            return {
                "status": "error",
                "error": "No input provided"
            }

        # Audit incoming request
        audit("RUNPOD_REQUEST_RECEIVED", job_input)

        print("BUILDING PROMPT")
        prompt = build_prompt(job_input)

        print("CALLING OPENAI")
        ai_raw = call_openai(prompt)

        print("VALIDATING RESPONSE")
        result = validate(ai_raw)

        audit("RUNPOD_PROFILE_GENERATED", result)

        print("SUCCESS")

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        print("ERROR:", str(e))
        audit("RUNPOD_ERROR", str(e))

        return {
            "status": "error",
            "error": str(e)
        }


# Required for RunPod Serverless / Load Balancer
runpod.serverless.start({
    "handler": handler
})
