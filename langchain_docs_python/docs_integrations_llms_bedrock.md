Bedrock
=======

[Amazon Bedrock](https://aws.amazon.com/bedrock/) is a fully managed service that makes FMs from leading AI startups and Amazon available via an API, so you can choose from a wide range of FMs to find the model that is best suited for your use case

    %pip install boto3

    from langchain.llms.bedrock import Bedrockllm = Bedrock(    credentials_profile_name="bedrock-admin",    model_id="amazon.titan-tg1-large",    endpoint_url="custom_endpoint_url",)

### Using in a conversation chain[](#using-in-a-conversation-chain "Direct link to Using in a conversation chain")

    from langchain.chains import ConversationChainfrom langchain.memory import ConversationBufferMemoryconversation = ConversationChain(    llm=llm, verbose=True, memory=ConversationBufferMemory())conversation.predict(input="Hi there!")