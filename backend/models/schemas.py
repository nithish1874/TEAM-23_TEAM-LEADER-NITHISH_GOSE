"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class Source(str, Enum):
    GMAIL = "gmail"
    SLACK = "slack"


class UrgencyLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Action(str, Enum):
    SHOW = "SHOW"
    HIDE = "HIDE"
    POSTPONE = "POSTPONE"
    SUMMARIZE = "SUMMARIZE"


class FocusMode(str, Enum):
    DEEP_WORK = "deep_work"
    NORMAL = "normal"
    RELAX = "relax"


# Input Agent Schemas
class NormalizedMessage(BaseModel):
    source: str
    sender: str
    content: str
    timestamp: datetime
    metadata: Dict[str, Any] = {}


# Priority Agent Schemas
class PriorityOutput(BaseModel):
    priority_score: float  # 1-10
    reasoning: str


# Context Agent Schemas
class ContextOutput(BaseModel):
    urgency_level: str  # "high", "medium", "low"
    explanation: str


# Focus Agent Schemas
class FocusOutput(BaseModel):
    action: str  # "SHOW", "HIDE", "POSTPONE", "SUMMARIZE"
    justification: str


# Supervisor Agent Schemas
class SupervisorOutput(BaseModel):
    final_decision: str
    explanation: str
    confidence_score: float  # 0.0-1.0
    agent_outputs: Dict[str, Any]


# API Request/Response Schemas
class IngestRequest(BaseModel):
    source: str
    sender: str
    content: str
    metadata: Dict[str, Any] = {}


class MessageResponse(BaseModel):
    id: int
    source: str
    sender: str
    content: str
    timestamp: datetime
    priority_score: Optional[float]
    urgency_level: Optional[str]
    final_decision: Optional[str]
    confidence_score: Optional[float]
    supervisor_explanation: Optional[str]
    shown_to_user: bool
    
    class Config:
        from_attributes = True


class DashboardResponse(BaseModel):
    total_messages: int
    messages_shown: int
    messages_hidden: int
    messages_postponed: int
    messages_summarized: int
    mental_load_score: Optional[float]
    recent_messages: List[MessageResponse]
    focus_mode: str


class FocusModeRequest(BaseModel):
    focus_mode: FocusMode


class UserSettingsResponse(BaseModel):
    current_focus_mode: str
    working_hours_start: str
    working_hours_end: str
    working_days: str
    important_contacts: List[str]
    priority_keywords: List[str]
    notification_enabled: bool
    daily_summary_enabled: bool
    
    class Config:
        from_attributes = True

