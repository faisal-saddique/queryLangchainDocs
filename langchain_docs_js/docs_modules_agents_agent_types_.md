Agent types
===========

Action agents[](#action-agents "Direct link to Action agents")
---------------------------------------------------------------

Agents use an LLM to determine which actions to take and in what order. An action can either be using a tool and observing its output, or returning a response to the user. Here are the agents available in LangChain.

### [Zero-shot ReAct](/docs/modules/agents/agent_types/react)[](#zero-shot-react "Direct link to zero-shot-react")

This agent uses the [ReAct](https://arxiv.org/pdf/2205.00445.pdf) framework to determine which tool to use based solely on the tool's description. Any number of tools can be provided. This agent requires that a description is provided for each tool.

**Note**: This is the most general purpose action agent.

### [OpenAI Functions](/docs/modules/agents/agent_types/openai_functions_agent)[](#openai-functions "Direct link to openai-functions")

Certain OpenAI models (like gpt-3.5-turbo-0613 and gpt-4-0613) have been explicitly fine-tuned to detect when a function should to be called and respond with the inputs that should be passed to the function. The OpenAI Functions Agent is designed to work with these models.

### [Conversational](/docs/modules/agents/agent_types/chat_conversation_agent)[](#conversational "Direct link to conversational")

This agent is designed to be used in conversational settings. The prompt is designed to make the agent helpful and conversational. It uses the ReAct framework to decide which tool to use, and uses memory to remember the previous conversation interactions.

[Plan-and-execute agents](/docs/modules/agents/agent_types/plan_and_execute)[](#plan-and-execute-agents "Direct link to plan-and-execute-agents")
--------------------------------------------------------------------------------------------------------------------------------------------------

Plan and execute agents accomplish an objective by first planning what to do, then executing the sub tasks. This idea is largely inspired by [BabyAGI](https://github.com/yoheinakajima/babyagi) and then the ["Plan-and-Solve" paper](https://arxiv.org/abs/2305.04091).