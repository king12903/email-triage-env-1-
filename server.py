from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn

from environment import EmailTriageEnv, Action

app = FastAPI()
envs = {}

class ResetRequest(BaseModel):
    task_id: str = "easy"

class StepRequest(BaseModel):
    task_id: str
    priority: str
    category: str
    should_reply: bool
    reply_text: Optional[str] = None

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/reset")
def reset(req: ResetRequest):
    env = EmailTriageEnv(req.task_id)
    envs[req.task_id] = env
    return env.reset().dict()

@app.post("/step")
def step(req: StepRequest):
    env = envs.get(req.task_id)
    if not env:
        raise HTTPException(400, "Reset first")

    action = Action(**req.dict())
    obs, reward, done, _ = env.step(action)

    return {
        "observation": obs.dict() if obs else None,
        "reward": reward.dict(),
        "done": done
    }

@app.get("/state")
def state(task_id: str):
    env = envs.get(task_id)
    return env.state().dict()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)