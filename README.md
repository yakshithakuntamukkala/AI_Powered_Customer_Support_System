# AI_Powered_Customer_Support_System
AI-Powered Customer Support Automation System using LangGraph, RAG, SQLite Memory, and Human-in-the-Loop.

#AI-Powered Customer Support Automation System

An intelligent Customer Support Automation System built using **LangGraph**, **LangChain**, **Groq LLM**, **FAISS**, and **SQLite Memory**. The system classifies customer queries, retrieves relevant company information using Retrieval-Augmented Generation (RAG), maintains conversation history, routes requests to specialized support agents, and supports Human-in-the-Loop approval for high-risk operations.

---

##Project Overview

ABC Technologies receives thousands of customer support requests daily. This project automates customer support using AI by:

* Classifying customer queries
* Routing requests to specialized support agents
* Retrieving information from company documents using RAG
* Maintaining customer conversation history with SQLite
* Requesting human approval for critical requests
* Reviewing responses using a Supervisor Agent

---

#Features

*  LangGraph Workflow
*  Intent Classification
*  Conditional Routing
*  Specialized Support Agents
*  Retrieval-Augmented Generation (RAG)
*  SQLite Conversation Memory
*  Human-in-the-Loop Approval
*  Supervisor Agent
*  Multi-Agent Architecture
*  FAISS Vector Store
*  Groq LLM Integration

---

#Technologies Used

* Python
* LangGraph
* LangChain
* LangChain-Groq
* Groq API
* FAISS
* SQLite
* FastAPI
* HuggingFace Embeddings
* Python Dotenv

---

#Project Structure

```text
customer-support-ai-langgraph/
│
├── backend/
│   ├── agents/
│   ├── graph/
│   ├── rag/
│   ├── memory/
│   ├── data/
│   ├── app.py
│   ├── requirements.txt
│   └── memory.db
│
├── diagrams/
│   └── workflow.png
│
├── docs/
│
├── screenshots/
│
├── README.md
└── LICENSE
```

---

#Workflow

```text
START
   │
Receive Customer Query
   │
Retrieve Memory (SQLite)
   │
Intent Classification
   │
Human Approval Check
   │
Route to Department
   │
Sales | Technical | Billing | Account
   │
Supervisor Agent
   │
Save Conversation
   │
END
```

---

#Knowledge Base

The system retrieves information from:

* Company Policy
* Pricing Guide
* Technical Manual
* FAQ Document

using Retrieval-Augmented Generation (RAG).

---

#Memory

SQLite is used to store customer conversations.

Example:

Customer:

> My name is David. I have a billing issue.

Later:

> What was my previous support issue?

The system retrieves the previous conversation from SQLite memory.

---

#Human-in-the-Loop

The following requests require human approval:

* Refund Requests
* Subscription Cancellation
* Account Closure
* Compensation Requests
* Escalation to Management

---

#Demonstration Queries

| Query                                            | Department               |
| ------------------------------------------------ | ------------------------ |
| What are the pricing plans available?            | Sales                    |
| I forgot my account password.                    | Account                  |
| My application crashes whenever I upload a file. | Technical                |
| I need a refund for my annual subscription.      | Billing + Human Approval |
| What was my previous support issue?              | Memory                   |

---

#Installation

Clone the repository

```bash
git clone https://github.com/yakshithakuntamukkala/AI_Powered_Customer_Support_System.git
```

Navigate to the project

```bash
cd AI_Powered_Customer_Support_System/backend
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / Codespaces

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here.
```

Run the application

```bash
python app.py
```

---

#Screenshots

The `screenshots/` folder contains:

* Agent Routing
* RAG Retrieval
* SQLite Memory
* Human Approval
* Supervisor Review
* Final Response

---

#Assignment Tasks Completed

* Task 1 – LangGraph Workflow
* Task 2 – State Management
* Task 3 – Intent Classification
* Task 4 – Conditional Routing
* Task 5 – Specialized Agents
* Task 6 – RAG Integration
* Task 7 – SQLite Memory
* Task 8 – Human-in-the-Loop
* Task 9 – Supervisor Agent
* Task 10 – System Demonstration

---

#Author

**Yakshitha Kuntamukkala**

VIT-AP University

Computer Science and Engineering

---

#License

This project is developed for educational purposes as part of a LangGraph-based AI Customer Support Automation System assignment.

