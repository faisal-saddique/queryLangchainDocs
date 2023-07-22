Bedrock Embeddings
==================

    %pip install boto3

    from langchain.embeddings import BedrockEmbeddingsembeddings = BedrockEmbeddings(    credentials_profile_name="bedrock-admin", endpoint_url="custom_endpoint_url")

    embeddings.embed_query("This is a content of the document")

    embeddings.embed_documents(["This is a content of the document"])