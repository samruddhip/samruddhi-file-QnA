import streamlit as st
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI

# Try to load from .env file first
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed, continue without it
    pass

# Configuration - All values can be set via environment variables
# Try to get API key from environment variables first, then from Streamlit secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# If not found in environment, try Streamlit secrets (for Streamlit Cloud)
if not OPENAI_API_KEY:
    try:
        OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    except:
        pass

# Clean up the API key (remove quotes if present)
if OPENAI_API_KEY:
    OPENAI_API_KEY = OPENAI_API_KEY.strip().strip('"').strip("'")

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0"))
OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "1000"))

# Text processing configuration
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "150"))
CHUNK_SEPARATORS = os.getenv("CHUNK_SEPARATORS", "\\n").split(",")

# UI Configuration
APP_TITLE = os.getenv("APP_TITLE", "PDF Chatbot - Ask Questions About Your Documents")
SIDEBAR_TITLE = os.getenv("SIDEBAR_TITLE", "Your Documents")
FILE_UPLOADER_TEXT = os.getenv("FILE_UPLOADER_TEXT", "Upload a PDF file and start asking questions")
QUESTION_INPUT_TEXT = os.getenv("QUESTION_INPUT_TEXT", "Type your question here")

# Check if API key is provided
if not OPENAI_API_KEY:
    st.error("⚠️ OpenAI API key not found!")
    st.markdown("""
    **Please set your OpenAI API key:**
    
    **For Streamlit Cloud:**
    1. Go to your app's Settings → Secrets
    2. Add: `OPENAI_API_KEY = "your-key-here"`
    3. Save and restart the app
    
    **For Local Development:**
    ```bash
    export OPENAI_API_KEY='your-key-here'
    # or create .env file
    ```
    """)
    st.stop()

# Upload PDF files
st.header(APP_TITLE)

with st.sidebar:
    st.title(SIDEBAR_TITLE)
    file = st.file_uploader(FILE_UPLOADER_TEXT, type="pdf")

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
                separators=CHUNK_SEPARATORS,
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
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
                    user_question = st.text_input(QUESTION_INPUT_TEXT)
                    
                    # Do similarity search
                    if user_question:
                        try:
                            match = vector_store.similarity_search(user_question)
                            
                            # Define the LLM
                            llm = ChatOpenAI(
                                openai_api_key=OPENAI_API_KEY,
                                temperature=OPENAI_TEMPERATURE,
                                max_tokens=OPENAI_MAX_TOKENS,
                                model_name=OPENAI_MODEL
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