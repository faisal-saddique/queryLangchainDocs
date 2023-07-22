TaskPrioritizationChain
=======================

Chain to prioritize tasks.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`LLMChain`](/docs/api/chains/classes/LLMChain).**TaskPrioritizationChain**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new TaskPrioritizationChain**(`fields`: [`LLMChainInput`](/docs/api/chains/interfaces/LLMChainInput)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>): [`TaskPrioritizationChain`](/docs/api/experimental_babyagi/classes/TaskPrioritizationChain)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`LLMChainInput`](/docs/api/chains/interfaces/LLMChainInput)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Returns[​](#returns "Direct link to Returns")

[`TaskPrioritizationChain`](/docs/api/experimental_babyagi/classes/TaskPrioritizationChain)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[constructor](/docs/api/chains/classes/LLMChain#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L70)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[lc\_kwargs](/docs/api/chains/classes/LLMChain#lc_kwargs)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[lc\_serializable](/docs/api/chains/classes/LLMChain#lc_serializable)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L50)

### llm[​](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

LLM Wrapper to use

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[llm](/docs/api/chains/classes/LLMChain#llm)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:54](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L54)

### outputKey[​](#outputkey "Direct link to outputKey")

> **outputKey**: `string` = `"text"`

Key to use for output, defaults to `text`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[outputKey](/docs/api/chains/classes/LLMChain#outputkey)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L58)

### prompt[​](#prompt "Direct link to prompt")

> **prompt**: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)

Prompt object to use

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[prompt](/docs/api/chains/classes/LLMChain#prompt)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:52](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L52)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[verbose](/docs/api/chains/classes/LLMChain#verbose)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[callbacks](/docs/api/chains/classes/LLMChain#callbacks)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### llmKwargs?[​](#llmkwargs "Direct link to llmKwargs?")

> **llmKwargs**: [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

Kwargs to pass to LLM

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[llmKwargs](/docs/api/chains/classes/LLMChain#llmkwargs)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L56)

### memory?[​](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[memory](/docs/api/chains/classes/LLMChain#memory)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/chains/base.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L29)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[metadata](/docs/api/chains/classes/LLMChain#metadata)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### outputParser?[​](#outputparser "Direct link to outputParser?")

> **outputParser**: [`BaseLLMOutputParser`](/docs/api/schema_output_parser/classes/BaseLLMOutputParser)<`string`\>

OutputParser to use

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[outputParser](/docs/api/chains/classes/LLMChain#outputparser)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:60](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L60)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[tags](/docs/api/chains/classes/LLMChain#tags)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### inputKeys[​](#inputkeys "Direct link to inputKeys")

> **inputKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

LLMChain.inputKeys

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:62](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L62)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[inputKeys](/docs/api/chains/classes/LLMChain#inputkeys)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:62](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L62)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

LLMChain.lc\_aliases

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[lc\_aliases](/docs/api/chains/classes/LLMChain#lc_aliases)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

LLMChain.lc\_attributes

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[lc\_attributes](/docs/api/chains/classes/LLMChain#lc_attributes)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[​](#returns-4 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

LLMChain.lc\_namespace

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[lc\_namespace](/docs/api/chains/classes/LLMChain#lc_namespace)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

LLMChain.lc\_secrets

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[lc\_secrets](/docs/api/chains/classes/LLMChain#lc_secrets)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

### outputKeys[​](#outputkeys "Direct link to outputKeys")

> **outputKeys**(): `string`\[\]

#### Returns[​](#returns-6 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

LLMChain.outputKeys

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L66)

#### Inherited from[​](#inherited-from-24 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[outputKeys](/docs/api/chains/classes/LLMChain#outputkeys)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L66)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_chainType()[​](#_chaintype "Direct link to _chaintype")

Return the string type key uniquely identifying this class of chain.

> **\_chainType**(): "llm"

#### Returns[​](#returns-7 "Direct link to Returns")

"llm"

#### Inherited from[​](#inherited-from-25 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[\_chainType](/docs/api/chains/classes/LLMChain#_chaintype)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:178](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L178)

### apply()[​](#apply "Direct link to apply()")

Call the chain on all inputs in the list

> **apply**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues)\[\], `config`?: ([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]

`config?`

([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Inherited from[​](#inherited-from-26 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[apply](/docs/api/chains/classes/LLMChain#apply)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/chains/base.ts:192](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L192)

### call()[​](#call "Direct link to call()")

Run the core logic of this chain and add to output if desired.

Wraps \_call and handles memory.

> **call**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues) & [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`values`

[`ChainValues`](/docs/api/schema/types/ChainValues) & [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Inherited from[​](#inherited-from-27 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[call](/docs/api/chains/classes/LLMChain#call)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:121](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L121)

### predict()[​](#predict "Direct link to predict()")

Format prompt with values and pass to LLM

#### Example[​](#example "Direct link to Example")

    llm.predict({ adjective: "funny" });

> **predict**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues) & [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbackManager`?: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)): `Promise`<`string`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

Description

`values`

[`ChainValues`](/docs/api/schema/types/ChainValues) & [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

keys to pass to prompt template

`callbackManager?`

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

CallbackManager to use

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`string`\>

Completion from LLM.

#### Inherited from[​](#inherited-from-28 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[predict](/docs/api/chains/classes/LLMChain#predict)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:170](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L170)

### run()[​](#run "Direct link to run()")

> **run**(`input`: `any`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<`string`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`input`

`any`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-29 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[run](/docs/api/chains/classes/LLMChain#run)

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/chains/base.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L94)

### serialize()[​](#serialize "Direct link to serialize()")

#### Deprecated[​](#deprecated "Direct link to Deprecated")

> **serialize**(): [`SerializedLLMChain`](/docs/api/chains/types/SerializedLLMChain)

#### Returns[​](#returns-12 "Direct link to Returns")

[`SerializedLLMChain`](/docs/api/chains/types/SerializedLLMChain)

#### Inherited from[​](#inherited-from-30 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[serialize](/docs/api/chains/classes/LLMChain#serialize)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:198](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L198)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-13 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-31 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[toJSON](/docs/api/chains/classes/LLMChain#tojson)

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-14 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-32 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[toJSONNotImplemented](/docs/api/chains/classes/LLMChain#tojsonnotimplemented)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load a chain from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLMChain`](/docs/api/chains/types/SerializedLLMChain)): `Promise`<[`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLMChain`](/docs/api/chains/types/SerializedLLMChain)

#### Returns[​](#returns-15 "Direct link to Returns")

`Promise`<[`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>\>

#### Inherited from[​](#inherited-from-33 "Direct link to Inherited from")

[LLMChain](/docs/api/chains/classes/LLMChain).[deserialize](/docs/api/chains/classes/LLMChain#deserialize)

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:182](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L182)

### fromLLM()[​](#fromllm "Direct link to fromLLM()")

> `Static` **fromLLM**(`fields`: `Omit`<[`LLMChainInput`](/docs/api/chains/interfaces/LLMChainInput)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>, "prompt"\>): [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`fields`

`Omit`<[`LLMChainInput`](/docs/api/chains/interfaces/LLMChainInput)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>, "prompt"\>

#### Returns[​](#returns-16 "Direct link to Returns")

[`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/experimental/babyagi/task\_prioritization.ts:6](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/task_prioritization.ts#L6)