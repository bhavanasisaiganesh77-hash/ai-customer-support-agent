from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.support_agent import SupportAgent

app = FastAPI(title="AI Support API")

agent = SupportAgent()


class SupportRequest(BaseModel):
    message: str


@app.get("/health")
def health():
    return {
        "status": "online",
        "service": "AI Support API"
    }


@app.post("/api/chat")
def chat(request: SupportRequest):

    result = agent.respond(request.message)

    return {
        "message": request.message,
        "intent": result["intent"],
        "response": result["final_response"]
    }


app.mount("/", StaticFiles(directory="static", html=True), name="static")
