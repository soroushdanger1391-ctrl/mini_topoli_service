import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

@app.route("/")
def home():
    return "MINI TOPOLI SERVER IS READY!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "")

    if not isinstance(question, str) or not question.strip():
        return jsonify({"error": "پیام خالی است"}), 400

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions="تو تپلی هستی؛ یک دستیار فارسی دوستانه و کوتاه‌گو.",
        input=question
    )

    return jsonify({"answer": response.output_text})

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
                               )
