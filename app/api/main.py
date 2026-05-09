from fastapi import FastAPI
from app.agents.orchestrator import orchestrator

app = FastAPI()


@app.get("/")
async def home():

    return {
        "message": "Multi-Agent System Running"
    }


@app.get("/query")
async def query(q: str):

    result = orchestrator(q)

    return result