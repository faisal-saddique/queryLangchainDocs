BaseStepContainer
=================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ListStepContainer`](/docs/api/experimental_plan_and_execute/classes/ListStepContainer)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new BaseStepContainer**(): [`BaseStepContainer`](/docs/api/experimental_plan_and_execute/classes/BaseStepContainer)

#### Returns[](#returns "Direct link to Returns")

[`BaseStepContainer`](/docs/api/experimental_plan_and_execute/classes/BaseStepContainer)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### addStep()[](#addstep "Direct link to addStep()")

> `Abstract` **addStep**(`action`: [`StepAction`](/docs/api/experimental_plan_and_execute/types/StepAction), `result`: [`StepResult`](/docs/api/experimental_plan_and_execute/types/StepResult)): `void`

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`action`

[`StepAction`](/docs/api/experimental_plan_and_execute/types/StepAction)

`result`

[`StepResult`](/docs/api/experimental_plan_and_execute/types/StepResult)

#### Returns[](#returns-1 "Direct link to Returns")

`void`

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:39](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/plan_and_execute/base.ts#L39)

### getFinalResponse()[](#getfinalresponse "Direct link to getFinalResponse()")

> `Abstract` **getFinalResponse**(): `string`

#### Returns[](#returns-2 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:43](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/plan_and_execute/base.ts#L43)

### getSteps()[](#getsteps "Direct link to getSteps()")

> `Abstract` **getSteps**(): [`Step`](/docs/api/experimental_plan_and_execute/types/Step)\[\]

#### Returns[](#returns-3 "Direct link to Returns")

[`Step`](/docs/api/experimental_plan_and_execute/types/Step)\[\]

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/base.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/plan_and_execute/base.ts#L41)