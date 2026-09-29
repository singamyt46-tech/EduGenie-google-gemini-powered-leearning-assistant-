from gemini_client import generate_text


def answer_question(question: str) -> str:

    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question accurately,
clearly, and concisely.

Explain difficult terms when necessary.

If the question is ambiguous,
clearly state the assumption.

Do not invent sources or citations.

Student Question:

{question}

Provide a useful educational answer.
"""

    return generate_text(
        prompt,
        temperature=0.3,
        max_output_tokens=1000
    )