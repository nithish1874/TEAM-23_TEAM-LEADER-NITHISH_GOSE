# API Documentation

Digital Fatigue Manager API - Complete API Reference

Base URL: `http://localhost:8000/api`

## Authentication

Currently, the API does not require authentication for development. In production, implement JWT or OAuth authentication.

## Messages API

### Ingest Message

Process a new message through the agent system.

**Endpoint:** `POST /messages/ingest`

**Request Body:**
```json
{
  "source": "gmail" | "slack",
  "sender": "user@example.com",
  "content": "Message content here",
  "metadata": {
    "subject": "Email subject (optional)",
    "channel": "channel-id (for Slack)",
    "thread_id": "thread-id (optional)"
  }
}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "source": "gmail",
  "sender": "user@example.com",
  "content": "Message content here",
  "timestamp": "2024-01-01T10:00:00Z",
  "priority_score": 7.5,
  "urgency_level": "high",
  "final_decision": "SHOW",
  "confidence_score": 0.85,
  "supervisor_explanation": "Priority Score: 7.5/10 (Important sender + urgent keyword detected) | Urgency: HIGH (Recent message (< 1 hour)) | Suggested Action: SHOW (Priority 7.5 meets normal mode threshold (6.0)) | Final Decision: SHOW",
  "shown_to_user": true
}
```

### Get Messages

Retrieve messages with optional filters.

**Endpoint:** `GET /messages`

**Query Parameters:**
- `limit` (optional, default: 50): Number of messages to return
- `source` (optional): Filter by source ("gmail" | "slack")
- `decision` (optional): Filter by decision ("SHOW" | "HIDE" | "POSTPONE" | "SUMMARIZE")

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "source": "gmail",
    "sender": "user@example.com",
    "content": "Message content",
    "timestamp": "2024-01-01T10:00:00Z",
    "priority_score": 7.5,
    "urgency_level": "high",
    "final_decision": "SHOW",
    "confidence_score": 0.85,
    "supervisor_explanation": "...",
    "shown_to_user": true
  }
]
```

### Get Message by ID

**Endpoint:** `GET /messages/{message_id}`

**Response:** `200 OK` (same as single message object)

### Interact with Message

Record user interaction with a message.

**Endpoint:** `POST /messages/{message_id}/interact?action={action}`

**Query Parameters:**
- `action`: "dismissed" | "responded" | "archived"

**Response:** `200 OK`
```json
{
  "status": "success",
  "message": "Action 'responded' recorded"
}
```

## Gmail API

### Get Gmail Messages

Fetch messages from Gmail (optionally process through agents).

**Endpoint:** `GET /gmail/messages`

**Query Parameters:**
- `max_results` (optional, default: 10): Maximum number of messages to fetch
- `fetch_and_process` (optional, default: false): If true, fetch from Gmail API and process through agents

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "source": "gmail",
    "sender": "sender@example.com",
    "content": "Email content",
    "timestamp": "2024-01-01T10:00:00Z",
    "priority_score": 7.5,
    "urgency_level": "high",
    "final_decision": "SHOW",
    "confidence_score": 0.85,
    "supervisor_explanation": "...",
    "shown_to_user": true
  }
]
```

### Get Gmail Auth Status

Check Gmail authentication status.

**Endpoint:** `GET /gmail/auth/status`

**Response:** `200 OK`
```json
{
  "authenticated": true,
  "status": "connected"
}
```

## Slack API

### Slack Events Webhook

Handle Slack Events API webhook.

**Endpoint:** `POST /slack/events`

**Headers:**
- `X-Slack-Signature`: Slack request signature
- `X-Slack-Request-Timestamp`: Request timestamp

**Request Body:** (Slack Events API format)
```json
{
  "type": "event_callback",
  "event": {
    "type": "message",
    "user": "U123456",
    "text": "Message text",
    "channel": "C123456",
    "ts": "1234567890.123456"
  }
}
```

**Response:** `200 OK`
```json
{
  "status": "processed",
  "message_id": 1
}
```

