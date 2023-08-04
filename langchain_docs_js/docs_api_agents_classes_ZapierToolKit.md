ZapierToolKit
=============

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Toolkit`](/docs/api/agents/classes/Toolkit).**ZapierToolKit**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new ZapierToolKit**(): [`ZapierToolKit`](/docs/api/agents/classes/ZapierToolKit)

#### Returns[](#returns "Direct link to Returns")

[`ZapierToolKit`](/docs/api/agents/classes/ZapierToolKit)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[Toolkit](/docs/api/agents/classes/Toolkit).[constructor](/docs/api/agents/classes/Toolkit#constructor)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### tools[](#tools "Direct link to tools")

> **tools**: [`Tool`](/docs/api/tools/classes/Tool)\[\] = `[]`

#### Overrides[](#overrides "Direct link to Overrides")

[Toolkit](/docs/api/agents/classes/Toolkit).[tools](/docs/api/agents/classes/Toolkit#tools)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/agents/toolkits/zapier/zapier.ts:6](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/zapier/zapier.ts#L6)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### fromZapierNLAWrapper()[](#fromzapiernlawrapper "Direct link to fromZapierNLAWrapper()")

> `Static` **fromZapierNLAWrapper**(`zapierNLAWrapper`: [`ZapierNLAWrapper`](/docs/api/tools/classes/ZapierNLAWrapper)): `Promise`<[`ZapierToolKit`](/docs/api/agents/classes/ZapierToolKit)\>

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`zapierNLAWrapper`

[`ZapierNLAWrapper`](/docs/api/tools/classes/ZapierNLAWrapper)

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`ZapierToolKit`](/docs/api/agents/classes/ZapierToolKit)\>

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/toolkits/zapier/zapier.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/zapier/zapier.ts#L8)