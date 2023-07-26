Tools
=====

info

Head to [Integrations](/docs/integrations/tools/) for documentation on built-in tool integrations.

Tools are interfaces that an agent can use to interact with the world.

Get started[](#get-started "Direct link to Get started")
---------------------------------------------------------

Tools are functions that agents can use to interact with the world. These tools can be generic utilities (e.g. search), other chains, or even other agents.

Currently, tools can be loaded with the following snippet:

    from langchain.agents import load_toolstool_names = [...]tools = load_tools(tool_names)

Some tools (e.g. chains, agents) may require a base LLM to use to initialize them. In that case, you can pass in an LLM as well:

    from langchain.agents import load_toolstool_names = [...]llm = ...tools = load_tools(tool_names, llm=llm)