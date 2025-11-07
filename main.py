import grid
import agent



def main():
    print("Input the desired number of rows/columns (only quadratic grid possible)")

    my_grid = grid.Grid(grid_size=input())
    my_grid.print_grid()

    print()

    my_agent = agent.Agent(my_grid)
    my_agent.search_bfs()



if __name__ == "__main__":
    main()

