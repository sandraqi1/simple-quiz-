from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of Rwanda",
        "answer": "kigali"
    },
    {
        "question": "What is 5+3?",
        "answer": "8"   
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "answer": "def"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    score = 0
    if request.method == "POST":
        for i in range(len(questions)):
            user_answer = request.form.get(f"q{i}", "").lower()  # ← Added default ""
            if user_answer == questions[i]["answer"]:
                score += 1
        return render_template("quiz.html", questions=questions, score=score)
    return render_template("quiz.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)