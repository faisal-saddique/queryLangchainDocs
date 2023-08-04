ZeroShotCreatePromptArgs
========================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`AWSSfnCreatePromptArgs`](/docs/api/agents_toolkits_aws_sfn/interfaces/AWSSfnCreatePromptArgs)
*   [`SqlCreatePromptArgs`](/docs/api/agents_toolkits_sql/interfaces/SqlCreatePromptArgs)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### inputVariables?[](#inputvariables "Direct link to inputVariables?")

> **inputVariables**: `string`\[\]

List of input variables the final prompt will expect.

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/agents/mrkl/index.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/mrkl/index.ts#L23)

### prefix?[](#prefix "Direct link to prefix?")

> **prefix**: `string`

String to put before the list of tools.

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/mrkl/index.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/mrkl/index.ts#L21)

### suffix?[](#suffix "Direct link to suffix?")

> **suffix**: `string`

String to put after the list of tools.

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/agents/mrkl/index.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/mrkl/index.ts#L19)