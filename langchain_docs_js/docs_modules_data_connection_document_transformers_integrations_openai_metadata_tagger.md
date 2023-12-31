OpenAI functions metadata tagger
================================

It can often be useful to tag ingested documents with structured metadata, such as the title, tone, or length of a document, to allow for more targeted similarity search later. However, for large numbers of documents, performing this labelling process manually can be tedious.

The `MetadataTagger` document transformer automates this process by extracting metadata from each provided document according to a provided schema. It uses a configurable OpenAI Functions-powered chain under the hood, so if you pass a custom LLM instance, it must be an OpenAI model with functions support.

**Note:** This document transformer works best with complete documents, so it's best to run it first with whole documents before doing any other splitting or processing!

### Usage[](#usage "Direct link to Usage")

For example, let's say you wanted to index a set of movie reviews. You could initialize the document transformer as follows:

    import { z } from "zod";import { createMetadataTaggerFromZod } from "langchain/document_transformers/openai_functions";import { ChatOpenAI } from "langchain/chat_models/openai";import { Document } from "langchain/document";const zodSchema = z.object({  movie_title: z.string(),  critic: z.string(),  tone: z.enum(["positive", "negative"]),  rating: z    .optional(z.number())    .describe("The number of stars the critic rated the movie"),});const metadataTagger = createMetadataTaggerFromZod(zodSchema, {  llm: new ChatOpenAI({ modelName: "gpt-3.5-turbo" }),});const documents = [  new Document({    pageContent:      "Review of The Bee Movie\nBy Roger Ebert\nThis is the greatest movie ever made. 4 out of 5 stars.",  }),  new Document({    pageContent:      "Review of The Godfather\nBy Anonymous\n\nThis movie was super boring. 1 out of 5 stars.",    metadata: { reliable: false },  }),];const taggedDocuments = await metadataTagger.transformDocuments(documents);console.log(taggedDocuments);/*  [    Document {      pageContent: 'Review of The Bee Movie\n' +        'By Roger Ebert\n' +        'This is the greatest movie ever made. 4 out of 5 stars.',      metadata: {        movie_title: 'The Bee Movie',        critic: 'Roger Ebert',        tone: 'positive',        rating: 4      }    },    Document {      pageContent: 'Review of The Godfather\n' +        'By Anonymous\n' +        '\n' +        'This movie was super boring. 1 out of 5 stars.',      metadata: {        movie_title: 'The Godfather',        critic: 'Anonymous',        tone: 'negative',        rating: 1,        reliable: false      }    }  ]*/

#### API Reference:

*   [createMetadataTaggerFromZod](/docs/api/document_transformers_openai_functions/functions/createMetadataTaggerFromZod) from `langchain/document_transformers/openai_functions`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [Document](/docs/api/document/classes/Document) from `langchain/document`

There is an additional `createMetadataTagger` method that accepts a valid JSON Schema object as well.

### Customization[](#customization "Direct link to Customization")

You can pass the underlying tagging chain the standard LLMChain arguments in the second options parameter. For example, if you wanted to ask the LLM to focus specific details in the input documents, or extract metadata in a certain style, you could pass in a custom prompt:

    import { z } from "zod";import { createMetadataTaggerFromZod } from "langchain/document_transformers/openai_functions";import { ChatOpenAI } from "langchain/chat_models/openai";import { Document } from "langchain/document";import { PromptTemplate } from "langchain/prompts";const taggingChainTemplate = `Extract the desired information from the following passage.Anonymous critics are actually Roger Ebert.Passage:{input}`;const zodSchema = z.object({  movie_title: z.string(),  critic: z.string(),  tone: z.enum(["positive", "negative"]),  rating: z    .optional(z.number())    .describe("The number of stars the critic rated the movie"),});const metadataTagger = createMetadataTaggerFromZod(zodSchema, {  llm: new ChatOpenAI({ modelName: "gpt-3.5-turbo" }),  prompt: PromptTemplate.fromTemplate(taggingChainTemplate),});const documents = [  new Document({    pageContent:      "Review of The Bee Movie\nBy Roger Ebert\nThis is the greatest movie ever made. 4 out of 5 stars.",  }),  new Document({    pageContent:      "Review of The Godfather\nBy Anonymous\n\nThis movie was super boring. 1 out of 5 stars.",    metadata: { reliable: false },  }),];const taggedDocuments = await metadataTagger.transformDocuments(documents);console.log(taggedDocuments);/*  [    Document {      pageContent: 'Review of The Bee Movie\n' +        'By Roger Ebert\n' +        'This is the greatest movie ever made. 4 out of 5 stars.',      metadata: {        movie_title: 'The Bee Movie',        critic: 'Roger Ebert',        tone: 'positive',        rating: 4      }    },    Document {      pageContent: 'Review of The Godfather\n' +        'By Anonymous\n' +        '\n' +        'This movie was super boring. 1 out of 5 stars.',      metadata: {        movie_title: 'The Godfather',        critic: 'Roger Ebert',        tone: 'negative',        rating: 1,        reliable: false      }    }  ]*/

#### API Reference:

*   [createMetadataTaggerFromZod](/docs/api/document_transformers_openai_functions/functions/createMetadataTaggerFromZod) from `langchain/document_transformers/openai_functions`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [Document](/docs/api/document/classes/Document) from `langchain/document`
*   [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) from `langchain/prompts`