ListStepContainer
=================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseStepContainer`](/docs/api/experimental_plan_and_execute/classes/BaseStepContainer).**ListStepContainer**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new ListStepContainer**(): [`ListStepContainer`](/docs/api/experimental_plan_and_execute/classes/ListStepContainer)

#### Returns[​](#returns "Direct link to Returns")

[`ListStepContainer`](/docs/api/experimental_plan_and_execute/classes/ListStepContainer)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseStepContainer](/docs/api/experimental_plan_and_execute/classes/BaseStepContainer).[constructor](/docs/api/experimental_plan_and_execute/classes/BaseStepContainer#constructor)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### addStep()[​](#addstep "Direct link to addStep()")

> **addStep**(`action`: [`StepAction`](/docs/api/experimental_plan_and_execute/types/StepAction), `result`: [`StepResult`](/docs/api/experimental_plan_and_execute/types/StepResult)): `void`

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`action`

[`StepAction`](/docs/api/experimental_plan_and_execute/types/StepAction)

`result`

[`StepResult`](/docs/api/experimental_plan_and_execute/types/StepResult)

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseStepContainer](/docs/api/experimental_plan_and_execute/classes/BaseStepContainer).[addStep](/docs/api/experimental_plan_and_execute/classes/BaseStepContainer#addstep)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/plan_and_execute/base.ts#L49)

### getFinalResponse()[​](#getfinalresponse "Direct link to getFinalResponse()")

> **getFinalResponse**(): `string`

#### Returns[​](#returns-2 "Direct link to Returns")

`string`

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseStepContainer](/docs/api/experimental_plan_and_execute/classes/BaseStepContainer).[getFinalResponse](/docs/api/experimental_plan_and_execute/classes/BaseStepContainer#getfinalresponse)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/plan_and_execute/base.ts#L57)

### getSteps()[​](#getsteps "Direct link to getSteps()")

> **getSteps**(): [`Step`](/docs/api/experimental_plan_and_execute/types/Step)\[\]

#### Returns[​](#returns-3 "Direct link to Returns")

[`Step`](/docs/api/experimental_plan_and_execute/types/Step)\[\]

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseStepContainer](/docs/api/experimental_plan_and_execute/classes/BaseStepContainer).[getSteps](/docs/api/experimental_plan_and_execute/classes/BaseStepContainer#getsteps)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/plan_and_execute/base.ts#L53)