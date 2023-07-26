ReadTheDocs Documentation
=========================

> [Read the Docs](https://readthedocs.org/) is an open-sourced free software documentation hosting platform. It generates documentation written with the `Sphinx` documentation generator.

This notebook covers how to load content from HTML that was generated as part of a `Read-The-Docs` build.

For an example of this in the wild, see [here](https://github.com/hwchase17/chat-langchain).

This assumes that the HTML has already been scraped into a folder. This can be done by uncommenting and running the following command

    #!pip install beautifulsoup4

    #!wget -r -A.html -P rtdocs https://python.langchain.com/en/latest/

    from langchain.document_loaders import ReadTheDocsLoader

    loader = ReadTheDocsLoader("rtdocs", features="html.parser")

    docs = loader.load()