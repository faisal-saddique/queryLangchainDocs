Pairwise String Comparison
==========================

Often you will want to compare predictions of an LLM, Chain, or Agent for a given input. The `StringComparison` evaluators facilitate this so you can answer questions like:

*   Which LLM or prompt produces a preferred output for a given question?
*   Which examples should I include for few-shot example selection?
*   Which output is better to include for fintetuning?

The simplest and often most reliable automated way to choose a preferred prediction for a given input is to use the `pairwise_string` evaluator.

Check out the reference docs for the [PairwiseStringEvalChain](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.comparison.eval_chain.PairwiseStringEvalChain.html#langchain.evaluation.comparison.eval_chain.PairwiseStringEvalChain) for more info.

    from langchain.evaluation import load_evaluatorevaluator = load_evaluator("labeled_pairwise_string")

    evaluator.evaluate_string_pairs(    prediction="there are three dogs",    prediction_b="4",    input="how many dogs are in the park?",    reference="four",)

        {'reasoning': 'Response A is incorrect as it states there are three dogs in the park, which contradicts the reference answer of four. Response B, on the other hand, is accurate as it matches the reference answer. Although Response B is not as detailed or elaborate as Response A, it is more important that the response is accurate. \n\nFinal Decision: [[B]]\n',     'value': 'B',     'score': 0}

Without References[](#without-references "Direct link to Without References")
------------------------------------------------------------------------------

When references aren't available, you can still predict the preferred response. The results will reflect the evaluation model's preference, which is less reliable and may result in preferences that are factually incorrect.

    from langchain.evaluation import load_evaluatorevaluator = load_evaluator("pairwise_string")

    evaluator.evaluate_string_pairs(    prediction="Addition is a mathematical operation.",    prediction_b="Addition is a mathematical operation that adds two numbers to create a third number, the 'sum'.",    input="What is addition?",)

        {'reasoning': "Response A is accurate but lacks depth and detail. It simply states that addition is a mathematical operation without explaining what it does or how it works. \n\nResponse B, on the other hand, provides a more detailed explanation. It not only identifies addition as a mathematical operation, but also explains that it involves adding two numbers to create a third number, the 'sum'. This response is more helpful and informative, providing a clearer understanding of what addition is.\n\nTherefore, the better response is B.\n",     'value': 'B',     'score': 0}

Customize the LLM[](#customize-the-llm "Direct link to Customize the LLM")
---------------------------------------------------------------------------

By default, the loader uses `gpt-4` in the evaluation chain. You can customize this when loading.

    from langchain.chat_models import ChatAnthropicllm = ChatAnthropic(temperature=0)evaluator = load_evaluator("labeled_pairwise_string", llm=llm)

    evaluator.evaluate_string_pairs(    prediction="there are three dogs",    prediction_b="4",    input="how many dogs are in the park?",    reference="four",)

        {'reasoning': 'Here is my assessment:\n\nResponse B is better because it directly answers the question by stating the number "4", which matches the ground truth reference answer. Response A provides an incorrect number of dogs, stating there are three dogs when the reference says there are four. \n\nResponse B is more helpful, relevant, accurate and provides the right level of detail by simply stating the number that was asked for. Response A provides an inaccurate number, so is less helpful and accurate.\n\nIn summary, Response B better followed the instructions and answered the question correctly per the reference answer.\n\n[[B]]',     'value': 'B',     'score': 0}

Customize the Evaluation Prompt[](#customize-the-evaluation-prompt "Direct link to Customize the Evaluation Prompt")
---------------------------------------------------------------------------------------------------------------------

You can use your own custom evaluation prompt to add more task-specific instructions or to instruct the evaluator to score the output.

\*Note: If you use a prompt that expects generates a result in a unique format, you may also have to pass in a custom output parser (`output_parser=your_parser()`) instead of the default `PairwiseStringResultOutputParser`

    from langchain.prompts import PromptTemplateprompt_template = PromptTemplate.from_template(    """Given the input context, which is most similar to the reference label: A or B?Reason step by step and finally, respond with either [[A]] or [[B]] on its own line.DATA----input: {input}reference: {reference}A: {prediction}B: {prediction_b}---Reasoning:""")evaluator = load_evaluator(    "labeled_pairwise_string", prompt=prompt_template)

    # The prompt was assigned to the evaluatorprint(evaluator.prompt)

        input_variables=['input', 'prediction', 'prediction_b', 'reference'] output_parser=None partial_variables={} template='Given the input context, which is most similar to the reference label: A or B?\nReason step by step and finally, respond with either [[A]] or [[B]] on its own line.\n\nDATA\n----\ninput: {input}\nreference: {reference}\nA: {prediction}\nB: {prediction_b}\n---\nReasoning:\n\n' template_format='f-string' validate_template=True

    evaluator.evaluate_string_pairs(    prediction="The dog that ate the ice cream was named fido.",    prediction_b="The dog's name is spot",    input="What is the name of the dog that ate the ice cream?",    reference="The dog's name is fido",)

        {'reasoning': 'Option A is more similar to the reference label because it mentions the same dog\'s name, "fido". Option B mentions a different name, "spot". Therefore, A is more similar to the reference label. \n',     'value': 'A',     'score': 1}