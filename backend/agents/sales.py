from graph.state import CustomerSupportState


def sales_agent(state: CustomerSupportState):

    print("Sales Agent is handling the request.")

    state["department"] = "Sales"

    state["draft_response"] = "Sales team will assist you."

    return state