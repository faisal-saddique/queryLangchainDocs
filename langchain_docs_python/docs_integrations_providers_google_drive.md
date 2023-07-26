Google Drive
============

> [Google Drive](https://en.wikipedia.org/wiki/Google_Drive) is a file storage and synchronization service developed by Google.

Currently, only `Google Docs` are supported.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

First, you need to install several python package.

    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

Document Loader[](#document-loader "Direct link to Document Loader")
---------------------------------------------------------------------

See a [usage example and authorizing instructions](/docs/integrations/document_loaders/google_drive.html).

    from langchain.document_loaders import GoogleDriveLoader