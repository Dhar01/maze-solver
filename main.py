from cell import Cell
from graphics import Window


def main():
    win = Window(800, 600)

    # line = Line(Point(50, 50), Point(400, 400))
    # win.draw_line(line, "black")

    # cell = Cell(win)
    # cell.has_left_wall = False
    # cell.draw(50, 50, 100, 100)
    # cell = Cell(win)
    # cell.has_right_wall = False
    # cell.draw(125, 125, 200, 200)
    # cell = Cell(win)
    # cell.has_top_wall = False
    # cell.draw(225, 225, 250, 250)
    # cell = Cell(win)
    # cell.has_bottom_wall = False
    # cell.draw(300, 300, 500, 500)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2)

    win.wait_for_close()


main()
