Manifest
========

This notebook goes over how to use Manifest and LangChain.

For more detailed information on `manifest`, and how to use it with local hugginface models like in this example, see [https://github.com/HazyResearch/manifest](https://github.com/HazyResearch/manifest)

Another example of [using Manifest with Langchain](https://github.com/HazyResearch/manifest/blob/main/examples/langchain_chatgpt.html).

    pip install manifest-ml

    from manifest import Manifestfrom langchain.llms.manifest import ManifestWrapper

    manifest = Manifest(    client_name="huggingface", client_connection="http://127.0.0.1:5000")print(manifest.client.get_model_params())

    llm = ManifestWrapper(    client=manifest, llm_kwargs={"temperature": 0.001, "max_tokens": 256})

    # Map reduce examplefrom langchain import PromptTemplatefrom langchain.text_splitter import CharacterTextSplitterfrom langchain.chains.mapreduce import MapReduceChain_prompt = """Write a concise summary of the following:{text}CONCISE SUMMARY:"""prompt = PromptTemplate(template=_prompt, input_variables=["text"])text_splitter = CharacterTextSplitter()mp_chain = MapReduceChain.from_params(llm, prompt, text_splitter)

    with open("../../../state_of_the_union.txt") as f:    state_of_the_union = f.read()mp_chain.run(state_of_the_union)

        'President Obama delivered his annual State of the Union address on Tuesday night, laying out his priorities for the coming year. Obama said the government will provide free flu vaccines to all Americans, ending the government shutdown and allowing businesses to reopen. The president also said that the government will continue to send vaccines to 112 countries, more than any other nation. "We have lost so much to COVID-19," Trump said. "Time with one another. And worst of all, so much loss of life." He said the CDC is working on a vaccine for kids under 5, and that the government will be ready with plenty of vaccines when they are available. Obama says the new guidelines are a "great step forward" and that the virus is no longer a threat. He says the government is launching a "Test to Treat" initiative that will allow people to get tested at a pharmacy and get antiviral pills on the spot at no cost. Obama says the new guidelines are a "great step forward" and that the virus is no longer a threat. He says the government will continue to send vaccines to 112 countries, more than any other nation. "We are coming for your'

Compare HF Models[](#compare-hf-models "Direct link to Compare HF Models")
---------------------------------------------------------------------------

    from langchain.model_laboratory import ModelLaboratorymanifest1 = ManifestWrapper(    client=Manifest(        client_name="huggingface", client_connection="http://127.0.0.1:5000"    ),    llm_kwargs={"temperature": 0.01},)manifest2 = ManifestWrapper(    client=Manifest(        client_name="huggingface", client_connection="http://127.0.0.1:5001"    ),    llm_kwargs={"temperature": 0.01},)manifest3 = ManifestWrapper(    client=Manifest(        client_name="huggingface", client_connection="http://127.0.0.1:5002"    ),    llm_kwargs={"temperature": 0.01},)llms = [manifest1, manifest2, manifest3]model_lab = ModelLaboratory(llms)

    model_lab.compare("What color is a flamingo?")

        Input:    What color is a flamingo?        ManifestWrapper    Params: {'model_name': 'bigscience/T0_3B', 'model_path': 'bigscience/T0_3B', 'temperature': 0.01}    pink        ManifestWrapper    Params: {'model_name': 'EleutherAI/gpt-neo-125M', 'model_path': 'EleutherAI/gpt-neo-125M', 'temperature': 0.01}    A flamingo is a small, round        ManifestWrapper    Params: {'model_name': 'google/flan-t5-xl', 'model_path': 'google/flan-t5-xl', 'temperature': 0.01}    pink