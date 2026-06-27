from graph.workflow import graph

state = {
    "customer_name": "David",
    "query": "I need a refund.",
    "intent": "",
    "department": "",
    "retrieved_docs": [],
    "draft_response": "",
    "requires_approval": False,
    "approved": False,
    "final_response": "",
    "conversation_history": [],
}

result = graph.invoke(state)

print(result)