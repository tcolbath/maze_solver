from graphics import Window
from maze import Maze
import sys

def main():
    sys.setrecursionlimit(10000)
    
    # colors!
    window_color = "gray"
    wall_color = "black"
    line_solution_color = "red"
    line_undo_color = "light gray"
    
    # maze style
    num_rows = 15
    num_cols = 20 
    margin = 20
    screen_width = 1200
    screen_height = 900
    cell_size_x = (screen_width - 2 * margin) / num_cols
    cell_size_y = (screen_height - 2 * margin) / num_rows
    
    # create maze
    win = Window(screen_width, screen_height, window_color)
    win.get_colors(window_color, wall_color, line_solution_color, line_undo_color)    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Maze created.")
    
    # maze solve
    solveable = maze.solve()
    if solveable:
        print("Solution Found!")
    else:
        print("Cannot be solved :(")

    win.wait_for_close()


main()