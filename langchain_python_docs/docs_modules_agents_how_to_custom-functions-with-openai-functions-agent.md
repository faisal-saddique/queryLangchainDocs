Custom functions with OpenAI Functions Agent
============================================

This notebook goes through how to integrate custom functions with OpenAI Functions agent.

Install libraries which are required to run this example notebook

`pip install -q openai langchain yfinance`

Define custom functions[​](#define-custom-functions "Direct link to Define custom functions")
---------------------------------------------------------------------------------------------

    import yfinance as yffrom datetime import datetime, timedeltadef get_current_stock_price(ticker):    """Method to get current stock price"""    ticker_data = yf.Ticker(ticker)    recent = ticker_data.history(period="1d")    return {"price": recent.iloc[0]["Close"], "currency": ticker_data.info["currency"]}def get_stock_performance(ticker, days):    """Method to get stock price change in percentage"""    past_date = datetime.today() - timedelta(days=days)    ticker_data = yf.Ticker(ticker)    history = ticker_data.history(start=past_date)    old_price = history.iloc[0]["Close"]    current_price = history.iloc[-1]["Close"]    return {"percent_change": ((current_price - old_price) / old_price) * 100}

    get_current_stock_price("MSFT")

        {'price': 334.57000732421875, 'currency': 'USD'}

    get_stock_performance("MSFT", 30)

        {'percent_change': 1.014466941163018}

Make custom tools[​](#make-custom-tools "Direct link to Make custom tools")
---------------------------------------------------------------------------

    from typing import Typefrom pydantic import BaseModel, Fieldfrom langchain.tools import BaseToolclass CurrentStockPriceInput(BaseModel):    """Inputs for get_current_stock_price"""    ticker: str = Field(description="Ticker symbol of the stock")class CurrentStockPriceTool(BaseTool):    name = "get_current_stock_price"    description = """        Useful when you want to get current stock price.        You should enter the stock ticker symbol recognized by the yahoo finance        """    args_schema: Type[BaseModel] = CurrentStockPriceInput    def _run(self, ticker: str):        price_response = get_current_stock_price(ticker)        return price_response    def _arun(self, ticker: str):        raise NotImplementedError("get_current_stock_price does not support async")class StockPercentChangeInput(BaseModel):    """Inputs for get_stock_performance"""    ticker: str = Field(description="Ticker symbol of the stock")    days: int = Field(description="Timedelta days to get past date from current date")class StockPerformanceTool(BaseTool):    name = "get_stock_performance"    description = """        Useful when you want to check performance of the stock.        You should enter the stock ticker symbol recognized by the yahoo finance.        You should enter days as number of days from today from which performance needs to be check.        output will be the change in the stock price represented as a percentage.        """    args_schema: Type[BaseModel] = StockPercentChangeInput    def _run(self, ticker: str, days: int):        response = get_stock_performance(ticker, days)        return response    def _arun(self, ticker: str):        raise NotImplementedError("get_stock_performance does not support async")

Create Agent[​](#create-agent "Direct link to Create Agent")
------------------------------------------------------------

    from langchain.agents import AgentTypefrom langchain.chat_models import ChatOpenAIfrom langchain.agents import initialize_agentllm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0)tools = [CurrentStockPriceTool(), StockPerformanceTool()]agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

    agent.run(    "What is the current price of Microsoft stock? How it has performed over past 6 months?")

                > Entering new  chain...        Invoking: `get_current_stock_price` with `{'ticker': 'MSFT'}`            {'price': 334.57000732421875, 'currency': 'USD'}    Invoking: `get_stock_performance` with `{'ticker': 'MSFT', 'days': 180}`            {'percent_change': 40.163963297187905}The current price of Microsoft stock is $334.57 USD.         Over the past 6 months, Microsoft stock has performed well with a 40.16% increase in its price.        > Finished chain.    'The current price of Microsoft stock is $334.57 USD. \n\nOver the past 6 months, Microsoft stock has performed well with a 40.16% increase in its price.'

    agent.run("Give me recent stock prices of Google and Meta?")

                > Entering new  chain...        Invoking: `get_current_stock_price` with `{'ticker': 'GOOGL'}`            {'price': 118.33000183105469, 'currency': 'USD'}    Invoking: `get_current_stock_price` with `{'ticker': 'META'}`            {'price': 287.04998779296875, 'currency': 'USD'}The recent stock price of Google (GOOGL) is $118.33 USD and the recent stock price of Meta (META) is $287.05 USD.        > Finished chain.    'The recent stock price of Google (GOOGL) is $118.33 USD and the recent stock price of Meta (META) is $287.05 USD.'

    agent.run(    "In the past 3 months, which stock between Microsoft and Google has performed the best?")

                > Entering new  chain...        Invoking: `get_stock_performance` with `{'ticker': 'MSFT', 'days': 90}`            {'percent_change': 18.043096235165596}    Invoking: `get_stock_performance` with `{'ticker': 'GOOGL', 'days': 90}`            {'percent_change': 17.286155760642853}In the past 3 months, Microsoft (MSFT) has performed better than Google (GOOGL). Microsoft's stock price has increased by 18.04% while Google's stock price has increased by 17.29%.        > Finished chain.    "In the past 3 months, Microsoft (MSFT) has performed better than Google (GOOGL). Microsoft's stock price has increased by 18.04% while Google's stock price has increased by 17.29%."