import tkinter
import agent
import grid


class GUI:
    def __init__(self):
        self._root = tkinter.Tk(screenName="Search Agent", baseName="Search Agent", className=" Search Agent Window", useTk=1)
        self._root.minsize(1280, 1000)
        self._root.resizable(False, False)

        self._my_grid = None
        self._my_grid_offset_x = self._my_grid_offset_y = 5
        self._my_grid_rectangle_length = 0

        self._my_canvas_width = 980
        self._my_canvas_height = 980
        self._my_canvas = tkinter.Canvas(self._root, width=self._my_canvas_width, height=self._my_canvas_height, bg="white")
        self._my_canvas.place(x=285, y=8)

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
        self._is_shortest_path_drawn = False


    def run(self):
        self._root.mainloop()

    def _save_input(self):
        self._grid_size_input = self._entry_field_for_gird_size.get()
        self._grid_size_input = self._validate_input(self._grid_size_input)
        self._my_grid_rectangle_length = self._calculate_rectangle_length(self._grid_size_input, self._my_grid_offset_x)
        self._entry_field_for_gird_size.delete(0, "end")

        if self._my_grid is None:
            if self._grid_size_input == "":
                self._display_text.config(text="Please enter a grid size.")
            else:
                self._my_grid = grid.Grid(self._grid_size_input)
                self._grid_size_input = self._my_grid.get_grid_size()
                self._display_text.config(text=f"Registered grid size: {self._grid_size_input} x {self._grid_size_input}")
                self._draw_grid(self._grid_size_input)
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
            self._is_shortest_path_drawn = False

    def _start_search(self):
        if self._my_grid is None:
            self._display_text.config(text=f"Error: Grid is not initialized!")
        else:
            my_agent = agent.Agent(self._my_grid)
            my_agent.search_bfs()
            shortest_path = my_agent.get_shortest_path()
            if shortest_path is None:
                self._display_text.config(text=f"No shortest Path exists!")
            elif not self._is_shortest_path_drawn:
                self._draw_shortest_path(shortest_path)
                self._is_shortest_path_drawn = True

    def _draw_grid(self, grid_size_input):          # TODO redundancy with _draw_shortest_path()
        x0 = self._my_grid_offset_x
        y0 = self._my_grid_offset_y
        x1 = x0 + self._my_grid_rectangle_length
        y1 = y0 + self._my_grid_rectangle_length

        for column in range(grid_size_input):
            offset_y = column * self._my_grid_rectangle_length
            for row in range(grid_size_input):
                offset_x = row * self._my_grid_rectangle_length

                top_left_x = x0 + offset_x
                top_left_y = y0 + offset_y
                down_right_x = x1 + offset_x
                down_right_y = y1 + offset_y

                if self._my_grid.get_grid()[column][row] == 1:
                    self._draw_rectangle(top_left_x, top_left_y, down_right_x, down_right_y, "black")
                elif self._my_grid.get_grid()[column][row] == grid.Grid.START_POINT:
                    self._draw_rectangle(top_left_x, top_left_y, down_right_x, down_right_y, "green")
                elif self._my_grid.get_grid()[column][row] == grid.Grid.GOAL_POINT:
                    self._draw_rectangle(top_left_x, top_left_y, down_right_x, down_right_y, "blue")
                else:
                   self._draw_rectangle(top_left_x, top_left_y, down_right_x, down_right_y)


    def _draw_rectangle(self, top_left_corner_x, top_left_corner_y, down_right_corner_x, down_right_corner_y, color: str=None) -> None:
        self._my_canvas.create_rectangle(top_left_corner_x, top_left_corner_y, down_right_corner_x, down_right_corner_y, fill=color)
        return

    def _calculate_rectangle_length(self, grid_size_input: int, offset) -> float:
        return round((self._my_canvas_height-offset) / grid_size_input, 1)

    def _draw_shortest_path(self, shortest_path):               #TODO maybe refactor? shorter?
        x0 = self._my_grid_offset_x
        y0 = self._my_grid_offset_y
        x1 = x0 + self._my_grid_rectangle_length
        y1 = y0 + self._my_grid_rectangle_length

        for cords in shortest_path:
            column, row = cords
            offset_x = (row*self._my_grid_rectangle_length)
            offset_y = (column*self._my_grid_rectangle_length)

            top_left_x = x0 + offset_x
            top_left_y = y0 + offset_y
            down_right_x = x1 + offset_x
            down_right_y = y1 + offset_y

            self._draw_rectangle(top_left_x, top_left_y, down_right_x, down_right_y, "red")
        return

    @staticmethod
    def _validate_input(grid_size: str) -> int:
        default_value = 10
        try:
            temp = int(grid_size)
        except ValueError:
            temp = default_value
        return temp if grid.Grid.MINIMAL_GRID_SIZE < temp <= grid.Grid.MAXIMAL_GRID_SIZE else default_value