from fastapi import APIRouter
from backend.models.database import get_db

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("")
def get_dashboard():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM messages")
    total_messages = cursor.fetchone()[0]

    cursor.execute(
        "SELECT id, source, sender, content, decision, priority FROM messages ORDER BY id DESC"
    )
    messages = cursor.fetchall()

    db.close()

    return {
        "total_messages": total_messages,
        "messages": [
            {
                "id": m[0],
                "source": m[1],
                "sender": m[2],
                "content": m[3],
                "decision": m[4],
                "priority": m[5],
            }
            for m in messages
        ],
    }
