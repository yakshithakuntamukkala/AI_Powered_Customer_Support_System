from langchain_community.document_loaders import TextLoader
from pathlib import Path


def load_documents():
    """
    Load all knowledge base documents.
    """

    data_path = Path("data")

    files = [
        "company_policy.txt",
        "pricing_guide.txt",
        "technical_manual.txt",
        "faq.txt"
    ]

    documents = []

    for file in files:
        loader = TextLoader(data_path / file)
        documents.extend(loader.load())

    return documents