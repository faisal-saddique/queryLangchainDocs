SageMaker Endpoint
==================

> [Amazon SageMaker](https://aws.amazon.com/sagemaker/) is a system that can build, train, and deploy machine learning (ML) models with fully managed infrastructure, tools, and workflows.

We use `SageMaker` to host our model and expose it as the `SageMaker Endpoint`.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

    pip install boto3

For instructions on how to expose model as a `SageMaker Endpoint`, please see [here](https://www.philschmid.de/custom-inference-huggingface-sagemaker).

**Note**: In order to handle batched requests, we need to adjust the return line in the `predict_fn()` function within the custom `inference.py` script:

Change from

    return {"vectors": sentence_embeddings[0].tolist()}

to:

    return {"vectors": sentence_embeddings.tolist()}

We have to set up following required parameters of the `SagemakerEndpoint` call:

*   `endpoint_name`: The name of the endpoint from the deployed Sagemaker model. Must be unique within an AWS Region.
*   `credentials_profile_name`: The name of the profile in the ~/.aws/credentials or ~/.aws/config files, which has either access keys or role information specified. If not specified, the default credential profile or, if on an EC2 instance, credentials from IMDS will be used. See [this guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).

LLM[](#llm "Direct link to LLM")
---------------------------------

See a [usage example](/docs/integrations/llms/sagemaker).

    from langchain import SagemakerEndpointfrom langchain.llms.sagemaker_endpoint import LLMContentHandler

Text Embedding Models[](#text-embedding-models "Direct link to Text Embedding Models")
---------------------------------------------------------------------------------------

See a [usage example](/docs/integrations/text_embedding/sagemaker-endpoint).

    from langchain.embeddings import SagemakerEndpointEmbeddingsfrom langchain.llms.sagemaker_endpoint import ContentHandlerBase