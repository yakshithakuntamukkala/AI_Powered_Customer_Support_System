from agents.supervisor import supervisor_agent

state = {
    "query": "I need a refund.",
    "draft_response": "Refund request received.",
    "final_response": ""
}

result = supervisor_agent(state)

print(result["final_response"])