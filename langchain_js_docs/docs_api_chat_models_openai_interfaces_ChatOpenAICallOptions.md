ChatOpenAICallOptions
=====================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions).**ChatOpenAICallOptions**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

Callbacks for this call and any sub-calls (eg. a Chain calling an LLM). Tags are passed to all callbacks, metadata is passed to handle\*Start callbacks.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[OpenAICallOptions](/docs/api/llms_openai/interfaces/OpenAICallOptions).[callbacks](/docs/api/llms_openai/interfaces/OpenAICallOptions#callbacks)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:61](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L61)

### function\_call?[​](#function_call "Direct link to function_call?")

> **function\_call**: `CreateChatCompletionRequestFunctionCall`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:87](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/openai.ts#L87)

### functions?[​](#functions "Direct link to functions?")

> **functions**: `ChatCompletionFunctions`\[\]

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:88](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/openai.ts#L88)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

Metadata for this call and any sub-calls (eg. a Chain calling an LLM). Keys should be strings, values should be JSON-serializable.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[OpenAICallOptions](/docs/api/llms_openai/interfaces/OpenAICallOptions).[metadata](/docs/api/llms_openai/interfaces/OpenAICallOptions#metadata)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L55)

### options?[​](#options "Direct link to options?")

> **options**: `AxiosRequestConfig`<`any`\>

Additional options to pass to the underlying axios request.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[OpenAICallOptions](/docs/api/llms_openai/interfaces/OpenAICallOptions).[options](/docs/api/llms_openai/interfaces/OpenAICallOptions#options)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:63](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L63)

### promptIndex?[​](#promptindex "Direct link to promptIndex?")

> **promptIndex**: `number`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/openai.ts#L90)

### signal?[​](#signal "Direct link to signal?")

> **signal**: `AbortSignal`

Abort signal for this call. If provided, the call will be aborted when the signal is aborted.

#### See[​](#see "Direct link to See")

[https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[OpenAICallOptions](/docs/api/llms_openai/interfaces/OpenAICallOptions).[signal](/docs/api/llms_openai/interfaces/OpenAICallOptions#signal)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:93](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L93)

### stop?[​](#stop "Direct link to stop?")

> **stop**: `string`\[\]

Stop tokens to use for this call. If not provided, the default stop tokens for the model will be used.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[OpenAICallOptions](/docs/api/llms_openai/interfaces/OpenAICallOptions).[stop](/docs/api/llms_openai/interfaces/OpenAICallOptions#stop)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:81](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L81)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

Tags for this call and any sub-calls (eg. a Chain calling an LLM). You can use these to filter calls.

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[OpenAICallOptions](/docs/api/llms_openai/interfaces/OpenAICallOptions).[tags](/docs/api/llms_openai/interfaces/OpenAICallOptions#tags)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L49)

### timeout?[​](#timeout "Direct link to timeout?")

> **timeout**: `number`

Timeout for this call in milliseconds.

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[OpenAICallOptions](/docs/api/llms_openai/interfaces/OpenAICallOptions).[timeout](/docs/api/llms_openai/interfaces/OpenAICallOptions#timeout)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:86](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L86)

### tools?[​](#tools "Direct link to tools?")

> **tools**: [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\]

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:89](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/openai.ts#L89)