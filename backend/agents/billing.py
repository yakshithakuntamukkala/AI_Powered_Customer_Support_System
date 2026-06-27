from graph.state import CustomerSupportState


def billing_agent(state: CustomerSupportState):

    print("💳 Billing Agent is handling the request...")

    state["department"] = "Billing"

    query = state["query"].lower()

    if "refund" in query:
        response = (
            "Your refund request has been received and will be reviewed."
        )

    elif "invoice" in query:
        response = (
            "Invoices are available in the Billing section of your account."
        )

    else:
        response = (
            "Our Billing Team will assist you."
        )

    state["draft_response"] = response

    return state