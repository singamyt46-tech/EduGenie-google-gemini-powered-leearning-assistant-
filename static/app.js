async function sendRequest(url, data) {

    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    if (!response.ok) {
        throw new Error(
            result.detail || "Something went wrong"
        );
    }

    return result;
}


function showLoading(element) {
    element.innerHTML =
        '<p class="loading">⏳ EduGenie is thinking...</p>';
}


function showError(element, error) {
    element.innerHTML =
        `<p class="error">❌ ${error.message}</p>`;
}


// Question & Answer
async function askQuestion() {

    const question =
        document.getElementById("qaQuestion").value.trim();

    const result =
        document.getElementById("qaResult");

    if (!question) {
        result.innerHTML =
            "<p class='error'>Please enter a question.</p>";
        return;
    }

    showLoading(result);

    try {

        const data = await sendRequest(
            "/qa",
            {
                question: question
            }
        );

        result.innerHTML =
            `<p>${formatText(data.answer)}</p>`;

    } catch (error) {

        showError(result, error);
    }
}


// Topic Explanation
async function explainTopic() {

    const topic =
        document.getElementById("explainTopic").value.trim();

    const level =
        document.getElementById("explainLevel").value;

    const result =
        document.getElementById("explainResult");

    if (!topic) {
        result.innerHTML =
            "<p class='error'>Please enter a topic.</p>";
        return;
    }

    showLoading(result);

    try {

        const data = await sendRequest(
            "/explain",
            {
                topic: topic,
                level: level
            }
        );

        result.innerHTML =
            `<p>${formatText(data.answer)}</p>`;

    } catch (error) {

        showError(result, error);
    }
}


// Quiz Generator
async function generateQuiz() {

    const text =
        document.getElementById("quizText").value.trim();

    const result =
        document.getElementById("quizResult");

    if (!text) {
        result.innerHTML =
            "<p class='error'>Please enter some educational text.</p>";
        return;
    }

    showLoading(result);

    try {

        const data = await sendRequest(
            "/quiz",
            {
                text: text
            }
        );

        displayQuiz(data.quiz, result);

    } catch (error) {

        showError(result, error);
    }
}


// Display Quiz
function displayQuiz(quiz, result) {

    let html = "";

    quiz.forEach((item, index) => {

        html += `
            <div class="quiz-question">

                <h3>
                    ${index + 1}. ${escapeHtml(item.question)}
                </h3>

                <div>
        `;

        item.options.forEach(option => {

            html += `
                <div class="quiz-option">
                    ${escapeHtml(option)}
                </div>
            `;

        });

        html += `
                </div>

                <div class="quiz-answer">
                    ✅ Answer:
                    ${escapeHtml(item.answer)}
                </div>

                <div class="quiz-explanation">
                    💡 ${escapeHtml(item.explanation)}
                </div>

            </div>
        `;

    });

    result.innerHTML = html;
}


// Summarizer
async function summarizeText() {

    const text =
        document.getElementById("summaryText").value.trim();

    const result =
        document.getElementById("summaryResult");

    if (!text) {
        result.innerHTML =
            "<p class='error'>Please enter text to summarize.</p>";
        return;
    }

    showLoading(result);

    try {

        const data = await sendRequest(
            "/summarize",
            {
                text: text
            }
        );

        result.innerHTML =
            `<p>${formatText(data.summary)}</p>`;

    } catch (error) {

        showError(result, error);
    }
}


// Learning Path
async function getLearningPath() {

    const topic =
        document.getElementById("learningTopic").value.trim();

    const level =
        document.getElementById("learningLevel").value;

    const result =
        document.getElementById("learningResult");

    if (!topic) {
        result.innerHTML =
            "<p class='error'>Please enter a topic.</p>";
        return;
    }

    showLoading(result);

    try {

        const data = await sendRequest(
            "/learn/recommendations",
            {
                topic: topic,
                level: level
            }
        );

        result.innerHTML =
            `<p>${formatText(data.recommendations)}</p>`;

    } catch (error) {

        showError(result, error);
    }
}


// Basic text formatting
function formatText(text) {

    return escapeHtml(text)
        .replace(/\n/g, "<br>");
}


// Prevent HTML injection
function escapeHtml(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}