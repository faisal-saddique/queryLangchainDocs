Azure OpenAI
============

You can also use the `OpenAI` class to call OpenAI models hosted on Azure. Here's an example:

    import { OpenAI } from "langchain/llms/openai";const model = new OpenAI({  temperature: 0.9,  azureOpenAIApiKey: "YOUR-API-KEY",  azureOpenAIApiInstanceName: "YOUR-INSTANCE-NAME",  azureOpenAIApiDeploymentName: "YOUR-DEPLOYMENT-NAME",  azureOpenAIApiVersion: "YOUR-API-VERSION",});const res = await model.call(  "What would be a good company name a company that makes colorful socks?");console.log({ res });