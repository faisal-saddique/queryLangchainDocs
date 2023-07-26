Azure
=====

This notebook goes over how to connect to an Azure hosted OpenAI endpoint

    from langchain.chat_models import AzureChatOpenAIfrom langchain.schema import HumanMessage

    BASE_URL = "https://${TODO}.openai.azure.com"API_KEY = "..."DEPLOYMENT_NAME = "chat"model = AzureChatOpenAI(    openai_api_base=BASE_URL,    openai_api_version="2023-05-15",    deployment_name=DEPLOYMENT_NAME,    openai_api_key=API_KEY,    openai_api_type="azure",)

    model(    [        HumanMessage(            content="Translate this sentence from English to French. I love programming."        )    ])

        AIMessage(content="\n\nJ'aime programmer.", additional_kwargs={})