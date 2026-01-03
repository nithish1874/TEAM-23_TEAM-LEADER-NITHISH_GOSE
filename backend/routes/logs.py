from fastapi import APIRouter

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.get("/decisions")
def get_decisions():
    return [
        {
            "message_id": 1,
            "decision": "SHOW",
            "reason": "High priority sender"
        }
    ]
