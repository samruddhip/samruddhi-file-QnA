#!/bin/bash

# PDF Chatbot Workshop Setup Script
set -e  # Exit on any error

echo "🚀 Setting up PDF Chatbot Workshop Environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $PYTHON_VERSION found, but Python $REQUIRED_VERSION+ is required."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check if virtual environment already exists
if [ -d ".venv" ]; then
    echo "📦 Virtual environment already exists. Removing old one..."
    rm -rf .venv
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Verify installation
echo "🔍 Verifying installation..."
python3 -c "import streamlit, PyPDF2, langchain; print('✅ All dependencies installed successfully')"

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Get your OpenAI API key from https://platform.openai.com/"
echo "2. Set your API key:"
echo "   - For local development: export OPENAI_API_KEY='your-key-here'"
echo "   - Or create a .env file with: OPENAI_API_KEY=your-key-here"
echo "3. Run the app: streamlit run chatbot.py"
echo ""
echo "The app will open at http://localhost:8501"
echo ""
echo "💡 Pro tip: Use 'source .venv/bin/activate' to activate the virtual environment in future sessions"
