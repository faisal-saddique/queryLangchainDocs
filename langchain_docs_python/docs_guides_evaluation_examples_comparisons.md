Comparing Chain Outputs
=======================

Suppose you have two different prompts (or LLMs). How do you know which will generate "better" results?

One automated way to predict the preferred configuration is to use a `PairwiseStringEvaluator` like the `PairwiseStringEvalChain`[\[1\]](#cite_note-1). This chain prompts an LLM to select which output is preferred, given a specific input.

For this evaluation, we will need 3 things:

1.  An evaluator
2.  A dataset of inputs
3.  2 (or more) LLMs, Chains, or Agents to compare

Then we will aggregate the restults to determine the preferred model.

### Step 1. Create the Evaluator[](#step-1-create-the-evaluator "Direct link to Step 1. Create the Evaluator")

In this example, you will use gpt-4 to select which output is preferred.

    from langchain.chat_models import ChatOpenAIfrom langchain.evaluation.comparison import PairwiseStringEvalChainllm = ChatOpenAI(model="gpt-4")eval_chain = PairwiseStringEvalChain.from_llm(llm=llm)

### Step 2. Select Dataset[](#step-2-select-dataset "Direct link to Step 2. Select Dataset")

If you already have real usage data for your LLM, you can use a representative sample. More examples provide more reliable results. We will use some example queries someone might have about how to use langchain here.

    from langchain.evaluation.loading import load_datasetdataset = load_dataset("langchain-howto-queries")

        Found cached dataset parquet (/Users/wfh/.cache/huggingface/datasets/LangChainDatasets___parquet/LangChainDatasets--langchain-howto-queries-bbb748bbee7e77aa/0.0.0/2a3b91fbd88a2c90d1dbbb32b460cf621d31bd5b05b934492fdef7d8d6f236ec)      0%|          | 0/1 [00:00<?, ?it/s]

### Step 3. Define Models to Compare[](#step-3-define-models-to-compare "Direct link to Step 3. Define Models to Compare")

We will be comparing two agents in this case.

    from langchain import SerpAPIWrapperfrom langchain.agents import initialize_agent, Toolfrom langchain.agents import AgentTypefrom langchain.chat_models import ChatOpenAI# Initialize the language model# You can add your own OpenAI API key by adding openai_api_key="<your_api_key>"llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")# Initialize the SerpAPIWrapper for search functionality# Replace <your_api_key> in openai_api_key="<your_api_key>" with your actual SerpAPI key.search = SerpAPIWrapper()# Define a list of tools offered by the agenttools = [    Tool(        name="Search",        func=search.run,        coroutine=search.arun,        description="Useful when you need to answer questions about current events. You should ask targeted questions.",    ),]

    functions_agent = initialize_agent(    tools, llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=False)conversations_agent = initialize_agent(    tools, llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=False)

### Step 4. Generate Responses[](#step-4-generate-responses "Direct link to Step 4. Generate Responses")

We will generate outputs for each of the models before evaluating them.

    from tqdm.notebook import tqdmimport asyncioresults = []agents = [functions_agent, conversations_agent]concurrency_level = 6  # How many concurrent agents to run. May need to decrease if OpenAI is rate limiting.# We will only run the first 20 examples of this dataset to speed things up# This will lead to larger confidence intervals downstream.batch = []for example in tqdm(dataset[:20]):    batch.extend([agent.acall(example["inputs"]) for agent in agents])    if len(batch) >= concurrency_level:        batch_results = await asyncio.gather(*batch, return_exceptions=True)        results.extend(list(zip(*[iter(batch_results)] * 2)))        batch = []if batch:    batch_results = await asyncio.gather(*batch, return_exceptions=True)    results.extend(list(zip(*[iter(batch_results)] * 2)))

          0%|          | 0/20 [00:00<?, ?it/s]    Retrying langchain.chat_models.openai.acompletion_with_retry.<locals>._completion_with_retry in 1.0 seconds as it raised ServiceUnavailableError: The server is overloaded or not ready yet..    Retrying langchain.chat_models.openai.acompletion_with_retry.<locals>._completion_with_retry in 1.0 seconds as it raised ServiceUnavailableError: The server is overloaded or not ready yet..

Step 5. Evaluate Pairs[](#step-5-evaluate-pairs "Direct link to Step 5. Evaluate Pairs")
-----------------------------------------------------------------------------------------

Now it's time to evaluate the results. For each agent response, run the evaluation chain to select which output is preferred (or return a tie).

Randomly select the input order to reduce the likelihood that one model will be preferred just because it is presented first.

    import randomdef predict_preferences(dataset, results) -> list:    preferences = []    for example, (res_a, res_b) in zip(dataset, results):        input_ = example["inputs"]        # Flip a coin to reduce persistent position bias        if random.random() < 0.5:            pred_a, pred_b = res_a, res_b            a, b = "a", "b"        else:            pred_a, pred_b = res_b, res_a            a, b = "b", "a"        eval_res = eval_chain.evaluate_string_pairs(            prediction=pred_a["output"] if isinstance(pred_a, dict) else str(pred_a),            prediction_b=pred_b["output"] if isinstance(pred_b, dict) else str(pred_b),            input=input_,        )        if eval_res["value"] == "A":            preferences.append(a)        elif eval_res["value"] == "B":            preferences.append(b)        else:            preferences.append(None)  # No preference    return preferences

    preferences = predict_preferences(dataset, results)

**Print out the ratio of preferences.**

    from collections import Countername_map = {    "a": "OpenAI Functions Agent",    "b": "Structured Chat Agent",}counts = Counter(preferences)pref_ratios = {k: v / len(preferences) for k, v in counts.items()}for k, v in pref_ratios.items():    print(f"{name_map.get(k)}: {v:.2%}")

        OpenAI Functions Agent: 90.00%    Structured Chat Agent: 10.00%

### Estimate Confidence Intervals[](#estimate-confidence-intervals "Direct link to Estimate Confidence Intervals")

The results seem pretty clear, but if you want to have a better sense of how confident we are, that model "A" (the OpenAI Functions Agent) is the preferred model, we can calculate confidence intervals.

Below, use the Wilson score to estimate the confidence interval.

    from math import sqrtdef wilson_score_interval(    preferences: list, which: str = "a", z: float = 1.96) -> tuple:    """Estimate the confidence interval using the Wilson score.    See: https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval    for more details, including when to use it and when it should not be used.    """    total_preferences = preferences.count("a") + preferences.count("b")    n_s = preferences.count(which)    if total_preferences == 0:        return (0, 0)    p_hat = n_s / total_preferences    denominator = 1 + (z**2) / total_preferences    adjustment = (z / denominator) * sqrt(        p_hat * (1 - p_hat) / total_preferences        + (z**2) / (4 * total_preferences * total_preferences)    )    center = (p_hat + (z**2) / (2 * total_preferences)) / denominator    lower_bound = min(max(center - adjustment, 0.0), 1.0)    upper_bound = min(max(center + adjustment, 0.0), 1.0)    return (lower_bound, upper_bound)

    for which_, name in name_map.items():    low, high = wilson_score_interval(preferences, which=which_)    print(        f'The "{name}" would be preferred between {low:.2%} and {high:.2%} percent of the time (with 95% confidence).'    )

        The "OpenAI Functions Agent" would be preferred between 69.90% and 97.21% percent of the time (with 95% confidence).    The "Structured Chat Agent" would be preferred between 2.79% and 30.10% percent of the time (with 95% confidence).

**Print out the p-value.**

    from scipy import statspreferred_model = max(pref_ratios, key=pref_ratios.get)successes = preferences.count(preferred_model)n = len(preferences) - preferences.count(None)p_value = stats.binom_test(successes, n, p=0.5, alternative="two-sided")print(    f"""The p-value is {p_value:.5f}. If the null hypothesis is true (i.e., if the selected eval chain actually has no preference between the models),then there is a {p_value:.5%} chance of observing the {name_map.get(preferred_model)} be preferred at least {successes}times out of {n} trials.""")

        The p-value is 0.00040. If the null hypothesis is true (i.e., if the selected eval chain actually has no preference between the models),    then there is a 0.04025% chance of observing the OpenAI Functions Agent be preferred at least 18    times out of 20 trials.

\_1. Note: Automated evals are still an open research topic and are best used alongside other evaluation approaches. LLM preferences exhibit biases, including banal ones like the order of outputs. In choosing preferences, "ground truth" may not be taken into account, which may lead to scores that aren't grounded in utility.\_