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

4. **Set up OpenAI API key**
   - Get your API key from [OpenAI Platform](https://platform.openai.com/)
   - Replace the API key in `chatbot.py`:
   ```python
   OPENAI_API_KEY = "your-actual-api-key-here"
   ```

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

### Streamlit Cloud
1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Deploy with one click

### Local Deployment
```bash
streamlit run chatbot.py --server.port 8501
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

## 🔗 Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)