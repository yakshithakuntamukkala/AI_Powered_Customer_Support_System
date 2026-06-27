from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from rag.embeddings import split_documents


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    split_documents(),
    embeddings
)


def retrieve_context(query: str):

    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    docs = retriever.invoke(query)

    return docs