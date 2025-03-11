from window import Window
from maze import Maze

def main():
    window = Window(800, 600)

    maze = Maze(25, 25, 7, 5, 45, 45, window)

    window.wait_for_close()


main()
