#!/bin/bash

# AI Career Recommender - Unix/Linux/Mac Quick Start Script

echo ""
echo "================================================================================"
echo "     AI Career Recommender System - Quick Start"
echo "================================================================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.9+ from https://www.python.org/"
    echo ""
    exit 1
fi

echo "[1/4] Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "       Python $PYTHON_VERSION detected ✓"
echo ""

echo "[2/4] Installing backend dependencies..."
cd backend
pip3 install -r requirements.txt --quiet
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "       Dependencies installed ✓"
cd ..
echo ""

echo "[3/4] Starting backend server..."
echo "       Backend will start on http://127.0.0.1:8000"
echo "       Press Ctrl+C to stop the server"
echo ""

# Start backend in background
cd backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000 &
BACKEND_PID=$!
cd ..

sleep 3

echo "[4/4] Opening frontend in browser..."
sleep 2

# Open browser (works on macOS and Linux)
if [[ "$OSTYPE" == "darwin"* ]]; then
    open index.html
else
    xdg-open index.html 2>/dev/null || firefox index.html 2>/dev/null || google-chrome index.html 2>/dev/null
fi

echo ""
echo "================================================================================"
echo "     ✓ System Started Successfully!"
echo "================================================================================"
echo ""
echo "   Frontend:  Open index.html in your browser"
echo "   Backend:   http://127.0.0.1:8000"
echo "   API Docs:  Read API_DOCS.md for endpoint documentation"
echo ""
echo "   To test:"
echo "   1. Enter skills: 'Python, Machine Learning'"
echo "   2. Click 'Get Recommendation'"
echo "   3. View results with missing skills and tasks"
echo ""
echo "   Troubleshooting:"
echo "   - If backend doesn't start, ensure port 8000 is available"
echo "   - Check that Python 3.9+ is installed"
echo "   - Review DEPLOYMENT.md for detailed setup"
echo ""
echo "================================================================================"
echo ""

# Wait for backend process
wait $BACKEND_PID
