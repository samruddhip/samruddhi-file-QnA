import streamlit as st
import os
import hashlib
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
    pass

# Helper functions
def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def get_config_value(key, default_value, value_type=str):
    """Get configuration value from Streamlit secrets or environment variables"""
    try:
        value = st.secrets[key]
        if value_type == str:
            return value.strip().strip('"').strip("'")
        return value_type(value)
    except:
        env_value = os.getenv(key, default_value)
        if value_type == str:
            return env_value
        return value_type(env_value)

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None

# Authentication functions
def check_credentials(username, password):
    """Check if username and password are correct using Streamlit secrets"""
    try:
        # Get credentials from Streamlit secrets
        config_username = st.secrets["APP_USERNAME"]
        config_password_hash = st.secrets["APP_PASSWORD_HASH"]
        
        # Compare username and hashed password
        return username == config_username and hash_password(password) == config_password_hash
    except:
        # If secrets are not available, show error
        st.error("⚠️ Authentication configuration not found. Please check your Streamlit secrets.")
        return False

def login_page():
    """Display login page"""
    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.title("🔐 PDF Chatbot")
        st.markdown("### Please login to access the PDF Chatbot")
        
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            
            login_button = st.form_submit_button("🚀 Login", use_container_width=True)
            
            if login_button:
                if check_credentials(username, password):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.success("✅ Login successful!")
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password!")

def logout():
    """Logout user"""
    st.session_state.authenticated = False
    st.session_state.username = None
    st.rerun()

# Check authentication - show login page if not authenticated
if not st.session_state.authenticated:
    login_page()
    st.stop()


# OpenAI Configuration
OPENAI_API_KEY = get_config_value("OPENAI_API_KEY", None, str)
OPENAI_MODEL = get_config_value("OPENAI_MODEL", "gpt-3.5-turbo", str)
OPENAI_TEMPERATURE = get_config_value("OPENAI_TEMPERATURE", "0", float)
OPENAI_MAX_TOKENS = get_config_value("OPENAI_MAX_TOKENS", "1000", int)

# Text processing configuration
CHUNK_SIZE = get_config_value("CHUNK_SIZE", "1000", int)
CHUNK_OVERLAP = get_config_value("CHUNK_OVERLAP", "150", int)
CHUNK_SEPARATORS = get_config_value("CHUNK_SEPARATORS", "\\n", str).split(",")

# UI Configuration
APP_TITLE = get_config_value("APP_TITLE", "PDF Chatbot - Ask Questions About Your Documents", str)
SIDEBAR_TITLE = get_config_value("SIDEBAR_TITLE", "Your Documents", str)
FILE_UPLOADER_TEXT = get_config_value("FILE_UPLOADER_TEXT", "Upload a PDF file and start asking questions", str)
QUESTION_INPUT_TEXT = get_config_value("QUESTION_INPUT_TEXT", "Type your question here", str)

# Authentication Configuration
APP_USERNAME = get_config_value("APP_USERNAME", "admin", str)
APP_PASSWORD_HASH = get_config_value("APP_PASSWORD_HASH", hash_password("admin123"), str)

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



# Main application (only shown if authenticated)
# Add user info and logout in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown(f"👤 **Logged in as:** {st.session_state.get('username', 'admin')}")
if st.sidebar.button("🚪 Logout", use_container_width=True):
    logout()
st.sidebar.markdown("---")

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