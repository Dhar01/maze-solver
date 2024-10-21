from tkinter import BOTH, Canvas, Tk

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, x1, x2) -> None:
        self.x1 = x1
        self.x2 = x2

    def draw(self, canvas: Canvas, fill_color="black") -> None:
        canvas.create_line(
            self.x1.x, self.x1.y, self.x2.x, self.x2.y, fill=fill_color, width=2
        )


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()

        # window title
        self.__root.title("Maze Solver")

        # canvas widget
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()

        print("window closed...")

    def close(self):
        self.__running = False
