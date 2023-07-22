OpenAPI Calls
=============

Compatibility

Must be used with an [OpenAI Functions](https://platform.openai.com/docs/guides/gpt/function-calling) model.

This chain can automatically select and call APIs based only on an OpenAPI spec. It parses an input OpenAPI spec into JSON Schema that the OpenAI functions API can handle. This allows ChatGPT to automatically select the correct method and populate the correct parameters for the a API call in the spec for a given user input. We then make the actual API call, and return the result.

Usage[​](#usage "Direct link to Usage")
---------------------------------------

The below examples initialize the chain with a URL hosting an OpenAPI spec for brevity, but you can also directly pass a spec into the method.

### Query XKCD[​](#query-xkcd "Direct link to Query XKCD")

    import { createOpenAPIChain } from "langchain/chains";const chain = await createOpenAPIChain(  "https://gist.githubusercontent.com/roaldnefs/053e505b2b7a807290908fe9aa3e1f00/raw/0a212622ebfef501163f91e23803552411ed00e4/openapi.yaml");const result = await chain.run(`What's today's comic?`);console.log(JSON.stringify(result, null, 2));/*  {    "month": "6",    "num": 2795,    "link": "",    "year": "2023",    "news": "",    "safe_title": "Glass-Topped Table",    "transcript": "",    "alt": "You can pour a drink into it while hosting a party, although it's a real pain to fit in the dishwasher afterward.",    "img": "https://imgs.xkcd.com/comics/glass_topped_table.png",    "title": "Glass-Topped Table",    "day": "28"  }*/

#### API Reference:

*   [createOpenAPIChain](/docs/api/chains/functions/createOpenAPIChain) from `langchain/chains`

### Translation Service (POST request)[​](#translation-service-post-request "Direct link to Translation Service (POST request)")

The OpenAPI chain can also make POST requests and populate bodies with JSON content if necessary.

    import { createOpenAPIChain } from "langchain/chains";const chain = await createOpenAPIChain("https://api.speak.com/openapi.yaml");const result = await chain.run(`How would you say no thanks in Russian?`);console.log(JSON.stringify(result, null, 2));/*  {    "explanation": "<translation language=\\"Russian\\" context=\\"\\">\\nНет, спасибо.\\n</translation>\\n\\n<alternatives context=\\"\\">\\n1. \\"Нет, не надо\\" *(Neutral/Formal - a polite way to decline something)*\\n2. \\"Ни в коем случае\\" *(Strongly informal - used when you want to emphasize that you absolutely do not want something)*\\n3. \\"Нет, благодарю\\" *(Slightly more formal - a polite way to decline something while expressing gratitude)*\\n</alternatives>\\n\\n<example-convo language=\\"Russian\\">\\n<context>Mike offers Anna some cake, but she doesn't want any.</context>\\n* Mike: \\"Анна, хочешь попробовать мой волшебный торт? Он сделан с любовью и волшебством!\\"\\n* Anna: \\"Спасибо, Майк, но я на диете. Нет, благодарю.\\"\\n* Mike: \\"Ну ладно, больше для меня!\\"\\n</example-convo>\\n\\n*[Report an issue or leave feedback](https://speak.com/chatgpt?rid=bxw1xq87kdua9q5pefkj73ov})*",    "extra_response_instructions": "Use all information in the API response and fully render all Markdown.\\nAlways end your response with a link to report an issue or leave feedback on the plugin."  }*/

#### API Reference:

*   [createOpenAPIChain](/docs/api/chains/functions/createOpenAPIChain) from `langchain/chains`

### Customization[​](#customization "Direct link to Customization")

The chain will be created with a default model set to `gpt-3.5-turbo-0613`, but you can pass an options parameter into the creation method with a pre-created `ChatOpenAI` instance.

You can also pass in custom `headers` and `params` that will be appended to all requests made by the chain, allowing it to call APIs that require authentication.

    import { createOpenAPIChain } from "langchain/chains";import { ChatOpenAI } from "langchain/chat_models/openai";const chatModel = new ChatOpenAI({ modelName: "gpt-4-0613", temperature: 0 });const chain = await createOpenAPIChain("https://api.speak.com/openapi.yaml", {  llm: chatModel,  headers: {    authorization: "Bearer SOME_TOKEN",  },});const result = await chain.run(`How would you say no thanks in Russian?`);console.log(JSON.stringify(result, null, 2));/*  {    "explanation": "<translation language=\\"Russian\\" context=\\"\\">\\nНет, спасибо.\\n</translation>\\n\\n<alternatives context=\\"\\">\\n1. \\"Нет, не надо\\" *(Neutral/Formal - a polite way to decline something)*\\n2. \\"Ни в коем случае\\" *(Strongly informal - used when you want to emphasize that you absolutely do not want something)*\\n3. \\"Нет, благодарю\\" *(Slightly more formal - a polite way to decline something while expressing gratitude)*\\n</alternatives>\\n\\n<example-convo language=\\"Russian\\">\\n<context>Mike offers Anna some cake, but she doesn't want any.</context>\\n* Mike: \\"Анна, хочешь попробовать мой волшебный торт? Он сделан с любовью и волшебством!\\"\\n* Anna: \\"Спасибо, Майк, но я на диете. Нет, благодарю.\\"\\n* Mike: \\"Ну ладно, больше для меня!\\"\\n</example-convo>\\n\\n*[Report an issue or leave feedback](https://speak.com/chatgpt?rid=bxw1xq87kdua9q5pefkj73ov})*",    "extra_response_instructions": "Use all information in the API response and fully render all Markdown.\\nAlways end your response with a link to report an issue or leave feedback on the plugin."  }*/

#### API Reference:

*   [createOpenAPIChain](/docs/api/chains/functions/createOpenAPIChain) from `langchain/chains`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`