# PDF Chatbot Project

A Streamlit-based PDF chatbot that uses LangChain and OpenAI to answer questions about uploaded PDF documents.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd PyCharmMiscProject
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up OpenAI API key securely**
   
   **Option A: Environment variable (Recommended for production)**
   ```bash
   export OPENAI_API_KEY='your-actual-api-key-here'
   ```
   
   **Option B: .env file (Recommended for development)**
   ```bash
   # Copy the example file
   cp .env.example .env
   # Edit .env and add your actual API key
   nano .env
   ```
   
   Get your API key from [OpenAI Platform](https://platform.openai.com/)

5. **Set up authentication (Optional)**
   
   **Default credentials:** `admin` / `admin123`
   
   **To change credentials:**
   ```bash
   # Generate new password hash
   python generate_password.py
   
   # Set environment variables
   export APP_USERNAME='your_username'
   export APP_PASSWORD_HASH='your_hashed_password'
   ```

6. **Run the application**
   ```bash
   streamlit run chatbot.py
   ```

7. **Open in browser**
   - The app will open at `http://localhost:8501`

## 📁 Project Structure

```
PyCharmMiscProject/
├── chatbot.py              # Main Streamlit application
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── .gitignore              # Git ignore rules
└── workshop/               # Workshop materials
    ├── chatbot.py          # Workshop version
    ├── requirements.txt    # Workshop dependencies
    └── README.md           # Workshop guide
```

## 🛠️ Features

- **PDF Upload**: Upload PDF files through a user-friendly interface
- **Text Extraction**: Automatically extract text from PDF documents
- **Smart Chunking**: Break documents into optimal chunks for processing
- **Vector Search**: Use FAISS for efficient similarity search
- **AI-Powered Q&A**: Get intelligent answers using OpenAI's GPT models
- **Error Handling**: Comprehensive error handling and user feedback

## 🔧 Dependencies

- `streamlit` - Web application framework
- `PyPDF2` - PDF text extraction
- `langchain` - LLM application framework
- `langchain-openai` - OpenAI integration
- `langchain-community` - Community integrations
- `faiss-cpu` - Vector similarity search
- `openai` - OpenAI API client

## 📚 Workshop Materials

The `workshop/` folder contains complete materials for conducting a workshop:
- Step-by-step setup guide
- Code explanations
- Troubleshooting guide
- Sample documents recommendations

## 🚀 Deployment

### Streamlit Cloud (Recommended - Free & Easy)

**Step-by-Step Deployment:**

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

3. **Deploy your app**
   - Click "New app"
   - Select your repository: `samruddhip/samruddhi-file-QnA`
   - Set main file path: `chatbot.py`
   - Click "Deploy!"

4. **Set your API key**
   - Go to your app's settings
   - Add secret: `OPENAI_API_KEY`
   - Value: `your_actual_api_key_here`
   - Save and restart

5. **Your app is live!** 🎉
   - Share the URL with anyone
   - No technical setup required

### Local Development
```bash
# Set your API key
export OPENAI_API_KEY='your_key_here'

# Run locally
streamlit run chatbot.py
```

### Environment Variables
```bash
# Required
OPENAI_API_KEY=your_actual_api_key_here

# Optional (customize your app)
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0
CHUNK_SIZE=1000
APP_TITLE=PDF Chatbot
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:
1. Check the troubleshooting section in `workshop/README.md`
2. Open an issue on GitHub
3. Check the [Streamlit documentation](https://docs.streamlit.io/)

## ⚙️ Configuration

The application is configurable through environment variables:

**Basic Setup:**
```bash
OPENAI_API_KEY=your_key_here
```

**Custom Model:**
```bash
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.1
CHUNK_SIZE=1500
```

**Custom UI:**
```bash
OPENAI_API_KEY=your_key_here
APP_TITLE=My Custom PDF Assistant
SIDEBAR_TITLE=Document Library
```

## 🔒 Security Features

### ✅ Authentication System
- **Login required** - Users must authenticate before accessing the app
- **Password hashing** - Passwords are hashed using SHA-256
- **Session management** - Secure session handling with logout functionality
- **Configurable credentials** - Set custom usernames and passwords

### ✅ API Key Protection
- **Never hardcoded** - API keys are read from environment variables
- **Git ignored** - `.env` files are automatically excluded from version control
- **Secure by default** - Application stops if no API key is provided

### 🔐 How to Set Up Security

**Default Login Credentials:**
- Username: `admin`
- Password: `admin123`

**Change Default Credentials:**
```bash
# Generate new password hash
python generate_password.py

# Set environment variables
export APP_USERNAME='your_username'
export APP_PASSWORD_HASH='your_hashed_password'
```

**For Streamlit Cloud:**
Add to secrets:
```
# Required
OPENAI_API_KEY = "your_openai_api_key_here"

# Authentication (Optional)
APP_USERNAME = "your_username"
APP_PASSWORD_HASH = "your_hashed_password"

# Optional Configuration
OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_TEMPERATURE = "0"
OPENAI_MAX_TOKENS = "1000"
CHUNK_SIZE = "1000"
CHUNK_OVERLAP = "150"
APP_TITLE = "PDF Chatbot - Ask Questions About Your Documents"
SIDEBAR_TITLE = "Your Documents"
FILE_UPLOADER_TEXT = "Upload a PDF file and start asking questions"
QUESTION_INPUT_TEXT = "Type your question here"
```

### 🛡️ Security Best Practices
- ✅ Change default credentials immediately
- ✅ Use strong passwords
- ✅ Use different credentials for development and production
- ✅ Never share your `.env` file
- ✅ Rotate API keys regularly
- ✅ Monitor API usage in OpenAI dashboard

## 🔗 Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)