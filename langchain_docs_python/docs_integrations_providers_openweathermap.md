OpenWeatherMap
==============

> [OpenWeatherMap](https://openweathermap.org/api/) provides all essential weather data for a specific location:
> 
> *   Current weather
> *   Minute forecast for 1 hour
> *   Hourly forecast for 48 hours
> *   Daily forecast for 8 days
> *   National weather alerts
> *   Historical weather data for 40+ years back

This page covers how to use the `OpenWeatherMap API` within LangChain.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Install requirements with

    pip install pyowm

*   Go to OpenWeatherMap and sign up for an account to get your API key [here](https://openweathermap.org/api/)
*   Set your API key as `OPENWEATHERMAP_API_KEY` environment variable

Wrappers[](#wrappers "Direct link to Wrappers")
------------------------------------------------

### Utility[](#utility "Direct link to Utility")

There exists a OpenWeatherMapAPIWrapper utility which wraps this API. To import this utility:

    from langchain.utilities.openweathermap import OpenWeatherMapAPIWrapper

For a more detailed walkthrough of this wrapper, see [this notebook](/docs/integrations/tools/openweathermap.html).

### Tool[](#tool "Direct link to Tool")

You can also easily load this wrapper as a Tool (to use with an Agent). You can do this with:

    from langchain.agents import load_toolstools = load_tools(["openweathermap-api"])

For more information on tools, see [this page](/docs/modules/agents/tools/).