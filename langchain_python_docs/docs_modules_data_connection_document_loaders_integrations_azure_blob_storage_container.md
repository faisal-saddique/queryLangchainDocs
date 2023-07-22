Azure Blob Storage Container
============================

> [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction) is Microsoft's object storage solution for the cloud. Blob Storage is optimized for storing massive amounts of unstructured data. Unstructured data is data that doesn't adhere to a particular data model or definition, such as text or binary data.

`Azure Blob Storage` is designed for:

*   Serving images or documents directly to a browser.
*   Storing files for distributed access.
*   Streaming video and audio.
*   Writing to log files.
*   Storing data for backup and restore, disaster recovery, and archiving.
*   Storing data for analysis by an on-premises or Azure-hosted service.

This notebook covers how to load document objects from a container on `Azure Blob Storage`.

    #!pip install azure-storage-blob

    from langchain.document_loaders import AzureBlobStorageContainerLoader

    loader = AzureBlobStorageContainerLoader(conn_str="<conn_str>", container="<container>")

    loader.load()

        [Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpaa9xl6ch/fake.docx'}, lookup_index=0)]

Specifying a prefix[​](#specifying-a-prefix "Direct link to Specifying a prefix")
---------------------------------------------------------------------------------

You can also specify a prefix for more finegrained control over what files to load.

    loader = AzureBlobStorageContainerLoader(    conn_str="<conn_str>", container="<container>", prefix="<prefix>")

    loader.load()

        [Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpujbkzf_l/fake.docx'}, lookup_index=0)]