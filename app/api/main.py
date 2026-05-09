from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {
        "message": "Multi-Agent System Running"
    }