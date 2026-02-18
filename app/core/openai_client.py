import os
import time
from openai import OpenAI

# Get API key from environment (RunPod Environment Variables)
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_KEY:
    raise Exception("OPENAI_API_KEY environment variable not set")

# Create OpenAI client
client = OpenAI(api_key=OPENAI_KEY)


def call_openai(prompt: str) -> str:
    """
    Call OpenAI safely with timeout, logging, and error handling.
    """

    print("OPENAI CALL STARTED")

    try:
        start_time = time.time()

        response = client.chat.completions.create(
            model="gpt-4o-mini",

            messages=[
                {
                    "role": "system",
                    "content": "You are a senior HR expert. Always respond in valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.1,

            # Force JSON output
            response_format={"type": "json_object"},

            # IMPORTANT → prevents infinite hanging
            timeout=30
        )

        result = response.choices[0].message.content

        end_time = time.time()
        print(f"OPENAI CALL SUCCESS ({end_time-start_time:.2f}s)")

        return result

    except Exception as e:
        print("OPENAI ERROR:", str(e))
        raise Exception(f"OpenAI API failed: {str(e)}")
