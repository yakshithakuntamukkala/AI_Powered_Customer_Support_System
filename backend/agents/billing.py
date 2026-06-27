from graph.state import CustomerSupportState


def billing_agent(state: CustomerSupportState):

    print("Billing Agent is handling the request.")

    state["department"] = "Billing"

    state["draft_response"] = "Billing team will assist you."

    return state