from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -----------------------------
# Environment state
# -----------------------------

current_email = {
    "id": 1,
    "content": "Customer is asking for a refund for a damaged product."
}

done = False


# -----------------------------
# Action model
# -----------------------------

class ActionRequest(BaseModel):
    action: str


# -----------------------------
# Root endpoint
# -----------------------------

@app.get("/")
def root():
    return {"status": "ok"}


# -----------------------------
# Reset endpoint
# IMPORTANT: no request body
# -----------------------------

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
        "observation": current_email["content"],
        "done": False
    }


# -----------------------------
# Step endpoint
# -----------------------------

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


# -----------------------------
# State endpoint
# -----------------------------

@app.get("/state")
def state():
    return {
        "email": current_email,
        "done": done
    }
