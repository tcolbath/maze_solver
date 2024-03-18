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
        self.visited = False


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
        width = 4
        wall_color = self._win._wall_color
        window_color = self._win._window_color

        if self.has_top_wall:   
            self._win.draw_line(tw, wall_color, width)
        else:
            self._win.draw_line(tw, window_color, width)

        if self.has_right_wall:
            self._win.draw_line(rw, wall_color, width)
        else:
            self._win.draw_line(rw, window_color, width)

        if self.has_bottom_wall:
            self._win.draw_line(bw, wall_color, width)
        else:
            self._win.draw_line(bw, window_color, width)

        if self.has_left_wall:
            self._win.draw_line(lw, wall_color, width)
        else:
            self._win.draw_line(lw, window_color, width)


    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        
        # center coords
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = self._win._line_solution_color
        if undo:
            fill_color = self._win._line_undo_color
        width = 2

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color, width)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, fill_color, width)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color, width)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color, width)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, fill_color, width)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color, width)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color, width)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color, width)