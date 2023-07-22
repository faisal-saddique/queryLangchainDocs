Plan and execute
================

Plan and execute agents accomplish an objective by first planning what to do, then executing the sub tasks. This idea is largely inspired by [BabyAGI](https://github.com/yoheinakajima/babyagi) and then the ["Plan-and-Solve" paper](https://arxiv.org/abs/2305.04091).

The planning is almost always done by an LLM.

The execution is usually done by a separate agent (equipped with tools).

This agent uses a two step process:

1.  First, the agent uses an LLM to create a plan to answer the query with clear steps.
2.  Once it has a plan, it uses an embedded traditional Action Agent to solve each step.

The idea is that the planning step keeps the LLM more "on track" by breaking up a larger task into simpler subtasks. However, this method requires more individual LLM queries and has higher latency compared to Action Agents.

**Note**: This agent currently only supports Chat Models.

    import { Calculator } from "langchain/tools/calculator";import { SerpAPI } from "langchain/tools";import { ChatOpenAI } from "langchain/chat_models/openai";import { PlanAndExecuteAgentExecutor } from "langchain/experimental/plan_and_execute";const tools = [new Calculator(), new SerpAPI()];const model = new ChatOpenAI({  temperature: 0,  modelName: "gpt-3.5-turbo",  verbose: true,});const executor = PlanAndExecuteAgentExecutor.fromLLMAndTools({  llm: model,  tools,});const result = await executor.call({  input: `Who is the current president of the United States? What is their current age raised to the second power?`,});console.log({ result });

#### API Reference:

*   [Calculator](/docs/api/tools_calculator/classes/Calculator) from `langchain/tools/calculator`
*   [SerpAPI](/docs/api/tools/classes/SerpAPI) from `langchain/tools`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [PlanAndExecuteAgentExecutor](/docs/api/experimental_plan_and_execute/classes/PlanAndExecuteAgentExecutor) from `langchain/experimental/plan_and_execute`