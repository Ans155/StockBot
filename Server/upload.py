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
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_website_text(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Failed to fetch URL (status code: {response.status_code})")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'span'])

    text = ' '.join(element.get_text(separator='\n') for element in text_elements)

    return text


def get_pdf_text_from_folder(folder_path):

    text = ""
    for filename in os.listdir(folder_path):

        if filename.endswith(".pdf"):
            filepath = os.path.join(folder_path, filename)
            pdf_reader = PdfReader(filepath)
            for page in pdf_reader.pages:
                text += page.extract_text()

    text = text.replace("\n", "").replace("\t", "")
    return text

def get_text_chunks(text):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):

    embeddings = HuggingFaceInstructEmbeddings( model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

if __name__ == "__main__":

    
    website_url = "https://www.stockgro.club/faq/"
    website_text = get_website_text(website_url)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    website_texts = text_splitter.split_text(website_text)
    get_vector_store(website_texts)
    pdf_folder_path = "pdf"
    pdf_folder_full_path = os.path.join(os.path.dirname(__file__), pdf_folder_path)
    raw_text = get_pdf_text_from_folder(pdf_folder_full_path)
    text_chunks = get_text_chunks(raw_text)
    get_vector_store(text_chunks)

