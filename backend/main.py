from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from backend.routes.messages import router as messages_router
from backend.routes.dashboard import router as dashboard_router
from backend.routes.settings import router as settings_router
from backend.routes.logs import router as logs_router

app = FastAPI(
    title="Digital Fatigue Manager API",
    description="Agentic AI to Manage Digital & AI Fatigue",
    version="1.0.0"
)

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Routes
app.include_router(messages_router)
app.include_router(dashboard_router)
app.include_router(settings_router)
app.include_router(logs_router)

@app.get("/")
def root():
    return {"status": "Backend is running"}

# ✅ THIS IS THE MISSING PART
if __name__ == "__main__":
    uvicorn.run(
    "backend.main:app",
    host="127.0.0.1",
    port=8001,
    reload=True
  )
from backend.models.database import init_db

@app.on_event("startup")
def startup():
    init_db()

from backend.routes.slack import router as slack_router
app.include_router(slack_router)
from backend.routes.gmail import router as gmail_router
app.include_router(gmail_router)
