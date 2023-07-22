Context
=======

![Context - Product Analytics for AI Chatbots](https://go.getcontext.ai/langchain.png)

[Context](https://getcontext.ai/) provides product analytics for AI chatbots.

Context helps you understand how users are interacting with your AI chat products. Gain critical insights, optimise poor experiences, and minimise brand risks.

In this guide we will show you how to integrate with Context.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

    $ pip install context-python --upgrade

### Getting API Credentials[​](#getting-api-credentials "Direct link to Getting API Credentials")

To get your Context API token:

1.  Go to the settings page within your Context account ([https://go.getcontext.ai/settings](https://go.getcontext.ai/settings)).
2.  Generate a new API Token.
3.  Store this token somewhere secure.

### Setup Context[​](#setup-context "Direct link to Setup Context")

To use the `ContextCallbackHandler`, import the handler from Langchain and instantiate it with your Context API token.

Ensure you have installed the `context-python` package before using the handler.

    import osfrom langchain.callbacks import ContextCallbackHandlertoken = os.environ["CONTEXT_API_TOKEN"]context_callback = ContextCallbackHandler(token)

Usage[​](#usage "Direct link to Usage")
---------------------------------------

### Using the Context callback within a Chat Model[​](#using-the-context-callback-within-a-chat-model "Direct link to Using the Context callback within a Chat Model")

The Context callback handler can be used to directly record transcripts between users and AI assistants.

#### Example[​](#example "Direct link to Example")

    import osfrom langchain.chat_models import ChatOpenAIfrom langchain.schema import (    SystemMessage,    HumanMessage,)from langchain.callbacks import ContextCallbackHandlertoken = os.environ["CONTEXT_API_TOKEN"]chat = ChatOpenAI(    headers={"user_id": "123"}, temperature=0, callbacks=[ContextCallbackHandler(token)])messages = [    SystemMessage(        content="You are a helpful assistant that translates English to French."    ),    HumanMessage(content="I love programming."),]print(chat(messages))

### Using the Context callback within Chains[​](#using-the-context-callback-within-chains "Direct link to Using the Context callback within Chains")

The Context callback handler can also be used to record the inputs and outputs of chains. Note that intermediate steps of the chain are not recorded - only the starting inputs and final outputs.

**Note:** Ensure that you pass the same context object to the chat model and the chain.

Wrong:

>     chat = ChatOpenAI(temperature=0.9, callbacks=[ContextCallbackHandler(token)])chain = LLMChain(llm=chat, prompt=chat_prompt_template, callbacks=[ContextCallbackHandler(token)])

Correct:

>     handler = ContextCallbackHandler(token)chat = ChatOpenAI(temperature=0.9, callbacks=[callback])chain = LLMChain(llm=chat, prompt=chat_prompt_template, callbacks=[callback])

#### Example[​](#example-1 "Direct link to Example")

    import osfrom langchain.chat_models import ChatOpenAIfrom langchain import LLMChainfrom langchain.prompts import PromptTemplatefrom langchain.prompts.chat import (    ChatPromptTemplate,    HumanMessagePromptTemplate,)from langchain.callbacks import ContextCallbackHandlertoken = os.environ["CONTEXT_API_TOKEN"]human_message_prompt = HumanMessagePromptTemplate(    prompt=PromptTemplate(        template="What is a good name for a company that makes {product}?",        input_variables=["product"],    ))chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])callback = ContextCallbackHandler(token)chat = ChatOpenAI(temperature=0.9, callbacks=[callback])chain = LLMChain(llm=chat, prompt=chat_prompt_template, callbacks=[callback])print(chain.run("colorful socks"))