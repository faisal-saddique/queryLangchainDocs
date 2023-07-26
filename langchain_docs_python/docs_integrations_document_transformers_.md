Document transformers
=====================

[

📄️ Doctran Extract Properties
------------------------------

We can extract useful features of documents using the Doctran library, which uses OpenAI's function calling feature to extract specific metadata.

](/docs/integrations/document_transformers/doctran_extract_properties)

[

📄️ Doctran Interrogate Documents
---------------------------------

Documents used in a vector store knowledge base are typically stored in narrative or conversational format. However, most user queries are in question format. If we convert documents into Q&A format before vectorizing them, we can increase the liklihood of retrieving relevant documents, and decrease the liklihood of retrieving irrelevant documents.

](/docs/integrations/document_transformers/doctran_interrogate_document)

[

📄️ Doctran Translate Documents
-------------------------------

Comparing documents through embeddings has the benefit of working across multiple languages. "Harrison says hello" and "Harrison dice hola" will occupy similar positions in the vector space because they have the same meaning semantically.

](/docs/integrations/document_transformers/doctran_translate_document)

[

📄️ html2text
-------------

html2text is a Python script that converts a page of HTML into clean, easy-to-read plain ASCII text.

](/docs/integrations/document_transformers/html2text)

[

📄️ OpenAI Functions Metadata Tagger
------------------------------------

It can often be useful to tag ingested documents with structured metadata, such as the title, tone, or length of a document, to allow for more targeted similarity search later. However, for large numbers of documents, performing this labelling process manually can be tedious.

](/docs/integrations/document_transformers/openai_metadata_tagger)