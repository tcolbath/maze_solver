from graphics import Window, Line, Point


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window


    def draw(self, x1, y1, x2, y2):
        if self._win == None:
            return
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        # wall postions
        tw = Line(Point(x1, y1), Point(x2, y1))
        rw = Line(Point(x2, y1), Point(x2, y2))
        bw = Line(Point(x1, y2), Point(x2, y2))
        lw = Line(Point(x1, y1), Point(x1, y2))

        # draw walls
        if self.has_top_wall:   
            self._win.draw_line(tw)
        else:
            self._win.draw_line(tw, "white")

        if self.has_right_wall:
            self._win.draw_line(rw)
        else:
            self._win.draw_line(rw, "white")

        if self.has_bottom_wall:
            self._win.draw_line(bw)
        else:
            self._win.draw_line(bw, "white")

        if self.has_left_wall:
            self._win.draw_line(lw)
        else:
            self._win.draw_line(lw, "white")


    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        
        # center coords
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color)