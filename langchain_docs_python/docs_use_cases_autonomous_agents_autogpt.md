AutoGPT
=======

Implementation of [https://github.com/Significant-Gravitas/Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) but with LangChain primitives (LLMs, PromptTemplates, VectorStores, Embeddings, Tools)

Set up tools[](#set-up-tools "Direct link to Set up tools")
------------------------------------------------------------

We'll set up an AutoGPT with a search tool, and write-file tool, and a read-file tool

    from langchain.utilities import SerpAPIWrapperfrom langchain.agents import Toolfrom langchain.tools.file_management.write import WriteFileToolfrom langchain.tools.file_management.read import ReadFileToolsearch = SerpAPIWrapper()tools = [    Tool(        name="search",        func=search.run,        description="useful for when you need to answer questions about current events. You should ask targeted questions",    ),    WriteFileTool(),    ReadFileTool(),]

Set up memory[](#set-up-memory "Direct link to Set up memory")
---------------------------------------------------------------

The memory here is used for the agents intermediate steps

    from langchain.vectorstores import FAISSfrom langchain.docstore import InMemoryDocstorefrom langchain.embeddings import OpenAIEmbeddings

    # Define your embedding modelembeddings_model = OpenAIEmbeddings()# Initialize the vectorstore as emptyimport faissembedding_size = 1536index = faiss.IndexFlatL2(embedding_size)vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})

Setup model and AutoGPT[](#setup-model-and-autogpt "Direct link to Setup model and AutoGPT")
---------------------------------------------------------------------------------------------

Initialize everything! We will use ChatOpenAI model

    from langchain.experimental import AutoGPTfrom langchain.chat_models import ChatOpenAI

    agent = AutoGPT.from_llm_and_tools(    ai_name="Tom",    ai_role="Assistant",    tools=tools,    llm=ChatOpenAI(temperature=0),    memory=vectorstore.as_retriever(),)# Set verbose to be trueagent.chain.verbose = True

Run an example[](#run-an-example "Direct link to Run an example")
------------------------------------------------------------------

Here we will make it write a weather report for SF

    agent.run(["write a weather report for SF today"])

Chat History Memory[](#chat-history-memory "Direct link to Chat History Memory")
---------------------------------------------------------------------------------

In addition to the memory that holds the agent immediate steps, we also have a chat history memory. By default, the agent will use 'ChatMessageHistory' and it can be changed. This is useful when you want to use a different type of memory for example 'FileChatHistoryMemory'

    from langchain.memory.chat_message_histories import FileChatMessageHistoryagent = AutoGPT.from_llm_and_tools(    ai_name="Tom",    ai_role="Assistant",    tools=tools,    llm=ChatOpenAI(temperature=0),    memory=vectorstore.as_retriever(),    chat_history_memory=FileChatMessageHistory("chat_history.txt"),)