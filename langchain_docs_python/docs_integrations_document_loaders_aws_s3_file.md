AWS S3 File
===========

> [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) is an object storage service.

> [AWS S3 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)

This covers how to load document objects from an `AWS S3 File` object.

    from langchain.document_loaders import S3FileLoader

    #!pip install boto3

    loader = S3FileLoader("testing-hwc", "fake.docx")

    loader.load()

        [Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpxvave6wl/fake.docx'}, lookup_index=0)]