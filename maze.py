import time
import random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window

        if seed:
            random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        self._cells = []

        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(
                    Cell(
                        x1=self.x1 + (i * self.cell_size_x), 
                        y1=self.y1 + (j * self.cell_size_y), 
                        x2=self.x1 + ((i + 1) * self.cell_size_x), 
                        y2=self.y1 + ((j + 1) * self.cell_size_y),
                        index=(i,j),
                        window=self.window,
                    )
                )
            self._cells.append(row)
        
    def build_maze(self, window=None):
        for row in self._cells:
            for cell in row:
                cell.draw()
                self._animate()
        if self.window:
            self._break_entrance_and_exit()
            self._break_walls(0, 0)
            self._reset_cells_visited()
        

    def _animate(self):
        self.window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]

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

    def _get_cell(self, i, j):
        too_low = i < 0 or j < 0
        too_high = i > self.num_rows-1 or j > self.num_cols-1
        return self._cells[i][j] if not too_low and not too_high else None

    def _get_cell_in_direction(self, dir, i, j):
        match dir:
            case "top":
                return self._get_cell(i, j-1)
            case "right":
                return self._get_cell(i+1, j)
            case "bottom":
                return self._get_cell(i, j+1)
            case "left":
                return self._get_cell(i-1, j)

    def _break_walls(self, i, j):
        current_cell = self._get_cell(i, j)
        current_cell.visited = True
        adjacent = { dir:self._get_cell_in_direction(dir, i, j) for dir in ["top", "left", "right", "bottom"]}
        to_visit = {dir:cell for (dir, cell) in adjacent.items() if cell}

        while to_visit:
            dir = random.choice(list(to_visit.keys()))
            target_cell = to_visit[dir]
            if not target_cell.visited:
                match dir:
                    case "top":
                        current_cell.has_top_wall = False
                        target_cell.has_bottom_wall = False
                        target_cell.draw()
                        self._animate()
                        self._break_walls(target_cell.row_idx, target_cell.col_idx)
                    case "right":
                        current_cell.has_right_wall = False
                        target_cell.has_left_wall = False
                        target_cell.draw()
                        self._animate()
                        self._break_walls(target_cell.row_idx, target_cell.col_idx)
                    case "bottom":
                        current_cell.has_bottom_wall = False
                        target_cell.has_top_wall = False
                        target_cell.draw()
                        self._animate()
                        self._break_walls(target_cell.row_idx, target_cell.col_idx)
                    case "left":
                        current_cell.has_left_wall = False
                        target_cell.has_right_wall = False
                        target_cell.draw()
                        self._animate()
                        self._break_walls(target_cell.row_idx, target_cell.col_idx)
            del to_visit[dir]
        current_cell.draw()

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
        current_cell = self._get_cell(i, j)
        current_cell.visited = True
        for dir in ["top", "right", "bottom", "left"]:
            wall = f"has_{dir}_wall"
            target_cell = self._get_cell_in_direction(dir, i, j)
            if target_cell and not target_cell.visited and not getattr(current_cell, wall):
                current_cell.draw_move(target_cell)
                if self._solve_r(target_cell.row_idx, target_cell.col_idx):
                    return True
                else:
                    current_cell.draw_move(target_cell, undo=True)
        return False



