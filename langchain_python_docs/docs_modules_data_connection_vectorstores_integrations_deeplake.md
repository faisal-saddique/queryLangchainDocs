Activeloop's Deep Lake
======================

> [Activeloop's Deep Lake](https://docs.activeloop.ai/) as a Multi-Modal Vector Store that stores embeddings and their metadata including text, jsons, images, audio, video, and more. It saves the data locally, in your cloud, or on Activeloop storage. It performs hybrid search including embeddings and their attributes.

This notebook showcases basic functionality related to `Activeloop's Deep Lake`. While `Deep Lake` can store embeddings, it is capable of storing any type of data. It is a serverless data lake with version control, query engine and streaming dataloaders to deep learning frameworks.

For more information, please see the Deep Lake [documentation](https://docs.activeloop.ai) or [api reference](https://docs.deeplake.ai)

    pip install openai 'deeplake[enterprise]' tiktoken

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores import DeepLake

    import osimport getpassos.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")activeloop_token = getpass.getpass("activeloop token:")embeddings = OpenAIEmbeddings()

    from langchain.document_loaders import TextLoaderloader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()

Create a dataset locally at `./deeplake/`, then run similarity search. The Deeplake+LangChain integration uses Deep Lake datasets under the hood, so `dataset` and `vector store` are used interchangeably. To create a dataset in your own cloud, or in the Deep Lake storage, [adjust the path accordingly](https://docs.activeloop.ai/storage-and-credentials/storage-options).

    db = DeepLake(    dataset_path="./my_deeplake/", embedding_function=embeddings, overwrite=True)db.add_documents(docs)# or shorter# db = DeepLake.from_documents(docs, dataset_path="./my_deeplake/", embedding=embeddings, overwrite=True)query = "What did the president say about Ketanji Brown Jackson"docs = db.similarity_search(query)

    print(docs[0].page_content)

Later, you can reload the dataset without recomputing embeddings

    db = DeepLake(    dataset_path="./my_deeplake/", embedding_function=embeddings, read_only=True)docs = db.similarity_search(query)

Deep Lake, for now, is single writer and multiple reader. Setting `read_only=True` helps to avoid acquiring the writer lock.

### Retrieval Question/Answering[​](#retrieval-questionanswering "Direct link to Retrieval Question/Answering")

    from langchain.chains import RetrievalQAfrom langchain.llms import OpenAIChatqa = RetrievalQA.from_chain_type(    llm=OpenAIChat(model="gpt-3.5-turbo"),    chain_type="stuff",    retriever=db.as_retriever(),)

    query = "What did the president say about Ketanji Brown Jackson"qa.run(query)

### Attribute based filtering in metadata[​](#attribute-based-filtering-in-metadata "Direct link to Attribute based filtering in metadata")

Let's create another vector store containing metadata with the year the documents were created.

    import randomfor d in docs:    d.metadata["year"] = random.randint(2012, 2014)db = DeepLake.from_documents(    docs, embeddings, dataset_path="./my_deeplake/", overwrite=True)

    db.similarity_search(    "What did the president say about Ketanji Brown Jackson",    filter={"metadata": {"year": 2013}},)

### Choosing distance function[​](#choosing-distance-function "Direct link to Choosing distance function")

Distance function `L2` for Euclidean, `L1` for Nuclear, `Max` l-infinity distance, `cos` for cosine similarity, `dot` for dot product

    db.similarity_search(    "What did the president say about Ketanji Brown Jackson?", distance_metric="cos")

### Maximal Marginal relevance[​](#maximal-marginal-relevance "Direct link to Maximal Marginal relevance")

Using maximal marginal relevance

    db.max_marginal_relevance_search(    "What did the president say about Ketanji Brown Jackson?")

### Delete dataset[​](#delete-dataset "Direct link to Delete dataset")

    db.delete_dataset()

        

and if delete fails you can also force delete

    DeepLake.force_delete_by_path("./my_deeplake")

        

Deep Lake datasets on cloud (Activeloop, AWS, GCS, etc.) or in memory[​](#deep-lake-datasets-on-cloud-activeloop-aws-gcs-etc-or-in-memory "Direct link to Deep Lake datasets on cloud (Activeloop, AWS, GCS, etc.) or in memory")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, Deep Lake datasets are stored locally. To store them in memory, in the Deep Lake Managed DB, or in any object storage, you can provide the [corresponding path and credentials when creating the vector store](https://docs.activeloop.ai/storage-and-credentials/storage-options). Some paths require registration with Activeloop and creation of an API token that can be [retrieved here](https://app.activeloop.ai/)

    os.environ["ACTIVELOOP_TOKEN"] = activeloop_token

    # Embed and store the textsusername = "<username>"  # your username on app.activeloop.aidataset_path = f"hub://{username}/langchain_testing_python"  # could be also ./local/path (much faster locally), s3://bucket/path/to/dataset, gcs://path/to/dataset, etc.docs = text_splitter.split_documents(documents)embedding = OpenAIEmbeddings()db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings, overwrite=True)db.add_documents(docs)

    query = "What did the president say about Ketanji Brown Jackson"docs = db.similarity_search(query)print(docs[0].page_content)

#### `tensor_db` execution option[​](#tensor_db-execution-option "Direct link to tensor_db-execution-option")

In order to utilize Deep Lake's Managed Tensor Database, it is necessary to specify the runtime parameter as {'tensor\_db': True} during the creation of the vector store. This configuration enables the execution of queries on the Managed Tensor Database, rather than on the client side. It should be noted that this functionality is not applicable to datasets stored locally or in-memory. In the event that a vector store has already been created outside of the Managed Tensor Database, it is possible to transfer it to the Managed Tensor Database by following the prescribed steps.

    # Embed and store the textsusername = "adilkhan"  # your username on app.activeloop.aidataset_path = f"hub://{username}/langchain_testing"docs = text_splitter.split_documents(documents)embedding = OpenAIEmbeddings()db = DeepLake(    dataset_path=dataset_path,    embedding_function=embeddings,    overwrite=True,    runtime={"tensor_db": True},)db.add_documents(docs)

### TQL Search[​](#tql-search "Direct link to TQL Search")

Furthermore, the execution of queries is also supported within the similarity\_search method, whereby the query can be specified utilizing Deep Lake's Tensor Query Language (TQL).

    search_id = db.vectorstore.dataset.id[0].numpy()

    docs = db.similarity_search(    query=None,    tql_query=f"SELECT * WHERE id == '{search_id[0]}'",)

    docs

### Creating vector stores on AWS S3[​](#creating-vector-stores-on-aws-s3 "Direct link to Creating vector stores on AWS S3")

    dataset_path = f"s3://BUCKET/langchain_test"  # could be also ./local/path (much faster locally), hub://bucket/path/to/dataset, gcs://path/to/dataset, etc.embedding = OpenAIEmbeddings()db = DeepLake.from_documents(    docs,    dataset_path=dataset_path,    embedding=embeddings,    overwrite=True,    creds={        "aws_access_key_id": os.environ["AWS_ACCESS_KEY_ID"],        "aws_secret_access_key": os.environ["AWS_SECRET_ACCESS_KEY"],        "aws_session_token": os.environ["AWS_SESSION_TOKEN"],  # Optional    },)

        s3://hub-2.0-datasets-n/langchain_test loaded successfully.    Evaluating ingest: 100%|██████████| 1/1 [00:10<00:00    \    Dataset(path='s3://hub-2.0-datasets-n/langchain_test', tensors=['embedding', 'ids', 'metadata', 'text'])          tensor     htype     shape     dtype  compression      -------   -------   -------   -------  -------      embedding  generic  (4, 1536)  float32   None           ids      text     (4, 1)      str     None        metadata    json     (4, 1)      str     None          text      text     (4, 1)      str     None        

Deep Lake API[​](#deep-lake-api "Direct link to Deep Lake API")
---------------------------------------------------------------

you can access the Deep Lake dataset at `db.vectorstore`

    # get structure of the datasetdb.vectorstore.summary()

        Dataset(path='hub://adilkhan/langchain_testing', tensors=['embedding', 'id', 'metadata', 'text'])          tensor      htype      shape      dtype  compression      -------    -------    -------    -------  -------      embedding  embedding  (42, 1536)  float32   None           id        text      (42, 1)      str     None        metadata     json      (42, 1)      str     None          text       text      (42, 1)      str     None   

    # get embeddings numpy arrayembeds = db.vectorstore.dataset.embedding.numpy()

### Transfer local dataset to cloud[​](#transfer-local-dataset-to-cloud "Direct link to Transfer local dataset to cloud")

Copy already created dataset to the cloud. You can also transfer from cloud to local.

    import deeplakeusername = "davitbun"  # your username on app.activeloop.aisource = f"hub://{username}/langchain_test"  # could be local, s3, gcs, etc.destination = f"hub://{username}/langchain_test_copy"  # could be local, s3, gcs, etc.deeplake.deepcopy(src=source, dest=destination, overwrite=True)

        Copying dataset: 100%|██████████| 56/56 [00:38<00:00    This dataset can be visualized in Jupyter Notebook by ds.visualize() or at https://app.activeloop.ai/davitbun/langchain_test_copy    Your Deep Lake dataset has been successfully created!    The dataset is private so make sure you are logged in!    Dataset(path='hub://davitbun/langchain_test_copy', tensors=['embedding', 'ids', 'metadata', 'text'])

    db = DeepLake(dataset_path=destination, embedding_function=embeddings)db.add_documents(docs)

             This dataset can be visualized in Jupyter Notebook by ds.visualize() or at https://app.activeloop.ai/davitbun/langchain_test_copy        /    hub://davitbun/langchain_test_copy loaded successfully.        Deep Lake Dataset in hub://davitbun/langchain_test_copy already exists, loading from the storage    Dataset(path='hub://davitbun/langchain_test_copy', tensors=['embedding', 'ids', 'metadata', 'text'])          tensor     htype     shape     dtype  compression      -------   -------   -------   -------  -------      embedding  generic  (4, 1536)  float32   None           ids      text     (4, 1)      str     None        metadata    json     (4, 1)      str     None          text      text     (4, 1)      str     None       Evaluating ingest: 100%|██████████| 1/1 [00:31<00:00    -    Dataset(path='hub://davitbun/langchain_test_copy', tensors=['embedding', 'ids', 'metadata', 'text'])          tensor     htype     shape     dtype  compression      -------   -------   -------   -------  -------      embedding  generic  (8, 1536)  float32   None           ids      text     (8, 1)      str     None        metadata    json     (8, 1)      str     None          text      text     (8, 1)      str     None            ['ad42f3fe-e188-11ed-b66d-41c5f7b85421',     'ad42f3ff-e188-11ed-b66d-41c5f7b85421',     'ad42f400-e188-11ed-b66d-41c5f7b85421',     'ad42f401-e188-11ed-b66d-41c5f7b85421']