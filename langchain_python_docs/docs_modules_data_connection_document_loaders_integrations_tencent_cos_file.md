Tencent COS File
================

This covers how to load document object from a `Tencent COS File`.

    #! pip install cos-python-sdk-v5

    from langchain.document_loaders import TencentCOSFileLoaderfrom qcloud_cos import CosConfig

    conf = CosConfig(    Region="your cos region",    SecretId="your cos secret_id",    SecretKey="your cos secret_key",)loader = TencentCOSFileLoader(conf=conf, bucket="you_cos_bucket", key="fake.docx")

    loader.load()