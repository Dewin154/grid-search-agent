import agent

agent = agent.Agent()


def create_walls():
    pass



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

for row in range(rows):
    print(grid[row])

create_walls()

