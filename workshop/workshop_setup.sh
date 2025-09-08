#!/bin/bash

# PDF Chatbot Workshop Setup Script
echo "🚀 Setting up PDF Chatbot Workshop Environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install requirements
echo "📚 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Get your OpenAI API key from https://platform.openai.com/"
echo "2. Replace 'your-openai-api-key-here' in chatbot.py with your actual key"
echo "3. Run: streamlit run chatbot.py"
echo ""
echo "The app will open at http://localhost:8501"
