Prompt Selector
===============

One of the goals of chains in LangChain is to enable people to get started with a particular use case as quickly as possible. A big part of this is having good prompts.

The problem is that a prompt that works for one model may not work as well for another model. We want to enable chains to work well for all types of models. Therefore, rather than hardcoding a default prompt to use in chains, we have the concept of a PromptSelector. This PromptSelector is responsible for choosing a default prompt depending on the model passed in.

The most common use case of PromptSelectors is to set different default prompts for LLMs vs Chat Models. However, this can also be used to set different default prompts for different model providers, should one choose.