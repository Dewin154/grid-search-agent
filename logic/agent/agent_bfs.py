from logic.agent.agent_abstract import Agent
from queue import Queue


class AgentBFS(Agent):
    def __init__(self, grid):
        super().__init__(grid, queue=Queue())

