from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ---------------------------
# Environment State
# ---------------------------

current_email = {
    "id": 1,
    "content": "Customer is asking for a refund for a damaged product."
}

done = False


# ---------------------------
# Request Model
# ---------------------------

class Action(BaseModel):
    action: str


# ---------------------------
# Root Endpoint
# ---------------------------

@app.get("/")
def root():
    return {"status": "ok"}


# ---------------------------
# Reset Environment
# ---------------------------

@app.post("/reset")
def reset():
    global current_email, done

    done = False
    current_email = {
        "id": 1,
        "content": "Customer is asking for a refund for a damaged product."
    }

    return {
        "task": "Handle the incoming customer email",
        "observation": current_email["content"]
    }


# ---------------------------
# Step Function
# ---------------------------

@app.post("/step")
def step(action: Action):
    global done

    correct_action = "reply"

    reward = 1 if action.action.lower() == correct_action else 0
    done = True

    return {
        "observation": "Action processed",
        "reward": reward,
        "done": done
    }


# ---------------------------
# State Endpoint
# ---------------------------

@app.get("/state")
def state():
    return {
        "email": current_email,
        "done": done
    }
