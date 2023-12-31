AWS SageMakerEndpoint
=====================

LangChain.js supports integration with AWS SageMaker-hosted endpoints. Check [Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) for a list of available models, and how to deploy your own.

Here's an example:

*   npm
*   Yarn
*   pnpm

    npm install @aws-sdk/client-sagemaker-runtime

    yarn add @aws-sdk/client-sagemaker-runtime

    pnpm add @aws-sdk/client-sagemaker-runtime

    import {  SageMakerLLMContentHandler,  SageMakerEndpoint,} from "langchain/llms/sagemaker_endpoint";// Custom for whatever model you'll be usingclass HuggingFaceTextGenerationGPT2ContentHandler  implements SageMakerLLMContentHandler{  contentType = "application/json";  accepts = "application/json";  async transformInput(prompt: string, modelKwargs: Record<string, unknown>) {    const inputString = JSON.stringify({      text_inputs: prompt,      ...modelKwargs,    });    return Buffer.from(inputString);  }  async transformOutput(output: Uint8Array) {    const responseJson = JSON.parse(Buffer.from(output).toString("utf-8"));    return responseJson.generated_texts[0];  }}const contentHandler = new HuggingFaceTextGenerationGPT2ContentHandler();const model = new SageMakerEndpoint({  endpointName:    "jumpstart-example-huggingface-textgener-2023-05-16-22-35-45-660", // Your endpoint name here  modelKwargs: { temperature: 1e-10 },  contentHandler,  clientOptions: {    region: "YOUR AWS ENDPOINT REGION",    credentials: {      accessKeyId: "YOUR AWS ACCESS ID",      secretAccessKey: "YOUR AWS SECRET ACCESS KEY",    },  },});const res = await model.call("Hello, my name is ");console.log({ res });/*  {    res: "_____. I am a student at the University of California, Berkeley. I am a member of the American Association of University Professors."  } */

#### API Reference:

*   [SageMakerLLMContentHandler](/docs/api/llms_sagemaker_endpoint/types/SageMakerLLMContentHandler) from `langchain/llms/sagemaker_endpoint`
*   [SageMakerEndpoint](/docs/api/llms_sagemaker_endpoint/classes/SageMakerEndpoint) from `langchain/llms/sagemaker_endpoint`