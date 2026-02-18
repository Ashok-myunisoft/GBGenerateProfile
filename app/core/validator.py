import json


def validate(raw):

    try:
        return json.loads(raw)
    except Exception:
        raise ValueError("AI returned invalid JSON")
