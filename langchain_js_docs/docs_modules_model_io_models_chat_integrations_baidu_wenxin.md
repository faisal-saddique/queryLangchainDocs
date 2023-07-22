ChatBaiduWenxin
===============

LangChain.js supports Baidu's ERNIE-bot family of models. Here's an example:

    import { ChatBaiduWenxin } from "langchain/chat_models/baiduwenxin";import { HumanMessage } from "langchain/schema";// Default model is ERNIE-Bot-turboconst ernieTurbo = new ChatBaiduWenxin({  baiduApiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.BAIDU_API_KEY  baiduSecretKey: "YOUR-SECRET-KEY", // In Node.js defaults to process.env.BAIDU_SECRET_KEY});// Use ERNIE-Botconst ernie = new ChatBaiduWenxin({  modelName: "ERNIE-Bot",  temperature: 1, // Only ERNIE-Bot supports temperature  baiduApiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.BAIDU_API_KEY  baiduSecretKey: "YOUR-SECRET-KEY", // In Node.js defaults to process.env.BAIDU_SECRET_KEY});const messages = [new HumanMessage("Hello")];let res = await ernieTurbo.call(messages);/*AIChatMessage {  text: 'Hello! How may I assist you today?',  name: undefined,  additional_kwargs: {}  }}*/res = await ernie.call(messages);/*AIChatMessage {  text: 'Hello! How may I assist you today?',  name: undefined,  additional_kwargs: {}  }}*/

#### API Reference:

*   [ChatBaiduWenxin](/docs/api/chat_models_baiduwenxin/classes/ChatBaiduWenxin) from `langchain/chat_models/baiduwenxin`
*   [HumanMessage](/docs/api/schema/classes/HumanMessage) from `langchain/schema`