from math import floor
import random
import agent


random_obj = random.Random()

def print_grid(row):
    for row in range(rows):
        print(grid[row])
    return 0

def calculate_wall_ratio(wall_size: int):
    ratio = 0.3                            # Tinker with this to adjust the count of walls
    return floor((wall_size**2) * ratio)

def check_if_start_goal_are_blocked():

    start_radius = ((1,0), (0,1), (1,1))
    goal_radius = ((rows-1, columns-2), (rows-2, columns-2), (rows-2, columns-1))

    for (r, c) in (*start_radius, *goal_radius):                # *-operator unpacks both tuples into one tuple of the loop
        grid[r][c] = 0

def create_walls(wall_size):
    max_walls = calculate_wall_ratio(wall_size)
    current_walls = 0

    while current_walls <= max_walls:
        rand_x = random_obj.randint(0, columns-1)
        rand_y = random_obj.randint(1, rows-1)

        if grid[rand_x][rand_y] == 0:
            grid[rand_x][rand_y] = 1
            current_walls += 1

    check_if_start_goal_are_blocked()

    return "Walls created"

print("Input the desired number of rows/columns (only quadratic grid possible)")
grid_size = input()
rows = 0
columns = 0
grid = None

try:
    rows = int(grid_size)
    columns = rows
    grid = [[0] * columns for _ in range(rows)]
except ValueError:
    print("Invalid input")

print(f"Registered grid size: {rows}x{columns}")

grid[0][0] = "S"
grid[rows-1][columns-1] = "Z"

print_grid(grid)

create_walls(rows)
print()

print_grid(grid)

agent = agent.Agent(grid, rows)
print()
agent.search_bfs()      # TODO output the found route
