NLP Cloud
=========

NLP Cloud is an artificial intelligence platform that allows you to use the most advanced AI engines, and even train your own engines with your own data.

The [embeddings](https://docs.nlpcloud.com/#embeddings) endpoint offers several models:

*   `paraphrase-multilingual-mpnet-base-v2`: Paraphrase Multilingual MPNet Base V2 is a very fast model based on Sentence Transformers that is perfectly suited for embeddings extraction in more than 50 languages (see the full list here).
    
*   `gpt-j`: GPT-J returns advanced embeddings. It might return better results than Sentence Transformers based models (see above) but it is also much slower.
    
*   `dolphin`: Dolphin returns advanced embeddings. It might return better results than Sentence Transformers based models (see above) but it is also much slower. It natively understands the following languages: Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, French, German, Hungarian, Italian, Japanese, Polish, Portuguese, Romanian, Russian, Serbian, Slovenian, Spanish, Swedish, and Ukrainian.
    

    pip install nlpcloud

    from langchain.embeddings import NLPCloudEmbeddings

    import osos.environ["NLPCLOUD_API_KEY"] = "xxx"nlpcloud_embd = NLPCloudEmbeddings()

    text = "This is a test document."

    query_result = nlpcloud_embd.embed_query(text)

    doc_result = nlpcloud_embd.embed_documents([text])