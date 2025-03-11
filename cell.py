from consts import BG_COLOR
from line import Point, Line

class Cell:
    def __init__(self, x1, y1, x2, y2, window = None):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall= True
        self.has_bottom_wall = True
        self.window = window

        self.center = Point(((x2 - x1) / 2) + x1, ((y2 - y1) / 2) + y1)

    def draw(self):
        visible = "white"
        hidden = BG_COLOR

        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self.window.draw_line(top_wall, visible if self.has_top_wall else hidden)

        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self.window.draw_line(right_wall, visible if self.has_right_wall else hidden)

        bottom_wall = Line(Point(self._x2, self._y2), Point(self._x1, self._y2))
        self.window.draw_line(bottom_wall, visible if self.has_bottom_wall else hidden)

        left_wall = Line(Point(self._x1, self._y2), Point(self._x1, self._y1))
        self.window.draw_line(left_wall, visible if self.has_left_wall else hidden)

    def draw_move(self, to_cell, undo=False):
        line = Line(self.center, to_cell.center)
        self.window.draw_line(line, "gray" if undo else "red")
