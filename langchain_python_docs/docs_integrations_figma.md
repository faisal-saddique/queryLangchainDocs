Figma
=====

> [Figma](https://www.figma.com/) is a collaborative web application for interface design.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

The Figma API requires an `access token`, `node_ids`, and a `file key`.

The `file key` can be pulled from the URL. [https://www.figma.com/file/{filekey}/sampleFilename](https://www.figma.com/file/%7Bfilekey%7D/sampleFilename)

`Node IDs` are also available in the URL. Click on anything and look for the '?node-id={node\_id}' param.

`Access token` [instructions](https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens).

Document Loader[​](#document-loader "Direct link to Document Loader")
---------------------------------------------------------------------

See a [usage example](/docs/modules/data_connection/document_loaders/integrations/figma.html).

    from langchain.document_loaders import FigmaFileLoader