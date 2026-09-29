from gemini_client import generate_json


QUIZ_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string"
            },
            "options": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "minItems": 4,
                "maxItems": 4
            },
            "answer": {
                "type": "string"
            },
            "explanation": {
                "type": "string"
            }
        },
        "required": [
            "question",
            "options",
            "answer",
            "explanation"
        ]
    }
}


def generate_quiz(text: str):

    prompt = f"""
You are EduGenie,
an educational quiz generator.

Create exactly 3 multiple-choice questions
from the educational text below.

Rules:

- Exactly 3 questions.
- Exactly 4 options per question.
- Only one correct answer.
- The answer must exactly match
  one of the options.
- Include a short explanation.
- Questions must be based only
  on the supplied text.

Educational Text:

{text}
"""

    quiz = generate_json(
        prompt,
        QUIZ_SCHEMA,
        max_output_tokens=1800
    )

    if not isinstance(quiz, list):
        raise RuntimeError(
            "Quiz response is not a list."
        )

    if len(quiz) != 3:
        raise RuntimeError(
            "Gemini did not generate exactly 3 questions."
        )

    return quiz