## Dashboard API

### Get Dashboard Data

Get dashboard statistics and recent messages.

**Endpoint:** `GET /dashboard`

**Response:** `200 OK`
```json
{
  "total_messages": 42,
  "messages_shown": 15,
  "messages_hidden": 20,
  "messages_postponed": 5,
  "messages_summarized": 2,
  "mental_load_score": 45.5,
  "recent_messages": [...],
  "focus_mode": "normal"
}
```

## Settings API

### Get Settings

Get user settings.

**Endpoint:** `GET /settings`

**Response:** `200 OK`
```json
{
  "current_focus_mode": "normal",
  "working_hours_start": "09:00",
  "working_hours_end": "17:00",
  "working_days": "mon,tue,wed,thu,fri",
  "important_contacts": ["boss@company.com", "team@company.com"],
  "priority_keywords": ["urgent", "deadline", "asap", "important"],
  "notification_enabled": true,
  "daily_summary_enabled": true
}
```

### Update Focus Mode

Update current focus mode.

**Endpoint:** `POST /settings/focus-mode`

**Request Body:**
```json
{
  "focus_mode": "deep_work" | "normal" | "relax"
}
```

**Response:** `200 OK`
```json
{
  "status": "success",
  "focus_mode": "deep_work"
}
```

### Update Settings

Update user settings.

**Endpoint:** `PUT /settings`

**Request Body:** (all fields optional)
```json
{
  "working_hours_start": "09:00",
  "working_hours_end": "17:00",
  "working_days": "mon,tue,wed,thu,fri",
  "important_contacts": ["email1@example.com"],
  "priority_keywords": ["urgent", "deadline"],
  "notification_enabled": true,
  "daily_summary_enabled": true,
  "summary_time": "18:00"
}
```

**Response:** `200 OK` (same format as GET /settings)

## Logs API

### Get Agent Decisions

Get agent decision logs.

**Endpoint:** `GET /logs/decisions`

**Query Parameters:**
- `message_id` (optional): Filter by message ID
- `limit` (optional, default: 50): Number of logs to return

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "message_id": 1,
    "input_agent_output": {...},
    "priority_agent_output": {
      "priority_score": 7.5,
      "reasoning": "Important sender + urgent keyword detected"
    },
    "context_agent_output": {
      "urgency_level": "high",
      "explanation": "Recent message (< 1 hour)"
    },
    "focus_agent_output": {
      "action": "SHOW",
      "justification": "Priority 7.5 meets normal mode threshold (6.0)"
    },
    "supervisor_agent_output": {...},
    "created_at": "2024-01-01T10:00:00Z"
  }
]
```

### Get Agent Decision by ID

**Endpoint:** `GET /logs/decisions/{decision_id}`

**Response:** `200 OK` (same as single decision object)

### Get Message Reasoning

Get full reasoning for a message decision.

**Endpoint:** `GET /logs/messages/{message_id}/reasoning`

**Response:** `200 OK`
```json
{
  "message_id": 1,
  "priority_score": 7.5,
  "priority_reasoning": "Important sender + urgent keyword detected",
  "urgency_level": "high",
  "context_explanation": "Recent message (< 1 hour)",
  "action": "SHOW",
  "focus_justification": "Priority 7.5 meets normal mode threshold (6.0)",
  "final_decision": "SHOW",
  "supervisor_explanation": "...",
  "confidence_score": 0.85,
  "full_decision_log": {...}
}
```

## Error Responses

All endpoints may return error responses:

**400 Bad Request**
```json
{
  "detail": "Error message"
}
```

**404 Not Found**
```json
{
  "detail": "Resource not found"
}
```

**500 Internal Server Error**
```json
{
  "detail": "Internal server error"
}
```

## Rate Limiting

Currently no rate limiting. In production, implement rate limiting (e.g., 100 requests/minute per IP).

## CORS

CORS is enabled for development. Configure `CORS_ORIGINS` in environment variables for production.

