import unittest
from maze import Maze
from cell import Cell
from line import Point

class TestMaze(unittest.TestCase):
    def test_create_cells(self):
        num_cols = 12
        num_rows = 10
        cell_size = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size, cell_size)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_cells_are_spaced_correctly(self):
        num_cols = 2
        num_rows = 2
        cell_size = 10
        m1 = Maze(5, 5, num_rows, num_cols, cell_size, cell_size)

        cell1 = m1._cells[0][0]
        self.assertEqual(cell1._x1, 5)
        self.assertEqual(cell1._y1, 5)
        self.assertEqual(cell1._x2, 15)
        self.assertEqual(cell1._y2, 15)

        cell2 = m1._cells[0][1]
        self.assertEqual(cell2._x1, 5)
        self.assertEqual(cell2._y1, 15)
        self.assertEqual(cell2._x2, 15)
        self.assertEqual(cell2._y2, 25)

        cell3 = m1._cells[1][0]
        self.assertEqual(cell3._x1, 15)
        self.assertEqual(cell3._y1, 5)
        self.assertEqual(cell3._x2, 25)
        self.assertEqual(cell3._y2, 15)

        cell4 = m1._cells[1][1]
        self.assertEqual(cell4._x1, 15)
        self.assertEqual(cell4._y1, 15)
        self.assertEqual(cell4._x2, 25)
        self.assertEqual(cell4._y2, 25)

    def test_break_entrance_and_exit(self):
        num_cols = 4
        num_rows = 4
        cell_size = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size, cell_size, seed=1) 
        m1._break_entrance_and_exit()
        entrance_cell = m1._cells[0][0]
        exit_cell = m1._cells[-1][-1]
        self.assertTrue(entrance_cell.has_top_wall is False)
        self.assertTrue(exit_cell.has_bottom_wall is False)

        m2 = Maze(0, 0, num_cols, num_rows, cell_size, cell_size, seed=11) 
        m2._break_entrance_and_exit()
        entrance_cell = m2._cells[0][0]
        exit_cell = m2._cells[-1][-1]
        self.assertTrue(entrance_cell.has_left_wall is False)
        self.assertTrue(exit_cell.has_right_wall is False)

    def test_get_cell(self):
        num_cols = 5
        num_rows = 3
        cell_size = 10
        m = Maze(0, 0, num_rows, num_cols, cell_size, cell_size)
        self.assertEqual(m._get_cell(0, 0), m._cells[0][0])
        self.assertEqual(m._get_cell(2, 4), m._cells[-1][-1])
        self.assertEqual(m._get_cell(-1, 0), None)
        self.assertEqual(m._get_cell(1, -1), None)
        self.assertEqual(m._get_cell(5, 2), None)
        self.assertEqual(m._get_cell(1, 7), None)

    def test_reset_cells_visited(self):
        num_rows = 2
        num_cols = 1
        cell_size = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size, cell_size, seed=1) 
        m1._reset_cells_visited()
        unvisited_cells = [not cell.visited for row in m1._cells for cell in row]
        self.assertTrue(all(unvisited_cells))


class TestCell(unittest.TestCase):
    def test_center_correctly_calculated(self):
        cell = Cell(0, 0, 10, 10)
        self.assertEqual(cell.center, Point(5.0,5.0))

if __name__ == "__main__":
    unittest.main()
