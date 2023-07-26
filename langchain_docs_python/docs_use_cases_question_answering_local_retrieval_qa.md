Running LLMs locally
====================

The popularity of projects like [PrivateGPT](https://github.com/imartinez/privateGPT), [llama.cpp](https://github.com/ggerganov/llama.cpp), and [GPT4All](https://github.com/nomic-ai/gpt4all) underscore the importance of running LLMs locally.

LangChain has [integrations](https://integrations.langchain.com/) with many open source LLMs that can be run locally.

For example, here we show how to run `GPT4All` or `Llama-v2` locally (e.g., on your laptop) using local embeddings and a local LLM.

Document Loading[](#document-loading "Direct link to Document Loading")
------------------------------------------------------------------------

First, install packages needed for local embeddings and vector storage.

    pip install gpt4all pip install chromadb

Load and split an example docucment.

We'll use a blog post on agents as an example.

    from langchain.document_loaders import WebBaseLoaderloader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")data = loader.load()from langchain.text_splitter import RecursiveCharacterTextSplittertext_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)all_splits = text_splitter.split_documents(data)

Next, the below steps will download the `GPT4All` embeddings locally (if you don't already have them).

    from langchain.vectorstores import Chromafrom langchain.embeddings import GPT4AllEmbeddingsvectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())

        Found model file at  /Users/rlm/.cache/gpt4all/ggml-all-MiniLM-L6-v2-f16.bin

Test similarity search is working with our local embeddings.

    question = "What are the approaches to Task Decomposition?"docs = vectorstore.similarity_search(question)len(docs)

        4

    docs[0]

        Document(page_content='Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.', metadata={'description': 'Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.\nAgent System Overview In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components:', 'language': 'en', 'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'title': "LLM Powered Autonomous Agents | Lil'Log"})

Model[](#model "Direct link to Model")
---------------------------------------

### Llama-v2[](#llama-v2 "Direct link to Llama-v2")

Download a GGML converted model (e.g., [here](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)).

    pip install llama-cpp-python

To enable use of GPU on Apple Silicon, follow the steps [here](https://github.com/abetlen/llama-cpp-python/blob/main/docs/install/macos.md) to use the Python binding `with Metal support`.

In particular, ensure that `conda` is using the correct virtual enviorment that you created (`miniforge3`).

E.g., for me:

    conda activate /Users/rlm/miniforge3/envs/llama

With this confirmed:

    CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install -U llama-cpp-python --no-cache-dir

    from langchain.llms import LlamaCppfrom langchain.callbacks.manager import CallbackManagerfrom langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

Setting model parameters as noted in the [llama.cpp docs](https://python.langchain.com/docs/integrations/llms/llamacpp).

    n_gpu_layers = 1  # Metal set to 1 is enough.n_batch = 512  # Should be between 1 and n_ctx, consider the amount of RAM of your Apple Silicon Chip.callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])# Make sure the model path is correct for your system!llm = LlamaCpp(    model_path="/Users/rlm/Desktop/Code/llama.cpp/llama-2-13b-chat.ggmlv3.q4_0.bin",    n_gpu_layers=n_gpu_layers,    n_batch=n_batch,    n_ctx=2048,    f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls    callback_manager=callback_manager,    verbose=True,)

        llama.cpp: loading model from /Users/rlm/Desktop/Code/llama.cpp/llama-2-13b-chat.ggmlv3.q4_0.bin    llama_model_load_internal: format     = ggjt v3 (latest)    llama_model_load_internal: n_vocab    = 32000    llama_model_load_internal: n_ctx      = 2048    llama_model_load_internal: n_embd     = 5120    llama_model_load_internal: n_mult     = 256    llama_model_load_internal: n_head     = 40    llama_model_load_internal: n_layer    = 40    llama_model_load_internal: n_rot      = 128    llama_model_load_internal: freq_base  = 10000.0    llama_model_load_internal: freq_scale = 1    llama_model_load_internal: ftype      = 2 (mostly Q4_0)    llama_model_load_internal: n_ff       = 13824    llama_model_load_internal: model size = 13B    llama_model_load_internal: ggml ctx size =    0.09 MB    llama_model_load_internal: mem required  = 8819.71 MB (+ 1608.00 MB per state)    llama_new_context_with_model: kv self size  = 1600.00 MB    ggml_metal_init: allocating    ggml_metal_init: using MPS    ggml_metal_init: loading '/Users/rlm/miniforge3/envs/llama/lib/python3.9/site-packages/llama_cpp/ggml-metal.metal'    ggml_metal_init: loaded kernel_add                            0x76add7460    ggml_metal_init: loaded kernel_mul                            0x76add5090    ggml_metal_init: loaded kernel_mul_row                        0x76addae00    ggml_metal_init: loaded kernel_scale                          0x76adb2940    ggml_metal_init: loaded kernel_silu                           0x76adb8610    ggml_metal_init: loaded kernel_relu                           0x76addb700    ggml_metal_init: loaded kernel_gelu                           0x76addc100    ggml_metal_init: loaded kernel_soft_max                       0x76addcb80    ggml_metal_init: loaded kernel_diag_mask_inf                  0x76addd600    ggml_metal_init: loaded kernel_get_rows_f16                   0x295f16380    ggml_metal_init: loaded kernel_get_rows_q4_0                  0x295f165e0    ggml_metal_init: loaded kernel_get_rows_q4_1                  0x295f16840    ggml_metal_init: loaded kernel_get_rows_q2_K                  0x295f16aa0    ggml_metal_init: loaded kernel_get_rows_q3_K                  0x295f16d00    ggml_metal_init: loaded kernel_get_rows_q4_K                  0x295f16f60    ggml_metal_init: loaded kernel_get_rows_q5_K                  0x295f171c0    ggml_metal_init: loaded kernel_get_rows_q6_K                  0x295f17420    ggml_metal_init: loaded kernel_rms_norm                       0x295f17680    ggml_metal_init: loaded kernel_norm                           0x295f178e0    ggml_metal_init: loaded kernel_mul_mat_f16_f32                0x295f17b40    ggml_metal_init: loaded kernel_mul_mat_q4_0_f32               0x295f17da0    ggml_metal_init: loaded kernel_mul_mat_q4_1_f32               0x295f18000    ggml_metal_init: loaded kernel_mul_mat_q2_K_f32               0x7962b9900    ggml_metal_init: loaded kernel_mul_mat_q3_K_f32               0x7962bf5f0    ggml_metal_init: loaded kernel_mul_mat_q4_K_f32               0x7962bc630    ggml_metal_init: loaded kernel_mul_mat_q5_K_f32               0x142045960    ggml_metal_init: loaded kernel_mul_mat_q6_K_f32               0x7962ba2b0    ggml_metal_init: loaded kernel_rope                           0x7962c35f0    ggml_metal_init: loaded kernel_alibi_f32                      0x7962c30b0    ggml_metal_init: loaded kernel_cpy_f32_f16                    0x7962c15b0    ggml_metal_init: loaded kernel_cpy_f32_f32                    0x7962beb10    ggml_metal_init: loaded kernel_cpy_f16_f16                    0x7962bf060    ggml_metal_init: recommendedMaxWorkingSetSize = 21845.34 MB    ggml_metal_init: hasUnifiedMemory             = true    ggml_metal_init: maxTransferRate              = built-in GPU    ggml_metal_add_buffer: allocated 'data            ' buffer, size =  6984.06 MB, (35852.94 / 21845.34), warning: current allocated size is greater than the recommended max working set size    ggml_metal_add_buffer: allocated 'eval            ' buffer, size =  1026.00 MB, (36878.94 / 21845.34), warning: current allocated size is greater than the recommended max working set size    ggml_metal_add_buffer: allocated 'kv              ' buffer, size =  1602.00 MB, (38480.94 / 21845.34), warning: current allocated size is greater than the recommended max working set size    ggml_metal_add_buffer: allocated 'scr0            ' buffer, size =   298.00 MB, (38778.94 / 21845.34), warning: current allocated size is greater than the recommended max working set size    AVX = 0 | AVX2 = 0 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 0 | NEON = 1 | ARM_FMA = 1 | F16C = 0 | FP16_VA = 1 | WASM_SIMD = 0 | BLAS = 1 | SSE3 = 0 | VSX = 0 |     ggml_metal_add_buffer: allocated 'scr1            ' buffer, size =   512.00 MB, (39290.94 / 21845.34), warning: current allocated size is greater than the recommended max working set size

Note that these indicate that [Metal was enabled properly](https://python.langchain.com/docs/integrations/llms/llamacpp):

    ggml_metal_init: allocatingggml_metal_init: using MPS

    prompt = """Question: A rap battle between Stephen Colbert and John Oliver"""llm(prompt)

        Llama.generate: prefix-match hit        Setting: The Late Show with Stephen Colbert. The studio audience is filled with fans of both comedians, and the energy is electric. The two comedians are seated at a table, ready to begin their epic rap battle.        Stephen Colbert: (smirking) Oh, you think you can take me down, John? You're just a Brit with a funny accent, and I'm the king of comedy!    John Oliver: (grinning) Oh, you think you're tough, Stephen? You're just a has-been from South Carolina, and I'm the future of comedy!    The battle begins, with each comedian delivering clever rhymes and witty insults. Here are a few lines that might be included:    Stephen Colbert: (rapping) You may have a big brain, John, but you can't touch my charm / I've got the audience in stitches, while you're just a blemish on the screen / Your accent is so thick, it's like trying to hear a speech through a mouthful of marshmallows / You may have        llama_print_timings:        load time =  2201.54 ms    llama_print_timings:      sample time =   182.54 ms /   256 runs   (    0.71 ms per token,  1402.41 tokens per second)    llama_print_timings: prompt eval time =     0.00 ms /     1 tokens (    0.00 ms per token,      inf tokens per second)    llama_print_timings:        eval time =  8484.62 ms /   256 runs   (   33.14 ms per token,    30.17 tokens per second)    llama_print_timings:       total time =  9000.62 ms    "\nSetting: The Late Show with Stephen Colbert. The studio audience is filled with fans of both comedians, and the energy is electric. The two comedians are seated at a table, ready to begin their epic rap battle.\n\nStephen Colbert: (smirking) Oh, you think you can take me down, John? You're just a Brit with a funny accent, and I'm the king of comedy!\nJohn Oliver: (grinning) Oh, you think you're tough, Stephen? You're just a has-been from South Carolina, and I'm the future of comedy!\nThe battle begins, with each comedian delivering clever rhymes and witty insults. Here are a few lines that might be included:\nStephen Colbert: (rapping) You may have a big brain, John, but you can't touch my charm / I've got the audience in stitches, while you're just a blemish on the screen / Your accent is so thick, it's like trying to hear a speech through a mouthful of marshmallows / You may have"

### GPT4All[](#gpt4all "Direct link to GPT4All")

Similarly, we can use `GPT4All`.

[Download the GPT4All model binary](https://python.langchain.com/docs/integrations/llms/gpt4all).

The Model Explorer on the [GPT4All](https://gpt4all.io/index.html) is a great way to choose and download a model.

Then, specify the path that you downloaded to to.

E.g., for me, the model lives here:

`/Users/rlm/Desktop/Code/gpt4all/models/nous-hermes-13b.ggmlv3.q4_0.bin`

    from langchain.llms import GPT4Allllm = GPT4All(    model="/Users/rlm/Desktop/Code/gpt4all/models/nous-hermes-13b.ggmlv3.q4_0.bin",    max_tokens=2048,)

        Found model file at  /Users/rlm/Desktop/Code/gpt4all/models/nous-hermes-13b.ggmlv3.q4_0.bin    objc[47842]: Class GGMLMetalClass is implemented in both /Users/rlm/anaconda3/envs/lcn2/lib/python3.9/site-packages/gpt4all/llmodel_DO_NOT_MODIFY/build/libreplit-mainline-metal.dylib (0x29f48c208) and /Users/rlm/anaconda3/envs/lcn2/lib/python3.9/site-packages/gpt4all/llmodel_DO_NOT_MODIFY/build/libllamamodel-mainline-metal.dylib (0x29f970208). One of the two will be used. Which one is undefined.    llama.cpp: using Metal    llama.cpp: loading model from /Users/rlm/Desktop/Code/gpt4all/models/nous-hermes-13b.ggmlv3.q4_0.bin    llama_model_load_internal: format     = ggjt v3 (latest)    llama_model_load_internal: n_vocab    = 32001    llama_model_load_internal: n_ctx      = 2048    llama_model_load_internal: n_embd     = 5120    llama_model_load_internal: n_mult     = 256    llama_model_load_internal: n_head     = 40    llama_model_load_internal: n_layer    = 40    llama_model_load_internal: n_rot      = 128    llama_model_load_internal: ftype      = 2 (mostly Q4_0)    llama_model_load_internal: n_ff       = 13824    llama_model_load_internal: n_parts    = 1    llama_model_load_internal: model size = 13B    llama_model_load_internal: ggml ctx size =    0.09 MB    llama_model_load_internal: mem required  = 9031.71 MB (+ 1608.00 MB per state)    llama_new_context_with_model: kv self size  = 1600.00 MB    ggml_metal_init: allocating    ggml_metal_init: using MPS    ggml_metal_init: loading '/Users/rlm/anaconda3/envs/lcn2/lib/python3.9/site-packages/gpt4all/llmodel_DO_NOT_MODIFY/build/ggml-metal.metal'    ggml_metal_init: loaded kernel_add                            0x115fcbfb0    ggml_metal_init: loaded kernel_mul                            0x115fcd4a0    ggml_metal_init: loaded kernel_mul_row                        0x115fce850    ggml_metal_init: loaded kernel_scale                          0x115fcd700    ggml_metal_init: loaded kernel_silu                           0x115fcd960    ggml_metal_init: loaded kernel_relu                           0x115fcfd50    ggml_metal_init: loaded kernel_gelu                           0x115fd03c0    ggml_metal_init: loaded kernel_soft_max                       0x115fcf640    ggml_metal_init: loaded kernel_diag_mask_inf                  0x115fd07f0    ggml_metal_init: loaded kernel_get_rows_f16                   0x1147b2450    ggml_metal_init: loaded kernel_get_rows_q4_0                  0x11479d1d0    ggml_metal_init: loaded kernel_get_rows_q4_1                  0x1147ad1f0    ggml_metal_init: loaded kernel_get_rows_q2_k                  0x1147aef50    ggml_metal_init: loaded kernel_get_rows_q3_k                  0x1147af1b0    ggml_metal_init: loaded kernel_get_rows_q4_k                  0x1147af410    ggml_metal_init: loaded kernel_get_rows_q5_k                  0x1147affa0    ggml_metal_init: loaded kernel_get_rows_q6_k                  0x1147b0200    ggml_metal_init: loaded kernel_rms_norm                       0x1147b0460    ggml_metal_init: loaded kernel_norm                           0x1147bfc90    ggml_metal_init: loaded kernel_mul_mat_f16_f32                0x1147c0230    ggml_metal_init: loaded kernel_mul_mat_q4_0_f32               0x1147c0490    ggml_metal_init: loaded kernel_mul_mat_q4_1_f32               0x1147c06f0    ggml_metal_init: loaded kernel_mul_mat_q2_k_f32               0x1147c0950    ggml_metal_init: loaded kernel_mul_mat_q3_k_f32               0x1147c0bb0    ggml_metal_init: loaded kernel_mul_mat_q4_k_f32               0x1147c0e10    ggml_metal_init: loaded kernel_mul_mat_q5_k_f32               0x1147c1070    ggml_metal_init: loaded kernel_mul_mat_q6_k_f32               0x1147c13d0    ggml_metal_init: loaded kernel_rope                           0x1147c1a00    ggml_metal_init: loaded kernel_alibi_f32                      0x1147c2120    ggml_metal_init: loaded kernel_cpy_f32_f16                    0x115fd1690    ggml_metal_init: loaded kernel_cpy_f32_f32                    0x115fd1c60    ggml_metal_init: loaded kernel_cpy_f16_f16                    0x115fd2d40    ggml_metal_init: recommendedMaxWorkingSetSize = 21845.34 MB    ggml_metal_init: hasUnifiedMemory             = true    ggml_metal_init: maxTransferRate              = built-in GPU    ggml_metal_add_buffer: allocated 'data            ' buffer, size =  6984.06 MB, ( 6984.45 / 21845.34)    ggml_metal_add_buffer: allocated 'eval            ' buffer, size =  1024.00 MB, ( 8008.45 / 21845.34)    ggml_metal_add_buffer: allocated 'kv              ' buffer, size =  1602.00 MB, ( 9610.45 / 21845.34)    ggml_metal_add_buffer: allocated 'scr0            ' buffer, size =   512.00 MB, (10122.45 / 21845.34)    ggml_metal_add_buffer: allocated 'scr1            ' buffer, size =   512.00 MB, (10634.45 / 21845.34)

LLMChain[](#llmchain "Direct link to LLMChain")
------------------------------------------------

Run an `LLMChain` (see [here](https://python.langchain.com/docs/modules/chains/foundational/llm_chain)) with either model by passing in the retrieved docs and a simple prompt.

It formats the prompt template using the input key values provided and passes the formatted string to `GPT4All`, `LLama-V2`, or another specified LLM.

In this case, the list of retrieved documents (`docs`) above are pass into `{context}`.

    from langchain import PromptTemplate, LLMChain# Promptprompt = PromptTemplate.from_template(    "Summarize the main themes in these retrieved docs: {docs}")# Chainllm_chain = LLMChain(llm=llm, prompt=prompt)# Runquestion = "What are the approaches to Task Decomposition?"docs = vectorstore.similarity_search(question)result = llm_chain(docs)# Outputresult["text"]

        Llama.generate: prefix-match hit        Based on the retrieved documents, the main themes are:    1. Task decomposition: The ability to break down complex tasks into smaller subtasks, which can be handled by an LLM or other components of the agent system.    2. LLM as the core controller: The use of a large language model (LLM) as the primary controller of an autonomous agent system, complemented by other key components such as a knowledge graph and a planner.    3. Potentiality of LLM: The idea that LLMs have the potential to be used as powerful general problem solvers, not just for generating well-written copies but also for solving complex tasks and achieving human-like intelligence.    4. Challenges in long-term planning: The challenges in planning over a lengthy history and effectively exploring the solution space, which are important limitations of current LLM-based autonomous agent systems.        llama_print_timings:        load time =  1191.88 ms    llama_print_timings:      sample time =   134.47 ms /   193 runs   (    0.70 ms per token,  1435.25 tokens per second)    llama_print_timings: prompt eval time = 39470.18 ms /  1055 tokens (   37.41 ms per token,    26.73 tokens per second)    llama_print_timings:        eval time =  8090.85 ms /   192 runs   (   42.14 ms per token,    23.73 tokens per second)    llama_print_timings:       total time = 47943.12 ms    '\nBased on the retrieved documents, the main themes are:\n1. Task decomposition: The ability to break down complex tasks into smaller subtasks, which can be handled by an LLM or other components of the agent system.\n2. LLM as the core controller: The use of a large language model (LLM) as the primary controller of an autonomous agent system, complemented by other key components such as a knowledge graph and a planner.\n3. Potentiality of LLM: The idea that LLMs have the potential to be used as powerful general problem solvers, not just for generating well-written copies but also for solving complex tasks and achieving human-like intelligence.\n4. Challenges in long-term planning: The challenges in planning over a lengthy history and effectively exploring the solution space, which are important limitations of current LLM-based autonomous agent systems.'

QA Chain[](#qa-chain "Direct link to QA Chain")
------------------------------------------------

We can use a `QA chain` to handle our question above.

`chain_type="stuff"` (see [here](https://python.langchain.com/docs/modules/chains/document/stuff)) means that all the docs will be added (stuffed) into a prompt.

    from langchain.chains.question_answering import load_qa_chain# Prompttemplate = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum and keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. {context}Question: {question}Helpful Answer:"""QA_CHAIN_PROMPT = PromptTemplate(    input_variables=["context", "question"],    template=template,)# Chainchain = load_qa_chain(llm, chain_type="stuff", prompt=QA_CHAIN_PROMPT)# Runchain({"input_documents": docs, "question": question}, return_only_outputs=True)

        Llama.generate: prefix-match hit     Hi there! There are three main approaches to task decomposition. One is using LLM with simple prompting like "Steps for XYZ." or "What are the subgoals for achieving XYZ?" Another approach is by using task-specific instructions, such as "Write a story outline" for writing a novel. Finally, task decomposition can also be done with human inputs. Thanks for asking!        llama_print_timings:        load time =  1191.88 ms    llama_print_timings:      sample time =    61.21 ms /    85 runs   (    0.72 ms per token,  1388.64 tokens per second)    llama_print_timings: prompt eval time =  8014.11 ms /   267 tokens (   30.02 ms per token,    33.32 tokens per second)    llama_print_timings:        eval time =  2908.17 ms /    84 runs   (   34.62 ms per token,    28.88 tokens per second)    llama_print_timings:       total time = 11096.23 ms    {'output_text': ' Hi there! There are three main approaches to task decomposition. One is using LLM with simple prompting like "Steps for XYZ." or "What are the subgoals for achieving XYZ?" Another approach is by using task-specific instructions, such as "Write a story outline" for writing a novel. Finally, task decomposition can also be done with human inputs. Thanks for asking!'}

RetrievalQA[](#retrievalqa "Direct link to RetrievalQA")
---------------------------------------------------------

For an even simpler flow, use `RetrievalQA`.

This will use a QA default prompt (shown [here](https://github.com/hwchase17/langchain/blob/275b926cf745b5668d3ea30236635e20e7866442/langchain/chains/retrieval_qa/prompt.py#L4)) and will retrieve from the vectorDB.

But, you can still pass in a prompt, as before, if desired.

    from langchain.chains import RetrievalQAqa_chain = RetrievalQA.from_chain_type(    llm,    retriever=vectorstore.as_retriever(),    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},)

    qa_chain({"query": question})

        Llama.generate: prefix-match hit         The three approaches to Task decomposition are LLMs with simple prompting, task-specific instructions, or human inputs. Thanks for asking!        llama_print_timings:        load time =  1191.88 ms    llama_print_timings:      sample time =    22.78 ms /    31 runs   (    0.73 ms per token,  1360.66 tokens per second)    llama_print_timings: prompt eval time =     0.00 ms /     1 tokens (    0.00 ms per token,      inf tokens per second)    llama_print_timings:        eval time =  1320.23 ms /    31 runs   (   42.59 ms per token,    23.48 tokens per second)    llama_print_timings:       total time =  1387.70 ms    {'query': 'What are the approaches to Task Decomposition?',     'result': ' \nThe three approaches to Task decomposition are LLMs with simple prompting, task-specific instructions, or human inputs. Thanks for asking!'}