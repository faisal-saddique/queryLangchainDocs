Pairwise String Comparison
==========================

Often you will want to compare predictions of an LLM, Chain, or Agent for a given input. The `StringComparison` evaluators facilitate this so you can answer questions like:

*   Which LLM or prompt produces a preferred output for a given question?
*   Which examples should I include for few-shot example selection?
*   Which output is better to include for fintetuning?

The simplest and often most reliable automated way to choose a preferred prediction for a given input is to use the `pairwise_string` evaluator.

Check out the reference docs for the [PairwiseStringEvalChain](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.comparison.eval_chain.PairwiseStringEvalChain.html#langchain.evaluation.comparison.eval_chain.PairwiseStringEvalChain) for more info.

    from langchain.evaluation import load_evaluatorevaluator = load_evaluator("pairwise_string", requires_reference=True)

    evaluator.evaluate_string_pairs(    prediction="there are three dogs",    prediction_b="4",    input="how many dogs are in the park?",    reference="four",)

        {'reasoning': 'Response A provides an incorrect answer by stating there are three dogs in the park, while the reference answer indicates there are four. Response B, on the other hand, provides the correct answer, matching the reference answer. Although Response B is less detailed, it is accurate and directly answers the question. \n\nTherefore, the better response is [[B]].\n',     'value': 'B',     'score': 0}

Without References[​](#without-references "Direct link to Without References")
------------------------------------------------------------------------------

When references aren't available, you can still predict the preferred response. The results will reflect the evaluation model's preference, which is less reliable and may result in preferences that are factually incorrect.

    from langchain.evaluation import load_evaluatorevaluator = load_evaluator("pairwise_string")

    evaluator.evaluate_string_pairs(    prediction="Addition is a mathematical operation.",    prediction_b="Addition is a mathematical operation that adds two numbers to create a third number, the 'sum'.",    input="What is addition?",)

        {'reasoning': "Response A is accurate but lacks depth and detail. It simply states that addition is a mathematical operation without explaining what it does or how it works. \n\nResponse B, on the other hand, provides a more detailed explanation. It not only identifies addition as a mathematical operation, but also explains that it involves adding two numbers to create a third number, the 'sum'. This response is more helpful and informative, providing a clearer understanding of what addition is.\n\nTherefore, the better response is B.\n",     'value': 'B',     'score': 0}

Customize the LLM[​](#customize-the-llm "Direct link to Customize the LLM")
---------------------------------------------------------------------------

By default, the loader uses `gpt-4` in the evaluation chain. You can customize this when loading.

    from langchain.chat_models import ChatAnthropicllm = ChatAnthropic(temperature=0)evaluator = load_evaluator("pairwise_string", llm=llm, requires_reference=True)

    evaluator.evaluate_string_pairs(    prediction="there are three dogs",    prediction_b="4",    input="how many dogs are in the park?",    reference="four",)

        {'reasoning': 'Response A provides a specific number but is inaccurate based on the reference answer. Response B provides the correct number but lacks detail or explanation. Overall, Response B is more helpful and accurate in directly answering the question, despite lacking depth or creativity.\n\n[[B]]\n',     'value': 'B',     'score': 0}

Customize the Evaluation Prompt[​](#customize-the-evaluation-prompt "Direct link to Customize the Evaluation Prompt")
---------------------------------------------------------------------------------------------------------------------

You can use your own custom evaluation prompt to add more task-specific instructions or to instruct the evaluator to score the output.

\*Note: If you use a prompt that expects generates a result in a unique format, you may also have to pass in a custom output parser (`output_parser=your_parser()`) instead of the default `PairwiseStringResultOutputParser`

    from langchain.prompts import PromptTemplateprompt_template = PromptTemplate.from_template(    """Given the input context, which is most similar to the reference label: A or B?Reason step by step and finally, respond with either [[A]] or [[B]] on its own line.DATA----input: {input}reference: {reference}A: {prediction}B: {prediction_b}---Reasoning:""")evaluator = load_evaluator(    "pairwise_string", prompt=prompt_template, requires_reference=True)

    # The prompt was assigned to the evaluatorprint(evaluator.prompt)

        input_variables=['input', 'prediction', 'prediction_b', 'reference'] output_parser=None partial_variables={} template='Given the input context, which is most similar to the reference label: A or B?\nReason step by step and finally, respond with either [[A]] or [[B]] on its own line.\n\nDATA\n----\ninput: {input}\nreference: {reference}\nA: {prediction}\nB: {prediction_b}\n---\nReasoning:\n\n' template_format='f-string' validate_template=True

    evaluator.evaluate_string_pairs(    prediction="The dog that ate the ice cream was named fido.",    prediction_b="The dog's name is spot",    input="What is the name of the dog that ate the ice cream?",    reference="The dog's name is fido",)

        {'reasoning': "Option A is most similar to the reference label. Both the reference label and option A state that the dog's name is Fido. Option B, on the other hand, gives a different name for the dog. Therefore, option A is the most similar to the reference label. \n",     'value': 'A',     'score': 1}