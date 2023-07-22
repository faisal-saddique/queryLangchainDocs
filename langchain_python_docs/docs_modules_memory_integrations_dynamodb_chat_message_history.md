Dynamodb Chat Message History
=============================

This notebook goes over how to use Dynamodb to store chat message history.

First make sure you have correctly configured the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html). Then make sure you have installed boto3.

Next, create the DynamoDB Table where we will be storing messages:

    import boto3# Get the service resource.dynamodb = boto3.resource("dynamodb")# Create the DynamoDB table.table = dynamodb.create_table(    TableName="SessionTable",    KeySchema=[{"AttributeName": "SessionId", "KeyType": "HASH"}],    AttributeDefinitions=[{"AttributeName": "SessionId", "AttributeType": "S"}],    BillingMode="PAY_PER_REQUEST",)# Wait until the table exists.table.meta.client.get_waiter("table_exists").wait(TableName="SessionTable")# Print out some data about the table.print(table.item_count)

        0

DynamoDBChatMessageHistory[​](#dynamodbchatmessagehistory "Direct link to DynamoDBChatMessageHistory")
------------------------------------------------------------------------------------------------------

    from langchain.memory.chat_message_histories import DynamoDBChatMessageHistoryhistory = DynamoDBChatMessageHistory(table_name="SessionTable", session_id="0")history.add_user_message("hi!")history.add_ai_message("whats up?")

    history.messages

        [HumanMessage(content='hi!', additional_kwargs={}, example=False),     AIMessage(content='whats up?', additional_kwargs={}, example=False)]

DynamoDBChatMessageHistory with Custom Endpoint URL[​](#dynamodbchatmessagehistory-with-custom-endpoint-url "Direct link to DynamoDBChatMessageHistory with Custom Endpoint URL")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes it is useful to specify the URL to the AWS endpoint to connect to. For instance, when you are running locally against [Localstack](https://localstack.cloud/). For those cases you can specify the URL via the `endpoint_url` parameter in the constructor.

    from langchain.memory.chat_message_histories import DynamoDBChatMessageHistoryhistory = DynamoDBChatMessageHistory(    table_name="SessionTable",    session_id="0",    endpoint_url="http://localhost.localstack.cloud:4566",)

Agent with DynamoDB Memory[​](#agent-with-dynamodb-memory "Direct link to Agent with DynamoDB Memory")
------------------------------------------------------------------------------------------------------

    from langchain.agents import Toolfrom langchain.memory import ConversationBufferMemoryfrom langchain.chat_models import ChatOpenAIfrom langchain.agents import initialize_agentfrom langchain.agents import AgentTypefrom langchain.utilities import PythonREPLfrom getpass import getpassmessage_history = DynamoDBChatMessageHistory(table_name="SessionTable", session_id="1")memory = ConversationBufferMemory(    memory_key="chat_history", chat_memory=message_history, return_messages=True)

    python_repl = PythonREPL()# You can create the tool to pass to an agenttools = [    Tool(        name="python_repl",        description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",        func=python_repl.run,    )]

    llm = ChatOpenAI(temperature=0)agent_chain = initialize_agent(    tools,    llm,    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,    verbose=True,    memory=memory,)

    agent_chain.run(input="Hello!")

                > Entering new AgentExecutor chain...    {        "action": "Final Answer",        "action_input": "Hello! How can I assist you today?"    }        > Finished chain.    'Hello! How can I assist you today?'

    agent_chain.run(input="Who owns Twitter?")

                > Entering new AgentExecutor chain...    {        "action": "python_repl",        "action_input": "import requests\nfrom bs4 import BeautifulSoup\n\nurl = 'https://en.wikipedia.org/wiki/Twitter'\nresponse = requests.get(url)\nsoup = BeautifulSoup(response.content, 'html.parser')\nowner = soup.find('th', text='Owner').find_next_sibling('td').text.strip()\nprint(owner)"    }    Observation: X Corp. (2023–present)Twitter, Inc. (2006–2023)        Thought:{        "action": "Final Answer",        "action_input": "X Corp. (2023–present)Twitter, Inc. (2006–2023)"    }        > Finished chain.    'X Corp. (2023–present)Twitter, Inc. (2006–2023)'

    agent_chain.run(input="My name is Bob.")

                > Entering new AgentExecutor chain...    {        "action": "Final Answer",        "action_input": "Hello Bob! How can I assist you today?"    }        > Finished chain.    'Hello Bob! How can I assist you today?'

    agent_chain.run(input="Who am I?")

                > Entering new AgentExecutor chain...    {        "action": "Final Answer",        "action_input": "Your name is Bob."    }        > Finished chain.    'Your name is Bob.'