Question answering over a group chat messages using Activeloop's DeepLake
=========================================================================

In this tutorial, we are going to use Langchain + Activeloop's Deep Lake with GPT4 to semantically search and ask questions over a group chat.

View a working demo [here](https://twitter.com/thisissukh_/status/1647223328363679745)

1\. Install required packages[](#1-install-required-packages "Direct link to 1. Install required packages")
------------------------------------------------------------------------------------------------------------

    python3 -m pip install --upgrade langchain 'deeplake[enterprise]' openai tiktoken

2\. Add API keys[](#2-add-api-keys "Direct link to 2. Add API keys")
---------------------------------------------------------------------

    import osimport getpassfrom langchain.document_loaders import PyPDFLoader, TextLoaderfrom langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import (    RecursiveCharacterTextSplitter,    CharacterTextSplitter,)from langchain.vectorstores import DeepLakefrom langchain.chains import ConversationalRetrievalChain, RetrievalQAfrom langchain.chat_models import ChatOpenAIfrom langchain.llms import OpenAIos.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")activeloop_token = getpass.getpass("Activeloop Token:")os.environ["ACTIVELOOP_TOKEN"] = activeloop_tokenos.environ["ACTIVELOOP_ORG"] = getpass.getpass("Activeloop Org:")org_id = os.environ["ACTIVELOOP_ORG"]embeddings = OpenAIEmbeddings()dataset_path = "hub://" + org_id + "/data"

2\. Create sample data[](#2-create-sample-data "Direct link to 2. Create sample data")
---------------------------------------------------------------------------------------

You can generate a sample group chat conversation using ChatGPT with this prompt:

    Generate a group chat conversation with three friends talking about their day, referencing real places and fictional names. Make it funny and as detailed as possible.

I've already generated such a chat in `messages.txt`. We can keep it simple and use this for our example.

3\. Ingest chat embeddings[](#3-ingest-chat-embeddings "Direct link to 3. Ingest chat embeddings")
---------------------------------------------------------------------------------------------------

We load the messages in the text file, chunk and upload to ActiveLoop Vector store.

    with open("messages.txt") as f:    state_of_the_union = f.read()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)pages = text_splitter.split_text(state_of_the_union)text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)texts = text_splitter.create_documents(pages)print(texts)dataset_path = "hub://" + org + "/data"embeddings = OpenAIEmbeddings()db = DeepLake.from_documents(    texts, embeddings, dataset_path=dataset_path, overwrite=True)

`Optional`: You can also use Deep Lake's Managed Tensor Database as a hosting service and run queries there. In order to do so, it is necessary to specify the runtime parameter as {'tensor\_db': True} during the creation of the vector store. This configuration enables the execution of queries on the Managed Tensor Database, rather than on the client side. It should be noted that this functionality is not applicable to datasets stored locally or in-memory. In the event that a vector store has already been created outside of the Managed Tensor Database, it is possible to transfer it to the Managed Tensor Database by following the prescribed steps.

    # with open("messages.txt") as f:#     state_of_the_union = f.read()# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)# pages = text_splitter.split_text(state_of_the_union)# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)# texts = text_splitter.create_documents(pages)# print(texts)# dataset_path = "hub://" + org + "/data"# embeddings = OpenAIEmbeddings()# db = DeepLake.from_documents(#     texts, embeddings, dataset_path=dataset_path, overwrite=True, runtime="tensor_db"# )

4\. Ask questions[](#4-ask-questions "Direct link to 4. Ask questions")
------------------------------------------------------------------------

Now we can ask a question and get an answer back with a semantic search:

    db = DeepLake(dataset_path=dataset_path, read_only=True, embedding_function=embeddings)retriever = db.as_retriever()retriever.search_kwargs["distance_metric"] = "cos"retriever.search_kwargs["k"] = 4qa = RetrievalQA.from_chain_type(    llm=OpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=False)# What was the restaurant the group was talking about called?query = input("Enter query:")# The Hungry Lobsterans = qa({"query": query})print(ans)