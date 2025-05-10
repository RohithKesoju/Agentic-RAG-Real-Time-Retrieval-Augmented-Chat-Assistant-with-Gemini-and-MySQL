from fastapi import FastAPI, Request
from agent.agent_handler import run_agent

app = FastAPI()

@app.post("/query")
async def query_agent(request: Request):
    data = await request.json()
    query = data["query"]
    result = await run_agent(query)
    return {"response": result}

from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="ui", html=True), name="ui")

