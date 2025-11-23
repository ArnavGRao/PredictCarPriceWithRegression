#!/bin/bash

# Activation Script for Car Price Prediction Project
# This script activates the virtual environment for the project

echo "🚗 Car Price Prediction Project - Virtual Environment Setup"
echo "=========================================================="

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "✅ Virtual environment created!"
fi

# Activate the virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Check if requirements are installed
echo "📦 Checking dependencies..."
if ! .venv/bin/python -c "import pandas, numpy, sklearn, matplotlib" 2>/dev/null; then
    echo "📥 Installing required packages..."
    .venv/bin/pip install --upgrade pip
    .venv/bin/pip install -r requirements-simple.txt
    echo "✅ All dependencies installed!"
else
    echo "✅ All dependencies are already installed!"
fi

echo ""
echo "🎉 Environment is ready!"
echo "📋 Available commands:"
echo "   python main.py                 - Run the full ML pipeline"
echo "   python examples/quick_start.py - Run quick example"
echo "   jupyter notebook               - Start Jupyter for exploration"
echo "   deactivate                     - Exit virtual environment"
echo ""
echo "💡 You are now in the virtual environment. Happy coding! 🐍"
