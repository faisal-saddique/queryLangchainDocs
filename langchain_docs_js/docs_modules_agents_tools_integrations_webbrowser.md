Web Browser Tool
================

The Webbrowser Tool gives your agent the ability to visit a website and extract information. It is described to the agent as

    useful for when you need to find something on or summarize a webpage. input should be a comma separated list of "valid URL including protocol","what you want to find on the page or empty string for a summary".

It exposes two modes of operation:

*   when called by the Agent with only a URL it produces a summary of the website contents
*   when called by the Agent with a URL and a description of what to find it will instead use an in-memory Vector Store to find the most relevant snippets and summarise those

Setup[](#setup "Direct link to Setup")
---------------------------------------

To use the Webbrowser Tool you need to install the dependencies:

*   npm
*   Yarn
*   pnpm

    npm install cheerio axios

    yarn add cheerio axios

    pnpm add cheerio axios

Usage, standalone[](#usage-standalone "Direct link to Usage, standalone")
--------------------------------------------------------------------------

    import { WebBrowser } from "langchain/tools/webbrowser";import { ChatOpenAI } from "langchain/chat_models/openai";import { OpenAIEmbeddings } from "langchain/embeddings/openai";export async function run() {  // this will not work with Azure OpenAI API yet  // Azure OpenAI API does not support embedding with multiple inputs yet  // Too many inputs. The max number of inputs is 1.  We hope to increase the number of inputs per request soon. Please contact us through an Azure support request at: https://go.microsoft.com/fwlink/?linkid=2213926 for further questions.  // So we will fail fast, when Azure OpenAI API is used  if (process.env.AZURE_OPENAI_API_KEY) {    throw new Error(      "Azure OpenAI API does not support embedding with multiple inputs yet"    );  }  const model = new ChatOpenAI({ temperature: 0 });  const embeddings = new OpenAIEmbeddings(    process.env.AZURE_OPENAI_API_KEY      ? { azureOpenAIApiDeploymentName: "Embeddings2" }      : {}  );  const browser = new WebBrowser({ model, embeddings });  const result = await browser.call(    `"https://www.themarginalian.org/2015/04/09/find-your-bliss-joseph-campbell-power-of-myth","who is joseph campbell"`  );  console.log(result);  /*  Joseph Campbell was a mythologist and writer who discussed spirituality, psychological archetypes, cultural myths, and the mythology of self. He sat down with Bill Moyers for a lengthy conversation at George Lucas’s Skywalker Ranch in California, which continued the following year at the American Museum of Natural History in New York. The resulting 24 hours of raw footage were edited down to six one-hour episodes and broadcast on PBS in 1988, shortly after Campbell’s death, in what became one of the most popular in the history of public television.  Relevant Links:  - [The Holstee Manifesto](http://holstee.com/manifesto-bp)  - [The Silent Music of the Mind: Remembering Oliver Sacks](https://www.themarginalian.org/2015/08/31/remembering-oliver-sacks)  - [Joseph Campbell series](http://billmoyers.com/spotlight/download-joseph-campbell-and-the-power-of-myth-audio/)  - [Bill Moyers](https://www.themarginalian.org/tag/bill-moyers/)  - [books](https://www.themarginalian.org/tag/books/)  */}

#### API Reference:

*   [WebBrowser](/docs/api/tools_webbrowser/classes/WebBrowser) from `langchain/tools/webbrowser`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

Usage, in an Agent[](#usage-in-an-agent "Direct link to Usage, in an Agent")
-----------------------------------------------------------------------------

    import { OpenAI } from "langchain/llms/openai";import { initializeAgentExecutorWithOptions } from "langchain/agents";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { SerpAPI } from "langchain/tools";import { Calculator } from "langchain/tools/calculator";import { WebBrowser } from "langchain/tools/webbrowser";export const run = async () => {  const model = new OpenAI({ temperature: 0 });  const embeddings = new OpenAIEmbeddings();  const tools = [    new SerpAPI(process.env.SERPAPI_API_KEY, {      location: "Austin,Texas,United States",      hl: "en",      gl: "us",    }),    new Calculator(),    new WebBrowser({ model, embeddings }),  ];  const executor = await initializeAgentExecutorWithOptions(tools, model, {    agentType: "zero-shot-react-description",    verbose: true,  });  console.log("Loaded agent.");  const input = `What is the word of the day on merriam webster. What is the top result on google for that word`;  console.log(`Executing with input "${input}"...`);  const result = await executor.call({ input });  /*  Entering new agent_executor chain...  I need to find the word of the day on Merriam Webster and then search for it on Google  Action: web-browser  Action Input: "https://www.merriam-webster.com/word-of-the-day", ""  Summary: Merriam-Webster is a website that provides users with a variety of resources, including a dictionary, thesaurus, word finder, word of the day, games and quizzes, and more. The website also allows users to log in and save words, view recents, and access their account settings. The Word of the Day for April 14, 2023 is "lackadaisical", which means lacking in life, spirit, or zest. The website also provides quizzes and games to help users build their vocabulary.  Relevant Links:   - [Test Your Vocabulary](https://www.merriam-webster.com/games)  - [Thesaurus](https://www.merriam-webster.com/thesaurus)  - [Word Finder](https://www.merriam-webster.com/wordfinder)  - [Word of the Day](https://www.merriam-webster.com/word-of-the-day)  - [Shop](https://shop.merriam-webster.com/?utm_source=mwsite&utm_medium=nav&utm_content=  I now need to search for the word of the day on Google  Action: search  Action Input: "lackadaisical"  lackadaisical implies a carefree indifference marked by half-hearted efforts. lackadaisical college seniors pretending to study. listless suggests a lack of ...  Finished chain.  */  console.log(`Got output ${JSON.stringify(result, null, 2)}`);  /*  Got output {    "output": "The word of the day on Merriam Webster is \"lackadaisical\", which implies a carefree indifference marked by half-hearted efforts.",    "intermediateSteps": [      {        "action": {          "tool": "web-browser",          "toolInput": "https://www.merriam-webster.com/word-of-the-day\", ",          "log": " I need to find the word of the day on Merriam Webster and then search for it on Google\nAction: web-browser\nAction Input: \"https://www.merriam-webster.com/word-of-the-day\", \"\""        },        "observation": "\n\nSummary: Merriam-Webster is a website that provides users with a variety of resources, including a dictionary, thesaurus, word finder, word of the day, games and quizzes, and more. The website also allows users to log in and save words, view recents, and access their account settings. The Word of the Day for April 14, 2023 is \"lackadaisical\", which means lacking in life, spirit, or zest. The website also provides quizzes and games to help users build their vocabulary.\n\nRelevant Links: \n- [Test Your Vocabulary](https://www.merriam-webster.com/games)\n- [Thesaurus](https://www.merriam-webster.com/thesaurus)\n- [Word Finder](https://www.merriam-webster.com/wordfinder)\n- [Word of the Day](https://www.merriam-webster.com/word-of-the-day)\n- [Shop](https://shop.merriam-webster.com/?utm_source=mwsite&utm_medium=nav&utm_content="      },      {        "action": {          "tool": "search",          "toolInput": "lackadaisical",          "log": " I now need to search for the word of the day on Google\nAction: search\nAction Input: \"lackadaisical\""        },        "observation": "lackadaisical implies a carefree indifference marked by half-hearted efforts. lackadaisical college seniors pretending to study. listless suggests a lack of ..."      }    ]  }  */};

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [initializeAgentExecutorWithOptions](/docs/api/agents/functions/initializeAgentExecutorWithOptions) from `langchain/agents`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [SerpAPI](/docs/api/tools/classes/SerpAPI) from `langchain/tools`
*   [Calculator](/docs/api/tools_calculator/classes/Calculator) from `langchain/tools/calculator`
*   [WebBrowser](/docs/api/tools_webbrowser/classes/WebBrowser) from `langchain/tools/webbrowser`