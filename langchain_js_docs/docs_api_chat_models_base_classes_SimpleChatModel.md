SimpleChatModel
===============

Base class for language models.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatModel`](/docs/api/chat_models_base/classes/BaseChatModel).**SimpleChatModel**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new SimpleChatModel**(`fields`: [`BaseLanguageModelParams`](/docs/api/base_language/interfaces/BaseLanguageModelParams)): [`SimpleChatModel`](/docs/api/chat_models_base/classes/SimpleChatModel)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`BaseLanguageModelParams`](/docs/api/base_language/interfaces/BaseLanguageModelParams)

#### Returns[​](#returns "Direct link to Returns")

[`SimpleChatModel`](/docs/api/chat_models_base/classes/SimpleChatModel)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[constructor](/docs/api/chat_models_base/classes/BaseChatModel#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L50)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[​](#calloptions "Direct link to CallOptions")

> **CallOptions**: [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[CallOptions](/docs/api/chat_models_base/classes/BaseChatModel#calloptions)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L41)

### ParsedCallOptions[​](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[ParsedCallOptions](/docs/api/chat_models_base/classes/BaseChatModel#parsedcalloptions)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L43)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[caller](/docs/api/chat_models_base/classes/BaseChatModel#caller)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L116)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_kwargs](/docs/api/chat_models_base/classes/BaseChatModel#lc_kwargs)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_namespace](/docs/api/chat_models_base/classes/BaseChatModel#lc_namespace)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:48](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L48)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_serializable](/docs/api/chat_models_base/classes/BaseChatModel#lc_serializable)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[verbose](/docs/api/chat_models_base/classes/BaseChatModel#verbose)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[callbacks](/docs/api/chat_models_base/classes/BaseChatModel#callbacks)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[metadata](/docs/api/chat_models_base/classes/BaseChatModel#metadata)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[tags](/docs/api/chat_models_base/classes/BaseChatModel#tags)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[​](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

BaseChatModel.callKeys

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[callKeys](/docs/api/chat_models_base/classes/BaseChatModel#callkeys)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

BaseChatModel.lc\_aliases

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_aliases](/docs/api/chat_models_base/classes/BaseChatModel#lc_aliases)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

BaseChatModel.lc\_attributes

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_attributes](/docs/api/chat_models_base/classes/BaseChatModel#lc_attributes)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

BaseChatModel.lc\_secrets

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_secrets](/docs/api/chat_models_base/classes/BaseChatModel#lc_secrets)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_call()[​](#_call "Direct link to _call")

> `Abstract` **\_call**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`: `Omit`<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `Promise`<`string`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options`

`Omit`<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:220](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L220)

### \_generate()[​](#_generate "Direct link to _generate")

> **\_generate**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`: `Omit`<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `Promise`<[`ChatResult`](/docs/api/schema/interfaces/ChatResult)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options`

`Omit`<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`ChatResult`](/docs/api/schema/interfaces/ChatResult)\>

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_generate](/docs/api/chat_models_base/classes/BaseChatModel#_generate)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:226](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L226)

### \_identifyingParams()[​](#_identifyingparams "Direct link to _identifyingparams")

Get the identifying parameters of the LLM.

> **\_identifyingParams**(): `Record`<`string`, `any`\>

#### Returns[​](#returns-7 "Direct link to Returns")

`Record`<`string`, `any`\>

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_identifyingParams](/docs/api/chat_models_base/classes/BaseChatModel#_identifyingparams)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:184](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L184)

### \_llmType()[​](#_llmtype "Direct link to _llmtype")

> `Abstract` **\_llmType**(): `string`

#### Returns[​](#returns-8 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_llmType](/docs/api/chat_models_base/classes/BaseChatModel#_llmtype)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:162](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L162)

### \_modelType()[​](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[​](#returns-9 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_modelType](/docs/api/chat_models_base/classes/BaseChatModel#_modeltype)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:158](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L158)

### call()[​](#call "Direct link to call()")

> **call**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[call](/docs/api/chat_models_base/classes/BaseChatModel#call)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:181](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L181)

### callPrompt()[​](#callprompt "Direct link to callPrompt()")

> **callPrompt**(`promptValue`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue), `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`promptValue`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[callPrompt](/docs/api/chat_models_base/classes/BaseChatModel#callprompt)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:191](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L191)

### generate()[​](#generate "Direct link to generate()")

> **generate**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\[\], `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\[\]

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-24 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[generate](/docs/api/chat_models_base/classes/BaseChatModel#generate)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L58)

### generatePrompt()[​](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-13 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-25 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[generatePrompt](/docs/api/chat_models_base/classes/BaseChatModel#generateprompt)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:164](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L164)

### getNumTokens()[​](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-14 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[​](#inherited-from-26 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[getNumTokens](/docs/api/chat_models_base/classes/BaseChatModel#getnumtokens)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L154)

### invocationParams()[​](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`_options`?: `Omit`<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>): `any`

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`_options?`

`Omit`<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-15 "Direct link to Returns")

`any`

#### Inherited from[​](#inherited-from-27 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[invocationParams](/docs/api/chat_models_base/classes/BaseChatModel#invocationparams)

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L154)

### predict()[​](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-16 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-28 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[predict](/docs/api/chat_models_base/classes/BaseChatModel#predict)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:208](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L208)

### predictMessages()[​](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-17 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-29 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[predictMessages](/docs/api/chat_models_base/classes/BaseChatModel#predictmessages)

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:200](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L200)

### serialize()[​](#serialize "Direct link to serialize()")

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Returns[​](#returns-18 "Direct link to Returns")

[`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Inherited from[​](#inherited-from-30 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[serialize](/docs/api/chat_models_base/classes/BaseChatModel#serialize)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:192](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L192)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-19 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-31 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[toJSON](/docs/api/chat_models_base/classes/BaseChatModel#tojson)

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-20 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-32 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[toJSONNotImplemented](/docs/api/chat_models_base/classes/BaseChatModel#tojsonnotimplemented)

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### \_combineLLMOutput()?[​](#_combinellmoutput "Direct link to _combinellmoutput")

> `Optional` `Abstract` **\_combineLLMOutput**(...`llmOutputs`: (`undefined` | `Record`<`string`, `any`\>)\[\]): `undefined` | `Record`<`string`, `any`\>

#### Parameters[​](#parameters-11 "Direct link to Parameters")

Parameter

Type

`...llmOutputs`

(`undefined` | `Record`<`string`, `any`\>)\[\]

#### Returns[​](#returns-21 "Direct link to Returns")

`undefined` | `Record`<`string`, `any`\>

#### Inherited from[​](#inherited-from-33 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_combineLLMOutput](/docs/api/chat_models_base/classes/BaseChatModel#_combinellmoutput)

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:54](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L54)

### deserialize()[​](#deserialize "Direct link to deserialize()")

#### Deprecated[​](#deprecated-1 "Direct link to Deprecated")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)): `Promise`<[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Parameters[​](#parameters-12 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Returns[​](#returns-22 "Direct link to Returns")

`Promise`<[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Inherited from[​](#inherited-from-34 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[deserialize](/docs/api/chat_models_base/classes/BaseChatModel#deserialize)

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:204](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L204)