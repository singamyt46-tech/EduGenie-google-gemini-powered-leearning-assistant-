from gemini_client import generate_text


def explain_topic(
    topic: str,
    level: str = "beginner"
) -> str:

    prompt = f"""
You are EduGenie,
a friendly and patient teacher.

Explain the following topic
for a {level} learner.

Topic:

{topic}

Use the following structure:

1. Definition
2. Simple explanation
3. Real-world example
4. Important points
5. Short revision summary

Avoid unnecessary technical jargon.

Make the explanation easy for a student
to understand and revise.
"""

    return generate_text(
        prompt,
        temperature=0.35,
        max_output_tokens=1200
    )