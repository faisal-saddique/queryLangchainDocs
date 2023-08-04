Analyze Document
================

The AnalyzeDocumentChain can be used as an end-to-end to chain. This chain takes in a single document, splits it up, and then runs it through a CombineDocumentsChain.

The below example uses a `MapReduceDocumentsChain` to generate a summary.

    import { OpenAI } from "langchain/llms/openai";import { loadSummarizationChain, AnalyzeDocumentChain } from "langchain/chains";import * as fs from "fs";// In this example, we use the `AnalyzeDocumentChain` to summarize a large text document.const text = fs.readFileSync("state_of_the_union.txt", "utf8");const model = new OpenAI({ temperature: 0 });const combineDocsChain = loadSummarizationChain(model);const chain = new AnalyzeDocumentChain({  combineDocumentsChain: combineDocsChain,});const res = await chain.call({  input_document: text,});console.log({ res });/*{  res: {    text: ' President Biden is taking action to protect Americans from the COVID-19 pandemic and Russian aggression, providing economic relief, investing in infrastructure, creating jobs, and fighting inflation.    He is also proposing measures to reduce the cost of prescription drugs, protect voting rights, and reform the immigration system. The speaker is advocating for increased economic security, police reform, and the Equality Act, as well as providing support for veterans and military families.    The US is making progress in the fight against COVID-19, and the speaker is encouraging Americans to come together and work towards a brighter future.'  }}*/

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [loadSummarizationChain](/docs/api/chains/functions/loadSummarizationChain) from `langchain/chains`
*   [AnalyzeDocumentChain](/docs/api/chains/classes/AnalyzeDocumentChain) from `langchain/chains`