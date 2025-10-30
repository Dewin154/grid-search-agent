from queue import Queue


class Agent:
    def __init__(self, grid):
        self._grid = grid
        self._start_point = [(x,y) for x in range(len(self._grid)) for y in range(len(self._grid[0])) if self._grid[x][y] == "S"]
        self._goal_point = [(x,y) for x in range(len(self._grid)) for y in range(len(self._grid[0])) if self._grid[x][y] == "Z"]
        self._queue = Queue()

        

    def search(self):
        pass