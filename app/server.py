from flask import Flask, jsonify, request

from app.llm_client import ask_claude, ask_openai
from app.rag import answer

app = Flask(__name__)


@app.post("/chat")
def chat():
    body = request.get_json()
    provider = body.get("provider", "openai")
    fn = ask_claude if provider == "anthropic" else ask_openai
    return jsonify({"reply": fn(body["prompt"])})


@app.post("/ask")
def ask():
    return jsonify({"answer": answer(request.get_json()["question"])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
