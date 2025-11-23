@echo off
REM Activation Script for Car Price Prediction Project (Windows)
REM This script activates the virtual environment for the project

echo 🚗 Car Price Prediction Project - Virtual Environment Setup
echo ==========================================================

REM Check if virtual environment exists
if not exist ".venv" (
    echo ❌ Virtual environment not found!
    echo Creating virtual environment...
    python -m venv .venv
    echo ✅ Virtual environment created!
)

REM Activate the virtual environment
echo 🔧 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Check if requirements are installed
echo 📦 Checking dependencies...
.venv\Scripts\python.exe -c "import pandas, numpy, sklearn, matplotlib" >nul 2>&1
if errorlevel 1 (
    echo 📥 Installing required packages...
    .venv\Scripts\python.exe -m pip install --upgrade pip
    .venv\Scripts\pip.exe install -r requirements-simple.txt
    echo ✅ All dependencies installed!
) else (
    echo ✅ All dependencies are already installed!
)

echo.
echo 🎉 Environment is ready!
echo 📋 Available commands:
echo    python main.py                 - Run the full ML pipeline
echo    python examples\quick_start.py - Run quick example
echo    jupyter notebook               - Start Jupyter for exploration
echo    deactivate                     - Exit virtual environment
echo.
echo 💡 You are now in the virtual environment. Happy coding! 🐍

cmd /k
