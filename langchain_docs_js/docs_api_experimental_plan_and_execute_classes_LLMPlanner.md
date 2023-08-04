LLMPlanner
==========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BasePlanner`](/docs/api/experimental_plan_and_execute/classes/BasePlanner).**LLMPlanner**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new LLMPlanner**(`llmChain`: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>, `outputParser`: [`BaseOutputParser`](/docs/api/schema_output_parser/classes/BaseOutputParser)<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>): [`LLMPlanner`](/docs/api/experimental_plan_and_execute/classes/LLMPlanner)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`llmChain`

[`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

`outputParser`

[`BaseOutputParser`](/docs/api/schema_output_parser/classes/BaseOutputParser)<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Returns[](#returns "Direct link to Returns")

[`LLMPlanner`](/docs/api/experimental_plan_and_execute/classes/LLMPlanner)

#### Overrides[](#overrides "Direct link to Overrides")

[BasePlanner](/docs/api/experimental_plan_and_execute/classes/BasePlanner).[constructor](/docs/api/experimental_plan_and_execute/classes/BasePlanner#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/plan_and_execute/base.ts#L63)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### plan()[](#plan "Direct link to plan()")

> **plan**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `runManager`?: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)): `Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`runManager?`

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BasePlanner](/docs/api/experimental_plan_and_execute/classes/BasePlanner).[plan](/docs/api/experimental_plan_and_execute/classes/BasePlanner#plan)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/plan_and_execute/base.ts#L70)