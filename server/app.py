from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Global state
current_email = {
    "id": 1,
    "content": "Customer is asking for a refund for a damaged product."
}

done = False


class ResetRequest(BaseModel):
    pass


class ActionRequest(BaseModel):
    action: str


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/reset")
def reset(req: ResetRequest):
    global current_email, done

    done = False

    current_email = {
        "id": 1,
        "content": "Customer is asking for a refund for a damaged product."
    }

    return {
        "observation": current_email["content"],
        "done": False
    }


@app.post("/step")
def step(request: ActionRequest):
    global done

    correct_action = "reply"

    if request.action.lower() == correct_action:
        reward = 1
    else:
        reward = 0

    done = True

    return {
        "observation": "Action processed",
        "reward": reward,
        "done": done
    }


@app.get("/state")
def state():
    return {
        "email": current_email,
        "done": done
    }
