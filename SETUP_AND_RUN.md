# 🚀 Complete Setup and Run Instructions

## ✅ Project Verified - Ready to Run!

I've reviewed your project structure. Everything is in place. Follow these steps:

---

## 📝 STEP 1: Install Backend Dependencies

Open PowerShell in the project directory and run:

```powershell
pip install -r requirements.txt
```

**Wait for installation to complete** (takes 1-2 minutes)

---

## 📝 STEP 2: Initialize Database

```powershell
python -c "import sys; sys.path.insert(0, '.'); from backend.models.database import init_db; init_db(); print('Database initialized!')"
```

**Expected:** `Database initialized!`

---

## 📝 STEP 3: (Optional) Load Sample Data

```powershell
python sample_data.py
```

**Expected:** `SUCCESS: Sample data created successfully!`

---

## 📝 STEP 4: Install Frontend Dependencies

```powershell
cd frontend
npm install
cd ..
```

**Wait for installation to complete** (takes 1-2 minutes)

---

## ▶️ RUNNING THE APPLICATION

### 🖥️ Terminal 1 - Backend

```powershell
cd backend
python main.py
```

**You should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**✅ Backend running at:** http://localhost:8000

---

### 🖥️ Terminal 2 - Frontend (NEW WINDOW)

Open a **NEW PowerShell window**:

```powershell
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\frontend"
npm run dev
```

**You should see:**
```
  VITE v6.x.x  ready in xxx ms
  ➜  Local:   http://localhost:5173/
```

**✅ Frontend running at:** http://localhost:5173

---

## ✅ Verify It Works

1. **Open browser:** http://localhost:5173
2. **You should see:** The Digital Fatigue Manager interface
3. **Check API:** http://localhost:8000/docs (should show API documentation)

---

## 🔧 If Something Goes Wrong

### Backend won't start?
- Make sure you're in `backend` folder: `cd backend`
- Check Python: `python --version` (need 3.10+)
- Try: `python -m uvicorn backend.main:app --reload`

### Frontend won't start?
- Make sure you ran `npm install` in the `frontend` folder
- Check Node.js: `node --version` (need 18+)
- Delete `node_modules` and reinstall: `npm install`

### Database errors?
- Delete `fatigue_manager.db` and run Step 2 again

---

## 📋 Complete Command Checklist

**One-time setup:**
- [ ] `pip install -r requirements.txt`
- [ ] `python -c "import sys; sys.path.insert(0, '.'); from backend.models.database import init_db; init_db()"`
- [ ] `python sample_data.py` (optional)
- [ ] `cd frontend && npm install`

**Every time you run:**
- [ ] Terminal 1: `cd backend && python main.py`
- [ ] Terminal 2: `cd frontend && npm run dev`

---

**That's it! You're ready to go! 🎉**

