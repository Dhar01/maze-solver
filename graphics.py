from tkinter import BOTH, Canvas, Tk
class Point:
    def __init__(self, x: int, y: int) -> None:
        """
        x = the x-coordinate (horizontal) in pixels of the point; left of the screen
        y = the y-coordinate (vertical) in pixels of the point; top of the screen
        """
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()

        # window title
        self.__root.title("Maze Solver")

        # canvas widget
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill="both", expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True

        while self.__running:
            self.redraw()

        print("window closed...")

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.__canvas, fill_color)