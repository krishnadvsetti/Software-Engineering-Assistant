from app.agents.base.base_agent import BaseAgent


class AgentRegistry:

    def __init__(self):
        self._agents: dict[str, BaseAgent] = {}

    def register(
        self,
        name: str,
        agent: BaseAgent,
    ):
        self._agents[name] = agent

    def get(
        self,
        name: str,
    ) -> BaseAgent:

        if name not in self._agents:
            raise ValueError(f"Agent '{name}' not registered.")

        return self._agents[name]

    def list_agents(self):
        return list(self._agents.keys())