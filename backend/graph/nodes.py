from graph.state import CustomerSupportState


def receive_customer_query(state: CustomerSupportState):
    print(f"\nCustomer Query: {state['query']}")
    return state


def classify_intent(state: CustomerSupportState):
    """
    Classify the customer's query into a department.
    """

    query = state["query"].lower()

    if any(word in query for word in ["price", "pricing", "plan", "subscription"]):
        state["intent"] = "Sales"

    elif any(word in query for word in ["error", "bug", "login", "crash", "install", "configuration"]):
        state["intent"] = "Technical"

    elif any(word in query for word in ["invoice", "payment", "refund", "billing"]):
        state["intent"] = "Billing"

    elif any(word in query for word in ["password", "profile", "account", "activate", "deactivate"]):
        state["intent"] = "Account"

    else:
        state["intent"] = "Unknown"

    print(f"Detected Intent: {state['intent']}")

    return state