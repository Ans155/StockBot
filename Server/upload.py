import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceInstructEmbeddings
import requests
from bs4 import BeautifulSoup

from langchain.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import AstraDB
from langchain_core.output_parsers import StrOutputParser
load_dotenv()     
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
astra_db_application_token=os.getenv("astra_db_application_token")
astra_db_api_endpoint=os.getenv("astra_db_api_endpoint")
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_pdf_text_from_folder(folder_path):
    loader = PyPDFDirectoryLoader(folder_path)
    docs = loader.load()
    return docs
    

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
    texts = text_splitter.split_documents(text)
    return texts

def get_vector_store(text_chunks):

    #embeddings = HuggingFaceInstructEmbeddings( model_name="sentence-transformers/all-MiniLM-L6-v2")
    embeddings = HuggingFaceInstructEmbeddings( model_name="hkunlp/instructor-large")
    vstore = AstraDB(
        embedding=embeddings,
        collection_name="pdfdata",
        token=astra_db_application_token,
        api_endpoint=astra_db_api_endpoint
    )
    vstore.add_documents(text_chunks)
    # vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    # vector_store.save_local("faiss_index")

if __name__ == "__main__":
    # loader = WebBaseLoader("https://www.stockgro.club/faq/")
    # data = loader.load()
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
    # website_texts = text_splitter.split_documents(data)
    # get_vector_store(website_texts)
    pdf_folder_path = "pdf"
    pdf_folder_full_path = os.path.join(os.path.dirname(__file__), pdf_folder_path)
    raw_text = get_pdf_text_from_folder(pdf_folder_full_path)
    text_chunks = get_text_chunks(raw_text)
    get_vector_store(text_chunks)

