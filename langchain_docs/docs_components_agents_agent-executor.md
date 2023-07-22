Agent Executor
==============

info

[Python Guide](https://python.langchain.com/en/latest/modules/agents/agent_executors.html)

[JS Guide](https://js.langchain.com/docs/modules/agents/exector)

An Agent Executor is an Agent and set of Tools. The agent executor is responsible for calling the agent, getting back and action and action input, calling the tool that the action references with the corresponding input, getting the output of the tool, and then passing all that information back into the Agent to get the next action it should take