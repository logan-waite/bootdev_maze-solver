class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=color, width=2)

    def __repr__(self):
        return f"{self.start} -> {self.end}"
