import streamlit as st
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI

# Hardcoded API key (replace with your actual key)
OPENAI_API_KEY = "api-key-here"


#Upload PDF files
st.header("My first Chatbot")


with  st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader(" Upload a PDf file and start asking questions", type="pdf")


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