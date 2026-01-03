from datetime import datetime

def context_agent(message: dict, focus_mode: str) -> dict:
    hour = datetime.now().hour

    urgency = "LOW"

    if "deadline" in message["content"].lower():
        urgency = "HIGH"
    elif hour >= 18:
        urgency = "LOW"

    return {
        "urgency": urgency,
        "focus_mode": focus_mode
    }
