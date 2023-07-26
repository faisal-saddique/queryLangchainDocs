# Import necessary libraries
from pprint import pprint  # For pretty-printing data structures
import openai  # OpenAI API client library
import tiktoken  # Tokenization library for counting tokens in a text
from dotenv import load_dotenv  # For loading environment variables from a .env file
import json  # For working with JSON data
import os  # For interacting with the operating system
from langchain.vectorstores import FAISS  # Library for vector search
from langchain.embeddings.openai import OpenAIEmbeddings  # Library for OpenAI language model embeddings

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key using the loaded environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize an empty list to store the conversation messages
messages = []

# Create an instance of OpenAIEmbeddings, which allows converting text to embeddings
embeddings = OpenAIEmbeddings()

# Load the vector store from the local storage using FAISS
# The vector store is used to search for relevant documents based on query embeddings
db = FAISS.load_local("langchain_python_docs_vectorstore", embeddings)

# Function to retrieve matching chunks from the vector store for a given query
def get_matching_chunks_from_vecstore(query: str):
    global db
    # Perform similarity search in the vector store and get the top 3 most similar documents
    docs = db.similarity_search(query, k=3)

    # Prepare a formatted string with the content of each document
    context = "\n--------------------------------------\n"
    for doc in docs:
        context += doc.page_content + "\n--------------------------------------\n"

    return context

# Function to create an input prompt for the chat with the AI assistant
def create_input_prompt(query: str):
    # Get the relevant context based on the query from the vector store
    context = get_matching_chunks_from_vecstore(query=query)

    # Combine the context and query to form the input prompt for the AI assistant
    prompt = f"""Answer the question in your own words as truthfully as possible from the context given to you.\nIf you do not know the answer to the question, simply respond with "I don't know. Can you ask another question".\nIf questions are asked where there is no relevant context available, simply respond with "I don't know. Please ask a question relevant to the documents"\n\nCONTEXT: {context}\n\nHUMAN: {query}\nASSISTANT:"""

    return prompt

# Function to count the number of tokens in a text string
def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# Function to manage chat history by adding messages and handling token limits
def manage_chat_history(role, content):
    global messages  # Specify that we want to modify the global 'messages' list
    messages.append({"role": f"{role}", "content": f"{content}"})

    # Count the number of tokens used in the chat history
    chat_history_tokens = num_tokens_from_string(json.dumps(messages))
    print(f"\nChat history consumes {chat_history_tokens} tokens up till now\n")

    # Check if the token limit (3500 tokens) is about to be hit, if yes, remove extra messages
    if chat_history_tokens >= 3500:
        print("Avoiding token limit hit, removing extra chat messages...")
        # Keep only the system prompt and last 2 messages to reduce token usage
        messages = [messages[0]] + messages[-2:]

# Function to get the AI assistant's response using OpenAI's ChatCompletion API
def get_gpt_response(messages):
    # Make a request to the GPT-3.5 Turbo model to get the response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=1024
    )

    # Extract and return the content of the AI assistant's response
    return response['choices'][0]['message']['content'].strip()

# Start the conversation by introducing the AI assistant
manage_chat_history("system", "You are a helpful assistant which answers the user questions based on the provided context.")

# Enter an infinite loop to interact with the AI assistant
while True:
    # Get user input (query) and create an input prompt for the AI assistant
    query = input("Please enter your query: ")
    query = create_input_prompt(query)
    
    # Add user's query to the chat history
    manage_chat_history("user", query)
    
    # Get the AI assistant's response
    response = get_gpt_response(messages=messages)
    
    # Print and display the AI assistant's response
    print(response)
    
    # Add AI assistant's response to the chat history
    manage_chat_history("assistant", response)

# Note: The code is designed to run indefinitely, so it will keep accepting and responding to queries from the user.
# It ensures the conversation history doesn't exceed the token limit, preventing potential issues with API calls.
# The 'messages' list is used to keep track of the conversation, which includes both user and AI assistant messages.
