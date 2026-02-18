from openai import OpenAI
from app.config import OPENAI_KEY

client = OpenAI(api_key=OPENAI_KEY)


def call_openai(prompt: str) -> str:

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a senior HR expert. Always respond in valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,

        # FORCE JSON OUTPUT
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content
