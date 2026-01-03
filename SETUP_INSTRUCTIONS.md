# Complete Setup Instructions

## 🚀 Quick Setup (Recommended)

### Option 1: Using Setup Script (Windows)

1. **Double-click `setup_project.bat`** - This will:
   - Install all Python dependencies
   - Initialize the database
   - Load sample data
   - Install frontend dependencies

2. **Run Backend:**
   - Double-click `run_backend.bat`
   - OR run: `cd backend && python main.py`

3. **Run Frontend (in new terminal):**
   - Double-click `run_frontend.bat`
   - OR run: `cd frontend && npm run dev`

---

## 📝 Manual Setup

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Initialize Database

```bash
python -c "from backend.models.database import init_db; init_db()"
```

### Step 3: (Optional) Load Sample Data

```bash
python sample_data.py
```

### Step 4: Install Frontend Dependencies

```bash
cd frontend
npm install
cd ..
```

---

## ▶️ Running the Application

### Terminal 1 - Backend

```bash
cd backend
python main.py
```

Backend runs on: **http://localhost:8000**
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

### Terminal 2 - Frontend

```bash
cd frontend
npm run dev
```

Frontend runs on: **http://localhost:5173**

---

## ✅ Verify Setup

1. **Check Backend:**
   - Open: http://localhost:8000
   - Should see: `{"message":"Digital Fatigue Manager API","version":"1.0.0","status":"running"}`

2. **Check API Docs:**
   - Open: http://localhost:8000/docs
   - Should see Swagger UI

3. **Check Frontend:**
   - Open: http://localhost:5173
   - Should see the application interface

---

## 🔧 Troubleshooting

### Backend Issues

**Import errors:**
- Make sure you're in the project root when running commands
- Check Python version: `python --version` (need 3.10+)
- Verify packages installed: `pip list | findstr fastapi`

**Database errors:**
- Delete `fatigue_manager.db` and reinitialize
- Run: `python -c "from backend.models.database import init_db; init_db()"`

**Port 8000 in use:**
- Change port in `backend/main.py` line 72
- Or use: `uvicorn backend.main:app --port 8001`

### Frontend Issues

**npm install fails:**
- Delete `frontend/node_modules` and `frontend/package-lock.json`
- Run: `npm install --legacy-peer-deps`

**Port 5173 in use:**
- Vite will automatically use the next available port

**Module not found:**
- Make sure you ran `npm install` in the frontend directory
- Check `frontend/node_modules` exists

---

## 📋 Requirements Checklist

- [ ] Python 3.10+ installed
- [ ] Node.js 18+ installed
- [ ] pip packages installed (`pip install -r requirements.txt`)
- [ ] Database initialized
- [ ] Frontend dependencies installed (`npm install` in frontend/)
- [ ] Backend running on port 8000
- [ ] Frontend running on port 5173

---

## 🎯 Next Steps After Setup

1. **Configure Environment Variables** (optional):
   - Create `.env` file in project root
   - Add Gmail/Slack API credentials (see README.md)

2. **Test the Application:**
   - Visit http://localhost:5173
   - Navigate to Dashboard
   - Try changing focus modes
   - View analytics

3. **Explore Features:**
   - Settings page - configure preferences
   - Analytics page - view statistics
   - Test message ingestion via API

---

## 📚 Additional Resources

- **Full Documentation**: See README.md
- **API Reference**: See API_DOCUMENTATION.md
- **Architecture**: See ARCHITECTURE.md
- **Deployment**: See DEPLOYMENT.md

---

**Need Help?** Check the troubleshooting section or review the error messages in the terminal.

