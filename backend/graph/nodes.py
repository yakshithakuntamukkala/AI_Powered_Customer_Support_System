from graph.state import CustomerSupportState


def receive_customer_query(state: CustomerSupportState):
    """
    Entry node of the graph.
    Receives the customer's query.
    """

    print("Customer Query:", state["query"])

    return state