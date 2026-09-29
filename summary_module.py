from gemini_client import generate_text


def summarize_text(text: str) -> str:

    prompt = f"""
You are EduGenie,
an educational summarization assistant.

Summarize the following passage
for quick student revision.

Requirements:

- Keep the important facts.
- Remove unnecessary repetition.
- Keep the original meaning.
- Use simple language.
- Use bullet points where useful.
- Do not add unsupported information.

Educational Passage:

{text}
"""

    return generate_text(
        prompt,
        temperature=0.2,
        max_output_tokens=1200
    )