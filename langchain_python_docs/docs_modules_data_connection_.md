Data connection
===============

Many LLM applications require user-specific data that is not part of the model's training set. LangChain gives you the building blocks to load, transform, store and query your data via:

*   [Document loaders](/docs/modules/data_connection/document_loaders/): Load documents from many different sources
*   [Document transformers](/docs/modules/data_connection/document_transformers/): Split documents, convert documents into Q&A format, drop redundant documents, and more
*   [Text embedding models](/docs/modules/data_connection/text_embedding/): Take unstructured text and turn it into a list of floating point numbers
*   [Vector stores](/docs/modules/data_connection/vectorstores/): Store and search over embedded data
*   [Retrievers](/docs/modules/data_connection/retrievers/): Query your data

![data_connection_diagram](/assets/images/data_connection-c42d68c3d092b85f50d08d4cc171fc25.jpg)