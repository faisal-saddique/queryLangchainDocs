Iugu
====

> [Iugu](https://www.iugu.com/) is a Brazilian services and software as a service (SaaS) company. It offers payment-processing software and application programming interfaces for e-commerce websites and mobile applications.

This notebook covers how to load data from the `Iugu REST API` into a format that can be ingested into LangChain, along with example usage for vectorization.

    import osfrom langchain.document_loaders import IuguLoaderfrom langchain.indexes import VectorstoreIndexCreator

The Iugu API requires an access token, which can be found inside of the Iugu dashboard.

This document loader also requires a `resource` option which defines what data you want to load.

Following resources are available:

`Documentation` [Documentation](https://dev.iugu.com/reference/metadados)

    iugu_loader = IuguLoader("charges")

    # Create a vectorstore retriever from the loader# see https://python.langchain.com/en/latest/modules/data_connection/getting_started.html for more detailsindex = VectorstoreIndexCreator().from_loaders([iugu_loader])iugu_doc_retriever = index.vectorstore.as_retriever()