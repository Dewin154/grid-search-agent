import tkinter
import agent
import grid


class GUI:
    def __init__(self):
        self._root = tkinter.Tk(screenName="Search Agent", baseName="Search Agent", className="Search Agent Window", useTk=1)
        self._my_grid = None
        self._my_canvas = tkinter.Canvas(self._root, width=980, height=980, bg="white")

        self._root.minsize(1280, 1000)
        self._root.resizable(False, False)

        self._entry_field_label = tkinter.Label(self._root,
                                                text=f"Enter desired grid size."
                                                     f" Min. size: {grid.Grid.MINIMAL_GRID_SIZE},"
                                                     f" Max. size: {grid.Grid.MAXIMAL_GRID_SIZE}")
        self._entry_field_label.place(x=0, y=0)

        self._display_text = tkinter.Label(self._root, text="")
        self._display_text.place(relx=0.094, y = 130, anchor="center")

        self._entry_field_for_gird_size = tkinter.Entry(self._root)
        self._entry_field_for_gird_size.place(x=60, y=30)

        self._confirm_button = tkinter.Button(self._root, text="Confirm",bg="green", width=10, command=self._save_input)
        self._confirm_button.place(x=82, y=60)

        self._clear_button = tkinter.Button(self._root, text="Delete grid", width=10, bg="red", command=self._delete_grid)
        self._clear_button.place(x=82, y=90)

        self._start_search_button = tkinter.Button(self._root, text="Start Search", width=10, command=self._start_search)
        self._start_search_button.place(x =82, y=180)

        self._my_canvas.place(x=285, y=8)


    def run(self):
        self._root.mainloop()

    def _save_input(self):
        self._grid_size_input = self._entry_field_for_gird_size.get()
        self._grid_size_input = self._validate_input(self._grid_size_input)
        self._entry_field_for_gird_size.delete(0, "end")

        if self._my_grid is None:
            if self._grid_size_input == "":
                self._display_text.config(text="Please enter a grid size.")
            else:
                self._my_grid = grid.Grid(self._grid_size_input)
                self._grid_size_input = self._my_grid.get_grid_size()
                self._display_text.config(text=f"Registered grid size: {self._grid_size_input} x {self._grid_size_input}")
                self._draw_rectangle(self._grid_size_input)
        else:
            if self._grid_size_input != "":
                current_size = self._my_grid.get_grid_size()
                self._display_text.config(text=f"Error: Grid {current_size}x{current_size} exists. Delete first.")

    def _delete_grid(self):
        if self._my_grid is not None:
            self._grid_size_input = 0
            self._my_grid = None
            self._display_text.config(text="Grid deleted!")
            self._my_canvas.delete("all")

    def _start_search(self):
        if self._my_grid is None:
            self._display_text.config(text=f"Error: Grid is not initialized!")
        else:
            my_agent = agent.Agent(self._my_grid)
            my_agent.search_bfs()
            shortest_path = my_agent.get_shortest_path()
            if shortest_path is None:
                self._display_text.config(text=f"No shortest Path exists!")
            else:
                self._draw_rectangle(self._grid_size_input, shortest_path)

    def _draw_rectangle(self, grid_size_input, shortest_path=None):
        rectangle_length = round(975/grid_size_input, 1)
        x0 = 5
        y0 = 5
        x1 = x0 + rectangle_length
        y1 = y0 + rectangle_length

        for column in range(grid_size_input):
            offset_y = column*rectangle_length
            for row in range(grid_size_input):
                offset_x = row*rectangle_length

                if shortest_path is not None:
                    for cords in shortest_path:
                        if cords == (column, row):
                            self._my_canvas.create_rectangle(x0 + offset_x, y0 + offset_y, x1 + offset_x, y1 + offset_y, fill="red")
                else:
                    if self._my_grid.get_grid()[column][row] == 1:
                        self._my_canvas.create_rectangle(x0 + offset_x, y0 + offset_y, x1 + offset_x, y1 + offset_y, fill="black")
                    elif self._my_grid.get_grid()[column][row] == grid.Grid.START_POINT:
                        self._my_canvas.create_rectangle(x0 + offset_x, y0 + offset_y, x1 + offset_x, y1 + offset_y, fill="green")
                    elif self._my_grid.get_grid()[column][row] == grid.Grid.GOAL_POINT:
                        self._my_canvas.create_rectangle(x0 + offset_x, y0 + offset_y, x1 + offset_x, y1 + offset_y, fill="blue")
                    else:
                        self._my_canvas.create_rectangle(x0 + offset_x, y0 + offset_y, x1 + offset_x, y1 + offset_y)

    @staticmethod
    def _validate_input(grid_size: str) -> int:
            default_value = 10
            try:
                temp = int(grid_size)
            except ValueError:
                temp = default_value
            return temp if grid.Grid.MINIMAL_GRID_SIZE < temp <= grid.Grid.MAXIMAL_GRID_SIZE else default_value