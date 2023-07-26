Redis
=====

> [Redis (Remote Dictionary Server)](https://en.wikipedia.org/wiki/Redis) is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability.

This notebook shows how to use functionality related to the [Redis vector database](https://redis.com/solutions/use-cases/vector-database/).

As database either Redis standalone server or Redis Sentinel HA setups are supported for connections with the "redis\_url" parameter. More information about the different formats of the redis connection url can be found in the LangChain [Redis Readme](/docs/integrations/vectorstores/redis) file

Installing[](#installing "Direct link to Installing")
------------------------------------------------------

    pip install redis

We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

    import osimport getpassos.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

Example[](#example "Direct link to Example")
---------------------------------------------

    from langchain.embeddings import OpenAIEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores.redis import Redis

    from langchain.document_loaders import TextLoaderloader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()

If you're not interested in the keys of your entries you can also create your redis instance from the documents.

    rds = Redis.from_documents(    docs, embeddings, redis_url="redis://localhost:6379", index_name="link")

If you're interested in the keys of your entries you have to split your docs in texts and metadatas

    texts = [d.page_content for d in docs]metadatas = [d.metadata for d in docs]rds, keys = Redis.from_texts_return_keys(    texts, embeddings, redis_url="redis://localhost:6379", index_name="link")

    rds.index_name

    query = "What did the president say about Ketanji Brown Jackson"results = rds.similarity_search(query)print(results[0].page_content)

    print(rds.add_texts(["Ankush went to Princeton"]))

    query = "Princeton"results = rds.similarity_search(query)print(results[0].page_content)

    # Load from existing indexrds = Redis.from_existing_index(    embeddings, redis_url="redis://localhost:6379", index_name="link")query = "What did the president say about Ketanji Brown Jackson"results = rds.similarity_search(query)print(results[0].page_content)

Redis as Retriever[](#redis-as-retriever "Direct link to Redis as Retriever")
------------------------------------------------------------------------------

Here we go over different options for using the vector store as a retriever.

There are three different search methods we can use to do retrieval. By default, it will use semantic similarity.

    retriever = rds.as_retriever()

    docs = retriever.get_relevant_documents(query)

We can also use similarity\_limit as a search method. This is only return documents if they are similar enough

    retriever = rds.as_retriever(search_type="similarity_limit")

    # Here we can see it doesn't return any results because there are no relevant documentsretriever.get_relevant_documents("where did ankush go to college?")

Delete keys
===========

To delete your entries you have to address them by their keys.

    Redis.delete(keys, redis_url="redis://localhost:6379")

### Redis connection Url examples[](#redis-connection-url-examples "Direct link to Redis connection Url examples")

Valid Redis Url scheme are:

1.  `redis://` - Connection to Redis standalone, unencrypted
2.  `rediss://` - Connection to Redis standalone, with TLS encryption
3.  `redis+sentinel://` - Connection to Redis server via Redis Sentinel, unencrypted
4.  `rediss+sentinel://` - Connection to Redis server via Redis Sentinel, booth connections with TLS encryption

More information about additional connection parameter can be found in the redis-py documentation at [https://redis-py.readthedocs.io/en/stable/connections.html](https://redis-py.readthedocs.io/en/stable/connections.html)

    # connection to redis standalone at localhost, db 0, no passwordredis_url = "redis://localhost:6379"# connection to host "redis" port 7379 with db 2 and password "secret" (old style authentication scheme without username / pre 6.x)redis_url = "redis://:secret@redis:7379/2"# connection to host redis on default port with user "joe", pass "secret" using redis version 6+ ACLsredis_url = "redis://joe:secret@redis/0"# connection to sentinel at localhost with default group mymaster and db 0, no passwordredis_url = "redis+sentinel://localhost:26379"# connection to sentinel at host redis with default port 26379 and user "joe" with password "secret" with default group mymaster and db 0redis_url = "redis+sentinel://joe:secret@redis"# connection to sentinel, no auth with sentinel monitoring group "zone-1" and database 2redis_url = "redis+sentinel://redis:26379/zone-1/2"# connection to redis standalone at localhost, db 0, no password but with TLS supportredis_url = "rediss://localhost:6379"# connection to redis sentinel at localhost and default port, db 0, no password# but with TLS support for booth Sentinel and Redis serverredis_url = "rediss+sentinel://localhost"