Natural Language APIs
=====================

Natural Language API Toolkits (NLAToolkits) permit LangChain Agents to efficiently plan and combine calls across endpoints. This notebook demonstrates a sample composition of the Speak, Klarna, and Spoonacluar APIs.

For a detailed walkthrough of the OpenAPI chains wrapped within the NLAToolkit, see the [OpenAPI Operation Chain](/docs/modules/chains/additional/openapi.html) notebook.

### First, import dependencies and load the LLM[](#first-import-dependencies-and-load-the-llm "Direct link to First, import dependencies and load the LLM")

    from typing import List, Optionalfrom langchain.chains import LLMChainfrom langchain.llms import OpenAIfrom langchain.prompts import PromptTemplatefrom langchain.requests import Requestsfrom langchain.tools import APIOperation, OpenAPISpecfrom langchain.agents import AgentType, Tool, initialize_agentfrom langchain.agents.agent_toolkits import NLAToolkit

    # Select the LLM to use. Here, we use text-davinci-003llm = OpenAI(    temperature=0, max_tokens=700)  # You can swap between different core LLM's here.

### Next, load the Natural Language API Toolkits[](#next-load-the-natural-language-api-toolkits "Direct link to Next, load the Natural Language API Toolkits")

    speak_toolkit = NLAToolkit.from_llm_and_url(llm, "https://api.speak.com/openapi.yaml")klarna_toolkit = NLAToolkit.from_llm_and_url(    llm, "https://www.klarna.com/us/shopping/public/openai/v0/api-docs/")

        Attempting to load an OpenAPI 3.0.1 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.    Attempting to load an OpenAPI 3.0.1 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.    Attempting to load an OpenAPI 3.0.1 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.

### Create the Agent[](#create-the-agent "Direct link to Create the Agent")

    # Slightly tweak the instructions from the default agentopenapi_format_instructions = """Use the following format:Question: the input question you must answerThought: you should always think about what to doAction: the action to take, should be one of [{tool_names}]Action Input: what to instruct the AI Action representative.Observation: The Agent's response... (this Thought/Action/Action Input/Observation can repeat N times)Thought: I now know the final answer. User can't see any of my observations, API responses, links, or tools.Final Answer: the final answer to the original input question with the right amount of detailWhen responding with your Final Answer, remember that the person you are responding to CANNOT see any of your Thought/Action/Action Input/Observations, so if there is any relevant information there you need to include it explicitly in your response."""

    natural_language_tools = speak_toolkit.get_tools() + klarna_toolkit.get_tools()mrkl = initialize_agent(    natural_language_tools,    llm,    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,    verbose=True,    agent_kwargs={"format_instructions": openapi_format_instructions},)

    mrkl.run(    "I have an end of year party for my Italian class and have to buy some Italian clothes for it")

                > Entering new AgentExecutor chain...     I need to find out what kind of Italian clothes are available    Action: Open_AI_Klarna_product_Api.productsUsingGET    Action Input: Italian clothes    Observation: The API response contains two products from the Alé brand in Italian Blue. The first is the Alé Colour Block Short Sleeve Jersey Men - Italian Blue, which costs $86.49, and the second is the Alé Dolid Flash Jersey Men - Italian Blue, which costs $40.00.    Thought: I now know what kind of Italian clothes are available and how much they cost.    Final Answer: You can buy two products from the Alé brand in Italian Blue for your end of year party. The Alé Colour Block Short Sleeve Jersey Men - Italian Blue costs $86.49, and the Alé Dolid Flash Jersey Men - Italian Blue costs $40.00.        > Finished chain.    'You can buy two products from the Alé brand in Italian Blue for your end of year party. The Alé Colour Block Short Sleeve Jersey Men - Italian Blue costs $86.49, and the Alé Dolid Flash Jersey Men - Italian Blue costs $40.00.'

### Using Auth + Adding more Endpoints[](#using-auth--adding-more-endpoints "Direct link to Using Auth + Adding more Endpoints")

Some endpoints may require user authentication via things like access tokens. Here we show how to pass in the authentication information via the `Requests` wrapper object.

Since each NLATool exposes a concisee natural language interface to its wrapped API, the top level conversational agent has an easier job incorporating each endpoint to satisfy a user's request.

**Adding the Spoonacular endpoints.**

