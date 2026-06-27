from graph.state import CustomerSupportState
from rag.retriever import retrieve_context


def sales_agent(state: CustomerSupportState):

    print("📈 Sales Agent is handling the request...")

    state["department"] = "Sales"

    docs = retrieve_context(state["query"])

    context = "\n\n".join(doc.page_content for doc in docs)

    state["retrieved_docs"] = [doc.page_content for doc in docs]

    state["draft_response"] = context

    return state