Refine
======

The refine documents chain constructs a response by looping over the input documents and iteratively updating its answer. For each document, it passes all non-document inputs, the current document, and the latest intermediate answer to an LLM chain to get a new answer.

Since the Refine chain only passes a single document to the LLM at a time, it is well-suited for tasks that require analyzing more documents than can fit in the model's context. The obvious tradeoff is that this chain will make far more LLM calls than, for example, the Stuff documents chain. There are also certain tasks which are difficult to accomplish iteratively. For example, the Refine chain can perform poorly when documents frequently cross-reference one another or when a task requires detailed information from many documents.

![refine_diagram](/assets/images/refine-a70f30dd7ada6fe5e3fcc40dd70de037.jpg)

Here's how it looks in practice:

    import { loadQARefineChain } from "langchain/chains";import { OpenAI } from "langchain/llms/openai";import { TextLoader } from "langchain/document_loaders/fs/text";import { MemoryVectorStore } from "langchain/vectorstores/memory";import { OpenAIEmbeddings } from "langchain/embeddings/openai";// Create the models and chainconst embeddings = new OpenAIEmbeddings();const model = new OpenAI({ temperature: 0 });const chain = loadQARefineChain(model);// Load the documents and create the vector storeconst loader = new TextLoader("./state_of_the_union.txt");const docs = await loader.loadAndSplit();const store = await MemoryVectorStore.fromDocuments(docs, embeddings);// Select the relevant documentsconst question = "What did the president say about Justice Breyer";const relevantDocs = await store.similaritySearch(question);// Call the chainconst res = await chain.call({  input_documents: relevantDocs,  question,});console.log(res);/*{  output_text: '\n' +    '\n' +    "The president said that Justice Stephen Breyer has dedicated his life to serve this country and thanked him for his service. He also mentioned that Judge Ketanji Brown Jackson will continue Justice Breyer's legacy of excellence, and that the constitutional right affirmed in Roe v. Wade—standing precedent for half a century—is under attack as never before. He emphasized the importance of protecting access to health care, preserving a woman's right to choose, and advancing maternal health care in America. He also expressed his support for the LGBTQ+ community, and his commitment to protecting their rights, including offering a Unity Agenda for the Nation to beat the opioid epidemic, increase funding for prevention, treatment, harm reduction, and recovery, and strengthen the Violence Against Women Act."}*/

#### API Reference:

*   [loadQARefineChain](/docs/api/chains/functions/loadQARefineChain) from `langchain/chains`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader) from `langchain/document_loaders/fs/text`
*   [MemoryVectorStore](/docs/api/vectorstores_memory/classes/MemoryVectorStore) from `langchain/vectorstores/memory`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

Prompt customization[](#prompt-customization "Direct link to Prompt customization")
------------------------------------------------------------------------------------

You may want to tweak the behavior of a step by changing the prompt. Here's an example of how to do that:

    import { loadQARefineChain } from "langchain/chains";import { OpenAI } from "langchain/llms/openai";import { TextLoader } from "langchain/document_loaders/fs/text";import { MemoryVectorStore } from "langchain/vectorstores/memory";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { PromptTemplate } from "langchain/prompts";export const questionPromptTemplateString = `Context information is below.---------------------{context}---------------------Given the context information and not prior knowledge, answer the question: {question}`;const questionPrompt = new PromptTemplate({  inputVariables: ["context", "question"],  template: questionPromptTemplateString,});const refinePromptTemplateString = `The original question is as follows: {question}We have provided an existing answer: {existing_answer}We have the opportunity to refine the existing answer(only if needed) with some more context below.------------{context}------------Given the new context, refine the original answer to better answer the question.You must provide a response, either original answer or refined answer.`;const refinePrompt = new PromptTemplate({  inputVariables: ["question", "existing_answer", "context"],  template: refinePromptTemplateString,});// Create the models and chainconst embeddings = new OpenAIEmbeddings();const model = new OpenAI({ temperature: 0 });const chain = loadQARefineChain(model, {  questionPrompt,  refinePrompt,});// Load the documents and create the vector storeconst loader = new TextLoader("./state_of_the_union.txt");const docs = await loader.loadAndSplit();const store = await MemoryVectorStore.fromDocuments(docs, embeddings);// Select the relevant documentsconst question = "What did the president say about Justice Breyer";const relevantDocs = await store.similaritySearch(question);// Call the chainconst res = await chain.call({  input_documents: relevantDocs,  question,});console.log(res);/*{  output_text: '\n' +    '\n' +    "The president said that Justice Stephen Breyer has dedicated his life to serve this country and thanked him for his service. He also mentioned that Judge Ketanji Brown Jackson will continue Justice Breyer's legacy of excellence, and that the constitutional right affirmed in Roe v. Wade—standing precedent for half a century—is under attack as never before. He emphasized the importance of protecting access to health care, preserving a woman's right to choose, and advancing maternal health care in America. He also expressed his support for the LGBTQ+ community, and his commitment to protecting their rights, including offering a Unity Agenda for the Nation to beat the opioid epidemic, increase funding for prevention, treatment, harm reduction, and recovery, and strengthen the Violence Against Women Act."}*/

#### API Reference:

*   [loadQARefineChain](/docs/api/chains/functions/loadQARefineChain) from `langchain/chains`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader) from `langchain/document_loaders/fs/text`
*   [MemoryVectorStore](/docs/api/vectorstores_memory/classes/MemoryVectorStore) from `langchain/vectorstores/memory`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) from `langchain/prompts`