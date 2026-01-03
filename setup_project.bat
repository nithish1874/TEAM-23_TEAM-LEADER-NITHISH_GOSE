@echo off
echo ========================================
echo Digital Fatigue Manager - Setup Script
echo ========================================
echo.

echo [1/4] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install Python dependencies
    pause
    exit /b 1
)

echo.
echo [2/4] Initializing database...
python -c "from backend.models.database import init_db; init_db()"
if errorlevel 1 (
    echo ERROR: Failed to initialize database
    pause
    exit /b 1
)

echo.
echo [3/4] Loading sample data...
python sample_data.py
if errorlevel 1 (
    echo WARNING: Failed to load sample data (this is optional)
)

echo.
echo [4/4] Installing frontend dependencies...
cd frontend
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install frontend dependencies
    cd ..
    pause
    exit /b 1
)
cd ..

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the application:
echo   1. Backend:   cd backend ^&^& python main.py
echo   2. Frontend:  cd frontend ^&^& npm run dev
echo.
pause

