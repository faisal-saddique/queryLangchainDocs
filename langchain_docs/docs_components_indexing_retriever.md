Retriever
=========

info

[Python Guide](https://python.langchain.com/en/latest/modules/indexes/retrievers.html)

[JS Guide](https://js.langchain.com/docs/modules/indexes/retrievers)

A way of storing data such that it can be queried by a language model. The only interface this object must expose is a `get_relevant_texts` method which takes in a string and returns a list of Documents.