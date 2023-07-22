PGVector
========

> [PGVector](https://github.com/pgvector/pgvector) is an open-source vector similarity search for `Postgres`

It supports:

*   exact and approximate nearest neighbor search
*   L2 distance, inner product, and cosine distance

This notebook shows how to use the Postgres vector database (`PGVector`).

See the [installation instruction](https://github.com/pgvector/pgvector).

    # Pip install necessary packagepip install pgvectorpip install openaipip install psycopg2-binarypip install tiktoken

        Requirement already satisfied: pgvector in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (0.1.8)    Requirement already satisfied: numpy in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from pgvector) (1.24.3)    Requirement already satisfied: openai in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (0.27.7)    Requirement already satisfied: requests>=2.20 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from openai) (2.28.2)    Requirement already satisfied: tqdm in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from openai) (4.65.0)    Requirement already satisfied: aiohttp in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from openai) (3.8.4)    Requirement already satisfied: charset-normalizer<4,>=2 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from requests>=2.20->openai) (3.1.0)    Requirement already satisfied: idna<4,>=2.5 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from requests>=2.20->openai) (3.4)    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from requests>=2.20->openai) (1.26.15)    Requirement already satisfied: certifi>=2017.4.17 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from requests>=2.20->openai) (2023.5.7)    Requirement already satisfied: attrs>=17.3.0 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (23.1.0)    Requirement already satisfied: multidict<7.0,>=4.5 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (6.0.4)    Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (4.0.2)    Requirement already satisfied: yarl<2.0,>=1.0 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (1.9.2)    Requirement already satisfied: frozenlist>=1.1.1 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (1.3.3)    Requirement already satisfied: aiosignal>=1.1.2 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (1.3.1)    Requirement already satisfied: psycopg2-binary in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (2.9.6)    Requirement already satisfied: tiktoken in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (0.4.0)    Requirement already satisfied: regex>=2022.1.18 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from tiktoken) (2023.5.5)    Requirement already satisfied: requests>=2.26.0 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from tiktoken) (2.28.2)    Requirement already satisfied: charset-normalizer<4,>=2 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from requests>=2.26.0->tiktoken) (3.1.0)    Requirement already satisfied: idna<4,>=2.5 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from requests>=2.26.0->tiktoken) (3.4)    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from requests>=2.26.0->tiktoken) (1.26.15)    Requirement already satisfied: certifi>=2017.4.17 in /Users/joyeed/langchain/langchain/.venv/lib/python3.9/site-packages (from requests>=2.26.0->tiktoken) (2023.5.7)

We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

    import osimport getpassos.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

        OpenAI API Key:········

    ## Loading Environment Variablesfrom typing import List, Tuplefrom dotenv import load_dotenvload_dotenv()

        False

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores.pgvector import PGVectorfrom langchain.document_loaders import TextLoaderfrom langchain.docstore.document import Document

    loader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()

    # PGVector needs the connection string to the database.CONNECTION_STRING = "postgresql+psycopg2://harrisonchase@localhost:5432/test3"# # Alternatively, you can create it from enviornment variables.# import os# CONNECTION_STRING = PGVector.connection_string_from_db_params(#     driver=os.environ.get("PGVECTOR_DRIVER", "psycopg2"),#     host=os.environ.get("PGVECTOR_HOST", "localhost"),#     port=int(os.environ.get("PGVECTOR_PORT", "5432")),#     database=os.environ.get("PGVECTOR_DATABASE", "postgres"),#     user=os.environ.get("PGVECTOR_USER", "postgres"),#     password=os.environ.get("PGVECTOR_PASSWORD", "postgres"),# )

