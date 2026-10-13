"""Simple RAG pipeline over the docs dataset."""
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Qdrant

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
store = Qdrant.from_existing_collection(embeddings=embeddings, collection_name="docs",
                                        url="http://qdrant:6333")
qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model_name="gpt-4o"),
                                 retriever=store.as_retriever())


def answer(question: str) -> str:
    return qa.run(question)
