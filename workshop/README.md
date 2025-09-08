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

### Step 4: Create the Chatbot Application
Create `chatbot.py` with the following code:

```python
import streamlit as st
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI

# Hardcoded API key (replace with your actual key)
OPENAI_API_KEY = "your-openai-api-key-here"

# Upload PDF files
st.header("PDF Chatbot - Ask Questions About Your Documents")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

# Extract the text
if file is not None:
    try:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        if not text.strip():
            st.warning("No text could be extracted from the PDF. Please try a different file.")
        else:
            st.success(f"Successfully extracted {len(text)} characters from the PDF.")
            
            # Break it into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                separators="\n",
                chunk_size=1000,
                chunk_overlap=150,
                length_function=len
            )
            chunks = text_splitter.split_text(text)
            
            if chunks:
                # Generate embeddings
                try:
                    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
                    
                    # Create vector store - FAISS
                    vector_store = FAISS.from_texts(chunks, embeddings)
                    
                    # Get user question
                    user_question = st.text_input("Type your question here")
                    
                    # Do similarity search
                    if user_question:
                        try:
                            match = vector_store.similarity_search(user_question)
                            
                            # Define the LLM
                            llm = ChatOpenAI(
                                openai_api_key=OPENAI_API_KEY,
                                temperature=0,
                                max_tokens=1000,
                                model_name="gpt-3.5-turbo"
                            )
                            
                            # Output results
                            chain = load_qa_chain(llm, chain_type="stuff")
                            with st.spinner("Generating response..."):
                                response = chain.run(input_documents=match, question=user_question)
                            
                            st.write("**Answer:**")
                            st.write(response)
                            
                        except Exception as e:
                            st.error(f"Error generating response: {str(e)}")
                            
                except Exception as e:
                    st.error(f"Error creating embeddings: {str(e)}")
            else:
                st.warning("No text chunks could be created from the PDF.")
                
    except Exception as e:
        st.error(f"Error reading PDF file: {str(e)}")
```

### Step 5: Get OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and replace `"your-openai-api-key-here"` in the code

### Step 6: Run the Application
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
