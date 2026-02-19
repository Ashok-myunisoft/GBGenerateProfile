import runpod
from app.api.routes import generate, ProfileRequest
from pydantic import ValidationError
import json
import traceback

def handler(event):
    """
    RunPod handler for generating AI profiles - FIXED VERSION
    """
    try:
        # 1. Extract input
        job_input = event.get("input")
        if not job_input:
            return {"error": "No input provided", "output": None}

        print(f"✅ Received input: {job_input}")

        # 2. Validate input using Pydantic model
        try:
            profile_request = ProfileRequest(**job_input)
            print(f"✅ Validated request: {profile_request}")
        except ValidationError as e:
            error_msg = f"Validation error: {e.errors()}"
            print(f"❌ {error_msg}")
            return {"error": error_msg, "output": None}

        # 3. Process logic
        print("🔄 Calling generate function...")
        result = generate(profile_request)
        print(f"✅ Generate returned type: {type(result)}")
        
        # 4. CRITICAL: Format the output exactly as RunPod expects
        # RunPod expects a dictionary with an "output" field
        formatted_response = {
            "output": result  # Wrap whatever result is in an "output" field
        }
        
        # 5. Verify it's JSON serializable (RunPod requirement)
        try:
            # Test if it can be serialized
            json.dumps(formatted_response)
            print("✅ Response is JSON serializable")
            return formatted_response
        except TypeError as e:
            print(f"❌ Response not JSON serializable: {e}")
            # If result itself isn't serializable, convert it to string
            return {
                "output": {
                    "data": str(result),
                    "type": str(type(result))
                }
            }

    except Exception as e:
        print(f"❌ ERROR: {traceback.format_exc()}")
        return {
            "error": f"Internal server error: {str(e)}",
            "output": None
        }

if __name__ == "__main__":
    print("🚀 Starting RunPod serverless worker...")
    runpod.serverless.start({"handler": handler})