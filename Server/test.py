from fastapi import FastAPI
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
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.memory import (
    ChatMessageHistory,
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryBufferMemory,
    VectorStoreRetrieverMemory,
)
from langchain.chains import ConversationChain
from langchain_community.vectorstores import AstraDB
from langchain_core.output_parsers import StrOutputParser
load_dotenv()     
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
astra_db_application_token=os.getenv("astra_db_application_token")
astra_db_api_endpoint=os.getenv("astra_db_api_endpoint")
memory = ConversationBufferWindowMemory(memory_key="chat_history", input_key="human_input",k=3)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str
def get_pdf_text_from_folder(folder_path):
    text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            filepath = os.path.join(folder_path, filename)
            pdf_reader = PdfReader(filepath)
            for page in pdf_reader.pages:
                text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings( model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details. If the answer is not available in the provided context just try to answer without context but keeping chat_history in mind. Try add two Logical follow up questions in next line that can be asked by the user at the end of generated answer with the heading "Want to know more?, ask these follow up questions :"\n\n
    Current conversation:
    {chat_history}
    Context:\n {context}?\n 
    Question: \n{human_input}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.8)

    prompt = PromptTemplate(template=prompt_template, input_variables=["chat_history","context", "human_input"])
    # conversation = ConversationChain(
    #     prompt=prompt,
    #     llm=model,
    #     verbose=True,
    #     memory=ConversationBufferMemory(ai_prefix="Agent"),
    # )
    # parser = StrOutputParser()
    # chain = prompt | model | parser
    chain = load_qa_chain(model, chain_type="stuff",memory=memory,prompt=prompt)
    return chain

def user_input(user_question):
    #embeddings = HuggingFaceInstructEmbeddings( model_name="sentence-transformers/all-MiniLM-L6-v2")
    embeddings = HuggingFaceInstructEmbeddings( model_name="hkunlp/instructor-large")
    vstore = AstraDB(
        embedding=embeddings,
        collection_name="pdfdata",
        token=astra_db_application_token,
        api_endpoint=astra_db_api_endpoint
    )
    # new_db = FAISS.load_local("faiss_index", embeddings)
    # docs = new_db.similarity_search(user_question)
    relevant_docs = vstore.similarity_search(user_question, astra_db_application_token="AstraCS:caMHvgsIrkHpjTCAoyhRnsRK:945bdbb46d23f616e73a5a3675bcbfa6353152446500bec0e2ab1185119736f3", search_kwargs={"k": 2})

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details. If the answer is not available in the provided context just try to answer without context but keeping chat_history in mind. Try add two Logical follow up questions in next line that can be asked by the user at the end of generated answer with the heading "Want to know more?, ask these follow up questions :"\n\n
    Current conversation:
    {chat_history}
    Context:\n {context}?\n 
    Question: \n{human_input}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.8)
    chain =get_conversational_chain()

    response = chain({"input_documents": relevant_docs, "human_input": user_question}, return_only_outputs=True)


   # print(chain.memory.buffer)
    return response['output_text']

@app.options("/answer/")
async def options_answer():
    return {"method": "OPTIONS"}
@app.post("/answer/")
async def get_answer(request: QuestionRequest):
    question = request.question
    answer=user_input(question)
    print(answer)
    return {"answer": answer}
