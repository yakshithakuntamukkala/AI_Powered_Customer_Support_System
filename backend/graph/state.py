from typing import TypedDict, List


class CustomerSupportState(TypedDict):
    customer_name: str

    query: str

    intent: str

    department: str

    retrieved_docs: List[str]

    draft_response: str

    requires_approval: bool

    approved: bool

    final_response: str

    previous_query: str

    previous_response: str