BabyAGI
=======

info

Original Repo: [https://github.com/yoheinakajima/babyagi](https://github.com/yoheinakajima/babyagi)

BabyAGI is made up of 3 components:

*   A chain responsible for creating tasks
*   A chain responsible for prioritising tasks
*   A chain responsible for executing tasks

These chains are executed in sequence until the task list is empty or the maximum number of iterations is reached.

Simple Example[](#simple-example "Direct link to Simple Example")
------------------------------------------------------------------

In this example we use BabyAGI directly without any tools. You'll see this results in successfully creating a list of tasks but when it comes to executing the tasks we do not get concrete results. This is because we have not provided any tools to the BabyAGI. We'll see how to do that in the next example.

    import { BabyAGI } from "langchain/experimental/babyagi";import { MemoryVectorStore } from "langchain/vectorstores/memory";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { OpenAI } from "langchain/llms/openai";const vectorStore = new MemoryVectorStore(new OpenAIEmbeddings());const babyAGI = BabyAGI.fromLLM({  llm: new OpenAI({ temperature: 0 }),  vectorstore: vectorStore,  maxIterations: 3,});await babyAGI.call({ objective: "Write a weather report for SF today" });/******TASK LIST*****1: Make a todo list*****NEXT TASK*****1: Make a todo list*****TASK RESULT*****1. Check the weather forecast for San Francisco today2. Make note of the temperature, humidity, wind speed, and other relevant weather conditions3. Write a weather report summarizing the forecast4. Check for any weather alerts or warnings5. Share the report with the relevant stakeholders*****TASK LIST*****2: Check the current temperature in San Francisco3: Check the current humidity in San Francisco4: Check the current wind speed in San Francisco5: Check for any weather alerts or warnings in San Francisco6: Check the forecast for the next 24 hours in San Francisco7: Check the forecast for the next 48 hours in San Francisco8: Check the forecast for the next 72 hours in San Francisco9: Check the forecast for the next week in San Francisco10: Check the forecast for the next month in San Francisco11: Check the forecast for the next 3 months in San Francisco1: Write a weather report for SF today*****NEXT TASK*****2: Check the current temperature in San Francisco*****TASK RESULT*****I will check the current temperature in San Francisco. I will use an online weather service to get the most up-to-date information.*****TASK LIST*****3: Check the current UV index in San Francisco4: Check the current air quality in San Francisco5: Check the current precipitation levels in San Francisco6: Check the current cloud cover in San Francisco7: Check the current barometric pressure in San Francisco8: Check the current dew point in San Francisco9: Check the current wind direction in San Francisco10: Check the current humidity levels in San Francisco1: Check the current temperature in San Francisco to the average temperature for this time of year2: Check the current visibility in San Francisco11: Write a weather report for SF today*****NEXT TASK*****3: Check the current UV index in San Francisco*****TASK RESULT*****The current UV index in San Francisco is moderate, with a value of 5. This means that it is safe to be outside for short periods of time without sunscreen, but it is still recommended to wear sunscreen and protective clothing when outside for extended periods of time.*/

#### API Reference:

*   [BabyAGI](/docs/api/experimental_babyagi/classes/BabyAGI) from `langchain/experimental/babyagi`
*   [MemoryVectorStore](/docs/api/vectorstores_memory/classes/MemoryVectorStore) from `langchain/vectorstores/memory`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`

Example with Tools[](#example-with-tools "Direct link to Example with Tools")
------------------------------------------------------------------------------

In this next example we replace the execution chain with a custom agent with a Search tool. This gives BabyAGI the ability to use real-world data when executing tasks, which makes it much more powerful. You can add additional tools to give it more capabilities.

    import { BabyAGI } from "langchain/experimental/babyagi";import { MemoryVectorStore } from "langchain/vectorstores/memory";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { OpenAI } from "langchain/llms/openai";import { PromptTemplate } from "langchain/prompts";import { LLMChain } from "langchain/chains";import { ChainTool, SerpAPI, Tool } from "langchain/tools";import { initializeAgentExecutorWithOptions } from "langchain/agents";// First, we create a custom agent which will serve as execution chain.const todoPrompt = PromptTemplate.fromTemplate(  "You are a planner who is an expert at coming up with a todo list for a given objective. Come up with a todo list for this objective: {objective}");const tools: Tool[] = [  new SerpAPI(process.env.SERPAPI_API_KEY, {    location: "San Francisco,California,United States",    hl: "en",    gl: "us",  }),  new ChainTool({    name: "TODO",    chain: new LLMChain({      llm: new OpenAI({ temperature: 0 }),      prompt: todoPrompt,    }),    description:      "useful for when you need to come up with todo lists. Input: an objective to create a todo list for. Output: a todo list for that objective. Please be very clear what the objective is!",  }),];const agentExecutor = await initializeAgentExecutorWithOptions(  tools,  new OpenAI({ temperature: 0 }),  {    agentType: "zero-shot-react-description",    agentArgs: {      prefix: `You are an AI who performs one task based on the following objective: {objective}. Take into account these previously completed tasks: {context}.`,      suffix: `Question: {task}{agent_scratchpad}`,      inputVariables: ["objective", "task", "context", "agent_scratchpad"],    },  });const vectorStore = new MemoryVectorStore(new OpenAIEmbeddings());// Then, we create a BabyAGI instance.const babyAGI = BabyAGI.fromLLM({  llm: new OpenAI({ temperature: 0 }),  executionChain: agentExecutor, // an agent executor is a chain  vectorstore: vectorStore,  maxIterations: 10,});await babyAGI.call({ objective: "Write a short weather report for SF today" });/******TASK LIST*****1: Make a todo list*****NEXT TASK*****1: Make a todo list*****TASK RESULT*****Today in San Francisco, the weather is sunny with a temperature of 70 degrees Fahrenheit, light winds, and low humidity. The forecast for the next few days is expected to be similar.*****TASK LIST*****2: Find the forecasted temperature for the next few days in San Francisco3: Find the forecasted wind speed for the next few days in San Francisco4: Find the forecasted humidity for the next few days in San Francisco5: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the next few days6: Research the average temperature for San Francisco in the past week7: Research the average wind speed for San Francisco in the past week8: Research the average humidity for San Francisco in the past week9: Create a graph showing the temperature, wind speed, and humidity for San Francisco over the past week*****NEXT TASK*****2: Find the forecasted temperature for the next few days in San Francisco*****TASK RESULT*****The forecasted temperature for the next few days in San Francisco is 63°, 65°, 71°, 73°, and 66°.*****TASK LIST*****3: Find the forecasted wind speed for the next few days in San Francisco4: Find the forecasted humidity for the next few days in San Francisco5: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the next few days6: Research the average temperature for San Francisco in the past week7: Research the average wind speed for San Francisco in the past week8: Research the average humidity for San Francisco in the past week9: Create a graph showing the temperature, wind speed, and humidity for San Francisco over the past week10: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average temperature, wind speed, and humidity for San Francisco over the past week11: Find the forecasted precipitation for the next few days in San Francisco12: Research the average wind direction for San Francisco in the past week13: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the past week14: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to*****NEXT TASK*****3: Find the forecasted wind speed for the next few days in San Francisco*****TASK RESULT*****West winds 10 to 20 mph. Gusts up to 35 mph in the evening. Tuesday. Sunny. Highs in the 60s to upper 70s. West winds 5 to 15 mph.*****TASK LIST*****4: Research the average precipitation for San Francisco in the past week5: Research the average temperature for San Francisco in the past week6: Research the average wind speed for San Francisco in the past week7: Research the average humidity for San Francisco in the past week8: Research the average wind direction for San Francisco in the past week9: Find the forecasted temperature, wind speed, and humidity for San Francisco over the next few days10: Find the forecasted precipitation for the next few days in San Francisco11: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the next few days12: Create a graph showing the temperature, wind speed, and humidity for San Francisco over the past week13: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the past month14: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average temperature, wind speed, and humidity for San Francisco over the past week15: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the*****NEXT TASK*****4: Research the average precipitation for San Francisco in the past week*****TASK RESULT*****According to Weather Underground, the forecasted precipitation for San Francisco in the next few days is 7-hour rain and snow with 24-hour rain accumulation.*****TASK LIST*****5: Research the average wind speed for San Francisco over the past month6: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the past month7: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average temperature, wind speed, and humidity for San Francisco over the past month8: Research the average temperature for San Francisco over the past month9: Research the average wind direction for San Francisco over the past month10: Create a graph showing the forecasted precipitation for San Francisco over the next few days11: Compare the forecasted precipitation for San Francisco over the next few days to the average precipitation for San Francisco over the past week12: Find the forecasted temperature, wind speed, and humidity for San Francisco over the next few days13: Find the forecasted precipitation for the next few days in San Francisco14: Create a graph showing the temperature, wind speed, and humidity for San Francisco over the past week15: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the next few days16: Compare the forecast*****NEXT TASK*****5: Research the average wind speed for San Francisco over the past month*****TASK RESULT*****The average wind speed for San Francisco over the past month is 3.2 meters per second.*****TASK LIST*****6: Find the forecasted temperature, wind speed, and humidity for San Francisco over the next few days,7: Find the forecasted precipitation for the next few days in San Francisco,8: Create a graph showing the temperature, wind speed, and humidity for San Francisco over the past week,9: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the next few days,10: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average wind speed for San Francisco over the past month,11: Research the average wind speed for San Francisco over the past week,12: Create a graph showing the forecasted precipitation for San Francisco over the next few days,13: Compare the forecasted precipitation for San Francisco over the next few days to the average precipitation for San Francisco over the past month,14: Research the average temperature for San Francisco over the past month,15: Research the average humidity for San Francisco over the past month,16: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average temperature,*****NEXT TASK*****6: Find the forecasted temperature, wind speed, and humidity for San Francisco over the next few days,*****TASK RESULT*****The forecast for San Francisco over the next few days is mostly sunny, with a high near 64. West wind 7 to 12 mph increasing to 13 to 18 mph in the afternoon. Winds could gust as high as 22 mph. Humidity will be around 50%.*****TASK LIST*****7: Find the forecasted precipitation for the next few days in San Francisco,8: Create a graph showing the temperature, wind speed, and humidity for San Francisco over the past week,9: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the next few days,10: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average wind speed for San Francisco over the past month,11: Research the average wind speed for San Francisco over the past week,12: Create a graph showing the forecasted precipitation for San Francisco over the next few days,13: Compare the forecasted precipitation for San Francisco over the next few days to the average precipitation for San Francisco over the past month,14: Research the average temperature for San Francisco over the past month,15: Research the average humidity for San Francisco over the past month,16: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average temperature*****NEXT TASK*****7: Find the forecasted precipitation for the next few days in San Francisco,*****TASK RESULT*****According to Weather Underground, the forecasted precipitation for the next few days in San Francisco is 7-hour rain and snow with 24-hour rain accumulation, radar and satellite maps of precipitation.*****TASK LIST*****8: Create a graph showing the temperature, wind speed, and humidity for San Francisco over the past week,9: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the next few days,10: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average wind speed for San Francisco over the past month,11: Research the average wind speed for San Francisco over the past week,12: Create a graph showing the forecasted precipitation for San Francisco over the next few days,13: Compare the forecasted precipitation for San Francisco over the next few days to the average precipitation for San Francisco over the past month,14: Research the average temperature for San Francisco over the past month,15: Research the average humidity for San Francisco over the past month,16: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average temperature*****NEXT TASK*****8: Create a graph showing the temperature, wind speed, and humidity for San Francisco over the past week,*****TASK RESULT*****A graph showing the temperature, wind speed, and humidity for San Francisco over the past week.*****TASK LIST*****9: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the next few days10: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average wind speed for San Francisco over the past month11: Research the average wind speed for San Francisco over the past week12: Create a graph showing the forecasted precipitation for San Francisco over the next few days13: Compare the forecasted precipitation for San Francisco over the next few days to the average precipitation for San Francisco over the past month14: Research the average temperature for San Francisco over the past month15: Research the average humidity for San Francisco over the past month16: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average temperature*****NEXT TASK*****9: Create a graph showing the forecasted temperature, wind speed, and humidity for San Francisco over the next few days*****TASK RESULT*****The forecasted temperature, wind speed, and humidity for San Francisco over the next few days can be seen in the graph created.*****TASK LIST*****10: Research the average wind speed for San Francisco over the past month11: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average humidity for San Francisco over the past month12: Create a graph showing the forecasted precipitation for San Francisco over the next few days13: Compare the forecasted precipitation for San Francisco over the next few days to the average precipitation for San Francisco over the past month14: Research the average temperature for San Francisco over the past week15: Compare the forecasted temperature, wind speed, and humidity for San Francisco over the next few days to the average wind speed for San Francisco over the past week*****NEXT TASK*****10: Research the average wind speed for San Francisco over the past month*****TASK RESULT*****The average wind speed for San Francisco over the past month is 2.7 meters per second.[...]*/

#### API Reference:

*   [BabyAGI](/docs/api/experimental_babyagi/classes/BabyAGI) from `langchain/experimental/babyagi`
*   [MemoryVectorStore](/docs/api/vectorstores_memory/classes/MemoryVectorStore) from `langchain/vectorstores/memory`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) from `langchain/prompts`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`
*   [ChainTool](/docs/api/tools/classes/ChainTool) from `langchain/tools`
*   [SerpAPI](/docs/api/tools/classes/SerpAPI) from `langchain/tools`
*   [Tool](/docs/api/tools/classes/Tool) from `langchain/tools`
*   [initializeAgentExecutorWithOptions](/docs/api/agents/functions/initializeAgentExecutorWithOptions) from `langchain/agents`