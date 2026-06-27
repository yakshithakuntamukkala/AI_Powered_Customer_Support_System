from memory.sqlite_memory import SQLiteMemory

memory = SQLiteMemory()

memory.save_conversation(
    "David",
    "I have a billing issue.",
    "Billing department will assist you."
)

previous = memory.get_last_conversation("David")

print(previous)