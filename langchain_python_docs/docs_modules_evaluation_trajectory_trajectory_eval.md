Agent Trajectory
================

Agents can be difficult to holistically evaluate due to the breadth of actions and generation they can make. We recommend using multiple evaluation techniques appropriate to your use case. One way to evaluate an agent is to look at the whole trajectory of actions taken along with their responses.

Evaluators that do this can implement the `AgentTrajectoryEvaluator` interface. This walkthrough will show how to use the `trajectory` evaluator to grade an OpenAI functions agent.

For more information, check out the reference docs for the [TrajectoryEvalChain](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.agents.trajectory_eval_chain.TrajectoryEvalChain.html#langchain.evaluation.agents.trajectory_eval_chain.TrajectoryEvalChain) for more info.

    from langchain.evaluation import load_evaluatorevaluator = load_evaluator("trajectory")

Capturing Trajectory[​](#capturing-trajectory "Direct link to Capturing Trajectory")
------------------------------------------------------------------------------------

The easiest way to return an agent's trajectory (without using tracing callbacks like those in LangSmith) for evaluation is to initialize the agent with `return_intermediate_steps=True`.

Below, create an example agent we will call to evaluate.

    import osfrom langchain.chat_models import ChatOpenAIfrom langchain.tools import toolfrom langchain.agents import AgentType, initialize_agentfrom pydantic import HttpUrlimport subprocessfrom urllib.parse import urlparse@tooldef ping(url: HttpUrl, return_error: bool) -> str:    """Ping the fully specified url. Must include https:// in the url."""    hostname = urlparse(str(url)).netloc    completed_process = subprocess.run(        ["ping", "-c", "1", hostname], capture_output=True, text=True    )    output = completed_process.stdout    if return_error and completed_process.returncode != 0:        return completed_process.stderr    return output@tooldef trace_route(url: HttpUrl, return_error: bool) -> str:    """Trace the route to the specified url. Must include https:// in the url."""    hostname = urlparse(str(url)).netloc    completed_process = subprocess.run(        ["traceroute", hostname], capture_output=True, text=True    )    output = completed_process.stdout    if return_error and completed_process.returncode != 0:        return completed_process.stderr    return outputllm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0)agent = initialize_agent(    llm=llm,    tools=[ping, trace_route],    agent=AgentType.OPENAI_MULTI_FUNCTIONS,    return_intermediate_steps=True,  # IMPORTANT!)result = agent("What's the latency like for https://langchain.com?")

Evaluate Trajectory[​](#evaluate-trajectory "Direct link to Evaluate Trajectory")
---------------------------------------------------------------------------------

Pass the input, trajectory, and pass to the [evaluate\_agent\_trajectory](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.schema.AgentTrajectoryEvaluator.html#langchain.evaluation.schema.AgentTrajectoryEvaluator.evaluate_agent_trajectory) method.

    evaluation_result = evaluator.evaluate_agent_trajectory(    prediction=result["output"],    input=result["input"],    agent_trajectory=result["intermediate_steps"],)evaluation_result["score"]

        Type <class 'langchain.agents.openai_functions_multi_agent.base._FunctionsAgentAction'> not serializable    1.0

Configuring the Evaluation LLM[​](#configuring-the-evaluation-llm "Direct link to Configuring the Evaluation LLM")
------------------------------------------------------------------------------------------------------------------

If you don't select an LLM to use for evaluation, the [load\_evaluator](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.loading.load_evaluator.html#langchain.evaluation.loading.load_evaluator) function will use `gpt-4` to power the evaluation chain. You can select any chat model for the agent trajectory evaluator as below.

    # %pip install anthropic# ANTHROPIC_API_KEY=<YOUR ANTHROPIC API KEY>

    from langchain.chat_models import ChatAnthropiceval_llm = ChatAnthropic(temperature=0)evaluator = load_evaluator("trajectory", llm=eval_llm)

    evaluation_result = evaluator.evaluate_agent_trajectory(    prediction=result["output"],    input=result["input"],    agent_trajectory=result["intermediate_steps"],)evaluation_result["score"]

        1.0

Providing List of Valid Tools[​](#providing-list-of-valid-tools "Direct link to Providing List of Valid Tools")
---------------------------------------------------------------------------------------------------------------

By default, the evaluator doesn't take into account the tools the agent is permitted to call. You can provide these to the evaluator via the `agent_tools` argument.

    from langchain.evaluation import load_evaluatorevaluator = load_evaluator("trajectory", agent_tools=[ping, trace_route])

    evaluation_result = evaluator.evaluate_agent_trajectory(    prediction=result["output"],    input=result["input"],    agent_trajectory=result["intermediate_steps"],)evaluation_result["score"]

        1.0