import requests

BASE_URL = "https://jkkingjk-email-triage-env.hf.space"

def reset():
    r = requests.post(f"{BASE_URL}/reset")
    return r.json()

def step(action):
    r = requests.post(f"{BASE_URL}/step", json={"action": action})
    return r.json()

if __name__ == "__main__":
    print(reset())