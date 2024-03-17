from cell import Cell
import time


class Maze:
    def __init__(
            self, 
            x1, y1, 
            num_rows, num_cols, 
            cell_size_x, cell_size_y, 
            win
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()


    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            row_of_cells = []
            for j in range(self._num_rows):
                row_of_cells.append(Cell(self._win))
            self._cells.append(row_of_cells)

        for column in range(0, self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(column, row)            
                

    def _draw_cell(self, column, row):
        cell_x1 = self._x1 + (column * self._cell_size_x)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y1 = self._y1 + (row * self._cell_size_y)
        cell_y2 = cell_y1 + self._cell_size_y

        self._cells[column][row].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.02)

