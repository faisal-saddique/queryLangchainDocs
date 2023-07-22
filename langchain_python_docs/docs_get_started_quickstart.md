Quickstart
==========

Installation[​](#installation "Direct link to Installation")
------------------------------------------------------------

To install LangChain run:

*   Pip
*   Conda

    pip install langchain

    conda install langchain -c conda-forge

For more details, see our [Installation guide](/docs/get_started/installation.html).

Environment setup[​](#environment-setup "Direct link to Environment setup")
---------------------------------------------------------------------------

Using LangChain will usually require integrations with one or more model providers, data stores, APIs, etc. For this example, we'll use OpenAI's model APIs.

First we'll need to install their Python package:

    pip install openai

Accessing the API requires an API key, which you can get by creating an account and heading [here](https://platform.openai.com/account/api-keys). Once we have a key we'll want to set it as an environment variable by running:

    export OPENAI_API_KEY="..."

If you'd prefer not to set an environment variable you can pass the key in directly via the `openai_api_key` named parameter when initiating the OpenAI LLM class:

    from langchain.llms import OpenAIllm = OpenAI(openai_api_key="...")

Building an application[​](#building-an-application "Direct link to Building an application")
---------------------------------------------------------------------------------------------

Now we can start building our language model application. LangChain provides many modules that can be used to build language model applications. Modules can be used as stand-alones in simple applications and they can be combined for more complex use cases.

LLMs[​](#llms "Direct link to LLMs")
------------------------------------

#### Get predictions from a language model[​](#get-predictions-from-a-language-model "Direct link to Get predictions from a language model")

The basic building block of LangChain is the LLM, which takes in text and generates more text.

As an example, suppose we're building an application that generates a company name based on a company description. In order to do this, we need to initialize an OpenAI model wrapper. In this case, since we want the outputs to be MORE random, we'll initialize our model with a HIGH temperature.

    from langchain.llms import OpenAIllm = OpenAI(temperature=0.9)

And now we can pass in text and get predictions!

    llm.predict("What would be a good company name for a company that makes colorful socks?")# >> Feetful of Fun

Chat models[​](#chat-models "Direct link to Chat models")
---------------------------------------------------------

Chat models are a variation on language models. While chat models use language models under the hood, the interface they expose is a bit different: rather than expose a "text in, text out" API, they expose an interface where "chat messages" are the inputs and outputs.

You can get chat completions by passing one or more messages to the chat model. The response will be a message. The types of messages currently supported in LangChain are `AIMessage`, `HumanMessage`, `SystemMessage`, and `ChatMessage` -- `ChatMessage` takes in an arbitrary role parameter. Most of the time, you'll just be dealing with `HumanMessage`, `AIMessage`, and `SystemMessage`.

    from langchain.chat_models import ChatOpenAIfrom langchain.schema import (    AIMessage,    HumanMessage,    SystemMessage)chat = ChatOpenAI(temperature=0)chat.predict_messages([HumanMessage(content="Translate this sentence from English to French. I love programming.")])# >> AIMessage(content="J'aime programmer.", additional_kwargs={})

It is useful to understand how chat models are different from a normal LLM, but it can often be handy to just be able to treat them the same. LangChain makes that easy by also exposing an interface through which you can interact with a chat model as you would a normal LLM. You can access this through the `predict` interface.

    chat.predict("Translate this sentence from English to French. I love programming.")# >> J'aime programmer

Prompt templates[​](#prompt-templates "Direct link to Prompt templates")
------------------------------------------------------------------------

Most LLM applications do not pass user input directly into an LLM. Usually they will add the user input to a larger piece of text, called a prompt template, that provides additional context on the specific task at hand.

In the previous example, the text we passed to the model contained instructions to generate a company name. For our application, it'd be great if the user only had to provide the description of a company/product, without having to worry about giving the model instructions.

*   LLMs
*   Chat models

With PromptTemplates this is easy! In this case our template would be very simple:

    from langchain.prompts import PromptTemplateprompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")prompt.format(product="colorful socks")

    What is a good name for a company that makes colorful socks?

Similar to LLMs, you can make use of templating by using a `MessagePromptTemplate`. You can build a `ChatPromptTemplate` from one or more `MessagePromptTemplate`s. You can use `ChatPromptTemplate`'s `format_messages` method to generate the formatted messages.

Because this is generating a list of messages, it is slightly more complex than the normal prompt template which is generating only a string. Please see the detailed guides on prompts to understand more options available to you here.

    from langchain.prompts.chat import (    ChatPromptTemplate,    SystemMessagePromptTemplate,    HumanMessagePromptTemplate,)template = "You are a helpful assistant that translates {input_language} to {output_language}."system_message_prompt = SystemMessagePromptTemplate.from_template(template)human_template = "{text}"human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")

    [    SystemMessage(content="You are a helpful assistant that translates English to French.", additional_kwargs={}),    HumanMessage(content="I love programming.")]

Chains[​](#chains "Direct link to Chains")
------------------------------------------

Now that we've got a model and a prompt template, we'll want to combine the two. Chains give us a way to link (or chain) together multiple primitives, like models, prompts, and other chains.

*   LLMs
*   Chat models

The simplest and most common type of chain is an LLMChain, which passes an input first to a PromptTemplate and then to an LLM. We can construct an LLM chain from our existing model and prompt template.

Using this we can replace

    llm.predict("What would be a good company name for a company that makes colorful socks?")

with

    from langchain.chains import LLMChainchain = LLMChain(llm=llm, prompt=prompt)chain.run("colorful socks")

    Feetful of Fun

There we go, our first chain! Understanding how this simple chain works will set you up well for working with more complex chains.

The `LLMChain` can be used with chat models as well:

    from langchain import LLMChainfrom langchain.chat_models import ChatOpenAIfrom langchain.prompts.chat import (    ChatPromptTemplate,    SystemMessagePromptTemplate,    HumanMessagePromptTemplate,)chat = ChatOpenAI(temperature=0)template = "You are a helpful assistant that translates {input_language} to {output_language}."system_message_prompt = SystemMessagePromptTemplate.from_template(template)human_template = "{text}"human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])chain = LLMChain(llm=chat, prompt=chat_prompt)chain.run(input_language="English", output_language="French", text="I love programming.")

    J'aime programmer.

Agents[​](#agents "Direct link to Agents")
------------------------------------------

Our first chain ran a pre-determined sequence of steps. To handle complex workflows, we need to be able to dynamically choose actions based on inputs.

Agents do just this: they use a language model to determine which actions to take and in what order. Agents are given access to tools, and they repeatedly choose a tool, run the tool, and observe the output until they come up with a final answer.

To load an agent, you need to choose a(n):

*   LLM/Chat model: The language model powering the agent.
*   Tool(s): A function that performs a specific duty. This can be things like: Google Search, Database lookup, Python REPL, other chains. For a list of predefined tools and their specifications, see the [Tools documentation](/docs/modules/agents/tools/).
*   Agent name: A string that references a supported agent class. An agent class is largely parameterized by the prompt the language model uses to determine which action to take. Because this notebook focuses on the simplest, highest level API, this only covers using the standard supported agents. If you want to implement a custom agent, see [here](/docs/modules/agents/how_to/custom_agent.html). For a list of supported agents and their specifications, see [here](/docs/modules/agents/agent_types/).

For this example, we'll be using SerpAPI to query a search engine.

You'll need to install the SerpAPI Python package:

    pip install google-search-results

And set the `SERPAPI_API_KEY` environment variable.

*   LLMs
*   Chat models

    from langchain.agents import AgentType, initialize_agent, load_toolsfrom langchain.llms import OpenAI# The language model we're going to use to control the agent.llm = OpenAI(temperature=0)# The tools we'll give the Agent access to. Note that the 'llm-math' tool uses an LLM, so we need to pass that in.tools = load_tools(["serpapi", "llm-math"], llm=llm)# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)# Let's test it out!agent.run("What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?")

    > Entering new AgentExecutor chain...Thought: I need to find the temperature first, then use the calculator to raise it to the .023 power.Action: SearchAction Input: "High temperature in SF yesterday"Observation: San Francisco Temperature Yesterday. Maximum temperature yesterday: 57 °F (at 1:56 pm) Minimum temperature yesterday: 49 °F (at 1:56 am) Average temperature ...Thought: I now have the temperature, so I can use the calculator to raise it to the .023 power.Action: CalculatorAction Input: 57^.023Observation: Answer: 1.0974509573251117Thought: I now know the final answerFinal Answer: The high temperature in SF yesterday in Fahrenheit raised to the .023 power is 1.0974509573251117.> Finished chain.

    The high temperature in SF yesterday in Fahrenheit raised to the .023 power is 1.0974509573251117.

Agents can also be used with chat models, you can initialize one using `AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION` as the agent type.

    from langchain.agents import load_toolsfrom langchain.agents import initialize_agentfrom langchain.agents import AgentTypefrom langchain.chat_models import ChatOpenAIfrom langchain.llms import OpenAI# First, let's load the language model we're going to use to control the agent.chat = ChatOpenAI(temperature=0)# Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.llm = OpenAI(temperature=0)tools = load_tools(["serpapi", "llm-math"], llm=llm)# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.agent = initialize_agent(tools, chat, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)# Now let's test it out!agent.run("Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?")

    > Entering new AgentExecutor chain...Thought: I need to use a search engine to find Olivia Wilde's boyfriend and a calculator to raise his age to the 0.23 power.Action:{    "action": "Search",    "action_input": "Olivia Wilde boyfriend"}Observation: Sudeikis and Wilde's relationship ended in November 2020. Wilde was publicly served with court documents regarding child custody while she was presenting Don't Worry Darling at CinemaCon 2022. In January 2021, Wilde began dating singer Harry Styles after meeting during the filming of Don't Worry Darling.Thought:I need to use a search engine to find Harry Styles' current age.Action:{    "action": "Search",    "action_input": "Harry Styles age"}Observation: 29 yearsThought:Now I need to calculate 29 raised to the 0.23 power.Action:{    "action": "Calculator",    "action_input": "29^0.23"}Observation: Answer: 2.169459462491557Thought:I now know the final answer.Final Answer: 2.169459462491557> Finished chain.'2.169459462491557'

Memory[​](#memory "Direct link to Memory")
------------------------------------------

The chains and agents we've looked at so far have been stateless, but for many applications it's necessary to reference past interactions. This is clearly the case with a chatbot for example, where you want it to understand new messages in the context of past messages.

The Memory module gives you a way to maintain application state. The base Memory interface is simple: it lets you update state given the latest run inputs and outputs and it lets you modify (or contextualize) the next input using the stored state.

There are a number of built-in memory systems. The simplest of these is a buffer memory which just prepends the last few inputs/outputs to the current input - we will use this in the example below.

*   LLMs
*   Chat models

    from langchain import OpenAI, ConversationChainllm = OpenAI(temperature=0)conversation = ConversationChain(llm=llm, verbose=True)conversation.run("Hi there!")

here's what's going on under the hood

    > Entering new chain...Prompt after formatting:The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.Current conversation:Human: Hi there!AI:> Finished chain.>> 'Hello! How are you today?'

Now if we run the chain again

    conversation.run("I'm doing well! Just having a conversation with an AI.")

we'll see that the full prompt that's passed to the model contains the input and output of our first interaction, along with our latest input

    > Entering new chain...Prompt after formatting:The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.Current conversation:Human: Hi there!AI:  Hello! How are you today?Human: I'm doing well! Just having a conversation with an AI.AI:> Finished chain.>> "That's great! What would you like to talk about?"

You can use Memory with chains and agents initialized with chat models. The main difference between this and Memory for LLMs is that rather than trying to condense all previous messages into a string, we can keep them as their own unique memory object.

    from langchain.prompts import (    ChatPromptTemplate,    MessagesPlaceholder,    SystemMessagePromptTemplate,    HumanMessagePromptTemplate)from langchain.chains import ConversationChainfrom langchain.chat_models import ChatOpenAIfrom langchain.memory import ConversationBufferMemoryprompt = ChatPromptTemplate.from_messages([    SystemMessagePromptTemplate.from_template(        "The following is a friendly conversation between a human and an AI. The AI is talkative and "        "provides lots of specific details from its context. If the AI does not know the answer to a "        "question, it truthfully says it does not know."    ),    MessagesPlaceholder(variable_name="history"),    HumanMessagePromptTemplate.from_template("{input}")])llm = ChatOpenAI(temperature=0)memory = ConversationBufferMemory(return_messages=True)conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)conversation.predict(input="Hi there!")

    Hello! How can I assist you today?

    conversation.predict(input="I'm doing well! Just having a conversation with an AI.")

    That sounds like fun! I'm happy to chat with you. Is there anything specific you'd like to talk about?

    conversation.predict(input="Tell me about yourself.")

    Sure! I am an AI language model created by OpenAI. I was trained on a large dataset of text from the internet, which allows me to understand and generate human-like language. I can answer questions, provide information, and even have conversations like this one. Is there anything else you'd like to know about me?