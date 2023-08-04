Custom LLM Agent (with a ChatModel)
===================================

This notebook goes through how to create your own custom agent based on a chat model.

An LLM chat agent consists of three parts:

*   PromptTemplate: This is the prompt template that can be used to instruct the language model on what to do
*   ChatModel: This is the language model that powers the agent
*   `stop` sequence: Instructs the LLM to stop generating as soon as this string is found
*   OutputParser: This determines how to parse the LLMOutput into an AgentAction or AgentFinish object

The LLMAgent is used in an AgentExecutor. This AgentExecutor can largely be thought of as a loop that:

1.  Passes user input and any previous steps to the Agent (in this case, the LLMAgent)
2.  If the Agent returns an `AgentFinish`, then return that directly to the user
3.  If the Agent returns an `AgentAction`, then use that to call a tool and get an `Observation`
4.  Repeat, passing the `AgentAction` and `Observation` back to the Agent until an `AgentFinish` is emitted.

`AgentAction` is a response that consists of `action` and `action_input`. `action` refers to which tool to use, and `action_input` refers to the input to that tool. `log` can also be provided as more context (that can be used for logging, tracing, etc).

`AgentFinish` is a response that contains the final message to be sent back to the user. This should be used to end an agent run.

    import {  AgentActionOutputParser,  AgentExecutor,  LLMSingleActionAgent,} from "langchain/agents";import { LLMChain } from "langchain/chains";import { ChatOpenAI } from "langchain/chat_models/openai";import {  BaseChatPromptTemplate,  BasePromptTemplate,  SerializedBasePromptTemplate,  renderTemplate,} from "langchain/prompts";import {  AgentAction,  AgentFinish,  AgentStep,  BaseMessage,  HumanMessage,  InputValues,  PartialValues,} from "langchain/schema";import { SerpAPI, Tool } from "langchain/tools";import { Calculator } from "langchain/tools/calculator";const PREFIX = `Answer the following questions as best you can. You have access to the following tools:`;const formatInstructions = (  toolNames: string) => `Use the following format in your response:Question: the input question you must answerThought: you should always think about what to doAction: the action to take, should be one of [${toolNames}]Action Input: the input to the actionObservation: the result of the action... (this Thought/Action/Action Input/Observation can repeat N times)Thought: I now know the final answerFinal Answer: the final answer to the original input question`;const SUFFIX = `Begin!Question: {input}Thought:{agent_scratchpad}`;class CustomPromptTemplate extends BaseChatPromptTemplate {  tools: Tool[];  constructor(args: { tools: Tool[]; inputVariables: string[] }) {    super({ inputVariables: args.inputVariables });    this.tools = args.tools;  }  _getPromptType(): string {    throw new Error("Not implemented");  }  async formatMessages(values: InputValues): Promise<BaseMessage[]> {    /** Construct the final template */    const toolStrings = this.tools      .map((tool) => `${tool.name}: ${tool.description}`)      .join("\n");    const toolNames = this.tools.map((tool) => tool.name).join("\n");    const instructions = formatInstructions(toolNames);    const template = [PREFIX, toolStrings, instructions, SUFFIX].join("\n\n");    /** Construct the agent_scratchpad */    const intermediateSteps = values.intermediate_steps as AgentStep[];    const agentScratchpad = intermediateSteps.reduce(      (thoughts, { action, observation }) =>        thoughts +        [action.log, `\nObservation: ${observation}`, "Thought:"].join("\n"),      ""    );    const newInput = { agent_scratchpad: agentScratchpad, ...values };    /** Format the template. */    const formatted = renderTemplate(template, "f-string", newInput);    return [new HumanMessage(formatted)];  }  partial(_values: PartialValues): Promise<BasePromptTemplate> {    throw new Error("Not implemented");  }  serialize(): SerializedBasePromptTemplate {    throw new Error("Not implemented");  }}class CustomOutputParser extends AgentActionOutputParser {  lc_namespace = ["langchain", "agents", "custom_llm_agent_chat"];  async parse(text: string): Promise<AgentAction | AgentFinish> {    if (text.includes("Final Answer:")) {      const parts = text.split("Final Answer:");      const input = parts[parts.length - 1].trim();      const finalAnswers = { output: input };      return { log: text, returnValues: finalAnswers };    }    const match = /Action: (.*)\nAction Input: (.*)/s.exec(text);    if (!match) {      throw new Error(`Could not parse LLM output: ${text}`);    }    return {      tool: match[1].trim(),      toolInput: match[2].trim().replace(/^"+|"+$/g, ""),      log: text,    };  }  getFormatInstructions(): string {    throw new Error("Not implemented");  }}export const run = async () => {  const model = new ChatOpenAI({ temperature: 0 });  const tools = [    new SerpAPI(process.env.SERPAPI_API_KEY, {      location: "Austin,Texas,United States",      hl: "en",      gl: "us",    }),    new Calculator(),  ];  const llmChain = new LLMChain({    prompt: new CustomPromptTemplate({      tools,      inputVariables: ["input", "agent_scratchpad"],    }),    llm: model,  });  const agent = new LLMSingleActionAgent({    llmChain,    outputParser: new CustomOutputParser(),    stop: ["\nObservation"],  });  const executor = new AgentExecutor({    agent,    tools,  });  console.log("Loaded agent.");  const input = `Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?`;  console.log(`Executing with input "${input}"...`);  const result = await executor.call({ input });  console.log(`Got output ${result.output}`);};run();

#### API Reference:

*   [AgentActionOutputParser](/docs/api/agents/classes/AgentActionOutputParser) from `langchain/agents`
*   [AgentExecutor](/docs/api/agents/classes/AgentExecutor) from `langchain/agents`
*   [LLMSingleActionAgent](/docs/api/agents/classes/LLMSingleActionAgent) from `langchain/agents`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate) from `langchain/prompts`
*   [BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate) from `langchain/prompts`
*   [SerializedBasePromptTemplate](/docs/api/prompts/types/SerializedBasePromptTemplate) from `langchain/prompts`
*   [renderTemplate](/docs/api/prompts/functions/renderTemplate) from `langchain/prompts`
*   [AgentAction](/docs/api/schema/types/AgentAction) from `langchain/schema`
*   [AgentFinish](/docs/api/schema/types/AgentFinish) from `langchain/schema`
*   [AgentStep](/docs/api/schema/types/AgentStep) from `langchain/schema`
*   [BaseMessage](/docs/api/schema/classes/BaseMessage) from `langchain/schema`
*   [HumanMessage](/docs/api/schema/classes/HumanMessage) from `langchain/schema`
*   [InputValues](/docs/api/schema/types/InputValues) from `langchain/schema`
*   [PartialValues](/docs/api/schema/types/PartialValues) from `langchain/schema`
*   [SerpAPI](/docs/api/tools/classes/SerpAPI) from `langchain/tools`
*   [Tool](/docs/api/tools/classes/Tool) from `langchain/tools`
*   [Calculator](/docs/api/tools_calculator/classes/Calculator) from `langchain/tools/calculator`