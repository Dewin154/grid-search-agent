from ui import gui, splash



def main():

    splash.show_splash_screen()

    my_gui = gui.GUI()
    my_gui.run()


if __name__ == "__main__":
    main()

