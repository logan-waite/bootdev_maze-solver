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
        self.assertEqual(len(m1._cells), num_rows * num_cols)

    def test_cells_are_spaced_correctly(self):
        num_cols = 2
        num_rows = 2
        cell_size = 10
        m1 = Maze(5, 5, num_rows, num_cols, cell_size, cell_size)

        cell1 = m1._cells[0]
        self.assertEqual(cell1._x1, 5)
        self.assertEqual(cell1._y1, 5)
        self.assertEqual(cell1._x2, 15)
        self.assertEqual(cell1._y2, 15)

        cell2 = m1._cells[1]
        self.assertEqual(cell2._x1, 5)
        self.assertEqual(cell2._y1, 15)
        self.assertEqual(cell2._x2, 15)
        self.assertEqual(cell2._y2, 25)

        cell3 = m1._cells[2]
        self.assertEqual(cell3._x1, 15)
        self.assertEqual(cell3._y1, 5)
        self.assertEqual(cell3._x2, 25)
        self.assertEqual(cell3._y2, 15)

        cell4 = m1._cells[3]
        self.assertEqual(cell4._x1, 15)
        self.assertEqual(cell4._y1, 15)
        self.assertEqual(cell4._x2, 25)
        self.assertEqual(cell4._y2, 25)

    def test_break_entrance_and_exit(self):
        num_cols = 4
        num_rows = 4
        cell_size = 10
        m = Maze(0, 0, num_cols, num_rows, cell_size, cell_size) 
        m._break_entrance_and_exit()
        entrance_cell = m._cells[0]
        exit_cell = m._cells[-1]
        self.assertTrue(entrance_cell.has_left_wall is False or entrance_cell.has_top_wall is False)
        self.assertTrue(exit_cell.has_right_wall is False or exit_cell.has_bottom_wall is False)


class TestCell(unittest.TestCase):
    def test_center_correctly_calculated(self):
        cell = Cell(0, 0, 10, 10)
        self.assertEqual(cell.center, Point(5.0,5.0))

if __name__ == "__main__":
    unittest.main()
