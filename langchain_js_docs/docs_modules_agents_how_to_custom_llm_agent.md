Custom LLM Agent
================

This notebook goes through how to create your own custom LLM agent.

An LLM agent consists of three parts:

*   PromptTemplate: This is the prompt template that can be used to instruct the language model on what to do
*   LLM: This is the language model that powers the agent
*   `stop` sequence: Instructs the LLM to stop generating as soon as this string is found
*   OutputParser: This determines how to parse the LLMOutput into an AgentAction or AgentFinish object

The LLMAgent is used in an AgentExecutor. This AgentExecutor can largely be thought of as a loop that:

1.  Passes user input and any previous steps to the Agent (in this case, the LLMAgent)
2.  If the Agent returns an `AgentFinish`, then return that directly to the user
3.  If the Agent returns an `AgentAction`, then use that to call a tool and get an `Observation`
4.  Repeat, passing the `AgentAction` and `Observation` back to the Agent until an `AgentFinish` is emitted.

`AgentAction` is a response that consists of `action` and `action_input`. `action` refers to which tool to use, and `action_input` refers to the input to that tool. `log` can also be provided as more context (that can be used for logging, tracing, etc).

`AgentFinish` is a response that contains the final message to be sent back to the user. This should be used to end an agent run.

    import {  LLMSingleActionAgent,  AgentActionOutputParser,  AgentExecutor,} from "langchain/agents";import { LLMChain } from "langchain/chains";import { OpenAI } from "langchain/llms/openai";import {  BasePromptTemplate,  BaseStringPromptTemplate,  SerializedBasePromptTemplate,  renderTemplate,} from "langchain/prompts";import {  InputValues,  PartialValues,  AgentStep,  AgentAction,  AgentFinish,} from "langchain/schema";import { SerpAPI, Tool } from "langchain/tools";import { Calculator } from "langchain/tools/calculator";const PREFIX = `Answer the following questions as best you can. You have access to the following tools:`;const formatInstructions = (  toolNames: string) => `Use the following format in your response:Question: the input question you must answerThought: you should always think about what to doAction: the action to take, should be one of [${toolNames}]Action Input: the input to the actionObservation: the result of the action... (this Thought/Action/Action Input/Observation can repeat N times)Thought: I now know the final answerFinal Answer: the final answer to the original input question`;const SUFFIX = `Begin!Question: {input}Thought:{agent_scratchpad}`;class CustomPromptTemplate extends BaseStringPromptTemplate {  tools: Tool[];  constructor(args: { tools: Tool[]; inputVariables: string[] }) {    super({ inputVariables: args.inputVariables });    this.tools = args.tools;  }  _getPromptType(): string {    throw new Error("Not implemented");  }  format(input: InputValues): Promise<string> {    /** Construct the final template */    const toolStrings = this.tools      .map((tool) => `${tool.name}: ${tool.description}`)      .join("\n");    const toolNames = this.tools.map((tool) => tool.name).join("\n");    const instructions = formatInstructions(toolNames);    const template = [PREFIX, toolStrings, instructions, SUFFIX].join("\n\n");    /** Construct the agent_scratchpad */    const intermediateSteps = input.intermediate_steps as AgentStep[];    const agentScratchpad = intermediateSteps.reduce(      (thoughts, { action, observation }) =>        thoughts +        [action.log, `\nObservation: ${observation}`, "Thought:"].join("\n"),      ""    );    const newInput = { agent_scratchpad: agentScratchpad, ...input };    /** Format the template. */    return Promise.resolve(renderTemplate(template, "f-string", newInput));  }  partial(_values: PartialValues): Promise<BasePromptTemplate> {    throw new Error("Not implemented");  }  serialize(): SerializedBasePromptTemplate {    throw new Error("Not implemented");  }}class CustomOutputParser extends AgentActionOutputParser {  lc_namespace = ["langchain", "agents", "custom_llm_agent"];  async parse(text: string): Promise<AgentAction | AgentFinish> {    if (text.includes("Final Answer:")) {      const parts = text.split("Final Answer:");      const input = parts[parts.length - 1].trim();      const finalAnswers = { output: input };      return { log: text, returnValues: finalAnswers };    }    const match = /Action: (.*)\nAction Input: (.*)/s.exec(text);    if (!match) {      throw new Error(`Could not parse LLM output: ${text}`);    }    return {      tool: match[1].trim(),      toolInput: match[2].trim().replace(/^"+|"+$/g, ""),      log: text,    };  }  getFormatInstructions(): string {    throw new Error("Not implemented");  }}export const run = async () => {  const model = new OpenAI({ temperature: 0 });  const tools = [    new SerpAPI(process.env.SERPAPI_API_KEY, {      location: "Austin,Texas,United States",      hl: "en",      gl: "us",    }),    new Calculator(),  ];  const llmChain = new LLMChain({    prompt: new CustomPromptTemplate({      tools,      inputVariables: ["input", "agent_scratchpad"],    }),    llm: model,  });  const agent = new LLMSingleActionAgent({    llmChain,    outputParser: new CustomOutputParser(),    stop: ["\nObservation"],  });  const executor = new AgentExecutor({    agent,    tools,  });  console.log("Loaded agent.");  const input = `Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?`;  console.log(`Executing with input "${input}"...`);  const result = await executor.call({ input });  console.log(`Got output ${result.output}`);};

#### API Reference:

*   [LLMSingleActionAgent](/docs/api/agents/classes/LLMSingleActionAgent) from `langchain/agents`
*   [AgentActionOutputParser](/docs/api/agents/classes/AgentActionOutputParser) from `langchain/agents`
*   [AgentExecutor](/docs/api/agents/classes/AgentExecutor) from `langchain/agents`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate) from `langchain/prompts`
*   [BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate) from `langchain/prompts`
*   [SerializedBasePromptTemplate](/docs/api/prompts/types/SerializedBasePromptTemplate) from `langchain/prompts`
*   [renderTemplate](/docs/api/prompts/functions/renderTemplate) from `langchain/prompts`
*   [InputValues](/docs/api/schema/types/InputValues) from `langchain/schema`
*   [PartialValues](/docs/api/schema/types/PartialValues) from `langchain/schema`
*   [AgentStep](/docs/api/schema/types/AgentStep) from `langchain/schema`
*   [AgentAction](/docs/api/schema/types/AgentAction) from `langchain/schema`
*   [AgentFinish](/docs/api/schema/types/AgentFinish) from `langchain/schema`
*   [SerpAPI](/docs/api/tools/classes/SerpAPI) from `langchain/tools`
*   [Tool](/docs/api/tools/classes/Tool) from `langchain/tools`
*   [Calculator](/docs/api/tools_calculator/classes/Calculator) from `langchain/tools/calculator`