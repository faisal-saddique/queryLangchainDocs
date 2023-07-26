RST
===

> A [reStructured Text (RST)](https://en.wikipedia.org/wiki/ReStructuredText) file is a file format for textual data used primarily in the Python programming language community for technical documentation.

`UnstructuredRSTLoader`[](#unstructuredrstloader "Direct link to unstructuredrstloader")
-----------------------------------------------------------------------------------------

You can load data from RST files with `UnstructuredRSTLoader` using the following workflow.

    from langchain.document_loaders import UnstructuredRSTLoader

    loader = UnstructuredRSTLoader(file_path="example_data/README.rst", mode="elements")docs = loader.load()

    print(docs[0])

        page_content='Example Docs' metadata={'source': 'example_data/README.rst', 'filename': 'README.rst', 'file_directory': 'example_data', 'filetype': 'text/x-rst', 'page_number': 1, 'category': 'Title'}