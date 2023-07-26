Azure Cognitive Services Toolkit
================================

This toolkit is used to interact with the Azure Cognitive Services API to achieve some multimodal capabilities.

Currently There are four tools bundled in this toolkit:

*   AzureCogsImageAnalysisTool: used to extract caption, objects, tags, and text from images. (Note: this tool is not available on Mac OS yet, due to the dependency on `azure-ai-vision` package, which is only supported on Windows and Linux currently.)
*   AzureCogsFormRecognizerTool: used to extract text, tables, and key-value pairs from documents.
*   AzureCogsSpeech2TextTool: used to transcribe speech to text.
*   AzureCogsText2SpeechTool: used to synthesize text to speech.

First, you need to set up an Azure account and create a Cognitive Services resource. You can follow the instructions [here](https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account?tabs=multiservice%2Cwindows) to create a resource.

Then, you need to get the endpoint, key and region of your resource, and set them as environment variables. You can find them in the "Keys and Endpoint" page of your resource.

    # !pip install --upgrade azure-ai-formrecognizer > /dev/null# !pip install --upgrade azure-cognitiveservices-speech > /dev/null# For Windows/Linux# !pip install --upgrade azure-ai-vision > /dev/null

    import osos.environ["OPENAI_API_KEY"] = "sk-"os.environ["AZURE_COGS_KEY"] = ""os.environ["AZURE_COGS_ENDPOINT"] = ""os.environ["AZURE_COGS_REGION"] = ""

Create the Toolkit[](#create-the-toolkit "Direct link to Create the Toolkit")
------------------------------------------------------------------------------

    from langchain.agents.agent_toolkits import AzureCognitiveServicesToolkittoolkit = AzureCognitiveServicesToolkit()

    [tool.name for tool in toolkit.get_tools()]

        ['Azure Cognitive Services Image Analysis',     'Azure Cognitive Services Form Recognizer',     'Azure Cognitive Services Speech2Text',     'Azure Cognitive Services Text2Speech']

Use within an Agent[](#use-within-an-agent "Direct link to Use within an Agent")
---------------------------------------------------------------------------------

    from langchain import OpenAIfrom langchain.agents import initialize_agent, AgentType

    llm = OpenAI(temperature=0)agent = initialize_agent(    tools=toolkit.get_tools(),    llm=llm,    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,    verbose=True,)

    agent.run(    "What can I make with these ingredients?"    "https://images.openai.com/blob/9ad5a2ab-041f-475f-ad6a-b51899c50182/ingredients.png")

                > Entering new AgentExecutor chain...        Action:    ```
{      "action": "Azure Cognitive Services Image Analysis",      "action_input": "https://images.openai.com/blob/9ad5a2ab-041f-475f-ad6a-b51899c50182/ingredients.png"    }    
```            Observation: Caption: a group of eggs and flour in bowls    Objects: Egg, Egg, Food    Tags: dairy, ingredient, indoor, thickening agent, food, mixing bowl, powder, flour, egg, bowl    Thought: I can use the objects and tags to suggest recipes    Action:    ```
{      "action": "Final Answer",      "action_input": "You can make pancakes, omelettes, or quiches with these ingredients!"    }    
```        > Finished chain.    'You can make pancakes, omelettes, or quiches with these ingredients!'

    audio_file = agent.run("Tell me a joke and read it out for me.")

                > Entering new AgentExecutor chain...    Action:    ```
{      "action": "Azure Cognitive Services Text2Speech",      "action_input": "Why did the chicken cross the playground? To get to the other slide!"    }    
```            Observation: /tmp/tmpa3uu_j6b.wav    Thought: I have the audio file of the joke    Action:    ```
{      "action": "Final Answer",      "action_input": "/tmp/tmpa3uu_j6b.wav"    }    
```        > Finished chain.    '/tmp/tmpa3uu_j6b.wav'

    from IPython import displayaudio = display.Audio(audio_file)display.display(audio)