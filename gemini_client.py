import json
import os
from functools import lru_cache

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load .env BEFORE reading the model name
load_dotenv()

MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.5-flash-lite"
)


@lru_cache(maxsize=1)
def get_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. "
            "Please create a .env file and add your Gemini API key."
        )

    return genai.Client(api_key=api_key)


def generate_text(
    prompt: str,
    temperature: float = 0.4,
    max_output_tokens: int = 1200
):
    client = get_client()

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_output_tokens
        )
    )

    text = getattr(response, "text", None)

    if not text:
        raise RuntimeError(
            "Gemini returned an empty response."
        )

    return text.strip()


def generate_json(
    prompt: str,
    schema: dict,
    max_output_tokens: int = 1800
):
    client = get_client()

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=max_output_tokens,
            response_mime_type="application/json",
            response_schema=schema
        )
    )

    text = getattr(response, "text", None)

    if not text:
        raise RuntimeError(
            "Gemini returned an empty JSON response."
        )

    try:
        return json.loads(text)

    except json.JSONDecodeError as error:
        raise RuntimeError(
            f"Invalid JSON returned by Gemini: {error}"
        )