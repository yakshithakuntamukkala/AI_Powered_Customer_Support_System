from graph.workflow import graph

state = {
    "customer_name": "David",
    "query": "What are your pricing plans?",
    "intent": "",
    "department": "",
    "retrieved_docs": [],
    "draft_response": "",
    "requires_approval": False,
    "approved": False,
    "final_response": "",
    "previous_query": "",
    "previous_response": ""
}

result = graph.invoke(state)

print("\n========== FINAL STATE ==========")

for key, value in result.items():
    print(f"{key}: {value}")