from langgraph.graph import StateGraph, START, END

from graph.state import CustomerSupportState
from graph.nodes import (
    receive_customer_query,
    classify_intent,
)

from graph.router import route_department

from agents.sales import sales_agent
from agents.technical import technical_agent
from agents.billing import billing_agent
from agents.account import account_agent


builder = StateGraph(CustomerSupportState)

# Nodes
builder.add_node("receive_query", receive_customer_query)
builder.add_node("intent_classifier", classify_intent)

builder.add_node("sales_agent", sales_agent)
builder.add_node("technical_agent", technical_agent)
builder.add_node("billing_agent", billing_agent)
builder.add_node("account_agent", account_agent)

# Flow
builder.add_edge(START, "receive_query")
builder.add_edge("receive_query", "intent_classifier")

# Conditional Routing
builder.add_conditional_edges(
    "intent_classifier",
    route_department
)

# End after each department
builder.add_edge("sales_agent", END)
builder.add_edge("technical_agent", END)
builder.add_edge("billing_agent", END)
builder.add_edge("account_agent", END)

graph = builder.compile()