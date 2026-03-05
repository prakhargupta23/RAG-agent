from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import run_agent

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    answer = run_agent(request.question)
    return {"answer": answer}