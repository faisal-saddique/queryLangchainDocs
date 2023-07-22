ChainStepExecutor
=================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseStepExecutor`](/docs/api/experimental_plan_and_execute/classes/BaseStepExecutor).**ChainStepExecutor**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new ChainStepExecutor**(`chain`: [`BaseChain`](/docs/api/chains/classes/BaseChain)): [`ChainStepExecutor`](/docs/api/experimental_plan_and_execute/classes/ChainStepExecutor)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`chain`

[`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Returns[​](#returns "Direct link to Returns")

[`ChainStepExecutor`](/docs/api/experimental_plan_and_execute/classes/ChainStepExecutor)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseStepExecutor](/docs/api/experimental_plan_and_execute/classes/BaseStepExecutor).[constructor](/docs/api/experimental_plan_and_execute/classes/BaseStepExecutor#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:77](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/plan_and_execute/base.ts#L77)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### step()[​](#step "Direct link to step()")

> **step**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `runManager`?: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)): `Promise`<[`StepResult`](/docs/api/experimental_plan_and_execute/types/StepResult)\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`runManager?`

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`StepResult`](/docs/api/experimental_plan_and_execute/types/StepResult)\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseStepExecutor](/docs/api/experimental_plan_and_execute/classes/BaseStepExecutor).[step](/docs/api/experimental_plan_and_execute/classes/BaseStepExecutor#step)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:81](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/plan_and_execute/base.ts#L81)