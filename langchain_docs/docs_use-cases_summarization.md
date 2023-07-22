Summarization
=============

info

[Python Guide](https://python.langchain.com/en/latest/use_cases/summarization.html)

[JS Guide](https://js.langchain.com/docs/use_cases/summarization/)

A common use case is wanting to summarize long documents. This naturally runs into the context window limitations. Unlike in question-answering, you can't just do some semantic search hacks to only select the chunks of text most relevant to the question (because, in this case, there is no particular question - you want to summarize everything). So what do you do then?

The most common way around this is to split the documents into chunks and then do summarization in a recursive manner. By this we mean you first summarize each chunk by itself, then you group the summaries into chunks and summarize each chunk of summaries, and continue doing that until only one is left.