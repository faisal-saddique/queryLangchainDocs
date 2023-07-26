EPub
====

> [EPUB](https://en.wikipedia.org/wiki/EPUB) is an e-book file format that uses the ".epub" file extension. The term is short for electronic publication and is sometimes styled ePub. `EPUB` is supported by many e-readers, and compatible software is available for most smartphones, tablets, and computers.

This covers how to load `.epub` documents into the Document format that we can use downstream. You'll need to install the [`pandoc`](https://pandoc.org/installing.html) package for this loader to work.

    #!pip install pandoc

    from langchain.document_loaders import UnstructuredEPubLoader

    loader = UnstructuredEPubLoader("winter-sports.epub")

    data = loader.load()

Retain Elements[](#retain-elements "Direct link to Retain Elements")
---------------------------------------------------------------------

Under the hood, Unstructured creates different "elements" for different chunks of text. By default we combine those together, but you can easily keep that separation by specifying `mode="elements"`.

    loader = UnstructuredEPubLoader("winter-sports.epub", mode="elements")

    data = loader.load()

    data[0]

        Document(page_content='The Project Gutenberg eBook of Winter Sports in\nSwitzerland, by E. F. Benson', lookup_str='', metadata={'source': 'winter-sports.epub', 'page_number': 1, 'category': 'Title'}, lookup_index=0)