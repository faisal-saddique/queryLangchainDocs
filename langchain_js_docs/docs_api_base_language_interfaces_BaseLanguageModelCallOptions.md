BaseLanguageModelCallOptions
============================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `BaseCallbackConfig`.**BaseLanguageModelCallOptions**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

Callbacks for this call and any sub-calls (eg. a Chain calling an LLM). Tags are passed to all callbacks, metadata is passed to handle\*Start callbacks.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

BaseCallbackConfig.callbacks

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:61](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L61)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

Metadata for this call and any sub-calls (eg. a Chain calling an LLM). Keys should be strings, values should be JSON-serializable.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

BaseCallbackConfig.metadata

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L55)

### signal?[​](#signal "Direct link to signal?")

> **signal**: `AbortSignal`

Abort signal for this call. If provided, the call will be aborted when the signal is aborted.

#### See[​](#see "Direct link to See")

[https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:93](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L93)

### stop?[​](#stop "Direct link to stop?")

> **stop**: `string`\[\]

Stop tokens to use for this call. If not provided, the default stop tokens for the model will be used.

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:81](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L81)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

Tags for this call and any sub-calls (eg. a Chain calling an LLM). You can use these to filter calls.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

BaseCallbackConfig.tags

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L49)

### timeout?[​](#timeout "Direct link to timeout?")

> **timeout**: `number`

Timeout for this call in milliseconds.

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:86](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L86)