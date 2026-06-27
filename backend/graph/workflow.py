from langgraph.graph import StateGraph, START, END

from graph.state import CustomerSupportState
from graph.nodes import receive_customer_query


builder = StateGraph(CustomerSupportState)

builder.add_node("receive_query", receive_customer_query)

builder.add_edge(START, "receive_query")
builder.add_edge("receive_query", END)

graph = builder.compile()