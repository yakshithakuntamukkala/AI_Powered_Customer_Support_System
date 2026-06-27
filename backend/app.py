from fastapi import FastAPI

app = FastAPI(
    title="Customer Support AI",
    description="AI-Powered Customer Support Automation System using LangGraph",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Customer Support AI Backend is Running!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }