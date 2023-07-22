logging\_tracing\_portkey
=========================

Log, Trace, and Monitor Langchain LLM Calls
===========================================

When building apps or agents using Langchain, you end up making multiple API calls to fulfill a single user request. However, these requests are not chained when you want to analyse them. With [**Portkey**](/docs/ecosystem/integrations/portkey), all the embeddings, completion, and other requests from a single user request will get logged and traced to a common ID, enabling you to gain full visibility of user interactions.

This notebook serves as a step-by-step guide on how to integrate and use Portkey in your Langchain app.

First, let's import Portkey, OpenAI, and Agent tools

    import osfrom langchain.agents import AgentType, initialize_agent, load_toolsfrom langchain.llms import OpenAIfrom langchain.utilities import Portkey

Paste your OpenAI API key below. [(You can find it here)](https://platform.openai.com/account/api-keys)

    os.environ["OPENAI_API_KEY"] = "<OPENAI_API_KEY>"

Get Portkey API Key[​](#get-portkey-api-key "Direct link to Get Portkey API Key")
---------------------------------------------------------------------------------

1.  Sign up for [Portkey here](https://app.portkey.ai/login)
2.  On your [dashboard](https://app.portkey.ai/), click on the profile icon on the top left, then click on "Copy API Key"
3.  Paste it below

    PORTKEY_API_KEY = "<PORTKEY_API_KEY>"  # Paste your Portkey API Key here

Set Trace ID[​](#set-trace-id "Direct link to Set Trace ID")
------------------------------------------------------------

1.  Set the trace id for your request below
2.  The Trace ID can be common for all API calls originating from a single request

    TRACE_ID = "portkey_langchain_demo"  # Set trace id here

Generate Portkey Headers[​](#generate-portkey-headers "Direct link to Generate Portkey Headers")
------------------------------------------------------------------------------------------------

    headers = Portkey.Config(    api_key=PORTKEY_API_KEY,    trace_id=TRACE_ID,)

Run your agent as usual. The **only** change is that we will **include the above headers** in the request now.

    llm = OpenAI(temperature=0, headers=headers)tools = load_tools(["serpapi", "llm-math"], llm=llm)agent = initialize_agent(    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)# Let's test it out!agent.run(    "What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?")

How Logging & Tracing Works on Portkey[​](#how-logging--tracing-works-on-portkey "Direct link to How Logging & Tracing Works on Portkey")
-----------------------------------------------------------------------------------------------------------------------------------------

**Logging**

*   Sending your request through Portkey ensures that all of the requests are logged by default
*   Each request log contains `timestamp`, `model name`, `total cost`, `request time`, `request json`, `response json`, and additional Portkey features

**Tracing**

*   Trace id is passed along with each request and is visibe on the logs on Portkey dashboard
*   You can also set a **distinct trace id** for each request if you want
*   You can append user feedback to a trace id as well. [More info on this here](https://docs.portkey.ai/key-features/feedback-api)

Advanced LLMOps Features - Caching, Tagging, Retries[​](#advanced-llmops-features---caching-tagging-retries "Direct link to Advanced LLMOps Features - Caching, Tagging, Retries")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to logging and tracing, Portkey provides more features that add production capabilities to your existing workflows:

**Caching**

Respond to previously served customers queries from cache instead of sending them again to OpenAI. Match exact strings OR semantically similar strings. Cache can save costs and reduce latencies by 20x.

**Retries**

Automatically reprocess any unsuccessful API requests **`upto 5`** times. Uses an **`exponential backoff`** strategy, which spaces out retry attempts to prevent network overload.

Feature

Config Key

Value (Type)

[🔁 Automatic Retries](https://docs.portkey.ai/key-features/automatic-retries)

`retry_count`

`integer` \[1,2,3,4,5\]

[🧠 Enabling Cache](https://docs.portkey.ai/key-features/request-caching)

`cache`

`simple` OR `semantic`

**Tagging**

Track and audit ach user interaction in high detail with predefined tags.

Tag

Config Key

Value (Type)

User Tag

`user`

`string`

Organisation Tag

`organisation`

`string`

Environment Tag

`environment`

`string`

Prompt Tag (version/id/string)

`prompt`

`string`

Code Example With All Features[​](#code-example-with-all-features "Direct link to Code Example With All Features")
------------------------------------------------------------------------------------------------------------------

    headers = Portkey.Config(    # Mandatory    api_key="<PORTKEY_API_KEY>",    # Cache Options    cache="semantic",    cache_force_refresh="True",    cache_age=1729,    # Advanced    retry_count=5,    trace_id="langchain_agent",    # Metadata    environment="production",    user="john",    organisation="acme",    prompt="Frost",)llm = OpenAI(temperature=0.9, headers=headers)print(llm("Two roads diverged in the yellow woods"))