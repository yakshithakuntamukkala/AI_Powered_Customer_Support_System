from graph.nodes import (

receive_customer_query,

retrieve_memory,

classify_intent,

save_memory

)

from agents.memory import memory_agent

from graph.approval import requires_human_approval

from graph.human_review import human_review

from agents.supervisor import supervisor_agent

from langgraph.graph import StateGraph, START, END

from graph.state import CustomerSupportState

from graph.router import route_department

from agents.sales import sales_agent

from agents.technical import technical_agent

from agents.billing import billing_agent

from agents.account import account_agent

builder = StateGraph(CustomerSupportState)

#Nodes

builder.add_node("receive_query", receive_customer_query)

builder.add_node("intent_classifier", classify_intent)

builder.add_node("sales_agent", sales_agent)

builder.add_node("technical_agent", technical_agent)

builder.add_node("billing_agent", billing_agent)

builder.add_node("account_agent", account_agent)

builder.add_node("retrieve_memory", retrieve_memory)

builder.add_node("save_memory", save_memory)

builder.add_node("approval_check", requires_human_approval)

builder.add_node("human_review", human_review)

builder.add_node("supervisor", supervisor_agent)

builder.add_node("memory_agent", memory_agent)



#Flow

builder.add_edge(START, "receive_query")

builder.add_edge("receive_query", "retrieve_memory")

builder.add_edge("retrieve_memory", "intent_classifier")

builder.add_edge("memory_agent", "human_review")

#Check if approval is needed

builder.add_edge("intent_classifier", "approval_check")

#After approval check, continue with routing

builder.add_conditional_edges(

"approval_check",

route_department

)

#Every agent goes to human review

builder.add_edge("sales_agent", "human_review")

builder.add_edge("technical_agent", "human_review")

builder.add_edge("billing_agent", "human_review")

builder.add_edge("account_agent", "human_review")

#Then supervisor reviews

builder.add_edge("human_review", "supervisor")

#Finally save conversation

builder.add_edge("supervisor", "save_memory")

builder.add_edge("save_memory", END)

graph = builder.compile()
