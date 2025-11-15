from tkinter import *

class GUI:
    def __init__(self):
        self._root = Tk(screenName="Search Agent", baseName="Search Agent", className=" Search Agent Window", useTk=1)
        self._root.minsize(1280, 720)

        self._confirm_button = Button(self._root, text="Confirm", width=50, command=self._root.destroy)
        self._confirm_button.grid(row=2, column=5)


        self._entry_field_label = Label(self._root, text="Enter desired grid size (Only quadratic grid possible)")
        self._entry_field_label.grid(row=0, column=0)

        self._entry_field_for_gird_size = Entry(self._root)
        self._entry_field_for_gird_size.grid(row=0, column=5)

        self._root.mainloop()
