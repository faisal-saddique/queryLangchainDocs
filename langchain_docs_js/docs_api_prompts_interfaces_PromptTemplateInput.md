PromptTemplateInput
===================

Inputs to create a [PromptTemplate](/docs/api/prompts/classes/PromptTemplate)

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BasePromptTemplateInput`](/docs/api/prompts/interfaces/BasePromptTemplateInput).**PromptTemplateInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### inputVariables[](#inputvariables "Direct link to inputVariables")

> **inputVariables**: `string`\[\]

A list of variable names the prompt template expects

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BasePromptTemplateInput](/docs/api/prompts/interfaces/BasePromptTemplateInput).[inputVariables](/docs/api/prompts/interfaces/BasePromptTemplateInput#inputvariables)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/prompts/base.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L41)

### template[](#template "Direct link to template")

> **template**: `string`

The prompt template

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/prompt.ts#L19)

### outputParser?[](#outputparser "Direct link to outputParser?")

> **outputParser**: [`BaseOutputParser`](/docs/api/schema_output_parser/classes/BaseOutputParser)<`unknown`\>

How to parse the output of calling an LLM on this formatted prompt

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BasePromptTemplateInput](/docs/api/prompts/interfaces/BasePromptTemplateInput).[outputParser](/docs/api/prompts/interfaces/BasePromptTemplateInput#outputparser)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/prompts/base.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L46)

### partialVariables?[](#partialvariables "Direct link to partialVariables?")

> **partialVariables**: [`PartialValues`](/docs/api/schema/types/PartialValues)

Partial variables

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BasePromptTemplateInput](/docs/api/prompts/interfaces/BasePromptTemplateInput).[partialVariables](/docs/api/prompts/interfaces/BasePromptTemplateInput#partialvariables)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/prompts/base.ts:49](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L49)

### templateFormat?[](#templateformat "Direct link to templateFormat?")

> **templateFormat**: [`TemplateFormat`](/docs/api/prompts/types/TemplateFormat)

The format of the prompt template. Options are 'f-string', 'jinja-2'

#### Default Value[](#default-value "Direct link to Default Value")

'f-string'

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/prompt.ts#L26)

### validateTemplate?[](#validatetemplate "Direct link to validateTemplate?")

> **validateTemplate**: `boolean`

Whether or not to try validating the template on initialization

#### Default Value[](#default-value-1 "Direct link to Default Value")

`true`

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:33](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/prompt.ts#L33)