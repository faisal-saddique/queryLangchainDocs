Org-mode
========

> A [Org Mode document](https://en.wikipedia.org/wiki/Org-mode) is a document editing, formatting, and organizing mode, designed for notes, planning, and authoring within the free software text editor Emacs.

`UnstructuredOrgModeLoader`[​](#unstructuredorgmodeloader "Direct link to unstructuredorgmodeloader")
-----------------------------------------------------------------------------------------------------

You can load data from Org-mode files with `UnstructuredOrgModeLoader` using the following workflow.

    from langchain.document_loaders import UnstructuredOrgModeLoader

    loader = UnstructuredOrgModeLoader(file_path="example_data/README.org", mode="elements")docs = loader.load()

    print(docs[0])

        page_content='Example Docs' metadata={'source': 'example_data/README.org', 'filename': 'README.org', 'file_directory': 'example_data', 'filetype': 'text/org', 'page_number': 1, 'category': 'Title'}