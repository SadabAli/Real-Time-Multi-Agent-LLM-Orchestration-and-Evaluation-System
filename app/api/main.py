from fastapi import FastAPI
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse

from app.agents.orchestrator import orchestrator
from app.evaluation.evaluator import run_evaluation

from app.db.database import SessionLocal
from app.db.models import ExecutionTrace

import asyncio


app = FastAPI()


# -----------------------------
# Request Schema
# -----------------------------
class QueryRequest(BaseModel):
    query: str


# -----------------------------
# Query Endpoint
# -----------------------------
@app.post("/query")
async def query_pipeline(
    request: QueryRequest
):

    async def event_generator():

        query = request.query

        agents = [
            "orchestrator",
            "decomposition_agent",
            "retrieval_agent",
            "critique_agent",
            "synthesis_agent"
        ]

        for agent in agents:

            yield {
                "event": "message",
                "data": f"{agent} running..."
            }

            await asyncio.sleep(1)

        result = orchestrator(query)

        yield {
            "event": "message",
            "data": str(result)
        }

    return EventSourceResponse(
        event_generator()
    )


# -----------------------------
# Trace Endpoint
# -----------------------------
@app.get("/trace/{job_id}")
async def get_trace(job_id: str):

    db = SessionLocal()

    traces = db.query(
        ExecutionTrace
    ).filter(
        ExecutionTrace.job_id == job_id
    ).all()

    db.close()

    return [
        {
            "agent": t.agent,
            "event_type": t.event_type,
            "input": t.input_data,
            "output": t.output_data,
            "latency": t.latency,
            "token_count": t.token_count
        }
        for t in traces
    ]


# -----------------------------
# Latest Evaluation Endpoint
# -----------------------------
@app.get("/eval/latest")
async def latest_eval():

    return run_evaluation()


# -----------------------------
# Prompt Review Endpoint
# -----------------------------
@app.post("/prompt/review")
async def review_prompt():

    return {
        "message":
        "Prompt review recorded"
    }


# -----------------------------
# Re-run Evaluation Endpoint
# -----------------------------
@app.post("/eval/rerun")
async def rerun_eval():

    return {
        "message":
        "Targeted re-evaluation triggered"
    }