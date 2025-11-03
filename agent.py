from queue import Queue


class Agent:
    def __init__(self, grid):
        self._grid = grid
        self._start_point = self._find_start_point()
        self._goal_point = self._find_end_point()
        self._current_point = (0,0)
        self._queue = Queue()


    def search_bfs(self):
        self._current_point = self._start_point

        #while self._current_point != self._goal_point:
        self._check_for_next_points(self._current_point)

        return print(list(self._queue.queue))

    def _check_for_next_points(self, _current_point):
        x, y = _current_point
        next_points = [(x - 1 , y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for nx, ny in next_points:
            pass


    def _find_start_point(self):
        start_point = [(x,y) for x in range(len(self._grid)) for y in range(len(self._grid[0])) if self._grid[x][y] == "S"]
        start_point = start_point[0]
        return start_point

    def _find_end_point(self):
        end_point = [(x,y) for x in range(len(self._grid)) for y in range(len(self._grid[0])) if self._grid[x][y] == "Z"]
        end_point = end_point[0]
        return end_point