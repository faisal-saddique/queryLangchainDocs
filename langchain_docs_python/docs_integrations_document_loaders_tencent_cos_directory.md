Tencent COS Directory
=====================

This covers how to load document objects from a `Tencent COS Directory`.

    #! pip install cos-python-sdk-v5

    from langchain.document_loaders import TencentCOSDirectoryLoaderfrom qcloud_cos import CosConfig

    conf = CosConfig(    Region="your cos region",    SecretId="your cos secret_id",    SecretKey="your cos secret_key",)loader = TencentCOSDirectoryLoader(conf=conf, bucket="you_cos_bucket")

    loader.load()

Specifying a prefix[](#specifying-a-prefix "Direct link to Specifying a prefix")
---------------------------------------------------------------------------------

You can also specify a prefix for more finegrained control over what files to load.

    loader = TencentCOSDirectoryLoader(conf=conf, bucket="you_cos_bucket", prefix="fake")

    loader.load()