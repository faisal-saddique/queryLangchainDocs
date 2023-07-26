from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

load_dotenv()

text_loader_kwargs={'autodetect_encoding': True}

loader = DirectoryLoader('./langchain_docs_python', glob="**/*.md", loader_cls=TextLoader,loader_kwargs=text_loader_kwargs, silent_errors=True, use_multithreading=True)

docs = loader.load()

print(len(docs))

text_splitter = RecursiveCharacterTextSplitter(
    separators=["##","\n\n", "\n", " ", ""],
    keep_separator=True,
    chunk_size = 3000,
    chunk_overlap  = 20,
    length_function = len,
)

newdocs = text_splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()

db = FAISS.from_documents(newdocs, embeddings)

db.save_local("langchain_python_docs_vectorstore")