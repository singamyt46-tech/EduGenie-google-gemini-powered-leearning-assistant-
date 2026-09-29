import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


# Load environment variables from .env
load_dotenv()


# Project folder
BASE_DIR = Path(__file__).resolve().parent


# Create FastAPI application
app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


# Serve CSS and JavaScript files
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


# Templates folder
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# -----------------------------
# Request Models
# -----------------------------

class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=10000
    )


class TopicRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=1,
        max_length=5000
    )

    level: str = Field(
        default="beginner",
        max_length=50
    )


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=30000
    )


# -----------------------------
# Home Page
# -----------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "gemini_configured": bool(
            os.getenv("GEMINI_API_KEY")
        )
    }


# -----------------------------
# Question & Answer
# -----------------------------

@app.post("/qa")
async def qa(request: QuestionRequest):

    try:

        answer = answer_question(
            request.question
        )

        return {
            "answer": answer
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# -----------------------------
# Topic Explanation
# -----------------------------

@app.post("/explain")
async def explain(request: TopicRequest):

    try:

        answer = explain_topic(
            request.topic,
            request.level
        )

        return {
            "answer": answer
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# -----------------------------
# Quiz Generator
# -----------------------------

@app.post("/quiz")
async def quiz(request: TextRequest):

    try:

        quiz = generate_quiz(
            request.text
        )

        return {
            "quiz": quiz
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# -----------------------------
# Text Summarizer
# -----------------------------

@app.post("/summarize")
async def summarize(request: TextRequest):

    try:

        summary = summarize_text(
            request.text
        )

        return {
            "summary": summary
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# -----------------------------
# Personalized Learning Path
# -----------------------------

@app.post("/learn/recommendations")
async def learning_recommendations(
    request: TopicRequest
):

    try:

        recommendations = get_learning_recommendations(
            request.topic,
            request.level
        )

        return {
            "recommendations": recommendations
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )