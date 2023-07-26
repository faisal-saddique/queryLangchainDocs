MosaicML embeddings
===================

[MosaicML](https://docs.mosaicml.com/en/latest/inference.html) offers a managed inference service. You can either use a variety of open source models, or deploy your own.

This example goes over how to use LangChain to interact with MosaicML Inference for text embedding.

    # sign up for an account: https://forms.mosaicml.com/demo?utm_source=langchainfrom getpass import getpassMOSAICML_API_TOKEN = getpass()

    import osos.environ["MOSAICML_API_TOKEN"] = MOSAICML_API_TOKEN

    from langchain.embeddings import MosaicMLInstructorEmbeddings

    embeddings = MosaicMLInstructorEmbeddings(    query_instruction="Represent the query for retrieval: ")

    query_text = "This is a test query."query_result = embeddings.embed_query(query_text)

    document_text = "This is a test document."document_result = embeddings.embed_documents([document_text])

    import numpy as npquery_numpy = np.array(query_result)document_numpy = np.array(document_result[0])similarity = np.dot(query_numpy, document_numpy) / (    np.linalg.norm(query_numpy) * np.linalg.norm(document_numpy))print(f"Cosine similarity between document and query: {similarity}")