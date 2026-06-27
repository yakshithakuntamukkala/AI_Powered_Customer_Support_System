from graph.state import CustomerSupportState


def human_review(state: CustomerSupportState):

    if state["requires_approval"]:

        print("\n==============================")
        print(" HUMAN APPROVAL REQUIRED ")
        print("==============================")

        print(f"Customer Query:\n{state['query']}")

        approval = input("\nApprove request? (yes/no): ").strip().lower()

        if approval == "yes":
            state["approved"] = True
            print("Request Approved.")
        else:
            state["approved"] = True
            state["final_response"] = (
                "Your request has not been approved by the supervisor."
            )
            print("Request Rejected.")

    return state