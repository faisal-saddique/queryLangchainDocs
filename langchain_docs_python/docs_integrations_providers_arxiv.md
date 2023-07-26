Arxiv
=====

> [arXiv](https://arxiv.org/) is an open-access archive for 2 million scholarly articles in the fields of physics, mathematics, computer science, quantitative biology, quantitative finance, statistics, electrical engineering and systems science, and economics.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

First, you need to install `arxiv` python package.

    pip install arxiv

Second, you need to install `PyMuPDF` python package which transforms PDF files downloaded from the `arxiv.org` site into the text format.

    pip install pymupdf

Document Loader[](#document-loader "Direct link to Document Loader")
---------------------------------------------------------------------

See a [usage example](/docs/integrations/document_loaders/arxiv).

    from langchain.document_loaders import ArxivLoader

Retriever[](#retriever "Direct link to Retriever")
---------------------------------------------------

See a [usage example](/docs/integrations/retrievers/arxiv).

    from langchain.retrievers import ArxivRetriever