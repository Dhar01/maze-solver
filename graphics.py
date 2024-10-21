from tkinter import BOTH, Canvas, Tk


class Line:
    def __init__(self):
        self.x1 = x1

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
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

    def draw_line(self, line: Line, fill_color: str):
        line.draw(fill_color)

    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()

        print("window closed")

    def close(self):
        self.__running = False


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
