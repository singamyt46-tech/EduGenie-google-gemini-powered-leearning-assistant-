from gemini_client import generate_text


def get_learning_recommendations(
    topic: str,
    level: str = "beginner"
) -> str:

    prompt = f"""
You are EduGenie,
a personalized learning-path assistant.

Create a structured learning path
for the following topic:

Topic:
{topic}

Learner Level:
{level}

Include:

1. Prerequisites
2. Beginner concepts
3. Intermediate concepts
4. Advanced concepts
5. Recommended learning sequence
6. Practice activities
7. Project ideas
8. Types of useful resources

The learning path should progress
from beginner to advanced.

Do not invent specific URLs.
"""

    return generate_text(
        prompt,
        temperature=0.45,
        max_output_tokens=1800
    )