"""Local Hugging Face inference: summarization + embeddings."""
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

CHAT_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"
tokenizer = AutoTokenizer.from_pretrained(CHAT_MODEL)
model = AutoModelForCausalLM.from_pretrained(CHAT_MODEL)


def summarize(text: str) -> str:
    return summarizer(text, max_length=120, min_length=30)[0]["summary_text"]


def embed(texts):
    return embedder.encode(texts)
