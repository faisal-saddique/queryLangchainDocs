ChatAnthropic
=============

LangChain supports Anthropic's Claude family of chat models. You can initialize an instance like this:

    import { ChatAnthropic } from "langchain/chat_models/anthropic";const model = new ChatAnthropic({  temperature: 0.9,  anthropicApiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.ANTHROPIC_API_KEY});

#### API Reference:

*   [ChatAnthropic](/docs/api/chat_models_anthropic/classes/ChatAnthropic) from `langchain/chat_models/anthropic`