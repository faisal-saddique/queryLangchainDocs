Google Cloud Platform Vertex AI PaLM
====================================

Note: This is seperate from the Google PaLM integration. Google has chosen to offer an enterprise version of PaLM through GCP, and this supports the models made available through there.

PaLM API on Vertex AI is a Preview offering, subject to the Pre-GA Offerings Terms of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms).

Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using PaLM API on Vertex AI, you agree to the Generative AI Preview [terms and conditions](https://cloud.google.com/trustedtester/aitos) (Preview Terms).

For PaLM API on Vertex AI, you can process personal data as outlined in the Cloud Data Processing Addendum, subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms).

To use Vertex AI PaLM you must have the `google-cloud-aiplatform` Python package installed and either:

*   Have credentials configured for your environment (gcloud, workload identity, etc...)
*   Store the path to a service account JSON file as the GOOGLE\_APPLICATION\_CREDENTIALS environment variable

This codebase uses the `google.auth` library which first looks for the application credentials variable mentioned above, and then looks for system-level auth.

For more information, see:

*   [https://cloud.google.com/docs/authentication/application-default-credentials#GAC](https://cloud.google.com/docs/authentication/application-default-credentials#GAC)
*   [https://googleapis.dev/python/google-auth/latest/reference/google.auth.html#module-google.auth](https://googleapis.dev/python/google-auth/latest/reference/google.auth.html#module-google.auth)

    #!pip install google-cloud-aiplatform

    from langchain.llms import VertexAIfrom langchain import PromptTemplate, LLMChain

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = VertexAI()

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"llm_chain.run(question)

        'Justin Bieber was born on March 1, 1994. The Super Bowl in 1994 was won by the San Francisco 49ers.\nThe final answer: San Francisco 49ers.'

You can now leverage the Codey API for code generation within Vertex AI. The model names are:

*   code-bison: for code suggestion
*   code-gecko: for code completion

    llm = VertexAI(model_name="code-bison")

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "Write a python function that identifies if the number is a prime number?"llm_chain.run(question)

        '```python\ndef is_prime(n):\n  """\n  Determines if a number is prime.\n\n  Args:\n    n: The number to be tested.\n\n  Returns:\n    True if the number is prime, False otherwise.\n  """\n\n  # Check if the number is 1.\n  if n == 1:\n    return False\n\n  # Check if the number is 2.\n  if n == 2:\n    return True\n\n'