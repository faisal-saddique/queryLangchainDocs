Streaming
=========

Some LLMs provide a streaming response. This means that instead of waiting for the entire response to be returned, you can start processing it as soon as it's available. This is useful if you want to display the response to the user as it's being generated, or if you want to process the response as it's being generated.

To utilize streaming, use a [`CallbackHandler`](https://github.com/hwchase17/langchainjs/blob/main/langchain/src/callbacks/base.ts) like so:

    import { OpenAI } from "langchain/llms/openai";// To enable streaming, we pass in `streaming: true` to the LLM constructor.// Additionally, we pass in a handler for the `handleLLMNewToken` event.const model = new OpenAI({  maxTokens: 25,  streaming: true,});const response = await model.call("Tell me a joke.", {  callbacks: [    {      handleLLMNewToken(token: string) {        console.log({ token });      },    },  ],});console.log(response);/*{ token: '\n' }{ token: '\n' }{ token: 'Q' }{ token: ':' }{ token: ' Why' }{ token: ' did' }{ token: ' the' }{ token: ' chicken' }{ token: ' cross' }{ token: ' the' }{ token: ' playground' }{ token: '?' }{ token: '\n' }{ token: 'A' }{ token: ':' }{ token: ' To' }{ token: ' get' }{ token: ' to' }{ token: ' the' }{ token: ' other' }{ token: ' slide' }{ token: '.' }Q: Why did the chicken cross the playground?A: To get to the other slide.*/

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`

We still have access to the end `LLMResult` if using `generate`. However, `token_usage` is not currently supported for streaming.