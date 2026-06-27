import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from rag.retriever import retrieve_context

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


def answer_with_rag(query: str):

    docs = retrieve_context(query)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a customer support assistant for ABC Technologies.

Answer ONLY using the information below.

Context:
{context}

Customer Question:
{query}

Provide a clear and professional response.
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "documents": docs
    }