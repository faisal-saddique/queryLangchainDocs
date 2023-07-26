AWS S3 Directory
================

> [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) is an object storage service.

> [AWS S3 Directory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html)

> [AWS S3 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

    pip install boto3

Document Loader[](#document-loader "Direct link to Document Loader")
---------------------------------------------------------------------

See a [usage example for S3DirectoryLoader](/docs/integrations/document_loaders/aws_s3_directory.html).

See a [usage example for S3FileLoader](/docs/integrations/document_loaders/aws_s3_file.html).

    from langchain.document_loaders import S3DirectoryLoader, S3FileLoader