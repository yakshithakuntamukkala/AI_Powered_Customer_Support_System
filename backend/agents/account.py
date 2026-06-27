from graph.state import CustomerSupportState


def account_agent(state: CustomerSupportState):

    print("Account Agent is handling the request.")

    state["department"] = "Account"

    state["draft_response"] = "Account team will assist you."

    return state