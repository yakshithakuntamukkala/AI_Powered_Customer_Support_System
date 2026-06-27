from rag.retriever import create_vector_store

vectorstore = create_vector_store()

retriever = vectorstore.as_retriever()

query = "What are the pricing plans?"

docs = retriever.invoke(query)

print("\nRetrieved Documents:\n")

for doc in docs:
    print("=" * 60)
    print(doc.page_content)
    print()