from pprint import pprint
import openai
import tiktoken
from dotenv import load_dotenv
import json
import os
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

embeddings = OpenAIEmbeddings()

db = FAISS.load_local("langchain_python_docs_vectorstore", embeddings)

def get_matching_chunks_from_vecstore(query: str):
    global db
    docs = db.similarity_search(query,k=3)

    context = "\n--------------------------------------\n"
    for doc in docs:
        context += doc.page_content + "\n--------------------------------------\n"

    return context

def create_input_prompt(query: str):
    context = get_matching_chunks_from_vecstore(query=query)
    prompt = f"""Answer the question in your own words as truthfully as possible from the context given to you.\nIf you do not know the answer to the question, simply respond with "I don't know. Can you ask another question".\nIf questions are asked where there is no relevant context available, simply respond with "I don't know. Please ask a question relevant to the documents"\n\nCONTEXT: {context}\n\nHUMAN: {query}\nASSISTANT:"""
    return prompt

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def manage_chat_history(role, content):
    global messages  # Specify that we want to modify the global 'messages' list
    messages.append({"role": f"{role}", "content": f"{content}"})

    chat_history_tokens = num_tokens_from_string(json.dumps(messages))
    print(f"\nChat history consumes {chat_history_tokens} tokens up till now\n")

    if chat_history_tokens >= 3500:
        print("Avoiding token limit hit, removing extra chat messages...")
        # Keep only the system prompt and last 2 messages
        messages = [messages[0]] + messages[-2:]

def get_gpt_response(messages):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0,
    max_tokens=1024
    )

    return response['choices'][0]['message']['content'].strip()

manage_chat_history("system","You are a helpful assistant which answers the user questions based on the provided context.")

while True:
    query = input("Please enter your query: ")
    query = create_input_prompt(query)
    manage_chat_history("user",query)
    response = get_gpt_response(messages=messages)
    print(response)
    manage_chat_history("assistant",response)
    # pprint(f"{messages}")