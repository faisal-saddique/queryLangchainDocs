AI21
====

Base interface for language model parameters. A subclass of [BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel) should have a constructor that takes in a parameter that extends this interface.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`LLM`](/docs/api/llms_base/classes/LLM).**AI21**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`AI21Input`](/docs/api/llms_ai21/interfaces/AI21Input)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new AI21**(`fields`?: [`AI21Input`](/docs/api/llms_ai21/interfaces/AI21Input)): [`AI21`](/docs/api/llms_ai21/classes/AI21)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`AI21Input`](/docs/api/llms_ai21/interfaces/AI21Input)

#### Returns[​](#returns "Direct link to Returns")

[`AI21`](/docs/api/llms_ai21/classes/AI21)

#### Overrides[​](#overrides "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[constructor](/docs/api/llms_base/classes/LLM#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/llms/ai21.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L56)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[​](#calloptions "Direct link to CallOptions")

> **CallOptions**: [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[CallOptions](/docs/api/llms_base/classes/LLM#calloptions)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/llms/base.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L44)

### ParsedCallOptions[​](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[ParsedCallOptions](/docs/api/llms_base/classes/LLM#parsedcalloptions)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L46)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[caller](/docs/api/llms_base/classes/LLM#caller)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L116)

### countPenalty[​](#countpenalty "Direct link to countPenalty")

> **countPenalty**: [`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[countPenalty](/docs/api/llms_ai21/interfaces/AI21Input#countpenalty)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L42)

### frequencyPenalty[​](#frequencypenalty "Direct link to frequencyPenalty")

> **frequencyPenalty**: [`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[frequencyPenalty](/docs/api/llms_ai21/interfaces/AI21Input#frequencypenalty)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L44)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_kwargs](/docs/api/llms_base/classes/LLM#lc_kwargs)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_namespace](/docs/api/llms_base/classes/LLM#lc_namespace)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/base.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L51)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_serializable](/docs/api/llms_base/classes/LLM#lc_serializable)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### maxTokens[​](#maxtokens "Direct link to maxTokens")

> **maxTokens**: `number` = `1024`

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[maxTokens](/docs/api/llms_ai21/interfaces/AI21Input#maxtokens)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L34)

### minTokens[​](#mintokens "Direct link to minTokens")

> **minTokens**: `number` = `0`

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[minTokens](/docs/api/llms_ai21/interfaces/AI21Input#mintokens)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L36)

### model[​](#model "Direct link to model")

> **model**: `string` = `"j2-jumbo-instruct"`

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[model](/docs/api/llms_ai21/interfaces/AI21Input#model)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L30)

### numResults[​](#numresults "Direct link to numResults")

> **numResults**: `number` = `1`

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[numResults](/docs/api/llms_ai21/interfaces/AI21Input#numresults)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L46)

### presencePenalty[​](#presencepenalty "Direct link to presencePenalty")

> **presencePenalty**: [`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[presencePenalty](/docs/api/llms_ai21/interfaces/AI21Input#presencepenalty)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L40)

### temperature[​](#temperature "Direct link to temperature")

> **temperature**: `number` = `0.7`

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[temperature](/docs/api/llms_ai21/interfaces/AI21Input#temperature)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L32)

### topP[​](#topp "Direct link to topP")

> **topP**: `number` = `1`

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[topP](/docs/api/llms_ai21/interfaces/AI21Input#topp)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L38)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[​](#implementation-of-9 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[verbose](/docs/api/llms_ai21/interfaces/AI21Input#verbose)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[verbose](/docs/api/llms_base/classes/LLM#verbose)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### ai21ApiKey?[​](#ai21apikey "Direct link to ai21ApiKey?")

> **ai21ApiKey**: `string`

#### Implementation of[​](#implementation-of-10 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[ai21ApiKey](/docs/api/llms_ai21/interfaces/AI21Input#ai21apikey)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L50)

### baseUrl?[​](#baseurl "Direct link to baseUrl?")

> **baseUrl**: `string`

#### Implementation of[​](#implementation-of-11 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[baseUrl](/docs/api/llms_ai21/interfaces/AI21Input#baseurl)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:54](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L54)

### cache?[​](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Implementation of[​](#implementation-of-12 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[cache](/docs/api/llms_ai21/interfaces/AI21Input#cache)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[cache](/docs/api/llms_base/classes/LLM#cache)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/llms/base.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L53)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[​](#implementation-of-13 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[callbacks](/docs/api/llms_ai21/interfaces/AI21Input#callbacks)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[callbacks](/docs/api/llms_base/classes/LLM#callbacks)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### logitBias?[​](#logitbias "Direct link to logitBias?")

> **logitBias**: `Record`<`string`, `number`\>

#### Implementation of[​](#implementation-of-14 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[logitBias](/docs/api/llms_ai21/interfaces/AI21Input#logitbias)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:48](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L48)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[​](#implementation-of-15 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[metadata](/docs/api/llms_ai21/interfaces/AI21Input#metadata)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[metadata](/docs/api/llms_base/classes/LLM#metadata)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### stop?[​](#stop "Direct link to stop?")

> **stop**: `string`\[\]

#### Implementation of[​](#implementation-of-16 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[stop](/docs/api/llms_ai21/interfaces/AI21Input#stop)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:52](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L52)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[​](#implementation-of-17 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[tags](/docs/api/llms_ai21/interfaces/AI21Input#tags)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[tags](/docs/api/llms_base/classes/LLM#tags)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[​](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

LLM.callKeys

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[callKeys](/docs/api/llms_base/classes/LLM#callkeys)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

### defaultParams[​](#defaultparams "Direct link to defaultParams")

Get the default parameters for calling AI21 API.

> **defaultParams**(): `object`

#### Returns[​](#returns-2 "Direct link to Returns")

`object`

Member

Type

`countPenalty`

[`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

`frequencyPenalty`

[`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

`logitBias`

`undefined` | `Record`<`string`, `number`\>

`maxTokens`

`number`

`minTokens`

`number`

`numResults`

`number`

`presencePenalty`

[`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

`temperature`

`number`

`topP`

`number`

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:100](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L100)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:100](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L100)

### identifyingParams[​](#identifyingparams "Direct link to identifyingParams")

Get the identifying parameters for this LLM.

> **identifyingParams**(): `object`

#### Returns[​](#returns-3 "Direct link to Returns")

`object`

Member

Type

`countPenalty`

[`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

`frequencyPenalty`

[`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

`logitBias`

`undefined` | `Record`<`string`, `number`\>

`maxTokens`

`number`

`minTokens`

`number`

`model`

`string`

`numResults`

`number`

`presencePenalty`

[`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

`temperature`

`number`

`topP`

`number`

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:115](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L115)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:115](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L115)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

LLM.lc\_aliases

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_aliases](/docs/api/llms_base/classes/LLM#lc_aliases)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

LLM.lc\_attributes

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_attributes](/docs/api/llms_base/classes/LLM#lc_attributes)

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-6 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

LLM.lc\_secrets

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_secrets](/docs/api/llms_base/classes/LLM#lc_secrets)

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_call()[​](#_call "Direct link to _call")

Call out to AI21's complete endpoint. Args: prompt: The prompt to pass into the model. stop: Optional list of stop words to use when generating.

    Returns:

The string generated by the model.

Example: let response = ai21.\_call("Tell me a joke.");

> **\_call**(`prompt`: `string`, `options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>): `Promise`<`string`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`string`\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[\_call](/docs/api/llms_base/classes/LLM#_call)

#### Defined in[​](#defined-in-37 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:130](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L130)

### \_flattenLLMResult()[​](#_flattenllmresult "Direct link to _flattenllmresult")

> **\_flattenLLMResult**(`llmResult`: [`LLMResult`](/docs/api/schema/types/LLMResult)): [`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`llmResult`

[`LLMResult`](/docs/api/schema/types/LLMResult)

#### Returns[​](#returns-8 "Direct link to Returns")

[`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_flattenLLMResult](/docs/api/llms_base/classes/LLM#_flattenllmresult)

#### Defined in[​](#defined-in-38 "Direct link to Defined in")

[langchain/src/llms/base.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L94)

### \_generate()[​](#_generate "Direct link to _generate")

Run the LLM on the given prompts and input.

> **\_generate**(`prompts`: `string`\[\], `options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_generate](/docs/api/llms_base/classes/LLM#_generate)

#### Defined in[​](#defined-in-39 "Direct link to Defined in")

[langchain/src/llms/base.ts:343](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L343)

### \_identifyingParams()[​](#_identifyingparams "Direct link to _identifyingparams")

Get the identifying parameters of the LLM.

> **\_identifyingParams**(): `Record`<`string`, `any`\>

#### Returns[​](#returns-10 "Direct link to Returns")

`Record`<`string`, `any`\>

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_identifyingParams](/docs/api/llms_base/classes/LLM#_identifyingparams)

#### Defined in[​](#defined-in-40 "Direct link to Defined in")

[langchain/src/llms/base.ts:284](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L284)

### \_llmType()[​](#_llmtype "Direct link to _llmtype")

Get the type of LLM.

> **\_llmType**(): `string`

#### Returns[​](#returns-11 "Direct link to Returns")

`string`

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[\_llmType](/docs/api/llms_base/classes/LLM#_llmtype)

#### Defined in[​](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:95](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L95)

### \_modelType()[​](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[​](#returns-12 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_modelType](/docs/api/llms_base/classes/LLM#_modeltype)

#### Defined in[​](#defined-in-42 "Direct link to Defined in")

[langchain/src/llms/base.ts:304](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L304)

### call()[​](#call "Direct link to call()")

Convenience wrapper for [generate](/docs/api/llms_base/classes/BaseLLM#generate) that takes in a single string prompt and returns a single string output.

> **call**(`prompt`: `string`, `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-13 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[call](/docs/api/llms_base/classes/LLM#call)

#### Defined in[​](#defined-in-43 "Direct link to Defined in")

[langchain/src/llms/base.ts:249](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L249)

### generate()[​](#generate "Direct link to generate()")

Run the LLM on the given propmts an input, handling caching.

> **generate**(`prompts`: `string`\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-14 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-24 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[generate](/docs/api/llms_base/classes/LLM#generate)

#### Defined in[​](#defined-in-44 "Direct link to Defined in")

[langchain/src/llms/base.ts:177](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L177)

### generatePrompt()[​](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-15 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-25 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[generatePrompt](/docs/api/llms_base/classes/LLM#generateprompt)

#### Defined in[​](#defined-in-45 "Direct link to Defined in")

[langchain/src/llms/base.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L66)

### getNumTokens()[​](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-16 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[​](#inherited-from-26 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[getNumTokens](/docs/api/llms_base/classes/LLM#getnumtokens)

#### Defined in[​](#defined-in-46 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L154)

### invocationParams()[​](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`_options`?: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>): `any`

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`_options?`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-17 "Direct link to Returns")

`any`

#### Inherited from[​](#inherited-from-27 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[invocationParams](/docs/api/llms_base/classes/LLM#invocationparams)

#### Defined in[​](#defined-in-47 "Direct link to Defined in")

[langchain/src/llms/base.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L90)

### predict()[​](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-18 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-28 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[predict](/docs/api/llms_base/classes/LLM#predict)

#### Defined in[​](#defined-in-48 "Direct link to Defined in")

[langchain/src/llms/base.ts:262](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L262)

### predictMessages()[​](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-19 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-29 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[predictMessages](/docs/api/llms_base/classes/LLM#predictmessages)

#### Defined in[​](#defined-in-49 "Direct link to Defined in")

[langchain/src/llms/base.ts:270](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L270)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-20 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Inherited from[​](#inherited-from-30 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[serialize](/docs/api/llms_base/classes/LLM#serialize)

#### Defined in[​](#defined-in-50 "Direct link to Defined in")

[langchain/src/llms/base.ts:296](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L296)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-21 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-31 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[toJSON](/docs/api/llms_base/classes/LLM#tojson)

#### Defined in[​](#defined-in-51 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-22 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-32 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[toJSONNotImplemented](/docs/api/llms_base/classes/LLM#tojsonnotimplemented)

#### Defined in[​](#defined-in-52 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### validateEnvironment()[​](#validateenvironment "Direct link to validateEnvironment()")

> **validateEnvironment**(): `void`

#### Returns[​](#returns-23 "Direct link to Returns")

`void`

#### Defined in[​](#defined-in-53 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:75](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L75)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Parameters[​](#parameters-11 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-24 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Inherited from[​](#inherited-from-33 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[deserialize](/docs/api/llms_base/classes/LLM#deserialize)

#### Defined in[​](#defined-in-54 "Direct link to Defined in")

[langchain/src/llms/base.ts:311](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L311)

### getDefaultAI21PenaltyData()[​](#getdefaultai21penaltydata "Direct link to getDefaultAI21PenaltyData()")

> `Static` **getDefaultAI21PenaltyData**(): [`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Returns[​](#returns-25 "Direct link to Returns")

[`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Defined in[​](#defined-in-55 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:83](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L83)