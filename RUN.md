# How to Run the Application

## Quick Run Instructions

### Option 1: Run Backend Only

**Terminal 1 - Backend:**
```bash
# 1. Install dependencies (first time only)
pip install -r requirements.txt

# 2. Initialize database (first time only)
python -c "from backend.models.database import init_db; init_db()"

# 3. Run backend
cd backend
python main.py
```

Backend runs on: **http://localhost:8000**
API Docs: **http://localhost:8000/docs**

---

### Option 2: Run Both Backend + Frontend

**Terminal 1 - Backend:**
```bash
# Navigate to project root
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue"

# Install Python dependencies (first time only)
pip install -r requirements.txt

# Initialize database (first time only)
python -c "from backend.models.database import init_db; init_db()"

# (Optional) Load sample data
python sample_data.py

# Run backend
cd backend
python main.py
```

**Terminal 2 - Frontend (Open a NEW terminal):**
```bash
# Navigate to project root
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\frontend"

# Install dependencies (first time only)
npm install

# Run frontend
npm run dev
```

Frontend runs on: **http://localhost:5173**

---

## Step-by-Step for First Time Setup

### 1. Setup Backend (One-time setup)

```bash
# Navigate to project directory
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue"

# Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate

# Install Python packages
pip install -r requirements.txt

# Initialize database
python -c "from backend.models.database import init_db; init_db()"

# (Optional) Add sample data
python sample_data.py
```

### 2. Run Backend

```bash
cd backend
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### 3. Setup Frontend (One-time setup - in NEW terminal)

```bash
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\frontend"
npm install
```

### 4. Run Frontend (in the same terminal as step 3)

```bash
npm run dev
```

You should see:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

---

## Verify It's Working

1. **Backend**: Open browser to http://localhost:8000
   - Should see: `{"message":"Digital Fatigue Manager API","version":"1.0.0","status":"running"}`

2. **API Docs**: Open http://localhost:8000/docs
   - Should see Swagger UI with all API endpoints

3. **Frontend**: Open browser to http://localhost:5173
   - Should see the Login/Dashboard page

---

## Common Commands

### Backend Commands
```bash
# Run backend
cd backend && python main.py

# Run with uvicorn directly
uvicorn backend.main:app --reload

# Initialize database
python -c "from backend.models.database import init_db; init_db()"

# Load sample data
python sample_data.py
```

### Frontend Commands
```bash
# Run frontend
cd frontend && npm run dev

# Build for production
cd frontend && npm run build

# Preview production build
cd frontend && npm run preview
```

---

## Troubleshooting

**Backend issues:**
- If port 8000 is busy: Change port in `backend/main.py` or use `uvicorn backend.main:app --port 8001`
- If imports fail: Make sure you're in the project root when running commands
- If database errors: Delete `fatigue_manager.db` and reinitialize

**Frontend issues:**
- If port 5173 is busy: Vite will auto-assign a new port
- If npm install fails: Try `npm install --legacy-peer-deps`
- If build fails: Delete `node_modules` and `package-lock.json`, then `npm install`

---

## Using Windows PowerShell

All commands work the same in PowerShell. Just make sure you're in the correct directory:

```powershell
# Navigate to project
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue"

# Run backend
cd backend
python main.py

# In another PowerShell window for frontend:
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\frontend"
npm install
npm run dev
```

