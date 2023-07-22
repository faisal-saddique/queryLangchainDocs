Psychic
=======

This notebook covers how to load documents from `Psychic`. See [here](/docs/ecosystem/integrations/psychic.html) for more details.

Prerequisites[​](#prerequisites "Direct link to Prerequisites")
---------------------------------------------------------------

1.  Follow the Quick Start section in [this document](/docs/ecosystem/integrations/psychic.html)
2.  Log into the [Psychic dashboard](https://dashboard.psychic.dev/) and get your secret key
3.  Install the frontend react library into your web app and have a user authenticate a connection. The connection will be created using the connection id that you specify.

Loading documents[​](#loading-documents "Direct link to Loading documents")
---------------------------------------------------------------------------

Use the `PsychicLoader` class to load in documents from a connection. Each connection has a connector id (corresponding to the SaaS app that was connected) and a connection id (which you passed in to the frontend library).

    # Uncomment this to install psychicapi if you don't already have it installedpoetry run pip -q install psychicapi

            [notice] A new release of pip is available: 23.0.1 -> 23.1.2    [notice] To update, run: pip install --upgrade pip

    from langchain.document_loaders import PsychicLoaderfrom psychicapi import ConnectorId# Create a document loader for google drive. We can also load from other connectors by setting the connector_id to the appropriate value e.g. ConnectorId.notion.value# This loader uses our test credentialsgoogle_drive_loader = PsychicLoader(    api_key="7ddb61c1-8b6a-4d31-a58e-30d1c9ea480e",    connector_id=ConnectorId.gdrive.value,    connection_id="google-test",)documents = google_drive_loader.load()

Converting the docs to embeddings[​](#converting-the-docs-to-embeddings "Direct link to Converting the docs to embeddings")
---------------------------------------------------------------------------------------------------------------------------

We can now convert these documents into embeddings and store them in a vector database like Chroma

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.vectorstores import Chromafrom langchain.text_splitter import CharacterTextSplitterfrom langchain.llms import OpenAIfrom langchain.chains import RetrievalQAWithSourcesChain

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)texts = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()docsearch = Chroma.from_documents(texts, embeddings)chain = RetrievalQAWithSourcesChain.from_chain_type(    OpenAI(temperature=0), chain_type="stuff", retriever=docsearch.as_retriever())chain({"question": "what is psychic?"}, return_only_outputs=True)