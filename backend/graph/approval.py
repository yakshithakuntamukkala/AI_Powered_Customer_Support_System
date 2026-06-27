from graph.state import CustomerSupportState


HIGH_RISK_KEYWORDS = [
    "refund",
    "cancel",
    "cancellation",
    "account closure",
    "close account",
    "compensation",
    "manager",
    "management",
    "escalate"
]


def requires_human_approval(state: CustomerSupportState):

    query = state["query"].lower()

    for keyword in HIGH_RISK_KEYWORDS:
        if keyword in query:
            state["requires_approval"] = True
            return state

    state["requires_approval"] = False
    return state