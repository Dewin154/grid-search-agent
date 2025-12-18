from abc import ABC, abstractmethod


class Agent(ABC):
    def __init__(self, grid) -> None:
        self._grid_obj = grid
        self._grid_list = self._grid_obj.get_grid()
        self._grid_size = len(self._grid_list[0])
        self._start_point = self._grid_obj.get_start_point_cords()
        self._goal_point = self._grid_obj.get_goal_point_cords()
        self._current_point = self._start_point
        self._wall = self._grid_obj.WALL
        self._shortest_path = [Agent.Node(self._start_point)]
        self._visited_points = [self._current_point]  # Starting point counts as already visited

    class Node:
        def __init__(self, node=None, parent=None):
            self.node = node
            self.parent = parent

        def __str__(self):
            return f"(Node: {self.node}, Parent:{self.parent})"

    def get_current_point(self):
        return self._current_point

    def get_shortest_path(self) -> list:
        return None if self._shortest_path is None else list(self._shortest_path)

    def _reconstruct_shortest_path(self) -> list:
        shortest_path = []
        current_node = self._goal_point

        while self._start_point not in shortest_path:
            for node_in_list in self._shortest_path:
                if node_in_list.node == current_node:
                    shortest_path.append(current_node)
                    current_node = node_in_list.parent

        return list(reversed(shortest_path))

    def _goal_test(self) -> bool:
        return self._current_point == self._goal_point
