from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse
import asyncio

app = FastAPI()


@app.get("/")
async def home():
    return {
        "message": "Multi-Agent System Running"
    }


@app.get("/stream")
async def stream():

    async def event_generator():

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

        yield {
            "event": "message",
            "data": "pipeline complete"
        }

    return EventSourceResponse(event_generator())