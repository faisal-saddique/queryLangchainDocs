Google Cloud Storage
====================

> [Google Cloud Storage](https://en.wikipedia.org/wiki/Google_Cloud_Storage) is a managed service for storing unstructured data.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

First, you need to install `google-cloud-bigquery` python package.

    pip install google-cloud-storage

Document Loader[​](#document-loader "Direct link to Document Loader")
---------------------------------------------------------------------

There are two loaders for the `Google Cloud Storage`: the `Directory` and the `File` loaders.

See a [usage example](/docs/modules/data_connection/document_loaders/integrations/google_cloud_storage_directory.html).

    from langchain.document_loaders import GCSDirectoryLoader

See a [usage example](/docs/modules/data_connection/document_loaders/integrations/google_cloud_storage_file.html).

    from langchain.document_loaders import GCSFileLoader