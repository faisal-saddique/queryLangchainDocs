multi\_modal\_output\_agent
===========================

Multi-modal outputs: Image & Text[](#multi-modal-outputs-image--text "Direct link to Multi-modal outputs: Image & Text")
-------------------------------------------------------------------------------------------------------------------------

This notebook shows how non-text producing tools can be used to create multi-modal agents.

This example is limited to text and image outputs and uses UUIDs to transfer content across tools and agents.

This example uses Steamship to generate and store generated images. Generated are auth protected by default.

You can get your Steamship api key here: [https://steamship.com/account/api](https://steamship.com/account/api)

    from steamship import Block, Steamshipimport refrom IPython.display import Image

    from langchain import OpenAIfrom langchain.agents import initialize_agentfrom langchain.agents import AgentTypefrom langchain.tools import SteamshipImageGenerationTool

    llm = OpenAI(temperature=0)

Dall-E[](#dall-e "Direct link to Dall-E")
------------------------------------------

    tools = [SteamshipImageGenerationTool(model_name="dall-e")]

    mrkl = initialize_agent(    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    output = mrkl.run("How would you visualize a parot playing soccer?")

                > Entering new AgentExecutor chain...     I need to generate an image of a parrot playing soccer.    Action: GenerateImage    Action Input: A parrot wearing a soccer uniform, kicking a soccer ball.    Observation: E28BE7C7-D105-41E0-8A5B-2CE21424DFEC    Thought: I now have the UUID of the generated image.    Final Answer: The UUID of the generated image is E28BE7C7-D105-41E0-8A5B-2CE21424DFEC.        > Finished chain.

    def show_output(output):    """Display the multi-modal output from the agent."""    UUID_PATTERN = re.compile(        r"([0-9A-Za-z]{8}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{12})"    )    outputs = UUID_PATTERN.split(output)    outputs = [        re.sub(r"^\W+", "", el) for el in outputs    ]  # Clean trailing and leading non-word characters    for output in outputs:        maybe_block_id = UUID_PATTERN.search(output)        if maybe_block_id:            display(Image(Block.get(Steamship(), _id=maybe_block_id.group()).raw()))        else:            print(output, end="\n\n")

    show_output(output)

        The UUID of the generated image is         ![png](_multi_modal_output_agent_files/output_10_1.png)    

StableDiffusion[](#stablediffusion "Direct link to StableDiffusion")
---------------------------------------------------------------------

    tools = [SteamshipImageGenerationTool(model_name="stable-diffusion")]

    mrkl = initialize_agent(    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    output = mrkl.run("How would you visualize a parot playing soccer?")

                > Entering new AgentExecutor chain...     I need to generate an image of a parrot playing soccer.    Action: GenerateImage    Action Input: A parrot wearing a soccer uniform, kicking a soccer ball.    Observation: 25BB588F-85E4-4915-82BE-67ADCF974881    Thought: I now have the UUID of the generated image.    Final Answer: The UUID of the generated image is 25BB588F-85E4-4915-82BE-67ADCF974881.        > Finished chain.

    show_output(output)

        The UUID of the generated image is         ![png](_multi_modal_output_agent_files/output_15_1.png)