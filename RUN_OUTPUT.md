# Running the Application - Output

## Backend Server Output

When you run the backend server, you should see output like this:

```
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx] using WatchFiles
```

## Testing the Backend

### Health Check
```bash
curl http://localhost:8000/health
```

**Expected Response:**
```json
{"status":"healthy"}
```

### Root Endpoint
```bash
curl http://localhost:8000/
```

**Expected Response:**
```json
{
  "message": "Digital Fatigue Manager API",
  "version": "1.0.0",
  "status": "running"
}
```

### Dashboard API
```bash
curl http://localhost:8000/api/dashboard
```

**Expected Response:**
```json
{
  "total_messages": 5,
  "messages_shown": 2,
  "messages_hidden": 1,
  "messages_postponed": 1,
  "messages_summarized": 1,
  "mental_load_score": 45.5,
  "recent_messages": [...],
  "focus_mode": "normal"
}
```

## Frontend Server Output

When you run the frontend server, you should see output like this:

```
  VITE v6.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

## Browser Output

When you open http://localhost:5173, you should see:
- Login page or Dashboard (depending on routing)
- Navigation sidebar with Dashboard, Settings, Analytics
- Message cards with priority scores
- Focus mode toggle
- Mental load meter

## API Documentation

Visit http://localhost:8000/docs to see:
- Interactive Swagger UI
- All API endpoints
- Request/response schemas
- Try-it-out functionality

