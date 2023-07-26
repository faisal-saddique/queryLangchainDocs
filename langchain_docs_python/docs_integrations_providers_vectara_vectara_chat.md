Chat Over Documents with Vectara
================================

This notebook is based on the [chat\_vector\_db](https://github.com/hwchase17/langchain/blob/master/docs/modules/chains/index_examples/chat_vector_db.html) notebook, but using Vectara as the vector database.

    import osfrom langchain.vectorstores import Vectarafrom langchain.vectorstores.vectara import VectaraRetrieverfrom langchain.llms import OpenAIfrom langchain.chains import ConversationalRetrievalChain

Load in documents. You can replace this with a loader for whatever type of data you want

    from langchain.document_loaders import TextLoaderloader = TextLoader("../../modules/state_of_the_union.txt")documents = loader.load()

We now split the documents, create embeddings for them, and put them in a vectorstore. This allows us to do semantic search over them.

    vectorstore = Vectara.from_documents(documents, embedding=None)

We can now create a memory object, which is neccessary to track the inputs/outputs and hold a conversation.

    from langchain.memory import ConversationBufferMemorymemory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

We now initialize the `ConversationalRetrievalChain`

    openai_api_key = os.environ["OPENAI_API_KEY"]llm = OpenAI(openai_api_key=openai_api_key, temperature=0)retriever = vectorstore.as_retriever(lambda_val=0.025, k=5, filter=None)d = retriever.get_relevant_documents(    "What did the president say about Ketanji Brown Jackson")qa = ConversationalRetrievalChain.from_llm(llm, retriever, memory=memory)

    query = "What did the president say about Ketanji Brown Jackson"result = qa({"question": query})

    result["answer"]

        " The president said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence."

    query = "Did he mention who she suceeded"result = qa({"question": query})

    result["answer"]

        ' Justice Stephen Breyer'

Pass in chat history[](#pass-in-chat-history "Direct link to Pass in chat history")
------------------------------------------------------------------------------------

In the above example, we used a Memory object to track chat history. We can also just pass it in explicitly. In order to do this, we need to initialize a chain without any memory object.

    qa = ConversationalRetrievalChain.from_llm(    OpenAI(temperature=0), vectorstore.as_retriever())

Here's an example of asking a question with no chat history

    chat_history = []query = "What did the president say about Ketanji Brown Jackson"result = qa({"question": query, "chat_history": chat_history})

    result["answer"]

        " The president said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence."

Here's an example of asking a question with some chat history

    chat_history = [(query, result["answer"])]query = "Did he mention who she suceeded"result = qa({"question": query, "chat_history": chat_history})

    result["answer"]

        ' Justice Stephen Breyer'

Return Source Documents[](#return-source-documents "Direct link to Return Source Documents")
---------------------------------------------------------------------------------------------

You can also easily return source documents from the ConversationalRetrievalChain. This is useful for when you want to inspect what documents were returned.

    qa = ConversationalRetrievalChain.from_llm(    llm, vectorstore.as_retriever(), return_source_documents=True)

    chat_history = []query = "What did the president say about Ketanji Brown Jackson"result = qa({"question": query, "chat_history": chat_history})

    result["source_documents"][0]

        Document(page_content='Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. \n\nTonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. \n\nOne of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. \n\nAnd I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', metadata={'source': '../../../state_of_the_union.txt'})

ConversationalRetrievalChain with `search_distance`[](#conversationalretrievalchain-with-search_distance "Direct link to conversationalretrievalchain-with-search_distance")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are using a vector store that supports filtering by search distance, you can add a threshold value parameter.

    vectordbkwargs = {"search_distance": 0.9}

    qa = ConversationalRetrievalChain.from_llm(    OpenAI(temperature=0), vectorstore.as_retriever(), return_source_documents=True)chat_history = []query = "What did the president say about Ketanji Brown Jackson"result = qa(    {"question": query, "chat_history": chat_history, "vectordbkwargs": vectordbkwargs})

    print(result["answer"])

         The president said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence.

ConversationalRetrievalChain with `map_reduce`[](#conversationalretrievalchain-with-map_reduce "Direct link to conversationalretrievalchain-with-map_reduce")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

We can also use different types of combine document chains with the ConversationalRetrievalChain chain.

    from langchain.chains import LLMChainfrom langchain.chains.question_answering import load_qa_chainfrom langchain.chains.conversational_retrieval.prompts import CONDENSE_QUESTION_PROMPT

    question_generator = LLMChain(llm=llm, prompt=CONDENSE_QUESTION_PROMPT)doc_chain = load_qa_chain(llm, chain_type="map_reduce")chain = ConversationalRetrievalChain(    retriever=vectorstore.as_retriever(),    question_generator=question_generator,    combine_docs_chain=doc_chain,)

    chat_history = []query = "What did the president say about Ketanji Brown Jackson"result = chain({"question": query, "chat_history": chat_history})

    result["answer"]

        " The president said that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson, who he described as one of the nation's top legal minds, to continue Justice Breyer's legacy of excellence."

ConversationalRetrievalChain with Question Answering with sources[](#conversationalretrievalchain-with-question-answering-with-sources "Direct link to ConversationalRetrievalChain with Question Answering with sources")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also use this chain with the question answering with sources chain.

    from langchain.chains.qa_with_sources import load_qa_with_sources_chain

    question_generator = LLMChain(llm=llm, prompt=CONDENSE_QUESTION_PROMPT)doc_chain = load_qa_with_sources_chain(llm, chain_type="map_reduce")chain = ConversationalRetrievalChain(    retriever=vectorstore.as_retriever(),    question_generator=question_generator,    combine_docs_chain=doc_chain,)

    chat_history = []query = "What did the president say about Ketanji Brown Jackson"result = chain({"question": query, "chat_history": chat_history})

    result["answer"]

        " The president said that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson, who he described as one of the nation's top legal minds, and that she will continue Justice Breyer's legacy of excellence.\nSOURCES: ../../../state_of_the_union.txt"

ConversationalRetrievalChain with streaming to `stdout`[](#conversationalretrievalchain-with-streaming-to-stdout "Direct link to conversationalretrievalchain-with-streaming-to-stdout")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Output from the chain will be streamed to `stdout` token by token in this example.

    from langchain.chains.llm import LLMChainfrom langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandlerfrom langchain.chains.conversational_retrieval.prompts import (    CONDENSE_QUESTION_PROMPT,    QA_PROMPT,)from langchain.chains.question_answering import load_qa_chain# Construct a ConversationalRetrievalChain with a streaming llm for combine docs# and a separate, non-streaming llm for question generationllm = OpenAI(temperature=0, openai_api_key=openai_api_key)streaming_llm = OpenAI(    streaming=True,    callbacks=[StreamingStdOutCallbackHandler()],    temperature=0,    openai_api_key=openai_api_key,)question_generator = LLMChain(llm=llm, prompt=CONDENSE_QUESTION_PROMPT)doc_chain = load_qa_chain(streaming_llm, chain_type="stuff", prompt=QA_PROMPT)qa = ConversationalRetrievalChain(    retriever=vectorstore.as_retriever(),    combine_docs_chain=doc_chain,    question_generator=question_generator,)

    chat_history = []query = "What did the president say about Ketanji Brown Jackson"result = qa({"question": query, "chat_history": chat_history})

         The president said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence.

    chat_history = [(query, result["answer"])]query = "Did he mention who she suceeded"result = qa({"question": query, "chat_history": chat_history})

         Justice Stephen Breyer

get\_chat\_history Function[](#get_chat_history-function "Direct link to get_chat_history Function")
-----------------------------------------------------------------------------------------------------

You can also specify a `get_chat_history` function, which can be used to format the chat\_history string.

    def get_chat_history(inputs) -> str:    res = []    for human, ai in inputs:        res.append(f"Human:{human}\nAI:{ai}")    return "\n".join(res)qa = ConversationalRetrievalChain.from_llm(    llm, vectorstore.as_retriever(), get_chat_history=get_chat_history)

    chat_history = []query = "What did the president say about Ketanji Brown Jackson"result = qa({"question": query, "chat_history": chat_history})

    result["answer"]

        " The president said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence."