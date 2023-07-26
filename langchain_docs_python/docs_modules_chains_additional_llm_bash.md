Bash chain
==========

This notebook showcases using LLMs and a bash process to perform simple filesystem commands.

    from langchain.chains import LLMBashChainfrom langchain.llms import OpenAIllm = OpenAI(temperature=0)text = "Please write a bash script that prints 'Hello World' to the console."bash_chain = LLMBashChain.from_llm(llm, verbose=True)bash_chain.run(text)

                > Entering new LLMBashChain chain...    Please write a bash script that prints 'Hello World' to the console.        ```
bash    echo "Hello World"    
```    Code: ['echo "Hello World"']    Answer: Hello World        > Finished chain.    'Hello World\n'

Customize Prompt[](#customize-prompt "Direct link to Customize Prompt")
------------------------------------------------------------------------

You can also customize the prompt that is used. Here is an example prompting to avoid using the 'echo' utility

    from langchain.prompts.prompt import PromptTemplatefrom langchain.chains.llm_bash.prompt import BashOutputParser_PROMPT_TEMPLATE = """If someone asks you to perform a task, your job is to come up with a series of bash commands that will perform the task. There is no need to put "#!/bin/bash" in your answer. Make sure to reason step by step, using this format:Question: "copy the files in the directory named 'target' into a new directory at the same level as target called 'myNewDirectory'"I need to take the following actions:- List all files in the directory- Create a new directory- Copy the files from the first directory into the second directory```
bashlsmkdir myNewDirectorycp -r target/* myNewDirectory

Do not use 'echo' when writing the script.

That is the format. Begin! Question: {question}"""

PROMPT = PromptTemplate( input\_variables=\["question"\], template=\_PROMPT\_TEMPLATE, output\_parser=BashOutputParser(), )


```pythonbash_chain = LLMBashChain.from_llm(llm, prompt=PROMPT, verbose=True)text = "Please write a bash script that prints 'Hello World' to the console."bash_chain.run(text)

                > Entering new LLMBashChain chain...    Please write a bash script that prints 'Hello World' to the console.        ```
bash    printf "Hello World\n"    
```    Code: ['printf "Hello World\\n"']    Answer: Hello World        > Finished chain.    'Hello World\n'

Persistent Terminal[](#persistent-terminal "Direct link to Persistent Terminal")
---------------------------------------------------------------------------------

By default, the chain will run in a separate subprocess each time it is called. This behavior can be changed by instantiating with a persistent bash process.

    from langchain.utilities.bash import BashProcesspersistent_process = BashProcess(persistent=True)bash_chain = LLMBashChain.from_llm(llm, bash_process=persistent_process, verbose=True)text = "List the current directory then move up a level."bash_chain.run(text)

                > Entering new LLMBashChain chain...    List the current directory then move up a level.        ```
bash    ls    cd ..    
```    Code: ['ls', 'cd ..']    Answer: api.html            llm_summarization_checker.html    constitutional_chain.html   moderation.html    llm_bash.html           openai_openapi.yaml    llm_checker.html        openapi.html    llm_math.html           pal.html    llm_requests.html       sqlite.html    > Finished chain.    'api.html\t\t\tllm_summarization_checker.html\r\nconstitutional_chain.html\tmoderation.html\r\nllm_bash.html\t\t\topenai_openapi.yaml\r\nllm_checker.html\t\topenapi.html\r\nllm_math.html\t\t\tpal.html\r\nllm_requests.html\t\tsqlite.html'

    # Run the same command again and see that the state is maintained between callsbash_chain.run(text)

                > Entering new LLMBashChain chain...    List the current directory then move up a level.        ```
bash    ls    cd ..    
```    Code: ['ls', 'cd ..']    Answer: examples        getting_started.html    index_examples    generic         how_to_guides.rst    > Finished chain.    'examples\t\tgetting_started.html\tindex_examples\r\ngeneric\t\t\thow_to_guides.rst'