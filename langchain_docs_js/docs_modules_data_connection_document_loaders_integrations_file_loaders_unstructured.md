Unstructured
============

This example covers how to use [Unstructured](/docs/modules/data_connection/document_loaders/integrations/file_loaders/docs/ecosystem/integrations/unstructured) to load files of many types. Unstructured currently supports loading of text files, powerpoints, html, pdfs, images, and more.

Setup[](#setup "Direct link to Setup")
---------------------------------------

You can run Unstructured locally in your computer using Docker. To do so, you need to have Docker installed. You can find the instructions to install Docker [here](https://docs.docker.com/get-docker/).

    docker run -p 8000:8000 -d --rm --name unstructured-api quay.io/unstructured-io/unstructured-api:latest --port 8000 --host 0.0.0.0

Usage[](#usage "Direct link to Usage")
---------------------------------------

Once Unstructured is running, you can use it to load files from your computer. You can use the following code to load a file from your computer.

    import { UnstructuredLoader } from "langchain/document_loaders/fs/unstructured";const options = {  apiKey: "MY_API_KEY",};const loader = new UnstructuredLoader(  "src/document_loaders/example_data/notion.md",  options);const docs = await loader.load();

#### API Reference:

*   [UnstructuredLoader](/docs/api/document_loaders_fs_unstructured/classes/UnstructuredLoader) from `langchain/document_loaders/fs/unstructured`

Directories[](#directories "Direct link to Directories")
---------------------------------------------------------

You can also load all of the files in the directory using `UnstructuredDirectoryLoader`, which inherits from [`DirectoryLoader`](/docs/modules/data_connection/document_loaders/integrations/file_loaders/directory):

    import { UnstructuredDirectoryLoader } from "langchain/document_loaders/fs/unstructured";const options = {  apiKey: "MY_API_KEY",};const loader = new UnstructuredDirectoryLoader(  "langchain/src/document_loaders/tests/example_data",  options);const docs = await loader.load();

#### API Reference:

*   [UnstructuredDirectoryLoader](/docs/api/document_loaders_fs_unstructured/classes/UnstructuredDirectoryLoader) from `langchain/document_loaders/fs/unstructured`