from fastapi import APIRouter
from pydantic import BaseModel
from backend.models.database import get_db
from backend.agents.priority_agent import priority_agent
from backend.agents.context_agent import context_agent
from backend.agents.focus_agent import focus_agent
from backend.agents.supervisor_agent import supervisor_agent

router = APIRouter(prefix="/messages", tags=["Messages"])

FOCUS_MODE = "NORMAL"

class MessageIn(BaseModel):
    source: str
    sender: str
    content: str

@router.post("/ingest")
def ingest_message(msg: MessageIn):
    message = msg.dict()

    priority = priority_agent(message)
    context = context_agent(message, FOCUS_MODE)
    focus = focus_agent(priority["priority_score"], context["urgency"], FOCUS_MODE)
    decision = supervisor_agent(message, priority["priority_score"], context, focus)

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO messages (source, sender, content, decision, priority) VALUES (?, ?, ?, ?, ?)",
        (msg.source, msg.sender, msg.content, decision["final_decision"], priority["priority_score"])
    )
    db.commit()
    db.close()

    return decision

@router.get("")
def get_messages():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM messages")
    rows = cursor.fetchall()
    db.close()

    return rows
