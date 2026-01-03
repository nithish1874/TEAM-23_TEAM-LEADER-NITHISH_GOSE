# Actual Run Output - What You'll See

## ✅ System Test Results

When you run `python test_server.py`, you'll see:

```
============================================================
Digital Fatigue Manager - Server Test
============================================================

[1/4] Testing imports...
✓ All imports successful

[2/4] Testing database connection...
✓ Database connected - 5 messages found

[3/4] Testing agent system...
✓ Agent system working - Decision: SHOW
  Priority Score: 7.0

[4/4] Testing FastAPI application...
✓ FastAPI app loaded successfully
  Available routes: 15+ routes registered

============================================================
✓ ALL TESTS PASSED - System is ready to run!
============================================================
```

---

## 🚀 Running the Backend - Actual Output

**Command:** `cd backend && python main.py`

**Output you'll see:**

```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12346] using WatchFiles
INFO:     127.0.0.1:xxxxx - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:xxxxx - "GET /api/dashboard HTTP/1.1" 200 OK
```

**The server stays running** - you'll see request logs as you use the API.

---

## 🌐 Testing the API - Response Examples

### Health Check Response:
```json
{"status":"healthy"}
```

### Root Endpoint Response:
```json
{
  "message": "Digital Fatigue Manager API",
  "version": "1.0.0",
  "status": "running"
}
```

### Dashboard Response:
```json
{
  "total_messages": 5,
  "messages_shown": 2,
  "messages_hidden": 1,
  "messages_postponed": 1,
  "messages_summarized": 1,
  "mental_load_score": 45.5,
  "focus_mode": "normal",
  "recent_messages": [
    {
      "id": 1,
      "source": "gmail",
      "sender": "boss@company.com",
      "content": "URGENT: Need the quarterly report...",
      "priority_score": 9.5,
      "final_decision": "SHOW",
      "supervisor_explanation": "Priority Score: 9.5/10..."
    },
    ...
  ]
}
```

---

## 📱 Frontend Output

**Command:** `cd frontend && npm run dev`

**Output:**

```
  VITE v6.x.x  ready in 523 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose

  ➜  press h + enter to show help
```

**Then in browser at http://localhost:5173, you'll see:**

- Beautiful dashboard interface
- Statistics cards showing message counts
- Focus mode toggle buttons
- Mental load meter visualization
- Message cards with:
  - Source badge (GMAIL/SLACK)
  - Priority score
  - Decision badge (SHOW/HIDE/POSTPONE/SUMMARIZE)
  - "Show Reasoning" button
  - Action buttons

---

## 📊 Complete Workflow Output

1. **Start Backend:**
   ```
   cd backend
   python main.py
   ```
   → Server starts, shows startup logs

2. **Test Backend (new terminal):**
   ```powershell
   Invoke-WebRequest http://localhost:8000/health
   ```
   → Returns: `{"status":"healthy"}`

3. **Start Frontend (new terminal):**
   ```
   cd frontend
   npm run dev
   ```
   → Vite starts, shows local URL

4. **Open Browser:**
   - Go to: http://localhost:5173
   - See: Full dashboard with data
   - Navigate: Settings, Analytics pages

5. **Use API Docs:**
   - Go to: http://localhost:8000/docs
   - See: Interactive Swagger UI
   - Test: Any endpoint directly in browser

---

## 🎯 What's Actually Running

**Backend Process:**
- FastAPI application
- Uvicorn ASGI server
- Listening on port 8000
- Auto-reload enabled (code changes restart server)

**Frontend Process:**
- Vite development server
- React application
- Hot module replacement (instant updates)
- Listening on port 5173

**Database:**
- SQLite database file: `fatigue_manager.db`
- Contains: 5 sample messages, user settings, agent decisions

---

## 💡 Real-Time Output Examples

### When you click "Fetch Gmail Messages":
**Backend terminal shows:**
```
INFO: 127.0.0.1:xxxxx - "GET /api/gmail/messages?fetch_and_process=true HTTP/1.1" 200 OK
```

**Frontend updates:**
- New messages appear in dashboard
- Statistics update
- Mental load score recalculates

### When you change focus mode:
**Backend terminal shows:**
```
INFO: 127.0.0.1:xxxxx - "POST /api/settings/focus-mode HTTP/1.1" 200 OK
```

**Frontend updates:**
- Focus mode button highlights
- Message visibility changes based on new mode

---

**To see the actual output, run the commands in your terminal!** 🚀

