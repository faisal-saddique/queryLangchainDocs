Agent simulations
=================

Agent simulations involve interacting one of more agents with each other. Agent simulations generally involve two main components:

*   Long Term Memory
*   Simulation Environment

Specific implementations of agent simulations (or parts of agent simulations) include:

Simulations with One Agent[](#simulations-with-one-agent "Direct link to Simulations with One Agent")
------------------------------------------------------------------------------------------------------

*   [Simulated Environment: Gymnasium](/docs/use_cases/agent_simulations/gymnasium.html): an example of how to create a simple agent-environment interaction loop with [Gymnasium](https://gymnasium.farama.org/) (formerly [OpenAI Gym](https://github.com/openai/gym)).

Simulations with Two Agents[](#simulations-with-two-agents "Direct link to Simulations with Two Agents")
---------------------------------------------------------------------------------------------------------

*   [CAMEL](/docs/use_cases/agent_simulations/camel_role_playing.html): an implementation of the CAMEL (Communicative Agents for “Mind” Exploration of Large Scale Language Model Society) paper, where two agents communicate with each other.
*   [Two Player D&D](/docs/use_cases/agent_simulations/two_player_dnd.html): an example of how to use a generic simulator for two agents to implement a variant of the popular Dungeons & Dragons role playing game.
*   [Agent Debates with Tools](/docs/use_cases/agent_simulations/two_agent_debate_tools.html): an example of how to enable Dialogue Agents to use tools to inform their responses.

Simulations with Multiple Agents[](#simulations-with-multiple-agents "Direct link to Simulations with Multiple Agents")
------------------------------------------------------------------------------------------------------------------------

*   [Multi-Player D&D](/docs/use_cases/agent_simulations/multi_player_dnd.html): an example of how to use a generic dialogue simulator for multiple dialogue agents with a custom speaker-ordering, illustrated with a variant of the popular Dungeons & Dragons role playing game.
*   [Decentralized Speaker Selection](/docs/use_cases/agent_simulations/multiagent_bidding.html): an example of how to implement a multi-agent dialogue without a fixed schedule for who speaks when. Instead the agents decide for themselves who speaks by outputting bids to speak. This example shows how to do this in the context of a fictitious presidential debate.
*   [Authoritarian Speaker Selection](/docs/use_cases/agent_simulations/multiagent_authoritarian.html): an example of how to implement a multi-agent dialogue, where a privileged agent directs who speaks what. This example also showcases how to enable the privileged agent to determine when the conversation terminates. This example shows how to do this in the context of a fictitious news show.
*   [Simulated Environment: PettingZoo](/docs/use_cases/agent_simulations/petting_zoo.html): an example of how to create a agent-environment interaction loop for multiple agents with [PettingZoo](https://pettingzoo.farama.org/) (a multi-agent version of [Gymnasium](https://gymnasium.farama.org/)).
*   [Generative Agents](/docs/use_cases/agent_simulations/characters.html): This notebook implements a generative agent based on the paper [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) by Park, et. al.