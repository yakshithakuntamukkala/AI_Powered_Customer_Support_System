from graph.state import CustomerSupportState


def account_agent(state: CustomerSupportState):

    print("👤 Account Agent is handling the request...")

    state["department"] = "Account"

    query = state["query"].lower()

    if "password" in query:
        response = (
            "Click 'Forgot Password' on the login page to reset your password."
        )

    elif "profile" in query:
        response = (
            "You can update your profile information from Account Settings."
        )

    else:
        response = (
            "Our Account Team will assist you."
        )

    state["draft_response"] = response

    return state