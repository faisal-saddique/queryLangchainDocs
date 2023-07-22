String Evaluators
=================

[

📄️ Evaluating Custom Criteria
------------------------------

Suppose you want to test a model's output against a custom rubric or custom set of criteria, how would you go about testing this?

](/docs/modules/evaluation/string/criteria_eval_chain)

[

📄️ Custom String Evaluator
---------------------------

You can make your own custom string evaluators by inheriting from the StringEvaluator class and implementing the evaluatestrings (and aevaluatestrings for async support) methods.

](/docs/modules/evaluation/string/custom)

[

📄️ Embedding Distance
----------------------

To measure semantic similarity (or dissimilarity) between a prediction and a reference label string, you could use a vector vector distance metric the two embedded representations using the embeddingdistance evaluator.\[1\]

](/docs/modules/evaluation/string/embedding_distance)

[

📄️ QA Correctness
------------------

When thinking about a QA system, one of the most important questions to ask is whether the final generated result is correct. The "qa" evaluator compares a question-answering model's response to a reference answer to provide this level of information. If you are able to annotate a test dataset, this evaluator will be useful.

](/docs/modules/evaluation/string/qa)

[

📄️ String Distance
-------------------

One of the simplest ways to compare an LLM or chain's string output against a reference label is by using string distance measurements such as Levenshtein or postfix distance. This can be used alongside approximate/fuzzy matching criteria for very basic unit testing.

](/docs/modules/evaluation/string/string_distance)