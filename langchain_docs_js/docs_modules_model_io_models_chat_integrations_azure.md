Azure ChatOpenAI
================

You can also use the `ChatOpenAI` class to access OpenAI instances hosted on Azure like this:

    import { ChatOpenAI } from "langchain/chat_models/openai";const model = new ChatOpenAI({  temperature: 0.9,  azureOpenAIApiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.AZURE_OPENAI_API_KEY  azureOpenAIApiInstanceName: "YOUR-INSTANCE-NAME", // In Node.js defaults to process.env.AZURE_OPENAI_API_INSTANCE_NAME  azureOpenAIApiDeploymentName: "YOUR-DEPLOYMENT-NAME", // In Node.js defaults to process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME  azureOpenAIApiVersion: "YOUR-API-VERSION", // In Node.js defaults to process.env.AZURE_OPENAI_API_VERSION  azureOpenAIBasePath: "YOUR-AZURE-OPENAI-BASE-PATH", // In Node.js defaults to process.env.AZURE_OPENAI_BASE_PATH});

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`