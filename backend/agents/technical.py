from graph.state import CustomerSupportState
from rag.generator import answer_with_rag


def technical_agent(state: CustomerSupportState):

    print("🛠 Technical Support Agent is handling the request...")

    result = answer_with_rag(state["query"])

    state["department"] = "Technical"

    state["retrieved_docs"] = [
        doc.page_content for doc in result["documents"]
    ]

    state["draft_response"] = result["answer"]

    return state