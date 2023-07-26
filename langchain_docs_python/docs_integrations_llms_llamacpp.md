Llama-cpp
=========

[llama-cpp](https://github.com/abetlen/llama-cpp-python) is a Python binding for [llama.cpp](https://github.com/ggerganov/llama.cpp). It supports [several LLMs](https://github.com/ggerganov/llama.cpp).

This notebook goes over how to run `llama-cpp` within LangChain.

Installation[](#installation "Direct link to Installation")
------------------------------------------------------------

There is a bunch of options how to install the llama-cpp package:

*   only CPU usage
*   CPU + GPU (using one of many BLAS backends)
*   Metal GPU (MacOS with Apple Silicon Chip)

### CPU only installation[](#cpu-only-installation "Direct link to CPU only installation")

    pip install llama-cpp-python

### Installation with OpenBLAS / cuBLAS / CLBlast[](#installation-with-openblas--cublas--clblast "Direct link to Installation with OpenBLAS / cuBLAS / CLBlast")

`lama.cpp` supports multiple BLAS backends for faster processing. Use the `FORCE_CMAKE=1` environment variable to force the use of cmake and install the pip package for the desired BLAS backend ([source](https://github.com/abetlen/llama-cpp-python#installation-with-openblas--cublas--clblast)).

Example installation with cuBLAS backend:

    CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python

**IMPORTANT**: If you have already installed a cpu only version of the package, you need to reinstall it from scratch: consider the following command:

    CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install --upgrade --force-reinstall llama-cpp-python --no-cache-dir

### Installation with Metal[](#installation-with-metal "Direct link to Installation with Metal")

`lama.cpp` supports Apple silicon first-class citizen - optimized via ARM NEON, Accelerate and Metal frameworks. Use the `FORCE_CMAKE=1` environment variable to force the use of cmake and install the pip package for the Metal support ([source](https://github.com/abetlen/llama-cpp-python/blob/main/docs/install/macos.md)).

Example installation with Metal Support:

    CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install llama-cpp-python

**IMPORTANT**: If you have already installed a cpu only version of the package, you need to reinstall it from scratch: consider the following command:

    CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install --upgrade --force-reinstall llama-cpp-python --no-cache-dir

### Installation with Windows[](#installation-with-windows "Direct link to Installation with Windows")

It is stable to install the `llama-cpp-python` library by compiling from the source. You can follow most of the instructions in the repository itself but there are some windows specific instructions which might be useful.

Requirements to install the `llama-cpp-python`,

*   git
*   python
*   cmake
*   Visual Studio Community (make sure you install this with the following settings)
    *   Desktop development with C++
    *   Python development
    *   Linux embedded development with C++

1.  Clone git repository recursively to get `llama.cpp` submodule as well

    git clone --recursive -j8 https://github.com/abetlen/llama-cpp-python.git

2.  Open up command Prompt (or anaconda prompt if you have it installed), set up environment variables to install. Follow this if you do not have a GPU, you must set both of the following variables.

    set FORCE_CMAKE=1set CMAKE_ARGS=-DLLAMA_CUBLAS=OFF

You can ignore the second environment variable if you have an NVIDIA GPU.

#### Compiling and installing[](#compiling-and-installing "Direct link to Compiling and installing")

In the same command prompt (anaconda prompt) you set the variables, you can cd into `llama-cpp-python` directory and run the following commands.

    python setup.py cleanpython setup.py install

Usage[](#usage "Direct link to Usage")
---------------------------------------

Make sure you are following all instructions to [install all necessary model files](https://github.com/ggerganov/llama.cpp).

You don't need an `API_TOKEN`!

    from langchain.llms import LlamaCppfrom langchain import PromptTemplate, LLMChainfrom langchain.callbacks.manager import CallbackManagerfrom langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

**Consider using a template that suits your model! Check the models page on HuggingFace etc. to get a correct prompting template.**

    template = """Question: {question}Answer: Let's work this out in a step by step way to be sure we have the right answer."""prompt = PromptTemplate(template=template, input_variables=["question"])

    # Callbacks support token-wise streamingcallback_manager = CallbackManager([StreamingStdOutCallbackHandler()])# Verbose is required to pass to the callback manager

### CPU[](#cpu "Direct link to CPU")

`Llama-v2`

    # Make sure the model path is correct for your system!llm = LlamaCpp(    model_path="/Users/rlm/Desktop/Code/llama/llama-2-7b-ggml/llama-2-7b-chat.ggmlv3.q4_0.bin",    input={"temperature": 0.75, "max_length": 2000, "top_p": 1},    callback_manager=callback_manager,    verbose=True,)

    prompt = """Question: A rap battle between Stephen Colbert and John Oliver"""llm(prompt)

            Stephen Colbert:    Yo, John, I heard you've been talkin' smack about me on your show.    Let me tell you somethin', pal, I'm the king of late-night TV    My satire is sharp as a razor, it cuts deeper than a knife    While you're just a british bloke tryin' to be funny with your accent and your wit.    John Oliver:    Oh Stephen, don't be ridiculous, you may have the ratings but I got the real talk.    My show is the one that people actually watch and listen to, not just for the laughs but for the facts.    While you're busy talkin' trash, I'm out here bringing the truth to light.    Stephen Colbert:    Truth? Ha! You think your show is about truth? Please, it's all just a joke to you.    You're just a fancy-pants british guy tryin' to be funny with your news and your jokes.    While I'm the one who's really makin' a difference, with my sat        llama_print_timings:        load time =   358.60 ms    llama_print_timings:      sample time =   172.55 ms /   256 runs   (    0.67 ms per token,  1483.59 tokens per second)    llama_print_timings: prompt eval time =   613.36 ms /    16 tokens (   38.33 ms per token,    26.09 tokens per second)    llama_print_timings:        eval time = 10151.17 ms /   255 runs   (   39.81 ms per token,    25.12 tokens per second)    llama_print_timings:       total time = 11332.41 ms    "\nStephen Colbert:\nYo, John, I heard you've been talkin' smack about me on your show.\nLet me tell you somethin', pal, I'm the king of late-night TV\nMy satire is sharp as a razor, it cuts deeper than a knife\nWhile you're just a british bloke tryin' to be funny with your accent and your wit.\nJohn Oliver:\nOh Stephen, don't be ridiculous, you may have the ratings but I got the real talk.\nMy show is the one that people actually watch and listen to, not just for the laughs but for the facts.\nWhile you're busy talkin' trash, I'm out here bringing the truth to light.\nStephen Colbert:\nTruth? Ha! You think your show is about truth? Please, it's all just a joke to you.\nYou're just a fancy-pants british guy tryin' to be funny with your news and your jokes.\nWhile I'm the one who's really makin' a difference, with my sat"

`Llama-v1`

    # Make sure the model path is correct for your system!llm = LlamaCpp(    model_path="./ggml-model-q4_0.bin", callback_manager=callback_manager, verbose=True)

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"llm_chain.run(question)

                1. First, find out when Justin Bieber was born.    2. We know that Justin Bieber was born on March 1, 1994.    3. Next, we need to look up when the Super Bowl was played in that year.    4. The Super Bowl was played on January 28, 1995.    5. Finally, we can use this information to answer the question. The NFL team that won the Super Bowl in the year Justin Bieber was born is the San Francisco 49ers.        llama_print_timings:        load time =   434.15 ms    llama_print_timings:      sample time =    41.81 ms /   121 runs   (    0.35 ms per token)    llama_print_timings: prompt eval time =  2523.78 ms /    48 tokens (   52.58 ms per token)    llama_print_timings:        eval time = 23971.57 ms /   121 runs   (  198.11 ms per token)    llama_print_timings:       total time = 28945.95 ms    '\n\n1. First, find out when Justin Bieber was born.\n2. We know that Justin Bieber was born on March 1, 1994.\n3. Next, we need to look up when the Super Bowl was played in that year.\n4. The Super Bowl was played on January 28, 1995.\n5. Finally, we can use this information to answer the question. The NFL team that won the Super Bowl in the year Justin Bieber was born is the San Francisco 49ers.'

### GPU[](#gpu "Direct link to GPU")

If the installation with BLAS backend was correct, you will see an `BLAS = 1` indicator in model properties.

Two of the most important parameters for use with GPU are:

*   `n_gpu_layers` - determines how many layers of the model are offloaded to your GPU.
*   `n_batch` - how many tokens are processed in parallel.

Setting these parameters correctly will dramatically improve the evaluation speed (see [wrapper code](https://github.com/mmagnesium/langchain/blob/master/langchain/llms/llamacpp.py) for more details).

    n_gpu_layers = 40  # Change this value based on your model and your GPU VRAM pool.n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.# Make sure the model path is correct for your system!llm = LlamaCpp(    model_path="./ggml-model-q4_0.bin",    n_gpu_layers=n_gpu_layers,    n_batch=n_batch,    callback_manager=callback_manager,    verbose=True,)

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"llm_chain.run(question)

         We are looking for an NFL team that won the Super Bowl when Justin Bieber (born March 1, 1994) was born.         First, let's look up which year is closest to when Justin Bieber was born:        * The year before he was born: 1993    * The year of his birth: 1994    * The year after he was born: 1995        We want to know what NFL team won the Super Bowl in the year that is closest to when Justin Bieber was born. Therefore, we should look up the NFL team that won the Super Bowl in either 1993 or 1994.        Now let's find out which NFL team did win the Super Bowl in either of those years:        * In 1993, the San Francisco 49ers won the Super Bowl against the Dallas Cowboys by a score of 20-16.    * In 1994, the San Francisco 49ers won the Super Bowl again, this time against the San Diego Chargers by a score of 49-26.        llama_print_timings:        load time =   238.10 ms    llama_print_timings:      sample time =    84.23 ms /   256 runs   (    0.33 ms per token)    llama_print_timings: prompt eval time =   238.04 ms /    49 tokens (    4.86 ms per token)    llama_print_timings:        eval time = 10391.96 ms /   255 runs   (   40.75 ms per token)    llama_print_timings:       total time = 15664.80 ms    " We are looking for an NFL team that won the Super Bowl when Justin Bieber (born March 1, 1994) was born. \n\nFirst, let's look up which year is closest to when Justin Bieber was born:\n\n* The year before he was born: 1993\n* The year of his birth: 1994\n* The year after he was born: 1995\n\nWe want to know what NFL team won the Super Bowl in the year that is closest to when Justin Bieber was born. Therefore, we should look up the NFL team that won the Super Bowl in either 1993 or 1994.\n\nNow let's find out which NFL team did win the Super Bowl in either of those years:\n\n* In 1993, the San Francisco 49ers won the Super Bowl against the Dallas Cowboys by a score of 20-16.\n* In 1994, the San Francisco 49ers won the Super Bowl again, this time against the San Diego Chargers by a score of 49-26.\n"

### Metal[](#metal "Direct link to Metal")

If the installation with Metal was correct, you will see an `NEON = 1` indicator in model properties.

Two of the most important parameters for use with GPU are:

*   `n_gpu_layers` - determines how many layers of the model are offloaded to your Metal GPU, in the most case, set it to `1` is enough for Metal
*   `n_batch` - how many tokens are processed in parallel, default is 8, set to bigger number.
*   `f16_kv` - for some reason, Metal only support `True`, otherwise you will get error such as `Asserting on type 0 GGML_ASSERT: .../ggml-metal.m:706: false && "not implemented"`

Setting these parameters correctly will dramatically improve the evaluation speed (see [wrapper code](https://github.com/mmagnesium/langchain/blob/master/langchain/llms/llamacpp.py) for more details).

    n_gpu_layers = 1  # Metal set to 1 is enough.n_batch = 512  # Should be between 1 and n_ctx, consider the amount of RAM of your Apple Silicon Chip.# Make sure the model path is correct for your system!llm = LlamaCpp(    model_path="./ggml-model-q4_0.bin",    n_gpu_layers=n_gpu_layers,    n_batch=n_batch,    f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls    callback_manager=callback_manager,    verbose=True,)

The rest are almost same as GPU, the console log will show the following log to indicate the Metal was enable properly.

    ggml_metal_init: allocatingggml_metal_init: using MPS...

You also could check the `Activity Monitor` by watching the % GPU of the process, the % CPU will drop dramatically after turn on `n_gpu_layers=1`. Also for the first time call LLM, the performance might be slow due to the model compilation in Metal GPU.