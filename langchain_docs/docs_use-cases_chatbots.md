Chatbots
========

info

[Python Guide](https://python.langchain.com/en/latest/use_cases/chatbots.html)

ChatGPT took the world by storm by exposing a powerful language model with a new interface - chat. There are several components that go into building a chatbot.

1.  The model - you can construct a chatbot from a normal language model or a Chat Model. The important thing to remember is that even if you are using a Chat Model, the API itself is stateless, meaning it won't remember previous interactions - you have to pass them in.
2.  PromptTemplate - this will guide how your chatbot acts. Are they sassy? Helpful? These can be used to give your chatbot some character.
3.  Memory - as mentioned above, the models themselves are stateless. Memory brings some concept of state to the table, allowing it remember previous interactions

Chatbots are often very powerful and more differentiated when combined with other sources of data. The same techniques that underpin "Question Answering Over Docs" can also be used here to give your chatbot access to that data.