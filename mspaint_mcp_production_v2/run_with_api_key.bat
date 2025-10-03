@echo off
REM MSPaint MCP Production v2 - Windows Batch Runner
REM Sets up environment and runs the demo

echo ========================================
echo MSPaint MCP Production v2 - Quick Start
echo ========================================

REM Set the Google Gemini API key
set GOOGLE_API_KEY=
set GEMINI_API_KEY=

echo ✅ API Key configured: %GOOGLE_API_KEY:~0,20%...

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

echo ✅ Python is available

REM Install requirements if needed
echo 📦 Installing/checking requirements...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install requirements
    pause
    exit /b 1
)

echo ✅ Requirements installed

REM Run the setup and demo
echo 🚀 Starting MSPaint MCP Demo...
python setup_and_run.py

pause
