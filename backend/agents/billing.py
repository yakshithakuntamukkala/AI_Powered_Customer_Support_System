from graph.state import CustomerSupportState
from rag.generator import answer_with_rag


def billing_agent(state: CustomerSupportState):

    print("💳 Billing Agent is handling the request...")

    result = answer_with_rag(state["query"])

    state["department"] = "Billing"

    state["retrieved_docs"] = [
        doc.page_content for doc in result["documents"]
    ]

    state["draft_response"] = result["answer"]

    return state