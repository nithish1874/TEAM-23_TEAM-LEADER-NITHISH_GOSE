# Quick Start Guide

Get up and running with Digital Fatigue Manager in 5 minutes!

## Prerequisites

- Python 3.10+
- Node.js 18+
- Git

## Step 1: Clone & Setup Backend

```bash
# Navigate to project directory
cd "Agentic AI to Manage Digital & AI Fatigue"

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Initialize database
python -c "from backend.models.database import init_db; init_db()"

# (Optional) Load sample data
python sample_data.py
```

## Step 2: Configure Environment

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=dev-secret-key-change-in-production
DATABASE_URL=sqlite:///./fatigue_manager.db
CORS_ORIGINS=http://localhost:5173
LOG_LEVEL=INFO
```

*Note: For Gmail/Slack integration, add API credentials to `.env` (see README.md)*

## Step 3: Run Backend

```bash
cd backend
python main.py
```

Backend will run on `http://localhost:8000`

Verify it's working:
- Visit: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Step 4: Setup & Run Frontend

Open a new terminal:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will run on `http://localhost:5173`

## Step 5: Access the Application

1. Open browser: http://localhost:5173
2. You should see the Login page
3. Navigate to Dashboard to see the interface
4. If you loaded sample data, you'll see example messages

## Testing the API

### Using cURL:

```bash
# Health check
curl http://localhost:8000/health

# Get dashboard data
curl http://localhost:8000/api/dashboard

# Get messages
curl http://localhost:8000/api/messages

# Ingest a test message
curl -X POST http://localhost:8000/api/messages/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "source": "gmail",
    "sender": "test@example.com",
    "content": "This is a test message",
    "metadata": {"subject": "Test"}
  }'
```

### Using the API Docs:

Visit http://localhost:8000/docs for interactive Swagger UI

## Next Steps

1. **Configure Gmail Integration:**
   - Get Gmail API credentials
   - Add to `.env` file
   - Test: `GET /api/gmail/messages?fetch_and_process=true`

2. **Configure Slack Integration:**
   - Create Slack app
   - Add webhook URL: `http://your-domain.com/api/slack/events`
   - Add credentials to `.env`

3. **Customize Settings:**
   - Visit Settings page in frontend
   - Add important contacts
   - Set working hours
   - Configure priority keywords

4. **Explore Features:**
   - Try different focus modes (Deep Work, Normal, Relax)
   - View analytics
   - Check agent decision logs

## Troubleshooting

**Backend won't start:**
- Check Python version: `python --version` (should be 3.10+)
- Verify dependencies: `pip list`
- Check port 8000 is available
- Look at logs in `logs/` directory

**Frontend won't start:**
- Check Node.js version: `node --version` (should be 18+)
- Delete `node_modules` and `package-lock.json`, then `npm install`
- Check port 5173 is available

**API connection errors:**
- Verify backend is running
- Check CORS settings in `.env`
- Verify API URL in browser console

**Database errors:**
- Delete `fatigue_manager.db` and reinitialize
- Check file permissions
- Verify SQLite is available

## Production Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for production deployment instructions.

## Need Help?

- Check [README.md](./README.md) for full documentation
- Review [API_DOCUMENTATION.md](./API_DOCUMENTATION.md) for API details
- See [ARCHITECTURE.md](./ARCHITECTURE.md) for system architecture

---

**Happy filtering! 🚀**

