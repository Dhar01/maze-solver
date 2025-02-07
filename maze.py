from cell import Cell
from time import sleep
from graphics import Window

class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window
    ) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

    def _create_cells(self) -> None:
        for i in range(self.__num_cols):
            col_cells = []
            for i in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j) -> None:
        pass

    def _animate(self) -> None:
        self.__win.redraw()
        sleep(0.05)
