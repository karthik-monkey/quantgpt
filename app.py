# Import os to set API key
import os
import openai
# Import OpenAI as main LLM service

import streamlit as st
from langchain.llms import OpenAI
# Bring in streamlit for UI/app interface
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
# Import PDF document loaders...there's other ones as well!

from langchain.agents.agent_toolkits import (
# Import chroma as the vector store 
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
# Import vector store stuff
)

# Set API key for OpenAI
os.environ['OPENAI_API_KEY'] = 'insert-api-key-here'

# Initialize OpenAI LLM
llm = OpenAI(temperature=0.1, verbose=True)
# Set APIkey for OpenAI Service

# Create embeddings instance
embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])

# Load the PDF
loader = PyPDFLoader('annualreport.pdf')
pages = loader.load_and_split()

# Use persist_directory to store vector data locally
persist_directory = 'chroma_storage'
# Split pages from pdf 

# Create Chroma vectorstore with local persistence
# Load documents into vector database aka ChromaDB
store = Chroma.from_documents(
    documents=pages, 
    embedding=embeddings, 
# Create vectorstore info object - metadata repo?
    collection_name='annualreport', 
    persist_directory=persist_directory
)

# Create vectorstore info object
vectorstore_info = VectorStoreInfo(
# Convert the document store into a langchain toolkit
    name='annualreport',
    description='A banking annual report as PDF',
    vectorstore=store
# Add the toolkit to an end-to-end LC
)

# Create a toolkit from the vectorstore info and include the LLM (llm) here
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info, llm=llm)

# Create the LangChain agent
agent_executor = create_vectorstore_agent(
# Create a text input box for the user
    llm=llm,
    toolkit=toolkit,
    verbose=True
# If the user hits enter
)

# Streamlit app UI
st.title('🦜🔗 GPT Investment Banker')
    # ...and write it out to the screen
prompt = st.text_input('Type your prompt here!')

if prompt:
    # Run the agent on the provided prompt
    response = agent_executor.run(prompt)
        # Find the relevant pages
    st.write(response)

    # Display document similarity search results
    with st.expander('Document Similarity Search'):
