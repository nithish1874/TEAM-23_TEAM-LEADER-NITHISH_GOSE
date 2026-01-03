# Complete Setup Guide - Digital Fatigue Manager

## ✅ Project Verified and Ready to Run

The project has been reviewed and all components are in place. Follow these steps to set up and run the application.

---

## 🚀 Quick Setup (3 Steps)

### Step 1: Install Backend Dependencies

Open PowerShell/Command Prompt in the project directory and run:

```powershell
# Make sure you're in the project directory
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue"

# Install Python packages
pip install -r requirements.txt
```

**Expected output:** Packages will be installed (may take 1-2 minutes)

---

### Step 2: Initialize Database

```powershell
# Initialize the database
python -c "import sys; sys.path.insert(0, '.'); from backend.models.database import init_db; init_db(); print('✅ Database initialized!')"

# (Optional) Load sample data for testing
python sample_data.py
```

**Expected output:** 
- `✅ Database initialized!`
- `✅ Sample data created successfully!`

---

### Step 3: Install Frontend Dependencies

```powershell
cd frontend
npm install
cd ..
```

**Expected output:** Node modules will be installed (may take 1-2 minutes)

---

## ▶️ Running the Application

### Terminal 1 - Start Backend Server

```powershell
cd backend
python main.py
```

**You should see:**
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**Backend is now running at:** http://localhost:8000

---

### Terminal 2 - Start Frontend Server

Open a **NEW** terminal/PowerShell window:

```powershell
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\frontend"
npm run dev
```

**You should see:**
```
  VITE v6.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

**Frontend is now running at:** http://localhost:5173

---

## ✅ Verify Everything Works

1. **Test Backend:**
   - Open browser: http://localhost:8000
   - Should see: `{"message":"Digital Fatigue Manager API","version":"1.0.0","status":"running"}`

2. **Test API Docs:**
   - Open: http://localhost:8000/docs
   - Should see interactive Swagger UI with all endpoints

3. **Test Frontend:**
   - Open: http://localhost:5173
   - Should see the application interface (Login/Dashboard page)

---

## 📋 Complete Command List

### One-Time Setup (Run Once)

```powershell
# 1. Navigate to project
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue"

# 2. Install backend dependencies
pip install -r requirements.txt

# 3. Initialize database
python -c "import sys; sys.path.insert(0, '.'); from backend.models.database import init_db; init_db(); print('✅ Database initialized!')"

# 4. Load sample data (optional)
python sample_data.py

# 5. Install frontend dependencies
cd frontend
npm install
cd ..
```

### Running (Every Time)

**Terminal 1:**
```powershell
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\backend"
python main.py
```

**Terminal 2 (New Window):**
```powershell
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\frontend"
npm run dev
```

---

## 🔧 Troubleshooting

### Backend Won't Start

**Problem:** `ModuleNotFoundError: No module named 'backend'`

**Solution:**
```powershell
# Make sure you're in the project root
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue"
cd backend
python main.py
```

**Problem:** Port 8000 already in use

**Solution:** Kill the process using port 8000 or change the port in `backend/main.py`

---

### Frontend Won't Start

**Problem:** `npm: command not found`

**Solution:** Install Node.js from https://nodejs.org/

**Problem:** Module not found errors

**Solution:**
```powershell
cd frontend
rm -r node_modules  # Or: Remove-Item -Recurse -Force node_modules (PowerShell)
npm install
```

---

### Database Errors

**Problem:** Database file errors

**Solution:**
```powershell
# Delete old database and reinitialize
Remove-Item fatigue_manager.db -ErrorAction SilentlyContinue
python -c "import sys; sys.path.insert(0, '.'); from backend.models.database import init_db; init_db()"
python sample_data.py
```

---

## 📁 Project Structure

```
Agentic AI to Manage Digital & AI Fatigue/
├── backend/              # Python FastAPI backend
│   ├── agents/          # AI agents
│   ├── models/          # Database models
│   ├── routes/          # API routes
│   ├── services/        # External services
│   └── main.py          # Entry point
├── frontend/            # React frontend
│   ├── src/
│   └── package.json
├── requirements.txt     # Python dependencies
├── sample_data.py       # Test data generator
└── README.md           # Full documentation
```

---

## 🎯 What You Get

✅ **5 AI Agents** working together  
✅ **Gmail Integration** (OAuth ready)  
✅ **Slack Integration** (Events API ready)  
✅ **Beautiful Dashboard** with analytics  
✅ **Focus Modes** (Deep Work, Normal, Relax)  
✅ **Mental Load Tracking**  
✅ **Full Explainability** - see why each decision was made  
✅ **Production Ready** codebase  

---

## 📚 Next Steps

1. **Explore the Dashboard** at http://localhost:5173
2. **Try Focus Modes** - Switch between Deep Work, Normal, Relax
3. **View Analytics** - See message statistics and charts
4. **Configure Settings** - Add important contacts, set working hours
5. **Test API** - Use http://localhost:8000/docs to test endpoints
6. **Review Documentation** - See README.md for full details

---

## 💡 Tips

- **Keep both terminals open** - Backend and Frontend run separately
- **Check terminal output** - Errors will be displayed there
- **Use API Docs** - http://localhost:8000/docs for testing
- **Sample data included** - Run `python sample_data.py` for test messages

---

**Ready to go! 🚀**

If you encounter any issues, check the error messages in the terminal and refer to the troubleshooting section above.

