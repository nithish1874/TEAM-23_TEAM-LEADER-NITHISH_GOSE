# Agentic AI to Manage Digital & AI Fatigue - Architecture

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                        FRONTEND (React)                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Dashboard │  │ Settings │  │ Analytics│  │  Login   │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
                            │
                    HTTP/REST API
                            │
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND (FastAPI)                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              API Routes Layer                        │   │
│  │  /ingest  /slack/events  /gmail/messages  /dashboard │   │
│  └─────────────────────────────────────────────────────┘   │
│                            │                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           SUPERVISOR AGENT (Orchestrator)            │   │
│  │  - Combines all agent outputs                        │   │
│  │  - Resolves conflicts                                │   │
│  │  - Makes final decision                              │   │
│  │  - Logs reasoning                                    │   │
│  └─────────────────────────────────────────────────────┘   │
│        │         │         │         │                      │
│  ┌─────▼──┐ ┌───▼───┐ ┌───▼───┐ ┌───▼────┐                │
│  │ INPUT  │ │PRIORITY│ │CONTEXT│ │ FOCUS  │                │
│  │ AGENT  │ │ AGENT  │ │ AGENT │ │ AGENT  │                │
│  └────┬───┘ └────────┘ └───────┘ └────────┘                │
│       │                                                      │
└───────┼──────────────────────────────────────────────────────┘
        │
┌───────┼──────────────────────────────────────────────────────┐
│       │            EXTERNAL APIS                              │
│  ┌────▼────┐         ┌──────────┐                           │
│  │  Gmail  │         │  Slack   │                           │
│  │   API   │         │  Events  │                           │
│  └─────────┘         └──────────┘                           │
└──────────────────────────────────────────────────────────────┘
                            │
                    ┌───────┴────────┐
                    │                │
            ┌───────▼─────┐  ┌──────▼──────┐
            │  Database   │  │   Logging   │
            │  (SQLite)   │  │   System    │
            └─────────────┘  └─────────────┘
```

## Agent Architecture

### 1. INPUT AGENT
**Purpose**: Collect and normalize data from multiple sources

**Inputs**:
- Gmail API messages
- Slack Events API messages

**Outputs**:
```json
{
  "source": "gmail|slack",
  "sender": "josephanand3107gmail.com@example.com",
  "content": "message text",
  "timestamp": "2024-01-01T10:00:00Z",
  "metadata": {
    "subject": "...",
    "thread_id": "...",
    "channel": "..."
  }
}
```

**Responsibilities**:
- OAuth authentication
- API data fetching
- Data normalization
- Error handling

---

### 2. PRIORITY AGENT
**Purpose**: Assign priority scores based on rules

**Inputs**: Normalized message from Input Agent

**Logic**:
- Sender importance (user-defined contacts list)
- Keywords: urgent, deadline, asap, important
- Time-sensitive indicators
- User interaction history

**Outputs**:
```json
{
  "priority_score": 1-10,
  "reasoning": "High priority sender + urgent keyword detected"
}
```

---

### 3. CONTEXT AGENT
**Purpose**: Determine urgency based on temporal context

**Inputs**: Normalized message + current time + user preferences

**Logic**:
- Current time vs working hours
- Deadline proximity
- Day of week
- User's focus mode state
- Message age

**Outputs**:
```json
{
  "urgency_level": "high|medium|low",
  "explanation": "Outside working hours, will wait until morning"
}
```

---

### 4. FOCUS AGENT
**Purpose**: Decide what action to take

**Inputs**: Priority score + Context urgency + Focus mode

**Focus Modes**:
- **Deep Work**: Only critical (priority 9-10)
- **Normal**: Priority 6+ shown immediately
- **Relax**: Only emergency (priority 10)

**Actions**:
- **SHOW**: Display immediately
- **HIDE**: Don't show, save for later
- **POSTPONE**: Schedule for specific time
- **SUMMARIZE**: Add to daily digest

**Outputs**:
```json
{
  "action": "SHOW|HIDE|POSTPONE|SUMMARIZE",
  "justification": "Deep work mode active, priority below threshold"
}
```

---

### 5. SUPERVISOR AGENT
**Purpose**: Orchestrate all agents and make final decision

**Inputs**: All agent outputs

**Logic**:
- Combine agent outputs
- Resolve conflicts (if Priority says high but Context says low)
- Apply business rules
- Calculate confidence score
- Generate comprehensive explanation

**Outputs**:
```json
{
  "final_decision": "SHOW|HIDE|POSTPONE|SUMMARIZE",
  "explanation": "Combined reasoning from all agents",
  "confidence_score": 0.0-1.0,
  "agent_outputs": {
    "priority": {...},
    "context": {...},
    "focus": {...}
  }
}
```

---

## Data Flow

1. **Message Arrives** → Gmail API or Slack Events API
2. **Input Agent** → Normalizes message
3. **Priority Agent** → Assigns score
4. **Context Agent** → Determines urgency
5. **Focus Agent** → Suggests action
6. **Supervisor Agent** → Makes final decision
7. **Decision Logged** → Database + Frontend notification
8. **User Sees Result** → Dashboard updates

## Technology Stack

**Backend**:
- Python 3.10+
- FastAPI
- SQLite (with SQLAlchemy)
- google-auth, google-api-python-client (Gmail)
- slack-sdk (Slack)
- python-dotenv (config)

**Frontend**:
- React 18+
- Vite
- Axios (HTTP client)
- React Router
- Tailwind CSS (styling)
- Recharts (analytics)

**Infrastructure**:
- SQLite for development (easily upgradeable to PostgreSQL)
- File-based logging
- Environment-based configuration

