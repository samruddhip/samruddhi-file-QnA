#!/usr/bin/env python3
"""
Environment Setup Script for PDF Chatbot
This script helps you set up your OpenAI API key securely.
"""

import os
import sys
from pathlib import Path

def get_config_value(prompt, default, value_type=str):
    """Get configuration value from user with default"""
    while True:
        user_input = input(f"{prompt} (default: {default}): ").strip()
        if not user_input:
            return default
        
        try:
            return value_type(user_input)
        except ValueError:
            print(f"❌ Invalid input. Please enter a valid {value_type.__name__}.")
            continue

def create_env_file():
    """Create .env file from user input"""
    print("🔧 PDF Chatbot Configuration Setup")
    print("=" * 50)
    print("Get your API key from: https://platform.openai.com/api-keys")
    print()
    
    # Get API key from user
    api_key = input("Enter your OpenAI API key: ").strip()
    
    if not api_key:
        print("❌ No API key provided. Exiting.")
        return False
    
    if not api_key.startswith('sk-'):
        print("⚠️  Warning: API key doesn't start with 'sk-'. Please verify it's correct.")
        confirm = input("Continue anyway? (y/N): ").strip().lower()
        if confirm != 'y':
            return False
    
    print("\n📝 Optional Configuration (press Enter for defaults):")
    print("-" * 50)
    
    # Get optional configurations
    model = get_config_value("OpenAI Model", "gpt-3.5-turbo")
    temperature = get_config_value("Temperature (0-1)", "0", float)
    max_tokens = get_config_value("Max Tokens", "1000", int)
    chunk_size = get_config_value("Chunk Size", "1000", int)
    chunk_overlap = get_config_value("Chunk Overlap", "150", int)
    app_title = get_config_value("App Title", "PDF Chatbot - Ask Questions About Your Documents")
    
    # Create .env file
    env_content = f"""# OpenAI API Configuration
OPENAI_API_KEY={api_key}

# OpenAI Model Configuration
OPENAI_MODEL={model}
OPENAI_TEMPERATURE={temperature}
OPENAI_MAX_TOKENS={max_tokens}

# Text Processing Configuration
CHUNK_SIZE={chunk_size}
CHUNK_OVERLAP={chunk_overlap}
CHUNK_SEPARATORS=\\n

# UI Configuration
APP_TITLE={app_title}
SIDEBAR_TITLE=Your Documents
FILE_UPLOADER_TEXT=Upload a PDF file and start asking questions
QUESTION_INPUT_TEXT=Type your question here

# Advanced Configuration (Optional)
# OPENAI_BASE_URL=https://api.openai.com/v1
# OPENAI_ORGANIZATION=your-org-id
# STREAMLIT_SERVER_PORT=8501
# STREAMLIT_SERVER_ADDRESS=localhost
"""
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ .env file created successfully!")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def check_env_file():
    """Check if .env file exists and has valid content"""
    env_file = Path('.env')
    if not env_file.exists():
        return False
    
    try:
        with open('.env', 'r') as f:
            content = f.read()
            return 'OPENAI_API_KEY=' in content and 'your_openai_api_key_here' not in content
    except:
        return False

def main():
    print("🚀 PDF Chatbot Environment Setup")
    print("=" * 40)
    
    # Check if .env already exists
    if check_env_file():
        print("✅ .env file already exists with API key!")
        print("You can run the chatbot with: streamlit run chatbot.py")
        return
    
    # Create .env file
    if create_env_file():
        print()
        print("🎉 Setup complete!")
        print("You can now run the chatbot with: streamlit run chatbot.py")
        print()
        print("📝 Note: The .env file is ignored by git for security.")
        print("   Never commit your actual API key to version control!")
    else:
        print("❌ Setup failed. Please try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
