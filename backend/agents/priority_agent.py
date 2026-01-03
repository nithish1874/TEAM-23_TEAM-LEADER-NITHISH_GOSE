KEYWORDS_HIGH = ["urgent", "asap", "deadline", "immediately"]

def priority_agent(message: dict) -> dict:
    score = 1
    reasoning = []

    content = message["content"].lower()

    if message["sender"].endswith("@company.com"):
        score += 3
        reasoning.append("Internal sender")

    for kw in KEYWORDS_HIGH:
        if kw in content:
            score += 3
            reasoning.append(f"Keyword detected: {kw}")

    score = min(score, 10)

    return {
        "priority_score": score,
        "reasoning": reasoning
    }
