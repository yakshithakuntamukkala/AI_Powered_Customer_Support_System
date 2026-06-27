from graph.state import CustomerSupportState
from memory.sqlite_memory import SQLiteMemory

memory = SQLiteMemory()

def receive_customer_query(state: CustomerSupportState):
    print(f"\nCustomer Query: {state['query']}")
    return state

def retrieve_memory(state: CustomerSupportState):
    """
    Retrieve the customer's previous conversation from SQLite.
    """

    previous = memory.get_last_conversation(state["customer_name"])

    if previous:
        previous_query, previous_response = previous

        state["conversation_history"] = [
            f"Previous Query: {previous_query}",
            f"Previous Response: {previous_response}"
        ]

        print("\nPrevious Conversation Found:")
        print(previous_query)

    else:
        state["conversation_history"] = []
        print("\nNo previous conversation found.")

    return state


def classify_intent(state: CustomerSupportState):
    """
    Classify the customer's query into a department.
    """

    query = state["query"].lower()

    if "previous" in query and "issue" in query:
        state["intent"] = "Memory"
        print("Detected Intent: Memory")
    

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

def save_memory(state: CustomerSupportState):
    """
    Save the latest conversation into SQLite.
    """

    memory.save_conversation(
        state["customer_name"],
        state["query"],
        state["draft_response"]
    )

    print("\nConversation saved to SQLite.")

    return state