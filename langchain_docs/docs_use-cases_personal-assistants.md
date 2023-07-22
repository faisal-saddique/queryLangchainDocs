Personal Assistants
===================

info

[Python Guide](https://python.langchain.com/en/latest/use_cases/personal_assistants.html)

[JS Guide](https://js.langchain.com/docs/use_cases/personal_assistants/)

Personal assistants are a perfect application to build because they combine both of the core value props of LangChain (action taking and personalized data). In order to build a personal assistant you should understand the following concepts:

1.  PromptTemplate - this will guide how your personal assistant acts. Are they sassy? Helpful? These can be used to give your personal assistant some character.
2.  Memory - your personal assistant should probably remember things. They should definitely be able to hold a conversation (short term memory) and they should probably have some concept of long term memory as well.
3.  Tools - your personal assistant will be differentiated by the tools you give it. What should it know how to do?
4.  Agent - your personal assistant will have to understand what actions it should take. Constructing the best agent possible will be important.
5.  Agent Executor - after you've got your tools and your agent, in order to put it into practice you'll need to set up an environment for the agent to use those tools. This is where the Agent Executor comes into play.