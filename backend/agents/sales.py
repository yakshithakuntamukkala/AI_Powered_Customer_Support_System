from graph.state import CustomerSupportState


def sales_agent(state: CustomerSupportState):

    print("📈 Sales Agent is handling the request...")

    state["department"] = "Sales"

    query = state["query"].lower()

    if "price" in query or "pricing" in query:
        response = (
            "We offer Basic, Professional, and Enterprise plans. "
            "You can choose the plan that best fits your business needs."
        )

    elif "subscription" in query:
        response = (
            "We provide monthly and annual subscription plans."
        )

    else:
        response = (
            "Our Sales Team will help you with product and pricing information."
        )

    state["draft_response"] = response

    return state