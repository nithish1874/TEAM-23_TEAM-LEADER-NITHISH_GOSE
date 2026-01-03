"""
Quick test script to verify the backend setup
Run this to test if everything is configured correctly
"""
import sys
sys.path.insert(0, '.')

print("=" * 60)
print("Digital Fatigue Manager - Server Test")
print("=" * 60)
print()

# Test 1: Check imports
print("[1/4] Testing imports...")
try:
    from backend.models.database import init_db, get_db
    from backend.agents.supervisor_agent import SupervisorAgent
    from backend.routes.messages import get_user_settings
    print("OK: All imports successful")
except Exception as e:
    print(f"ERROR: Import error: {e}")
    sys.exit(1)

# Test 2: Check database
print("\n[2/4] Testing database connection...")
try:
    from backend.models.database import SessionLocal, Message
    db = SessionLocal()
    count = db.query(Message).count()
    db.close()
    print(f"OK: Database connected - {count} messages found")
except Exception as e:
    print(f"ERROR: Database error: {e}")
    sys.exit(1)

# Test 3: Test agent system
print("\n[3/4] Testing agent system...")
try:
    test_message = {
        "source": "gmail",
        "sender": "test@example.com",
        "content": "This is a test message with urgent keyword",
        "timestamp": "2024-01-01T10:00:00Z",
        "metadata": {"subject": "Test"},
        "current_focus_mode": "normal"
    }
    supervisor = SupervisorAgent()
    result = supervisor.process(test_message)
    print(f"OK: Agent system working - Decision: {result['final_decision']}")
    print(f"  Priority Score: {result['agent_outputs']['priority']['priority_score']}")
except Exception as e:
    print(f"ERROR: Agent error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 4: Check FastAPI app
print("\n[4/4] Testing FastAPI application...")
try:
    from backend.main import app
    print("OK: FastAPI app loaded successfully")
    print(f"  Available routes: {len(app.routes)} routes registered")
except Exception as e:
    print(f"ERROR: FastAPI error: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("SUCCESS: ALL TESTS PASSED - System is ready to run!")
print("=" * 60)
print("\nTo start the server:")
print("  1. Backend:  cd backend && python main.py")
print("  2. Frontend: cd frontend && npm run dev")
print("\nThen open: http://localhost:5173")
print()

