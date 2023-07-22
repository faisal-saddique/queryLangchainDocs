Use LangChain, GPT and Activeloop's Deep Lake to work with code base
====================================================================

In this tutorial, we are going to use Langchain + Activeloop's Deep Lake with GPT to analyze the code base of the LangChain itself.

Design[​](#design "Direct link to Design")
------------------------------------------

1.  Prepare data:
    1.  Upload all python project files using the `langchain.document_loaders.TextLoader`. We will call these files the **documents**.
    2.  Split all documents to chunks using the `langchain.text_splitter.CharacterTextSplitter`.
    3.  Embed chunks and upload them into the DeepLake using `langchain.embeddings.openai.OpenAIEmbeddings` and `langchain.vectorstores.DeepLake`
2.  Question-Answering:
    1.  Build a chain from `langchain.chat_models.ChatOpenAI` and `langchain.chains.ConversationalRetrievalChain`
    2.  Prepare questions.
    3.  Get answers running the chain.

Implementation[​](#implementation "Direct link to Implementation")
------------------------------------------------------------------

### Integration preparations[​](#integration-preparations "Direct link to Integration preparations")

We need to set up keys for external services and install necessary python libraries.

    #!python3 -m pip install --upgrade langchain deeplake openai

Set up OpenAI embeddings, Deep Lake multi-modal vector store api and authenticate.

For full documentation of Deep Lake please follow [https://docs.activeloop.ai/](https://docs.activeloop.ai/) and API reference [https://docs.deeplake.ai/en/latest/](https://docs.deeplake.ai/en/latest/)

    import osfrom getpass import getpassos.environ["OPENAI_API_KEY"] = getpass()# Please manually enter OpenAI Key

Authenticate into Deep Lake if you want to create your own dataset and publish it. You can get an API key from the platform at [app.activeloop.ai](https://app.activeloop.ai)

    activeloop_token = getpass("Activeloop Token:")os.environ["ACTIVELOOP_TOKEN"] = activeloop_token

### Prepare data[​](#prepare-data "Direct link to Prepare data")

Load all repository files. Here we assume this notebook is downloaded as the part of the langchain fork and we work with the python files of the `langchain` repo.

If you want to use files from different repo, change `root_dir` to the root dir of your repo.

    ls "../../../.."

    from langchain.document_loaders import TextLoaderroot_dir = "../../../.."docs = []for dirpath, dirnames, filenames in os.walk(root_dir):    for file in filenames:        if file.endswith(".py") and "/.venv/" not in dirpath:            try:                loader = TextLoader(os.path.join(dirpath, file), encoding="utf-8")                docs.extend(loader.load_and_split())            except Exception as e:                passprint(f"{len(docs)}")

Then, chunk the files

    from langchain.text_splitter import CharacterTextSplittertext_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)texts = text_splitter.split_documents(docs)print(f"{len(texts)}")

Then embed chunks and upload them to the DeepLake.

This can take several minutes.

    from langchain.embeddings.openai import OpenAIEmbeddingsembeddings = OpenAIEmbeddings()embeddings

    from langchain.vectorstores import DeepLakedb = DeepLake.from_documents(    texts, embeddings, dataset_path=f"hub://{<org_id>}/langchain-code")db

`Optional`: You can also use Deep Lake's Managed Tensor Database as a hosting service and run queries there. In order to do so, it is necessary to specify the runtime parameter as {'tensor\_db': True} during the creation of the vector store. This configuration enables the execution of queries on the Managed Tensor Database, rather than on the client side. It should be noted that this functionality is not applicable to datasets stored locally or in-memory. In the event that a vector store has already been created outside of the Managed Tensor Database, it is possible to transfer it to the Managed Tensor Database by following the prescribed steps.

    # from langchain.vectorstores import DeepLake# db = DeepLake.from_documents(#     texts, embeddings, dataset_path=f"hub://{<org_id>}/langchain-code", runtime={"tensor_db": True}# )# db

### Question Answering[​](#question-answering "Direct link to Question Answering")

First load the dataset, construct the retriever, then construct the Conversational Chain

    db = DeepLake(    dataset_path=f"hub://{<org_id>}/langchain-code",    read_only=True,    embedding_function=embeddings,)

    retriever = db.as_retriever()retriever.search_kwargs["distance_metric"] = "cos"retriever.search_kwargs["fetch_k"] = 20retriever.search_kwargs["maximal_marginal_relevance"] = Trueretriever.search_kwargs["k"] = 20

You can also specify user defined functions using [Deep Lake filters](https://docs.deeplake.ai/en/latest/deeplake.core.dataset.html#deeplake.core.dataset.Dataset.filter)

    def filter(x):    # filter based on source code    if "something" in x["text"].data()["value"]:        return False    # filter based on path e.g. extension    metadata = x["metadata"].data()["value"]    return "only_this" in metadata["source"] or "also_that" in metadata["source"]### turn on below for custom filtering# retriever.search_kwargs['filter'] = filter

    from langchain.chat_models import ChatOpenAIfrom langchain.chains import ConversationalRetrievalChainmodel = ChatOpenAI(model_name="gpt-3.5-turbo")  # 'ada' 'gpt-3.5-turbo' 'gpt-4',qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)

    questions = [    "What is the class hierarchy?",    # "What classes are derived from the Chain class?",    # "What classes and functions in the ./langchain/utilities/ forlder are not covered by unit tests?",    # "What one improvement do you propose in code in relation to the class herarchy for the Chain class?",]chat_history = []for question in questions:    result = qa({"question": question, "chat_history": chat_history})    chat_history.append((question, result["answer"]))    print(f"-> **Question**: {question} \n")    print(f"**Answer**: {result['answer']} \n")

\-> **Question**: What is the class hierarchy?

**Answer**: There are several class hierarchies in the provided code, so I'll list a few:

1.  `BaseModel` -> `ConstitutionalPrinciple`: `ConstitutionalPrinciple` is a subclass of `BaseModel`.
2.  `BasePromptTemplate` -> `StringPromptTemplate`, `AIMessagePromptTemplate`, `BaseChatPromptTemplate`, `ChatMessagePromptTemplate`, `ChatPromptTemplate`, `HumanMessagePromptTemplate`, `MessagesPlaceholder`, `SystemMessagePromptTemplate`, `FewShotPromptTemplate`, `FewShotPromptWithTemplates`, `Prompt`, `PromptTemplate`: All of these classes are subclasses of `BasePromptTemplate`.
3.  `APIChain`, `Chain`, `MapReduceDocumentsChain`, `MapRerankDocumentsChain`, `RefineDocumentsChain`, `StuffDocumentsChain`, `HypotheticalDocumentEmbedder`, `LLMChain`, `LLMBashChain`, `LLMCheckerChain`, `LLMMathChain`, `LLMRequestsChain`, `PALChain`, `QAWithSourcesChain`, `VectorDBQAWithSourcesChain`, `VectorDBQA`, `SQLDatabaseChain`: All of these classes are subclasses of `Chain`.
4.  `BaseLoader`: `BaseLoader` is a subclass of `ABC`.
5.  `BaseTracer` -> `ChainRun`, `LLMRun`, `SharedTracer`, `ToolRun`, `Tracer`, `TracerException`, `TracerSession`: All of these classes are subclasses of `BaseTracer`.
6.  `OpenAIEmbeddings`, `HuggingFaceEmbeddings`, `CohereEmbeddings`, `JinaEmbeddings`, `LlamaCppEmbeddings`, `HuggingFaceHubEmbeddings`, `TensorflowHubEmbeddings`, `SagemakerEndpointEmbeddings`, `HuggingFaceInstructEmbeddings`, `SelfHostedEmbeddings`, `SelfHostedHuggingFaceEmbeddings`, `SelfHostedHuggingFaceInstructEmbeddings`, `FakeEmbeddings`, `AlephAlphaAsymmetricSemanticEmbedding`, `AlephAlphaSymmetricSemanticEmbedding`: All of these classes are subclasses of `BaseLLM`.

\-> **Question**: What classes are derived from the Chain class?

**Answer**: There are multiple classes that are derived from the Chain class. Some of them are:

*   APIChain
*   AnalyzeDocumentChain
*   ChatVectorDBChain
*   CombineDocumentsChain
*   ConstitutionalChain
*   ConversationChain
*   GraphQAChain
*   HypotheticalDocumentEmbedder
*   LLMChain
*   LLMCheckerChain
*   LLMRequestsChain
*   LLMSummarizationCheckerChain
*   MapReduceChain
*   OpenAPIEndpointChain
*   PALChain
*   QAWithSourcesChain
*   RetrievalQA
*   RetrievalQAWithSourcesChain
*   SequentialChain
*   SQLDatabaseChain
*   TransformChain
*   VectorDBQA
*   VectorDBQAWithSourcesChain

There might be more classes that are derived from the Chain class as it is possible to create custom classes that extend the Chain class.

\-> **Question**: What classes and functions in the ./langchain/utilities/ forlder are not covered by unit tests?

**Answer**: All classes and functions in the `./langchain/utilities/` folder seem to have unit tests written for them.