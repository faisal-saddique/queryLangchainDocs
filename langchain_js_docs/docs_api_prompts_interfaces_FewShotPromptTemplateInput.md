FewShotPromptTemplateInput
==========================

Input common to all prompt templates.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BasePromptTemplateInput`](/docs/api/prompts/interfaces/BasePromptTemplateInput).**FewShotPromptTemplateInput**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### examplePrompt[​](#exampleprompt "Direct link to examplePrompt")

> **examplePrompt**: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

An [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) used to format a single example.

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/prompts/few\_shot.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/few_shot.ts#L33)

### inputVariables[​](#inputvariables "Direct link to inputVariables")

> **inputVariables**: `string`\[\]

A list of variable names the prompt template expects

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BasePromptTemplateInput](/docs/api/prompts/interfaces/BasePromptTemplateInput).[inputVariables](/docs/api/prompts/interfaces/BasePromptTemplateInput#inputvariables)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/prompts/base.ts:39](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L39)

### exampleSelector?[​](#exampleselector "Direct link to exampleSelector?")

> **exampleSelector**: [`BaseExampleSelector`](/docs/api/prompts/classes/BaseExampleSelector)

An [BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector) Examples to format into the prompt. Exactly one of this or [examples](/docs/api/prompts/interfaces/FewShotPromptTemplateInput#examples) must be provided.

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/prompts/few\_shot.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/few_shot.ts#L28)

### exampleSeparator?[​](#exampleseparator "Direct link to exampleSeparator?")

> **exampleSeparator**: `string`

String separator used to join the prefix, the examples, and suffix.

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/prompts/few\_shot.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/few_shot.ts#L38)

### examples?[​](#examples "Direct link to examples?")

> **examples**: [`Example`](/docs/api/schema/types/Example)\[\]

Examples to format into the prompt. Exactly one of this or [exampleSelector](/docs/api/prompts/interfaces/FewShotPromptTemplateInput#exampleselector) must be provided.

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/prompts/few\_shot.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/few_shot.ts#L21)

### outputParser?[​](#outputparser "Direct link to outputParser?")

> **outputParser**: [`BaseOutputParser`](/docs/api/schema_output_parser/classes/BaseOutputParser)<`unknown`\>

How to parse the output of calling an LLM on this formatted prompt

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BasePromptTemplateInput](/docs/api/prompts/interfaces/BasePromptTemplateInput).[outputParser](/docs/api/prompts/interfaces/BasePromptTemplateInput#outputparser)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/prompts/base.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L44)

### partialVariables?[​](#partialvariables "Direct link to partialVariables?")

> **partialVariables**: [`PartialValues`](/docs/api/schema/types/PartialValues)

Partial variables

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BasePromptTemplateInput](/docs/api/prompts/interfaces/BasePromptTemplateInput).[partialVariables](/docs/api/prompts/interfaces/BasePromptTemplateInput#partialvariables)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/prompts/base.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L47)

### prefix?[​](#prefix "Direct link to prefix?")

> **prefix**: `string`

A prompt template string to put before the examples.

#### Default Value[​](#default-value "Direct link to Default Value")

`""`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/prompts/few\_shot.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/few_shot.ts#L45)

### suffix?[​](#suffix "Direct link to suffix?")

> **suffix**: `string`

A prompt template string to put after the examples.

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/prompts/few\_shot.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/few_shot.ts#L50)

### templateFormat?[​](#templateformat "Direct link to templateFormat?")

> **templateFormat**: [`TemplateFormat`](/docs/api/prompts/types/TemplateFormat)

The format of the prompt template. Options are: 'f-string', 'jinja-2'

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/prompts/few\_shot.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/few_shot.ts#L55)

### validateTemplate?[​](#validatetemplate "Direct link to validateTemplate?")

> **validateTemplate**: `boolean`

Whether or not to try validating the template on initialization.

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/prompts/few\_shot.ts:60](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/few_shot.ts#L60)