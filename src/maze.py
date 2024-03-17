from cell import Cell
import time
import random


class Maze:
    def __init__(
            self, 
            x1, y1, 
            num_rows, num_cols, 
            cell_size_x, cell_size_y, 
            win=None,
            seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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
        time.sleep(0.05)


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)


    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        # possible directions
        while True:
            remaining = {}
            if i + 1 < self._num_cols and not self._cells[i + 1][j].visited:
                remaining["right"] = i + 1, j
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                remaining["left"] = i - 1, j
            if j + 1 < self._num_rows and not self._cells[i][j + 1].visited:
                remaining["down"] = i, j + 1
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                remaining["up"] = i, j - 1
            if len(remaining.keys()) == 0:
                self._draw_cell(i, j)
                return
            next_cell = list(remaining.keys())
            next_cell = random.choice(next_cell)
            if next_cell == "right":
                current_cell.has_right_wall = False
                self._cells[remaining[next_cell][0]][remaining[next_cell][1]].has_left_wall = False
            if next_cell == "down":
                current_cell.has_bottom_wall = False
                self._cells[remaining[next_cell][0]][remaining[next_cell][1]].has_top_wall = False
            if next_cell == "left":
                current_cell.has_left_wall = False
                self._cells[remaining[next_cell][0]][remaining[next_cell][1]].has_right_wall = False
            if next_cell == "up":
                current_cell.has_top_wall = False
                self._cells[remaining[next_cell][0]][remaining[next_cell][1]].has_bottom_wall = False
            
            self._break_walls_r(remaining[next_cell][0], remaining[next_cell][1])
            
    
    def _reset_cells_visited(self):
        for columns in self._cells:
            for row in columns:
                row.visited = False
        


