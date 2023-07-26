Multion Toolkit
===============

This notebook walks you through connecting LangChain to the MultiOn Client in your browser

To use this toolkit, you will need to add MultiOn Extension to your browser as explained in the [MultiOn for Chrome](https://multion.notion.site/Download-MultiOn-ddddcfe719f94ab182107ca2612c07a5).

    pip install --upgrade multion > /dev/null

MultiOn Setup[](#multion-setup "Direct link to MultiOn Setup")
---------------------------------------------------------------

Login to establish connection with your extension.

    # Authorize connection to your Browser extentionimport multion multion.login()

Use Multion Toolkit within an Agent[](#use-multion-toolkit-within-an-agent "Direct link to Use Multion Toolkit within an Agent")
---------------------------------------------------------------------------------------------------------------------------------

    from langchain.agents.agent_toolkits import create_multion_agentfrom langchain.tools.multion.tool import MultionClientToolfrom langchain.agents.agent_types import AgentTypefrom langchain.chat_models import ChatOpenAI

    agent_executor = create_multion_agent(    llm=ChatOpenAI(temperature=0),    tool=MultionClientTool(),    agent_type=AgentType.OPENAI_FUNCTIONS,    verbose=True)

    agent.run("show me the weather today")

    agent.run(    "Tweet about Elon Musk")