import runpod
from app.core.prompt_builder import build_prompt
from app.core.openai_client import call_openai
from app.core.validator import validate
from app.utils.logger import audit


def handler(event):

    print("EVENT RECEIVED:", event, flush=True)

    try:
        job_input = event

        if not job_input:
            return {"error": "No input provided"}

        audit("RUNPOD_REQUEST_RECEIVED", job_input)

        prompt = build_prompt(job_input)

        ai_raw = call_openai(prompt)

        result = validate(ai_raw)

        audit("RUNPOD_PROFILE_GENERATED", result)

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:

        print("ERROR:", str(e), flush=True)

        return {"error": str(e)}


runpod.serverless.start({"handler": handler})
