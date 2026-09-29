# 🎓 EduGenie – Google Gemini Powered Learning Assistant

EduGenie is an AI-powered learning assistant designed to help students learn, understand, revise, and practice educational topics using Google Gemini.

The application provides an interactive web interface where students can ask questions, get topic explanations, generate quizzes, summarize text, and create personalized learning paths.

---

## 🚀 Features

### 💬 1. Ask a Question
Students can ask educational questions and receive clear and concise AI-generated answers.

### 📚 2. Explain a Topic
EduGenie explains a topic according to the learner's level:

- Beginner
- Intermediate
- Advanced

The explanation includes definitions, simple explanations, examples, important points, and a short revision summary.

### 📝 3. Generate Quiz
Students can paste educational content and generate:

- 3 multiple-choice questions
- 4 options for each question
- Correct answer
- Explanation for each answer

### 📖 4. Summarize Text
EduGenie converts long educational content into a simple and useful summary for quick revision.

### 🛤️ 5. Personalized Learning Path
Students can enter a topic and learning level to receive a structured learning path containing:

- Prerequisites
- Beginner concepts
- Intermediate concepts
- Advanced concepts
- Learning sequence
- Practice activities
- Project ideas
- Useful resource types

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn

### AI
- Google Gemini API
- Google GenAI Python SDK

### Other Technologies
- Jinja2
- Pydantic
- python-dotenv

---

## 📂 Project Structure

```text
EduGenie-AI/
│
├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── app.js
    └── style.css
