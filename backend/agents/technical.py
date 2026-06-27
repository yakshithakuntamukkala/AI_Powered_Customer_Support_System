from graph.state import CustomerSupportState


def technical_agent(state: CustomerSupportState):

    print("🛠 Technical Support Agent is handling the request...")

    state["department"] = "Technical"

    query = state["query"].lower()

    if "crash" in query:
        response = (
            "Please restart the application, verify the latest version is installed, "
            "and check the application logs."
        )

    elif "login" in query:
        response = (
            "Please verify your username and password, then try resetting your password if necessary."
        )

    else:
        response = (
            "Our Technical Support Team will investigate your issue."
        )

    state["draft_response"] = response

    return state