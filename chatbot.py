import streamlit as st
import os
import hashlib
from typing import Optional, List, Dict, Any
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI
from langchain.schema import Document

# Try to load from .env file first
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed, continue without it
    pass

# Helper functions
def get_config_value(key: str, default_value: Any, value_type: type = str) -> Any:
    """Get configuration value from Streamlit secrets or environment variables"""
    try:
        # Try Streamlit secrets first
        value = st.secrets[key]
        if value_type == str:
            return value.strip().strip('"').strip("'")
        return value_type(value)
    except (KeyError, AttributeError, TypeError):
        # Fallback to environment variables
        env_value = os.getenv(key, default_value)
        if value_type == str:
            return env_value
        return value_type(env_value)


def get_file_hash(file_content: bytes) -> str:
    """Generate a hash for file content to use as cache key"""
    return hashlib.md5(file_content).hexdigest()


def extract_text_from_pdf(file) -> str:
    """Extract text from PDF file with error handling"""
    try:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    except Exception as e:
        raise Exception(f"Failed to extract text from PDF: {str(e)}")


def create_text_chunks(text: str, chunk_size: int, chunk_overlap: int, separators: List[str]) -> List[str]:
    """Create text chunks with optimized parameters"""
    text_splitter = RecursiveCharacterTextSplitter(
        separators=separators,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    return text_splitter.split_text(text)


@st.cache_data(ttl=3600)  # Cache for 1 hour
def create_embeddings_and_vectorstore(chunks: List[str], api_key: str) -> FAISS:
    """Create embeddings and vector store with caching"""
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    return FAISS.from_texts(chunks, embeddings)


@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_llm_chain(api_key: str, model: str, temperature: float, max_tokens: int):
    """Create and cache LLM chain"""
    llm = ChatOpenAI(
        openai_api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens,
        model_name=model
    )
    return load_qa_chain(llm, chain_type="stuff")


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



# Main application
def main():
    """Main application function with optimized processing"""
    st.header(APP_TITLE)
    
    with st.sidebar:
        st.title(SIDEBAR_TITLE)
        file = st.file_uploader(FILE_UPLOADER_TEXT, type="pdf")
        
        # Show file info if uploaded
        if file is not None:
            file_size = len(file.getvalue())
            st.info(f"📄 File: {file.name}\n📊 Size: {file_size:,} bytes")
    
    # Process PDF if uploaded
    if file is not None:
        try:
            # Extract text from PDF
            with st.spinner("📖 Extracting text from PDF..."):
                text = extract_text_from_pdf(file)
            
            if not text:
                st.warning("⚠️ No text could be extracted from the PDF. Please try a different file.")
                return
            
            st.success(f"✅ Successfully extracted {len(text):,} characters from the PDF.")
            
            # Create text chunks
            with st.spinner("🔪 Creating text chunks..."):
                chunks = create_text_chunks(text, CHUNK_SIZE, CHUNK_OVERLAP, CHUNK_SEPARATORS)
            
            if not chunks:
                st.warning("⚠️ No text chunks could be created from the PDF.")
                return
            
            st.info(f"📝 Created {len(chunks)} text chunks")
            
            # Create embeddings and vector store (cached)
            with st.spinner("🧠 Creating embeddings and vector store..."):
                vector_store = create_embeddings_and_vectorstore(chunks, OPENAI_API_KEY)
            
            # Get user question
            st.markdown("---")
            user_question = st.text_input(
                QUESTION_INPUT_TEXT,
                placeholder="Ask a question about your document...",
                help="Type your question and press Enter to get an answer"
            )
            
            # Process question if provided
            if user_question:
                try:
                    with st.spinner("🔍 Searching for relevant content..."):
                        # Perform similarity search
                        matches = vector_store.similarity_search(user_question, k=min(4, len(chunks)))
                    
                    if not matches:
                        st.warning("No relevant content found for your question.")
                        return
                    
                    # Get cached LLM chain
                    chain = get_llm_chain(OPENAI_API_KEY, OPENAI_MODEL, OPENAI_TEMPERATURE, OPENAI_MAX_TOKENS)
                    
                    # Generate response
                    with st.spinner("🤖 Generating response..."):
                        response = chain.run(input_documents=matches, question=user_question)
                    
                    # Display response
                    st.markdown("### 💬 Answer:")
                    st.markdown(response)
                    
                    # Show source information
                    with st.expander("📚 Source Information"):
                        for i, match in enumerate(matches, 1):
                            st.text(f"Source {i}: {match.page_content[:200]}...")
                    
                except Exception as e:
                    st.error(f"❌ Error generating response: {str(e)}")
                    st.error("Please try rephrasing your question or check your API key.")
                    
        except Exception as e:
            st.error(f"❌ Error processing PDF: {str(e)}")
            st.error("Please ensure the file is a valid PDF and try again.")


if __name__ == "__main__":
    main()