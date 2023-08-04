Documents
=========

These are the core chains for working with Documents. They are useful for summarizing documents, answering questions over documents, extracting information from documents, and more.

These chains are all loaded in a similar way:

    import { OpenAI } from "langchain/llms/openai";import {  loadQAStuffChain,  loadQAMapReduceChain,  loadQARefineChain} from "langchain/chains";import { Document } from "langchain/document";// This first example uses the `StuffDocumentsChain`.const llmA = new OpenAI({});const chainA = loadQAStuffChain(llmA);const docs = [  new Document({ pageContent: "Harrison went to Harvard." }),  new Document({ pageContent: "Ankush went to Princeton." }),];const resA = await chainA.call({  input_documents: docs,  question: "Where did Harrison go to college?",});console.log({ resA });// { resA: { text: ' Harrison went to Harvard.' } }// This second example uses the `MapReduceChain`.// Optionally limit the number of concurrent requests to the language model.const llmB = new OpenAI({ maxConcurrency: 10 });const chainB = loadQAMapReduceChain(llmB);const resB = await chainB.call({  input_documents: docs,  question: "Where did Harrison go to college?",});console.log({ resB });// { resB: { text: ' Harrison went to Harvard.' } }

[

📄️ Stuff
---------

The stuff documents chain ("stuff" as in "to stuff" or "to fill") is the most straightforward of the document chains. It takes a list of documents, inserts them all into a prompt and passes that prompt to an LLM.

](/docs/modules/chains/document/stuff)

[

📄️ Refine
----------

The refine documents chain constructs a response by looping over the input documents and iteratively updating its answer. For each document, it passes all non-document inputs, the current document, and the latest intermediate answer to an LLM chain to get a new answer.

](/docs/modules/chains/document/refine)

[

📄️ Map reduce
--------------

The map reduce documents chain first applies an LLM chain to each document individually (the Map step), treating the chain output as a new document. It then passes all the new documents to a separate combine documents chain to get a single output (the Reduce step). It can optionally first compress, or collapse, the mapped documents to make sure that they fit in the combine documents chain (which will often pass them to an LLM). This compression step is performed recursively if necessary.

](/docs/modules/chains/document/map_reduce)