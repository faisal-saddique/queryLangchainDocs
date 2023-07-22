Replicate
=========

> [Replicate](https://replicate.com/blog/machine-learning-needs-better-tools) runs machine learning models in the cloud. We have a library of open-source models that you can run with a few lines of code. If you're building your own machine learning models, Replicate makes it easy to deploy them at scale.

This example goes over how to use LangChain to interact with `Replicate` [models](https://replicate.com/explore)

Setup[​](#setup "Direct link to Setup")
---------------------------------------

    # magics to auto-reload external modules in case you are making changes to langchain while working on this notebook%autoreload 2

To run this notebook, you'll need to create a [replicate](https://replicate.com) account and install the [replicate python client](https://github.com/replicate/replicate-python).

    pip install replicate

        Requirement already satisfied: replicate in /root/Source/github/docugami.langchain/.venv/lib/python3.9/site-packages (0.9.0)    Requirement already satisfied: packaging in /root/Source/github/docugami.langchain/.venv/lib/python3.9/site-packages (from replicate) (23.1)    Requirement already satisfied: pydantic>1 in /root/Source/github/docugami.langchain/.venv/lib/python3.9/site-packages (from replicate) (1.10.9)    Requirement already satisfied: requests>2 in /root/Source/github/docugami.langchain/.venv/lib/python3.9/site-packages (from replicate) (2.28.2)    Requirement already satisfied: typing-extensions>=4.2.0 in /root/Source/github/docugami.langchain/.venv/lib/python3.9/site-packages (from pydantic>1->replicate) (4.5.0)    Requirement already satisfied: charset-normalizer<4,>=2 in /root/Source/github/docugami.langchain/.venv/lib/python3.9/site-packages (from requests>2->replicate) (3.1.0)    Requirement already satisfied: idna<4,>=2.5 in /root/Source/github/docugami.langchain/.venv/lib/python3.9/site-packages (from requests>2->replicate) (3.4)    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /root/Source/github/docugami.langchain/.venv/lib/python3.9/site-packages (from requests>2->replicate) (1.26.16)    Requirement already satisfied: certifi>=2017.4.17 in /root/Source/github/docugami.langchain/.venv/lib/python3.9/site-packages (from requests>2->replicate) (2023.5.7)        [notice] A new release of pip is available: 23.1.2 -> 23.2    [notice] To update, run: pip install --upgrade pip

    # get a token: https://replicate.com/accountfrom getpass import getpassREPLICATE_API_TOKEN = getpass()

    import osos.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

    from langchain.llms import Replicatefrom langchain import PromptTemplate, LLMChain

Calling a model[​](#calling-a-model "Direct link to Calling a model")
---------------------------------------------------------------------

Find a model on the [replicate explore page](https://replicate.com/explore), and then paste in the model name and version in this format: model\_name/version.

For example, here is [`LLama-V2`](https://replicate.com/a16z-infra/llama13b-v2-chat).

    llm = Replicate(    model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",    input={"temperature": 0.75, "max_length": 500, "top_p": 1},)prompt = """User: Answer the following yes/no question by reasoning step by step. Can a dog drive a car?Assistant:"""llm(prompt)

        '1. Can a dog operate a vehicle? No.\n2. Do dogs have hands to manipulate the pedals and steering wheel? No.\n3. Can dogs see well enough to drive? No.\n4. Does a dog have the cognitive ability to understand traffic laws and make safe driving decisions? No.\n\nTherefore, the answer is no, a dog cannot drive a car.'

As another example, for this [dolly model](https://replicate.com/replicate/dolly-v2-12b), click on the API tab. The model name/version would be: `replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5`

Only the `model` param is required, but we can add other model params when initializing.

For example, if we were running stable diffusion and wanted to change the image dimensions:

    Replicate(model="stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf", input={'image_dimensions': '512x512'})

_Note that only the first output of a model will be returned._

    llm = Replicate(    model="replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5")

    prompt = """Answer the following yes/no question by reasoning step by step. Can a dog drive a car?"""llm(prompt)

        'It depends on how you define "can". Because dogs do have four legs, they are clearly able to move around in a car; it might even be possible for them to drive given proper training and enough motivation (e.g., food or comfort). From a legal perspective however, there are many reasons why this would not make sense at all: Dogs lack some of the vital capabilities required to safely operate a vehicle; their behaviour may differ significantly compared to humans due to their weaker cognitive abilities versus ours; and there could also exist valid concerns about safety since we don\'t really know what happens when two species with different psychological characteristics are put together under stressful conditions. Therefore, no, a dog cannot legally drive a car.\n\n'

We can call any replicate model using this syntax. For example, we can call stable diffusion.

    text2image = Replicate(    model="stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",    input={"image_dimensions": "512x512"},)

    image_output = text2image("A cat riding a motorcycle by Picasso")image_output

        'https://replicate.delivery/pbxt/j0nlxW0aoh7LExWGfdvyfgkmKA2GQWcF6e1wkYNWfoSakkHFB/out-0.png'

The model spits out a URL. Let's render it.

    pip install Pillow

        Requirement already satisfied: Pillow in /root/Source/github/docugami.langchain/.venv/lib/python3.9/site-packages (10.0.0)

    from PIL import Imageimport requestsfrom io import BytesIOresponse = requests.get(image_output)img = Image.open(BytesIO(response.content))img

        ![png](_replicate_files/output_18_0.png)    

Streaming Response[​](#streaming-response "Direct link to Streaming Response")
------------------------------------------------------------------------------

You can optionally stream the response as it is produced, which is helpful to show interactivity to users for time-consuming generations. See detailed docs on [Streaming](https://python.langchain.com/docs/modules/model_io/models/llms/how_to/streaming_llm) for more information.

    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandlerllm = Replicate(    streaming=True,    callbacks=[StreamingStdOutCallbackHandler()],    model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",    input={"temperature": 0.75, "max_length": 500, "top_p": 1},)prompt = """User: Answer the following yes/no question by reasoning step by step. Can a dog drive a car?Assistant:"""_ = llm(prompt)

        1. Dogs do not have the ability to operate complex machinery, such as cars.    2. Dogs do not have the cognitive ability to understand the concept of driving.    3. Dogs do not have the physical ability to reach the pedals or steering wheel of a car.    4. Dogs do not have the ability to communicate their intentions to other drivers or pedestrians.        Therefore, the answer is no, a dog cannot drive a car.

Chaining Calls[​](#chaining-calls "Direct link to Chaining Calls")
------------------------------------------------------------------

The whole point of langchain is to... chain! Here's an example of how do that.

    from langchain.chains import SimpleSequentialChain

First, let's define the LLM for this model as a flan-5, and text2image as a stable diffusion model.

    dolly_llm = Replicate(    model="replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5")text2image = Replicate(    model="stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")

First prompt in the chain

    prompt = PromptTemplate(    input_variables=["product"],    template="What is a good name for a company that makes {product}?",)chain = LLMChain(llm=dolly_llm, prompt=prompt)

Second prompt to get the logo for company description

    second_prompt = PromptTemplate(    input_variables=["company_name"],    template="Write a description of a logo for this company: {company_name}",)chain_two = LLMChain(llm=dolly_llm, prompt=second_prompt)

Third prompt, let's create the image based on the description output from prompt 2

    third_prompt = PromptTemplate(    input_variables=["company_logo_description"],    template="{company_logo_description}",)chain_three = LLMChain(llm=text2image, prompt=third_prompt)

Now let's run it!

    # Run the chain specifying only the input variable for the first chain.overall_chain = SimpleSequentialChain(    chains=[chain, chain_two, chain_three], verbose=True)catchphrase = overall_chain.run("colorful socks")print(catchphrase)

                > Entering new SimpleSequentialChain chain...     colorsocks.com            A stylized letter "s" in red, white and blue colors with a bright light shining through it, reminiscent of the sunlight streaming through a clear summer sky.                https://replicate.delivery/pbxt/Qau0h94c8e1xX6DnW4tHubR5vmdrdXJZh39cycjrjb3Wf3RRA/out-0.png        > Finished chain.    https://replicate.delivery/pbxt/Qau0h94c8e1xX6DnW4tHubR5vmdrdXJZh39cycjrjb3Wf3RRA/out-0.png

    response = requests.get(    "https://replicate.delivery/pbxt/Qau0h94c8e1xX6DnW4tHubR5vmdrdXJZh39cycjrjb3Wf3RRA/out-0.png")img = Image.open(BytesIO(response.content))img

        ![png](_replicate_files/output_33_0.png)