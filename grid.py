from math import floor
import random



class Grid:
    MINIMAL_GRID_SIZE = 2
    MAXIMAL_GRID_SIZE = 60
    WALL_RATIO = 0.3
    START_POINT = "S"
    GOAL_POINT = "Z"

    def __init__(self, grid_size):
        self._grid_size = self._parse_input(grid_size)
        self._rows = self._columns = self._grid_size
        self._random_obj = random.Random()
        self._grid = []
        self._start_point_cords: tuple = (0,0)
        self._goal_point_cords: tuple = (self._rows - 1,self._columns - 1)
        self._create_grid(self._grid_size)

    def print_grid(self) -> None:
        print()
        for row in range(self._rows):
            print(self._grid[row])
        return

    def get_start_point_cords(self) -> tuple:
        return self._start_point_cords

    def get_goal_point_cords(self) -> tuple:
        return self._goal_point_cords

    def get_grid(self) -> list:
        return self._grid

    def get_grid_size(self) -> int:
        return self._grid_size

    def _create_grid(self, grid_size: int) -> None:
        rows = columns = grid_size
        self._grid = [[0] * columns for _ in range(rows)]
        self._grid[0][0] = self.START_POINT
        self._grid[rows - 1][columns - 1] = self.GOAL_POINT
        self._create_walls(grid_size)

    def _check_if_start_goal_are_blocked(self) -> None:
        start_radius = ((1,0), (0,1), (1,1))
        goal_radius = ((self._rows-1, self._columns-2), (self._rows-2, self._columns-2), (self._rows-2, self._columns-1))

        for (r, c) in (*start_radius, *goal_radius):                # *-operator unpacks both tuples into one tuple for the loop
            self._grid[r][c] = 0

    def _create_walls(self, grid_size):
        max_walls = self._calculate_wall_ratio(grid_size)
        current_walls = 0

        while current_walls <= max_walls:
            rand_x = self._random_obj.randint(0, self._columns-1)
            rand_y = self._random_obj.randint(1, self._rows-1)

            if self._grid[rand_x][rand_y] == 0:
                self._grid[rand_x][rand_y] = 1
                current_walls += 1

        self._check_if_start_goal_are_blocked()

        return

    def _parse_input(self, grid_size: str) -> int:
        default_value = 10
        try:
            temp = int(grid_size)
        except ValueError:
            temp = default_value
        return temp if self.MINIMAL_GRID_SIZE < temp < self.MAXIMAL_GRID_SIZE else default_value

    def _calculate_wall_ratio(self, grid_size: int) -> int:
        return floor((grid_size ** 2) * self.WALL_RATIO)




