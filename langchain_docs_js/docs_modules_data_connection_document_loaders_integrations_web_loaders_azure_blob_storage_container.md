Azure Blob Storage Container
============================

Compatibility

Only available on Node.js.

This covers how to load a container on Azure Blob Storage into LangChain documents.

Setup[](#setup "Direct link to Setup")
---------------------------------------

To run this loader, you'll need to have Unstructured already set up and ready to use at an available URL endpoint. It can also be configured to run locally.

See the docs [here](https://js.langchain.com/docs/modules/indexes/document_loaders/examples/file_loaders/unstructured) for information on how to do that.

You'll also need to install the official Azure Storage Blob client library:

*   npm
*   Yarn
*   pnpm

    npm install @azure/storage-blob

    yarn add @azure/storage-blob

    pnpm add @azure/storage-blob

Usage[](#usage "Direct link to Usage")
---------------------------------------

Once Unstructured is configured, you can use the Azure Blob Storage Container loader to load files and then convert them into a Document.

    import { AzureBlobStorageContainerLoader } from "langchain/document_loaders/web/azure_blob_storage_container";const loader = new AzureBlobStorageContainerLoader({  azureConfig: {    connectionString: "",    container: "container_name",  },  unstructuredConfig: {    apiUrl: "http://localhost:8000/general/v0/general",    apiKey: "", // this will be soon required  },});const docs = await loader.load();console.log(docs);

#### API Reference:

*   [AzureBlobStorageContainerLoader](/docs/api/document_loaders_web_azure_blob_storage_container/classes/AzureBlobStorageContainerLoader) from `langchain/document_loaders/web/azure_blob_storage_container`