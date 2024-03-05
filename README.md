# StockBot : Your Personal Investment Assistant

StockBot is an intelligent chatbot designed to provide accurate answers related to stock market queries. Built on the Retrieval Augmented Generation (RAG) structure, StockBot leverages the power of two cutting-edge language models: Gemini Pro and Llama-2-7B. With its vast knowledge base encompassing PDFs and documents, StockBot delivers precise responses to user inquiries, making it an indispensable tool for investors and traders alike.

![image](https://github.com/Ans155/StockBot/assets/110165397/a684fc5b-68a2-4b6d-8764-20bb9095f243)

  
## Features

- **Advanced Models**: StockBot harnesses the capabilities of Gemini Pro and Llama-2-7B models, enabling it to understand complex queries and generate informative responses.
  
- **Knowledge Base**: StockBot's knowledge base comprises PDFs and documents related to the stock market, ensuring comprehensive coverage of relevant information.
  
- **Accurate Embeddings**: By employing the "hkunlp/instructor-lar" embedding model, StockBot delivers accurate storage and contextually relevant answers to user queries.
  
- **Data Management**: Leveraging DataStax as the database solution, StockBot efficiently manages and retrieves information, ensuring smooth operation even with large volumes of data.

- **User-friendly Interface**: StockBot features a sleek and intuitive user interface built using ReactJs and Material UI, providing users with a seamless experience.

- **Backend Processing**: Powered by Python FastAPI, StockBot's backend handles the heavy lifting of processing queries and generating responses, ensuring robust performance.

## Front-end
- HTML, CSS
- JavaScript
- ReactJs
- Material UI

## Back-end
- Python
- FastAPI
- Langchain

## Database
- Datastax AstraDB (Vector Database)
- FAISS

## LLM and Embedding Models 
- TheBloke/Llama-2-7B-chat-GPTQ
- Google Gemini Pro
- hkunlp/instructor-large


## Installation and Set-up for Backend

To deploy StockBot locally, follow these steps:

## Installing Python
Python is required to run StockBot. If you don't have Python installed, follow these steps:

### For Windows:
Download the latest Python installer from the official Python website.
Run the installer and make sure to check the box that says `Add Python to PATH` during installation.

### For macOS:
You can install Python using Homebrew, a package manager for macOS, with the following command in the terminal:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install Python:
```
brew install python
```
## Setting Up a Virtual Environment
It's recommended to use a virtual environment to avoid conflicts with other projects or system-wide Python packages.

### Install the virtualenv package:
First, ensure you have pip installed (it comes with Python if you're using version 3.4 and above).
Install virtualenv by running:
```
pip install virtualenv
```

### Create a Virtual Environment:
Navigate to your project's directory in the terminal.
Run the following command to create a virtual environment named venv (you can name it anything you like):
```
Python -m virtualenv venv
```

### Activate the Virtual Environment:
- On Windows, activate the virtual environment by running:
```
venv\Scripts\activate
```

- On macOS and Linux, activate it with:
```
source venv/bin/activate
```

Once your virtual environment is activated, you'll see its name in the terminal prompt. Now you're ready to use StockBot.

## Installing Required Packages

With the virtual environment activated, you can now install the required packages for StockBot. This is done using the `pip` package manager. Follow these steps:

1. Navigate to the directory containing the `requirements.txt` file in the terminal.
2. Run the following command to install the required packages:

```bash
pip install -r requirements.txt
```
Obtain a Google Gemini API key and create a DataStax AstraDB account. Configure a new database and set DataStax AstraDB token, DataStax AstraDB API endpoint, and Google Gemini API key as environment variables.

## Data Ingestion

To ingest data into StockBot, follow these steps:

1. Navigate to the `server` directory in the terminal.
2. Locate the `upload.py` script.
3. Run the following command to execute the script:

```bash
Python upload.py
```
## Running the FastAPI

To run the FastAPI backend server for StockBot, follow these steps:

1. Navigate to the `server` directory in the terminal.
2. Locate the `test.py` script.
3. Run the following command to start the FastAPI server:

```bash
uvicorn app:test --reload
```
This command will start the FastAPI server, allowing StockBot to process user queries and generate responses.
Once the server is up and running, StockBot is ready to use.

# Installation and Set-up for Frontend

Install dependencies for the client:

```bash
cd client
npm install
```

Start the client :

In the client directory, run npm start to start the React app.
Access the app in your browser at http://localhost:3000.

## Testing the App

To test the functionalities of our app, utilize the provided `.ipynb` files. Open `Bot_using_LLAMA2.ipynb` for StockBot with Llama2 LLM or `Bot_using_GeminiAPI.ipynb` for StockBot with Gemini LLM in Google Colab or any other virtual environment of your choice to experiment with the app.
