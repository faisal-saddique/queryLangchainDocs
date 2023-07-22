Querying Tabular Data
=====================

info

[Python Guide](https://python.langchain.com/en/latest/use_cases/tabular.html)

[JS Guide](https://js.langchain.com/docs/use_cases/tabular/)

Lots of data and information is stored in tabular data, whether it be csvs, excel sheets, or SQL tables. This page covers all resources available in LangChain for working with data in this format.

Document Loading[​](#document-loading "Direct link to Document Loading")
------------------------------------------------------------------------

If you have text data stored in a tabular format, you may want to load the data into a Document and then index it as you would other text/unstructured data. For this, you should use a document loader like the CSVLoader and then you should create an Index over that data, and query it that way.

Querying[​](#querying "Direct link to Querying")
------------------------------------------------

If you have more numeric tabular data, or have a large amount of data and don't want to index it, you can also use a language model to interact with it directly.

### Chains[​](#chains "Direct link to Chains")

If you are just getting started, and you have relatively small/simple tabular data, you should get started with chains. Chains are a sequence of predetermined steps, so they are good to get started with as they give you more control and let you understand what is happening better.

### Agents[​](#agents "Direct link to Agents")

Agents are more complex, and involve multiple queries to the LLM to understand what to do. The downside of agents are that you have less control. The upside is that they are more powerful, which allows you to use them on larger databases and more complex schemas.