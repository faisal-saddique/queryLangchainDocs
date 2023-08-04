BaseStepExecutor
================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ChainStepExecutor`](/docs/api/experimental_plan_and_execute/classes/ChainStepExecutor)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new BaseStepExecutor**(): [`BaseStepExecutor`](/docs/api/experimental_plan_and_execute/classes/BaseStepExecutor)

#### Returns[](#returns "Direct link to Returns")

[`BaseStepExecutor`](/docs/api/experimental_plan_and_execute/classes/BaseStepExecutor)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### step()[](#step "Direct link to step()")

> `Abstract` **step**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `runManager`?: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)): `Promise`<[`StepResult`](/docs/api/experimental_plan_and_execute/types/StepResult)\>

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`runManager?`

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`StepResult`](/docs/api/experimental_plan_and_execute/types/StepResult)\>

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:32](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/plan_and_execute/base.ts#L32)