from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.loader import load_documents


def split_documents():
    """
    Split documents into smaller chunks for RAG.
    """

    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    return chunks