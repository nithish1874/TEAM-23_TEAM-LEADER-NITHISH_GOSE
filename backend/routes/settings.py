from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/settings", tags=["Settings"])

FOCUS_MODE = {"mode": "NORMAL"}

class FocusMode(BaseModel):
    focus_mode: str

@router.get("")
def get_settings():
    return FOCUS_MODE

@router.post("/focus-mode")
def update_focus_mode(data: FocusMode):
    FOCUS_MODE["mode"] = data.focus_mode
    return FOCUS_MODE
