Map reduce
==========

The map reduce documents chain first applies an LLM chain to each document individually (the Map step), treating the chain output as a new document. It then passes all the new documents to a separate combine documents chain to get a single output (the Reduce step). It can optionally first compress, or collapse, the mapped documents to make sure that they fit in the combine documents chain (which will often pass them to an LLM). This compression step is performed recursively if necessary.

![map_reduce_diagram](/assets/images/map_reduce-c65525a871b62f5cacef431625c4d133.jpg)

Here's how it looks in practice:

    import { OpenAI } from "langchain/llms/openai";import { loadQAMapReduceChain } from "langchain/chains";import { Document } from "langchain/document";// Optionally limit the number of concurrent requests to the language model.const model = new OpenAI({ temperature: 0, maxConcurrency: 10 });const chain = loadQAMapReduceChain(model);const docs = [  new Document({ pageContent: "harrison went to harvard" }),  new Document({ pageContent: "ankush went to princeton" }),];const res = await chain.call({  input_documents: docs,  question: "Where did harrison go to college",});console.log({ res });

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [loadQAMapReduceChain](/docs/api/chains/functions/loadQAMapReduceChain) from `langchain/chains`
*   [Document](/docs/api/document/classes/Document) from `langchain/document`