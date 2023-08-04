AI21
====

Base interface for language model parameters. A subclass of [BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel) should have a constructor that takes in a parameter that extends this interface.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`LLM`](/docs/api/llms_base/classes/LLM).**AI21**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`AI21Input`](/docs/api/llms_ai21/interfaces/AI21Input)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new AI21**(`fields`?: [`AI21Input`](/docs/api/llms_ai21/interfaces/AI21Input)): [`AI21`](/docs/api/llms_ai21/classes/AI21)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`AI21Input`](/docs/api/llms_ai21/interfaces/AI21Input)

#### Returns[](#returns "Direct link to Returns")

[`AI21`](/docs/api/llms_ai21/classes/AI21)

#### Overrides[](#overrides "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[constructor](/docs/api/llms_base/classes/LLM#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/llms/ai21.ts:56](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L56)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[](#calloptions "Direct link to CallOptions")

> **CallOptions**: [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[CallOptions](/docs/api/llms_base/classes/LLM#calloptions)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:110](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L110) [langchain/src/base\_language/index.ts:115](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L115)

### ParsedCallOptions[](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[ParsedCallOptions](/docs/api/llms_base/classes/LLM#parsedcalloptions)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:49](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L49)

### caller[](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[caller](/docs/api/llms_base/classes/LLM#caller)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:128](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L128)

### countPenalty[](#countpenalty "Direct link to countPenalty")

> **countPenalty**: [`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[countPenalty](/docs/api/llms_ai21/interfaces/AI21Input#countpenalty)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:42](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L42)

### frequencyPenalty[](#frequencypenalty "Direct link to frequencyPenalty")

> **frequencyPenalty**: [`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[frequencyPenalty](/docs/api/llms_ai21/interfaces/AI21Input#frequencypenalty)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L44)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_kwargs](/docs/api/llms_base/classes/LLM#lc_kwargs)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_namespace](/docs/api/llms_base/classes/LLM#lc_namespace)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/base.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L54)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_serializable](/docs/api/llms_base/classes/LLM#lc_serializable)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### maxTokens[](#maxtokens "Direct link to maxTokens")

> **maxTokens**: `number` = `1024`

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[maxTokens](/docs/api/llms_ai21/interfaces/AI21Input#maxtokens)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L34)

### minTokens[](#mintokens "Direct link to minTokens")

> **minTokens**: `number` = `0`

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[minTokens](/docs/api/llms_ai21/interfaces/AI21Input#mintokens)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:36](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L36)

### model[](#model "Direct link to model")

> **model**: `string` = `"j2-jumbo-instruct"`

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[model](/docs/api/llms_ai21/interfaces/AI21Input#model)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:30](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L30)

### numResults[](#numresults "Direct link to numResults")

> **numResults**: `number` = `1`

#### Implementation of[](#implementation-of-5 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[numResults](/docs/api/llms_ai21/interfaces/AI21Input#numresults)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L46)

### presencePenalty[](#presencepenalty "Direct link to presencePenalty")

> **presencePenalty**: [`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Implementation of[](#implementation-of-6 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[presencePenalty](/docs/api/llms_ai21/interfaces/AI21Input#presencepenalty)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:40](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L40)

### temperature[](#temperature "Direct link to temperature")

> **temperature**: `number` = `0.7`

#### Implementation of[](#implementation-of-7 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[temperature](/docs/api/llms_ai21/interfaces/AI21Input#temperature)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:32](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L32)

### topP[](#topp "Direct link to topP")

> **topP**: `number` = `1`

#### Implementation of[](#implementation-of-8 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[topP](/docs/api/llms_ai21/interfaces/AI21Input#topp)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L38)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[](#implementation-of-9 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[verbose](/docs/api/llms_ai21/interfaces/AI21Input#verbose)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[verbose](/docs/api/llms_base/classes/LLM#verbose)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L44)

### ai21ApiKey?[](#ai21apikey "Direct link to ai21ApiKey?")

> **ai21ApiKey**: `string`

#### Implementation of[](#implementation-of-10 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[ai21ApiKey](/docs/api/llms_ai21/interfaces/AI21Input#ai21apikey)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L50)

### baseUrl?[](#baseurl "Direct link to baseUrl?")

> **baseUrl**: `string`

#### Implementation of[](#implementation-of-11 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[baseUrl](/docs/api/llms_ai21/interfaces/AI21Input#baseurl)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L54)

### cache?[](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Implementation of[](#implementation-of-12 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[cache](/docs/api/llms_ai21/interfaces/AI21Input#cache)

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[cache](/docs/api/llms_base/classes/LLM#cache)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/llms/base.ts:56](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L56)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[](#implementation-of-13 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[callbacks](/docs/api/llms_ai21/interfaces/AI21Input#callbacks)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[callbacks](/docs/api/llms_base/classes/LLM#callbacks)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L46)

### logitBias?[](#logitbias "Direct link to logitBias?")

> **logitBias**: `Record`<`string`, `number`\>

#### Implementation of[](#implementation-of-14 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[logitBias](/docs/api/llms_ai21/interfaces/AI21Input#logitbias)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L48)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[](#implementation-of-15 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[metadata](/docs/api/llms_ai21/interfaces/AI21Input#metadata)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[metadata](/docs/api/llms_base/classes/LLM#metadata)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L50)

### stop?[](#stop "Direct link to stop?")

> **stop**: `string`\[\]

#### Implementation of[](#implementation-of-16 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[stop](/docs/api/llms_ai21/interfaces/AI21Input#stop)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L52)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[](#implementation-of-17 "Direct link to Implementation of")

[AI21Input](/docs/api/llms_ai21/interfaces/AI21Input).[tags](/docs/api/llms_ai21/interfaces/AI21Input#tags)

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[tags](/docs/api/llms_base/classes/LLM#tags)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L48)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_runnable](/docs/api/llms_base/classes/LLM#lc_runnable)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

LLM.callKeys

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:120](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L120)

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[callKeys](/docs/api/llms_base/classes/LLM#callkeys)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:120](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L120)

### defaultParams[](#defaultparams "Direct link to defaultParams")

Get the default parameters for calling AI21 API.

> **defaultParams**(): `object`

#### Returns[](#returns-2 "Direct link to Returns")

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

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:100](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L100)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:100](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L100)

### identifyingParams[](#identifyingparams "Direct link to identifyingParams")

Get the identifying parameters for this LLM.

> **identifyingParams**(): `object`

#### Returns[](#returns-3 "Direct link to Returns")

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

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:115](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L115)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:115](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L115)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

LLM.lc\_aliases

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_aliases](/docs/api/llms_base/classes/LLM#lc_aliases)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

LLM.lc\_attributes

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_attributes](/docs/api/llms_base/classes/LLM#lc_attributes)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-6 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

LLM.lc\_secrets

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_secrets](/docs/api/llms_base/classes/LLM#lc_secrets)

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_call()[](#_call "Direct link to _call")

Call out to AI21's complete endpoint. Args: prompt: The prompt to pass into the model. stop: Optional list of stop words to use when generating.

    Returns:

The string generated by the model.

Example: let response = ai21.\_call("Tell me a joke.");

> **\_call**(`prompt`: `string`, `options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>): `Promise`<`string`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<`string`\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[\_call](/docs/api/llms_base/classes/LLM#_call)

#### Defined in[](#defined-in-38 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:130](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L130)

### \_flattenLLMResult()[](#_flattenllmresult "Direct link to _flattenllmresult")

> **\_flattenLLMResult**(`llmResult`: [`LLMResult`](/docs/api/schema/types/LLMResult)): [`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`llmResult`

[`LLMResult`](/docs/api/schema/types/LLMResult)

#### Returns[](#returns-8 "Direct link to Returns")

[`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_flattenLLMResult](/docs/api/llms_base/classes/LLM#_flattenllmresult)

#### Defined in[](#defined-in-39 "Direct link to Defined in")

[langchain/src/llms/base.ts:197](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L197)

### \_generate()[](#_generate "Direct link to _generate")

Run the LLM on the given prompts and input.

> **\_generate**(`prompts`: `string`\[\], `options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[](#returns-9 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_generate](/docs/api/llms_base/classes/LLM#_generate)

#### Defined in[](#defined-in-40 "Direct link to Defined in")

[langchain/src/llms/base.ts:435](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L435)

### \_identifyingParams()[](#_identifyingparams "Direct link to _identifyingparams")

Get the identifying parameters of the LLM.

> **\_identifyingParams**(): `Record`<`string`, `any`\>

#### Returns[](#returns-10 "Direct link to Returns")

`Record`<`string`, `any`\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_identifyingParams](/docs/api/llms_base/classes/LLM#_identifyingparams)

#### Defined in[](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/base.ts:374](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L374)

### \_llmType()[](#_llmtype "Direct link to _llmtype")

Get the type of LLM.

> **\_llmType**(): `string`

#### Returns[](#returns-11 "Direct link to Returns")

`string`

#### Overrides[](#overrides-2 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[\_llmType](/docs/api/llms_base/classes/LLM#_llmtype)

#### Defined in[](#defined-in-42 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:95](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L95)

### \_modelType()[](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[](#returns-12 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_modelType](/docs/api/llms_base/classes/LLM#_modeltype)

#### Defined in[](#defined-in-43 "Direct link to Defined in")

[langchain/src/llms/base.ts:394](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L394)

### \_patchConfig()[](#_patchconfig "Direct link to _patchconfig")

> **\_patchConfig**(`config`: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\> = `{}`, `callbackManager`: `undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager) = `undefined`): `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

Default value

`config`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

`{}`

`callbackManager`

`undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

`undefined`

#### Returns[](#returns-13 "Direct link to Returns")

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_patchConfig](/docs/api/llms_base/classes/LLM#_patchconfig)

#### Defined in[](#defined-in-44 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)): `AsyncGenerator`<`string`, `any`, `unknown`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

#### Returns[](#returns-14 "Direct link to Returns")

`AsyncGenerator`<`string`, `any`, `unknown`\>

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_streamIterator](/docs/api/llms_base/classes/LLM#_streamiterator)

#### Defined in[](#defined-in-45 "Direct link to Defined in")

[langchain/src/llms/base.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L102)

### \_streamResponseChunks()[](#_streamresponsechunks "Direct link to _streamresponsechunks")

> **\_streamResponseChunks**(`_input`: `string`, `_options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>, `_runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `AsyncGenerator`<[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk), `any`, `unknown`\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`_input`

`string`

`_options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>

`_runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[](#returns-15 "Direct link to Returns")

`AsyncGenerator`<[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk), `any`, `unknown`\>

#### Inherited from[](#inherited-from-26 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_streamResponseChunks](/docs/api/llms_base/classes/LLM#_streamresponsechunks)

#### Defined in[](#defined-in-46 "Direct link to Defined in")

[langchain/src/llms/base.ts:83](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L83)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\], `options`?: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\> | `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\], `batchOptions`?: `object`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`inputs`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\]

`options?`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\> | `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-27 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[batch](/docs/api/llms_base/classes/LLM#batch)

#### Defined in[](#defined-in-47 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `string`, [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Returns[](#returns-17 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `string`, [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Inherited from[](#inherited-from-28 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[bind](/docs/api/llms_base/classes/LLM#bind)

#### Defined in[](#defined-in-48 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### call()[](#call "Direct link to call()")

Convenience wrapper for [generate](/docs/api/llms_base/classes/BaseLLM#generate) that takes in a single string prompt and returns a single string output.

> **call**(`prompt`: `string`, `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-18 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-29 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[call](/docs/api/llms_base/classes/LLM#call)

#### Defined in[](#defined-in-49 "Direct link to Defined in")

[langchain/src/llms/base.ts:343](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L343)

### generate()[](#generate "Direct link to generate()")

Run the LLM on the given prompts and input, handling caching.

> **generate**(`prompts`: `string`\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-19 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[](#inherited-from-30 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[generate](/docs/api/llms_base/classes/LLM#generate)

#### Defined in[](#defined-in-50 "Direct link to Defined in")

[langchain/src/llms/base.ts:280](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L280)

### generatePrompt()[](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-20 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[](#inherited-from-31 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[generatePrompt](/docs/api/llms_base/classes/LLM#generateprompt)

#### Defined in[](#defined-in-51 "Direct link to Defined in")

[langchain/src/llms/base.ts:169](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L169)

### getNumTokens()[](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[](#returns-21 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[](#inherited-from-32 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[getNumTokens](/docs/api/llms_base/classes/LLM#getnumtokens)

#### Defined in[](#defined-in-52 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:166](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L166)

### invocationParams()[](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`_options`?: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>): `any`

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`_options?`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>

#### Returns[](#returns-22 "Direct link to Returns")

`any`

#### Inherited from[](#inherited-from-33 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[invocationParams](/docs/api/llms_base/classes/LLM#invocationparams)

#### Defined in[](#defined-in-53 "Direct link to Defined in")

[langchain/src/llms/base.ts:193](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L193)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)): `Promise`<`string`\>

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

#### Returns[](#returns-23 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-34 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[invoke](/docs/api/llms_base/classes/LLM#invoke)

#### Defined in[](#defined-in-54 "Direct link to Defined in")

[langchain/src/llms/base.ts:69](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L69)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>

#### Returns[](#returns-24 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Inherited from[](#inherited-from-35 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[pipe](/docs/api/llms_base/classes/LLM#pipe)

#### Defined in[](#defined-in-55 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### predict()[](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-25 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-36 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[predict](/docs/api/llms_base/classes/LLM#predict)

#### Defined in[](#defined-in-56 "Direct link to Defined in")

[langchain/src/llms/base.ts:352](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L352)

### predictMessages()[](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[](#parameters-17 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-26 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[](#inherited-from-37 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[predictMessages](/docs/api/llms_base/classes/LLM#predictmessages)

#### Defined in[](#defined-in-57 "Direct link to Defined in")

[langchain/src/llms/base.ts:360](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L360)

### serialize()[](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[](#returns-27 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Inherited from[](#inherited-from-38 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[serialize](/docs/api/llms_base/classes/LLM#serialize)

#### Defined in[](#defined-in-58 "Direct link to Defined in")

[langchain/src/llms/base.ts:386](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L386)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>): `Promise`<`IterableReadableStream`<`string`\>\>

#### Parameters[](#parameters-18 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Returns[](#returns-28 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`string`\>\>

#### Inherited from[](#inherited-from-39 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[stream](/docs/api/llms_base/classes/LLM#stream)

#### Defined in[](#defined-in-59 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-29 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-40 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[toJSON](/docs/api/llms_base/classes/LLM#tojson)

#### Defined in[](#defined-in-60 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-30 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-41 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[toJSONNotImplemented](/docs/api/llms_base/classes/LLM#tojsonnotimplemented)

#### Defined in[](#defined-in-61 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### validateEnvironment()[](#validateenvironment "Direct link to validateEnvironment()")

> **validateEnvironment**(): `void`

#### Returns[](#returns-31 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-62 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:75](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L75)

### deserialize()[](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\>

#### Parameters[](#parameters-19 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[](#returns-32 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\>

#### Inherited from[](#inherited-from-42 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[deserialize](/docs/api/llms_base/classes/LLM#deserialize)

#### Defined in[](#defined-in-63 "Direct link to Defined in")

[langchain/src/llms/base.ts:401](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L401)

### getDefaultAI21PenaltyData()[](#getdefaultai21penaltydata "Direct link to getDefaultAI21PenaltyData()")

> `Static` **getDefaultAI21PenaltyData**(): [`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Returns[](#returns-33 "Direct link to Returns")

[`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Defined in[](#defined-in-64 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:83](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/ai21.ts#L83)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-20 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-34 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-43 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[isRunnable](/docs/api/llms_base/classes/LLM#isrunnable)

#### Defined in[](#defined-in-65 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`string`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Parameters[](#parameters-21 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`string`\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-35 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-44 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_callWithConfig](/docs/api/llms_base/classes/LLM#_callwithconfig)

#### Defined in[](#defined-in-66 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\> | `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\], `length`: `number` = `0`): `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\]

#### Parameters[](#parameters-22 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\> | `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-36 "Direct link to Returns")

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\]

#### Inherited from[](#inherited-from-45 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_getOptionsList](/docs/api/llms_base/classes/LLM#_getoptionslist)

#### Defined in[](#defined-in-67 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`?: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>): \[`BaseCallbackConfig`, `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>\]

#### Parameters[](#parameters-23 "Direct link to Parameters")

Parameter

Type

`options?`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Returns[](#returns-37 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>\]

#### Inherited from[](#inherited-from-46 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_separateRunnableConfigFromCallOptions](/docs/api/llms_base/classes/LLM#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-68 "Direct link to Defined in")

[langchain/src/llms/base.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L91)

### \_convertInputToPromptValue()[](#_convertinputtopromptvalue "Direct link to _convertinputtopromptvalue")

> `Static` `Protected` **\_convertInputToPromptValue**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)): [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Parameters[](#parameters-24 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Returns[](#returns-38 "Direct link to Returns")

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Inherited from[](#inherited-from-47 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_convertInputToPromptValue](/docs/api/llms_base/classes/LLM#_convertinputtopromptvalue)

#### Defined in[](#defined-in-69 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:192](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L192)