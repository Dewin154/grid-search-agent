from logic.agent.agent_abstract import Agent
import queue


class AgentDFS(Agent):
    def __init__(self, grid):
        super().__init__(grid, queue=queue.LifoQueue())



