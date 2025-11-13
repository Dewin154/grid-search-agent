from queue import Queue


class Agent:
    def __init__(self, grid):
        self._grid = grid.get_grid()
        self._grid_size = len(self._grid[0])
        self._start_point = self._find_start_point()
        self._goal_point = self._find_end_point()
        self._current_point = (0, 0)
        self._queue = Queue()
        self.visited_points = [self._current_point]     # Starting point is already visited
        self._shortest_path = [Agent.Node(self._start_point)]


    class Node:
        def __init__(self, node=None, parent=None):
            self.node = node
            self.parent = parent

    def search_bfs(self):
        self._current_point = self._start_point
        print("Queue:")

        while not self._goal_test():
            self._check_for_next_points(self._current_point)
            print(list(self._queue.queue))
            self._current_point = self._queue.get()
            if self._queue.empty():
                return print("No Solution")

        self._shortest_path = self._reconstruct_shortest_path()
        return print(f"Solution found {self._shortest_path}")

    def _check_for_next_points(self, _current_point):
        x, y = _current_point
        next_points = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for nx, ny in next_points:
            if 0 <= nx < self._grid_size and 0 <= ny < self._grid_size:
                if self._grid[nx][ny] != 1 and (nx, ny) not in self.visited_points:
                    self._queue.put((nx,ny))
                    self.visited_points.append((nx, ny)) # This needs to be there to avoid duplicates in queue
                    self._shortest_path.append(Agent.Node((nx, ny), _current_point))


    def _reconstruct_shortest_path(self):
        shortest_path = []
        current_node = self._goal_point

        while self._start_point not in shortest_path:
            for node_in_list in self._shortest_path:
                if node_in_list.node == current_node:
                    shortest_path.append(current_node)
                    current_node = node_in_list.parent

        return list(reversed(shortest_path))

    def _goal_test(self):
        return any((x, y) == self._goal_point for (x, y) in self._queue.queue) # any() returns True immediately, otherwise False

    def _find_start_point(self):
        start_point = [(x, y) for x in range(len(self._grid)) for y in range(len(self._grid[0])) if self._grid[x][y] == "S"]
        start_point = start_point[0]
        return start_point

    def _find_end_point(self):
        end_point = [(x, y) for x in range(len(self._grid)) for y in range(len(self._grid[0])) if self._grid[x][y] == "Z"]
        end_point = end_point[0]
        return end_point