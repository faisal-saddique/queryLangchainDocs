Stuff
=====

The stuff documents chain ("stuff" as in "to stuff" or "to fill") is the most straightforward of the document chains. It takes a list of documents, inserts them all into a prompt and passes that prompt to an LLM.

This chain is well-suited for applications where documents are small and only a few are passed in for most calls.

![stuff_diagram](/assets/images/stuff-818da4c66ee17911bc8861c089316579.jpg)

Here's how it looks in practice:

    import { OpenAI } from "langchain/llms/openai";import { loadQAStuffChain } from "langchain/chains";import { Document } from "langchain/document";// This first example uses the `StuffDocumentsChain`.const llmA = new OpenAI({});const chainA = loadQAStuffChain(llmA);const docs = [  new Document({ pageContent: "Harrison went to Harvard." }),  new Document({ pageContent: "Ankush went to Princeton." }),];const resA = await chainA.call({  input_documents: docs,  question: "Where did Harrison go to college?",});console.log({ resA });// { resA: { text: ' Harrison went to Harvard.' } }

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [loadQAStuffChain](/docs/api/chains/functions/loadQAStuffChain) from `langchain/chains`
*   [Document](/docs/api/document/classes/Document) from `langchain/document`