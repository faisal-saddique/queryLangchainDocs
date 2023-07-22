Question Answering Over Documents
=================================

info

[Python Guide](https://python.langchain.com/en/latest/use_cases/question_answering.html)

[JS Guide](https://js.langchain.com/docs/use_cases/question_answering/)

Although LLMs are powerful, they do not know about information they were not trained on. If you want to use an LLM to answer questions about documents it was not trained on, you have to give it information about those documents. The most common way to do this is through "retrieval augmented generation".

The idea of retrieval augmented generation is that when given a question you first do a retrieval step to fetch any relevant documents. You then pass those documents, along with the original question, to the language model and have it generate a response. In order to do this, however, you first have to have your documents in a format where they can be queried in such a manner. This page goes over the high level ideas between those two steps: (1) ingestion of documents into a queriable format, and then (2) the retrieval augmented generation chain.

Ingestion[​](#ingestion "Direct link to Ingestion")
---------------------------------------------------

In order use a language model to interact with your data, you first have to get in a suitable format. That format would be an `Index`. By putting data into an Index, you make it easy for any downstream steps to interact with it.

There are several types of indexes, but by far the most common one is a Vectorstore. Ingesting documents into a vectorstore can be done with the following steps:

1.  Load documents (using a Document Loader)
2.  Split documents (using a Text Splitter)
3.  Create embeddings for documents (using a Text Embedding Model)
4.  Store documents and embeddings in a vectorstore

Generation[​](#generation "Direct link to Generation")
------------------------------------------------------

Now that we have an Index, how do we use this to do generation? This can be broken into the following steps:

1.  Receive user question
2.  Lookup documents in the index relevant to the question
3.  Construct a PromptValue from the question and any relevant documents (using a PromptTemplate).
4.  Pass the PromptValue to a model
5.  Get back the result and return to the user.