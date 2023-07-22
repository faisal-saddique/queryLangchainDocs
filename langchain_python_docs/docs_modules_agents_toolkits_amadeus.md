Amadeus Toolkit
===============

This notebook walks you through connecting LangChain to the Amadeus travel information API

To use this toolkit, you will need to set up your credentials explained in the [Amadeus for developers getting started overview](https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335). Once you've received a AMADEUS\_CLIENT\_ID and AMADEUS\_CLIENT\_SECRET, you can input them as environmental variables below.

    pip install --upgrade amadeus > /dev/null

Assign Environmental Variables[​](#assign-environmental-variables "Direct link to Assign Environmental Variables")
------------------------------------------------------------------------------------------------------------------

The toolkit will read the AMADEUS\_CLIENT\_ID and AMADEUS\_CLIENT\_SECRET environmental variables to authenticate the user so you need to set them here. You will also need to set your OPENAI\_API\_KEY to use the agent later.

    # Set environmental variables hereimport osos.environ["AMADEUS_CLIENT_ID"] = "CLIENT_ID"os.environ["AMADEUS_CLIENT_SECRET"] = "CLIENT_SECRET"os.environ["OPENAI_API_KEY"] = "API_KEY"

Create the Amadeus Toolkit and Get Tools[​](#create-the-amadeus-toolkit-and-get-tools "Direct link to Create the Amadeus Toolkit and Get Tools")
------------------------------------------------------------------------------------------------------------------------------------------------

To start, you need to create the toolkit, so you can access its tools later.

    from langchain.agents.agent_toolkits.amadeus.toolkit import AmadeusToolkittoolkit = AmadeusToolkit()tools = toolkit.get_tools()

Use Amadeus Toolkit within an Agent[​](#use-amadeus-toolkit-within-an-agent "Direct link to Use Amadeus Toolkit within an Agent")
---------------------------------------------------------------------------------------------------------------------------------

    from langchain import OpenAIfrom langchain.agents import initialize_agent, AgentType

    llm = OpenAI(temperature=0)agent = initialize_agent(    tools=tools,    llm=llm,    verbose=False,    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,)

    agent.run("What is the name of the airport in Cali, Colombia?")

        'The closest airport to Cali, Colombia is Alfonso Bonilla Aragón International Airport (CLO).'

    agent.run(    "What is the departure time of the cheapest flight on August 23, 2023 leaving Dallas, Texas before noon to Lincoln, Nebraska?")

        'The cheapest flight on August 23, 2023 leaving Dallas, Texas before noon to Lincoln, Nebraska has a departure time of 16:42 and a total price of 276.08 EURO.'

    agent.run(    "At what time does earliest flight on August 23, 2023 leaving Dallas, Texas to Lincoln, Nebraska land in Nebraska?")

        'The earliest flight on August 23, 2023 leaving Dallas, Texas to Lincoln, Nebraska lands in Lincoln, Nebraska at 16:07.'

    agent.run(    "What is the full travel time for the cheapest flight between Portland, Oregon to Dallas, TX on October 3, 2023?")

        'The cheapest flight between Portland, Oregon to Dallas, TX on October 3, 2023 is a Spirit Airlines flight with a total price of 84.02 EURO and a total travel time of 8 hours and 43 minutes.'

    agent.run(    "Please draft a concise email from Santiago to Paul, Santiago's travel agent, asking him to book the earliest flight from DFW to DCA on Aug 28, 2023. Include all flight details in the email.")

        'Dear Paul,\n\nI am writing to request that you book the earliest flight from DFW to DCA on Aug 28, 2023. The flight details are as follows:\n\nFlight 1: DFW to ATL, departing at 7:15 AM, arriving at 10:25 AM, flight number 983, carrier Delta Air Lines\nFlight 2: ATL to DCA, departing at 12:15 PM, arriving at 2:02 PM, flight number 759, carrier Delta Air Lines\n\nThank you for your help.\n\nSincerely,\nSantiago'