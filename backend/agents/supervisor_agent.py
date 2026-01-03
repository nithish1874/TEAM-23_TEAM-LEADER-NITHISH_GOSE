def supervisor_agent(message, priority, context, focus):
    return {
        "final_decision": focus["action"],
        "confidence": round(priority / 10, 2),
        "explanation": {
            "priority": priority,
            "context": context,
            "decision": focus["action"]
        }
    }
