from graph.state import CustomerSupportState


def technical_agent(state: CustomerSupportState):

    print("Technical Support Agent is handling the request.")

    state["department"] = "Technical"

    state["draft_response"] = "Technical team will assist you."

    return state