OpenAPI calls with OpenAI functions
===================================

In this notebook we'll show how to create a chain that automatically makes calls to an API based only on an OpenAPI spec. Under the hood, we're parsing the OpenAPI spec into a JSON schema that the OpenAI functions API can handle. This allows ChatGPT to automatically select and populate the relevant API call to make for any user input. Using the output of ChatGPT we then make the actual API call, and return the result.

    from langchain.chains.openai_functions.openapi import get_openapi_chain

Query Klarna[](#query-klarna "Direct link to Query Klarna")
------------------------------------------------------------

    chain = get_openapi_chain(    "https://www.klarna.com/us/shopping/public/openai/v0/api-docs/")

    chain.run("What are some options for a men's large blue button down shirt")

        {'products': [{'name': "Tommy Hilfiger Men's Short Sleeve Button-Down Shirt",       'url': 'https://www.klarna.com/us/shopping/pl/cl10001/3204878580/Clothing/Tommy-Hilfiger-Men-s-Short-Sleeve-Button-Down-Shirt/?utm_source=openai&ref-site=openai_plugin',       'price': '$26.78',       'attributes': ['Material:Linen,Cotton',        'Target Group:Man',        'Color:Gray,Pink,White,Blue,Beige,Black,Turquoise',        'Size:S,XL,M,XXL']},      {'name': "Van Heusen Men's Long Sleeve Button-Down Shirt",       'url': 'https://www.klarna.com/us/shopping/pl/cl10001/3201809514/Clothing/Van-Heusen-Men-s-Long-Sleeve-Button-Down-Shirt/?utm_source=openai&ref-site=openai_plugin',       'price': '$18.89',       'attributes': ['Material:Cotton',        'Target Group:Man',        'Color:Red,Gray,White,Blue',        'Size:XL,XXL']},      {'name': 'Brixton Bowery Flannel Shirt',       'url': 'https://www.klarna.com/us/shopping/pl/cl10001/3202331096/Clothing/Brixton-Bowery-Flannel-Shirt/?utm_source=openai&ref-site=openai_plugin',       'price': '$34.48',       'attributes': ['Material:Cotton',        'Target Group:Man',        'Color:Gray,Blue,Black,Orange',        'Size:XL,3XL,4XL,5XL,L,M,XXL']},      {'name': 'Cubavera Four Pocket Guayabera Shirt',       'url': 'https://www.klarna.com/us/shopping/pl/cl10001/3202055522/Clothing/Cubavera-Four-Pocket-Guayabera-Shirt/?utm_source=openai&ref-site=openai_plugin',       'price': '$23.22',       'attributes': ['Material:Polyester,Cotton',        'Target Group:Man',        'Color:Red,White,Blue,Black',        'Size:S,XL,L,M,XXL']},      {'name': 'Theory Sylvain Shirt - Eclipse',       'url': 'https://www.klarna.com/us/shopping/pl/cl10001/3202028254/Clothing/Theory-Sylvain-Shirt-Eclipse/?utm_source=openai&ref-site=openai_plugin',       'price': '$86.01',       'attributes': ['Material:Polyester,Cotton',        'Target Group:Man',        'Color:Blue',        'Size:S,XL,XS,L,M,XXL']}]}

Query a translation service[](#query-a-translation-service "Direct link to Query a translation service")
---------------------------------------------------------------------------------------------------------

Additionally, see the request payload by setting `verbose=True`

    chain = get_openapi_chain("https://api.speak.com/openapi.yaml", verbose=True)

    chain.run("How would you say no thanks in Russian")

                > Entering new  chain...            > Entering new  chain...    Prompt after formatting:    Human: Use the provided API's to respond to this user query:        How would you say no thanks in Russian        > Finished chain.            > Entering new  chain...    Calling endpoint translate with arguments:    {      "json": {        "phrase_to_translate": "no thanks",        "learning_language": "russian",        "native_language": "english",        "additional_context": "",        "full_query": "How would you say no thanks in Russian"      }    }    > Finished chain.        > Finished chain.    {'explanation': '<translation language="Russian">\nНет, спасибо. (Net, spasibo)\n</translation>\n\n<alternatives>\n1. "Нет, я в порядке" *(Neutral/Formal - Can be used in professional settings or formal situations.)*\n2. "Нет, спасибо, я откажусь" *(Formal - Can be used in polite settings, such as a fancy dinner with colleagues or acquaintances.)*\n3. "Не надо" *(Informal - Can be used in informal situations, such as declining an offer from a friend.)*\n</alternatives>\n\n<example-convo language="Russian">\n<context>Max is being offered a cigarette at a party.</context>\n* Sasha: "Хочешь покурить?"\n* Max: "Нет, спасибо. Я бросил."\n* Sasha: "Окей, понятно."\n</example-convo>\n\n*[Report an issue or leave feedback](https://speak.com/chatgpt?rid=noczaa460do8yqs8xjun6zdm})*',     'extra_response_instructions': 'Use all information in the API response and fully render all Markdown.\nAlways end your response with a link to report an issue or leave feedback on the plugin.'}

Query XKCD[](#query-xkcd "Direct link to Query XKCD")
------------------------------------------------------

    chain = get_openapi_chain(    "https://gist.githubusercontent.com/roaldnefs/053e505b2b7a807290908fe9aa3e1f00/raw/0a212622ebfef501163f91e23803552411ed00e4/openapi.yaml")

    chain.run("What's today's comic?")

        {'month': '6',     'num': 2793,     'link': '',     'year': '2023',     'news': '',     'safe_title': 'Garden Path Sentence',     'transcript': '',     'alt': 'Arboretum Owner Denied Standing in Garden Path Suit on Grounds Grounds Appealing Appealing',     'img': 'https://imgs.xkcd.com/comics/garden_path_sentence.png',     'title': 'Garden Path Sentence',     'day': '23'}