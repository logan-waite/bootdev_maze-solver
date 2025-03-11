from window import Window
from maze import Maze

def main():
    window = Window(800, 800)

    maze = Maze(25, 25, 15, 15, 50, 50, window)
    maze.build_maze()
    maze.solve()

    window.wait_for_close()


main()
