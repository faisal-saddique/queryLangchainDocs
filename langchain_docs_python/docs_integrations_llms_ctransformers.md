C Transformers
==============

The [C Transformers](https://github.com/marella/ctransformers) library provides Python bindings for GGML models.

This example goes over how to use LangChain to interact with `C Transformers` [models](https://github.com/marella/ctransformers#supported-models).

**Install**

    %pip install ctransformers

**Load Model**

    from langchain.llms import CTransformersllm = CTransformers(model="marella/gpt-2-ggml")

**Generate Text**

    print(llm("AI is going to"))

**Streaming**

    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandlerllm = CTransformers(    model="marella/gpt-2-ggml", callbacks=[StreamingStdOutCallbackHandler()])response = llm("AI is going to")

**LLMChain**

    from langchain import PromptTemplate, LLMChaintemplate = """Question: {question}Answer:"""prompt = PromptTemplate(template=template, input_variables=["question"])llm_chain = LLMChain(prompt=prompt, llm=llm)response = llm_chain.run("What is AI?")