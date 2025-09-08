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

5. **Run the application**
   ```bash
   streamlit run chatbot.py
   ```

6. **Open in browser**
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

### Quick Deploy Options

**1. Streamlit Cloud (Recommended - Free)**
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repository and set environment variables
4. Deploy!

**2. Docker (Production Ready)**
```bash
# Build and run
docker build -t pdf-chatbot .
docker run -p 8501:8501 -e OPENAI_API_KEY=your_key_here pdf-chatbot

# Or use docker-compose
docker-compose up --build
```

**3. Local Development**
```bash
streamlit run chatbot.py --server.port 8501
```

### Environment Variables for Deployment
```bash
# Required
OPENAI_API_KEY=your_actual_api_key_here

# Optional
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0
CHUNK_SIZE=1000
APP_TITLE=PDF Chatbot
```

📖 **See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment guide**

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

### ✅ API Key Protection
- **Never hardcoded** - API keys are read from environment variables
- **Git ignored** - `.env` files are automatically excluded from version control
- **Secure by default** - Application stops if no API key is provided

### 🔐 How to Set API Key Securely

**Development (using .env file):**
```bash
# 1. Copy example file
cp .env.example .env

# 2. Edit with your actual key
nano .env

# 3. Run the app
streamlit run chatbot.py
```

**Production (using environment variables):**
```bash
# Set environment variable
export OPENAI_API_KEY='sk-your-actual-key-here'

# Run the app
streamlit run chatbot.py
```

### 🛡️ Security Best Practices
- ✅ Use different API keys for development and production
- ✅ Never share your `.env` file
- ✅ Rotate API keys regularly
- ✅ Monitor API usage in OpenAI dashboard

## 🔗 Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)