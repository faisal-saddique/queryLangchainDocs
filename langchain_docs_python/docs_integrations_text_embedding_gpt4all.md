GPT4All
=======

This notebook explains how to use [GPT4All embeddings](https://docs.gpt4all.io/gpt4all_python_embedding.html#gpt4all.gpt4all.Embed4All) with LangChain.

    pip install gpt4all

    from langchain.embeddings import GPT4AllEmbeddings

    gpt4all_embd = GPT4AllEmbeddings()

        100%|████████████████████████| 45.5M/45.5M [00:02<00:00, 18.5MiB/s]    Model downloaded at:  /Users/rlm/.cache/gpt4all/ggml-all-MiniLM-L6-v2-f16.bin    objc[45711]: Class GGMLMetalClass is implemented in both /Users/rlm/anaconda3/envs/lcn2/lib/python3.9/site-packages/gpt4all/llmodel_DO_NOT_MODIFY/build/libreplit-mainline-metal.dylib (0x29fe18208) and /Users/rlm/anaconda3/envs/lcn2/lib/python3.9/site-packages/gpt4all/llmodel_DO_NOT_MODIFY/build/libllamamodel-mainline-metal.dylib (0x2a0244208). One of the two will be used. Which one is undefined.

    text = "This is a test document."

    query_result = gpt4all_embd.embed_query(text)

    doc_result = gpt4all_embd.embed_documents([text])