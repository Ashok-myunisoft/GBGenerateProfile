def build_prompt(data):

    return f"""
Generate a COMPLETE job profile.

Use this schema strictly.

{{
 "job_description": "string",
 "kpis": ["string"],
 "skills_matrix": {{
  "technical": ["string"],
  "soft": ["string"],
  "domain": ["string"]
 }},
 "interview_questions": {{
  "technical": ["string"],
  "managerial": ["string"],
  "situational": ["string"]
 }},
 "psychometric_tools": ["string"],
 "experience_qualifications": "string"
}}

Data:

Position: {data['position']}
Department: {data['department']}
Level: {data['level']}
Industry: {data['industry']}
Context: {data['context']}
"""
