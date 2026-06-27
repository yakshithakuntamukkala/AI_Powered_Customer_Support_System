from graph.approval import requires_human_approval

state = {
    "query": "What are your pricing plans?",
    "requires_approval": False
}

result = requires_human_approval(state)

print(result)