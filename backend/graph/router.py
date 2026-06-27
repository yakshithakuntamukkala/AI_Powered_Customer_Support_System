from graph.state import CustomerSupportState


def route_department(state: CustomerSupportState):
    """
    Decide which department should handle the query.
    """

    intent = state["intent"]

    if intent == "Sales":
        return "sales_agent"

    elif intent == "Technical":
        return "technical_agent"

    elif intent == "Billing":
        return "billing_agent"

    elif intent == "Account":
        return "account_agent"

    return "sales_agent"