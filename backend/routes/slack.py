from fastapi import APIRouter, Request

router = APIRouter(prefix="/slack", tags=["Slack"])

@router.post("/events")
async def slack_events(req: Request):
    data = await req.json()

    if "challenge" in data:
        return data["challenge"]

    event = data["event"]
    return {
        "source": "slack",
        "sender": event.get("user"),
        "content": event.get("text")
    }
