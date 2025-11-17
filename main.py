import grid
import agent
import gui



def main():
    #print("Input the desired number of rows/columns (only quadratic grid possible)")

    my_gui = gui.GUI()
    my_gui.run()

    #my_grid = grid.Grid(grid_size=10) # TODO remove, Python GUI ist AIDS
    #my_grid.print_grid()

    #print()

    #my_agent = agent.Agent(my_grid)
    #my_agent.search_bfs()



if __name__ == "__main__":
    main()

