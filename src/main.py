from graphics import Window, Line, Point
from cell import Cell
from maze import Maze


def main():

    
    win = Window(800, 600)
    maze = Maze(10,10,5,7,50,50,win)
    win.wait_for_close()



main()