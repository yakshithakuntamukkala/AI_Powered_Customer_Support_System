import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from graph.state import CustomerSupportState

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


def supervisor_agent(state: CustomerSupportState):

    print("👨‍💼 Supervisor Agent reviewing response...")

    prompt = f"""
You are a senior customer support supervisor.

Review the draft response below.

Make it:
- Professional
- Polite
- Clear
- Grammatically correct

Customer Query:
{state["query"]}

Draft Response:
{state["draft_response"]}

Return only the improved response.
"""

    response = llm.invoke(prompt)

    state["final_response"] = response.content

    return state