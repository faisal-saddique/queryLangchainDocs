BasePlanner
===========

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`LLMPlanner`](/docs/api/experimental_plan_and_execute/classes/LLMPlanner)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BasePlanner**(): [`BasePlanner`](/docs/api/experimental_plan_and_execute/classes/BasePlanner)

#### Returns[​](#returns "Direct link to Returns")

[`BasePlanner`](/docs/api/experimental_plan_and_execute/classes/BasePlanner)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### plan()[​](#plan "Direct link to plan()")

> `Abstract` **plan**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `runManager`?: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)): `Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`runManager?`

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/plan_and_execute/base.ts#L25)