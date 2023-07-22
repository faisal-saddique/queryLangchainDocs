MLflow AI Gateway
=================

The MLflow AI Gateway service is a powerful tool designed to streamline the usage and management of various large language model (LLM) providers, such as OpenAI and Anthropic, within an organization. It offers a high-level interface that simplifies the interaction with these services by providing a unified endpoint to handle specific LLM related requests. See [the MLflow AI Gateway documentation](https://mlflow.org/docs/latest/gateway/index.html) for more details.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

Install `mlflow` with MLflow AI Gateway dependencies:

    pip install 'mlflow[gateway]'

Set the OpenAI API key as an environment variable:

    export OPENAI_API_KEY=...

Create a configuration file:

    routes:  - name: completions    route_type: llm/v1/completions    model:      provider: openai      name: text-davinci-003      config:        openai_api_key: $OPENAI_API_KEY  - name: embeddings    route_type: llm/v1/embeddings    model:      provider: openai      name: text-embedding-ada-002      config:        openai_api_key: $OPENAI_API_KEY

Start the Gateway server:

    mlflow gateway start --config-path /path/to/config.yaml

Completions Example[​](#completions-example "Direct link to Completions Example")
---------------------------------------------------------------------------------

    import mlflowfrom langchain import LLMChain, PromptTemplatefrom langchain.llms import MlflowAIGatewaygateway = MlflowAIGateway(    gateway_uri="http://127.0.0.1:5000",    route="completions",    params={        "temperature": 0.0,        "top_p": 0.1,    },)llm_chain = LLMChain(    llm=gateway,    prompt=PromptTemplate(        input_variables=["adjective"],        template="Tell me a {adjective} joke",    ),)result = llm_chain.run(adjective="funny")print(result)with mlflow.start_run():    model_info = mlflow.langchain.log_model(chain, "model")model = mlflow.pyfunc.load_model(model_info.model_uri)print(model.predict([{"adjective": "funny"}]))

Embeddings Example[​](#embeddings-example "Direct link to Embeddings Example")
------------------------------------------------------------------------------

    from langchain.embeddings import MlflowAIGatewayEmbeddingsembeddings = MlflowAIGatewayEmbeddings(    gateway_uri="http://127.0.0.1:5000",    route="embeddings",)print(embeddings.embed_query("hello"))print(embeddings.embed_documents(["hello"]))

Databricks MLflow AI Gateway[​](#databricks-mlflow-ai-gateway "Direct link to Databricks MLflow AI Gateway")
------------------------------------------------------------------------------------------------------------

Databricks MLflow AI Gateway is in private preview. Please contact a Databricks representative to enroll in the preview.

    from langchain import LLMChain, PromptTemplatefrom langchain.llms import MlflowAIGatewaygateway = MlflowAIGateway(    gateway_uri="databricks",    route="completions",)llm_chain = LLMChain(    llm=gateway,    prompt=PromptTemplate(        input_variables=["adjective"],        template="Tell me a {adjective} joke",    ),)result = llm_chain.run(adjective="funny")print(result)