DeepInfra
=========

[DeepInfra](https://deepinfra.com/?utm_source=langchain) is a serverless inference as a service that provides access to a [variety of LLMs](https://deepinfra.com/models?utm_source=langchain) and [embeddings models](https://deepinfra.com/models?type=embeddings&utm_source=langchain). This notebook goes over how to use LangChain with DeepInfra for text embeddings.

    # sign up for an account: https://deepinfra.com/login?utm_source=langchainfrom getpass import getpassDEEPINFRA_API_TOKEN = getpass()

         ········

    import osos.environ["DEEPINFRA_API_TOKEN"] = DEEPINFRA_API_TOKEN

    from langchain.embeddings import DeepInfraEmbeddings

    embeddings = DeepInfraEmbeddings(    model_id="sentence-transformers/clip-ViT-B-32",    query_instruction="",    embed_instruction="",)

    docs = ["Dog is not a cat", "Beta is the second letter of Greek alphabet"]document_result = embeddings.embed_documents(docs)

    query = "What is the first letter of Greek alphabet"query_result = embeddings.embed_query(query)

    import numpy as npquery_numpy = np.array(query_result)for doc_res, doc in zip(document_result, docs):    document_numpy = np.array(doc_res)    similarity = np.dot(query_numpy, document_numpy) / (        np.linalg.norm(query_numpy) * np.linalg.norm(document_numpy)    )    print(f'Cosine similarity between "{doc}" and query: {similarity}')

        Cosine similarity between "Dog is not a cat" and query: 0.7489097144129355    Cosine similarity between "Beta is the second letter of Greek alphabet" and query: 0.9519380640702013