from rag.generator import answer_with_rag

response = answer_with_rag(
    "What pricing plans are available?"
)

print("\nGenerated Answer:\n")

print(response["answer"])

print("\nRetrieved Documents:")

for doc in response["documents"]:
    print("=" * 60)
    print(doc.page_content)