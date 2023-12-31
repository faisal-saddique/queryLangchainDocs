BasePromptTemplateInput
=======================

Input common to all prompt templates.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`PromptTemplateInput`](/docs/api/prompts/interfaces/PromptTemplateInput)
*   [`FewShotPromptTemplateInput`](/docs/api/prompts/interfaces/FewShotPromptTemplateInput)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### inputVariables[](#inputvariables "Direct link to inputVariables")

> **inputVariables**: `string`\[\]

A list of variable names the prompt template expects

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/prompts/base.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L41)

### outputParser?[](#outputparser "Direct link to outputParser?")

> **outputParser**: [`BaseOutputParser`](/docs/api/schema_output_parser/classes/BaseOutputParser)<`unknown`\>

How to parse the output of calling an LLM on this formatted prompt

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/prompts/base.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L46)

### partialVariables?[](#partialvariables "Direct link to partialVariables?")

> **partialVariables**: [`PartialValues`](/docs/api/schema/types/PartialValues)

Partial variables

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/prompts/base.ts:49](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L49)