from fastapi import APIRouter

router = APIRouter(prefix="/gmail", tags=["Gmail"])

@router.get("/messages")
def gmail_messages():
    return [
        {
            "sender": "boss@gmail.com",
            "content": "Urgent meeting at 3 PM"
        }
    ]
