RELLM
=====

[RELLM](https://github.com/r2d4/rellm) is a library that wraps local Hugging Face pipeline models for structured decoding.

It works by generating tokens one at a time. At each step, it masks tokens that don't conform to the provided partial regular expression.

**Warning - this module is still experimental**

    pip install rellm > /dev/null

### Hugging Face Baseline[](#hugging-face-baseline "Direct link to Hugging Face Baseline")

First, let's establish a qualitative baseline by checking the output of the model without structured decoding.

    import logginglogging.basicConfig(level=logging.ERROR)prompt = """Human: "What's the capital of the United States?"AI Assistant:{  "action": "Final Answer",  "action_input": "The capital of the United States is Washington D.C."}Human: "What's the capital of Pennsylvania?"AI Assistant:{  "action": "Final Answer",  "action_input": "The capital of Pennsylvania is Harrisburg."}Human: "What 2 + 5?"AI Assistant:{  "action": "Final Answer",  "action_input": "2 + 5 = 7."}Human: 'What's the capital of Maryland?'AI Assistant:"""

    from transformers import pipelinefrom langchain.llms import HuggingFacePipelinehf_model = pipeline(    "text-generation", model="cerebras/Cerebras-GPT-590M", max_new_tokens=200)original_model = HuggingFacePipeline(pipeline=hf_model)generated = original_model.generate([prompt], stop=["Human:"])print(generated)

        Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.    generations=[[Generation(text=' "What\'s the capital of Maryland?"\n', generation_info=None)]] llm_output=None

**_That's not so impressive, is it? It didn't answer the question and it didn't follow the JSON format at all! Let's try with the structured decoder._**

RELLM LLM Wrapper[](#rellm-llm-wrapper "Direct link to RELLM LLM Wrapper")
---------------------------------------------------------------------------

Let's try that again, now providing a regex to match the JSON structured format.

    import regex  # Note this is the regex library NOT python's re stdlib module# We'll choose a regex that matches to a structured json string that looks like:# {#  "action": "Final Answer",# "action_input": string or dict# }pattern = regex.compile(    r'\{\s*"action":\s*"Final Answer",\s*"action_input":\s*(\{.*\}|"[^"]*")\s*\}\nHuman:')

    from langchain.experimental.llms import RELLMmodel = RELLM(pipeline=hf_model, regex=pattern, max_new_tokens=200)generated = model.predict(prompt, stop=["Human:"])print(generated)

        {"action": "Final Answer",      "action_input": "The capital of Maryland is Baltimore."    }    

**Voila! Free of parsing errors.**