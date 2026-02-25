@echo off
REM AI Career Recommender - Windows Quick Start Script

setlocal enabledelayedexpansion

echo.
echo ================================================================================
echo     AI Career Recommender System - Quick Start
echo ================================================================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org/
    echo.
    pause
    exit /b 1
)

echo [1/4] Checking Python version...
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo        Python %PYTHON_VERSION% detected ✓
echo.

echo [2/4] Installing backend dependencies...
cd backend
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo        Dependencies installed ✓
cd ..
echo.

echo [3/4] Starting backend server...
echo        Backend will start on http://127.0.0.1:8000
echo        Press Ctrl+C to stop the server
echo.
start cmd /k "cd backend && uvicorn main:app --reload --host 127.0.0.1 --port 8000"
timeout /t 3 >nul

echo [4/4] Opening frontend in browser...
timeout /t 2 >nul
start index.html

echo.
echo ================================================================================
echo     ✓ System Started Successfully!
echo ================================================================================
echo.
echo   Frontend:  Open index.html in your browser
echo   Backend:   http://127.0.0.1:8000
echo   API Docs:  Read API_DOCS.md for endpoint documentation
echo.
echo   To test:
echo   1. Enter skills: "Python, Machine Learning"
echo   2. Click "Get Recommendation"
echo   3. View results with missing skills and tasks
echo.
echo   Troubleshooting:
echo   - If backend doesn't start, ensure port 8000 is available
echo   - Check that Python 3.9+ is installed
echo   - Review DEPLOYMENT.md for detailed setup
echo.
echo ================================================================================
echo.

endlocal
