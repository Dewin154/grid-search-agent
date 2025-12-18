from logic.agent.agent_abstract import Agent
import queue


class AgentDFS(Agent):
    def __init__(self, grid):
        super().__init__(grid)
        self._queue = queue.LifoQueue()

    # TODO redundancy with agent_bfs.py
    def search_dfs(self):
        self._current_point = self._start_point

        while True:
            if self._goal_test():
                break
            self._check_for_next_points(self._current_point)
            if self._queue.empty():
                self._shortest_path = None
                return
            self._current_point = self._queue.get()
            yield self._current_point

        self._shortest_path = self._reconstruct_shortest_path()
        return

    def _check_for_next_points(self, _current_point: tuple) -> None:
        x, y = _current_point
        next_points = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for nx, ny in next_points:
            if 0 <= nx < self._grid_size and 0 <= ny < self._grid_size:
                if self._grid_list[nx][ny] != self._wall and (nx, ny) not in self._visited_points:
                    self._queue.put((nx, ny))
                    self._visited_points.append((nx, ny))  # This needs to be here to avoid duplicates in queue
                    self._shortest_path.append(Agent.Node((nx, ny), _current_point))