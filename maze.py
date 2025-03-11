import time
import random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window

        self._create_cells()

    def _create_cells(self):
        self._cells = []

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells.append(
                    Cell(
                        self.x1 + (i * self.cell_size_x), 
                        self.y1 + (j * self.cell_size_y), 
                        self.x1 + ((i + 1) * self.cell_size_x), 
                        self.y1 + ((j + 1) * self.cell_size_y),
                        self.window,
                    )
                )
        
        if self.window:
            for cell in self._cells:
                cell.draw()
                self._animate()
            self._break_entrance_and_exit()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0]
        exit_cell = self._cells[-1]

        if random.randint(0, 1):
            entrance_cell.has_left_wall = False
        else:
            entrance_cell.has_top_wall = False

        if random.randint(0, 1):
            exit_cell.has_right_wall = False
        else:
            exit_cell.has_bottom_wall = False

        if self.window:
            entrance_cell.draw()
            exit_cell.draw()

