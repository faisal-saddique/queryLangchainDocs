Lemon AI NLP Workflow Automation
================================

\\ Full docs are available at: [https://github.com/felixbrock/lemonai-py-client](https://github.com/felixbrock/lemonai-py-client)

**Lemon AI helps you build powerful AI assistants in minutes and automate workflows by allowing for accurate and reliable read and write operations in tools like Airtable, Hubspot, Discord, Notion, Slack and Github.**

Most connectors available today are focused on read-only operations, limiting the potential of LLMs. Agents, on the other hand, have a tendency to hallucinate from time to time due to missing context or instructions.

With Lemon AI, it is possible to give your agents access to well-defined APIs for reliable read and write operations. In addition, Lemon AI functions allow you to further reduce the risk of hallucinations by providing a way to statically define workflows that the model can rely on in case of uncertainty.

Quick Start[](#quick-start "Direct link to Quick Start")
---------------------------------------------------------

The following quick start demonstrates how to use Lemon AI in combination with Agents to automate workflows that involve interaction with internal tooling.

### 1\. Install Lemon AI[](#1-install-lemon-ai "Direct link to 1. Install Lemon AI")

Requires Python 3.8.1 and above.

To use Lemon AI in your Python project run `pip install lemonai`

This will install the corresponding Lemon AI client which you can then import into your script.

The tool uses Python packages langchain and loguru. In case of any installation errors with Lemon AI, install both packages first and then install the Lemon AI package.

### 2\. Launch the Server[](#2-launch-the-server "Direct link to 2. Launch the Server")

The interaction of your agents and all tools provided by Lemon AI is handled by the [Lemon AI Server](https://github.com/felixbrock/lemonai-server). To use Lemon AI you need to run the server on your local machine so the Lemon AI Python client can connect to it.

### 3\. Use Lemon AI with Langchain[](#3-use-lemon-ai-with-langchain "Direct link to 3. Use Lemon AI with Langchain")

Lemon AI automatically solves given tasks by finding the right combination of relevant tools or uses Lemon AI Functions as an alternative. The following example demonstrates how to retrieve a user from Hackernews and write it to a table in Airtable:

#### (Optional) Define your Lemon AI Functions[](#optional-define-your-lemon-ai-functions "Direct link to (Optional) Define your Lemon AI Functions")

Similar to [OpenAI functions](https://openai.com/blog/function-calling-and-other-api-updates), Lemon AI provides the option to define workflows as reusable functions. These functions can be defined for use cases where it is especially important to move as close as possible to near-deterministic behavior. Specific workflows can be defined in a separate lemonai.json:

    [  {    "name": "Hackernews Airtable User Workflow",    "description": "retrieves user data from Hackernews and appends it to a table in Airtable",    "tools": ["hackernews-get-user", "airtable-append-data"]  }]

Your model will have access to these functions and will prefer them over self-selecting tools to solve a given task. All you have to do is to let the agent know that it should use a given function by including the function name in the prompt.

#### Include Lemon AI in your Langchain project[](#include-lemon-ai-in-your-langchain-project "Direct link to Include Lemon AI in your Langchain project")

    import osfrom lemonai import execute_workflowfrom langchain import OpenAI

#### Load API Keys and Access Tokens[](#load-api-keys-and-access-tokens "Direct link to Load API Keys and Access Tokens")

To use tools that require authentication, you have to store the corresponding access credentials in your environment in the format "{tool name}\_{authentication string}" where the authentication string is one of \["API\_KEY", "SECRET\_KEY", "SUBSCRIPTION\_KEY", "ACCESS\_KEY"\] for API keys or \["ACCESS\_TOKEN", "SECRET\_TOKEN"\] for authentication tokens. Examples are "OPENAI\_API\_KEY", "BING\_SUBSCRIPTION\_KEY", "AIRTABLE\_ACCESS\_TOKEN".

    """ Load all relevant API Keys and Access Tokens into your environment variables """os.environ["OPENAI_API_KEY"] = "*INSERT OPENAI API KEY HERE*"os.environ["AIRTABLE_ACCESS_TOKEN"] = "*INSERT AIRTABLE TOKEN HERE*"

    hackernews_username = "*INSERT HACKERNEWS USERNAME HERE*"airtable_base_id = "*INSERT BASE ID HERE*"airtable_table_id = "*INSERT TABLE ID HERE*"""" Define your instruction to be given to your LLM """prompt = f"""Read information from Hackernews for user {hackernews_username} and then write the results toAirtable (baseId: {airtable_base_id}, tableId: {airtable_table_id}). Only write the fields "username", "karma"and "created_at_i". Please make sure that Airtable does NOT automatically convert the field types.""""""Use the Lemon AI execute_workflow wrapper to run your Langchain agent in combination with Lemon AI  """model = OpenAI(temperature=0)execute_workflow(llm=model, prompt_string=prompt)

### 4\. Gain transparency on your Agent's decision making[](#4-gain-transparency-on-your-agents-decision-making "Direct link to 4. Gain transparency on your Agent's decision making")

To gain transparency on how your Agent interacts with Lemon AI tools to solve a given task, all decisions made, tools used and operations performed are written to a local `lemonai.log` file. Every time your LLM agent is interacting with the Lemon AI tool stack a corresponding log entry is created.

    2023-06-26T11:50:27.708785+0100 - b5f91c59-8487-45c2-800a-156eac0c7dae - hackernews-get-user2023-06-26T11:50:39.624035+0100 - b5f91c59-8487-45c2-800a-156eac0c7dae - airtable-append-data2023-06-26T11:58:32.925228+0100 - 5efe603c-9898-4143-b99a-55b50007ed9d - hackernews-get-user2023-06-26T11:58:43.988788+0100 - 5efe603c-9898-4143-b99a-55b50007ed9d - airtable-append-data

By using the [Lemon AI Analytics Tool](https://github.com/felixbrock/lemonai-analytics) you can easily gain a better understanding of how frequently and in which order tools are used. As a result, you can identify weak spots in your agent’s decision-making capabilities and move to a more deterministic behavior by defining Lemon AI functions.