Milvus
======

> [Milvus](https://milvus.io/docs/overview.md) is a database that stores, indexes, and manages massive embedding vectors generated by deep neural networks and other machine learning (ML) models.

This notebook shows how to use functionality related to the Milvus vector database.

To run, you should have a [Milvus instance up and running](https://milvus.io/docs/install_standalone-docker.md).

    pip install pymilvus

We want to use OpenAIEmbeddings so we have to get the OpenAI API Key.

    import osimport getpassos.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

        OpenAI API Key:········

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores import Milvusfrom langchain.document_loaders import TextLoader

    from langchain.document_loaders import TextLoaderloader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()

    vector_db = Milvus.from_documents(    docs,    embeddings,    connection_args={"host": "127.0.0.1", "port": "19530"},)

    query = "What did the president say about Ketanji Brown Jackson"docs = vector_db.similarity_search(query)

    docs[0].page_content

        'Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. \n\nTonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. \n\nOne of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. \n\nAnd I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.'