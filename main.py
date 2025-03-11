from window import Window
from cell import Cell

def main():
    window = Window(800, 600)

    cell1 = Cell(window, 25, 25, 50, 50)
    cell2 = Cell(window, 50, 25, 75, 50)
    cell3 = Cell(window, 75, 25, 100, 50)
    cell4 = Cell(window, 75, 50, 100, 75)
    cell5 = Cell(window, 75, 75, 100, 100)

    cell1.has_right_wall = False
    cell2.has_left_wall = False
    cell2.has_right_wall = False
    cell3.has_left_wall = False
    cell3.has_bottom_wall = False
    cell4.has_top_wall = False
    cell4.has_bottom_wall = False
    cell5.has_top_wall = False

    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell5.draw()

    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    cell3.draw_move(cell4)
    cell4.draw_move(cell5)

    window.wait_for_close()


main()
