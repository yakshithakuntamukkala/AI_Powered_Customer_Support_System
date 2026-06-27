from graph.state import CustomerSupportState


def memory_agent(state: CustomerSupportState):

    print("🧠 Memory Agent is handling the request...")

    if state["conversation_history"]:
        state["draft_response"] = "\n".join(state["conversation_history"])
    else:
        state["draft_response"] = "No previous conversation found."

    return state