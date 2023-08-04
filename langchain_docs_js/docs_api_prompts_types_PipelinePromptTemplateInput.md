PipelinePromptTemplateInput<PromptTemplateType\>
================================================

> **PipelinePromptTemplateInput**: <`PromptTemplateType`\> `Omit`<[`BasePromptTemplateInput`](/docs/api/prompts/interfaces/BasePromptTemplateInput), "inputVariables"\> & {`finalPrompt`: `PromptTemplateType`; `pipelinePrompts`: [`PipelinePromptParams`](/docs/api/prompts/types/PipelinePromptParams)<`PromptTemplateType`\>\[\];}

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `PromptTemplateType` _extends_ [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/prompts/pipeline.ts:13](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/pipeline.ts#L13)