Similarity Search with Euclidean Distance (Default)[​](#similarity-search-with-euclidean-distance-default "Direct link to Similarity Search with Euclidean Distance (Default)")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # The PGVector Module will try to create a table with the name of the collection.# So, make sure that the collection name is unique and the user has the permission to create a table.COLLECTION_NAME = "state_of_the_union_test"db = PGVector.from_documents(    embedding=embeddings,    documents=docs,    collection_name=COLLECTION_NAME,    connection_string=CONNECTION_STRING,)

    query = "What did the president say about Ketanji Brown Jackson"docs_with_score = db.similarity_search_with_score(query)

    for doc, score in docs_with_score:    print("-" * 80)    print("Score: ", score)    print(doc.page_content)    print("-" * 80)

        --------------------------------------------------------------------------------    Score:  0.18460171628856903    Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.         Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.         One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.         And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.    --------------------------------------------------------------------------------    --------------------------------------------------------------------------------    Score:  0.18460171628856903    Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.         Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.         One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.         And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.    --------------------------------------------------------------------------------    --------------------------------------------------------------------------------    Score:  0.18470284560586236    Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.         Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.         One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.         And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.    --------------------------------------------------------------------------------    --------------------------------------------------------------------------------    Score:  0.21730864082247825    A former top litigator in private practice. A former federal public defender. And from a family of public school educators and police officers. A consensus builder. Since she’s been nominated, she’s received a broad range of support—from the Fraternal Order of Police to former judges appointed by Democrats and Republicans.         And if we are to advance liberty and justice, we need to secure the Border and fix the immigration system.         We can do both. At our border, we’ve installed new technology like cutting-edge scanners to better detect drug smuggling.          We’ve set up joint patrols with Mexico and Guatemala to catch more human traffickers.          We’re putting in place dedicated immigration judges so families fleeing persecution and violence can have their cases heard faster.         We’re securing commitments and supporting partners in South and Central America to host more refugees and secure their own borders.    --------------------------------------------------------------------------------

Working with vectorstore[​](#working-with-vectorstore "Direct link to Working with vectorstore")
------------------------------------------------------------------------------------------------

Above, we created a vectorstore from scratch. However, often times we want to work with an existing vectorstore. In order to do that, we can initialize it directly.

    store = PGVector(    collection_name=COLLECTION_NAME,    connection_string=CONNECTION_STRING,    embedding_function=embeddings,)

### Add documents[​](#add-documents "Direct link to Add documents")

We can add documents to the existing vectorstore.

    store.add_documents([Document(page_content="foo")])

        ['048c2e14-1cf3-11ee-8777-e65801318980']

    docs_with_score = db.similarity_search_with_score("foo")

    docs_with_score[0]

        (Document(page_content='foo', metadata={}), 3.3203430005457335e-09)

    docs_with_score[1]

        (Document(page_content='A former top litigator in private practice. A former federal public defender. And from a family of public school educators and police officers. A consensus builder. Since she’s been nominated, she’s received a broad range of support—from the Fraternal Order of Police to former judges appointed by Democrats and Republicans. \n\nAnd if we are to advance liberty and justice, we need to secure the Border and fix the immigration system. \n\nWe can do both. At our border, we’ve installed new technology like cutting-edge scanners to better detect drug smuggling.  \n\nWe’ve set up joint patrols with Mexico and Guatemala to catch more human traffickers.  \n\nWe’re putting in place dedicated immigration judges so families fleeing persecution and violence can have their cases heard faster. \n\nWe’re securing commitments and supporting partners in South and Central America to host more refugees and secure their own borders.', metadata={'source': '../../../state_of_the_union.txt'}),     0.2404395365581814)

### Overriding a vectorstore[​](#overriding-a-vectorstore "Direct link to Overriding a vectorstore")

If you have an existing collection, you override it by doing `from_documents` and setting `pre_delete_collection` = True

    db = PGVector.from_documents(    documents=docs,    embedding=embeddings,    collection_name=COLLECTION_NAME,    connection_string=CONNECTION_STRING,    pre_delete_collection=True,)

    docs_with_score = db.similarity_search_with_score("foo")

    docs_with_score[0]

        (Document(page_content='A former top litigator in private practice. A former federal public defender. And from a family of public school educators and police officers. A consensus builder. Since she’s been nominated, she’s received a broad range of support—from the Fraternal Order of Police to former judges appointed by Democrats and Republicans. \n\nAnd if we are to advance liberty and justice, we need to secure the Border and fix the immigration system. \n\nWe can do both. At our border, we’ve installed new technology like cutting-edge scanners to better detect drug smuggling.  \n\nWe’ve set up joint patrols with Mexico and Guatemala to catch more human traffickers.  \n\nWe’re putting in place dedicated immigration judges so families fleeing persecution and violence can have their cases heard faster. \n\nWe’re securing commitments and supporting partners in South and Central America to host more refugees and secure their own borders.', metadata={'source': '../../../state_of_the_union.txt'}),     0.2404115088144465)

### Using a VectorStore as a Retriever[​](#using-a-vectorstore-as-a-retriever "Direct link to Using a VectorStore as a Retriever")

    retriever = store.as_retriever()

    print(retriever)

        tags=None metadata=None vectorstore=<langchain.vectorstores.pgvector.PGVector object at 0x29f94f880> search_type='similarity' search_kwargs={}