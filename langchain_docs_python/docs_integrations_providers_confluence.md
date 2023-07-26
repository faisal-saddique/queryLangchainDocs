Confluence
==========

> [Confluence](https://www.atlassian.com/software/confluence) is a wiki collaboration platform that saves and organizes all of the project-related material. `Confluence` is a knowledge base that primarily handles content management activities.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

    pip install atlassian-python-api

We need to set up `username/api_key` or `Oauth2 login`. See [instructions](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

Document Loader[](#document-loader "Direct link to Document Loader")
---------------------------------------------------------------------

See a [usage example](/docs/integrations/document_loaders/confluence).

    from langchain.document_loaders import ConfluenceLoader