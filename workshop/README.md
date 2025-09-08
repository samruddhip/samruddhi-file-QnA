# PDF Chatbot Workshop - Complete Setup Guide

## Workshop Overview
Build a PDF chatbot using Streamlit, LangChain, and OpenAI that can answer questions about uploaded PDF documents.

## Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Basic knowledge of Python

## Step-by-Step Installation Guide

### Step 1: Create Project Directory
```bash
mkdir pdf-chatbot-workshop
cd pdf-chatbot-workshop
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

### Step 3: Install Dependencies
Create a `requirements.txt` file:
```txt
streamlit
PyPDF2
langchain
langchain-openai
langchain-community
faiss-cpu
openai
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Step 4: Get OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and replace `"your-openai-api-key-here"` in the code

### Step 5: Run the Application
```bash
streamlit run chatbot.py
```

The app will open in your browser at `http://localhost:8501`

## Workshop Activities

### Activity 1: Basic Setup (15 minutes)
- Set up the project structure
- Install dependencies
- Run the basic app

### Activity 2: Understanding the Code (20 minutes)
- Explain each component:
  - PDF text extraction
  - Text chunking
  - Embeddings
  - Vector store
  - Question answering chain

### Activity 3: Testing the App (15 minutes)
- Upload a sample PDF
- Ask questions about the content
- Test different types of questions

### Activity 4: Customization (20 minutes)
- Modify chunk size and overlap
- Change the LLM model
- Add error handling improvements
- Customize the UI

### Activity 5: Advanced Features (20 minutes)
- Add support for multiple PDFs
- Implement conversation history
- Add file type validation
- Create a better UI layout

## Troubleshooting Common Issues

### Issue 1: ModuleNotFoundError
```bash
# Solution: Install missing packages
pip install langchain-openai
```

### Issue 2: API Key Error
- Ensure your OpenAI API key is correct
- Check if you have sufficient credits

### Issue 3: PDF Reading Error
- Try with a different PDF file
- Ensure the PDF contains extractable text

### Issue 4: Memory Issues
- Reduce chunk size
- Use smaller PDF files for testing

## Workshop Materials Needed

### For Instructor:
- Laptop with Python installed
- OpenAI API key
- Sample PDF files for testing
- Projector/screen for demonstration

### For Participants:
- Laptops with Python installed
- OpenAI API key (can use instructor's for demo)
- Sample PDF files

## Sample PDFs for Testing
- Research papers
- Technical documentation
- News articles
- User manuals

## Next Steps After Workshop
1. Deploy to Streamlit Cloud
2. Add authentication
3. Support for more file types
4. Database integration
5. User management

## Resources
- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [FAISS Documentation](https://faiss.ai/)

## Workshop Duration
- Total: 90 minutes
- Setup: 15 minutes
- Coding: 45 minutes
- Testing: 15 minutes
- Q&A: 15 minutes

## Prerequisites Check
Before starting, ensure participants have:
- [ ] Python 3.8+ installed
- [ ] Basic Python knowledge
- [ ] Text editor/IDE ready
- [ ] Internet connection
- [ ] OpenAI account (or access to API key)
