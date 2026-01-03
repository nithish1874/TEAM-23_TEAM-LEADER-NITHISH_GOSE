
def focus_agent(priority_score: int, urgency: str, focus_mode: str) -> dict:
    """
    Decides what to do with a message based on priority,
    urgency, and current focus mode.
    """

    if focus_mode == "DEEP_WORK" and priority_score < 7:
        return {
            "action": "POSTPONE",
            "reason": "User in deep work and priority is low"
        }

    if urgency == "HIGH":
        return {
            "action": "SHOW",
            "reason": "High urgency message"
        }

    return {
        "action": "HIDE",
        "reason": "Low priority and no urgency"
    }
