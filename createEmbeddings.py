# Import necessary libraries and modules
from langchain.document_loaders import DirectoryLoader  # For loading documents from a directory
from langchain.document_loaders import TextLoader  # For loading text documents
from langchain.text_splitter import RecursiveCharacterTextSplitter  # For splitting text documents into chunks

from dotenv import load_dotenv  # For loading environment variables from a .env file

# Import OpenAI embeddings and FAISS vector store libraries
from langchain.embeddings.openai import OpenAIEmbeddings  # Library for OpenAI language model embeddings
from langchain.vectorstores import FAISS  # Library for vector store

# Load environment variables from .env file
load_dotenv()

# Set optional keyword arguments for the text loader
text_loader_kwargs = {'autodetect_encoding': True}

# Create a DirectoryLoader instance to load documents from a specific directory
# The 'silent_errors' parameter is set to suppress errors during loading, and 'use_multithreading' allows loading multiple documents concurrently.
loader = DirectoryLoader('./langchain_docs_js', glob="**/*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs, silent_errors=True, use_multithreading=True)

# Load the documents using the DirectoryLoader
docs = loader.load()

# Print the number of loaded documents
print(len(docs))

# Create a RecursiveCharacterTextSplitter instance to split large text documents into smaller chunks
# The 'separators' parameter defines the characters that act as separators for splitting the text.
# 'keep_separator' preserves the separators as part of the chunks.
# 'chunk_size' specifies the maximum size of each chunk in characters.
# 'chunk_overlap' controls the overlap between adjacent chunks to avoid splitting sentences.
# 'length_function' defines the function to measure the length of a document (here, it's simply the 'len' function).
text_splitter = RecursiveCharacterTextSplitter(
    separators=["##", "\n\n", "\n", " ", ""],
    keep_separator=True,
    chunk_size=3000,
    chunk_overlap=20,
    length_function=len,
)

# Split the loaded documents into smaller chunks using the RecursiveCharacterTextSplitter
newdocs = text_splitter.split_documents(docs)

# Create an instance of OpenAIEmbeddings, which allows converting text to embeddings
embeddings = OpenAIEmbeddings()

# Create a new FAISS vector store from the split documents and their embeddings
db = FAISS.from_documents(newdocs, embeddings)

# Save the FAISS vector store locally with the given name 'langchain_python_docs_vectorstore'
db.save_local("langchain_js_docs_vectorstore")