1.  Go to the [Spoonacular API Console](https://spoonacular.com/food-api/console#Profile) and make a free account.
2.  Click on `Profile` and copy your API key below.

    spoonacular_api_key = ""  # Copy from the API Console

    requests = Requests(headers={"x-api-key": spoonacular_api_key})spoonacular_toolkit = NLAToolkit.from_llm_and_url(    llm,    "https://spoonacular.com/application/frontend/downloads/spoonacular-openapi-3.json",    requests=requests,    max_text_length=1800,  # If you want to truncate the response text)

        Attempting to load an OpenAPI 3.0.0 spec.  This may result in degraded performance. Convert your OpenAPI spec to 3.1.* spec for better support.    Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Accept. Valid values are ['path', 'query'] Ignoring optional parameter    Unsupported APIPropertyLocation "header" for parameter Content-Type. Valid values are ['path', 'query'] Ignoring optional parameter

    natural_language_api_tools = (    speak_toolkit.get_tools()    + klarna_toolkit.get_tools()    + spoonacular_toolkit.get_tools()[:30])print(f"{len(natural_language_api_tools)} tools loaded.")

        34 tools loaded.

    # Create an agent with the new toolsmrkl = initialize_agent(    natural_language_api_tools,    llm,    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,    verbose=True,    agent_kwargs={"format_instructions": openapi_format_instructions},)

    # Make the query more complex!user_input = (    "I'm learning Italian, and my language class is having an end of year party... "    " Could you help me find an Italian outfit to wear and"    " an appropriate recipe to prepare so I can present for the class in Italian?")

    mrkl.run(user_input)

                > Entering new AgentExecutor chain...     I need to find a recipe and an outfit that is Italian-themed.    Action: spoonacular_API.searchRecipes    Action Input: Italian    Observation: The API response contains 10 Italian recipes, including Turkey Tomato Cheese Pizza, Broccolini Quinoa Pilaf, Bruschetta Style Pork & Pasta, Salmon Quinoa Risotto, Italian Tuna Pasta, Roasted Brussels Sprouts With Garlic, Asparagus Lemon Risotto, Italian Steamed Artichokes, Crispy Italian Cauliflower Poppers Appetizer, and Pappa Al Pomodoro.    Thought: I need to find an Italian-themed outfit.    Action: Open_AI_Klarna_product_Api.productsUsingGET    Action Input: Italian    Observation: I found 10 products related to 'Italian' in the API response. These products include Italian Gold Sparkle Perfectina Necklace - Gold, Italian Design Miami Cuban Link Chain Necklace - Gold, Italian Gold Miami Cuban Link Chain Necklace - Gold, Italian Gold Herringbone Necklace - Gold, Italian Gold Claddagh Ring - Gold, Italian Gold Herringbone Chain Necklace - Gold, Garmin QuickFit 22mm Italian Vacchetta Leather Band, Macy's Italian Horn Charm - Gold, Dolce & Gabbana Light Blue Italian Love Pour Homme EdT 1.7 fl oz.    Thought: I now know the final answer.    Final Answer: To present for your Italian language class, you could wear an Italian Gold Sparkle Perfectina Necklace - Gold, an Italian Design Miami Cuban Link Chain Necklace - Gold, or an Italian Gold Miami Cuban Link Chain Necklace - Gold. For a recipe, you could make Turkey Tomato Cheese Pizza, Broccolini Quinoa Pilaf, Bruschetta Style Pork & Pasta, Salmon Quinoa Risotto, Italian Tuna Pasta, Roasted Brussels Sprouts With Garlic, Asparagus Lemon Risotto, Italian Steamed Artichokes, Crispy Italian Cauliflower Poppers Appetizer, or Pappa Al Pomodoro.        > Finished chain.    'To present for your Italian language class, you could wear an Italian Gold Sparkle Perfectina Necklace - Gold, an Italian Design Miami Cuban Link Chain Necklace - Gold, or an Italian Gold Miami Cuban Link Chain Necklace - Gold. For a recipe, you could make Turkey Tomato Cheese Pizza, Broccolini Quinoa Pilaf, Bruschetta Style Pork & Pasta, Salmon Quinoa Risotto, Italian Tuna Pasta, Roasted Brussels Sprouts With Garlic, Asparagus Lemon Risotto, Italian Steamed Artichokes, Crispy Italian Cauliflower Poppers Appetizer, or Pappa Al Pomodoro.'

Thank you![](#thank-you "Direct link to Thank you!")
-----------------------------------------------------

    natural_language_api_tools[1].run(    "Tell the LangChain audience to 'enjoy the meal' in Italian, please!")

        "In Italian, you can say 'Buon appetito' to someone to wish them to enjoy their meal. This phrase is commonly used in Italy when someone is about to eat, often at the beginning of a meal. It's similar to saying 'Bon appétit' in French or 'Guten Appetit' in German."