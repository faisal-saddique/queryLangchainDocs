Adding a timeout
================

By default, LangChain will wait indefinitely for a response from the model provider. If you want to add a timeout, you can pass a `timeout` option, in milliseconds, when you instantiate the model. For example, for OpenAI:

    import { OpenAIEmbeddings } from "langchain/embeddings/openai";const embeddings = new OpenAIEmbeddings({  timeout: 1000, // 1s timeout});/* Embed queries */const res = await embeddings.embedQuery("Hello world");console.log(res);/* Embed documents */const documentRes = await embeddings.embedDocuments(["Hello world", "Bye bye"]);console.log({ documentRes });

#### API Reference:

*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

Currently, the timeout option is only supported for OpenAI models.