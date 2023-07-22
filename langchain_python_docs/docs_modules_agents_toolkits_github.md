GitHub
======

This notebook goes over how to use the GitHub tool. The GitHub tool allows agents to interact with a given GitHub repository. It implements CRUD operations for modifying files and can read/comment on Issues. The tool wraps the [PyGitHub](https://github.com/PyGithub/PyGithub) library.

In order to interact with the GitHub API you must create a [GitHub app](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps). Next, you must set the following environment variables:

    GITHUB_APP_IDGITHUB_APP_PRIVATE_KEYGITHUB_REPOSITORYGITHUB_BRANCH

    %pip install pygithub

    import osfrom langchain.agents import AgentTypefrom langchain.agents import initialize_agentfrom langchain.agents.agent_toolkits.github.toolkit import GitHubToolkitfrom langchain.llms import OpenAIfrom langchain.utilities.github import GitHubAPIWrapper

    os.environ["GITHUB_APP_ID"] = "your-github-app-id"os.environ["GITHUB_APP_PRIVATE_KEY"] = "/path/to/your/private/key"os.environ["GITHUB_REPOSITORY"] = "user/repo"os.environ["GITHUB_BRANCH"] = "branch-name"os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

    llm = OpenAI(temperature=0)github = GitHubAPIWrapper()toolkit = GitHubToolkit.from_github_api_wrapper(github)agent = initialize_agent(    toolkit.get_tools(), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    agent.run(    "You have the software engineering capabilities of a Google Principle engineer. You are tasked with completing issues on a github repository. Please look at the existing issues and complete them.")

                > Entering new AgentExecutor chain...     I need to figure out what issues need to be completed and how to complete them.    Action: Get Issues    Action Input: N/A    Observation: Found 1 issues:    [{'title': 'Change the main script to print Hello AI!', 'number': 1}]    Thought: I need to get more information about this issue.    Action: Get Issue    Action Input: 1    Observation: {'title': 'Change the main script to print Hello AI!', 'body': None, 'comments': '[]'}    Thought: I need to update the main script to print Hello AI!    Action: Update File    Action Input: main.py    OLD <<<<    print("Hello World!")    >>>> OLD    NEW <<<<    print("Hello AI!")    >>>> NEW    Observation: File content was not updated because the old content was not found. It may be helpful to use the read_file action to get the current file contents.    Thought: I need to read the current file contents.    Action: Read File    Action Input: main.py    Observation: print("Hello world!")        Thought: I need to update the main script to print Hello AI!    Action: Update File    Action Input: main.py    OLD <<<<    print("Hello world!")    >>>> OLD    NEW <<<<    print("Hello AI!")    >>>> NEW    Observation: Updated file main.py    Thought: I now know the final answer    Final Answer: The main script has been updated to print "Hello AI!"        > Finished chain.    'The main script has been updated to print "Hello AI!"'