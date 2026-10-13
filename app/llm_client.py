"""LLM provider clients used by the summarizer service."""
import os

import anthropic
import openai
import requests

from config.settings import OPENAI_MODEL, ANTHROPIC_MODEL, OLLAMA_URL

openai.api_key = os.getenv("OPENAI_API_KEY")
claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def ask_openai(prompt: str) -> str:
    resp = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp["choices"][0]["message"]["content"]


def ask_claude(prompt: str) -> str:
    msg = claude.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def ask_ollama(prompt: str) -> str:
    r = requests.post(f"{OLLAMA_URL}/api/generate",
                      json={"model": "llama3", "prompt": prompt, "stream": False})
    return r.json()["response"]
